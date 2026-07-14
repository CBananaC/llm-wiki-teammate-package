#!/usr/bin/env python3
"""Detect which official memorial is quoting/answering which 硃批 (ZHU response pairing).

Sibling of run_yu_pairing.py. There the emperor side is a standalone 上諭; here it
is a 硃批 — the vermillion rescript the emperor wrote on an official's OWN earlier
memorial. That earlier memorial is a normal record (type zhupi / shangzou) whose
``rescript`` field holds the 硃批 text. When the same official later writes a new
memorial that opens ``…奉硃批：「…」欽此`` he is quoting the rescript on his own
earlier document — that earlier document is the emperor side of the pair.

Structural half (Python): identity (same author) + date window + 硃批 citation
marker with a 「…」 quotation + rescript-text overlap, to build candidate earlier
硃批-bearing documents per reply. Textual half (AI): confirm the quotation matches
that candidate's ``rescript`` (short-string match), extract spans, resolve the
named earlier memorial + receipt date, rate match_level. See
skills/zhu-response-pairing.md.

Scope (this version): quote-bearing replies only — a reply that merely states it
received a 硃批 without quoting it is a later phase.

Detection runs on the date-rich corpus (dual-timeline-data.json).

Examples:
  # structural preview, no proxy call:
  python3 scripts/run_zhu_pairing.py --doc-id 台46 --dry-run
  # every official doc sent in a month, against the proxy:
  python3 scripts/run_zhu_pairing.py --proxy https://... --reverse-month 1787/03 --skip-done
  # whole corpus:
  python3 scripts/run_zhu_pairing.py --proxy https://... --all
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "outputs" / "attempt-002" / "dual-timeline-data.json"
PROMPT_PATH = ROOT / "skills" / "zhu-response-pairing.md"
PROMPT_RE = re.compile(r"^##\s*Website Prompt[ \t]*\n(.*?)(?=\n##\s)", re.S | re.M)

# Markers an official uses to introduce a 硃批 he is quoting. These specifically
# introduce a *quotation* of a rescript; the bare word 硃批 is excluded because it
# also heads the memorial's own trailing 【硃批】 block (stripped separately).
ZHU_MARKERS = ("欽奉硃批", "敬奉硃批", "奉到硃批", "跪讀硃批", "恭讀硃批",
               "蒙硃批", "奉硃批", "承准硃批", "奉批")
# Window (days after the 硃批) within which a reply is even considered.
MAX_WINDOW_DAYS = 150


def parse_date(value):
    try:
        return datetime.strptime(value or "", "%Y/%m/%d")
    except (ValueError, TypeError):
        return None


def days_between(later, earlier):
    a, b = parse_date(later), parse_date(earlier)
    return (a - b).days if a and b else None


def website_prompt():
    m = PROMPT_RE.search(PROMPT_PATH.read_text(encoding="utf-8"))
    if not m:
        raise RuntimeError(f"No Website Prompt in {PROMPT_PATH}")
    return m.group(1).strip()


# The emperor side's own date: for a 硃批 that is when the official received it
# (recvAr); fall back to annotation/send date if absent.
def zhu_date(rec):
    return rec.get("recvAr") or rec.get("annAr") or rec.get("sendAr")


CN_DATE_RE = re.compile(
    r"(?:乾隆[元一二三四五六七八九十]+年)?(?:上年)?"
    r"[正臘閏元一二三四五六七八九十]{1,3}月[初一二三四五六七八九十]{1,3}日")

# The document's OWN rescript is appended after the closing 謹奏, as
#   「…謹奏。<發文日> <硃批日>奉硃批：已有旨了。欽此。【本文原收錄於軍機…】」
# — NOT inside a 【硃批】 block, so the old strip missed it and every such tail was
# mis-read as a bare citation of an earlier 硃批. Strip: the archival note, then a
# marker+text+欽此 anchored at end of string (no 「」 inside, so a genuine quoted
# citation ending near EOF is never removed).
_ARCHIVE_RE = re.compile(r"[【〔（(]?\s*本文(?:原)?收錄[\s\S]*$")
_OWN_TAIL_RE = re.compile(
    r"(?:謹奏[。]?\s*)?"
    r"(?:乾隆[^\n奉：「」]{0,26}日\s*){0,2}"
    r"(?:同日|是日|本日)?\s*"
    r"(?:欽奉|敬奉|奉到|承准|奉)?硃批[：:。]"
    r"[^「」]{0,260}?(?:欽此[。]?)?[\s」』】〕）)]*$")


def strip_own_rescript(body):
    """Drop the memorial's OWN trailing rescript so it is never mistaken for a
    citation of an EARLIER 硃批. Handles both the explicit 【硃批】 block and the
    common archival-tail form (…謹奏。<日期>奉硃批：X。欽此。【本文原收錄…】)."""
    b = re.sub(r"【硃批】[\s\S]*$", "", body or "")
    b = _ARCHIVE_RE.sub("", b)
    b = _OWN_TAIL_RE.sub("", b)
    return b.rstrip()


# Markers introducing a *quotation* of a 硃批 (a 「…」 follows). Reused for the
# label-only scan, where the same markers appear but with NO following quote.
_LABEL_MARKERS = ("欽奉硃批", "敬奉硃批", "奉到硃批", "蒙硃批", "奉硃批")
_MEM_REF_RE = re.compile(r"摺|前奏|前次|前摺|奏報|奏請|奏明|奏聞|奏覆|奏陳|具奏")


def label_only_citations(body):
    """Bare 硃批 references — a marker with NO following 「…」 quote — that sit in
    the narrative and name an earlier memorial (…前奏…一摺…奉到硃批…). These are the
    'received but not quoted' type; each names the official's own earlier memorial,
    often by date. Returns [{marker, passage, named_date}]. `body` must already have
    had strip_own_rescript applied so the doc's own tail rescript is gone."""
    text = body or ""
    out, seen = [], set()
    for marker in _LABEL_MARKERS:
        for m in re.finditer(re.escape(marker), text):
            # skip if a quotation actually follows (that's the quote path)
            if re.match(r"[：:，、。\s一道二三四五六七八九十內開閱奉]{0,16}[「『]",
                        text[m.end():m.end() + 20]):
                continue
            lead = text[max(0, m.start() - 44):m.start()]
            if not _MEM_REF_RE.search(lead):
                continue
            # A lead like "正月初二日奏報…各摺，於正月二十八日奉到硃批" carries TWO dates:
            # the memorial's own send date (正月初二日) and the 硃批 receipt date
            # (正月二十八日). Keep both — either may pin the candidate memorial.
            named_dates = [d.group(0) for d in CN_DATE_RE.finditer(lead)]
            start = max(0, m.start() - 44)
            passage = text[start:m.end() + 8].strip()
            key = passage[:20]
            if key in seen:
                continue
            seen.add(key)
            out.append({"marker": marker, "passage": passage,
                        "named_date": named_dates[-1] if named_dates else "",
                        "named_dates": named_dates})
    return out


def _title_grams(text):
    t = re.sub(r"[\s\W_為事]+", "", text or "")
    return {t[i:i + 2] for i in range(len(t) - 1)}


def topic_similarity(a_title, b_title):
    ga, gb = _title_grams(a_title), _title_grams(b_title)
    if not ga or not gb:
        return 0.0
    return round(len(ga & gb) / len(ga | gb), 4)


def _month_day_variants(named_date):
    """month+day of a Chinese date, with 正/一/元 month equivalence, e.g.
    '乾隆五十一年十二月十七日' -> {'十二月十七日'}; '一月十三日' -> {'一月十三日','正月十三日','元月十三日'}."""
    m = re.search(r"([正臘閏元一二三四五六七八九十]{1,3})月([初一二三四五六七八九十]{1,3})日", named_date or "")
    if not m:
        return set()
    month, day = m.group(1), m.group(2)
    months = {month}
    if month in ("一", "正", "元"):
        months |= {"一", "正", "元"}
    return {f"{mo}月{day}日" for mo in months}


def named_date_matches(named_date, cand):
    """True if the reply's named earlier-memorial date matches this candidate's own
    send date (compared against its Chinese sendCh, which carries month+day)."""
    sc = cand.get("sendCh") or ""
    return any(v in sc for v in _month_day_variants(named_date))


def no_quote_candidates(reply, records):
    """Label-only path: the reply acknowledges a 硃批 but does not quote it. The
    rescript sits on the official's OWN earlier memorial, so candidates are that
    author's earlier rescript-bearing docs. Rank by (1) the reply's NAMED memorial
    date matching the candidate's send date, then (2) topic similarity of titles,
    then recency. Returns (cands, cites) or None."""
    body = strip_own_rescript(reply.get("body"))
    if quoted_spans(body):
        return None  # a real quotation exists — handled by the quote path
    cites = label_only_citations(body)
    if not cites:
        return None
    named_dates = [d for c in cites for d in c.get("named_dates", []) if d]
    reply_author = reply.get("author_name")
    reply_send = reply.get("sendAr")
    reply_id = reply.get("id")
    scored = []
    for z in records:
        rescript = (z.get("rescript") or "").strip()
        if not rescript or z.get("id") == reply_id:
            continue
        if not _same_author(reply_author, z.get("author_name")):
            continue
        lag = days_between(reply_send, z.get("recvAr") or z.get("annAr") or z.get("sendAr"))
        if lag is None or lag <= 0 or lag > MAX_WINDOW_DAYS:
            continue
        nd_hit = any(named_date_matches(nd, z) for nd in named_dates)
        topic = topic_similarity(reply.get("title"), z.get("title"))
        scored.append((not nd_hit, -topic, lag, z, nd_hit, topic))
    if not scored:
        return None
    scored.sort(key=lambda r: r[:3])
    cands = [{
        "id": z["id"], "author": (z.get("author_name") or "").strip(),
        "title": z.get("title", ""), "recvAr": z.get("recvAr", ""),
        "sendAr": z.get("sendAr", ""), "sendCh": z.get("sendCh", ""),
        "rescript": (z.get("rescript") or "").strip(),
        "lag_days": lag, "named_date_hit": nd_hit, "topic": topic,
    } for (_a, _b, lag, z, nd_hit, topic) in scored[:8]]
    return cands, cites


_PUNCT_RE = re.compile(r"[。，、；：！？「」『』（）〈〉\s]")
_TAIL_RE = re.compile(r"(欽此|等因|等語|欽遵).*$")


def rescript_core(text):
    """Normalise a rescript / quoted span for short-string comparison: drop
    punctuation and any 欽此/等因 tail."""
    s = _TAIL_RE.sub("", text or "")
    return _PUNCT_RE.sub("", s)


def quoted_spans(body):
    """Every 「…」 span that follows a 硃批 citation marker in the reply body
    (own trailing rescript already stripped by the caller). Returns list of
    (marker, quoted_text, passage) where passage includes a lead-in for context."""
    text = body or ""
    out, seen = [], set()
    for marker in ZHU_MARKERS:
        for m in re.finditer(re.escape(marker), text):
            # the opening 「 sits right after the marker (allow a short lead like
            # "：", "一道，內開："); the closing 」 may be far for a long rescript,
            # so scan a wide window for it.
            after = text[m.end():m.end() + 240]
            q = re.match(r"[：:，、。\s一道二三四五六七八九十內開內閱奉]{0,16}[「『]([^」』]{1,180})[」』]", after)
            if not q:
                continue
            quoted = q.group(1)
            # Reach the passage start back to the DATE that identifies the original
            # memorial (e.g. "又上年十二月初十日奴才奏報登舟渡臺一摺，奉硃批：…"): snap to
            # the last Chinese date within 60 chars before the marker so the AI can
            # put that confirming date at the head of quote_in_reply. Fall back to a
            # plain 40-char lead when no date precedes the marker.
            lead_lo = max(0, m.start() - 60)
            lead = text[lead_lo:m.start()]
            dm = list(re.finditer(
                r"(?:乾隆[元一二三四五六七八九十]+年)?(?:上年)?"
                r"[正臘閏元一二三四五六七八九十]{1,3}月[初一二三四五六七八九十]{1,3}日", lead))
            start = (lead_lo + dm[-1].start()) if dm else max(0, m.start() - 40)
            stop = m.end() + q.end()
            passage = text[start:stop].strip()
            key = rescript_core(quoted)[:12] + marker
            if key in seen:
                continue
            seen.add(key)
            out.append((marker, quoted, passage))
    return out


def quote_matches_rescript(spans, rescript):
    """True when one of the reply's quoted 硃批 spans matches this candidate's
    rescript (short exact/near-exact: one string contains the other's core)."""
    rc = rescript_core(rescript)
    # require >=3 matched characters: 1-2 char boilerplate rescripts (是／覽) would
    # otherwise substring-match almost any quoted span. Such short rescripts still
    # reach the candidate list via the same-author signal; they just don't get the
    # decisive "引文相符" boost.
    if len(rc) < 3:
        return False
    for _marker, quoted, _passage in spans:
        qc = rescript_core(quoted)
        if len(qc) < 3:
            continue
        if rc in qc or qc in rc:
            return True
    return False


def _same_author(a, b):
    a, b = (a or "").strip(), (b or "").strip()
    if not a or not b:
        return False
    # tolerate 「（等）」 / role suffixes: match on the shorter being a substring
    a2, b2 = a.replace("（等）", "").strip(), b.replace("（等）", "").strip()
    return a2 in b2 or b2 in a2


def zhu_candidates_for(reply, records):
    """Given an official memorial, the earlier 硃批-bearing documents whose rescript
    it may be quoting. Structural net: the reply carries a 硃批 quotation marker;
    the candidate has a non-empty rescript, is dated before the reply, within the
    window, and either shares the reply's author (a 硃批 sits on that official's own
    memorial) OR its rescript text appears in one of the reply's quoted spans."""
    body = strip_own_rescript(reply.get("body"))
    spans = quoted_spans(body)
    if not spans:
        return []
    reply_send = reply.get("sendAr")
    reply_author = reply.get("author_name")
    reply_id = reply.get("id")
    out = []
    for z in records:
        rescript = (z.get("rescript") or "").strip()
        if not rescript or z.get("id") == reply_id:
            continue
        lag = days_between(reply_send, zhu_date(z))
        if lag is None or lag <= 0 or lag > MAX_WINDOW_DAYS:
            continue
        same_author = _same_author(reply_author, z.get("author_name"))
        quote_hit = quote_matches_rescript(spans, rescript)
        if not (same_author or quote_hit):
            continue
        out.append({
            "id": z["id"],
            "author": (z.get("author_name") or "").strip(),
            "title": z.get("title", ""),
            "type": z.get("type", ""),
            "recvAr": z.get("recvAr", ""),
            "sendAr": z.get("sendAr", ""),
            "rescript": rescript,
            "lag_days": lag,
            "same_author": same_author,
            "quote_hit": quote_hit,
        })
    # quote-text match is the decisive signal, then same author, then nearest date
    out.sort(key=lambda c: (not c["quote_hit"], not c["same_author"], c["lag_days"]))
    return out[:12], spans


def reply_block(reply, cands, spans, cites=None):
    label_mode = cites is not None
    lines = [
        "【本回應】",
        f"doc_id：{reply.get('id', '')}",
        f"具奏官員：{(reply.get('author_name') or '').strip()}",
        f"上奏日：{reply.get('sendAr') or '未明'}（{reply.get('sendCh') or ''}）",
        f"標題：{reply.get('title', '')}",
    ]
    if label_mode:
        lines.append("硃批引用情形：本摺僅具「奉硃批」等標記、未引錄硃批原文（label-only）。"
                     "以下為敘及先前奏摺並提及奉到硃批的段落：")
        for c in cites[:5]:
            lines.append(f"---\n{c['passage']}")
    else:
        lines.append("偵測到的硃批引用段落：")
        if spans:
            for _marker, _quoted, passage in spans[:5]:
                lines.append(f"---\n{passage}")
        else:
            lines.append("（未偵測到引用標記）")
    lines.append("")
    for i, c in enumerate(cands, 1):
        flags = []
        if c.get("quote_hit"):
            flags.append("引文相符")
        if c.get("named_date_hit"):
            flags.append("所奏日期相符")
        if c.get("same_author") or label_mode:
            flags.append("同一具奏官員")
        if c.get("topic"):
            flags.append(f"題旨相似 {c['topic']}")
        lines += [
            f"【候選硃批文書 {i}】",
            f"doc_id：{c['id']}",
            f"具奏官員：{c['author']}",
            f"硃批日：{c['recvAr'] or '未明'}（距本回應 {c['lag_days']} 日前）",
            f"該摺上奏日：{c.get('sendCh') or c.get('sendAr') or '未明'}",
            f"該摺標題：{c['title']}",
            f"硃批原文（rescript）：「{c['rescript']}」",
            "結構線索：" + ("、".join(flags) or "（僅日期）"),
            "",
        ]
    return "\n".join(lines)


# Extra instruction appended to the prompt when running the label-only (no quote)
# path — the base Website Prompt assumes a 「…」 quotation exists.
LABEL_MODE_INSTRUCTION = (
    "\n\n【本次為 label-only 判定】本摺並未引錄硃批原文，只說明曾就先前某摺奉到硃批。"
    "請依『敘及的先前奏摺 + 其日期 + 題旨』判斷所指的候選硃批文書；`matched_zhu_span` 留空，"
    "並於 evidence 加入 `\"quote_type\": \"label_only\"`。此類配對至多評為 `partial`"
    "（日期與題旨明確相符時）或 `weak`，不得評為 `high`。"
)


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


def parse_pairs(model_response, reply_id, cands):
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
        zid = str(p.get("zhu_doc_id", "")).strip()
        if zid not in valid:
            continue
        pairs.append({
            "reply_doc_id": reply_id,
            "zhu_doc_id": zid,
            # stored under yu_doc_id too so the website's existing pair-rendering
            # (which keys off yu_doc_id) draws the connector to the 硃批 dot.
            "yu_doc_id": zid,
            "relation": "reply_to_zhu",
            "match_level": p.get("match_level", "weak"),
            "evidence": p.get("evidence", {}),
        })
    return pairs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--proxy", default=os.environ.get("GEMINI_PROXY_URL", ""))
    ap.add_argument("--doc-id", help="Analyse one official document — find the 硃批 it quotes. "
                    "Comma-separate several.")
    ap.add_argument("--all", action="store_true",
                    help="Analyse every official document (non-上諭).")
    ap.add_argument("--reverse-month", "--month", dest="month", metavar="YYYY/MM",
                    help="Analyse every official doc SENT in this month (e.g. 1787/03) — "
                    "find the 硃批 each one quotes.")
    ap.add_argument("--skip-done", action="store_true",
                    help="Skip docs already present in the existing output and merge new "
                    "results into it (resume a long run).")
    ap.add_argument("--model", default="gemini-3.5-flash")
    ap.add_argument("--dry-run", action="store_true", help="Show candidates; no proxy call.")
    ap.add_argument("--include-weak", action="store_true",
                    help="Keep weak pairs too; default drops them.")
    ap.add_argument("--no-label-only", action="store_true",
                    help="Skip the label-only pass (replies that acknowledge a 硃批 "
                    "without quoting it); only pair quote-bearing replies.")
    ap.add_argument("--bundle-name", default="zhu-pairing")
    args = ap.parse_args()

    records = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    by_id = {r.get("id"): r for r in records}

    out_path = ROOT / "outputs" / "attempt-002" / "zhu-pairing.json"
    existing_pairs, existing_analyzed, done_ids = [], [], set()
    if args.skip_done and out_path.exists():
        prev = json.loads(out_path.read_text(encoding="utf-8"))
        if isinstance(prev, dict):
            existing_pairs, existing_analyzed = prev.get("pairs", []), prev.get("analyzed", [])
        else:
            existing_pairs = prev
        done_ids = {p.get("reply_doc_id") for p in existing_pairs}

    if args.doc_id:
        anchors = []
        for one in (x.strip() for x in args.doc_id.split(",") if x.strip()):
            rec = by_id.get(one)
            if not rec:
                ap.error(f"document not found: {one}")
            anchors.append(rec)
    elif args.all:
        anchors = [r for r in records if r.get("type") != "shangyu"]
    elif args.month:
        anchors = [r for r in records
                   if r.get("type") != "shangyu"
                   and (r.get("sendAr") or "").startswith(args.month)]
    else:
        ap.error("Pass --doc-id, --all, or --reverse-month YYYY/MM.")

    if args.skip_done:
        anchors = [a for a in anchors if a.get("id") not in done_ids]

    run_analyzed = [a.get("id") for a in anchors]

    prompt_text = website_prompt()
    all_pairs = []
    for reply in anchors:
        built = zhu_candidates_for(reply, records)
        if built:
            cands, spans, cites, mode = built[0], built[1], None, "quote"
        elif not args.no_label_only:
            nq = no_quote_candidates(reply, records)
            if not nq:
                continue
            cands, spans, cites, mode = nq[0], None, nq[1], "label"
        else:
            continue
        if args.dry_run:
            tag = "label-only" if mode == "label" else "quote"
            print(f"\n== [{tag}] {reply['id']}  {(reply.get('author_name') or '').strip()}  "
                  f"{reply.get('sendAr')} ==")
            if mode == "label":
                nds = [d for c in cites for d in c.get("named_dates", [])]
                print(f"   敘及先前奏摺日期：{'、'.join(nds) or '未名'}")
            for c in cands:
                flag = ("★引文相符" if c.get("quote_hit") else "") \
                    + (" ★日期符" if c.get("named_date_hit") else "") \
                    + (" 同官" if (c.get("same_author") or mode == "label") else "") \
                    + (f" 題旨{c['topic']}" if c.get("topic") else "")
                print(f"   硃批候選 {c['id']:>6}  {c['author']:<6} {c['recvAr'] or c.get('sendAr','')}  "
                      f"-{c['lag_days']}d  「{c['rescript'][:16]}」 {flag}")
            continue
        if not args.proxy:
            ap.error("Set GEMINI_PROXY_URL or pass --proxy (or use --dry-run).")
        question = prompt_text + (LABEL_MODE_INSTRUCTION if mode == "label" else "")
        payload = {
            "mode": "ask",
            "model": args.model,
            "doc_id": reply["id"],
            "doc_type": reply.get("doc_type", "奏摺"),
            "title": reply.get("title", ""),
            "body": reply_block(reply, cands, spans, cites),
            "question": question,
        }
        try:
            result = call_proxy(args.proxy, payload)
        except Exception as exc:
            print(f"  ! proxy failed for {reply['id']} after retries: {exc} — skipping",
                  file=sys.stderr)
            continue
        all_pairs.extend(parse_pairs(result, reply["id"], cands))

    if args.dry_run:
        return 0

    kept = all_pairs if args.include_weak else [p for p in all_pairs if p.get("match_level") != "weak"]
    dropped = len(all_pairs) - len(kept)

    seen, deduped = set(), []
    for p in existing_pairs + kept:
        key = (p["reply_doc_id"], p.get("zhu_doc_id") or p.get("yu_doc_id"))
        if key not in seen:
            seen.add(key)
            deduped.append(p)

    analyzed = sorted(set(existing_analyzed) | {a for a in run_analyzed if a})
    result = {"pairs": deduped, "analyzed": analyzed}
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    bundle_root = ROOT / "outputs" / "review-bundles" / args.bundle_name
    (bundle_root / "outputs").mkdir(parents=True, exist_ok=True)
    (bundle_root / "outputs" / "zhu-pairing.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (bundle_root / "manifest.json").write_text(json.dumps({
        "name": args.bundle_name,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "source": "outputs/attempt-002/dual-timeline-data.json",
        "doc_ids": sorted({p["reply_doc_id"] for p in deduped}
                          | {p.get("zhu_doc_id") or p.get("yu_doc_id") for p in deduped}),
        "chain": ["zhu-pairing"],
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(out_path)
    print(bundle_root)
    print(f"pairs: {len(deduped)} (dropped {dropped} weak; use --include-weak to keep)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
