#!/usr/bin/env python3
"""Publish the REVIEWED (human-adopted) 相關上諭配對（無引文）pairs as CONFIRMED
pairs, so they draw as 回應上諭 connector lines in both the live and sample app.

Why confirmed-pairs.json (not yu-pairing-nocite.json)
-----------------------------------------------------
The page draws connector lines from ``allDocPairs()`` = ``EDITS.__docPairs`` +
``CONFIRMED_PAIRS``, and ``CONFIRMED_PAIRS`` is loaded from **confirmed-pairs.json**.
``yu-pairing-nocite.json`` only seeds review *cards* (proposals to adopt) and never
draws a line. So reviewed pairs that should appear as lines belong in
confirmed-pairs.json.

Where the reviewed data comes from
----------------------------------
Clicking 加入配對 writes a pair into ``__docPairs``, persisted by review-app/server.py:
  * live app   : outputs/attempt-002/timeline-edits.local.json
  * sample app : outputs/attempt-002/sample-mode/sample-edits.local.json

What this does
--------------
1. Reads ``__docPairs`` from BOTH edits files.
2. Keeps the no-citation official_reply_to_yu pairs (explicit no_citation flag, or the
   no-citation evidence shape: relation_note/send_date and no citation marker).
3. Merges them and MERGES INTO each folder's confirmed-pairs.json, preserving the
   pairs already there, de-duplicating by (yu_doc_id, reply_doc_id, relation).
   A missing confirmed-pairs.json (sample folder) is created. Each existing file
   is backed up to <name>.bak first.

After running, reload each page: the reviewed no-citation pairs appear as
回應上諭 lines (CONFIRMED_PAIRS -> allDocPairs).

Usage:
  python3 "tool/scripts py/export_nocite_reviewed.py"
  python3 "tool/scripts py/export_nocite_reviewed.py" --dry-run
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ATTEMPT = ROOT / "outputs" / "attempt-002"

# (label, edits file to read, confirmed-pairs.json to merge into)
SITES = [
    ("live",   ATTEMPT / "timeline-edits.local.json",               ATTEMPT / "confirmed-pairs.json"),
    ("sample", ATTEMPT / "sample-mode" / "sample-edits.local.json", ATTEMPT / "sample-mode" / "confirmed-pairs.json"),
]

_CITATION_EV = ("marker", "issue_date", "receive_date", "receipt")


def is_nocite(pair: dict) -> bool:
    if (pair.get("relation") or "official_reply_to_yu") != "official_reply_to_yu":
        return False
    ev = pair.get("evidence") or {}
    if pair.get("no_citation") or ev.get("no_citation"):
        return True
    if (ev.get("relation_note") or ev.get("send_date")) and not any(ev.get(k) for k in _CITATION_EV):
        return True
    return False


def to_confirmed(pair: dict, now: str) -> dict:
    ev = pair.get("evidence") or {}
    return {
        "yu_doc_id": pair.get("yu_doc_id", ""),
        "reply_doc_id": pair.get("reply_doc_id", ""),
        "relation": "official_reply_to_yu",
        "no_citation": True,
        "match_level": pair.get("match_level") or ev.get("match_level") or "",
        "reply_status": pair.get("reply_status") or ev.get("reply_status") or "ack",
        "confirmed_at": pair.get("at") or now,
        "evidence": {
            "quote_in_reply": ev.get("quote_in_reply", ""),
            "matched_yu_span": ev.get("matched_yu_span", ""),
            "relation_note": ev.get("relation_note", ""),
            "send_date": ev.get("send_date", "未明"),
        },
    }


def key(p: dict) -> tuple[str, str, str]:
    return (str(p.get("yu_doc_id", "")), str(p.get("reply_doc_id", "")),
            str(p.get("relation") or "official_reply_to_yu"))


def load_docpairs(path: Path) -> list[dict]:
    if not path.exists():
        print(f"  (skip: {path.name} not found)")
        return []
    try:
        return (json.loads(path.read_text(encoding="utf-8")).get("__docPairs")) or []
    except Exception as exc:  # noqa: BLE001
        print(f"  (skip: {path.name} unreadable: {exc})")
        return []


def load_confirmed(path: Path) -> dict:
    """Return the confirmed-pairs.json dict ({kind,exported_at,count,pairs}),
    creating a skeleton if the file is missing or a bare list."""
    if not path.exists():
        return {"kind": "confirmed-pairs", "exported_at": "", "count": 0, "pairs": []}
    d = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(d, list):
        return {"kind": "confirmed-pairs", "exported_at": "", "count": len(d), "pairs": d}
    d.setdefault("pairs", [])
    return d


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="Report only; write nothing.")
    args = ap.parse_args()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    reviewed: list[dict] = []
    for label, edits_path, _out in SITES:
        pairs = load_docpairs(edits_path)
        hits = [p for p in pairs if is_nocite(p)]
        print(f"{label:>7}: {len(hits)} reviewed no-citation pair(s) in {edits_path.name} "
              f"(of {len(pairs)} adopted)")
        reviewed.extend(hits)

    # merge + dedup reviewed set
    merged: dict = {}
    for p in reviewed:
        k = key(p)
        if k[0] and k[1] and k not in merged:
            merged[k] = to_confirmed(p, now)
    reviewed_confirmed = list(merged.values())
    print(f"\nmerged unique reviewed pairs: {len(reviewed_confirmed)}")

    if args.dry_run:
        print("dry-run: no files written.")
        return 0

    for _label, _edits, out_path in SITES:
        doc = load_confirmed(out_path)
        existing = doc["pairs"]
        have = {key(p) for p in existing}
        added = 0
        for p in reviewed_confirmed:
            if key(p) not in have:
                existing.append(p)
                have.add(key(p))
                added += 1
        doc["exported_at"] = now
        doc["count"] = len(existing)

        out_path.parent.mkdir(parents=True, exist_ok=True)
        if out_path.exists():
            backup = out_path.with_suffix(out_path.suffix + ".bak")
            backup.write_text(out_path.read_text(encoding="utf-8"), encoding="utf-8")
            print(f"backed up {out_path.relative_to(ROOT)} -> {backup.name}")
        out_path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n",
                            encoding="utf-8")
        print(f"{out_path.relative_to(ROOT)}: +{added} new, {len(existing)} total confirmed pairs")

    print("\nDone. Reload each page; the reviewed no-citation pairs now draw as "
          "回應上諭 lines (via CONFIRMED_PAIRS).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
