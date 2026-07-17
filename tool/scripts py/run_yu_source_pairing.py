#!/usr/bin/env python3
"""上諭來源（據奏）配對 — find the earlier 奏摺 a 上諭 is drawing on (backward edge).

For one 上諭 (issue date = its announce date), extract every 據…奏 fragment, take
candidate 奏摺 the court RECEIVED in [issue - SOURCE_BACK, issue] days whose author
is named in a 據…奏 fragment, and ask the model which candidate is the source it
cites (author matches the throne-memorialist X AND reports the same information).
See tool/skills md/yu-source-pairing.md.

Output: outputs/attempt-002/yu-source.json plus a review bundle. Pairs use the
shared docpair shape with relation "yu_source".

Examples:
  python3 "tool/scripts py/run_yu_source_pairing.py" --doc-id 諭13 --dry-run
  python3 "tool/scripts py/run_yu_source_pairing.py" --proxy https://... --doc-id 諭13
  python3 "tool/scripts py/run_yu_source_pairing.py" --proxy https://... --all
"""

from __future__ import annotations

import argparse
import calendar
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "outputs" / "attempt-002" / "dual-timeline-data.json"
PROMPT_PATH = ROOT / "tool" / "skills md" / "yu-source-pairing.md"
PROMPT_RE = re.compile(r"^##\s*Website Prompt[ \t]*\n(.*?)(?=\n##\s)", re.S | re.M)

# Receipt window: a source 奏摺 was received on the issue day or up to SOURCE_BACK
# days before it.
SOURCE_BACK = 5
TOP_K = 8


def parse_date(value):
    try:
        return datetime.strptime(value or "", "%Y/%m/%d")
    except (ValueError, TypeError):
        if not isinstance(value, str):
            return None
        m = re.fullmatch(r"(\d{4})/(\d{2})/(\d{2})", value)
        if not m:
            return None
        year, month, day = map(int, m.groups())
        if day != 29 or month != 2:
            return None
        return datetime(year, month, calendar.monthrange(year, month)[1])


def days_between(later, earlier):
    a, b = parse_date(later), parse_date(earlier)
    return (a - b).days if a and b else None


def website_prompt():
    m = PROMPT_RE.search(PROMPT_PATH.read_text(encoding="utf-8"))
    if not m:
        raise RuntimeError(f"No Website Prompt in {PROMPT_PATH}")
    return m.group(1).strip()


def edict_date(edict):
    return edict.get("annAr") or edict.get("sendAr")


def ju_spans(body, reach=48):
    """Every 據…奏 fragment: from a 據 up to the next 奏 (bounded)."""
    text = body or ""
    out, i = [], 0
    while True:
        i = text.find("據", i)
        if i < 0:
            break
        seg = text[i:i + reach]
        k = seg.find("奏")
        if k >= 0:
            out.append(seg[:k + 1])
        i += 1
    return out


def source_lag(reply, issue):
    """issue - receipt (recvAr, fallback sendAr); must be in [0, SOURCE_BACK]."""
    for field in ("recvAr", "sendAr"):
        lag = days_between(issue, reply.get(field))  # issue - field
        if lag is not None:
            if 0 <= lag <= SOURCE_BACK:
                return lag
            return None
    return None


def candidates_for(edict, records):
    issue = edict_date(edict)
    spans = ju_spans(edict.get("body") or "")
    if not spans:
        return []
    scored = []
    for r in records:
        if r.get("type") == "shangyu" or r.get("id") == edict.get("id"):
            continue
        lag = source_lag(r, issue)
        if lag is None:
            continue
        author = (r.get("author_name") or "").strip()
        if not author or not any(author in sp for sp in spans):
            continue
        scored.append({
            "id": r["id"],
            "author": author,
            "sendAr": r.get("sendAr", ""),
            "recvAr": r.get("recvAr", ""),
            "lag_days": lag,
            "body": r.get("body") or "",
            "title": r.get("title") or "",
        })
    scored.sort(key=lambda c: c["lag_days"])  # nearest to issue first
    return scored[:TOP_K]


def candidate_block(edict, cands):
    spans = ju_spans(edict.get("body") or "")
    lines = [
        "【本上諭】",
        f"doc_id：{edict.get('id', '')}",
        f"發布日：{edict.get('annAr') or edict.get('sendAr') or '未明'}（{edict.get('annCh') or ''}）",
        f"受命官員：{'、'.join(n for n in (edict.get('recipients') or []) if n) or (edict.get('author_name') or '')}",
        f"標題：{edict.get('title', '')}",
        f"原文：\n{edict.get('body', '')}",
        "",
        "偵測到的據…奏片段：",
        *[f"・{s}" for s in spans[:8]],
        "",
    ]
    for i, c in enumerate(cands, 1):
        lines += [
            f"【候選來源奏摺 {i}】",
            f"doc_id：{c['id']}",
            f"具奏官員：{c['author']}",
            f"上奏日：{c['sendAr'] or '未明'}",
            f"收到／硃批日：{c['recvAr'] or '未明'}",
            f"距上諭：{c['lag_days']} 日前收到",
            f"原文：\n{c['body']}",
            "",
        ]
    return "\n".join(lines)


_RETRY_CODES = {429, 500, 502, 503, 504}


def call_proxy(proxy, payload, retries=4, backoff=3):
    req = Request(
        proxy.rstrip("/") + "/chat",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    last = None
    for attempt in range(retries):
        try:
            with urlopen(req, timeout=180) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except HTTPError as exc:
            last = exc
            if exc.code in _RETRY_CODES and attempt < retries - 1:
                time.sleep(backoff * (attempt + 1))
                continue
            raise
        except (URLError, TimeoutError) as exc:
            last = exc
            if attempt < retries - 1:
                time.sleep(backoff * (attempt + 1))
                continue
            raise
    raise last


def repair_json(text):
    s = (text or "").strip()
    if s.startswith("```"):
        s = s.split("\n", 1)[1] if "\n" in s else s
        if s.rstrip().endswith("```"):
            s = s.rstrip()[:-3]
    a, b = s.find("{"), s.rfind("}")
    return s[a:b + 1] if a >= 0 and b > a else s


def parse_pairs(model_response, edict_id, cands):
    text = model_response.get("text") if isinstance(model_response, dict) else model_response
    obj = None
    for cand in (text, repair_json(text or "")):
        try:
            obj = json.loads(cand)
            break
        except (json.JSONDecodeError, TypeError):
            continue
    if not isinstance(obj, dict):
        return []
    valid = {c["id"] for c in cands}
    pairs = []
    for p in obj.get("pairs", []):
        sid = str(p.get("source_doc_id", p.get("reply_doc_id", ""))).strip()
        if sid not in valid:
            continue
        pairs.append({
            "yu_doc_id": edict_id,
            "reply_doc_id": sid,
            "relation": "yu_source",
            "match_level": p.get("match_level", "weak"),
            "evidence": p.get("evidence", {}),
        })
    return pairs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--proxy", default=os.environ.get("GEMINI_PROXY_URL", ""))
    ap.add_argument("--doc-id", help="One or more 上諭 ids (comma-separated).")
    ap.add_argument("--all", action="store_true", help="Every 上諭.")
    ap.add_argument("--model", default="gemini-3.5-flash")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--skip-done", action="store_true",
                    help="Skip 上諭 already present in the existing output and merge.")
    ap.add_argument("--dry-run", action="store_true", help="Show candidates; no proxy call.")
    ap.add_argument("--include-weak", action="store_true",
                    help="Keep weak pairs too; default drops them.")
    ap.add_argument("--bundle-name", default="yu-source")
    args = ap.parse_args()

    records = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    by_id = {r.get("id"): r for r in records}

    out_path = ROOT / "outputs" / "attempt-002" / "yu-source.json"
    existing_pairs, existing_analyzed, done_ids = [], [], set()
    if args.skip_done and out_path.exists():
        prev = json.loads(out_path.read_text(encoding="utf-8"))
        if isinstance(prev, dict):
            existing_pairs, existing_analyzed = prev.get("pairs", []), prev.get("analyzed", [])
        else:
            existing_pairs = prev
        done_ids = {p.get("yu_doc_id") for p in existing_pairs}

    if args.doc_id:
        anchors = []
        for one in (x.strip() for x in args.doc_id.split(",") if x.strip()):
            rec = by_id.get(one)
            if not rec:
                ap.error(f"document not found: {one}")
            if rec.get("type") != "shangyu":
                ap.error(f"not an 上諭 (this pass is 上諭-anchored): {one}")
            anchors.append(rec)
    elif args.all:
        anchors = [r for r in records if r.get("type") == "shangyu"]
    else:
        ap.error("Pass --doc-id or --all.")

    if args.skip_done:
        anchors = [a for a in anchors if a.get("id") not in done_ids]

    run_analyzed = [a.get("id") for a in anchors]
    jobs = [(edict, candidates_for(edict, records)) for edict in anchors]

    if args.dry_run:
        for edict, cands in jobs:
            print(f"\n== 上諭 {edict['id']} ({edict_date(edict)}) 來源窗 [issue-{SOURCE_BACK}, issue] ==")
            for s in ju_spans(edict.get("body") or "")[:8]:
                print(f"   據奏: {s}")
            for c in cands:
                print(f"  {c['id']:>6}  {c['author']:<6} recv={c['recvAr']}  -{c['lag_days']}d")
        return 0

    proxy_jobs = [(edict, cands) for edict, cands in jobs if cands]
    if proxy_jobs and not args.proxy:
        ap.error("Set GEMINI_PROXY_URL or pass --proxy (or use --dry-run).")

    prompt_text = website_prompt()

    def _run_job(edict, cands):
        payload = {
            "mode": "ask",
            "model": args.model,
            "doc_id": edict["id"],
            "doc_type": edict.get("doc_type", "上諭"),
            "title": edict.get("title", ""),
            "body": candidate_block(edict, cands),
            "question": prompt_text,
        }
        try:
            result = call_proxy(args.proxy, payload)
        except Exception as exc:
            print(f"  ! proxy failed for 上諭 {edict['id']}: {exc} — skipping", file=sys.stderr)
            return []
        return parse_pairs(result, edict["id"], cands)

    all_pairs = []
    total = len(proxy_jobs)
    workers = max(1, args.workers)
    if workers == 1 or total <= 1:
        for done, (edict, cands) in enumerate(proxy_jobs, 1):
            print(f"  [{done}/{total}] 上諭 {edict['id']}", file=sys.stderr)
            all_pairs.extend(_run_job(edict, cands))
    else:
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {pool.submit(_run_job, edict, cands): edict for edict, cands in proxy_jobs}
            for done, fut in enumerate(as_completed(futures), 1):
                edict = futures[fut]
                print(f"  [{done}/{total}] 上諭 {edict['id']}", file=sys.stderr)
                all_pairs.extend(fut.result())

    kept = all_pairs if args.include_weak else [p for p in all_pairs if p.get("match_level") != "weak"]
    dropped = len(all_pairs) - len(kept)

    seen, deduped = set(), []
    for p in existing_pairs + kept:
        key = (p["yu_doc_id"], p["reply_doc_id"])
        if key not in seen:
            seen.add(key)
            deduped.append(p)

    analyzed = sorted(set(existing_analyzed) | {a for a in run_analyzed if a})
    result = {"pairs": deduped, "analyzed": analyzed}
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    bundle_root = ROOT / "outputs" / "review-bundles" / args.bundle_name
    (bundle_root / "outputs").mkdir(parents=True, exist_ok=True)
    (bundle_root / "outputs" / "yu-source.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (bundle_root / "manifest.json").write_text(json.dumps({
        "name": args.bundle_name,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "source": "outputs/attempt-002/dual-timeline-data.json",
        "doc_ids": sorted({p["yu_doc_id"] for p in deduped} | {p["reply_doc_id"] for p in deduped}),
        "chain": ["yu-source"],
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(out_path)
    print(bundle_root)
    print(f"pairs: {len(deduped)} (dropped {dropped} weak; use --include-weak to keep)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
