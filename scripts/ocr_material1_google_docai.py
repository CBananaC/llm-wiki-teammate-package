#!/usr/bin/env python3
"""
OCR Material 1 pages with Google Cloud Document AI.

This script is designed for:

    《明清臺灣檔案彙編》，第貳輯，第30冊

It renders selected Finder/PDF pages to PNG for visual checking, extracts the
same pages as single-page PDFs, sends those PDFs to Google Cloud Document AI,
and writes page-separated OCR text.

Credentials are intentionally not stored in this script. It uses either:

- the current gcloud user credential via `gcloud auth print-access-token`, or
- an explicit bearer token supplied through GOOGLE_OAUTH_ACCESS_TOKEN.

Required:

- pdftoppm and pdfseparate available on PATH
- gcloud authenticated, unless GOOGLE_OAUTH_ACCESS_TOKEN is set
- a Document AI OCR processor ID
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_PROJECT_ID = "delta-entry-496910-e7"
DEFAULT_LOCATION = "us"
DEFAULT_DPI = 300


@dataclass(frozen=True)
class PageRequest:
    finder_page: int
    pdf_path: Path
    preview_image_path: Path


def parse_pages(spec: str) -> list[int]:
    pages: list[int] = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start_s, end_s = part.split("-", 1)
            start, end = int(start_s), int(end_s)
            if end < start:
                raise ValueError(f"Invalid page range: {part}")
            pages.extend(range(start, end + 1))
        else:
            pages.append(int(part))
    if not pages:
        raise ValueError("No pages requested")
    return pages


def run_command(args: list[str]) -> str:
    completed = subprocess.run(
        args,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout


def prepare_pages(pdf: Path, pages: list[int], work_dir: Path, dpi: int) -> list[PageRequest]:
    work_dir.mkdir(parents=True, exist_ok=True)
    first = min(pages)
    last = max(pages)
    png_prefix = work_dir / "page"
    run_command(
        [
            "pdftoppm",
            "-f",
            str(first),
            "-l",
            str(last),
            "-png",
            "-r",
            str(dpi),
            str(pdf),
            str(png_prefix),
        ]
    )
    pdf_pattern = work_dir / "page-%03d.pdf"
    run_command(
        [
            "pdfseparate",
            "-f",
            str(first),
            "-l",
            str(last),
            str(pdf),
            str(pdf_pattern),
        ]
    )
    requests: list[PageRequest] = []
    for page in pages:
        preview_image_path = work_dir / f"page-{page:03d}.png"
        page_pdf_path = work_dir / f"page-{page:03d}.pdf"
        if not preview_image_path.exists():
            raise FileNotFoundError(f"Expected rendered image not found: {preview_image_path}")
        if not page_pdf_path.exists():
            raise FileNotFoundError(f"Expected extracted PDF page not found: {page_pdf_path}")
        requests.append(
            PageRequest(
                finder_page=page,
                pdf_path=page_pdf_path,
                preview_image_path=preview_image_path,
            )
        )
    return requests


def get_access_token() -> str:
    token = os.environ.get("GOOGLE_OAUTH_ACCESS_TOKEN", "").strip()
    if token:
        return token
    return run_command(["gcloud", "auth", "print-access-token"]).strip()


def docai_process_document(
    *,
    input_path: Path,
    mime_type: str,
    project_id: str,
    location: str,
    processor_id: str,
    access_token: str,
) -> dict[str, Any]:
    input_bytes = input_path.read_bytes()
    payload = {
        "rawDocument": {
            "content": base64.b64encode(input_bytes).decode("ascii"),
            "mimeType": mime_type,
        }
    }
    url = (
        f"https://documentai.googleapis.com/v1/projects/{project_id}"
        f"/locations/{location}/processors/{processor_id}:process"
    )
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Document AI HTTP {exc.code}: {detail}") from exc


def text_from_anchor(full_text: str, layout: dict[str, Any]) -> str:
    anchor = layout.get("textAnchor", {})
    segments = anchor.get("textSegments", [])
    parts: list[str] = []
    for segment in segments:
        start = int(segment.get("startIndex", 0))
        end = int(segment.get("endIndex", 0))
        parts.append(full_text[start:end])
    return "".join(parts)


def poly_bounds(layout: dict[str, Any]) -> tuple[float, float, float, float]:
    vertices = (
        layout.get("boundingPoly", {}).get("normalizedVertices")
        or layout.get("boundingPoly", {}).get("vertices")
        or []
    )
    xs = [float(v.get("x", 0)) for v in vertices]
    ys = [float(v.get("y", 0)) for v in vertices]
    if not xs or not ys:
        return (0.0, 0.0, 0.0, 0.0)
    return (min(xs), min(ys), max(xs), max(ys))


def normalize_ocr_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def reconstruct_vertical_page(document: dict[str, Any]) -> str:
    """Reconstruct page text for vertical Traditional Chinese pages.

    Document AI text order is often usable, but vertical book pages can be
    mixed. This function sorts paragraphs/blocks from right to left, then
    top to bottom, which matches the page layout of Material 1.
    """
    doc = document.get("document", document)

    # Some Document AI processors, including Content Layout Parser style
    # processors, return recognized text under documentLayout.blocks rather
    # than the older document.text + pages[].paragraphs schema.
    layout_blocks = doc.get("documentLayout", {}).get("blocks", [])
    if layout_blocks:
        values: list[str] = []
        for block in layout_blocks:
            text = block.get("textBlock", {}).get("text", "")
            text = normalize_ocr_text(text)
            if text:
                values.append(text)
        return "\n\n".join(values).strip()

    full_text = doc.get("text", "")
    pages = doc.get("pages", [])
    if not pages:
        return normalize_ocr_text(full_text)

    units: list[tuple[float, float, float, str]] = []
    for page in pages:
        paragraphs = page.get("paragraphs") or []
        blocks = page.get("blocks") or []
        candidates = paragraphs if paragraphs else blocks
        for item in candidates:
            layout = item.get("layout", {})
            value = normalize_ocr_text(text_from_anchor(full_text, layout))
            if not value:
                continue
            min_x, min_y, max_x, _max_y = poly_bounds(layout)
            center_x = (min_x + max_x) / 2
            units.append((center_x, min_y, max_x - min_x, value))

    if not units:
        return normalize_ocr_text(full_text)

    # Vertical Traditional Chinese is read right-to-left by column, and
    # top-to-bottom inside each column. Sorting by -x then y approximates that.
    units.sort(key=lambda item: (-item[0], item[1]))
    lines: list[str] = []
    for _center_x, _min_y, _width, value in units:
        lines.append(value)
    return "\n".join(lines).strip()


def write_outputs(
    *,
    page: int,
    response: dict[str, Any],
    out_dir: Path,
) -> tuple[Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / f"user-source-1-finder-page-{page:03d}.docai.json"
    txt_path = out_dir / f"user-source-1-finder-page-{page:03d}.ocr.txt"
    json_path.write_text(json.dumps(response, ensure_ascii=False, indent=2), encoding="utf-8")
    text = reconstruct_vertical_page(response)
    txt_path.write_text(text + "\n", encoding="utf-8")
    return json_path, txt_path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="OCR Material 1 pages with Google Cloud Document AI."
    )
    parser.add_argument(
        "--pdf",
        default="/Users/creamybanana/Downloads/Source /明清台灣檔案匯編 30.pdf",
        help="Path to Material 1 PDF.",
    )
    parser.add_argument(
        "--pages",
        required=True,
        help="Finder/PDF page numbers, e.g. 43-47 or 43,45,47.",
    )
    parser.add_argument(
        "--project-id",
        default=os.environ.get("GOOGLE_CLOUD_PROJECT", DEFAULT_PROJECT_ID),
        help="Google Cloud project ID.",
    )
    parser.add_argument(
        "--location",
        default=os.environ.get("DOCAI_LOCATION", DEFAULT_LOCATION),
        help="Document AI processor location, e.g. us or eu.",
    )
    parser.add_argument(
        "--processor-id",
        default=os.environ.get("DOCAI_PROCESSOR_ID", ""),
        help="Document AI OCR processor ID. Can also be set as DOCAI_PROCESSOR_ID.",
    )
    parser.add_argument(
        "--image-dir",
        default="tmp/pdfs/material-1-google-ocr-images",
        help="Directory for rendered PNG previews and single-page PDFs.",
    )
    parser.add_argument(
        "--out-dir",
        default="llm-wiki/ocr/user-source-1",
        help="Directory for OCR text and raw JSON outputs.",
    )
    parser.add_argument("--dpi", type=int, default=DEFAULT_DPI)
    parser.add_argument(
        "--docai-mime-type",
        default="application/pdf",
        help="MIME type sent to Document AI. Default is application/pdf because some processors reject image/png.",
    )
    parser.add_argument(
        "--render-only",
        action="store_true",
        help="Only render selected pages; do not call Google Cloud.",
    )
    args = parser.parse_args()

    pdf = Path(args.pdf).expanduser()
    if not pdf.exists():
        raise FileNotFoundError(pdf)

    pages = parse_pages(args.pages)
    page_requests = prepare_pages(pdf, pages, Path(args.image_dir), args.dpi)
    print("Prepared page files:")
    for request in page_requests:
        print(f"- Finder page {request.finder_page}:")
        print(f"  PDF for Document AI: {request.pdf_path}")
        print(f"  PNG preview:         {request.preview_image_path}")

    if args.render_only:
        return 0

    if not args.processor_id:
        raise SystemExit(
            "Missing Document AI processor ID. Pass --processor-id or set DOCAI_PROCESSOR_ID."
        )

    access_token = get_access_token()
    out_dir = Path(args.out_dir)
    for request in page_requests:
        print(f"OCR Finder page {request.finder_page} with Google Document AI...")
        response = docai_process_document(
            input_path=request.pdf_path,
            mime_type=args.docai_mime_type,
            project_id=args.project_id,
            location=args.location,
            processor_id=args.processor_id,
            access_token=access_token,
        )
        json_path, txt_path = write_outputs(
            page=request.finder_page,
            response=response,
            out_dir=out_dir,
        )
        print(f"- JSON: {json_path}")
        print(f"- TXT:  {txt_path}")

    combined_path = out_dir / f"user-source-1-finder-pages-{min(pages):03d}-{max(pages):03d}.ocr.txt"
    combined_parts: list[str] = []
    for page in pages:
        txt_path = out_dir / f"user-source-1-finder-page-{page:03d}.ocr.txt"
        combined_parts.append(f"## Finder page {page}\n\n{txt_path.read_text(encoding='utf-8').strip()}")
    combined_path.write_text("\n\n".join(combined_parts) + "\n", encoding="utf-8")
    print(f"Combined TXT: {combined_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
