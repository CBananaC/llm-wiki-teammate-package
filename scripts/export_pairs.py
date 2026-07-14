#!/usr/bin/env python3
"""Export confirmed 上諭／硃批／在案前奏 pairs to shareable JSON.

Non-destructive alternative to merge_pairs.py: instead of writing into the
source corpus (stage1-date-adjusted.json), this reads the pairs you marked
"加入配對" (the site saves them into timeline-edits.local.json under __docPairs)
and writes a self-contained `confirmed-pairs.json` — each pair enriched with the
AI evidence (reasons, quote, dates) and both documents' info. It also writes a
loadable review-bundle so the website can redraw the connector lines from it.

Usage:
  python3 scripts/export_pairs.py            # write confirmed-pairs.json + bundle
  python3 scripts/export_pairs.py --dry-run  # report only
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ATTEMPT = ROOT / "outputs" / "attempt-002"
EDITS_PATH = ATTEMPT / "timeline-edits.local.json"          # written by review-app/server.py
CORPUS_PATH = ATTEMPT / "dual-timeline-data.json"
OUT_PATH = ATTEMPT / "confirmed-pairs.json"
BUNDLE_NAME = "confirmed-pairs"


def load(path: Path, fallback=None):
    if not path.exists():
        if fallback is not None:
            return fallback
        sys.exit(f"not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def doc_brief(rec: dict | None) -> dict:
    if not rec:
        return {}
    author = rec.get("author_name") or ""
    return {
        "id": rec.get("id", ""),
        "title": rec.get("title", ""),
        "type": rec.get("type", ""),
        "doc_type": rec.get("doc_type", ""),
        "author": author,
        "recipients": rec.get("recipients", []),
        "issue_date": rec.get("annAr", ""),
        "send_date": rec.get("sendAr", ""),
        "receive_date": rec.get("recvAr", ""),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--edits", type=Path, default=EDITS_PATH)
    ap.add_argument("--out", type=Path, default=OUT_PATH)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    edits = load(args.edits, fallback={})
    pairs = [p for p in (edits.get("__docPairs") or []) if p.get("yu_doc_id") and p.get("reply_doc_id")]
    if not pairs:
        print("No confirmed pairs in __docPairs. Click 加入配對 in the timeline first "
              "(served by run-local.py so the clicks are saved).")
        return 0

    by_id = {r.get("id"): r for r in load(CORPUS_PATH)}
    exported, missing = [], []
    for p in pairs:
        yu, reply = str(p["yu_doc_id"]), str(p["reply_doc_id"])
        relation = p.get("relation") or "reply_to_yu"
        if yu not in by_id or reply not in by_id:
            missing.append((reply, yu))
        item = {
            "yu_doc_id": yu,
            "reply_doc_id": reply,
            "relation": relation,
            "match_level": p.get("match_level", ""),
            "confirmed_at": p.get("at", ""),
            "evidence": p.get("evidence", {}),
            "yu": doc_brief(by_id.get(yu)),
            "reply": doc_brief(by_id.get(reply)),
        }
        if relation == "prior_report":
            item["previous_doc_id"] = str(p.get("previous_doc_id") or yu)
            item["previous"] = doc_brief(by_id.get(yu))
        elif relation == "reply_to_zhu":
            item["zhu_doc_id"] = str(p.get("zhu_doc_id") or yu)
            item["zhu"] = doc_brief(by_id.get(yu))
        exported.append(item)

    result = {
        "kind": "confirmed-pairs",
        "exported_at": datetime.now().isoformat(timespec="seconds"),
        "count": len(exported),
        "pairs": exported,
    }

    print(f"confirmed pairs: {len(exported)} | docs missing from corpus: {len(missing)}")
    for reply, yu in missing:
        print(f"  ! not found in corpus: {reply} or {yu}")
    if args.dry_run:
        print("\n(dry run — nothing written)")
        return 0

    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    bundle_root = ROOT / "outputs" / "review-bundles" / BUNDLE_NAME
    (bundle_root / "outputs").mkdir(parents=True, exist_ok=True)
    (bundle_root / "outputs" / "confirmed-pairs.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (bundle_root / "manifest.json").write_text(json.dumps({
        "name": BUNDLE_NAME,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "source": "outputs/attempt-002/timeline-edits.local.json",
        "doc_ids": sorted({p["yu_doc_id"] for p in exported} | {p["reply_doc_id"] for p in exported}),
        "chain": ["confirmed-pairs"],
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"\nwrote {args.out}\nbundle {bundle_root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
