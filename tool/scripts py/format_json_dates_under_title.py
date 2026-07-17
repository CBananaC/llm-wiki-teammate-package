#!/usr/bin/env python3
"""Place date fields immediately after title and keep date pairs on one line."""

from __future__ import annotations

import argparse
import json
import os
import tempfile
from pathlib import Path
from typing import Any


DATE_FIELDS = ("send_date", "receive_date", "announce_date", "issue_date")


def reorder_record(record: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    inserted_dates = False

    def insert_dates() -> None:
        nonlocal inserted_dates
        if inserted_dates:
            return
        for field in DATE_FIELDS:
            if field in record:
                out[field] = record[field]
        inserted_dates = True

    for key, value in record.items():
        if key in DATE_FIELDS:
            continue
        out[key] = value
        if key == "title":
            insert_dates()

    if not inserted_dates:
        insert_dates()
    return out


def reorder_data(data: Any) -> Any:
    if isinstance(data, list):
        return [reorder_data(item) for item in data]
    if isinstance(data, dict):
        return reorder_record(data)
    return data


def inline_list(value: Any) -> bool:
    return (
        isinstance(value, list)
        and len(value) <= 2
        and all(item is None or isinstance(item, (str, int, float, bool)) for item in value)
    )


def dump_value(value: Any, level: int = 0, indent: int = 2) -> str:
    pad = " " * (level * indent)
    next_pad = " " * ((level + 1) * indent)

    if isinstance(value, dict):
        if not value:
            return "{}"
        lines = ["{"]
        items = list(value.items())
        for i, (key, item) in enumerate(items):
            comma = "," if i < len(items) - 1 else ""
            lines.append(
                f"{next_pad}{json.dumps(key, ensure_ascii=False)}: {dump_value(item, level + 1, indent)}{comma}"
            )
        lines.append(f"{pad}}}")
        return "\n".join(lines)

    if isinstance(value, list):
        if inline_list(value):
            return json.dumps(value, ensure_ascii=False)
        if not value:
            return "[]"
        lines = ["["]
        for i, item in enumerate(value):
            comma = "," if i < len(value) - 1 else ""
            lines.append(f"{next_pad}{dump_value(item, level + 1, indent)}{comma}")
        lines.append(f"{pad}]")
        return "\n".join(lines)

    return json.dumps(value, ensure_ascii=False)


def atomic_write(path: Path, text: str) -> None:
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


def summarize(data: list[dict[str, Any]]) -> dict[str, Any]:
    bad_order = 0
    date_field_counts = {field: 0 for field in DATE_FIELDS}
    for record in data:
        keys = list(record.keys())
        if "title" in record:
            title_i = keys.index("title")
            seen_non_date_after_title = False
            for key in keys[title_i + 1:]:
                if key in DATE_FIELDS:
                    date_field_counts[key] += 1
                    if seen_non_date_after_title:
                        bad_order += 1
                else:
                    seen_non_date_after_title = True
        else:
            for key in DATE_FIELDS:
                if key in record:
                    date_field_counts[key] += 1
    return {
        "records": len(data),
        "date_field_counts": date_field_counts,
        "bad_date_order_after_title": bad_order,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("json_path", type=Path)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    data = json.loads(args.json_path.read_text(encoding="utf-8"))
    reordered = reorder_data(data)
    summary = summarize(reordered)
    print(json.dumps(summary, ensure_ascii=False, indent=2))

    if args.write:
        atomic_write(args.json_path, dump_value(reordered))
        print(f"wrote {args.json_path}")
    else:
        print("dry run only; pass --write to reformat")


if __name__ == "__main__":
    main()
