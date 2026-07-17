#!/usr/bin/env python3
"""Apply date-field semantics directly to 奏摺上諭結構化數據.json.

This script edits only the three main date fields according to doc_type:
- 上奏: keep memorial_date; remove rescript_date and issue_date.
- 硃批: keep memorial_date and rescript_date; remove issue_date.
- 上諭: keep issue_date; remove memorial_date and rescript_date.

It does not add new fields or inferred values.
"""

from __future__ import annotations

import argparse
import json
import os
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any


DEFAULT_JSON = Path("/Users/creamybanana/Downloads/林爽文/Final Drive Copy/奏摺上諭結構化數據.json")


def adjust_record(record: dict[str, Any]) -> tuple[dict[str, Any], bool]:
    out = dict(record)
    before_keys = set(out.keys())
    before_values = {k: out.get(k) for k in ("memorial_date", "rescript_date", "issue_date") if k in out}

    doc_type = out.get("doc_type")
    if doc_type == "上奏":
        out.pop("rescript_date", None)
        out.pop("issue_date", None)
    elif doc_type == "硃批":
        out.pop("issue_date", None)
    elif doc_type == "上諭":
        out.pop("memorial_date", None)
        out.pop("rescript_date", None)

    after_keys = set(out.keys())
    after_values = {k: out.get(k) for k in ("memorial_date", "rescript_date", "issue_date") if k in out}
    return out, before_keys != after_keys or before_values != after_values


def atomic_write_json(path: Path, data: list[dict[str, Any]]) -> None:
    text = json.dumps(data, ensure_ascii=False, indent=2)
    fd, tmp_name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
            f.write("\n")
        os.replace(tmp_name, path)
    except Exception:
        try:
            os.unlink(tmp_name)
        except FileNotFoundError:
            pass
        raise


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    data = json.loads(args.json.read_text(encoding="utf-8"))
    adjusted = []
    changed_by_type = Counter()
    for record in data:
        out, changed = adjust_record(record)
        adjusted.append(out)
        if changed:
            changed_by_type[out.get("doc_type")] += 1

    summary = {
        "records": len(data),
        "changed_by_type": dict(changed_by_type),
        "checks": {
            "bad_shangzou_extra_dates": sum(
                1 for row in adjusted
                if row.get("doc_type") == "上奏" and ("rescript_date" in row or "issue_date" in row)
            ),
            "bad_zhupi_issue_date": sum(
                1 for row in adjusted
                if row.get("doc_type") == "硃批" and "issue_date" in row
            ),
            "bad_shangyu_memorial_or_rescript": sum(
                1 for row in adjusted
                if row.get("doc_type") == "上諭" and ("memorial_date" in row or "rescript_date" in row)
            ),
        },
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if args.write:
        atomic_write_json(args.json, adjusted)
        print(f"wrote {args.json}")
    else:
        print("dry run only; pass --write to update the JSON")


if __name__ == "__main__":
    main()
