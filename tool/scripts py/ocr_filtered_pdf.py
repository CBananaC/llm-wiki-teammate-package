#!/usr/bin/env python3
"""OCR archival PDF pages while excluding red ink and scan watermarks."""

import argparse
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image
from paddleocr import PaddleOCR


DEFAULT_INPUT = Path(
    "/Users/creamybanana/Downloads/DH Project/intro Website/"
    "Website/Visual Material/3.4/npmpdf-2.pdf"
)
DEFAULT_OUTPUT = Path(
    "/Users/creamybanana/Downloads/DH Project/intro Website/"
    "Website/Visual Material/3.4/npmpdf-2.ocr.json"
)


# Convert PaddleOCR and NumPy values into ordinary Python values.
def to_python(value):
    if hasattr(value, "tolist"):
        return to_python(value.tolist())
    if isinstance(value, dict):
        return {key: to_python(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [to_python(item) for item in value]
    return value


# Render the PDF so each OCR region can be checked against its source colors.
def render_pdf(input_pdf, render_dir, dpi):
    pdftoppm = shutil.which("pdftoppm")
    if pdftoppm is None:
        raise RuntimeError("pdftoppm is required to render the PDF")

    prefix = render_dir / "page"
    subprocess.run(
        [pdftoppm, "-png", "-r", str(dpi), str(input_pdf), str(prefix)],
        check=True,
    )
    return sorted(render_dir.glob("page-*.png"))


# Measure red pixels inside an OCR box to identify handwritten red ink.
def red_pixel_ratio(image_array, box):
    x1, y1, x2, y2 = [int(value) for value in box]
    crop = image_array[
        max(0, y1): min(image_array.shape[0], y2 + 1),
        max(0, x1): min(image_array.shape[1], x2 + 1),
    ]
    if crop.size == 0:
        return 0.0

    red, green, blue = [crop[..., index].astype(int) for index in range(3)]
    red_mask = (
        (red > 100)
        & ((red - green) > 60)
        & ((red - blue) > 70)
    )
    return float(red_mask.mean())


# Identify watermark, red-ink, and scanner-calibration OCR regions to omit.
def ignored_reason(text, box, image_array):
    height = image_array.shape[0]
    normalized = re.sub(r"\s+", "", str(text)).upper()
    y_top = int(box[1])
    y_center = (int(box[1]) + int(box[3])) / 2

    if y_top >= height * 0.72:
        return "scanner_calibration_strip"
    red_ratio = red_pixel_ratio(image_array, box)
    if red_ratio >= 0.15 or (
        red_ratio >= 0.03 and len(str(text).strip()) <= 8
    ):
        return "red_handwritten_or_red_ink"
    if re.search(r"[A-Z]", normalized):
        return "watermark_or_scan_label"

    watermark_chars = set("國国立故宮宫博物院勿")
    if (
        0.25 * height < y_center < 0.75 * height
        and len(normalized) <= 3
        and normalized
        and all(character in watermark_chars for character in normalized)
    ):
        return "watermark_or_scan_label"

    return None


# Split a page's reading-order text into plain sentence strings.
def split_sentences(text):
    sentences = []
    start = 0
    for index, character in enumerate(text):
        if character in "。！？":
            sentences.append(text[start:index + 1])
            start = index + 1
    if start < len(text):
        sentences.append(text[start:])
    return [sentence for sentence in sentences if sentence]


# OCR one page from right to left and from the top of each column downward.
def ocr_page(ocr, image_path, pdf_page):
    image_array = np.asarray(Image.open(image_path).convert("RGB"))
    page_results = []
    ignored_counts = {}

    for result in ocr.predict(str(image_path)):
        payload = result.json
        if callable(payload):
            payload = payload()
        payload = to_python(payload)
        if isinstance(payload, dict) and isinstance(payload.get("res"), dict):
            payload = payload["res"]

        entries = []
        for box, text in zip(payload["rec_boxes"], payload["rec_texts"]):
            reason = ignored_reason(text, box, image_array)
            if reason is not None:
                ignored_counts[reason] = ignored_counts.get(reason, 0) + 1
                continue
            entries.append((box, str(text)))

        entries.sort(
            key=lambda item: (
                -int(item[0][0]),
                int(item[0][1]),
            )
        )
        text = "".join(item[1] for item in entries)
        page_results.append(
            {
                "pdf_page": pdf_page,
                "text": text,
                "sentences": split_sentences(text),
                "ignored_region_counts": ignored_counts,
            }
        )

    return page_results[0]


# Run OCR for every rendered page and write the grouped JSON document.
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--dpi", type=int, default=200)
    args = parser.parse_args()

    ocr = PaddleOCR(
        lang="chinese_cht",
        device="cpu",
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False,
    )

    with tempfile.TemporaryDirectory(prefix="ocr-pdf-") as temporary_dir:
        render_dir = Path(temporary_dir)
        image_paths = render_pdf(args.input, render_dir, args.dpi)
        pages = [
            ocr_page(ocr, image_path, pdf_page)
            for pdf_page, image_path in enumerate(image_paths, start=1)
        ]

    ignored_counts = {}
    for page in pages:
        for reason, count in page.pop("ignored_region_counts").items():
            ignored_counts[reason] = ignored_counts.get(reason, 0) + count

    output = {
        "schema_version": "1.0",
        "source": {
            "filename": args.input.name,
            "path": str(args.input),
            "pdf_page_count": len(pages),
            "reading_order": "right_to_left_columns_top_to_bottom",
        },
        "pages": pages,
        "ignored": {
            "watermark": "國立故宮博物院 / NATIONAL PALACE MUSEUM",
            "red_handwritten_words": True,
            "scanner_calibration_strip": True,
            "filtered_region_counts": ignored_counts,
        },
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote {args.output}")
    print(f"Pages: {len(pages)}")
    print(f"Ignored: {ignored_counts}")


if __name__ == "__main__":
    main()
