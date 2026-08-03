#!/usr/bin/env python3
"""Build the Part 1 interface-replica demonstration data module.

The introduction website's 第一部分「平台的整體介面」shows an interactive replica of
the sample review tool. The replica must not invent any historical content, so this
script derives every quotation, date, title and AI result from existing project data:

  - review-tools/shared data/stage1_original_text.json   (canonical 硃42 record)
  - review-tools/(2) sample/sample_all.data              (current sample review state)

Output:
  intro Website/Website/storymap/part-1-interface-data.js

The generated file is a plain hand-editable JS module assigned to
window.PART1_INTERFACE_DATA. It is loaded with a normal <script src> tag so the
introduction website keeps working when opened directly from disk. After
generating it you may edit the file by hand; re-running this script overwrites it.

Usage:
    cd "/Users/creamybanana/Downloads/DH Project"
    python3 "tool/scripts py/build_part1_interface_data.py"
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STAGE1 = ROOT / "review-tools" / "shared data" / "stage1_original_text.json"
SAMPLE_STATE = ROOT / "review-tools" / "(2) sample" / "sample_all.data"
OUT = ROOT / "intro Website" / "Website" / "storymap" / "part-1-interface-data.js"

DOC_ID = "硃42"

# Event subtitles selected from the current sample state. Each one is already a
# human-confirmed dot in the sample tool, so the replica shows real review output.
DOT_EVENT = "賊匪於三坎店交戰稍退"          # 第一線 戰場事件
DOT_EMPEROR = (
    "據柴大紀於三坎店大施火砲擊退賊眾之報研判臺灣郡城防守嚴密且全臺尚無他虞"
)                                          # 第四線 皇帝行動

# AI candidate cards offered for the 「加入」 demonstration in the AI 分析區.
AI_CANDIDATES = [
    "澎湖兵渡海前往臺灣赴援",
    "黃仕簡率兵由廈門放洋",
]


def fail(message: str) -> None:
    raise SystemExit(f"build_part1_interface_data: {message}")


def load_document() -> dict:
    records = json.loads(STAGE1.read_text(encoding="utf-8"))
    for record in records:
        if record.get("doc_id") == DOC_ID:
            return record
    fail(f"{DOC_ID} not found in {STAGE1}")


def load_events() -> list:
    state = json.loads(SAMPLE_STATE.read_text(encoding="utf-8"))
    return state.get("__events", [])


def find_event(events: list, subtitle: str) -> dict:
    for event in events:
        if event.get("subtitle") == subtitle:
            return event
    fail(f"event not found in sample state: {subtitle}")


def primary_source(event: dict) -> dict:
    sources = event.get("sources") or []
    if not sources:
        fail(f"event has no sources: {event.get('subtitle')}")
    return sources[0]


def event_payload(event: dict) -> dict:
    """Reduce a sample-state event to the fields the replica panel displays."""
    source = primary_source(event)
    return {
        "id": event.get("id"),
        "actor": event.get("actor"),
        "subtitle": event.get("subtitle"),
        "description": event.get("description"),
        "where": event.get("where"),
        "who": event.get("who") or [],
        "whenCh": event.get("whenCh"),
        "dateAr": event.get("dateAr"),
        "category": event.get("category"),
        "aiFilterLabel": event.get("aiFilterLabel"),
        "quote": source.get("quote"),
        "quoteDocId": source.get("doc_id"),
    }


def check_quote(body: str, quote: str, label: str) -> None:
    """The replica highlights quotations inside the original text, so every quote
    must be a literal substring of the canonical body."""
    if quote not in body:
        fail(f"quote for {label!r} is not a literal substring of {DOC_ID} body")


def main() -> int:
    document = load_document()
    events = load_events()
    body = document["body"]

    dot_event = event_payload(find_event(events, DOT_EVENT))
    dot_emperor = event_payload(find_event(events, DOT_EMPEROR))
    candidates = [event_payload(find_event(events, name)) for name in AI_CANDIDATES]

    # 硃42 is the memorial the replica opens; its own quotations must resolve.
    for item in [dot_event, *candidates]:
        check_quote(body, item["quote"], item["subtitle"])

    # The 皇帝行動 dot quotes 諭24, not 硃42, so it is checked against its own
    # source document rather than the memorial body.
    if dot_emperor["quoteDocId"] != "諭24":
        fail("expected the 皇帝行動 dot to be sourced from 諭24")

    payload = {
        "_generated_by": "tool/scripts py/build_part1_interface_data.py",
        "_sources": [
            "review-tools/shared data/stage1_original_text.json",
            "review-tools/(2) sample/sample_all.data",
        ],
        "document": {
            "docId": document["doc_id"],
            "docType": document["doc_type"],
            "title": document["title"],
            "author": document["author"],
            "series": document["series"],
            "compiledIn": document["compiled_in"],
            "sendDate": document["send_date"],
            "receiveDate": document["receive_date"],
            "body": body,
            "rescriptText": document.get("rescript_text"),
        },
        # Lane labels exactly as they appear in review-tools/(2) sample/index.html.
        "lanes": [
            {"key": "events", "label": "戰場事件", "short": "事件"},
            {"key": "official", "label": "官員上奏", "short": "上奏"},
            {"key": "imperial", "label": "皇帝硃批下旨", "short": "硃批下旨"},
            {"key": "emperor", "label": "皇帝行動", "short": "皇帝行動"},
        ],
        "dots": {
            "events": dot_event,
            "official": {
                "docId": document["doc_id"],
                "title": document["title"],
                "whenCh": document["send_date"][0],
                "dateAr": document["send_date"][1],
            },
            "imperial": {
                "docId": document["doc_id"],
                "title": document["title"],
                "whenCh": document["receive_date"][0],
                "dateAr": document["receive_date"][1],
                "rescriptText": document.get("rescript_text"),
            },
            "emperor": dot_emperor,
        },
        "aiCandidates": candidates,
    }

    header = (
        "/* Part 1 「平台的整體介面」replica demonstration data.\n"
        " *\n"
        " * GENERATED FILE — regenerate with:\n"
        " *   cd \"/Users/creamybanana/Downloads/DH Project\"\n"
        " *   python3 \"tool/scripts py/build_part1_interface_data.py\"\n"
        " *\n"
        " * Every quotation, date and AI result below is copied from the canonical\n"
        " * Stage 1 source file and the current sample review state. Do not hand-write\n"
        " * new historical content here; add it to the review tool first, then rebuild.\n"
        " * Presentation-only fields (labels, ordering) are safe to edit by hand.\n"
        " */\n"
    )
    body_js = json.dumps(payload, ensure_ascii=False, indent=2)
    OUT.write_text(f"{header}window.PART1_INTERFACE_DATA = {body_js};\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
    print(f"  document: {DOC_ID} ({len(body)} chars)")
    print(f"  dots: {', '.join(payload['dots'].keys())}")
    print(f"  ai candidates: {len(candidates)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
