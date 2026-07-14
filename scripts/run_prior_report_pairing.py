#!/usr/bin/env python3
"""Pair later `…在案` references with the official's earlier memorial.

Examples:
  python3 scripts/run_prior_report_pairing.py --doc-id 台171 --dry-run
  python3 scripts/run_prior_report_pairing.py --all --structural-only
  python3 scripts/run_prior_report_pairing.py --reverse-month 1787/02 --dry-run
  python3 scripts/run_prior_report_pairing.py --proxy https://... --all
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "outputs" / "attempt-002" / "dual-timeline-data.json"
PROMPT_PATH = ROOT / "skills" / "prior-report-pairing.md"
OUT_PATH = ROOT / "outputs" / "attempt-002" / "prior-report-pairing.json"
PROMPT_RE = re.compile(r"^##\s*Website Prompt[ \t]*\n(.*?)(?=\n##\s)", re.S | re.M)
MAX_WINDOW_DAYS = 240
MAX_FALLBACK_CANDIDATES = 24

CN_DATE_RE = re.compile(
    r"(?:乾隆[元一二三四五六七八九十]+年)?(?:上年|本年|去年)?"
    r"[正臘閏元一二三四五六七八九十]{1,3}月"
    r"[初一二三四五六七八九十廿卅]{1,3}日"
)
REPORT_WORD_RE = re.compile(r"奏|摺|片|奏報|奏明|奏聞|具奏|附摺|附片|聲明")
PUNCT_RE = re.compile(r"[。，、；：！？「」『』（）〈〉【】〔〕\s]")


def parse_date(value):
    try:
        return datetime.strptime(value or "", "%Y/%m/%d")
    except (ValueError, TypeError):
        return None


def days_between(later, earlier):
    a, b = parse_date(later), parse_date(earlier)
    return (a - b).days if a and b else None


def same_author(a, b):
    clean = lambda s: (s or "").replace("（等）", "").replace("等", "").strip()
    a, b = clean(a), clean(b)
    return bool(a and b and (a in b or b in a))


def month_day_variants(value):
    m = re.search(
        r"([正臘閏元一二三四五六七八九十]{1,3})月"
        r"([初一二三四五六七八九十廿卅]{1,3})日", value or "")
    if not m:
        return set()
    months = {m.group(1)}
    if m.group(1) in {"正", "一", "元"}:
        months |= {"正", "一", "元"}
    return {f"{month}月{m.group(2)}日" for month in months}


def cited_date_matches(value, candidate):
    return any(v in (candidate.get("sendCh") or "") for v in month_day_variants(value))


def normalise(text):
    return PUNCT_RE.sub("", text or "")


def report_similarity(reference, candidate):
    """Bigram coverage for ranking, plus an exact shared original-text span."""
    ref = normalise(reference)
    raw_body = (candidate.get("title") or "") + (candidate.get("body") or "")
    body = normalise(raw_body)
    if len(ref) < 6 or len(body) < 6:
        return 0.0, ""
    grams = {ref[i:i + 2] for i in range(len(ref) - 1)}
    score = sum(g in body for g in grams) / max(len(grams), 1)
    # The card needs a verbatim clickable span, not punctuation-free text.
    raw_match = SequenceMatcher(None, reference, raw_body, autojunk=False).find_longest_match()
    span = raw_body[raw_match.b:raw_match.b + raw_match.size].strip()
    return round(score, 4), span


def report_references(body):
    """Return report-like context windows ending at each `在案` occurrence."""
    text = body or ""
    out, seen = [], set()
    for m in re.finditer("在案", text):
        lo = max(0, m.start() - 230)
        lead = text[lo:m.start()]
        # Start after the nearest strong sentence boundary, but retain enough
        # preceding clauses for multi-part summaries such as the 台171 troop list.
        boundaries = [lead.rfind(ch) for ch in "。！？\n"]
        cut = max(boundaries)
        if cut >= 0 and len(lead) - cut > 55:
            lo += cut + 1
            lead = text[lo:m.start()]
        if not REPORT_WORD_RE.search(lead[-100:]):
            continue
        passage = text[lo:m.end()].strip(" \n，。；")
        dates = [x.group(0) for x in CN_DATE_RE.finditer(passage)]
        key = normalise(passage)[-80:]
        if not key or key in seen:
            continue
        seen.add(key)
        out.append({
            "marker": "在案",
            "passage": passage,
            "cited_dates": dates,
            "cited_date": dates[-1] if dates else "",
        })
    return out


def candidates_for(later, records):
    refs = report_references(later.get("body"))
    if not refs:
        return [], refs
    scored = []
    for previous in records:
        if previous.get("type") == "shangyu" or previous.get("id") == later.get("id"):
            continue
        if not same_author(later.get("author_name"), previous.get("author_name")):
            continue
        lag = days_between(later.get("sendAr"), previous.get("sendAr"))
        if lag is None or lag <= 0 or lag > MAX_WINDOW_DAYS:
            continue
        date_hit = any(cited_date_matches(d, previous) for ref in refs for d in ref["cited_dates"])
        best_score, best_span, best_ref = 0.0, "", refs[0]
        for ref in refs:
            score, span = report_similarity(ref["passage"], previous)
            if score > best_score:
                best_score, best_span, best_ref = score, span, ref
        scored.append({
            "id": previous["id"],
            "author": previous.get("author_name", ""),
            "title": previous.get("title", ""),
            "sendAr": previous.get("sendAr", ""),
            "sendCh": previous.get("sendCh", ""),
            "body": previous.get("body", ""),
            "lag_days": lag,
            "date_hit": date_hit,
            "text_score": best_score,
            "shared_span": best_span,
            "reference": best_ref["passage"],
            "cited_date": best_ref.get("cited_date", ""),
        })
    scored.sort(key=lambda c: (not c["date_hit"], -c["text_score"], c["lag_days"]))
    exact = [c for c in scored if c["date_hit"]]
    fallback = [c for c in scored if not c["date_hit"]][:MAX_FALLBACK_CANDIDATES]
    return exact + fallback, refs


def website_prompt():
    m = PROMPT_RE.search(PROMPT_PATH.read_text(encoding="utf-8"))
    if not m:
        raise RuntimeError(f"No Website Prompt in {PROMPT_PATH}")
    return m.group(1).strip()


def prompt_block(later, refs, candidates):
    lines = [
        "【本次奏報】",
        f"doc_id：{later.get('id', '')}",
        f"具奏官員：{later.get('author_name', '')}",
        f"上奏日：{later.get('sendAr') or '未明'}（{later.get('sendCh') or ''}）",
        f"標題：{later.get('title', '')}",
        "偵測到的在案段落：",
    ]
    lines += [f"---\n{r['passage']}" for r in refs]
    lines.append("")
    for i, c in enumerate(candidates, 1):
        flags = []
        if c["date_hit"]:
            flags.append("所奏日期相符")
        if c["text_score"]:
            flags.append(f"原文相似 {c['text_score']}")
        lines += [
            f"【候選前奏 {i}】",
            f"doc_id：{c['id']}",
            f"具奏官員：{c['author']}",
            f"上奏日：{c['sendAr'] or '未明'}（{c['sendCh']}）",
            f"標題：{c['title']}",
            "結構線索：" + ("、".join(flags) or "同官、日期範圍內"),
            "原文：",
            c["body"],
            "",
        ]
    return "\n".join(lines)


RETRY_CODES = {429, 500, 502, 503, 504}


def call_proxy(proxy, payload, retries=4):
    req = Request(proxy.rstrip("/") + "/chat",
                  data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
                  headers={"Content-Type": "application/json"}, method="POST")
    for attempt in range(retries):
        try:
            with urlopen(req, timeout=180) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except HTTPError as exc:
            if exc.code not in RETRY_CODES or attempt == retries - 1:
                raise
        except (URLError, TimeoutError):
            if attempt == retries - 1:
                raise
        time.sleep(3 * (attempt + 1))


def parse_pairs(result, later_id, candidates):
    text = result.get("text") if isinstance(result, dict) else result
    text = text or ""
    if text.strip().startswith("```"):
        text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip())
    try:
        obj = json.loads(text)
    except (json.JSONDecodeError, TypeError):
        a, b = text.find("{"), text.rfind("}")
        try:
            obj = json.loads(text[a:b + 1])
        except (json.JSONDecodeError, TypeError):
            return []
    valid = {c["id"] for c in candidates}
    pairs = []
    for p in obj.get("pairs", []):
        previous_id = str(p.get("previous_doc_id", "")).strip()
        if previous_id not in valid:
            continue
        pairs.append({
            "previous_doc_id": previous_id,
            "yu_doc_id": previous_id,
            "reply_doc_id": later_id,
            "relation": "prior_report",
            "match_level": p.get("match_level", "weak"),
            "evidence": p.get("evidence", {}),
        })
    return pairs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--proxy", default=os.environ.get("GEMINI_PROXY_URL", ""))
    ap.add_argument("--doc-id", help="Analyse one or several comma-separated later documents.")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--reverse-month", "--month", dest="month", metavar="YYYY/MM")
    ap.add_argument("--skip-done", action="store_true")
    ap.add_argument("--model", default="gemini-3.5-flash")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--structural-only", action="store_true",
                    help="Write conservative review suggestions without calling the AI proxy.")
    ap.add_argument("--include-weak", action="store_true")
    ap.add_argument("--bundle-name", default="prior-report-pairing")
    args = ap.parse_args()

    records = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    by_id = {r.get("id"): r for r in records}
    if args.doc_id:
        anchors = []
        for doc_id in (x.strip() for x in args.doc_id.split(",") if x.strip()):
            if doc_id not in by_id:
                ap.error(f"document not found: {doc_id}")
            anchors.append(by_id[doc_id])
    elif args.all:
        anchors = [r for r in records if r.get("type") != "shangyu"]
    elif args.month:
        anchors = [r for r in records if r.get("type") != "shangyu"
                   and (r.get("sendAr") or "").startswith(args.month)]
    else:
        ap.error("Pass --doc-id, --all, or --reverse-month YYYY/MM.")

    existing_pairs, existing_analyzed = [], []
    if args.skip_done and OUT_PATH.exists():
        old = json.loads(OUT_PATH.read_text(encoding="utf-8"))
        existing_pairs, existing_analyzed = old.get("pairs", []), old.get("analyzed", [])
        done = set(existing_analyzed)
        anchors = [r for r in anchors if r.get("id") not in done]

    prompt = website_prompt()
    found = []
    analyzed = [r.get("id") for r in anchors]
    for later in anchors:
        candidates, refs = candidates_for(later, records)
        if not refs or not candidates:
            continue
        if args.dry_run:
            print(f"\n== {later['id']} {later.get('author_name','')} {later.get('sendAr','')} ==")
            for ref in refs:
                print(f"   在案：{ref['passage']}")
            for c in candidates:
                print(f"   候選 {c['id']:>6} {c['sendAr']} -{c['lag_days']}d "
                      f"{'★日期符 ' if c['date_hit'] else ''}原文{c['text_score']} {c['title']}")
            continue
        if args.structural_only:
            dated = [c for c in candidates if c["date_hit"]]
            undated = [c for c in candidates if not c["date_hit"]]
            selected = []
            if dated:
                top = dated[0]["text_score"]
                floor = max(0.18, top * 0.65) if top >= 0.22 else top
                selected = [c for c in dated if c["text_score"] >= floor]
            elif undated and undated[0]["text_score"] >= 0.42:
                top = undated[0]["text_score"]
                selected = [c for c in undated if c["text_score"] >= max(0.42, top * 0.8)]
            for c in selected:
                level = "high" if c["date_hit"] and c["text_score"] >= 0.30 else "partial"
                found.append({
                    "previous_doc_id": c["id"], "yu_doc_id": c["id"],
                    "reply_doc_id": later["id"], "relation": "prior_report",
                    "match_level": level,
                    "evidence": {
                        "marker": "在案",
                        "reference_in_later_doc": c["reference"],
                        "previous_report_date": c.get("cited_date") or "未明",
                        "previous_report_summary": c["reference"],
                        "matched_previous_span": c.get("shared_span", ""),
                        "matched_later_span": c["reference"],
                        "date_note": ("前奏上奏日與在案段落所引日期相符。"
                                      if c["date_hit"] else "未見可用前奏日期；依原文內容相似度配對。"),
                        "structural_score": c["text_score"],
                    },
                })
            continue
        if not args.proxy:
            ap.error("Set GEMINI_PROXY_URL or pass --proxy (or use --dry-run).")
        payload = {"mode": "ask", "model": args.model, "doc_id": later["id"],
                   "doc_type": later.get("doc_type", "奏摺"),
                   "title": later.get("title", ""),
                   "body": prompt_block(later, refs, candidates), "question": prompt}
        try:
            found.extend(parse_pairs(call_proxy(args.proxy, payload), later["id"], candidates))
        except Exception as exc:
            print(f"  ! proxy failed for {later['id']}: {exc}", file=sys.stderr)

    if args.dry_run:
        return 0
    if not args.include_weak:
        found = [p for p in found if p.get("match_level") != "weak"]
    deduped, seen = [], set()
    for p in existing_pairs + found:
        key = (p.get("reply_doc_id"), p.get("previous_doc_id") or p.get("yu_doc_id"))
        if key not in seen:
            seen.add(key)
            deduped.append(p)
    result = {"pairs": deduped, "analyzed": sorted(set(existing_analyzed + analyzed))}
    OUT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    bundle = ROOT / "outputs" / "review-bundles" / args.bundle_name
    (bundle / "outputs").mkdir(parents=True, exist_ok=True)
    (bundle / "outputs" / "prior-report-pairing.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (bundle / "manifest.json").write_text(json.dumps({
        "name": args.bundle_name,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "source": "outputs/attempt-002/dual-timeline-data.json",
        "doc_ids": sorted({str(x) for p in deduped for x in
                           (p.get("previous_doc_id") or p.get("yu_doc_id"), p.get("reply_doc_id")) if x}),
        "chain": ["prior-report-pairing"],
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT_PATH)
    print(bundle)
    print(f"pairs: {len(deduped)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
