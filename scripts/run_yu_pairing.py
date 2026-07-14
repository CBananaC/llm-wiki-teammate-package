#!/usr/bin/env python3
"""Detect which official memorial is responding to which 上諭 (YU response pairing).

Structural half (Python): identity + date window + citation-marker / cited-date
extraction to build candidate reply lists per 上諭.  Textual half (AI): confirm
the citation, extract quotations, classify issue vs receive dates, rate
match_level.  See skills/yu-response-pairing.md.

Detection runs on the date-rich corpus (dual-timeline-data.json).  Write-back
(a later phase) targets stage1-date-adjusted.json.

Examples:
  # structural preview, no proxy call:
  python3 scripts/run_yu_pairing.py --doc-id 天43 --dry-run
  # full run against the proxy:
  python3 scripts/run_yu_pairing.py --proxy https://... --doc-id 天43
  # whole corpus:
  python3 scripts/run_yu_pairing.py --proxy https://... --all
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

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "outputs" / "attempt-002" / "dual-timeline-data.json"
PROMPT_PATH = ROOT / "skills" / "yu-response-pairing.md"
PROMPT_RE = re.compile(r"^##\s*Website Prompt[ \t]*\n(.*?)(?=\n##\s)", re.S | re.M)

# Citation markers an official uses to introduce the edict they received.
CITATION_MARKERS = ("欽奉上諭", "奉上諭", "奉到上諭", "接奉上諭", "奉聖諭",
                    "聖諭", "奉廷寄", "承准廷寄", "接准廷寄", "廷寄",
                    "欽奉諭旨", "接奉諭旨", "奉到諭旨", "諭旨", "硃批",
                    "承准", "接奉", "敬奉")
# Chinese-date pattern (optional 乾隆..年, month incl. 正/臘/閏, day).
CN_DATE_RE = re.compile(
    r"(?:乾隆[元一二三四五六七八九十]+年)?[正臘閏元一二三四五六七八九十]{1,3}月[初一二三四五六七八九十]{1,3}日"
)
# Window (days after the edict) within which a reply is even considered.
MAX_WINDOW_DAYS = 150
MAX_CANDIDATES = 48

# These markers introduce an imperial order/edict.  硃批 is deliberately not
# in this set: it is common in a memorial's own response metadata and is not,
# by itself, evidence that the memorial quotes an 上諭.
DIRECT_CITATION_MARKERS = (
    "欽奉上諭", "奉上諭", "奉到上諭", "接奉上諭", "奉聖諭", "聖諭",
    "奉廷寄", "承准廷寄", "接准廷寄", "廷寄", "欽奉諭旨", "接奉諭旨",
    "奉到諭旨", "接奉諭旨",
)


def parse_date(value):
    """Parse corpus dates, tolerating the corpus' occasional 2/29 overflow.

    The source uses the Chinese month/day in several places when generating
    the Arabic helper field, so values such as 1787/02/29 occur even though
    that Gregorian month has 28 days.  Clamping only this end-of-month overflow
    keeps ordering/window checks usable without rewriting the source corpus.
    """
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


# Populated once in main() from every author/recipient name in the corpus, used
# to recognise officials named inside an edict's body.
_KNOWN_OFFICIALS: set[str] = set()
# Directive verbs that mark an official as an addressee of the edict.
_DIRECTIVE_VERBS = ("傳諭", "諭令", "諭", "令", "著", "飭", "寄")


def build_known_officials(records):
    names = set()
    for r in records:
        a = (r.get("author_name") or "").strip()
        if a:
            names.add(a)
        for n in (r.get("recipients") or []):
            n = (n or "").strip()
            if n:
                names.add(n)
    return {n for n in names if 2 <= len(n) <= 4}


def body_recipients(body, known):
    """Officials named as addressees inside the edict body (e.g. 令孫士毅嚴密查拿),
    not just those in the recipients field — an edict often orders a secondary
    official within a document addressed to someone else."""
    text = body or ""
    found = set()
    for name in known:
        if any(verb + name in text for verb in _DIRECTIVE_VERBS):
            found.add(name)
    return found


def recipients_of(edict, known=None):
    if known is None:
        known = _KNOWN_OFFICIALS
    names = [n.strip() for n in (edict.get("recipients") or []) if n and n.strip()]
    if known:
        names += sorted(body_recipients(edict.get("body"), known))
    if not names and edict.get("author_name"):
        names = [edict["author_name"].strip()]
    return list(dict.fromkeys(names))


def transit_estimates(records):
    """Average send->receive(硃批) lag per author — a soft estimate of how long an
    imperial document takes to reach that official."""
    acc: dict[str, list[int]] = {}
    for r in records:
        lag = days_between(r.get("recvAr"), r.get("sendAr"))
        name = (r.get("author_name") or "").strip()
        if name and lag is not None and lag > 0:
            acc.setdefault(name, []).append(lag)
    return {name: round(sum(v) / len(v), 1) for name, v in acc.items()}


def _cn_date_variants(ann_ch):
    """Return substrings to search a reply body for the edict's own date, e.g.
    '乾隆五十二年一月十三日' -> {'一月十三日', '正月十三日'}."""
    if not ann_ch:
        return set()
    m = re.search(r"([正元一二三四五六七八九十]{1,3})月([初一二三四五六七八九十]{1,3})日", ann_ch)
    if not m:
        return set()
    month, day = m.group(1), m.group(2)
    months = {month}
    if month in ("一", "正", "元"):
        months |= {"一", "正", "元"}
    days = {day}
    # The reply may write 初六日 while the edict metadata writes 六日 (or
    # vice versa).  They are the same Chinese calendar date.
    if day.startswith("初"):
        days.add(day[1:])
    else:
        days.add("初" + day)
    return {f"{mo}月{dy}日" for mo in months for dy in days}


def citation_passages(body, max_passages=5, lead=34, window=1800, fallback=500):
    """Extract text around each citation marker (the reply's quotation of an edict).

    A quoted 上諭 can be very long (e.g. 台302 quotes from ``二月十一日奉上諭：「``
    all the way to ``…令其回奏。」欽此``), so we search a wide ``window`` after the
    marker for the true close ``欽此`` and include the whole span up to it. Only
    when no ``欽此``/``等因``/``等語`` is found in that window do we fall back to a
    generous ``fallback`` slice (never a short cut that would drop the quote).
    Includes ``lead`` chars before the marker so a preceding date / ``同日``
    back-reference stays in the passage.
    """
    text = body or ""
    passages, seen = [], set()
    for marker in CITATION_MARKERS:
        for m in re.finditer(re.escape(marker), text):
            start = max(0, m.start() - lead)
            after = text[m.start():m.start() + window]
            end = re.search(r"欽此", after) or re.search(r"(等因|等語)", after)
            stop = m.start() + (end.end() if end else min(fallback, len(after)))
            passage = text[start:stop]
            key = passage[:24]
            if key in seen:
                continue
            seen.add(key)
            passages.append(passage.strip())
            if len(passages) >= max_passages:
                return passages
    return passages


def has_direct_citation(body):
    """Whether the text contains a real quoted imperial-order lead-in.

    This is intentionally stricter than ``CITATION_MARKERS``.  A direct quote
    can be enough to surface a candidate even when the order was relayed to a
    secondary official who is not listed in the 上諭 recipients field.
    """
    text = body or ""
    for marker in DIRECT_CITATION_MARKERS:
        for m in re.finditer(re.escape(marker), text):
            lead = text[m.start():m.start() + 100]
            # Require the marker to introduce a quoted/colon-delimited order;
            # a bare “廷寄” or “諭旨” mention in ordinary narration is not
            # enough to bypass the recipient filter.
            if not re.search(r"[：:「『]", lead):
                continue
            tail = text[m.start():m.start() + 2200]
            if re.search(r"欽此|等因|等語", tail):
                return True
    return False


def explicit_citation_dates(body):
    """Distinct issue-date strings printed immediately before Yu citations."""
    text = body or ""
    found = []
    for marker in DIRECT_CITATION_MARKERS:
        for match in re.finditer(re.escape(marker), text):
            before = text[max(0, match.start() - 110):match.start()]
            dates = list(CN_DATE_RE.finditer(before))
            if dates:
                value = dates[-1].group()
                if value not in found:
                    found.append(value)
    return found


def citation_overlap(body, edict_body, passages=None):
    """Approximate how much of a cited passage is shared with the edict.

    This is only a structural ranking signal.  The model still decides the
    relationship, but the overlap keeps a true long quotation from being
    pushed out by a crowded candidate list.
    """
    source = re.sub(r"[\s\W_]+", "", edict_body or "")
    if len(source) < 3:
        return 0.0
    source_grams = {source[i:i + 3] for i in range(len(source) - 2)}
    best = 0.0
    for passage in (passages if passages is not None else citation_passages(body, max_passages=8)):
        text = re.sub(r"[\s\W_]+", "", passage or "")
        if len(text) < 3:
            continue
        grams = {text[i:i + 3] for i in range(len(text) - 2)}
        if grams:
            best = max(best, len(grams & source_grams) / len(grams))
    return round(best, 4)


def _longest_title_hit(body, title, passages=None, minimum=3, maximum=12):
    """Return the longest shared Chinese substring with an edict title.

    A few catalogue 上諭 rows have an empty/placeholder body (for example
    天99: ``正文見第一部分。``). Their titles still carry the subject named
    in a later quotation (``天地會`` in 台301). This is only a fallback for
    ranking such rows; the model must still confirm the pair from the quote.
    """
    title = re.sub(r"[\s\W_]+", "", title or "")
    if len(title) < minimum:
        return 0
    source = passages if passages is not None else citation_passages(body, max_passages=64)
    best = 0
    for passage in source:
        text = re.sub(r"[\s\W_]+", "", passage or "")
        if len(text) < minimum:
            continue
        upper = min(maximum, len(title), len(text))
        for size in range(upper, minimum - 1, -1):
            if any(title[i:i + size] in text for i in range(len(title) - size + 1)):
                best = max(best, size)
                break
    return best


def _passage_has_issue_date(passage, variants):
    """True when an issue-date variant sits next to a citation lead-in.

    Checking the whole memorial is too broad: a multi-諭回奏 normally ends
    with its own send date, which can accidentally equal an unrelated 上諭's
    issue date.  Restrict the date signal to a small window around a real
    ``奉到諭旨``/``奉上諭``-style marker.
    """
    if not variants:
        return False
    text = passage or ""
    for marker in DIRECT_CITATION_MARKERS:
        for match in re.finditer(re.escape(marker), text):
            # In the corpus the issue date is printed immediately before the
            # receipt lead-in (``二月十七日奉到諭旨``).  Do not count dates that
            # occur only after a generic ``節次奉到諭旨`` summary, especially
            # the memorial's own trailing send date.
            window = text[max(0, match.start() - 110):match.start()]
            if any(v in window for v in variants):
                return True
    return False


def _reply_passages_for_edict(body, edict, limit=5):
    """Return the citation passages most likely to quote this particular edict.

    A long memorial may quote many 上諭s.  The old ``citation_passages`` cap kept
    only the first five passages for every candidate, so later dated quotations
    were invisible to the model even when the structural candidate was correct.
    Prefer passages containing this edict's issue-date variants, then fall back
    to the first few passages when the date is not printed.
    """
    passages = citation_passages(body, max_passages=64)
    variants = _cn_date_variants(edict.get("annCh") or "")
    dated = [p for p in passages if _passage_has_issue_date(p, variants)] if variants else []
    # The date printed before ``奉到諭旨`` is often the *receipt* date, not the
    # 上諭's issue date (台301 is the canonical example).  When the dates differ,
    # issue-date filtering alone discards the correct quotation.  Rank every
    # extracted passage by its character overlap with this candidate's edict,
    # while still putting an exact issue-date passage first when one exists.
    scored = sorted(
        ((citation_overlap("", edict.get("body") or "", [p]), i, p)
         for i, p in enumerate(passages)),
        key=lambda x: (-x[0], x[1]),
    )
    ordered = []
    seen = set()
    # Content overlap is the primary ordering signal; the printed date is often
    # only the receipt date and must not force an unrelated passage to the front.
    for p in [row[2] for row in scored] + dated:
        if p in seen:
            continue
        seen.add(p)
        ordered.append(p)
        if len(ordered) >= limit:
            break
    return ordered or passages[:limit]


def _reply_event_lag(reply, edict, allow_same_day=False):
    """Return the earliest usable post-edict reply/receipt lag.

    For 硃批 records, ``sendAr`` can be the original memorial date while the
    imperial order being answered was received later (``recvAr``).  Consider
    both fields, preferring the earliest non-negative lag.  This fixes cases
    such as 台314, whose memorial predates the quoted order but whose receipt
    date follows it.
    """
    issue = edict_date(edict)
    values = []
    for field in ("sendAr", "recvAr"):
        lag = days_between(reply.get(field), issue)
        if lag is not None:
            values.append((lag, field))
    valid = [(lag, field) for lag, field in values
             if (lag > 0 or (allow_same_day and lag == 0))
             and lag <= MAX_WINDOW_DAYS]
    if valid:
        return min(valid, key=lambda x: (x[0], 0 if x[1] == "sendAr" else 1))
    if allow_same_day:
        same = [(lag, field) for lag, field in values if lag == 0]
        if same:
            return same[0]
    return (None, None)


def _reply_cand(reply, edict, transit):
    """Build a candidate-reply record describing `reply` relative to `edict`."""
    author = (reply.get("author_name") or "").strip()
    body = reply.get("body") or ""
    passages = _reply_passages_for_edict(body, edict)
    date_variants = _cn_date_variants(edict.get("annCh") or "")
    direct_citation = has_direct_citation(body)
    lag, date_basis = _reply_event_lag(reply, edict, allow_same_day=direct_citation)
    return {
        "id": reply["id"],
        "author": author,
        "sendAr": reply.get("sendAr", ""),
        "recvAr": reply.get("recvAr", ""),
        "lag_days": lag,
        "date_basis": date_basis,
        "transit_est": transit.get(author),
        "cites_edict_date": any(_passage_has_issue_date(p, date_variants)
                                 for p in citation_passages(body, max_passages=64)),
        "direct_citation": direct_citation,
        "quote_overlap": citation_overlap(body, edict.get("body") or "", passages),
        "title_hit": _longest_title_hit(body, edict.get("title") or "", passages),
        "passages": passages,
    }


def _pairable(edict, reply):
    """True if reply passes the structural net for edict: identity + date window
    + a citation marker or the edict's own date appearing in the reply."""
    targets = recipients_of(edict)
    author = (reply.get("author_name") or "").strip()
    if not author:
        return False
    identity_match = any(t and (t in author or author in t) for t in targets)
    direct_citation = has_direct_citation(reply.get("body") or "")
    # Orders were often relayed through another governor or a regional
    # commander.  A full cited 上諭 is strong enough to enter the AI review
    # queue even when the recipient field contains only the upstream official.
    if not identity_match and not direct_citation:
        return False
    lag, _ = _reply_event_lag(reply, edict, allow_same_day=direct_citation)
    if lag is None:
        return False
    body = reply.get("body") or ""
    has_marker = any(mk in body for mk in CITATION_MARKERS)
    cites_date = any(v in body for v in _cn_date_variants(edict.get("annCh") or ""))
    return has_marker or cites_date


def candidates_for(edict, records, transit):
    """Forward: given an 上諭, the official replies that may answer it."""
    out = [
        _reply_cand(r, edict, transit)
        for r in records
        if r.get("id") != edict.get("id")
        and r.get("type") != "shangyu"
        and _pairable(edict, r)
    ]
    out.sort(key=lambda c: (
        not c["direct_citation"],
        -c["quote_overlap"],
        not c["cites_edict_date"],
        c["lag_days"] if c["lag_days"] is not None else 999,
    ))
    return out[:MAX_CANDIDATES]


def edicts_for(reply, records, transit, cap=MAX_CANDIDATES):
    """Reverse: given an official doc, the 上諭 it may be answering. Returns a list
    of (edict, [reply_cand]) so each edict can drive the same pairing prompt.

    ``cap`` bounds the fan-out — in reverse mode EACH returned edict becomes its
    own proxy call, so this directly sets how many API calls one reply costs.
    The ranking below puts a directly-cited / high-overlap edict at the very top,
    so a modest cap keeps the true match while avoiding a long tail of calls."""
    out = []
    for y in records:
        if y.get("type") != "shangyu":
            continue
        if _pairable(y, reply):
            out.append(y)
    ranked = []
    for y in out:
        cand = _reply_cand(reply, y, transit)
        ranked.append((
            not cand["direct_citation"],
            -cand["quote_overlap"],
            not cand["cites_edict_date"],
            cand["lag_days"] if cand["lag_days"] is not None else 999,
            y,
            cand,
        ))
    ranked.sort(key=lambda row: row[:4])
    # A single memorial can explicitly quote a sequence of dated 上諭s.  Keep
    # every candidate whose issue date is printed in the memorial, even when
    # generic overlap ranking would push it past the reverse-mode cap.  The cap
    # still limits undated/topic-only fallbacks, so this restores recall without
    # turning every reverse scan into an unbounded set of proxy calls.
    # Keep the strongest content-overlap candidates first.  Date hits are
    # appended as a recall supplement rather than placed ahead of the overlap
    # ranking: in these long 回奏s the date before ``奉到諭旨`` is frequently a
    # receipt date, not the issue date of the 上諭 being quoted.
    selected = ranked[:cap]
    seen = {str(row[4].get("id")) for row in selected}
    for row in ranked:
        if not row[5].get("cites_edict_date"):
            continue
        key = str(row[4].get("id"))
        if key in seen:
            continue
        seen.add(key)
        selected.append(row)
    # Preserve catalogue entries whose full body is missing/placeholder when
    # the quotation clearly shares a distinctive subject phrase with the
    # title. These rows cannot be recovered by body-overlap ranking (e.g.
    # 天99, whose source text is only ``正文見第一部分。``), but the model can
    # still make a provisional title/date-based judgement from the quoted text.
    for row in ranked:
        y, cand = row[4], row[5]
        if len((y.get("body") or "").strip()) > 30 or cand.get("title_hit", 0) < 3:
            continue
        key = str(y.get("id"))
        if key in seen:
            continue
        seen.add(key)
        selected.append(row)
    return [(row[4], [row[5]]) for row in selected]


def candidate_block(edict, cands):
    lines = [
        "【本上諭】",
        f"doc_id：{edict.get('id', '')}",
        f"發布日：{edict.get('annAr') or edict.get('sendAr') or '未明'}"
        f"（{edict.get('annCh') or ''}）",
        f"受命官員：{'、'.join(recipients_of(edict))}",
        f"標題：{edict.get('title', '')}",
        f"原文：\n{edict.get('body', '')}",
        "",
    ]
    for i, c in enumerate(cands, 1):
        lines += [
            f"【候選回應 {i}】",
            f"doc_id：{c['id']}",
            f"具奏官員：{c['author']}",
            f"上奏日：{c['sendAr'] or '未明'}",
            f"硃批／收受日：{c['recvAr'] or '未明'}",
            f"結構日期依據：{c.get('date_basis') or '未明'}",
            f"距上諭：{c['lag_days']} 日"
            + (f"（該官平均往返約 {c['transit_est']} 日）" if c["transit_est"] else ""),
            "引用段落：\n" + ("\n---\n".join(c["passages"]) or "（未偵測到引用標記）"),
            "",
        ]
    return "\n".join(lines)


# Transient proxy hiccups (Cloud Run cold starts, overload) return these; a
# reverse run makes ~12 calls, so retry rather than lose the whole run to one.
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
        rid = str(p.get("reply_doc_id", "")).strip()
        if rid not in valid:
            continue
        pairs.append({
            "reply_doc_id": rid,
            "yu_doc_id": edict_id,
            "relation": "reply_to_yu",
            "match_level": p.get("match_level", "weak"),
            "evidence": p.get("evidence", {}),
        })
    return pairs


def build_jobs(anchor, records, transit, reverse_cap=MAX_CANDIDATES):
    """Return [(edict, [reply_cand,…]), …] for either direction, chosen by the
    anchor's type: an 上諭 anchors a forward search (its replies); an official doc
    anchors a reverse search (the 上諭 it answers)."""
    if anchor.get("type") == "shangyu":
        return [(anchor, candidates_for(anchor, records, transit))]
    return edicts_for(anchor, records, transit, reverse_cap)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--proxy", default=os.environ.get("GEMINI_PROXY_URL", ""))
    ap.add_argument("--doc-id", help="Analyse one document — an 上諭 (find its replies) "
                    "OR an official doc (find the 上諭 it answers). Direction is auto.")
    ap.add_argument("--all", action="store_true", help="Analyse every 上諭 (forward).")
    ap.add_argument("--reverse-month", metavar="YYYY/MM",
                    help="Reverse-pair every official doc SENT in this month "
                    "(e.g. 1787/01) — find the 上諭 each one answers.")
    ap.add_argument("--rescan-multi", action="store_true",
                    help="Rescan every official document whose text cites two or "
                    "more dated 上諭s, merging new pairs into the existing output.")
    ap.add_argument("--skip-done", action="store_true",
                    help="Skip docs already present in the existing output and merge "
                    "new results into it (resume a long run).")
    ap.add_argument("--model", default="gemini-3.5-flash")
    ap.add_argument("--workers", type=int, default=8,
                    help="Concurrent proxy calls (default 8). Use 1 for serial.")
    ap.add_argument("--reverse-cap", type=int, default=12,
                    help="In reverse mode, max 上諭 candidates examined per official "
                    "doc — each is one proxy call. Default 12 for undated/topic "
                    "fallbacks; explicitly cited issue-date candidates are always kept.")
    ap.add_argument("--dry-run", action="store_true", help="Show candidates; no proxy call.")
    ap.add_argument("--include-weak", action="store_true",
                    help="Keep weak (non-matching-date) pairs too; default drops them.")
    ap.add_argument("--bundle-name", default="yu-pairing")
    args = ap.parse_args()

    records = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    by_id = {r.get("id"): r for r in records}
    global _KNOWN_OFFICIALS
    _KNOWN_OFFICIALS = build_known_officials(records)
    transit = transit_estimates(records)

    out_path = ROOT / "outputs" / "attempt-002" / "yu-pairing.json"
    existing_pairs, existing_analyzed, done_ids = [], [], set()
    if args.skip_done and out_path.exists():
        prev = json.loads(out_path.read_text(encoding="utf-8"))
        if isinstance(prev, dict):
            existing_pairs, existing_analyzed = prev.get("pairs", []), prev.get("analyzed", [])
        else:
            existing_pairs = prev  # legacy flat-array format
        done_ids = {p.get("reply_doc_id") for p in existing_pairs} | {p.get("yu_doc_id") for p in existing_pairs}

    if args.doc_id:
        anchors = []
        for one in (x.strip() for x in args.doc_id.split(",") if x.strip()):
            rec = by_id.get(one)
            if not rec:
                ap.error(f"document not found: {one}")
            anchors.append(rec)
    elif args.rescan_multi:
        anchors = [r for r in records
                   if r.get("type") != "shangyu"
                   and len(explicit_citation_dates(r.get("body") or "")) >= 2]
    elif args.all:
        anchors = [r for r in records if r.get("type") == "shangyu"]
    elif args.reverse_month:
        anchors = [r for r in records
                   if r.get("type") != "shangyu"
                   and (r.get("sendAr") or "").startswith(args.reverse_month)]
    else:
        ap.error("Pass --doc-id, --all, or --reverse-month YYYY/MM.")

    if args.skip_done:
        # An official document may answer several 上諭s.  When the researcher
        # explicitly names a document, allow it to be rescanned even if one
        # earlier pair already exists; otherwise --skip-done would permanently
        # freeze a partial result (the 台301 failure mode).
        requested = {x.strip() for x in (args.doc_id or "").split(",") if x.strip()}
        if not args.rescan_multi:
            anchors = [a for a in anchors
                       if a.get("id") not in done_ids or a.get("id") in requested]

    # every doc we run the model on this pass — used so the site can show a
    # "no results" card for analyzed docs that produced no pair.
    run_analyzed = [a.get("id") for a in anchors]

    jobs = []
    for anchor in anchors:
        direction = "forward" if anchor.get("type") == "shangyu" else "reverse"
        jobs.extend((direction, anchor, ed, cands)
                    for ed, cands in build_jobs(anchor, records, transit, args.reverse_cap))

    if args.dry_run:
        for direction, anchor, edict, cands in jobs:
            tag = f"{anchor['id']} → 上諭 {edict['id']}" if direction == "reverse" else edict["id"]
            print(f"\n== [{direction}] {tag} ({edict.get('annAr') or edict.get('sendAr')}) "
                  f"受命：{'、'.join(recipients_of(edict))} ==")
            for c in cands:
                flag = "★cites-date" if c["cites_edict_date"] else ""
                print(f"  {c['id']:>6}  {c['author']:<6} {c['sendAr']}  +{c['lag_days']}d  {flag}")
                for p in c["passages"][:1]:
                    print(f"        「{p[:60]}…」")
        return 0

    # one proxy call per (edict, cands) job; run them concurrently since each is
    # an independent I/O-bound request (Cloud Run autoscales, call_proxy retries
    # transient 429/5xx). Order of completion doesn't matter — results are merged
    # and de-duplicated below.
    proxy_jobs = [(edict, cands) for _direction, _anchor, edict, cands in jobs if cands]
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

    # Drop weak pairs by default — a reply cites one edict, but its content
    # overlaps a whole series, so every near-identical edict comes back as a
    # weak candidate and floods the review with noise. Keep high/partial only
    # (the ones whose cited date/quote actually match) unless --include-weak.
    kept = all_pairs if args.include_weak else [p for p in all_pairs if p.get("match_level") != "weak"]
    dropped = len(all_pairs) - len(kept)

    # merge with prior results when resuming, then de-duplicate (reverse mode can
    # also re-surface a pair found forward)
    seen, deduped = set(), []
    for p in existing_pairs + kept:
        key = (p["reply_doc_id"], p["yu_doc_id"])
        if key not in seen:
            seen.add(key)
            deduped.append(p)

    analyzed = sorted(set(existing_analyzed) | {a for a in run_analyzed if a})
    result = {"pairs": deduped, "analyzed": analyzed}
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # website-loadable bundle (renders one card per pair; a "no results" card for
    # each analyzed doc that produced none)
    bundle_root = ROOT / "outputs" / "review-bundles" / args.bundle_name
    (bundle_root / "outputs").mkdir(parents=True, exist_ok=True)
    (bundle_root / "outputs" / "yu-pairing.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (bundle_root / "manifest.json").write_text(json.dumps({
        "name": args.bundle_name,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "source": "outputs/attempt-002/dual-timeline-data.json",
        "doc_ids": sorted({p["yu_doc_id"] for p in deduped} | {p["reply_doc_id"] for p in deduped}),
        "chain": ["yu-pairing"],
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(out_path)
    print(bundle_root)
    print(f"pairs: {len(deduped)} (dropped {dropped} weak; use --include-weak to keep)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
