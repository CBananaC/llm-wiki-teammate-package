#!/usr/bin/env python3
"""No-citation recall pairing: later documents that respond to an 上諭 WITHOUT
quoting it (相關上諭配對（無引文）).

The citation runner (tool/scripts py/run_yu_pairing.py) is high precision: it needs a
citation marker + a cited edict quotation + the author to be a named recipient.
This runner is the recall complement.  For one 上諭 it gathers later documents
whose send date falls after the cooling period, in the window
[issue + WINDOW_SKIP + 1, issue + WINDOW_SKIP +
WINDOW_SPAN] days (default: skip 10 days of transit, then search 30 days),
ACROSS ALL officials (no identity filter), rejects citation-bearing memorials,
and ranks the remaining candidates by
character-bigram overlap with the edict, and asks the model to judge each on two
axes: match_level (content relatedness) and reply_status (does it actually
answer/execute the edict).  See tool/skills md/yu-response-pairing-nocite.md.

Detection runs on the date-rich corpus (dual-timeline-data.json).  Output goes to
outputs/attempt-002/yu-pairing-nocite.json plus a website-loadable review bundle.

Examples:
  python3 "tool/scripts py/run_yu_pairing_nocite.py" --doc-id 天43 --dry-run
  python3 "tool/scripts py/run_yu_pairing_nocite.py" --proxy https://... --doc-id 天43
  python3 "tool/scripts py/run_yu_pairing_nocite.py" --proxy https://... --all
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
from http.client import RemoteDisconnected
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "outputs" / "attempt-002" / "dual-timeline-data.json"
PROMPT_PATH = ROOT / "tool" / "skills md" / "yu-response-pairing-nocite.md"
PROMPT_RE = re.compile(r"^##\s*Website Prompt[ \t]*\n(.*?)(?=\n##\s)", re.S | re.M)

# Reply window: skip the first WINDOW_SKIP days after issue (transit), then search
# the next WINDOW_SPAN days.  Candidate send-date lag must be in
# [WINDOW_SKIP + 1, WINDOW_SKIP + WINDOW_SPAN].
WINDOW_SKIP = 10
WINDOW_SPAN = 30
# How many top-overlap candidates per edict get sent to the model.
TOP_K = 8

# This pass is specifically for replies with no explicit 上諭／廷寄 citation.
# Citation-bearing memorials belong to run_yu_pairing.py and must not consume
# the short content-overlap shortlist here.  Scan the title as well as the body:
# several catalogue titles say 欽奉諭旨 even when the surviving body is damaged.
YU_CITATION_RE = re.compile(
    r"(?:欽奉上諭|奉到上諭|接奉上諭|奉上諭|奉聖諭|"
    r"欽奉諭旨|接奉諭旨|奉到諭旨|奉廷寄|承准廷寄|接准廷寄|"
    r"承准[^。\n]{0,40}字寄|(?:上諭|諭旨|廷寄)\s*[：:][「『]?)"
)


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


_PUNCT_RE = re.compile(r"[\s\W_]+")


def _norm(text):
    return _PUNCT_RE.sub("", text or "")


def bigram_overlap(a, b):
    """Fraction of the edict's character bigrams also present in the candidate."""
    sa, sb = _norm(a), _norm(b)
    if len(sa) < 2 or len(sb) < 2:
        return 0.0
    grams = {sa[i:i + 2] for i in range(len(sa) - 1)}
    if not grams:
        return 0.0
    hits = sum(1 for g in grams if g in sb)
    return round(hits / len(grams), 4)


def has_yu_citation(record):
    """True when a candidate explicitly cites/quotes an imperial order.

    Ignore the candidate's own trailing 硃批: that is the emperor's response to
    this memorial, not the memorial quoting a previous 上諭.
    """
    body = (record.get("body") or "").split("【硃批】", 1)[0]
    text = (record.get("title") or "") + "\n" + body
    return bool(YU_CITATION_RE.search(text))


def _reply_lag(reply, issue):
    """Reply send-date lag after the edict. Filter on the SEND date only: a reply
    is written after the edict has been received, so the memorial's own send date
    is what must fall in the window. Using the receipt/硃批 date would wrongly admit
    a memorial sent BEFORE the edict that was merely rescripted later."""
    lag = days_between(reply.get("sendAr"), issue)
    if lag is None or not (WINDOW_SKIP < lag <= WINDOW_SKIP + WINDOW_SPAN):
        return None
    return lag


def candidates_for(edict, records):
    """Forward, no-citation: given an 上諭, later docs in the window ranked by
    subject overlap, across ALL officials."""
    issue = edict_date(edict)
    edict_text = (edict.get("title") or "") + (edict.get("body") or "")
    scored = []
    for r in records:
        if r.get("type") == "shangyu":
            continue
        if r.get("id") == edict.get("id"):
            continue
        if has_yu_citation(r):
            continue
        lag = _reply_lag(r, issue)
        if lag is None:
            continue
        score = bigram_overlap(edict_text, (r.get("title") or "") + (r.get("body") or ""))
        if score <= 0:
            continue
        scored.append({
            "id": r["id"],
            "author": (r.get("author_name") or "").strip(),
            "sendAr": r.get("sendAr", ""),
            "recvAr": r.get("recvAr", ""),
            "lag_days": lag,
            "overlap": score,
            "body": r.get("body") or "",
            "title": r.get("title") or "",
        })
    scored.sort(key=lambda c: (-c["overlap"], c["lag_days"]))
    return scored[:TOP_K]


def candidate_block(edict, cands):
    lines = [
        "【本上諭】",
        f"doc_id：{edict.get('id', '')}",
        f"發布日：{edict.get('annAr') or edict.get('sendAr') or '未明'}"
        f"（{edict.get('annCh') or ''}）",
        f"受命官員：{'、'.join(n for n in (edict.get('recipients') or []) if n) or (edict.get('author_name') or '')}",
        f"標題：{edict.get('title', '')}",
        f"原文：\n{edict.get('body', '')}",
        "",
    ]
    for i, c in enumerate(cands, 1):
        lines += [
            f"【候選回應 {i}】",
            f"doc_id：{c['id']}",
            f"具奏官員：{c['author'] or '未明'}",
            f"上奏日：{c['sendAr'] or '未明'}",
            f"距上諭：{c['lag_days']} 日",
            f"主題重疊：{c['overlap']:.3f}",
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
        except (URLError, TimeoutError, RemoteDisconnected, ConnectionResetError) as exc:
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
        rid = str(p.get("reply_doc_id", "")).strip()
        if rid not in valid:
            continue
        pairs.append({
            "reply_doc_id": rid,
            "yu_doc_id": edict_id,
            "relation": "official_reply_to_yu",
            "no_citation": True,
            "match_level": p.get("match_level", "weak"),
            "reply_status": p.get("reply_status", "ack"),
            "evidence": p.get("evidence", {}),
        })
    return pairs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--proxy", default=os.environ.get("GEMINI_PROXY_URL", ""))
    ap.add_argument("--doc-id", help="One or more 上諭 ids (comma-separated).")
    ap.add_argument("--all", action="store_true", help="Every 上諭 (forward).")
    ap.add_argument("--model", default="gemini-3.5-flash")
    ap.add_argument("--workers", type=int, default=8,
                    help="Concurrent proxy calls (default 8). Use 1 for serial.")
    ap.add_argument("--skip-done", action="store_true",
                    help="Skip 上諭 already present in the existing output and merge.")
    ap.add_argument("--dry-run", action="store_true", help="Show candidates; no proxy call.")
    ap.add_argument("--include-weak", action="store_true",
                    help="Keep weak (incidental-overlap) pairs too; default drops them.")
    ap.add_argument("--include-unrelated", action="store_true",
                    help="Keep pairs the model judged reply_status=unrelated; default drops them.")
    ap.add_argument("--bundle-name", default="yu-pairing-nocite")
    args = ap.parse_args()

    records = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    by_id = {r.get("id"): r for r in records}

    out_path = ROOT / "outputs" / "attempt-002" / "yu-pairing-nocite.json"
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
            print(f"\n== 上諭 {edict['id']} ({edict_date(edict)}) "
                  f"窗 +{WINDOW_SKIP + 1}~+{WINDOW_SKIP + WINDOW_SPAN}日 ==")
            for c in cands:
                print(f"  {c['id']:>6}  {c['author']:<6} {c['sendAr']}  +{c['lag_days']}d  "
                      f"overlap={c['overlap']:.3f}")
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
            print(f"  ! proxy failed for 上諭 {edict['id']} after retries: {exc} — skipping",
                  file=sys.stderr)
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
            futures = {pool.submit(_run_job, edict, cands): edict
                       for edict, cands in proxy_jobs}
            for done, fut in enumerate(as_completed(futures), 1):
                edict = futures[fut]
                print(f"  [{done}/{total}] 上諭 {edict['id']}", file=sys.stderr)
                all_pairs.extend(fut.result())

    kept = all_pairs
    if not args.include_weak:
        kept = [p for p in kept if p.get("match_level") != "weak"]
    if not args.include_unrelated:
        kept = [p for p in kept if p.get("reply_status") != "unrelated"]
    dropped = len(all_pairs) - len(kept)

    seen, deduped = set(), []
    for p in existing_pairs + kept:
        key = (p["reply_doc_id"], p["yu_doc_id"])
        if key not in seen:
            seen.add(key)
            deduped.append(p)

    analyzed = sorted(set(existing_analyzed) | {a for a in run_analyzed if a})
    result = {"pairs": deduped, "analyzed": analyzed}
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    bundle_root = ROOT / "outputs" / "review-bundles" / args.bundle_name
    (bundle_root / "outputs").mkdir(parents=True, exist_ok=True)
    (bundle_root / "outputs" / "yu-pairing-nocite.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (bundle_root / "manifest.json").write_text(json.dumps({
        "name": args.bundle_name,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "source": "outputs/attempt-002/dual-timeline-data.json",
        "doc_ids": sorted({p["yu_doc_id"] for p in deduped} | {p["reply_doc_id"] for p in deduped}),
        "chain": ["yu-pairing-nocite"],
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(out_path)
    print(bundle_root)
    print(f"pairs: {len(deduped)} (dropped {dropped} weak/unrelated; "
          f"use --include-weak / --include-unrelated to keep)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
