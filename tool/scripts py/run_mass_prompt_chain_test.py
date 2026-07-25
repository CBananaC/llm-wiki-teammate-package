#!/usr/bin/env python3
"""Run the official-document review loop against selected source documents.

The loop is deliberately pair-grounded after event extraction. It does not
search all 上諭 by date and it does not run the old 回應時效/situfit stage:

  summary -> division -> 林方 events + per-event source chains
  -> 清方 three-in-one events + per-event source chains
  -> confirmed prior-上諭 response -> combined emperor actions
  -> confirmed official responses for each emperor action.

The bundle is written directly to the shared review-bundle directory used by
the website. Existing UI code supplies cross-document repeat-report matching
and the merge/separate choice when the bundle is loaded.
"""

from __future__ import annotations

import argparse
import hashlib
import http.client
import json
import os
import re
import sys
import time
import urllib.error
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from run_review_bundle_test import (  # noqa: E402
    BUNDLES_DIR,
    ROOT,
    SOURCE,
    date_pair_value,
    doc_best_ar,
    merge_source_chains_by_signature,
    post_json as _post_json,
    primary_date,
    print_cost_summary,
    read_json,
    record_payload,
    skill_prompt,
    write_json,
)


DEFAULT_DOC_IDS = "台83,台90,台155,台156"
DEFAULT_MODEL = "gemini-3.5-flash"
PAIR_DIR = ROOT / "review-tools" / "(1) formal"
YU_SOURCE_PATH = PAIR_DIR / "yu-source.json"
CONFIRMED_PAIRS_PATH = PAIR_DIR / "confirmed-pairs.json"
FORMAL_STATE_PATH = PAIR_DIR / "formal_all.data"

LOOP_CHAIN = [
    "summary",
    "divide",
    "lin-events+source",
    "qing-actions-all+source",
    "confirmed-yu-response",
    "combined-emperor-actions",
    "repeat-report-dedup (global, post-loop)",
    "official-response",
]

_ACCOUNTING_STEP = ""


@contextmanager
def accounting_step(label: str):
    global _ACCOUNTING_STEP
    previous = _ACCOUNTING_STEP
    _ACCOUNTING_STEP = label
    try:
        yield
    finally:
        _ACCOUNTING_STEP = previous


def post_json(
    url: str,
    payload: dict[str, Any],
    timeout: int,
    retries: int = 3,
    retry_sleep: int = 12,
) -> dict[str, Any]:
    """Call the proxy and retry transient Cloud Run/provider failures."""
    request_payload = dict(payload)
    if _ACCOUNTING_STEP:
        request_payload["_accounting_step"] = _ACCOUNTING_STEP
    last: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            return _post_json(url, request_payload, timeout, 1, retry_sleep)
        except http.client.RemoteDisconnected as exc:
            last = exc
            if attempt >= retries:
                raise
            print(f"    retry {attempt}/{retries} after remote disconnect")
            time.sleep(retry_sleep * attempt)
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code not in {429, 500, 502, 503, 504} or attempt >= retries:
                raise
            print(f"    retry {attempt}/{retries} after HTTP {exc.code}")
            time.sleep(retry_sleep * attempt)
        except (urllib.error.URLError, TimeoutError, ConnectionError) as exc:
            last = exc
            if attempt >= retries:
                raise
            print(f"    retry {attempt}/{retries} after {exc}")
            time.sleep(retry_sleep * attempt)
    raise last or RuntimeError("request failed")


def split_csv(value: str) -> list[str]:
    return [part.strip() for part in (value or "").split(",") if part.strip()]


def doc_id_of(record: dict[str, Any]) -> str:
    return str(record.get("doc_id") or record.get("id") or "")


def is_excluded_doc_id(doc_id: str) -> bool:
    """奏-prefixed documents are duplicate copies of the 硃-prefixed memorials (the
    same奏摺 held in a different archive series); they must not be loaded as
    responders or candidates, or the same reply gets counted twice."""
    return str(doc_id or "").startswith("奏")


def _norm_name(value: str) -> str:
    """Strip titles/offices so 「陸路提督黃仕簡」 and 「黃仕簡」 compare equal."""
    s = re.sub(r"\s+", "", str(value or ""))
    s = re.sub(r"^(?:奴才|臣|署|護理|署理|欽差|大臣|前|原)+", "", s)
    for office in ("閩浙總督", "陸路提督", "水師提督", "福建巡撫", "臺灣鎮總兵",
                   "臺灣道", "總兵", "提督", "巡撫", "總督", "將軍", "副將", "參將",
                   "都司", "守備", "同知", "知縣", "知府", "道員"):
        s = s.replace(office, "")
    return s


def is_self_reported_event(doc: dict[str, Any], item: dict[str, Any]) -> bool:
    """True when the card describes the memorialist's OWN act, reported first-hand.

    Such an action has no upstream informant chain -- the author is the source.
    Tracing it anyway produces either a degenerate 親歷 self-loop hop
    (黃仕簡 --親歷--> 黃仕簡) or, worse, borrows an unrelated informant chain from a
    neighbouring reported event and mis-attributes it (e.g. 黃仕簡擬赴臺由南路會剿
    wrongly credited to 柴大紀、永福 之咨會)."""
    if str(item.get("actor") or item.get("side") or "qing") == "lin":
        return False
    how = re.sub(r"\s+", "", str(item.get("howKnown") or ""))
    if how not in {"親歷", "親報", "官員親報", "自述"}:
        return False
    author = _norm_name(author_name(doc))
    if not author:
        return False
    who = item.get("who") if isinstance(item.get("who"), list) else []
    names = {_norm_name(w) for w in who if w}
    if not names:
        return False
    return any(n and (n in author or author in n) for n in names)


def strip_degenerate_hops(chains: list[Any]) -> list[dict[str, Any]]:
    """Drop hops whose informant and recipient are the same person (親歷 self-loops):
    they carry no information and render as a bogus source line on the website.
    A chain left with no hops is dropped entirely."""
    out: list[dict[str, Any]] = []
    for chain in chains or []:
        if not isinstance(chain, dict):
            continue
        hops = [
            h for h in (chain.get("hops") or [])
            if isinstance(h, dict)
            and not (
                _norm_name(h.get("from_person"))
                and _norm_name(h.get("from_person")) == _norm_name(h.get("to_person"))
            )
        ]
        if not hops:
            continue
        chain = dict(chain)
        chain["hops"] = hops
        out.append(chain)
    return out


def body_of(record: dict[str, Any]) -> str:
    return str(record.get("body") or "")


def rescript_of(record: dict[str, Any]) -> str:
    return str(record.get("rescript_text") or record.get("rescript") or "")


def author_name(record: dict[str, Any]) -> str:
    author = record.get("author")
    if isinstance(author, dict):
        return str(author.get("name") or "")
    if isinstance(author, str):
        return author
    return str(record.get("author_name") or "")


def record_date(record: dict[str, Any]) -> str:
    return (
        date_pair_value(record, "receive_date")
        or date_pair_value(record, "send_date")
        or date_pair_value(record, "announce_date")
        or date_pair_value(record, "issue_date")
    )


def imperial_date(record: dict[str, Any]) -> str:
    if record.get("doc_type") == "上諭":
        return date_pair_value(record, "announce_date") or date_pair_value(record, "send_date")
    return date_pair_value(record, "receive_date") or date_pair_value(record, "send_date")


def parse_date(value: str):
    value = str(value or "").replace("/", "-")
    if not re.fullmatch(r"\d{4}-\d{1,2}-\d{1,2}", value):
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None


def verified_quote(source: str, quote: str) -> str:
    src = re.sub(r"\s+", "", str(source or ""))
    raw = str(quote or "").strip()
    if not src or not raw:
        return ""
    candidates = [raw]
    if len(raw) >= 2 and raw[0] in "「『\"" and raw[-1] in "」』\"":
        candidates.append(raw[1:-1].strip())
    # Models sometimes include the explanatory label 「硃批：」 or 「上諭：」;
    # retain only the exact quoted imperial words when that suffix is verbatim.
    if "：" in raw:
        candidates.append(raw.split("：", 1)[1].strip())
    for candidate in candidates:
        q = re.sub(r"\s+", "", candidate)
        if q and q in src:
            return candidate.strip()
    return ""


def quote_is_verbatim(source: str, quote: str) -> bool:
    return bool(verified_quote(source, quote))


def source_text(record: dict[str, Any]) -> str:
    return body_of(record) + "\n" + rescript_of(record)


def add_default_source(item: dict[str, Any], did: str) -> dict[str, Any]:
    item = dict(item)
    item.setdefault("doc_id", did)
    sources = item.get("sources")
    if not isinstance(sources, list) or not sources:
        item["sources"] = [{"doc_id": did, "quote": item.get("quote") or ""}]
    return item


def pair_rows(path: Path) -> list[dict[str, Any]]:
    raw = read_json(path, {})
    if isinstance(raw, dict):
        rows = raw.get("pairs")
    else:
        rows = raw
    return [dict(row) for row in rows or [] if isinstance(row, dict)]


def pair_source_doc_id(pair: dict[str, Any]) -> str:
    for key in ("yu_doc_id", "zhu_doc_id", "source_doc_id", "source_id"):
        value = pair.get(key)
        if value:
            return str(value)
    for key in ("yu", "zhu", "source"):
        nested = pair.get(key)
        if isinstance(nested, dict) and nested.get("id"):
            return str(nested["id"])
    return ""


def pair_yu_doc_id(pair: dict[str, Any]) -> str:
    value = pair.get("yu_doc_id")
    if value:
        return str(value)
    nested = pair.get("yu")
    return str(nested.get("id") or "") if isinstance(nested, dict) else ""


def pair_reply_doc_id(pair: dict[str, Any]) -> str:
    for key in ("reply_doc_id", "reply_id"):
        value = pair.get(key)
        if value:
            return str(value)
    nested = pair.get("reply")
    return str(nested.get("id") or "") if isinstance(nested, dict) else ""


def load_existing_pairs() -> list[dict[str, Any]]:
    """Load only the pair graphs already accepted by the formal workspace."""
    candidates = pair_rows(YU_SOURCE_PATH) + pair_rows(CONFIRMED_PAIRS_PATH)
    formal = read_json(FORMAL_STATE_PATH, {})
    if isinstance(formal, dict):
        candidates.extend(row for row in formal.get("pairs", []) if isinstance(row, dict))
        candidates.extend(row for row in formal.get("__docPairs", []) if isinstance(row, dict))
    out: list[dict[str, Any]] = []
    seen: set[str] = set()
    for pair in candidates:
        relation = str(pair.get("relation") or "")
        source = pair_source_doc_id(pair)
        reply = pair_reply_doc_id(pair)
        key = "|".join((relation, source, reply, json.dumps(pair.get("evidence") or {}, ensure_ascii=False, sort_keys=True)))
        if key in seen:
            continue
        seen.add(key)
        out.append(pair)
    return out


def pairs_for_selected_yu_source(pairs: list[dict[str, Any]], did: str) -> list[dict[str, Any]]:
    return [
        pair
        for pair in pairs
        if str(pair.get("relation") or "") == "yu_source"
        and pair_reply_doc_id(pair) == did
        and pair_yu_doc_id(pair)
    ]


def pairs_for_previous_yu_response(pairs: list[dict[str, Any]], did: str) -> list[dict[str, Any]]:
    return [
        pair
        for pair in pairs
        if str(pair.get("relation") or "") == "official_reply_to_yu"
        and pair_reply_doc_id(pair) == did
        and pair_yu_doc_id(pair)
    ]


def pair_evidence(pair: dict[str, Any]) -> dict[str, Any]:
    evidence = pair.get("evidence")
    return dict(evidence) if isinstance(evidence, dict) else {}


def pair_yu_payload(pair: dict[str, Any], by_id: dict[str, dict[str, Any]]) -> dict[str, Any] | None:
    yid = pair_yu_doc_id(pair)
    record = by_id.get(yid)
    if not record or record.get("doc_type") != "上諭":
        return None
    evidence = pair_evidence(pair)
    return {
        "id": yid,
        "title": record.get("title") or "",
        "date": imperial_date(record) or primary_date(record),
        "body": body_of(record),
        "pair_evidence": {
            "quote_in_reply": evidence.get("quote_in_reply") or "",
            "matched_yu_span": evidence.get("matched_yu_span") or "",
            "relation_note": evidence.get("relation_note") or "",
        },
    }


def run_summary(proxy: str, model: str, doc: dict[str, Any], timeout: int, retries: int, retry_sleep: int) -> dict[str, Any]:
    payload = record_payload(doc, "summary", model)
    instruction = skill_prompt("summary")
    if instruction:
        payload["instruction"] = instruction
    with accounting_step("summary"):
        data = post_json(proxy, payload, timeout, retries, retry_sleep)
    text = data.get("text") or data.get("summary") or ""
    if isinstance(text, dict):
        text = text.get("text") or text.get("summary") or json.dumps(text, ensure_ascii=False)
    return {"doc_id": doc_id_of(doc), "title": doc.get("title") or "", "summary": str(text)}


def run_division(proxy: str, model: str, doc: dict[str, Any], timeout: int, retries: int, retry_sleep: int) -> dict[str, Any]:
    payload = record_payload(doc, "divide", model)
    instruction = skill_prompt("divide")
    if instruction:
        payload["instruction"] = instruction
    with accounting_step("divide"):
        data = post_json(proxy, payload, timeout, retries, retry_sleep)
    return {"doc_id": doc_id_of(doc), "title": doc.get("title") or "", "parts": data.get("parts", [])}


def run_events(
    proxy: str,
    model: str,
    doc: dict[str, Any],
    actor: str,
    category: str,
    skill_step: str,
    timeout: int,
    retries: int,
    retry_sleep: int,
) -> list[dict[str, Any]]:
    payload = record_payload(doc, "events", model)
    payload.update({
        "actor": actor,
        "category": category,
        "actor_instruction": skill_prompt(skill_step),
    })
    with accounting_step("lin-events" if actor == "lin" else "qing-actions-all"):
        data = post_json(proxy, payload, timeout, retries, retry_sleep)
    rows: list[dict[str, Any]] = []
    for raw in data.get("events", []) if isinstance(data.get("events"), list) else []:
        if not isinstance(raw, dict):
            continue
        item = add_default_source(raw, doc_id_of(doc))
        item.setdefault("actor", actor)
        if actor == "qing":
            item["category"] = str(item.get("category") or item.get("qing_category") or item.get("qcat") or "done")
            if item["category"] not in {"done", "plan", "nonmil"}:
                item["category"] = "done"
        rows.append(item)
    return rows


def trace_event(
    proxy: str,
    model: str,
    doc: dict[str, Any],
    item: dict[str, Any],
    side: str,
    timeout: int,
    retries: int,
    retry_sleep: int,
) -> dict[str, Any]:
    if is_self_reported_event(doc, {**item, "actor": side}):
        # the memorialist's own act: the author IS the source, so there is no chain to trace.
        print(f"      source-chain skipped (作者親歷): {item.get('subtitle') or '(untitled)'}")
        return {"doc_id": doc_id_of(doc), "evTitle": item.get("subtitle") or "", "actor": side,
                "event": item, "chains": [], "selfReported": True}
    payload = record_payload(doc, "trace", model)
    payload.update({
        "side": side,
        "single": True,
        "event": {
            "actor": side,
            "category": item.get("category") or "",
            "subtitle": item.get("subtitle") or "",
            "description": item.get("description") or "",
            "where": item.get("where") or "",
            "whenCh": item.get("whenCh") or item.get("whenAr") or "",
            "quote": item.get("quote") or ((item.get("sources") or [{}])[0].get("quote") or ""),
        },
    })
    instruction = skill_prompt("source-chain")
    if instruction:
        payload["question"] = instruction
    try:
        with accounting_step("lin-source-chain" if side == "lin" else "qing-source-chain"):
            data = post_json(proxy, payload, timeout, retries, retry_sleep)
        chains = data.get("chains", []) if isinstance(data.get("chains"), list) else []
        chains = strip_degenerate_hops(chains)
        return {"doc_id": doc_id_of(doc), "evTitle": item.get("subtitle") or "", "actor": side, "event": item, "chains": chains}
    except Exception as exc:  # a trace failure should not discard extracted events
        print(f"      source-chain failed for {item.get('subtitle') or '(untitled)'}: {exc}")
        return {"doc_id": doc_id_of(doc), "evTitle": item.get("subtitle") or "", "actor": side, "event": item, "chains": [], "error": str(exc)}


def trace_events_parallel(proxy, model, doc, items, side, timeout, retries, retry_sleep, workers=6):
    """Run per-event source-chain traces concurrently; order preserved."""
    if not items:
        return []
    if workers <= 1 or len(items) == 1:
        return [trace_event(proxy, model, doc, it, side, timeout, retries, retry_sleep) for it in items]
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=min(workers, len(items))) as ex:
        return list(ex.map(lambda it: trace_event(proxy, model, doc, it, side, timeout, retries, retry_sleep), items))


_ACTOR_ALIASES = {
    "emperor": {"emperor", "皇帝"},
    "lin": {"lin", "林", "林方"},
    "qing": {"qing", "清", "清方"},
}


def earlier_committed_events(actor_key: str, exclude_ids: set[str]) -> list[dict[str, Any]]:
    """Already-committed cards of one actor from formal_all.data, earliest first,
    with same-title duplicates collapsed. Shared by the emperor-action prompt and the
    lin/qing repeat-report dedup stage."""
    wanted = _ACTOR_ALIASES.get(actor_key, {actor_key})
    state = read_json(FORMAL_STATE_PATH, {})
    events = state.get("__events", []) if isinstance(state, dict) else []
    out: list[dict[str, Any]] = []
    for event in events:
        if not isinstance(event, dict):
            continue
        actor = str(event.get("actor") or "").lower()
        if actor not in wanted:
            continue
        sources = []
        for src in event.get("sources") or []:
            if isinstance(src, str):
                src = {"doc_id": src, "quote": ""}
            if not isinstance(src, dict):
                continue
            sources.append({"doc_id": str(src.get("doc_id") or ""), "quote": src.get("quote") or ""})
        if any(src.get("doc_id") in exclude_ids for src in sources):
            continue
        event_id = str(event.get("id") or "")
        if not event_id:
            continue
        out.append({
            "event_id": event_id,
            "date": event.get("dateAr") or event.get("whenAr") or "",
            "title": event.get("subtitle") or event.get("what") or "",
            "description": event.get("description") or "",
            "sources": sources,
        })
    out.sort(key=lambda row: (parse_date(row.get("date") or "") or datetime.max.date(), row.get("event_id") or ""))
    # formal_all.data can contain several saved extraction cards for the same
    # already-committed action. Keep the earliest representative in the prompt;
    # this both names the earliest action and avoids sending a large duplicate
    # registry to every combined-action call.
    unique: list[dict[str, Any]] = []
    seen_titles: set[str] = set()
    for row in out:
        title_key = re.sub(r"[\s，。、《》；：：「」『』（）()！？]", "", str(row.get("title") or ""))
        if title_key and title_key in seen_titles:
            continue
        if title_key:
            seen_titles.add(title_key)
        unique.append(row)
    return unique


def earlier_emperor_actions(exclude_ids: set[str], by_id: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    return earlier_committed_events("emperor", exclude_ids)


def _run_card_id(row: dict[str, Any], index: int) -> str:
    """Stable in-run id for a freshly-extracted card, so cards from this run can be
    offered to repeat_report as candidates for each other."""
    return "run:%s:%d" % (doc_id_of(row) or "?", index)


def dedup_event_rows_global(
    proxy: str,
    model: str,
    rows: list[dict[str, Any]],
    actor: str,
    by_id: dict[str, dict[str, Any]],
    timeout: int,
    retries: int,
    retry_sleep: int,
    top_k: int = 12,
) -> int:
    """Cross-document repeat-report pass over EVERY extracted card of one side.

    Runs once, after all documents have been processed, so a card can be matched
    against cards extracted from later documents in the same run as well as against
    already-committed events -- a per-document pass can only ever look backwards and
    would miss the repeat that arrives two documents on.

    Cards are compared in reporting-date order; each is judged against the already-seen
    cards of this run plus the committed registry, and the earliest equivalent wins, so
    `same_as_event_id` always points at the first report of the occurrence. Writes
    `same_as_event_id` / `repeat_of_title` in place for the website to merge on."""
    if not rows:
        return 0
    committed = earlier_committed_events(actor, set())
    order = sorted(
        range(len(rows)),
        key=lambda i: (
            parse_date(
                imperial_date(by_id.get(doc_id_of(rows[i]), {}))
                or primary_date(by_id.get(doc_id_of(rows[i]), {}))
                or ""
            ) or datetime.max.date(),
            doc_id_of(rows[i]),
            i,
        ),
    )
    seen: list[dict[str, Any]] = list(committed)
    flagged = 0
    for position, i in enumerate(order, 1):
        item = rows[i]
        did = doc_id_of(item)
        rec = by_id.get(did, {})
        card_text = str(item.get("subtitle") or "") + str(item.get("description") or "")
        candidates = _relevant_previous_actions(seen, {"title": card_text}, top_k=top_k) if seen else []
        # A repeat report is by definition cross-document: the SAME memorial listing three
        # distinct acts of 藍元枚 (交印、起程、赴蚶江) is three events, not one reported thrice.
        # Drop same-document candidates so the model can never collapse them into each other.
        candidates = [
            c for c in candidates
            if str(((c.get("sources") or [{}])[0]).get("doc_id", "")) != str(did)
        ]
        # register this card as a candidate for the ones that follow, whether or not it
        # is itself a repeat (a later card may match it and inherit its `same_as` target).
        seen.append({
            "event_id": _run_card_id(item, i),
            "date": imperial_date(rec) or primary_date(rec) or "",
            "title": item.get("subtitle") or "",
            "description": item.get("description") or "",
            "sources": [{"doc_id": did, "quote": item.get("quote") or ""}],
        })
        if not candidates:
            continue
        payload = {
            "mode": "repeat_report",
            "model": model,
            "actor": actor,
            "question": skill_prompt("repeat-report"),
            "card": {
                "title": item.get("subtitle") or "",
                "description": item.get("description") or "",
                "quote": item.get("quote") or "",
                "doc_id": did,
                "date": imperial_date(rec) or primary_date(rec) or "",
            },
            "candidates": [
                {
                    "id": c.get("event_id") or "",
                    "doc_id": (c.get("sources") or [{}])[0].get("doc_id", ""),
                    "date": c.get("date") or "",
                    "title": c.get("title") or "",
                    "description": c.get("description") or "",
                    "quote": (c.get("sources") or [{}])[0].get("quote", ""),
                }
                for c in candidates
            ],
        }
        try:
            with accounting_step("repeat-report"):
                data = post_json(proxy, payload, timeout, retries, retry_sleep)
        except Exception as exc:  # dedup is advisory; never lose an extracted card over it
            print(f"    repeat-report failed for {item.get('subtitle') or '(untitled)'}: {exc}")
            continue
        same_ids = data.get("same_ids") if isinstance(data.get("same_ids"), list) else []
        same_ids = [str(i2) for i2 in same_ids if str(i2)]
        if not same_ids:
            continue
        by_event = {str(c.get("event_id") or ""): c for c in candidates}
        target = same_ids[0]
        matched = by_event.get(target) or {}
        # if the match is another card from this run that was itself flagged as a repeat,
        # follow the link so every copy points at the single earliest report.
        for other_index, other in enumerate(rows):
            if _run_card_id(other, other_index) == target and other.get("same_as_event_id"):
                target = str(other.get("same_as_event_id"))
                matched = {"title": other.get("repeat_of_title") or other.get("subtitle") or ""}
                break
        item["same_as_event_id"] = target
        item["repeat_of_title"] = str(matched.get("title") or "")
        if len(same_ids) > 1:
            item["same_as_event_ids"] = same_ids
        flagged += 1
        print(f"    [{position}/{len(order)}] 重複：{item.get('subtitle') or ''} → {item['repeat_of_title']}")
    return flagged


def source_type(record: dict[str, Any]) -> str:
    return "上諭" if record.get("doc_type") == "上諭" else "硃批"


def selected_emperor_sources(
    doc: dict[str, Any],
    selected_pairs: list[dict[str, Any]],
    by_id: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    """Build the only imperial source set the combined-action call may see."""
    did = doc_id_of(doc)
    out: list[dict[str, Any]] = []
    if doc.get("doc_type") == "硃批":
        out.append({
            "id": did,
            "title": doc.get("title") or "",
            "date": imperial_date(doc),
            "body": body_of(doc),
            "source_type": "硃批",
            "pair_evidence": {},
        })
    seen = {did}
    for pair in selected_pairs:
        payload = pair_yu_payload(pair, by_id)
        if not payload or payload["id"] in seen:
            continue
        payload["source_type"] = "上諭"
        seen.add(payload["id"])
        out.append(payload)
    return out


# Routine acknowledgement rescripts. They mark that the memorial was seen and that a
# separate 上諭 carries the substance; on their own they are not an emperor action and
# must never stand as the quotation for one.
_BOILERPLATE_ZHUPI = (
    "已有旨了", "已有旨", "另有旨", "即有旨", "尋有旨", "有旨", "有旨諭", "有旨寄諭",
    "已有旨諭", "另有旨諭", "即有旨諭", "尋有旨諭", "已有旨了欽遵", "已有旨遵行",
    "知道了", "覽", "覽奏俱悉", "覽奏欣悉", "覽奏均悉", "俱悉", "已悉", "知道",
    "該部知道", "該部議奏", "依議", "是",
)


def is_boilerplate_zhupi(quote: str) -> bool:
    q = re.sub(r"[\s，。、；：:,.！!？?「」『』（）()]", "", str(quote or ""))
    q = re.sub(r"(欽此|奉硃批|奉朱批|硃批|朱批)", "", q)
    if not q:
        return True
    return q in _BOILERPLATE_ZHUPI


def normalize_action_sources(
    raw_sources: Any,
    allowed: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    if not isinstance(raw_sources, list):
        return []
    out: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for raw in raw_sources:
        if not isinstance(raw, dict):
            continue
        sid = str(raw.get("doc_id") or raw.get("id") or "")
        if sid not in allowed:
            continue
        quote = str(raw.get("quote") or "").strip()
        record = allowed[sid]
        quote = verified_quote(source_text(record), quote)
        if not quote:
            continue
        raw_stype = str(raw.get("source_type") or "").strip()
        if record.get("doc_type") == "上諭":
            stype = "上諭"
        elif raw_stype == "奏摺":
            # the originating memorial passage the 上諭/硃批 is responding to (the 據奏 report);
            # verified against the memorial body above, kept as its own source so the card shows
            # both the emperor's words and the official report they answer.
            stype = "奏摺"
        else:
            stype = "硃批"
        key = (sid, quote)
        if key in seen:
            continue
        seen.add(key)
        entry = {
            "doc_id": sid,
            "source_type": stype,
            "quote": quote,
            "title": raw.get("title") or record.get("title") or "",
            "date": raw.get("date") or imperial_date(record) or primary_date(record),
        }
        if stype == "硃批":
            if is_boilerplate_zhupi(quote):
                # 「已有旨了。欽此。」 and friends are acknowledgement 套語, not an emperor action.
                continue
            position, context = zhupi_position(record, quote)
            entry["position"] = position
            if context:
                entry["context_quote"] = context
        out.append(entry)
    return out


def zhupi_position(record: dict[str, Any], quote: str) -> tuple[str, str]:
    """Classify a 硃批 quote as 尾批 (the document's end rescript) or 夾批 (an
    interlinear （硃批：…） annotation in the body), and for a 夾批 return the body
    clause it annotates. The 尾批 lives in the rescript field; 夾批 live inline in
    the body wrapped in （硃批：…）."""
    q = re.sub(r"\s+", "", quote or "")
    resc = re.sub(r"\s+", "", rescript_of(record) or "")
    if q and resc and q in resc:
        return "尾批", ""
    body = body_of(record) or ""
    for mo in re.finditer(r"[（(](?:硃批|朱批)\s*[：:]([^）)]*)[）)]", body):
        inner = re.sub(r"\s+", "", mo.group(1) or "")
        if q and inner and (q in inner or inner in q):
            start = mo.start()
            cut = max(
                body.rfind("。", 0, start), body.rfind("\n", 0, start),
                body.rfind("）", 0, start), body.rfind(")", 0, start),
            )
            context = body[cut + 1:start].strip()
            return "夾批", context
    return "尾批", ""


def _relevant_previous_actions(previous, doc, top_k=20, max_desc=240):
    """Cap + trim the committed-action registry sent to the combined-emperor call.
    Shipping every prior emperor action (hundreds, some multi-paragraph) makes the
    request large and slow enough that Cloud Run drops the connection
    (http.client.RemoteDisconnected), and retries resend the same body. Keep only
    the top_k most topically relevant to this memorial and trim each description."""
    if len(previous) <= top_k and all(len(str(a.get("description") or "")) <= max_desc for a in previous):
        return previous
    def _bg(x):
        x = re.sub(r"\s+", "", str(x or ""))
        return {x[i:i + 2] for i in range(len(x) - 1)}
    target = _bg((doc.get("title") or "") + body_of(doc) + rescript_of(doc))
    def _ov(a):
        A = _bg((a.get("title") or "") + (a.get("description") or ""))
        return len(A & target) / len(A | target) if A and target else 0.0
    out = []
    for a in sorted(previous, key=_ov, reverse=True)[:top_k]:
        a = dict(a)
        d = str(a.get("description") or "")
        if len(d) > max_desc:
            a["description"] = d[:max_desc] + "…"
        out.append(a)
    return out


def combined_action_rows(
    proxy: str,
    model: str,
    doc: dict[str, Any],
    selected_pairs: list[dict[str, Any]],
    by_id: dict[str, dict[str, Any]],
    timeout: int,
    retries: int,
    retry_sleep: int,
) -> list[dict[str, Any]]:
    did = doc_id_of(doc)
    imperial_sources = selected_emperor_sources(doc, selected_pairs, by_id)
    if not imperial_sources:
        return []
    allowed = {did: doc}
    for payload in imperial_sources:
        if payload["id"] in by_id:
            allowed[payload["id"]] = by_id[payload["id"]]
    previous = _relevant_previous_actions(earlier_emperor_actions(set(allowed), by_id), doc)
    previous_ids = {str(row.get("event_id") or "") for row in previous}
    zhu_text = rescript_of(doc)
    inline = re.findall(r"(?:硃批|朱批)\s*[:：]\s*[^)）\n]+", body_of(doc))
    if inline:
        zhu_text = (zhu_text + "\n" if zhu_text else "") + "\n".join(inline)
    payload = {
        "mode": "combined_emperor_actions",
        "model": model,
        "question": skill_prompt("combined-emperor-actions"),
        "memorial": {
            "id": did,
            "author": author_name(doc),
            "date": imperial_date(doc) or primary_date(doc),
            "title": doc.get("title") or "",
            "body": body_of(doc),
            "rescript": rescript_of(doc),
            "zhupi_text": zhu_text,
        },
        "edicts": imperial_sources[1:] if imperial_sources and imperial_sources[0]["id"] == did else imperial_sources,
        "previous_actions": previous,
    }
    with accounting_step("combined-emperor-actions"):
        data = post_json(proxy, payload, timeout, retries, retry_sleep)
    actions = data.get("actions", []) if isinstance(data.get("actions"), list) else []
    rows: list[dict[str, Any]] = []
    for raw in actions:
        if not isinstance(raw, dict):
            continue
        sources = normalize_action_sources(raw.get("sources"), allowed)
        if not sources:
            continue
        # An emperor action must be grounded in the emperor's OWN words. A 奏摺 source is only
        # the memorial passage being answered, so a point carrying nothing but that is either a
        # recital of the official's report or an action whose imperial quote the model failed to
        # cite. The prompt now forbids it; flag any that still slip through so the card is
        # visibly incomplete on the website rather than silently reading as a 奏摺-only action.
        missing_emperor_quote = not any(
            source.get("source_type") in {"上諭", "硃批"} for source in sources
        )
        if missing_emperor_quote:
            print(f"      ⚠ emperor action without 上諭／硃批 quote: {raw.get('title') or '(untitled)'}")
        same = str(raw.get("same_as_event_id") or "")
        if same not in previous_ids:
            same = ""
        prior = next((row for row in previous if row.get("event_id") == same), None)
        description = str(raw.get("description") or raw.get("how") or "")
        # Keep this run's own SVO title even for a repeat -- the earliest action's title may be an
        # older, vaguer phrasing, and the "previously seen" note already flags the merge. (same_as
        # still links them; merging on the website adopts the target event's identity.)
        title = str(raw.get("title") or (prior.get("title") if prior else "") or "皇帝行動")
        point = {
            "title": title,
            "aspect": raw.get("action_type") or "",
            "action_type": raw.get("action_type") or "comment",
            "how": description,
            "description": description,
            "whenCh": raw.get("whenCh") or "",
            "whenAr": raw.get("whenAr") or "",
            "where": raw.get("where") or "",
            "who": raw.get("who") if isinstance(raw.get("who"), list) else [],
            "whoLoc": raw.get("who_loc") or raw.get("whoLoc") or {},
            "relations": raw.get("relations") if isinstance(raw.get("relations"), list) else [],
            "same_as_event_id": same,
            "sources": sources,
        }
        if missing_emperor_quote:
            point["missing_emperor_quote"] = True
        rows.append(point)
    if not rows:
        return []
    first = next((source for source in imperial_sources if source["id"] != did), imperial_sources[0])
    return [{
        "doc_id": did,
        "memDoc": did,
        "memTitle": doc.get("title") or "",
        "combinedEmperor": True,
        "marker": "既有配對",
        "items": [{
            "edict_id": first["id"],
            "title": first.get("title") or "硃批／既有配對上諭",
            "date": first.get("date") or imperial_date(doc),
            "memDoc": did,
            "memTitle": doc.get("title") or "",
            "summary": "只保留皇帝自己的評論、答覆或命令；同義硃批與上諭合為一項。",
            "points": rows,
        }],
    }]


def response_pairs_for_source(source_id: str, source_kind: str, pairs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    relation = "official_reply_to_yu" if source_kind == "上諭" else "official_reply_to_emperor_zhu"
    return [
        pair
        for pair in pairs
        if str(pair.get("relation") or "") == relation and pair_source_doc_id(pair) == source_id and pair_reply_doc_id(pair)
    ]


def action_addressees(sources: list[dict[str, Any]], by_id: dict[str, dict[str, Any]], selected_doc: dict[str, Any]) -> list[str]:
    out: list[str] = []
    for source in sources:
        record = by_id.get(str(source.get("doc_id") or ""), {})
        values = record.get("recipients") if source.get("source_type") == "上諭" else [author_name(selected_doc)]
        if not isinstance(values, list):
            values = [values] if values else []
        for value in values:
            if value and str(value) not in out:
                out.append(str(value))
    return out


def official_response_rows_for_actions(
    proxy: str,
    model: str,
    selected_docs: list[dict[str, Any]],
    combined_rows: list[dict[str, Any]],
    pairs: list[dict[str, Any]],
    by_id: dict[str, dict[str, Any]],
    timeout: int,
    retries: int,
    retry_sleep: int,
    skip_keys: set[tuple[str, str, tuple[str, ...]]] | None = None,
    workers: int = 6,
    on_row=None,
) -> list[dict[str, Any]]:
    """Build one official-response row per emperor-action point. The proxy calls
    run CONCURRENTLY (each action is independent), and on_row is invoked from the
    main thread as each result completes -- callers use it to save incrementally,
    so stopping the run never loses responses already found."""
    selected_by_id = {doc_id_of(doc): doc for doc in selected_docs}

    # Phase A (fast, no network): assemble one job per emperor-action point.
    jobs: list[dict[str, Any]] = []
    for combined in combined_rows:
        did = str(combined.get("doc_id") or combined.get("memDoc") or "")
        selected = selected_by_id.get(did)
        if not selected:
            continue
        for item in combined.get("items") or []:
            for point in item.get("points") or []:
                sources = [source for source in point.get("sources") or [] if isinstance(source, dict)]
                source_ids = list(dict.fromkeys(str(source.get("doc_id") or "") for source in sources if source.get("doc_id")))
                row_key = (did, str(point.get("title") or item.get("title") or "皇帝行動"), tuple(source_ids))
                if skip_keys and row_key in skip_keys:
                    continue
                source_pairs: list[dict[str, Any]] = []
                candidate_ids: list[str] = []
                for source in sources:
                    sid = str(source.get("doc_id") or "")
                    skind = str(source.get("source_type") or ("上諭" if by_id.get(sid, {}).get("doc_type") == "上諭" else "硃批"))
                    if skind == "奏摺":
                        # the originating-memorial source is a display/analysis anchor only; responders
                        # are found through the 上諭／硃批 sources, so it never contributes candidates.
                        continue
                    for pair in response_pairs_for_source(sid, skind, pairs):
                        rid = pair_reply_doc_id(pair)
                        if rid == did:
                            continue
                        if is_excluded_doc_id(rid):
                            # 奏-prefixed docs are duplicate copies of the 硃-prefixed memorials
                            # (same document, other archive series); drop them so responders aren't
                            # double-counted -- the 硃 twin already carries the same response.
                            continue
                        source_pairs.append(pair)
                        if rid and rid not in candidate_ids:
                            candidate_ids.append(rid)
                candidates = [by_id[rid] for rid in candidate_ids if rid in by_id]
                if len(candidates) > 6:
                    # Big output (many responders) is the main cause of slow calls / disconnects.
                    # Keep the 6 reply docs closest in time to the action; confirmed pairs are
                    # usually few, so this rarely drops a real responder.
                    _actd = parse_date(point.get("whenAr") or "") or parse_date(next((s.get("date") for s in sources if s.get("date")), "") or "")
                    def _prox(c, _a=_actd):
                        cd = parse_date(doc_best_ar(c) or "")
                        return abs((cd - _a).days) if (cd and _a) else 10 ** 6
                    candidates = sorted(candidates, key=_prox)[:6]
                addressees = action_addressees(sources, by_id, selected)
                action_quote = "\n".join(
                    f"【{source.get('source_type') or ''} {source.get('doc_id') or ''}】{source.get('quote') or ''}"
                    for source in sources
                    if source.get("quote")
                )
                jobs.append({
                    "did": did, "selected": selected, "point": point, "item": item,
                    "sources": sources, "source_ids": source_ids, "source_pairs": source_pairs,
                    "candidates": candidates, "addressees": addressees, "action_quote": action_quote,
                })

    rows: list[dict[str, Any]] = []

    def _row(job: dict[str, Any], response: dict[str, Any]) -> dict[str, Any]:
        valid_ids = {doc_id_of(c) for c in job["candidates"]}
        items = [r for r in response.get("items", []) if isinstance(r, dict) and str(r.get("doc_id") or "") in valid_ids]
        return {
            "doc_id": job["did"], "memDoc": job["did"], "memTitle": job["selected"].get("title") or "",
            "evTitle": job["point"].get("title") or job["item"].get("title") or "皇帝行動",
            "addressee": response.get("addressee") or "、".join(job["addressees"]),
            "items": items, "source_doc_ids": job["source_ids"], "action_doc_ids": job["source_ids"],
            "source_pairs": job["source_pairs"], "confirmedPairsOnly": True, "noConfirmedPairs": not bool(job["candidates"]),
        }

    def _emit(row: dict[str, Any]) -> None:
        rows.append(row)
        if on_row:
            on_row(row)

    # Actions with no confirmed reply candidate need no network call.
    for job in jobs:
        if not job["candidates"]:
            _emit(_row(job, {"addressee": "、".join(job["addressees"]), "items": []}))
    net_jobs = [job for job in jobs if job["candidates"]]

    def _call(job: dict[str, Any]):
        payload = {
            "mode": "official_response", "model": model, "confirmed_pairs_only": True,
            "action": {
                "what": job["point"].get("title") or job["item"].get("title") or "皇帝行動",
                "dateAr": job["point"].get("whenAr") or next((s.get("date") for s in job["sources"] if s.get("date")), ""),
                "quote": job["action_quote"],
            },
            "addressee": "、".join(job["addressees"]),
            "candidates": [
                {"doc_id": doc_id_of(c), "title": c.get("title") or "", "date": doc_best_ar(c), "body": body_of(c)[:1800]}
                for c in job["candidates"]
            ],
            "question": skill_prompt("official-response"),
        }
        ok = True
        try:
            resp = post_json(proxy, payload, timeout, retries, retry_sleep)
        except Exception as exc:
            print(f"    official-response failed for 「{job['point'].get('title') or ''}」: {exc}")
            resp = {"addressee": "、".join(job["addressees"]), "items": []}
            ok = False
        return job, resp, ok

    if net_jobs:
        # official-response payloads are large (candidate memorial bodies), so cap concurrency
        # lower than the source-chain workers to avoid overloading the proxy / provider and
        # triggering RemoteDisconnected. A failed call writes NO row, so --skip-done retries it.
        resp_workers = max(1, min(workers, 3))
        with accounting_step("official-response"):
            if resp_workers > 1 and len(net_jobs) > 1:
                from concurrent.futures import ThreadPoolExecutor, as_completed
                with ThreadPoolExecutor(max_workers=min(resp_workers, len(net_jobs))) as ex:
                    futures = [ex.submit(_call, job) for job in net_jobs]
                    for fut in as_completed(futures):
                        job, resp, ok = fut.result()
                        if ok:
                            _emit(_row(job, resp))   # on_row runs on the main thread -> no write race
            else:
                for job in net_jobs:
                    job, resp, ok = _call(job)
                    if ok:
                        _emit(_row(job, resp))
    return rows


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--proxy", default=os.environ.get("GEMINI_PROXY_URL", ""))
    ap.add_argument("--model", default=os.environ.get("GEMINI_MODEL", DEFAULT_MODEL))
    ap.add_argument("--doc-ids", default=DEFAULT_DOC_IDS, help="Comma-separated source document ids")
    ap.add_argument("--bundle", default="", help="Short semantic review-bundle name")
    ap.add_argument("--timeout", type=int, default=240)
    ap.add_argument("--retries", type=int, default=4)
    ap.add_argument("--retry-sleep", type=int, default=15)
    ap.add_argument("--skip-done", action="store_true")
    ap.add_argument("--workers", type=int, default=6, help="Concurrent proxy calls for source-chain traces and official-response")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--input-price-per-million", type=float, default=None)
    ap.add_argument("--output-price-per-million", type=float, default=None)
    args = ap.parse_args()

    records = json.loads(SOURCE.read_text(encoding="utf-8"))
    by_id = {doc_id_of(record): record for record in records}
    wanted = split_csv(args.doc_ids)
    missing = [did for did in wanted if did not in by_id]
    if missing:
        raise SystemExit("Missing doc_id(s): " + ", ".join(missing))
    docs = [by_id[did] for did in wanted]
    pairs = load_existing_pairs()

    if args.bundle:
        bundle_name = args.bundle
    else:
        digest = hashlib.sha1("-".join(wanted).encode("utf-8")).hexdigest()[:8]
        bundle_name = f"official-review-{wanted[0]}-plus{len(wanted) - 1}-{digest}"
    out_root = BUNDLES_DIR / bundle_name
    out_dir = out_root / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_root / "human-edits").mkdir(parents=True, exist_ok=True)

    if args.dry_run:
        print(f"DRY RUN -- bundle: {out_root.relative_to(ROOT)}")
        print(f"model: {args.model}")
        print(f"existing pair rows: {len(pairs)}")
        for doc in docs:
            did = doc_id_of(doc)
            print(f"\n[{did}] {doc.get('doc_type')} {doc.get('title')}")
            print(f"  date={record_date(doc)!r} author={author_name(doc)!r}")
            print(f"  prior 上諭 response pairs: {len(pairs_for_previous_yu_response(pairs, did))}")
            sources = pairs_for_selected_yu_source(pairs, did)
            print(f"  existing yu_source links: {len(sources)} ({', '.join(pair_yu_doc_id(p) for p in sources) or 'none'})")
        print("\n(no proxy calls made)")
        return

    if not args.proxy:
        raise SystemExit("Set GEMINI_PROXY_URL or pass --proxy (or use --dry-run).")

    files = {
        "summary": out_dir / "summary.json",
        "divide": out_dir / "division-parts.json",
        "lin": out_dir / "lin-events.json",
        "qing": out_dir / "qing-actions-all.json",
        "source_raw": out_dir / "_source-chain-raw.json",
        "source": out_dir / "source-chain.json",
        "reply": out_dir / "confirmed-yu-response.json",
        "emperor": out_dir / "combined-emperor-actions.json",
        "official": out_dir / "official-response.json",
    }
    status_path = out_dir / "_run-status.json"
    status = read_json(status_path, {}) if args.skip_done else {}

    def done(did: str, step: str) -> bool:
        return bool(args.skip_done and status.get(did, {}).get(step))

    def mark(did: str, step: str) -> None:
        status.setdefault(did, {})[step] = True
        write_json(status_path, status)

    summaries = read_json(files["summary"], []) if args.skip_done else []
    divisions = read_json(files["divide"], []) if args.skip_done else []
    lin_rows = read_json(files["lin"], []) if args.skip_done else []
    qing_rows = read_json(files["qing"], []) if args.skip_done else []
    source_raw = read_json(files["source_raw"], []) if args.skip_done else []
    reply_rows = read_json(files["reply"], []) if args.skip_done else []
    emperor_rows = read_json(files["emperor"], []) if args.skip_done else []
    official_rows = read_json(files["official"], []) if args.skip_done else []

    def flush_sources() -> None:
        write_json(files["source_raw"], source_raw)
        write_json(files["source"], merge_source_chains_by_signature(source_raw))

    for index, doc in enumerate(docs, 1):
        did = doc_id_of(doc)
        print(f"[{index}/{len(docs)}] {did} {doc.get('doc_type')} {doc.get('title')}")
        try:
            if not done(did, "summary"):
                print("  - summary")
                summaries.append(run_summary(args.proxy, args.model, doc, args.timeout, args.retries, args.retry_sleep))
                write_json(files["summary"], summaries)
                mark(did, "summary")

            if not done(did, "divide"):
                print("  - divide")
                divisions.append(run_division(args.proxy, args.model, doc, args.timeout, args.retries, args.retry_sleep))
                write_json(files["divide"], divisions)
                mark(did, "divide")

            if done(did, "lin-events"):
                lin_items = [row for row in lin_rows if doc_id_of(row) == did]
            else:
                print("  - lin-events + per-event source chain")
                lin_items = run_events(args.proxy, args.model, doc, "lin", "", "lin-events", args.timeout, args.retries, args.retry_sleep)
                lin_rows.extend(lin_items)
                write_json(files["lin"], lin_rows)
                mark(did, "lin-events")
            if not done(did, "source-chain-lin"):
                print(f"    - 林方來源鏈 ×{len(lin_items)}（並行 {args.workers}）")
                source_raw.extend(trace_events_parallel(args.proxy, args.model, doc, lin_items, "lin", args.timeout, args.retries, args.retry_sleep, args.workers))
                flush_sources()
                mark(did, "source-chain-lin")

            if done(did, "qing-actions-all"):
                qing_items = [row for row in qing_rows if doc_id_of(row) == did]
            else:
                print("  - qing-actions-all + per-event source chain")
                qing_items = run_events(args.proxy, args.model, doc, "qing", "all", "qing-actions-all", args.timeout, args.retries, args.retry_sleep)
                qing_rows.extend(qing_items)
                write_json(files["qing"], qing_rows)
                mark(did, "qing-actions-all")
            if not done(did, "source-chain-qing"):
                print(f"    - 清方來源鏈 ×{len(qing_items)}（並行 {args.workers}）")
                source_raw.extend(trace_events_parallel(args.proxy, args.model, doc, qing_items, "qing", args.timeout, args.retries, args.retry_sleep, args.workers))
                flush_sources()
                mark(did, "source-chain-qing")

            # The remaining stages are pair-grounded and therefore do not run a corpus search.
            if not done(did, "confirmed-yu-response"):
                prior_pairs = pairs_for_previous_yu_response(pairs, did)
                edicts = [payload for payload in (pair_yu_payload(pair, by_id) for pair in prior_pairs) if payload]
                if edicts:
                    print(f"  - confirmed prior 上諭 response ({len(edicts)} existing pair(s))")
                    payload = {
                        "mode": "confirmed_yu_response",
                        "model": args.model,
                        "reply": {"id": did, "author": author_name(doc), "date": record_date(doc), "title": doc.get("title") or "", "body": body_of(doc)},
                        "edicts": edicts,
                        "question": skill_prompt("confirmed-yu-response"),
                    }
                    with accounting_step("confirmed-yu-response"):
                        data = post_json(args.proxy, payload, args.timeout, args.retries, args.retry_sleep)
                    valid = {str(item["id"]) for item in edicts}
                    pair_by_yu = {pair_yu_doc_id(pair): pair for pair in prior_pairs}
                    items = []
                    for item in data.get("items", []) if isinstance(data.get("items"), list) else []:
                        yid = str(item.get("yu_doc_id") or "")
                        if yid not in valid:
                            continue
                        base = pair_by_yu.get(yid, {})
                        items.append(dict(item, yu_doc_id=yid))
                    reply_rows.append({"doc_id": did, "memDoc": did, "pairs": prior_pairs, "items": items})
                    write_json(files["reply"], reply_rows)
                mark(did, "confirmed-yu-response")

            if done(did, "combined-emperor-actions"):
                doc_emperor = [row for row in emperor_rows if str(row.get("doc_id") or row.get("memDoc") or "") == did]
            else:
                source_pairs = pairs_for_selected_yu_source(pairs, did)
                print(f"  - combined emperor actions ({len(source_pairs)} existing yu_source link(s))")
                doc_emperor = combined_action_rows(args.proxy, args.model, doc, source_pairs, by_id, args.timeout, args.retries, args.retry_sleep)
                emperor_rows.extend(doc_emperor)
                write_json(files["emperor"], emperor_rows)
                mark(did, "combined-emperor-actions")
        except Exception as exc:  # preserve completed earlier documents and resume safely
            print(f"  !! {did} failed ({exc}); rerun with --skip-done to continue")
            continue

    # Repeat-report dedup is a single GLOBAL pass, deliberately after every document has
    # been processed: a card extracted from 硃79 may be the same occurrence as one extracted
    # from 硃97, and a per-document pass could never see it.
    if not done("__global__", "dedup"):
        print("- 重複回報檢查（全域，所有文書擷取完畢後執行）")
        n_lin = dedup_event_rows_global(args.proxy, args.model, lin_rows, "lin", by_id, args.timeout, args.retries, args.retry_sleep)
        print(f"  林方：{n_lin}/{len(lin_rows)} 判為重複")
        write_json(files["lin"], lin_rows)
        n_qing = dedup_event_rows_global(args.proxy, args.model, qing_rows, "qing", by_id, args.timeout, args.retries, args.retry_sleep)
        print(f"  清方：{n_qing}/{len(qing_rows)} 判為重複")
        write_json(files["qing"], qing_rows)
        mark("__global__", "dedup")

    # Official response is intentionally post-loop so each action can be built
    # from the complete combined-emperor-actions output. Each action gets one
    # union of fixed pair edges, not a separate 30-day candidate search.
    if not done("__global__", "official-response"):
        print(f"- official-response for each extracted emperor action (existing pairs only; parallel {args.workers}, incremental save)")
        existing_keys = {(str(row.get("doc_id") or ""), str(row.get("evTitle") or ""), tuple(row.get("source_doc_ids") or [])) for row in official_rows}

        def _save_official(row):
            # incremental save: each completed response is written immediately, so
            # stopping the run never loses responses already found.
            official_rows.append(row)
            write_json(files["official"], official_rows)

        official_response_rows_for_actions(
            args.proxy,
            args.model,
            docs,
            emperor_rows,
            pairs,
            by_id,
            args.timeout,
            args.retries,
            args.retry_sleep,
            existing_keys if args.skip_done else None,
            workers=args.workers,
            on_row=_save_official,
        )
        mark("__global__", "official-response")

    if source_raw:
        flush_sources()

    manifest = {
        "name": bundle_name,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "source": str(SOURCE.relative_to(ROOT)),
        "model": args.model,
        "doc_ids": wanted,
        "chain": LOOP_CHAIN,
        "pair_files": [str(YU_SOURCE_PATH.relative_to(ROOT)), str(CONFIRMED_PAIRS_PATH.relative_to(ROOT))],
        "deduplication": "existing bundle loader matchCandidateInRegistry; earliest report plus merge/separate choice",
        "excluded_stages": ["edict-match", "info-source", "situfit", "date-window official-response search"],
    }
    write_json(out_root / "manifest.json", manifest)
    if not (out_root / "human-edits" / "notes.json").exists():
        write_json(out_root / "human-edits" / "notes.json", [])
    cost = print_cost_summary(args.model, args.input_price_per_million, args.output_price_per_million)
    write_json(out_dir / "cost-summary.json", cost)

    print(f"\nWrote bundle: {out_root.relative_to(ROOT)}")
    print("Open the timeline page and choose 資料 → 載入技能輸出.")


if __name__ == "__main__":
    main()
