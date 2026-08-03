#!/usr/bin/env python3
"""Build the Part 3「適合的研究問題」swimlane-gallery demonstration data.

Replaces two prose boxes with an interactive diagram showing three response
chains along the review tool's four lines (戰場事件／官員上奏／皇帝硃批下旨／
皇帝行動), plus a second slide showing the transmission-delay gap. Every dot,
date and quotation below is derived from existing project data, never invented:

  - review-tools/shared data/stage1_original_text.json   (硃42, 諭24, 硃113)
  - review-tools/(2) sample/sample_all.data              (confirmed event dots)

The chain used (硃42 -> 諭24 -> 硃113) is the same one already vetted and used
in Part 1 and in 研究清代奏折的主要困難, so this stays consistent with the rest
of the site rather than introducing a new, unchecked example.

Output: intro Website/Website/storymap/part-3-question-gallery-data.js
        (a hand-editable module assigned to window.PART3_QUESTION_DATA)

Usage:
    cd "/Users/creamybanana/Downloads/DH Project"
    python3 "tool/scripts py/build_part3_question_data.py"
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STAGE1 = ROOT / "review-tools" / "shared data" / "stage1_original_text.json"
SAMPLE_STATE = ROOT / "review-tools" / "(2) sample" / "sample_all.data"
OUT = ROOT / "intro Website" / "Website" / "storymap" / "part-3-question-gallery-data.js"

# Chain 1 — four 戰場事件 dots cited inside 硃42, oldest to newest. These are
# the four dots already confirmed as event nodes in the sample review state
# (not every event lin-events.json extracted from 硃42 was kept as its own
# dot; some duplicate earlier documents' dots and were deduplicated away).
EVENT_NAMES = [
    "賊匪於三坎店交戰稍退",
    "澎湖兵渡海前往臺灣赴援",
    "黃仕簡率兵由廈門放洋",
    "任承恩配兵登舟準備進剿",
]

# Chain 2 — three 皇帝行動 dots extracted from 諭24. Each must carry its own
# quotation (a few 諭24 action cards in the sample state have no `quote`,
# e.g. summarising ones without a single matching span; those are skipped).
EMPEROR_ACTION_NAMES = [
    "據柴大紀於三坎店大施火砲擊退賊眾之報研判臺灣郡城防守嚴密且全臺尚無他虞",
    "認可徐嗣曾由臣標及督標水師抽調一千五百名兵丁渡臺協剿",
    "准徐嗣曾飛咨粵浙酌撥備戰兵為後備並戒其不動聲色毋驚眾聽",
]

# Slide 2 — five real events from other memorials, all dated strictly between
# 硃42's send date (1786/12/18) and 諭24's issue date (1787/01/02), showing
# what happened in Fujian/Zhejiang while 硃42 was still in transit.
TRANSIT_EVENT_NAMES = [
    "常青派徐鼎士帶兵渡臺",
    "徐嗣曾預調官兵至省城",
    "孫士毅挑選水師千名備戰",
    "覺羅琅玕飛咨陳大用等撥兵",
    "陳大用調派五百名提標鎮海兵啟程赴閩浙交界聲援",
]

# 硃113's own reply to 諭24, already curated and displayed in 研究清代奏折的
# 主要困難 (硃113 document panel). Reused verbatim rather than re-derived.
ZHU113_REPLY_QUOTE = "又於十三日亥刻，承准廷寄，正月初二日奉上諭"


def fail(message: str) -> None:
    raise SystemExit(f"build_part3_question_data: {message}")


def load_stage1() -> dict:
    records = json.loads(STAGE1.read_text(encoding="utf-8"))
    return {record["doc_id"]: record for record in records}


def load_events() -> list:
    state = json.loads(SAMPLE_STATE.read_text(encoding="utf-8"))
    return state.get("__events", [])


def find_event(events: list, subtitle: str) -> dict:
    matches = [event for event in events if event.get("subtitle") == subtitle]
    if not matches:
        fail(f"event not found in sample state: {subtitle!r}")
    if len(matches) > 1:
        fail(f"ambiguous event subtitle (found {len(matches)}): {subtitle!r}")
    return matches[0]


def event_payload(event: dict) -> dict:
    source = (event.get("sources") or [{}])[0]
    return {
        "id": event.get("id"),
        "actor": event.get("actor"),
        "subtitle": event.get("subtitle"),
        "description": event.get("description"),
        "whenCh": event.get("whenCh"),
        "dateAr": event.get("dateAr"),
        "quote": source.get("quote"),
        "quoteDocId": source.get("doc_id"),
    }


def doc_payload(record: dict) -> dict:
    payload = {
        "docId": record["doc_id"],
        "docType": record["doc_type"],
        "title": record["title"],
        "author": record["author"],
        "body": record["body"],
    }
    if "send_date" in record:
        payload["sendDate"] = record["send_date"]
    if "receive_date" in record:
        payload["receiveDate"] = record["receive_date"]
    if "announce_date" in record:
        payload["announceDate"] = record["announce_date"]
    if record.get("rescript_text"):
        payload["rescriptText"] = record["rescript_text"]
    return payload


def check_quote(body: str, quote: str, label: str) -> None:
    if quote and quote not in body:
        fail(f"quote for {label!r} is not a literal substring of its source body")


def main() -> int:
    stage1 = load_stage1()
    events = load_events()

    for doc_id in ("硃42", "諭24", "硃113"):
        if doc_id not in stage1:
            fail(f"{doc_id} missing from {STAGE1}")

    zhu42 = doc_payload(stage1["硃42"])
    yu24 = doc_payload(stage1["諭24"])
    zhu113 = doc_payload(stage1["硃113"])

    event_dots = [event_payload(find_event(events, name)) for name in EVENT_NAMES]
    emperor_dots = [event_payload(find_event(events, name)) for name in EMPEROR_ACTION_NAMES]
    transit_dots = [event_payload(find_event(events, name)) for name in TRANSIT_EVENT_NAMES]

    for item in event_dots + emperor_dots:
        if not item.get("quote"):
            fail(f"{item['subtitle']!r} has no quote in sample state; pick a dot with a quotation")
    for item in event_dots:
        check_quote(zhu42["body"], item["quote"], item["subtitle"])
    for item in emperor_dots:
        check_quote(yu24["body"], item["quote"], item["subtitle"])
    for item in transit_dots:
        source_record = stage1.get(item["quoteDocId"])
        if not source_record:
            fail(f"transit event {item['subtitle']!r} cites unknown doc {item['quoteDocId']!r}")
        check_quote(source_record["body"], item["quote"], item["subtitle"])

    if ZHU113_REPLY_QUOTE not in zhu113["body"]:
        fail("硃113 reply quote is not a literal substring of its own body")

    payload = {
        "_generated_by": "tool/scripts py/build_part3_question_data.py",
        "_sources": [
            "review-tools/shared data/stage1_original_text.json",
            "review-tools/(2) sample/sample_all.data",
        ],
        "lanes": [
            {"key": "events", "label": "戰場事件", "color": "#b5462e"},
            {"key": "official", "label": "官員上奏", "color": "#2f75b5"},
            {"key": "imperial", "label": "皇帝硃批下旨", "color": "#c46a2b"},
            {"key": "emperor", "label": "皇帝行動", "color": "#7d4ab8"},
        ],
        "documents": {"硃42": zhu42, "諭24": yu24, "硃113": zhu113},
        "eventDots": event_dots,
        "emperorDots": emperor_dots,
        "transitDots": transit_dots,
        "zhu113Reply": {
            "docId": "硃113",
            "quote": ZHU113_REPLY_QUOTE,
            "respondsTo": "諭24",
        },
        # Precomputed day-lag between 硃42's send date and 諭24's issue date,
        # for the slide-2 time-gap annotation. Kept as data, not hard-coded
        # prose, so re-running the script recomputes it if the source dates
        # ever change.
        "transitGapDays": None,
    }

    from datetime import date

    def parse(value: str) -> date:
        year, month, day = (int(part) for part in value.split("/"))
        return date(year, month, day)

    send = parse(zhu42["sendDate"][1])
    issue = parse(yu24["announceDate"][1])
    payload["transitGapDays"] = (issue - send).days

    header = (
        "/* Part 3「適合的研究問題」swimlane gallery data.\n"
        " *\n"
        " * GENERATED FILE — regenerate with:\n"
        " *   cd \"/Users/creamybanana/Downloads/DH Project\"\n"
        " *   python3 \"tool/scripts py/build_part3_question_data.py\"\n"
        " *\n"
        " * Every quotation, date and event below is copied from the canonical\n"
        " * Stage 1 source file and the current sample review state. Do not\n"
        " * hand-write new historical content here; add it to the review tool\n"
        " * first, then rebuild. Presentation-only fields are safe to edit.\n"
        " */\n"
    )
    body_js = json.dumps(payload, ensure_ascii=False, indent=2)
    OUT.write_text(f"{header}window.PART3_QUESTION_DATA = {body_js};\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
    print(f"  events: {len(event_dots)}, emperor actions: {len(emperor_dots)}, transit events: {len(transit_dots)}")
    print(f"  transit gap: {payload['transitGapDays']} days (硃42 send -> 諭24 issue)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
