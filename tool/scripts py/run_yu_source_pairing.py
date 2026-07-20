#!/usr/bin/env python3
"""上諭來源配對 — trace both cited and unlabelled narrative sources.

The runner keeps the five-day receipt window fixed while building three
candidate classes: named `據…奏` sources, `據X等奏` corroborating co-reporters,
and bounded content-ranked window candidates for unlabelled narrative facts. See
``tool/skills md/yu-source-pairing.md``.

Output: the formal ``review-tools/(1) formal/yu-source.json`` plus a shared
review bundle. Pairs use relation ``yu_source``.
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
DATA_PATH = ROOT / "review-tools" / "shared data" / "stage1_original_text.json"
PROMPT_PATH = ROOT / "tool" / "skills md" / "yu-source-pairing.md"
PROMPT_RE = re.compile(r"^##\s*Website Prompt[ \t]*\n(.*?)(?=\n##\s)", re.S | re.M)
RECALL_PROMPT_RE = re.compile(
    r"^##\s*Completeness Audit Prompt[ \t]*\n(.*?)(?=\n##\s|\Z)",
    re.S | re.M,
)

# Receipt window: a source 奏摺 was received on the issue day or up to SOURCE_BACK
# days before it. The same window is used for all candidate classes.
SOURCE_BACK = 5
CORROB_MIN_OVERLAP = 0.12
TOP_K_WINDOW = 6
WINDOW_MIN_OVERLAP = 0.08
ET_AL_RE = re.compile(r"等[^奏]{0,4}奏$")


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


def completeness_audit_prompt():
    m = RECALL_PROMPT_RE.search(PROMPT_PATH.read_text(encoding="utf-8"))
    if not m:
        raise RuntimeError(f"No Completeness Audit Prompt in {PROMPT_PATH}")
    return m.group(1).strip()


def edict_date(edict):
    return edict.get("annAr") or edict.get("sendAr")


def _date_value(value):
    """Read either the reorganized source's [Chinese, Arabic] date or an old string."""
    if isinstance(value, list):
        return value[-1] if value else ""
    return value or ""


def normalize_record(raw):
    """Normalize stage1_original_text.json records to the runner's timeline shape."""
    raw = dict(raw or {})
    doc_type = raw.get("doc_type") or raw.get("type") or ""
    kind = raw.get("type")
    if not kind:
        kind = "shangyu" if doc_type == "上諭" else "official"
    author = raw.get("author")
    if isinstance(author, dict):
        author_name = author.get("name") or ""
    else:
        author_name = raw.get("author_name") or author or ""
    return {
        **raw,
        "id": raw.get("id") or raw.get("doc_id") or "",
        "doc_type": doc_type,
        "type": kind,
        "author_name": author_name,
        "sendAr": _date_value(raw.get("sendAr") or raw.get("send_date")),
        "recvAr": _date_value(raw.get("recvAr") or raw.get("receive_date")),
        "annAr": _date_value(
            raw.get("annAr") or raw.get("announce_date") or raw.get("issue_date")
        ),
        "rescript": raw.get("rescript") or raw.get("rescript_text") or "",
        "body": raw.get("body") or "",
        "title": raw.get("title") or "",
    }


def load_records():
    """Load canonical text, falling back to the formal page's normalized metadata.

    The shared Stage 1 file intentionally preserves original text and may leave
    some date metadata null. The formal HTML already contains the derived
    timeline metadata used by the review UI, so use it only when the shared
    records cannot provide an issue date for any 上諭.
    """
    records = [normalize_record(r) for r in json.loads(DATA_PATH.read_text(encoding="utf-8"))]
    shangyu = [r for r in records if r.get("type") == "shangyu"]
    if shangyu and all(edict_date(r) for r in shangyu):
        return records
    html_path = ROOT / "review-tools" / "(1) formal" / "index.html"
    text = html_path.read_text(encoding="utf-8")
    match = re.search(r"const DUAL = (\[.*?\]);\s*const TYPE_LABEL", text, re.S)
    if not match:
        raise RuntimeError(f"No normalized timeline metadata found in {html_path}")
    return [normalize_record(r) for r in json.loads(match.group(1))]


def ju_spans_with_pos(body, reach=48):
    """Every 據…奏 fragment as (text, start position)."""
    text = body or ""
    out, i = [], 0
    while True:
        i = text.find("據", i)
        if i < 0:
            break
        seg = text[i:i + reach]
        k = seg.find("奏")
        if k >= 0:
            out.append((seg[:k + 1], i))
        i += 1
    return out


def ju_spans(body, reach=48):
    return [s for s, _ in ju_spans_with_pos(body, reach)]


def has_et_al(span):
    return bool(ET_AL_RE.search(span or ""))


def report_clause(body, pos, reach=220):
    """Expand an 等奏 citation to the end of its relayed report."""
    window = (body or "")[pos:pos + reach]
    m = re.search(r"等語", window)
    if m:
        return window[:m.end()]
    m = re.search(r"據", window[1:])
    return window[:m.start() + 1] if m else window


def _norm_cjk(text):
    return re.sub(r"[。，、；：！？「」『』（）〈〉【】〔〕\s]", "", text or "")


def bigram_overlap(a, b):
    a, b = _norm_cjk(a), _norm_cjk(b)
    if len(a) < 2 or len(b) < 2:
        return 0.0
    grams = {a[i:i + 2] for i in range(len(a) - 1)}
    return sum(1 for g in grams if g in b) / len(grams)


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
    """Build named, corroborating, and narrative candidate classes."""
    issue = edict_date(edict)
    body = edict.get("body") or ""
    spans = ju_spans_with_pos(body)
    window_pool = []
    for r in records:
        if r.get("type") == "shangyu" or r.get("id") == edict.get("id"):
            continue
        lag = source_lag(r, issue)
        if lag is None:
            continue
        window_pool.append((r, lag))
    if not window_pool:
        return []

    named, corroborating = {}, {}
    for span, pos in spans:
        et_al = has_et_al(span)
        clause = report_clause(body, pos) if et_al else span
        for r, lag in window_pool:
            author = (r.get("author_name") or "").strip()
            if author and author in span:
                entry = named.setdefault(r["id"], {"r": r, "lag": lag})
                entry["lag"] = min(entry["lag"], lag)
            elif et_al:
                score = bigram_overlap(clause, (r.get("title") or "") + (r.get("body") or ""))
                if score >= CORROB_MIN_OVERLAP:
                    entry = corroborating.setdefault(r["id"], {"r": r, "lag": lag, "score": score})
                    entry["lag"] = min(entry["lag"], lag)
                    entry["score"] = max(entry["score"], score)

    def build(entry, basis):
        r = entry["r"]
        return {
            "id": r["id"], "author": (r.get("author_name") or "").strip(),
            "sendAr": r.get("sendAr", ""), "recvAr": r.get("recvAr", ""),
            "lag_days": entry["lag"], "body": r.get("body") or "",
            "title": r.get("title") or "", "match_basis": basis,
        }

    # Do not truncate named sources: the completeness pass must be able to
    # compare every same-window memorial by an author explicitly named in the
    # edict, including an earlier direct memorial and a later relay.
    primary = sorted((build(x, "named") for x in named.values()),
                     key=lambda c: c["lag_days"])
    have = {c["id"] for c in primary}
    # Corroborating candidates are also source candidates, not broad narrative
    # matches. Keep all of them within the same five-day window.
    corr = sorted(((rid, x) for rid, x in corroborating.items() if rid not in have),
                  key=lambda item: (-item[1]["score"], item[1]["lag"]))
    secondary = [build(x, "corroborating") for _, x in corr]
    have.update(c["id"] for c in secondary)

    edtext = (edict.get("title") or "") + body
    ranked = []
    for r, lag in window_pool:
        if r["id"] in have:
            continue
        score = bigram_overlap(edtext, (r.get("title") or "") + (r.get("body") or ""))
        if score >= WINDOW_MIN_OVERLAP:
            ranked.append((score, lag, r))
    ranked.sort(key=lambda x: (-x[0], x[1]))
    tertiary = [build({"r": r, "lag": lag}, "window") for _, lag, r in ranked[:TOP_K_WINDOW]]
    return primary + secondary + tertiary


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
        "偵測到的據…奏片段（僅為起點，非全部奏報事實）：",
        *[f"・{s}" for s in spans[:8]],
        "※ 上諭後段的無標籤敘述性奏報也要追溯來源；皇帝自己的評論、賞罰與命令不配對。",
        "※ 具名來源不是互斥排名：同一上諭資訊可由多份奏摺獨立支持；不得因已有一份直奏或轉述奏摺就省略其他有文字證據的來源。",
        "",
    ]
    basis_label = {
        "named": "具名來源（作者見於據…奏片段）",
        "corroborating": "同期候選（據…等奏，憑內容重疊入選）",
        "window": "全域候選（無據奏標籤，憑上諭內容重疊入選）",
    }
    for i, c in enumerate(cands, 1):
        lines += [
            f"【候選來源奏摺 {i}】",
            f"doc_id：{c['id']}",
            f"具奏官員：{c['author']}",
            f"上奏日：{c['sendAr'] or '未明'}",
            f"收到／硃批日：{c['recvAr'] or '未明'}",
            f"距上諭：{c['lag_days']} 日前收到",
            f"配對依據：{basis_label.get(c.get('match_basis'), '具名來源')}",
            f"原文：\n{c['body']}",
            "",
        ]
    return "\n".join(lines)


def recall_audit_candidates(cands):
    """Candidates the completeness pass must check for omitted source edges."""
    return [c for c in cands if c.get("match_basis") in {"named", "corroborating"}]


def completeness_audit_block(edict, cands, draft_pairs):
    """Build a compact second-pass block focused on recall, not new discovery."""
    audit_cands = recall_audit_candidates(cands)
    lines = [
        "【本上諭】",
        f"doc_id：{edict.get('id', '')}",
        f"發布日：{edict.get('annAr') or edict.get('sendAr') or '未明'}",
        f"標題：{edict.get('title', '')}",
        f"原文：\n{edict.get('body', '')}",
        "",
        "【初輪模型已選配對（可能不完整）】",
        json.dumps(
            [
                {
                    "source_doc_id": p.get("reply_doc_id"),
                    "evidence": p.get("evidence", {}),
                }
                for p in draft_pairs
            ],
            ensure_ascii=False,
            indent=2,
        ),
        "",
        "【必須逐一複核的同一五日來源窗候選】",
    ]
    basis_label = {
        "named": "具名來源（作者見於據…奏片段）",
        "corroborating": "同期候選（據…等奏，憑內容重疊入選）",
    }
    for i, c in enumerate(audit_cands, 1):
        lines += [
            f"【複核候選 {i}】",
            f"doc_id：{c['id']}",
            f"具奏官員：{c['author']}",
            f"收到／硃批日：{c['recvAr'] or '未明'}",
            f"距上諭：{c['lag_days']} 日前收到",
            f"配對依據：{basis_label.get(c.get('match_basis'), '候選')}",
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
    valid = {c["id"]: c for c in cands}
    pairs = []
    for p in obj.get("pairs", []):
        sid = str(p.get("source_doc_id", p.get("reply_doc_id", ""))).strip()
        cand = valid.get(sid)
        if not cand:
            continue
        evidence = dict(p.get("evidence", {}) or {})
        segments = []
        for seg in evidence.get("segments", []) or []:
            if not isinstance(seg, dict):
                continue
            yu = str(seg.get("yu", seg.get("matched_yu_span", "")) or "").strip()
            reply = str(seg.get("reply", seg.get("quote_in_reply", "")) or "").strip()
            if yu and reply:
                segments.append({"yu": yu, "reply": reply})
        if not segments:
            yu = str(evidence.get("matched_yu_span", "") or "").strip()
            reply = str(evidence.get("quote_in_reply", "") or "").strip()
            if yu and reply:
                segments.append({"yu": yu, "reply": reply})
        if not segments:
            continue
        evidence["segments"] = segments
        evidence["matched_yu_span"] = "／".join(x["yu"] for x in segments)
        evidence["quote_in_reply"] = "／".join(x["reply"] for x in segments)
        span_type = str(p.get("yu_span_type", evidence.get("yu_span_type", "")) or "").strip()
        if span_type not in {"cited", "narrative"}:
            span_type = "narrative" if cand.get("match_basis") == "window" else "cited"
        evidence["yu_span_type"] = span_type
        evidence.setdefault("match_basis", cand.get("match_basis", "named"))
        pairs.append({
            "yu_doc_id": edict_id,
            "reply_doc_id": sid,
            "relation": "yu_source",
            "match_level": p.get("match_level", "weak"),
            "evidence": evidence,
        })
    return pairs


def dedupe_pairs(pairs):
    """Keep one evidence card per 上諭/source document edge."""
    seen, deduped = set(), []
    for pair in pairs:
        key = (pair.get("yu_doc_id"), pair.get("reply_doc_id"))
        if key in seen:
            continue
        seen.add(key)
        deduped.append(pair)
    return deduped


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
    ap.add_argument("--no-recall-audit", action="store_true",
                    help="Disable the second-pass completeness audit.")
    ap.add_argument("--bundle-name", default="yu-source")
    ap.add_argument(
        "--bundle-only",
        action="store_true",
        help="Write only the shared review bundle; do not touch formal yu-source.json.",
    )
    args = ap.parse_args()

    records = load_records()
    by_id = {r.get("id"): r for r in records}

    out_path = None if args.bundle_only else ROOT / "review-tools" / "(1) formal" / "yu-source.json"
    existing_pairs, existing_analyzed, done_ids = [], [], set()
    if args.skip_done and out_path and out_path.exists():
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
                tag = "  [等奏：擴大同期候選]" if has_et_al(s) else ""
                print(f"   據奏: {s}{tag}")
            basis_label = {"named": "具名", "corroborating": "同期候選", "window": "全域候選"}
            for c in cands:
                print(f"  {c['id']:>6}  {c['author']:<6} recv={c['recvAr']}  {c['lag_days']}d-before-issue  [{basis_label.get(c.get('match_basis'), '?')}]")
        return 0

    proxy_jobs = [(edict, cands) for edict, cands in jobs if cands]
    if proxy_jobs and not args.proxy:
        ap.error("Set GEMINI_PROXY_URL or pass --proxy (or use --dry-run).")

    prompt_text = website_prompt()
    audit_prompt_text = completeness_audit_prompt()

    def _run_job(edict, cands):
        draft_pairs = []
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
            print(f"  ! primary proxy failed for 上諭 {edict['id']}: {exc}", file=sys.stderr)
        else:
            draft_pairs = parse_pairs(result, edict["id"], cands)

        audit_cands = recall_audit_candidates(cands)
        if args.no_recall_audit or len(audit_cands) < 2:
            return draft_pairs

        audit_payload = {
            "mode": "ask",
            "model": args.model,
            "doc_id": edict["id"],
            "doc_type": edict.get("doc_type", "上諭"),
            "title": edict.get("title", ""),
            "body": completeness_audit_block(edict, cands, draft_pairs),
            "question": audit_prompt_text,
        }
        try:
            audit_result = call_proxy(args.proxy, audit_payload)
        except Exception as exc:
            print(f"  ! completeness audit failed for 上諭 {edict['id']}: {exc}", file=sys.stderr)
            return draft_pairs
        additions = parse_pairs(audit_result, edict["id"], cands)
        for pair in additions:
            pair.setdefault("evidence", {})["selection_pass"] = "completeness_audit"
        return draft_pairs + additions

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

    deduped = dedupe_pairs(existing_pairs + kept)

    analyzed = sorted(set(existing_analyzed) | {a for a in run_analyzed if a})
    result = {"pairs": deduped, "analyzed": analyzed}
    if out_path:
        out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    bundle_root = ROOT / "review-tools" / "shared data" / "review-bundles" / args.bundle_name
    (bundle_root / "outputs").mkdir(parents=True, exist_ok=True)
    (bundle_root / "outputs" / "yu-source.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (bundle_root / "manifest.json").write_text(json.dumps({
        "name": args.bundle_name,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "source": "review-tools/shared data/stage1_original_text.json",
        "doc_ids": sorted({p["yu_doc_id"] for p in deduped} | {p["reply_doc_id"] for p in deduped}),
        "chain": ["yu-source"],
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if out_path:
        print(out_path)
    print(bundle_root)
    print(f"pairs: {len(deduped)} (dropped {dropped} weak; use --include-weak to keep)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
