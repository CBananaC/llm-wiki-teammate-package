#!/usr/bin/env python3
"""Run a small local review-bundle test through the Gemini proxy.

Example:
  GEMINI_PROXY_URL=https://... python3 "tool/scripts py/run_review_bundle_test.py" --limit 2
"""

from __future__ import annotations

import argparse
import http.client
import json
import os
import re
import time
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "outputs" / "attempt-002" / "stage1_original_text.json"
SKILLS_DIR = ROOT / "tool" / "skills md"

# Chain step -> the skill file that owns its prompt text. Same skill file is
# read by the website (via review-app's /api/skills) for the single-doc
# "top up during review" buttons, so both paths always use identical wording.
STEP_SKILL = {
    "summary": "quick-summary.md",
    "divide": "divide-into-parts.md",
    "lin-events": "extract-lin-actions.md",
    "source-chain": "trace-source-chain.md",
    "qing-events-done": "extract-qing-actions-done.md",
    "qing-events-plan": "extract-qing-actions-planned.md",
    "qing-events-nonmil": "extract-qing-nonmilitary-actions.md",
    "zhupi": "extract-zhupi.md",
    "edict-match": "edict-match.md",
    "official-response": "official-response.md",
}

# qing-events-* steps all use proxy mode "events" with actor=qing and a
# category; this table drives the generic qing-events loop below.
QING_EVENT_CATEGORY = {
    "qing-events-done": "done",
    "qing-events-plan": "plan",
    "qing-events-nonmil": "nonmil",
}

_WEBSITE_PROMPT_RE = re.compile(r"^##\s*Website Prompt[ \t]*\n(.*?)(?=\n##\s|\Z)", re.S | re.M)



# A provenance hop's from_person/to_person is free text pulled from wherever the source document
# happened to name that person AT THAT POINT -- the same real person can appear in one hop as a
# bare name ("程峻") and in another as "署北路淡水同知程峻", or "黃仕簡" vs "福建水師提督黃仕簡".
# Comparing hop signatures on the raw strings then treats one real transmission chain as several
# different ones just because an official's post was or wasn't spelled out that time. Strip a
# leading run of place/rank/office words (plus an "署"/"署理" acting-post marker) down to the bare
# personal name, and sort a multi-person hop label ("程峻、董得魁" vs "董得魁、程峻") so word order
# doesn't matter either. Keep this in sync with normPersonForChain() in stage1-timeline.html.
_CHAIN_TITLE_WORDS = (
    "署理|護理|署|福建|臺灣|北路|南路|中路|水師|陸路|淡水|彰化|諸羅|鳳山|噶瑪蘭|艋舺|鹿港|"
    "城守|副將|參將|遊擊|都司|守備|千總|把總|同知|通判|知府|知縣|知州|道員|按察使|布政使|"
    "巡撫|總督|提督|將軍|都統|大學士|總兵|副總兵|參領|佐領|通事|廳|營|汛"
)
_CHAIN_TITLE_RE = re.compile(rf"^(?:{_CHAIN_TITLE_WORDS})+")


def _norm_person_for_chain(name: str) -> str:
    parts = re.split(r"[、,，]", name or "")
    out = []
    for p in parts:
        s = p.strip()
        while True:
            stripped = _CHAIN_TITLE_RE.sub("", s)
            if stripped == s:
                break
            s = stripped
        out.append((s or p.strip()).strip())
    return "、".join(sorted(x for x in out if x))


def _chain_signature(chain: dict) -> str:
    hops = chain.get("hops") or []
    return "|".join(
        f"{_norm_person_for_chain(h.get('from_person',''))}>{_norm_person_for_chain(h.get('to_person',''))}"
        for h in hops
    )


def merge_source_chains_by_signature(source_chains: list[dict]) -> list[dict]:
    """The source-chain step above calls the trace proxy ONCE PER EXTRACTED EVENT, so the raw
    per-call records repeat the exact same chain once for every event that happens to share it
    (e.g. two events both reported by the same official through the same relay) -- loaded as-is,
    the website shows "event A: chain 1" then a separate "event B: chain 1" instead of one "chain 1:
    events A, B" entry. Group by doc_id (each document keeps its own chat log on the website side)
    and, within a document, merge chains with an identical hop signature so each distinct chain is
    listed once with every event it accounts for, matching how the live in-app trace/追溯 buttons
    already behave (see chainSig/bySig in stage1-timeline.html's runTraceBatch)."""
    by_doc: dict[str, list[dict]] = {}
    for rec in source_chains:
        doc_id = str(rec.get("doc_id") or "")
        by_doc.setdefault(doc_id, []).append(rec)

    merged_rows = []
    for doc_id, records in by_doc.items():
        merged: list[dict] = []
        by_sig: dict[str, dict] = {}
        for rec in records:
            event = rec.get("event") or {}
            fallback_event = {
                "subtitle": rec.get("evTitle") or event.get("subtitle") or "",
                "reporter": "",
                "whenCh": event.get("whenCh") or "",
                "where": event.get("where") or "",
                "quote": event.get("quote") or "",
                "doc_id": doc_id,
            }
            for chain in rec.get("chains") or []:
                chain = dict(chain)
                chain["hops"] = chain.get("hops") or []
                if not chain.get("events"):
                    chain["events"] = [fallback_event]
                sig = _chain_signature(chain)
                existing = by_sig.get(sig)
                if existing:
                    known = {e.get("subtitle") for e in existing["events"]}
                    for ev in chain["events"]:
                        if ev.get("subtitle") not in known:
                            existing["events"].append(ev)
                            known.add(ev.get("subtitle"))
                else:
                    by_sig[sig] = chain
                    merged.append(chain)
        label = f"本機來源鏈（{len(records)} 個事件，合併為 {len(merged)} 條鏈）" if len(records) > 1 else (records[0].get("evTitle") or "本機來源鏈")
        merged_rows.append({"doc_id": doc_id, "evTitle": label, "chains": merged})
    return merged_rows


def skill_prompt(step: str) -> str:
    """Read the '## Website Prompt' section of the skill file mapped to this
    step. Returns '' if the skill file is missing or has no such section, in
    which case callers should fall back to the proxy's built-in default."""
    fname = STEP_SKILL.get(step)
    if not fname:
        return ""
    path = SKILLS_DIR / fname
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    m = _WEBSITE_PROMPT_RE.search(text)
    if not m:
        return ""
    body = m.group(1).strip()
    fence = re.match(r"^```[a-zA-Z]*\n(.*?)\n```$", body, re.S)
    return fence.group(1).strip() if fence else body


# ---- token accounting -------------------------------------------------------
# Per-step (== per proxy "mode") token totals. Uses the exact `usage` the proxy
# returns when present; otherwise falls back to a CJK-aware estimate (marked ~).
TOKEN_STATS: dict[str, dict] = {}


def _est_tokens(s: str) -> int:
    s = s or ""
    cjk = sum(1 for ch in s if "㐀" <= ch <= "鿿")
    return int(cjk + (len(s) - cjk) / 4)


def _record_step_tokens(step: str, payload: dict, result: dict) -> None:
    st = TOKEN_STATS.setdefault(step, {"calls": 0, "prompt": 0, "completion": 0, "total": 0, "exact": True})
    st["calls"] += 1
    usage = result.get("usage") if isinstance(result, dict) else None
    if isinstance(usage, dict) and (usage.get("total_tokens") or usage.get("prompt_tokens") or usage.get("completion_tokens")):
        p = int(usage.get("prompt_tokens") or 0)
        c = int(usage.get("completion_tokens") or 0)
        t = int(usage.get("total_tokens") or (p + c))
    else:
        p = _est_tokens(json.dumps(payload, ensure_ascii=False))
        c = _est_tokens(json.dumps(result, ensure_ascii=False))
        t = p + c
        st["exact"] = False
    st["prompt"] += p
    st["completion"] += c
    st["total"] += t
    tag = "" if st["exact"] else "~"
    print(f"    [tokens] {step}: {tag}{t} (prompt {p} + completion {c})")


def print_token_summary() -> None:
    if not TOKEN_STATS:
        print("\n=== Token usage: no successful AI calls ===")
        return
    print("\n=== Token usage by step ===")
    print(f"{'step':<20}{'calls':>7}{'prompt':>13}{'completion':>13}{'total':>13}")
    gp = gc = gt = gcalls = 0
    any_est = False
    for step in sorted(TOKEN_STATS):
        st = TOKEN_STATS[step]
        tag = "" if st["exact"] else "~"
        any_est = any_est or not st["exact"]
        print(f"{step:<20}{st['calls']:>7}{tag + str(st['prompt']):>13}{tag + str(st['completion']):>13}{tag + str(st['total']):>13}")
        gp += st["prompt"]; gc += st["completion"]; gt += st["total"]; gcalls += st["calls"]
    print("-" * 66)
    print(f"{'ALL STEPS':<20}{gcalls:>7}{gp:>13}{gc:>13}{gt:>13}")
    if any_est:
        print("~ = estimated (proxy did not return exact usage; redeploy gemini-proxy for exact counts)")


def post_json(url: str, payload: dict[str, Any], timeout: int, retries: int = 3, retry_sleep: int = 12) -> dict[str, Any]:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        url.rstrip("/") + "/chat",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    last: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                result = json.loads(resp.read().decode("utf-8"))
                try:
                    _record_step_tokens(str(payload.get("mode") or "?"), payload, result)
                except Exception:
                    pass
                return result
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code not in {429, 500, 502, 503, 504} or attempt >= retries:
                raise
            factor = 5 if exc.code == 429 else 1
            delay = retry_sleep * attempt * factor
            print(f"    retry {attempt}/{retries} after HTTP {exc.code}; waiting {delay}s")
            time.sleep(delay)
        except (urllib.error.URLError, TimeoutError, http.client.RemoteDisconnected, ConnectionError) as exc:
            last = exc
            if attempt >= retries:
                raise
            delay = retry_sleep * attempt * 3
            print(f"    retry {attempt}/{retries} after {exc}; waiting {delay}s")
            time.sleep(delay)
    raise last or RuntimeError("request failed")


def record_payload(record: dict[str, Any], mode: str, model: str) -> dict[str, Any]:
    return {
        "mode": mode,
        "model": model,
        "doc_id": record.get("doc_id") or record.get("id"),
        "doc_type": record.get("doc_type"),
        "title": record.get("title"),
        "body": record.get("body") or "",
        "rescript": record.get("rescript_text") or record.get("rescript") or "",
        "summary": {},
    }


def date_pair_value(record: dict[str, Any], key: str) -> str:
    value = record.get(key)
    if isinstance(value, list) and len(value) > 1:
        return value[1] or ""
    return ""


def primary_date(record: dict[str, Any]) -> str:
    doc_type = record.get("doc_type")
    if doc_type == "上諭":
        return date_pair_value(record, "announce_date") or date_pair_value(record, "send_date") or date_pair_value(record, "receive_date")
    if doc_type == "硃批":
        return date_pair_value(record, "receive_date") or date_pair_value(record, "send_date")
    return date_pair_value(record, "send_date") or date_pair_value(record, "receive_date") or date_pair_value(record, "announce_date")


def all_record_dates(record: dict[str, Any]) -> list[str]:
    return [
        d for d in [
            date_pair_value(record, "send_date"),
            date_pair_value(record, "receive_date"),
            date_pair_value(record, "announce_date"),
            date_pair_value(record, "issue_date"),
        ]
        if d
    ]


def in_range(value: str, start: str, end: str) -> bool:
    if not value:
        return False
    value = value.replace("/", "-")
    return start <= value <= end


def parse_date(value: str):
    value = (value or "").replace("/", "-")
    if not re.fullmatch(r"\d{4}-\d{1,2}-\d{1,2}", value):
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None


def quote_is_verbatim(source: str, quote: str) -> bool:
    normalized_source = re.sub(r"\s+", "", str(source or ""))
    normalized_quote = re.sub(r"\s+", "", str(quote or ""))
    return bool(normalized_quote) and normalized_quote in normalized_source


# --- Chinese reign-date completion (ported from parseChFull / convertWhenCh in
#     stage1-timeline.html). Keeps the CHINESE date primary and reviewable: it
#     fills the missing reign year onto an event's whenCh using the parent
#     document's own date, and derives a SECONDARY Gregorian whenAr with the same
#     naive calendar mapping the website's event dots use (十二月十八日 -> 1786/12/18).
_CN_DIGITS = {"\u96f6": 0, "\u3007": 0, "\u4e00": 1, "\u4e8c": 2, "\u5169": 2,
              "\u4e09": 3, "\u56db": 4, "\u4e94": 5, "\u516d": 6, "\u4e03": 7,
              "\u516b": 8, "\u4e5d": 9}
_CN_UNITS = "\u96f6\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d"  # 零一二三四五六七八九


def _cnum(text):
    if not text:
        return None
    text = str(text).strip()
    if text.isdigit():
        return int(text)
    if text == "\u6b63":            # 正 -> 1
        return 1
    if text == "\u5341":            # 十 -> 10
        return 10
    if "\u5341" in text:            # X十Y
        a, _, b = text.partition("\u5341")
        tens = _CN_DIGITS.get(a, 0) if a else 1
        ones = _CN_DIGITS.get(b, 0) if b else 0
        return tens * 10 + ones
    value = 0
    for ch in text:
        if ch in _CN_DIGITS:
            value = value * 10 + _CN_DIGITS[ch]
    return value or None


def _cday_num(text):
    if not text:
        return None
    text = str(text).replace("\u521d", "").strip()   # strip 初
    if text.isdigit():
        return int(text)
    if text == "\u5eff":            # 廿 -> 20
        return 20
    if text == "\u5350":            # 卅 -> 30
        return 30
    if "\u5eff" in text:
        return 20 + (_cnum(text.replace("\u5eff", "")) or 0)
    if "\u5350" in text:
        return 30 + (_cnum(text.replace("\u5350", "")) or 0)
    return _cnum(text)


_RY_RE = re.compile(r"\u4e7e(?:\u9686)?\s*([0-9\u96f6\u3007\u4e00\u4e8c\u5169\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341]+)\s*\u5e74")
_MM_RE = re.compile(r"(?:\u958f)?\s*([0-9\u6b63\u4e00\u4e8c\u5169\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341]+)\s*\u6708")
_DD_RE = re.compile(r"\u6708\s*([0-9\u521d\u5eff\u5350\u4e00\u4e8c\u5169\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341]+)\s*\u65e5")


def _parse_ch_full(ch):
    if not ch:
        return None
    s = str(ch)
    ry = _RY_RE.search(s)
    mm = _MM_RE.search(s)
    dd = _DD_RE.search(s)
    lm = (1 if mm and mm.group(1) == "\u6b63" else _cnum(mm.group(1))) if mm else None
    return {
        "ry": _cnum(ry.group(1)) if ry else None,
        "lm": lm,
        "ld": _cday_num(dd.group(1)) if dd else None,
        "leap": "\u958f" in s,          # 閏
    }


def _int_to_cn(n):
    if n is None or n < 0:
        return "" if n is None else str(n)
    if n < 10:
        return "" if n == 0 else _CN_UNITS[n]
    if n < 20:
        return "\u5341" + ("" if n == 10 else _CN_UNITS[n - 10])
    tens, ones = divmod(n, 10)
    return _CN_UNITS[tens] + "\u5341" + ("" if ones == 0 else _CN_UNITS[ones])


def _day_to_cn(d):
    if not d:
        return ""
    if d <= 10:
        return "\u521d" + _int_to_cn(d)      # 初X
    if d < 20:
        return _int_to_cn(d)
    if d == 20:
        return "\u4e8c\u5341"               # 二十
    if d < 30:
        return "\u4e8c\u5341" + _CN_UNITS[d - 20]
    if d == 30:
        return "\u4e09\u5341"               # 三十
    return _int_to_cn(d)


def _doc_ref_ch(record):
    """The parent document's own Chinese date, used ONLY to supply the reign year
    an event's date string omits. Send first, then receive/announce/issue."""
    for key in ("send_date", "receive_date", "announce_date", "issue_date"):
        value = record.get(key)
        if isinstance(value, list) and value and value[0]:
            return str(value[0])
    return ""


def _complete_one(when_ch, ref):
    """Return (chinese_full, gregorian) for one raw Chinese date string, filling
    the reign year from `ref` (the doc's parsed date) when the string omits it.
    Chinese is primary; Gregorian uses the site's naive calendar mapping and is a
    YYYY/MM month-only value when the day is unknown."""
    p = _parse_ch_full(when_ch)
    if not p or not p["lm"]:
        return "", ""
    ry = p["ry"]
    if ry is None and ref:
        ry = ref.get("ry")
        if ry is not None and ref.get("lm") and p["lm"] > ref["lm"]:
            ry -= 1               # event month after the doc's month -> previous reign year
    if ry is None:
        return "", ""
    leap = "\u958f" if p["leap"] else ""    # 閏
    gy = 1735 + ry
    if p["ld"]:
        cn = "\u4e7e\u9686%s\u5e74%s%s\u6708%s\u65e5" % (
            _int_to_cn(ry), leap, _int_to_cn(p["lm"]), _day_to_cn(p["ld"]))
        greg = "%d/%02d/%02d" % (gy, p["lm"], p["ld"])
    else:
        cn = "\u4e7e\u9686%s\u5e74%s%s\u6708" % (_int_to_cn(ry), leap, _int_to_cn(p["lm"]))
        greg = "%d/%02d" % (gy, p["lm"])
    return cn, greg


def complete_event_dates(item, record):
    """Fill the reign year onto an event's Chinese date IN PLACE, keeping the
    Chinese date primary (whenChFull) and adding a secondary Gregorian whenAr.
    Events with no parsable date fall back to the document's own send date."""
    if not isinstance(item, dict):
        return item
    ref = _parse_ch_full(_doc_ref_ch(record))
    cn, greg = _complete_one(item.get("whenCh") or "", ref)
    if cn:
        item["whenChFull"] = cn
        model_ar = (item.get("whenAr") or "").strip()
        if model_ar and model_ar != greg:
            item["_whenArModel"] = model_ar     # keep model's own guess for traceability
        item["whenAr"] = greg
        raw = _parse_ch_full(item.get("whenCh") or "") or {}
        item["dateSource"] = "event" if raw.get("ry") else "event-year-inferred"
    else:
        item["whenChFull"] = ""
        item["dateSource"] = "doc-send"          # no event date -> display uses the doc's send date
        item["whenChFallback"] = _doc_ref_ch(record)
        item["whenArFallback"] = (
            date_pair_value(record, "send_date") or date_pair_value(record, "receive_date"))
    known = item.get("whenKnownCh") or ""
    if known:
        kcn, _kgreg = _complete_one(known, ref)
        if kcn:
            item["whenKnownChFull"] = kcn
    return item


def within_days(value: str, base: str, days: int) -> bool:
    dv = parse_date(value)
    db = parse_date(base)
    return bool(dv and db and abs((dv - db).days) <= days)


def doc_best_ar(record: dict[str, Any]) -> str:
    return (
        date_pair_value(record, "send_date")
        or date_pair_value(record, "receive_date")
        or date_pair_value(record, "announce_date")
    )


def official_response_candidates(
    records: list[dict[str, Any]], base_date: str, exclude_doc_id: str,
    addressee_names: list[str], window_days: int = 30, max_count: int = 40,
) -> list[dict[str, Any]]:
    """Python mirror of officialResponseCandidates()/actionRecipients() in stage1-timeline.html:
    documents dated in the ~30 days AFTER an emperor-action's own date, narrowed to the addressed
    official (by author_name or recipients) when a name is known, falling back to the unnarrowed
    date-window list only if that narrowing would eliminate every candidate. Capped and sorted by
    closeness to the action date, same reasoning as the website (a 30-day window on a dense corpus
    can pull in 100+ candidates with no addressee filter, burying the real response in noise)."""
    base = parse_date(base_date)
    if not base:
        return []
    dated: list[tuple[int, dict[str, Any]]] = []
    for r in records:
        doc_id = str(r.get("doc_id") or r.get("id"))
        if doc_id == str(exclude_doc_id):
            continue
        d = parse_date(doc_best_ar(r))
        if not d:
            continue
        diff = (d - base).days
        if 0 < diff <= window_days:
            dated.append((diff, r))
    names = [n for n in (addressee_names or []) if n]
    if names:
        def matches(r: dict[str, Any]) -> bool:
            author = str(r.get("author_name") or "")
            if author and any(n in author or author in n for n in names):
                return True
            for rc in r.get("recipients") or []:
                rc = str(rc or "")
                if rc and any(n in rc or rc in n for n in names):
                    return True
            return False
        narrowed = [(diff, r) for diff, r in dated if matches(r)]
        if narrowed:
            dated = narrowed
    dated.sort(key=lambda x: x[0])
    return [r for _, r in dated[:max_count]]


def split_csv(value: str) -> list[str]:
    return [s.strip() for s in value.split(",") if s.strip()]


def read_json(path: Path, fallback):
    if not path.exists():
        return fallback
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--proxy", default=os.environ.get("GEMINI_PROXY_URL", ""), help="Gemini proxy base URL")
    ap.add_argument("--model", default=os.environ.get("GEMINI_MODEL", "gemini-2.5-flash"))
    ap.add_argument("--limit", type=int, default=2)
    ap.add_argument("--offset", type=int, default=0)
    ap.add_argument("--doc-ids", default="", help="Comma-separated doc IDs to run, e.g. 台8,台44")
    ap.add_argument("--date-from", default="", help="Primary document date from, yyyy-mm-dd")
    ap.add_argument("--date-to", default="", help="Primary document date to, yyyy-mm-dd")
    ap.add_argument("--date-mode", choices=["primary", "any"], default="primary", help="primary = one timeline date per doc; any = any send/receive/announce/issue date")
    ap.add_argument("--doc-types", default="", help="Comma-separated doc types, e.g. 上奏,硃批,上諭")
    ap.add_argument("--steps", default="summary,divide,lin-events", help="Comma-separated: summary,divide,lin-events,source-chain,qing-events-done,qing-events-plan,qing-events-nonmil,zhupi,edict-match,official-response")
    ap.add_argument("--bundle", default="")
    ap.add_argument("--timeout", type=int, default=180)
    ap.add_argument("--skip-done", action="store_true", help="Resume an existing bundle and skip completed doc-level outputs")
    ap.add_argument("--retries", type=int, default=4)
    ap.add_argument("--retry-sleep", type=int, default=15)
    args = ap.parse_args()

    if not args.proxy:
        raise SystemExit("Set GEMINI_PROXY_URL or pass --proxy.")

    records = json.loads(SOURCE.read_text(encoding="utf-8"))
    if args.doc_ids.strip():
        wanted = [s.strip() for s in args.doc_ids.split(",") if s.strip()]
        by_id = {str(r.get("doc_id") or r.get("id")): r for r in records}
        missing = [doc_id for doc_id in wanted if doc_id not in by_id]
        if missing:
            raise SystemExit("Missing doc_id(s): " + ", ".join(missing))
        docs = [by_id[doc_id] for doc_id in wanted]
    else:
        docs = records
        types = set(split_csv(args.doc_types))
        if types:
            docs = [r for r in docs if r.get("doc_type") in types]
        if args.date_from or args.date_to:
            start = (args.date_from or "0000-01-01").replace("/", "-")
            end = (args.date_to or "9999-12-31").replace("/", "-")
            if args.date_mode == "any":
                docs = [r for r in docs if any(in_range(d, start, end) for d in all_record_dates(r))]
            else:
                docs = [r for r in docs if in_range(primary_date(r), start, end)]
        docs = docs[args.offset : args.offset + args.limit]
    steps = set(split_csv(args.steps))
    bundle_name = args.bundle or f"test-first-{args.limit}-docs-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    out_root = ROOT / "outputs" / "review-bundles" / bundle_name
    (out_root / "outputs").mkdir(parents=True, exist_ok=True)
    (out_root / "human-edits").mkdir(parents=True, exist_ok=True)

    manifest = {
        "name": bundle_name,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "source": str(SOURCE.relative_to(ROOT)),
        "offset": args.offset,
        "limit": args.limit,
        "date_from": args.date_from,
        "date_to": args.date_to,
        "date_mode": args.date_mode,
        "doc_types": split_csv(args.doc_types),
        "model": args.model,
        "doc_ids": [d.get("doc_id") or d.get("id") for d in docs],
        "chain": [s for s in ["summary", "divide", "lin-events", "source-chain",
                              "qing-events-done", "qing-events-plan", "qing-events-nonmil", "zhupi", "edict-match",
                              "official-response"] if s in steps],
    }

    summary_path = out_root / "outputs" / "summary.json"
    divisions_path = out_root / "outputs" / "division-parts.json"
    lin_events_path = out_root / "outputs" / "lin-events.json"
    source_chains_path = out_root / "outputs" / "source-chain.json"
    status_path = out_root / "outputs" / "_run-status.json"
    summaries = read_json(summary_path, []) if args.skip_done else []
    divisions = read_json(divisions_path, []) if args.skip_done else []
    lin_events = read_json(lin_events_path, []) if args.skip_done else []
    source_chains = read_json(source_chains_path, []) if args.skip_done else []
    status = read_json(status_path, {}) if args.skip_done else {}

    # qing-events-* / zhupi: same "one JSON list, one output file" pattern,
    # keyed generically by step name so a new QING_EVENT_CATEGORY entry
    # doesn't need new boilerplate below.
    extra_paths = {step: out_root / "outputs" / f"{step}.json" for step in (*QING_EVENT_CATEGORY, "zhupi", "edict-match")}
    extra_rows = {step: (read_json(p, []) if args.skip_done else []) for step, p in extra_paths.items()}
    extra_done = {step: {str(r.get("doc_id")) for r in rows if r.get("doc_id")} for step, rows in extra_rows.items()}
    all_edicts = [r for r in records if r.get("doc_type") == "上諭"]
    edicts_by_id = {str(r.get("doc_id") or r.get("id")): r for r in all_edicts}

    def done_docs(rows: list[dict[str, Any]]) -> set[str]:
        return {str(r.get("doc_id")) for r in rows if r.get("doc_id")}

    summary_done = done_docs(summaries)
    division_done = done_docs(divisions)
    event_done = done_docs(lin_events)
    chain_done = {(str(r.get("doc_id")), str(r.get("evTitle") or "")) for r in source_chains if r.get("doc_id")}

    def mark_done(doc_id: str, step: str) -> None:
        status.setdefault(str(doc_id), {})[step] = True
        write_json(status_path, status)

    def is_done(doc_id: str, step: str) -> bool:
        return bool(status.get(str(doc_id), {}).get(step))

    for i, doc in enumerate(docs, 1):
        doc_id = doc.get("doc_id") or doc.get("id")
        print(f"[{i}/{len(docs)}] {doc_id} {doc.get('doc_type')} {doc.get('title')}")

        if "summary" in steps:
            if args.skip_done and (str(doc_id) in summary_done or is_done(doc_id, "summary")):
                print("  - summary (skip done)")
            else:
                print("  - summary")
                s_payload = record_payload(doc, "summary", args.model)
                s_instruction = skill_prompt("summary")
                if s_instruction:
                    s_payload["instruction"] = s_instruction
                s = post_json(args.proxy, s_payload, args.timeout, args.retries, args.retry_sleep)
                summaries.append({
                    "doc_id": doc_id,
                    "title": doc.get("title"),
                    "summary": s.get("text", ""),
                    "analysis": {"what_info_telling_emperor": s.get("text", "")},
                    "_raw": s,
                })
                summary_done.add(str(doc_id))
                write_json(summary_path, summaries)
                mark_done(doc_id, "summary")

        if "divide" in steps:
            if args.skip_done and (str(doc_id) in division_done or is_done(doc_id, "divide")):
                print("  - divide (skip done)")
            else:
                print("  - divide")
                d_payload = record_payload(doc, "divide", args.model)
                d_instruction = skill_prompt("divide")
                if d_instruction:
                    d_payload["instruction"] = d_instruction
                d = post_json(args.proxy, d_payload, args.timeout, args.retries, args.retry_sleep)
                divisions.append({
                    "doc_id": doc_id,
                    "title": doc.get("title"),
                    "parts": d.get("parts", []),
                    "_raw": d,
                })
                division_done.add(str(doc_id))
                write_json(divisions_path, divisions)
                mark_done(doc_id, "divide")

        doc_events = []
        if "lin-events" in steps or "source-chain" in steps:
            if args.skip_done and (str(doc_id) in event_done or is_done(doc_id, "lin-events")):
                print("  - 林方行動 (skip done)")
                doc_events = [e for e in lin_events if str(e.get("doc_id")) == str(doc_id)]
            else:
                print("  - 林方行動")
                ev_payload = record_payload(doc, "events", args.model)
                ev_payload.update({
                    "actor": "lin",
                    "category": "",
                    "actor_instruction": skill_prompt("lin-events"),
                })
                e = post_json(args.proxy, ev_payload, args.timeout, args.retries, args.retry_sleep)
                for item in e.get("events", []):
                    item.setdefault("doc_id", doc_id)
                    complete_event_dates(item, doc)
                    doc_events.append(item)
                    if "lin-events" in steps:
                        lin_events.append(item)
                event_done.add(str(doc_id))
                if "lin-events" in steps:
                    write_json(lin_events_path, lin_events)
                mark_done(doc_id, "lin-events")

        if "source-chain" in steps:
            if args.skip_done and is_done(doc_id, "source-chain"):
                print("  - 林方來源鏈 (skip done)")
            else:
                for j, item in enumerate(doc_events, 1):
                    title = item.get("subtitle") or ""
                    if args.skip_done and (str(doc_id), str(title)) in chain_done:
                        print(f"  - 林方來源鏈 {j}/{len(doc_events)} (skip done): {title}")
                        continue
                    print(f"  - 林方來源鏈 {j}/{len(doc_events)}: {title}")
                    quote = item.get("quote") or ""
                    tr_payload = record_payload(doc, "trace", args.model)
                    tr_extra = skill_prompt("source-chain")
                    tr_payload.update({
                        "side": "lin",
                        "single": True,
                        **({"question": tr_extra} if tr_extra else {}),
                        "event": {
                            "actor": "lin",
                            "subtitle": item.get("subtitle") or "",
                            "description": item.get("description") or "",
                            "where": item.get("where") or "",
                            "whenCh": item.get("whenCh") or item.get("whenAr") or "",
                            "quote": quote,
                        },
                    })
                    try:
                        tr = post_json(args.proxy, tr_payload, args.timeout, args.retries, args.retry_sleep)
                    except Exception as exc:
                        print(f"    source-chain failed, saved error and continuing: {exc}")
                        tr = {"mode": "trace", "chains": [], "error": str(exc)}
                    source_chains.append({
                        "doc_id": doc_id,
                        "evTitle": title,
                        "event": item,
                        "chains": tr.get("chains", []),
                        "_raw": tr,
                    })
                    chain_done.add((str(doc_id), str(title)))
                    write_json(source_chains_path, source_chains)
                mark_done(doc_id, "source-chain")

        for step, category in QING_EVENT_CATEGORY.items():
            if step not in steps:
                continue
            if args.skip_done and (str(doc_id) in extra_done[step] or is_done(doc_id, step)):
                print(f"  - {step} (skip done)")
                continue
            print(f"  - {step}")
            qe_payload = record_payload(doc, "events", args.model)
            qe_payload.update({
                "actor": "qing",
                "category": category,
                "actor_instruction": skill_prompt(step),
            })
            qe = post_json(args.proxy, qe_payload, args.timeout, args.retries, args.retry_sleep)
            for item in qe.get("events", []):
                item.setdefault("doc_id", doc_id)
                complete_event_dates(item, doc)
                extra_rows[step].append(item)
            extra_done[step].add(str(doc_id))
            write_json(extra_paths[step], extra_rows[step])
            mark_done(doc_id, step)

        if "zhupi" in steps:
            if args.skip_done and (str(doc_id) in extra_done["zhupi"] or is_done(doc_id, "zhupi")):
                print("  - zhupi (skip done)")
            else:
                print("  - zhupi")
                zh_payload = record_payload(doc, "zhupi", args.model)
                zh_extra = skill_prompt("zhupi")
                if zh_extra:
                    zh_payload["question"] = zh_extra
                zh = post_json(args.proxy, zh_payload, args.timeout, args.retries, args.retry_sleep)
                for item in zh.get("zhupi", []):
                    item = dict(item)
                    item.setdefault("doc_id", doc_id)
                    extra_rows["zhupi"].append(item)
                extra_done["zhupi"].add(str(doc_id))
                write_json(extra_paths["zhupi"], extra_rows["zhupi"])
                mark_done(doc_id, "zhupi")

        if "edict-match" in steps:
            if doc.get("doc_type") == "上諭":
                print("  - edict-match (skip 上諭 source)")
                mark_done(doc_id, "edict-match")
                continue
            existing_edict_rows = [
                row for row in extra_rows["edict-match"]
                if str(row.get("doc_id") or row.get("memDoc") or "") == str(doc_id)
            ]
            invalid_existing = any(
                not (row.get("points") or [])
                or any(
                    not isinstance(point, dict)
                    or not quote_is_verbatim(doc.get("body") or "", point.get("memorial_quote") or "")
                    or not quote_is_verbatim(
                        (edicts_by_id.get(str(row.get("edict_id") or "")) or {}).get("body") or "",
                        point.get("edict_quote") or "",
                    )
                    for point in (row.get("points") or [])
                )
                for row in existing_edict_rows
            )
            if (
                args.skip_done
                and (str(doc_id) in extra_done["edict-match"] or is_done(doc_id, "edict-match"))
                and not invalid_existing
            ):
                print("  - edict-match (skip done)")
                continue
            base = primary_date(doc)
            cands = [r for r in all_edicts if within_days(primary_date(r), base, 3)][:20] if base else []
            if not cands:
                print("  - edict-match (no candidate 上諭)")
                extra_done["edict-match"].add(str(doc_id))
                mark_done(doc_id, "edict-match")
                continue
            print(f"  - edict-match ({len(cands)} candidate 上諭)")
            matches_for_doc = []
            question = skill_prompt("edict-match")
            for j, ed in enumerate(cands, 1):
                ed_id = ed.get("doc_id") or ed.get("id")
                print(f"    - {j}/{len(cands)} {doc_id} × {ed_id}")
                payload = {
                    "mode": "edict_match",
                    "model": args.model,
                    "question": question,
                    "memorial": {
                        "id": doc_id,
                        "title": doc.get("title") or "",
                        "date": base,
                        "body": doc.get("body") or "",
                    },
                    "edicts": [{
                        "id": ed_id,
                        "date": primary_date(ed),
                        "title": ed.get("title") or "",
                        "body": ed.get("body") or "",
                    }],
                }
                try:
                    data = post_json(args.proxy, payload, args.timeout, args.retries, args.retry_sleep)
                except Exception as exc:
                    print(f"      edict-match failed, saved error and continuing: {exc}")
                    data = {"mode": "edict_match", "matches": [], "error": str(exc)}
                candidate_points = []
                candidate_summaries = []
                seen_points = set()
                for match in data.get("matches", []):
                    if not isinstance(match, dict):
                        continue
                    returned_id = str(match.get("edict_id") or ed_id)
                    if returned_id != str(ed_id):
                        continue
                    points = match.get("points") if isinstance(match.get("points"), list) else []
                    if not points and (match.get("memorial_quote") or match.get("edict_quote") or match.get("how")):
                        points = [{
                            "aspect": "",
                            "memorial_quote": match.get("memorial_quote") or "",
                            "edict_quote": match.get("edict_quote") or "",
                            "how": match.get("how") or "",
                        }]
                    for point in points:
                        if not isinstance(point, dict):
                            continue
                        memorial_quote = str(point.get("memorial_quote") or "").strip()
                        edict_quote = str(point.get("edict_quote") or "").strip()
                        if not quote_is_verbatim(doc.get("body") or "", memorial_quote):
                            continue
                        if not quote_is_verbatim(ed.get("body") or "", edict_quote):
                            continue
                        key = (memorial_quote, edict_quote, str(point.get("title") or point.get("aspect") or ""))
                        if key in seen_points:
                            continue
                        seen_points.add(key)
                        candidate_points.append(point)
                    summary = str(match.get("summary") or "").strip()
                    if summary and summary not in candidate_summaries:
                        candidate_summaries.append(summary)
                if candidate_points:
                    matches_for_doc.append({
                        "doc_id": doc_id,
                        "memDoc": doc_id,
                        "memTitle": doc.get("title") or "",
                        "edict_id": str(ed_id),
                        "title": ed.get("title") or "",
                        "date": primary_date(ed),
                        "summary": " ".join(candidate_summaries),
                        "points": candidate_points,
                    })
            extra_rows["edict-match"] = [
                row for row in extra_rows["edict-match"]
                if str(row.get("doc_id") or row.get("memDoc") or "") != str(doc_id)
            ]
            extra_rows["edict-match"].extend(matches_for_doc)
            extra_done["edict-match"].add(str(doc_id))
            write_json(extra_paths["edict-match"], extra_rows["edict-match"])
            mark_done(doc_id, "edict-match")

    if "official-response" in steps:
        # Runs once after the per-doc loop, not inside it: candidates for "who responded" are
        # searched across the WHOLE loaded corpus (records), not just the docs in this bundle --
        # same reasoning as officialResponseCandidates() in stage1-timeline.html. Depends on
        # zhupi/edict-match having produced candidates for these docs, either earlier in this same
        # run or from a previous run's output files (read directly, regardless of --skip-done,
        # since this step is commonly run as a separate follow-up pass over an existing bundle).
        def existing_or_live(step: str) -> list[dict[str, Any]]:
            return extra_rows.get(step) or read_json(extra_paths[step], [])

        zhupi_items = existing_or_live("zhupi")
        edict_items = existing_or_live("edict-match")
        doc_ids_in_bundle = {str(d.get("doc_id") or d.get("id")) for d in docs}
        by_id_all = {str(r.get("doc_id") or r.get("id")): r for r in records}

        official_response_path = out_root / "outputs" / "official-response.json"
        official_rows = read_json(official_response_path, []) if args.skip_done else []
        or_done = {(str(r.get("doc_id")), str(r.get("evTitle") or "")) for r in official_rows}
        or_question = skill_prompt("official-response")

        # Build the flat list of (source_doc_id, title, dateAr, quote, addressee_names) actions to
        # search a response for -- one entry per 硃批 item, and one per 諭 point (or per edict item
        # itself when it carries no points), same granularity the website commits at.
        actions: list[dict[str, Any]] = []
        for it in zhupi_items:
            doc_id = str(it.get("doc_id") or "")
            if doc_id not in doc_ids_in_bundle:
                continue
            rec = by_id_all.get(doc_id) or {}
            date_ar = (
                date_pair_value(rec, "receive_date")
                or date_pair_value(rec, "send_date")
                or date_pair_value(rec, "announce_date")
            )
            # a 硃批 is written directly onto the memorial it responds to, so the memorial's OWN
            # author is exactly the official the emperor is addressing (unlike a 諭, which is its
            # own separate document naming its recipients explicitly).
            addressee = [rec.get("author_name")] if rec.get("author_name") else []
            actions.append({
                "doc_id": doc_id,
                "evTitle": it.get("title") or it.get("text") or "硃批",
                "dateAr": date_ar,
                "quote": it.get("text") or it.get("marker") or "",
                "addressee": addressee,
            })
        for it in edict_items:
            edict_id = str(it.get("edict_id") or "")
            mem_id = str(it.get("doc_id") or it.get("memDoc") or "")
            if not edict_id or (edict_id not in doc_ids_in_bundle and mem_id not in doc_ids_in_bundle):
                continue
            edict_rec = by_id_all.get(edict_id) or {}
            date_ar = it.get("date") or date_pair_value(edict_rec, "announce_date") or date_pair_value(edict_rec, "send_date")
            addressee = list(edict_rec.get("recipients") or [])
            pts = it.get("points") or []
            if pts:
                for pt in pts:
                    actions.append({
                        "doc_id": edict_id,
                        "evTitle": pt.get("title") or pt.get("aspect") or it.get("title") or "上諭",
                        "dateAr": date_ar,
                        "quote": pt.get("edict_quote") or "",
                        "addressee": addressee,
                    })
            else:
                actions.append({
                    "doc_id": edict_id, "evTitle": it.get("title") or "上諭", "dateAr": date_ar,
                    "quote": "", "addressee": addressee,
                })

        print(f"- official-response ({len(actions)} 皇帝行動 candidates)")
        for j, act in enumerate(actions, 1):
            key = (act["doc_id"], act["evTitle"])
            if args.skip_done and key in or_done:
                print(f"  - {j}/{len(actions)} (skip done): {act['evTitle']}")
                continue
            if not act["dateAr"]:
                print(f"  - {j}/{len(actions)}: {act['evTitle']} (無日期，略過)")
                continue
            cands = official_response_candidates(records, act["dateAr"], act["doc_id"], act["addressee"])
            if not cands:
                print(f"  - {j}/{len(actions)}: {act['evTitle']} (30日內找不到候選文書)")
                continue
            print(f"  - {j}/{len(actions)}: {act['evTitle']} ({len(cands)} 份候選文書)")
            payload = {
                "mode": "official_response",
                "model": args.model,
                "action": {"what": act["evTitle"], "whenCh": "", "dateAr": act["dateAr"], "quote": act["quote"]},
                "addressee": "、".join(act["addressee"]) if act["addressee"] else "",
                "candidates": [
                    {
                        "doc_id": str(c.get("doc_id") or c.get("id")),
                        "title": c.get("title") or "",
                        "date": doc_best_ar(c),
                        "body": c.get("body") or "",
                    }
                    for c in cands
                ],
                **({"question": or_question} if or_question else {}),
            }
            try:
                data = post_json(args.proxy, payload, args.timeout, args.retries, args.retry_sleep)
            except Exception as exc:
                print(f"    official-response failed, saved error and continuing: {exc}")
                data = {"items": [], "error": str(exc)}
            official_rows.append({
                "doc_id": act["doc_id"],
                "evTitle": act["evTitle"],
                "addressee": data.get("addressee") or ("、".join(act["addressee"]) if act["addressee"] else ""),
                "items": data.get("items", []),
            })
            write_json(official_response_path, official_rows)

    (out_root / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if summaries:
        (out_root / "outputs" / "summary.json").write_text(json.dumps(summaries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if divisions:
        (out_root / "outputs" / "division-parts.json").write_text(json.dumps(divisions, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if lin_events:
        (out_root / "outputs" / "lin-events.json").write_text(json.dumps(lin_events, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if source_chains:
        merged_chains = merge_source_chains_by_signature(source_chains)
        (out_root / "outputs" / "source-chain.json").write_text(json.dumps(merged_chains, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out_root / "human-edits" / "notes.json").write_text("[]\n", encoding="utf-8")

    print(f"\nWrote bundle: {out_root.relative_to(ROOT)}")
    print("Open the website and click: 資料 → 載入技能輸出")
    print_token_summary()


if __name__ == "__main__":
    main()
