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


def to_python(value):
    """Convert NumPy values and nested containers into JSON values."""
    if hasattr(value, "tolist"):
        return to_python(value.tolist())
    if isinstance(value, dict):
        return {key: to_python(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [to_python(item) for item in value]
    return value


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


def find_page_number(page_data):
    for index, text in enumerate(page_data["rec_texts"]):
        if re.fullmatch(r"\d{1,4}", str(text).strip()):
            return index, str(text).strip()
    return None, None


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


def find_region(page, fragment):
    for region in page["raw_regions"]:
        if fragment in region["text"]:
            return dict(region)
    raise ValueError(
        f"Could not find OCR region containing {fragment!r} "
        f"on PDF page {page['pdf_page']}"
    )


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
        "text": "".join(region["text"] for region in regions),
        "regions": regions,
    }


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

    return [
        make_part("paragraph-1", "paragraph", paragraph_one),
        make_part("paragraph-2", "paragraph", paragraph_two),
    ]


def build_output(input_pdf, results):
    pages = [
        build_page(result, pdf_page)
        for pdf_page, result in enumerate(results, start=1)
    ]

    page_one, page_two = pages

    header_rows = [
        {"row": 1, **find_region(page_one, "《天地會第一冊》")},
        {"row": 2, **find_region(page_one, "為奏彰化失陷")},
        {"row": 3, **find_region(page_one, "福建水師提督黃仕簡")},
    ]

    all_zhupi_regions = [
        {
            **region,
            "context": region["text"],
        }
        for page in pages
        for region in page["raw_regions"]
        if "硃批" in region["text"]
    ]

    last_two_zhupi = all_zhupi_regions[-2:]
    for order, region in enumerate(last_two_zhupi, start=1):
        region["order"] = order
        text = region["text"]
        if "（硃批" in text and "）" in text:
            start = text.index("（硃批")
            end = text.index("）", start) + 1
            region["text"] = text[start:end]

    other_parts = [
        make_part(
            "opening-formula",
            "opening_formula",
            [find_region(page_one, "福建水師提督一等海澄公")],
        ),
        make_part(
            "footer-date",
            "footer",
            [find_region(page_two, "乾隆五十一年十二月初十日")],
        ),
        make_part(
            "footer-zhupi-note",
            "footer",
            [find_region(page_two, "乾隆五十一年十二月二十七日奉硃批")],
        ),
    ]

    return {
        "schema_version": "2.0",
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
        "preserved": {
            "three_row_header": {
                "pdf_page": 1,
                "reading_direction": "right_to_left",
                "rows": header_rows,
            },
            "page_numbers": [
                page["page_number_region"]
                for page in pages
                if page["page_number_region"] is not None
            ],
            "last_two_zhupi_lines": last_two_zhupi,
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
        "paragraphs": build_paragraphs(pages),
        "other_parts": other_parts,
        "pages": pages,
    }


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
