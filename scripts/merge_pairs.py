#!/usr/bin/env python3
"""Merge confirmed 上諭／硃批／在案前奏 pairs into the source JSON.

Reads the pairs you clicked "加入配對" on in the timeline (the site auto-saves
them into timeline-edits.local.json under `__docPairs`) and writes each one as a
`responds_to` entry on the replying document in stage1-date-adjusted.json, plus a
reciprocal `responses` entry on the 上諭.

Usage:
  python3 scripts/merge_pairs.py            # merge everything you've confirmed
  python3 scripts/merge_pairs.py --dry-run  # show what would change, write nothing
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ATTEMPT = ROOT / "outputs" / "attempt-002"
EDITS_PATH = ATTEMPT / "timeline-edits.local.json"          # written by review-app/server.py
SOURCE_PATH = ATTEMPT / "stage1-date-adjusted.json"


def load(path: Path):
    if not path.exists():
        sys.exit(f"not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def confirmed_pairs(edits: dict) -> list[dict]:
    pairs = edits.get("__docPairs") or []
    if not isinstance(pairs, list):
        return []
    return [p for p in pairs if p.get("yu_doc_id") and p.get("reply_doc_id")]


def upsert(entries: list[dict], key_field: str, key_val: str, payload: dict) -> str:
    """Insert or update the entry whose key_field == key_val. Returns 'added'/'updated'."""
    for e in entries:
        if str(e.get(key_field)) == str(key_val):
            e.update(payload)
            return "updated"
    entries.append(payload)
    return "added"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--edits", type=Path, default=EDITS_PATH,
                    help="Edits file the site saved (default: timeline-edits.local.json).")
    ap.add_argument("--source", type=Path, default=SOURCE_PATH,
                    help="Source JSON to write into (default: stage1-date-adjusted.json).")
    ap.add_argument("--dry-run", action="store_true", help="Report only; write nothing.")
    args = ap.parse_args()

    edits = load(args.edits)
    pairs = confirmed_pairs(edits)
    if not pairs:
        print(f"No confirmed pairs in {args.edits.name} (__docPairs empty). "
              "Click 加入配對 in the timeline first — the site must be served by review-app/server.py "
              "so the clicks are saved to disk.")
        return 0

    source = load(args.source)
    by_id = {r.get("doc_id"): r for r in source}

    changes, missing = [], []
    for p in pairs:
        yu, reply = str(p["yu_doc_id"]), str(p["reply_doc_id"])
        relation = p.get("relation") or "reply_to_yu"
        ev = p.get("evidence") or {}
        r_rec, y_rec = by_id.get(reply), by_id.get(yu)
        if not r_rec or not y_rec:
            missing.append((reply, yu))
            continue
        # responds_to on the replying document
        relation_type = ("前奏（在案）" if relation == "prior_report"
                         else "硃批" if relation == "reply_to_zhu" else "上諭")
        st = upsert(r_rec.setdefault("responds_to", []), "doc_id", yu, {
            "doc_id": yu,
            "type": relation_type,
            "relation": relation,
            "issue_date": ev.get("issue_date") or ev.get("previous_report_date", ""),
            "receive_date": ev.get("receive_date", ""),
            "marker": ev.get("marker", ""),
            "quote": (ev.get("quote_in_reply") or ev.get("reference_in_later_doc")
                      or ev.get("matched_later_span", "")),
            "match_level": p.get("match_level", ""),
            "confirmed_at": p.get("at", ""),
        })
        # reciprocal responses entry on the 上諭
        upsert(y_rec.setdefault("responses", []), "doc_id", reply, {
            "doc_id": reply,
            "type": y_rec.get("doc_type", ""),
            "match_level": p.get("match_level", ""),
        })
        changes.append(f"  {reply} → {relation_type} {yu}  [{p.get('match_level','')}]  ({st})")

    print(f"confirmed pairs: {len(pairs)} | applied: {len(changes)} | missing docs: {len(missing)}")
    for line in changes:
        print(line)
    for reply, yu in missing:
        print(f"  ! doc not found in source: {reply} or {yu}")

    if args.dry_run:
        print("\n(dry run — nothing written)")
        return 0
    if not changes:
        return 0

    backup = args.source.with_suffix(f".backup-{datetime.now():%Y%m%d-%H%M%S}.json")
    shutil.copy2(args.source, backup)
    args.source.write_text(json.dumps(source, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\nwrote {args.source}\nbackup {backup}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
