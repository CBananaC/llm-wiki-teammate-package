#!/usr/bin/env python3
"""Export marked document pairs to shareable JSON.

Non-destructive alternative to merge_pairs.py: instead of writing into the
source corpus, this reads the pairs you marked "加入配對" (the formal site saves
them into `formal_all.data` under `__docPairs`) and writes a self-contained JSON
export. It supports response pairs and `yu_source` 上諭—來源 pairs, and also
writes a loadable review bundle.

Usage:
  python3 "tool/scripts py/export_pairs.py" --relation yu_source
  python3 "tool/scripts py/export_pairs.py" --relation yu_source --dry-run
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EDITS_PATH = ROOT / "review-tools" / "(1) formal" / "formal_all.data"
CORPUS_PATH = ROOT / "review-tools" / "shared data" / "stage1_original_text.json"
FORMAL_DIR = ROOT / "review-tools" / "(1) formal"
BUNDLES_DIR = ROOT / "review-tools" / "shared data" / "review-bundles"


def load(path: Path, fallback=None):
    if not path.exists():
        if fallback is not None:
            return fallback
        sys.exit(f"not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def doc_brief(rec: dict | None) -> dict:
    if not rec:
        return {}
    author = rec.get("author")
    if isinstance(author, dict):
        author = author.get("name") or ""
    author = author or rec.get("author_name") or ""
    doc_id = rec.get("id") or rec.get("doc_id") or ""
    return {
        "id": doc_id,
        "title": rec.get("title", ""),
        "type": rec.get("type", ""),
        "doc_type": rec.get("doc_type", ""),
        "author": author,
        "recipients": rec.get("recipients", []),
        "issue_date": rec.get("annAr") or rec.get("issue_date") or "",
        "send_date": rec.get("sendAr") or rec.get("send_date") or "",
        "receive_date": rec.get("recvAr") or rec.get("receive_date") or "",
    }


def records_by_id(path: Path) -> dict[str, dict]:
    rows = load(path)
    if isinstance(rows, dict):
        rows = rows.get("records") or rows.get("documents") or []
    return {
        str(r.get("id") or r.get("doc_id")): r
        for r in rows
        if isinstance(r, dict) and (r.get("id") or r.get("doc_id"))
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--edits", type=Path, default=EDITS_PATH)
    ap.add_argument("--source", type=Path, default=CORPUS_PATH,
                    help="Canonical document corpus used to enrich the export.")
    ap.add_argument("--out", type=Path,
                    help="Output JSON path; defaults according to --relation.")
    ap.add_argument("--bundle-name",
                    help="Review-bundle name; defaults according to --relation.")
    ap.add_argument(
        "--relation",
        choices=("all", "yu_source", "official_reply_to_yu", "official_reply_to_emperor_zhu"),
        default="all",
        help="Export all marked pairs or only one relationship type.",
    )
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if args.out is None:
        args.out = (FORMAL_DIR / "yu-source-confirmed.json"
                    if args.relation == "yu_source"
                    else FORMAL_DIR / "confirmed-pairs-export.json")
    if args.bundle_name is None:
        args.bundle_name = ("yu-source-confirmed"
                            if args.relation == "yu_source"
                            else "confirmed-pairs-export")

    edits = load(args.edits, fallback={})
    pairs = [
        p for p in (edits.get("__docPairs") or [])
        if p.get("yu_doc_id")
        and p.get("reply_doc_id")
        and (args.relation == "all" or (p.get("relation") or "official_reply_to_yu") == args.relation)
    ]
    if not pairs:
        print(f"No marked pairs for relation {args.relation!r} in __docPairs. "
              "Click 加入配對 in the formal timeline first and make sure the review server is running.")
        return 0

    by_id = records_by_id(args.source)
    exported, missing = [], []
    for p in pairs:
        yu, reply = str(p["yu_doc_id"]), str(p["reply_doc_id"])
        relation = p.get("relation") or "official_reply_to_yu"
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
        if relation == "yu_source":
            item["source_doc_id"] = reply
            item["source"] = doc_brief(by_id.get(reply))
        if relation == "official_reply_to_emperor_zhu":
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

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    bundle_root = BUNDLES_DIR / args.bundle_name
    output_name = args.out.name
    (bundle_root / "outputs").mkdir(parents=True, exist_ok=True)
    (bundle_root / "outputs" / output_name).write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (bundle_root / "manifest.json").write_text(json.dumps({
        "name": args.bundle_name,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "source": str(args.edits.absolute().relative_to(ROOT)),
        "output": output_name,
        "doc_ids": sorted({p["yu_doc_id"] for p in exported} | {p["reply_doc_id"] for p in exported}),
        "chain": ["confirmed-pairs"],
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"\nwrote {args.out}\nbundle {bundle_root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
