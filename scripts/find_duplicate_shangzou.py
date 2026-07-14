#!/usr/bin/env python3
"""Find near-duplicate 上奏 dots whose counterpart is a non-上奏 record.

This mirrors the website's local "隱藏重複上奏點" candidate search:
date window ±3 days, Dice similarity over 8-character shingles, and a
minimum length ratio gate. It only reports candidates; it does not hide or
edit anything.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "outputs" / "attempt-002" / "stage1-date-adjusted.json"


def pair_value(record: dict[str, Any], key: str) -> str:
    value = record.get(key)
    if isinstance(value, list) and len(value) > 1:
        return value[1] or ""
    return ""


def record_dates(record: dict[str, Any]) -> list[str]:
    return [
        d for d in [
            pair_value(record, "send_date"),
            pair_value(record, "receive_date"),
            pair_value(record, "announce_date"),
            pair_value(record, "issue_date"),
        ]
        if d
    ]


def parse_date(value: str):
    try:
        return datetime.strptime((value or "").replace("/", "-"), "%Y-%m-%d").date()
    except ValueError:
        return None


def norm_text(text: str) -> str:
    text = re.sub(r"【硃批】[\s\S]*$", "", text or "")
    return re.sub(r"[，。、《》；：：「」『』（）()！？\s\n\r\t]", "", text)


def shingles(text: str, size: int = 8) -> set[str]:
    text = norm_text(text)
    if len(text) < size:
        return set()
    return {text[i : i + size] for i in range(len(text) - size + 1)}


def dice_similarity(a: str, b: str) -> float:
    aa, bb = shingles(a), shingles(b)
    if not aa or not bb:
        return 0.0
    return (2 * len(aa & bb)) / (len(aa) + len(bb))


def shared_snippet(a: str, b: str) -> str:
    aa, bb = norm_text(a), norm_text(b)
    for length in range(42, 13, -7):
        for i in range(0, max(0, len(aa) - length + 1), 7):
            snippet = aa[i : i + length]
            if snippet and snippet in bb:
                return snippet
    return aa[:36]


def split_csv(value: str) -> list[str]:
    return [s.strip() for s in value.split(",") if s.strip()]


def main() -> None:
    ap = argparse.ArgumentParser(description="Find similar 上奏/non-上奏 document pairs.")
    ap.add_argument("--source", default=str(DEFAULT_SOURCE), help="Source JSON path")
    ap.add_argument("--doc-ids", default="", help="Comma-separated doc IDs to limit the visible/review set")
    ap.add_argument("--date-window", type=int, default=3, help="Maximum date difference in days")
    ap.add_argument("--sim-min", type=float, default=0.72, help="Minimum Dice similarity")
    ap.add_argument("--len-ratio-min", type=float, default=0.40, help="Minimum shorter/longer normalized text length ratio")
    ap.add_argument("--format", choices=["tsv", "json"], default="tsv")
    ap.add_argument("--output", default="", help="Optional output file")
    ap.add_argument("--bundle", default="", help="Write as a review bundle that can be loaded by the website")
    args = ap.parse_args()

    source = Path(args.source)
    records = json.loads(source.read_text(encoding="utf-8"))

    if args.doc_ids.strip():
        wanted = set(split_csv(args.doc_ids))
        records = [r for r in records if str(r.get("doc_id") or r.get("id")) in wanted]

    shangzou = [r for r in records if r.get("doc_type") == "上奏"]
    keepers = [r for r in records if r.get("doc_type") != "上奏"]
    pairs = []

    for shang in shangzou:
        shang_dates = [d for d in map(parse_date, record_dates(shang)) if d]
        if not shang_dates:
            continue
        shang_body = shang.get("body") or ""
        for keep in keepers:
            keep_dates = [d for d in map(parse_date, record_dates(keep)) if d]
            if not keep_dates:
                continue
            min_diff = min(abs((sd - kd).days) for sd in shang_dates for kd in keep_dates)
            if min_diff > args.date_window:
                continue
            keep_body = keep.get("body") or ""
            sim = dice_similarity(shang_body, keep_body)
            n1, n2 = len(norm_text(shang_body)), len(norm_text(keep_body))
            len_ratio = min(n1, n2) / max(n1, n2 or 1)
            if sim >= args.sim_min and len_ratio >= args.len_ratio_min:
                pairs.append({
                    "doc_id": shang.get("doc_id") or shang.get("id"),
                    "date": record_dates(shang)[0] if record_dates(shang) else "",
                    "day_diff": min_diff,
                    "sim": round(sim, 4),
                    "similarity": round(sim, 4),
                    "length_ratio": round(len_ratio, 4),
                    "hideId": shang.get("doc_id") or shang.get("id"),
                    "hide_id": shang.get("doc_id") or shang.get("id"),
                    "hideTitle": shang.get("title") or "",
                    "hide_title": shang.get("title") or "",
                    "hideType": shang.get("doc_type") or "",
                    "keepId": keep.get("doc_id") or keep.get("id"),
                    "keep_id": keep.get("doc_id") or keep.get("id"),
                    "keepType": keep.get("doc_type") or "",
                    "keep_type": keep.get("doc_type") or "",
                    "keepTitle": keep.get("title") or "",
                    "keep_title": keep.get("title") or "",
                    "common": f"日期相差 {min_diff} 天，原文高度重複（相似度 {round(sim * 100)}%）；共同片段：「{shared_snippet(shang_body, keep_body)}」。",
                    "diff": f"{shang.get('doc_id') or shang.get('id')} 是上奏；{keep.get('doc_id') or keep.get('id')} 是{keep.get('doc_type') or ''}。標題不同，但正文近似，可保留 {keep.get('doc_id') or keep.get('id')} 作為主要顯示點。",
                })

    if args.bundle:
        out_root = ROOT / "outputs" / "review-bundles" / args.bundle
        out_dir = out_root / "outputs"
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_root / "human-edits").mkdir(parents=True, exist_ok=True)
        bundle_doc_id = pairs[0]["doc_id"] if pairs else ""
        payload = [{
            "doc_id": bundle_doc_id,
            "kind": "dedupe",
            "prompt": "隱藏重複上奏點",
            "items": pairs,
            "model": "local duplicate check",
        }]
        (out_dir / "local-dedupe.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        manifest = {
            "name": args.bundle,
            "created_at": datetime.now().isoformat(timespec="seconds"),
            "source": str(source.relative_to(ROOT)) if source.is_relative_to(ROOT) else str(source),
            "doc_ids": split_csv(args.doc_ids),
            "chain": ["local-dedupe"],
            "date_window": args.date_window,
            "sim_min": args.sim_min,
            "len_ratio_min": args.len_ratio_min,
            "pair_count": len(pairs),
        }
        (out_root / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (out_root / "human-edits" / "notes.json").write_text("[]\n", encoding="utf-8")
        print(f"Wrote bundle: {out_root.relative_to(ROOT)} ({len(pairs)} pairs)")
        print("Open the website and click: 資料 → 載入技能輸出")
        return

    if args.format == "json":
        text = json.dumps(pairs, ensure_ascii=False, indent=2) + "\n"
    else:
        out = []
        fields = ["date", "day_diff", "similarity", "length_ratio", "hide_id", "keep_id", "keep_type", "hide_title", "keep_title", "common"]
        writer = csv.DictWriter(sys.stdout if not args.output else out, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        if args.output:
            from io import StringIO
            buf = StringIO()
            writer = csv.DictWriter(buf, fieldnames=fields, delimiter="\t", extrasaction="ignore")
            writer.writeheader()
            writer.writerows(pairs)
            text = buf.getvalue()
        else:
            writer.writeheader()
            writer.writerows(pairs)
            return

    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"Wrote {len(pairs)} pairs to {args.output}")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
