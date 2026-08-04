#!/usr/bin/env python3
"""OCR a vertical Chinese PDF and preserve source paragraphs as JSON parts."""

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import paddle
import paddleocr
from paddleocr import PaddleOCR


DEFAULT_INPUT = Path(
    "/Users/creamybanana/Downloads/DH Project/intro Website/"
    "Website/Visual Material/3.4/明清台灣檔案匯編 30 (dragged).pdf"
)
DEFAULT_OUTPUT = Path(
    "/Users/creamybanana/Downloads/DH Project/intro Website/"
    "Website/Visual Material/3.4/明清台灣檔案匯編 30 (dragged).ocr.json"
)
SENTENCE_ENDINGS = set("。！？")
ZHUPI_ANNOTATION_RE = re.compile(r"（硃批.*?）")


# Convert PaddleOCR and NumPy values into JSON-compatible Python values.
def to_python(value):
    """Convert NumPy values and nested containers into JSON values."""
    if hasattr(value, "tolist"):
        return to_python(value.tolist())
    if isinstance(value, dict):
        return {key: to_python(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [to_python(item) for item in value]
    return value


# Create one raw OCR region record, including text, confidence, and geometry.
def make_region(page_data, index, pdf_page):
    boxes = page_data["rec_boxes"]
    polygons = page_data.get("rec_polys", boxes)

    return {
        "pdf_page": pdf_page,
        "region_index": index,
        "text": page_data["rec_texts"][index],
        "confidence": round(float(page_data["rec_scores"][index]), 6),
        "box": [int(value) for value in boxes[index]],
        "polygon": [
            [int(value) for value in point]
            for point in polygons[index]
        ],
    }


# Identify the printed page-number region so it can be preserved separately.
def find_page_number(page_data):
    for index, text in enumerate(page_data["rec_texts"]):
        if re.fullmatch(r"\d{1,4}", str(text).strip()):
            return index, str(text).strip()
    return None, None


# Build the complete OCR record for one PDF page and its reading order.
def build_page(result, pdf_page):
    payload = result.json
    if callable(payload):
        payload = payload()
    page_data = to_python(payload)
    if isinstance(page_data, dict) and isinstance(page_data.get("res"), dict):
        page_data = page_data["res"]

    page_number_index, page_number = find_page_number(page_data)
    raw_regions = [
        make_region(page_data, index, pdf_page)
        for index in range(len(page_data["rec_texts"]))
    ]

    reading_indices = [
        index
        for index in range(len(page_data["rec_texts"]))
        if index != page_number_index
    ]
    reading_indices.sort(
        key=lambda index: (
            -int(page_data["rec_boxes"][index][0]),
            int(page_data["rec_boxes"][index][1]),
        )
    )

    page_number_region = (
        raw_regions[page_number_index]
        if page_number_index is not None
        else None
    )

    return {
        "pdf_page": pdf_page,
        "printed_page_number": page_number,
        "page_number_region": page_number_region,
        "raw_regions": raw_regions,
        "reading_order": "right_to_left_vertical_columns",
        "reading_order_regions": [
            raw_regions[index] for index in reading_indices
        ],
        "model_settings": page_data.get("model_settings"),
        "text_detection_parameters": page_data.get("text_det_params"),
        "text_recognition_score_threshold": page_data.get(
            "text_rec_score_thresh"
        ),
    }


# Find a raw OCR region by a source-text fragment used as a stable anchor.
def find_region(page, fragment):
    for region in page["raw_regions"]:
        if fragment in region["text"]:
            return dict(region)
    raise ValueError(
        f"Could not find OCR region containing {fragment!r} "
        f"on PDF page {page['pdf_page']}"
    )


# Remove an inline 硃批 annotation from the paragraph display text.
def remove_zhupi_annotation(text):
    return ZHUPI_ANNOTATION_RE.sub("", text)


# Split an ordered paragraph into sentence objects with source references.
def build_sentences(part_id, regions):
    pieces = []
    text_parts = []
    cursor = 0

    for region in regions:
        text = remove_zhupi_annotation(region["text"])
        if not text:
            continue
        start = cursor
        text_parts.append(text)
        cursor += len(text)
        pieces.append((start, cursor, region))

    combined_text = "".join(text_parts)
    ranges = []
    sentence_start = 0
    for index, character in enumerate(combined_text):
        if character in SENTENCE_ENDINGS:
            ranges.append((sentence_start, index + 1))
            sentence_start = index + 1
    if sentence_start < len(combined_text):
        ranges.append((sentence_start, len(combined_text)))

    sentences = []
    for order, (start, end) in enumerate(ranges, start=1):
        source_region_refs = []
        for region_start, region_end, region in pieces:
            if region_start < end and region_end > start:
                source_region_refs.append(
                    {
                        "pdf_page": region["pdf_page"],
                        "region_index": region["region_index"],
                    }
                )

        sentences.append(
            {
                "sentence_id": f"{part_id}-sentence-{order}",
                "text": combined_text[start:end],
                "source_region_refs": source_region_refs,
            }
        )

    return sentences


# Package an ordered sequence of OCR regions as one JSON part.
def make_part(part_id, part_type, regions):
    if not regions:
        raise ValueError(f"Part {part_id} has no OCR regions")

    return {
        "part_id": part_id,
        "part_type": part_type,
        "pdf_pages": sorted({region["pdf_page"] for region in regions}),
        "source_region_refs": [
            {
                "pdf_page": region["pdf_page"],
                "region_index": region["region_index"],
            }
            for region in regions
        ],
        "regions": regions,
    }


# Package a nonparagraph part as one continuous source-text object.
def make_text_part(part_id, part_type, regions):
    part = make_part(part_id, part_type, regions)
    part["text"] = "".join(region["text"] for region in regions)
    return part


# Group source OCR regions into one JSON part per paragraph.
def build_paragraphs(pages):
    page_one, page_two = pages

    # The first indented paragraph begins with 竊照 on page 80 and
    # continues across the page break through 等情前來 on page 81.
    paragraph_one = [
        find_region(page_one, "竊照"),
        find_region(page_one, "戌刻"),
        find_region(page_one, "刻，縣城"),
        find_region(page_one, "敢聚眾"),
        find_region(page_one, "雖未准"),
        find_region(page_one, "揚，先帶"),
        find_region(page_one, "地文武"),
        find_region(page_one, "營員弁"),
        find_region(page_one, "愈時發"),
        find_region(page_one, "剿捕"),
        find_region(page_one, "逃內地"),
        find_region(page_one, "營縣在於"),
        find_region(page_two, "現在派撥"),
        find_region(page_two, "領官兵"),
        find_region(page_two, "董得魁"),
        find_region(page_two, "字寄淡屬"),
        find_region(page_two, "陷，卑職"),
        find_region(page_two, "第兵力"),
        find_region(page_two, "艱未知"),
    ]

    # The second indented paragraph begins with 查 on page 81.
    paragraph_two = [
        find_region(page_two, "查，奴才"),
        find_region(page_two, "易。除"),
        find_region(page_two, "北路援剿"),
        find_region(page_two, "彰化賊匪"),
    ]

    paragraph_parts = []
    for part_id, regions in (
        ("paragraph-1", paragraph_one),
        ("paragraph-2", paragraph_two),
    ):
        part = make_part(part_id, "paragraph", regions)
        part["sentences"] = build_sentences(part_id, regions)
        paragraph_parts.append(part)
    return paragraph_parts


# Build the requested three-row header with readable text and provenance.
def build_header(page_one):
    header_rows = [
        {"row": 1, **find_region(page_one, "《天地會第一冊》")},
        {"row": 2, **find_region(page_one, "為奏彰化失陷")},
        {"row": 3, **find_region(page_one, "福建水師提督黃仕簡")},
    ]
    return {
        "row_count": 3,
        "reading_direction": "right_to_left",
        "rows": header_rows,
        "opening_formula": make_text_part(
            "opening-formula",
            "opening_formula",
            [find_region(page_one, "福建水師提督一等海澄公")],
        ),
    }


# Build the selected final two 硃批 lines as a separate readable area.
def build_zhupi_area(pages):
    all_zhupi_regions = [
        region
        for page in pages
        for region in page["raw_regions"]
        if "硃批" in region["text"]
    ]
    selected_regions = all_zhupi_regions[-2:]

    lines = []
    for order, region in enumerate(selected_regions, start=1):
        source_text = region["text"]
        inline_match = ZHUPI_ANNOTATION_RE.search(source_text)
        text = (
            inline_match.group(0)
            if inline_match
            else source_text
        )
        position = "inline" if inline_match else "footer"
        lines.append(
            {
                "line_id": f"zhu-{order}",
                "order": order,
                "position": position,
                "text": text,
                "source_region_ref": {
                    "pdf_page": region["pdf_page"],
                    "region_index": region["region_index"],
                },
                "source_region_text": source_text,
                "region": region,
            }
        )

    return {
        "selection": "last_two_zhupi_regions",
        "lines": lines,
    }


# Keep the footer date separate from the header, paragraphs, and 硃批 area.
def build_footer(page_two):
    return {
        "date": make_text_part(
            "footer-date",
            "footer",
            [find_region(page_two, "乾隆五十一年十二月初十日")],
        )
    }


# Assemble pages, preserved headers/footers, paragraphs, and OCR metadata.
def build_output(input_pdf, results):
    pages = [
        build_page(result, pdf_page)
        for pdf_page, result in enumerate(results, start=1)
    ]

    page_one, page_two = pages

    return {
        "schema_version": "3.0",
        "source": {
            "path": str(input_pdf),
            "filename": input_pdf.name,
            "pdf_page_count": len(pages),
            "printed_page_numbers": [
                page["printed_page_number"] for page in pages
            ],
        },
        "ocr": {
            "provider": "PaddleOCR",
            "paddleocr_version": getattr(
                paddleocr, "__version__", "unknown"
            ),
            "paddlepaddle_version": paddle.__version__,
            "detection_model": "PP-OCRv6_medium_det",
            "recognition_model": "PP-OCRv6_medium_rec",
            "language": "chinese_cht",
            "device": "cpu",
            "use_doc_orientation_classify": False,
            "use_doc_unwarping": False,
            "use_textline_orientation": False,
            "generated_at": datetime.now(
                ZoneInfo("Asia/Hong_Kong")
            ).isoformat(timespec="seconds"),
        },
        "header": build_header(page_one),
        "page_numbers": [
            page["page_number_region"]
            for page in pages
            if page["page_number_region"] is not None
        ],
        "paragraphs": build_paragraphs(pages),
        "zhu_area": build_zhupi_area(pages),
        "footer": build_footer(page_two),
        "preserved": {
            "page_numbers": [
                page["printed_page_number"] for page in pages
            ],
            "three_row_header": True,
            "last_two_zhupi_lines": True,
            "paragraph_boundary_method": (
                "Source-layout anchors: the indented 竊照 paragraph "
                "continues across the page break; the indented 查 paragraph "
                "starts a new part on page 81."
            ),
            "evidence_status": (
                "OCR candidates retained from the source scan; no "
                "researcher correction or silent deletion was applied."
            ),
        },
        "raw_ocr_pages": pages,
    }


# Parse command-line paths, run PaddleOCR, and write the JSON output.
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    ocr = PaddleOCR(
        lang="chinese_cht",
        device="cpu",
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False,
    )

    results = list(ocr.predict(str(args.input)))
    output = build_output(args.input, results)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Wrote {args.output}")
    print(f"Paragraphs: {len(output['paragraphs'])}")
    print(
        "Paragraph page spans: "
        + ", ".join(
            str(part["pdf_pages"])
            for part in output["paragraphs"]
        )
    )


if __name__ == "__main__":
    main()
