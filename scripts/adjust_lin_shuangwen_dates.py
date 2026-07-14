#!/usr/bin/env python3
"""Create the Stage 1 subset from the current source JSON date schema.

Input:
  /Users/creamybanana/Downloads/林爽文/Final Drive Copy/奏摺上諭結構化數據.json

Output:
  outputs/attempt-002/stage1-date-adjusted.json

Current source JSON date schema:
  - send_date: [Chinese date, Arabic date]
  - receive_date: [Chinese date, Arabic date]
  - announce_date: [Chinese date, Arabic date]
  - issue_date: [Chinese date, Arabic date] for remaining non-上諭 records

Stage 1 filter:
  黃仕簡、任承恩分路渡臺階段, roughly 乾隆五十一年十一月至乾隆五十二年三月.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


SOURCE = Path("/Users/creamybanana/Downloads/林爽文/Final Drive Copy/奏摺上諭結構化數據.json")
OUT_DIR = Path("outputs/attempt-002")
OUT_JSON = OUT_DIR / "stage1-date-adjusted.json"
OUT_SUMMARY = OUT_DIR / "stage1-date-adjustment-summary.md"

CN_NUM = {
    "〇": 0,
    "零": 0,
    "一": 1,
    "二": 2,
    "兩": 2,
    "两": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9,
}


def cn_int(text: str | None) -> int | None:
    if not text:
        return None
    text = text.strip().replace("初", "").replace("廿", "二十").replace("卅", "三十")
    if text in {"正", "元"}:
        return 1
    if text == "冬":
        return 11
    if text in {"臘", "腊"}:
        return 12
    if text.isdigit():
        return int(text)
    if "十" in text:
        left, _, right = text.partition("十")
        tens = CN_NUM.get(left, 1) if left else 1
        ones = CN_NUM.get(right, 0) if right else 0
        return tens * 10 + ones
    value = 0
    for ch in text:
        if ch not in CN_NUM:
            return None
        value = value * 10 + CN_NUM[ch]
    return value if value else None


DATE_RE = re.compile(
    r"乾隆(?P<year>[〇零一二兩两三四五六七八九十]+)年"
    r"(?:(?P<leap>閏)?(?P<month>正|元|冬|臘|腊|[〇零一二兩两三四五六七八九十]+)月)?"
    r"(?:(?P<day>初?[〇零一二兩两三四五六七八九十廿卅]+)日)?"
)


def chinese_part(value: Any) -> Any:
    if isinstance(value, list) and value:
        return value[0]
    return value


def parse_qianlong(raw_value: Any) -> tuple[int | None, int | None]:
    raw = chinese_part(raw_value)
    if not isinstance(raw, str):
        return None, None
    raw = raw.strip()
    if not raw or raw == "/":
        return None, None
    m = DATE_RE.search(raw)
    if not m:
        return None, None
    return cn_int(m.group("year")), cn_int(m.group("month"))


def is_stage1_date(raw: Any) -> bool:
    year, month = parse_qianlong(raw)
    if year is None or month is None:
        return False
    return (year == 51 and month >= 11) or (year == 52 and month <= 3)


def stage1_relevant(record: dict[str, Any]) -> bool:
    for field in ("send_date", "receive_date", "announce_date", "issue_date"):
        if is_stage1_date(record.get(field)):
            return True
    return False


def main() -> None:
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    stage1 = [row for row in data if stage1_relevant(row)]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(stage1, ensure_ascii=False, indent=2), encoding="utf-8")

    counts = Counter(row.get("doc_type") for row in stage1)
    all_counts = Counter(row.get("doc_type") for row in data)

    lines = [
        "# Attempt 002 Stage 1 Date Adjustment Summary",
        "",
        "Related pages: [[research-attempts/attempt-002-lin-shuangwen-early-stages]], [[background/lin-shuangwen-war-stages]], [[corpora/lin-shuangwen-first-hand-json]]",
        "",
        "## Rule",
        "",
        "This pass filters the current source JSON schema and does not add interpretive fields to each record.",
        "",
        "- `send_date`, `receive_date`, `announce_date`, and remaining `issue_date` values are `[Chinese date, Arabic date]` pairs.",
        "- Stage 1 filtering uses the Chinese date in each pair.",
        "",
        "Stage 1 filter: any remaining date field falls within 乾隆五十一年十一月至乾隆五十二年三月.",
        "",
        "## Counts",
        "",
        f"- Original corpus records: {len(data)}",
        f"- Stage 1 adjusted records: {len(stage1)}",
        "",
        "### Original corpus by document type",
        "",
        "| doc_type | Count |",
        "| --- | ---: |",
    ]
    for doc_type, count in all_counts.most_common():
        lines.append(f"| {doc_type} | {count} |")

    lines.extend([
        "",
        "### Stage 1 adjusted records by document type",
        "",
        "| doc_type | Count |",
        "| --- | ---: |",
    ])
    for doc_type, count in counts.most_common():
        lines.append(f"| {doc_type} | {count} |")

    lines.extend([
        "",
        "## Output",
        "",
        f"- `{OUT_JSON}`",
        "",
    ])
    OUT_SUMMARY.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
