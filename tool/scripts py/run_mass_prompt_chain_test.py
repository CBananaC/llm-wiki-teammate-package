#!/usr/bin/env python3
"""Run the official-document review loop against selected source documents.

The loop is deliberately pair-grounded after event extraction. It does not
search all 上諭 by date and it does not run the old 回應時效/situfit stage:

  summary -> division -> 林方 events + per-event source chains
  -> 清方 three-in-one events + per-event source chains
  -> cross-document 林/清 repeat-report check (LLM judged)
  -> confirmed prior-上諭 response -> combined emperor actions
  -> confirmed official responses for each emperor action.

The bundle is written directly to the shared review-bundle directory used by
the website. The repeat-report pass annotates 林/清 cards with the earliest
cross-document report; the website supplies the merge/separate choice when the
bundle is loaded.
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
    "repeat-report",
    "confirmed-yu-response",
    "combined-emperor-actions",
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


# ---- cross-document repeat-report dedup ------------------------------------
# This is deliberately an LLM-verdict pass. The local overlap score below is
# only a high-recall candidate retriever, so different wording can still reach
# Gemini; it is never used to decide that two events are the same.
_REPEAT_EVENT_FILES = {
    "lin": ("lin-events.json",),
    "qing": (
        "qing-actions-all.json",
        # Older official-document bundles used three separate Qing files.
        "qing-events-done.json",
        "qing-events-plan.json",
        "qing-events-nonmil.json",
    ),
}
_REPEAT_FORMAL: dict[str, Any] | None = None


def _repeat_formal_state() -> dict[str, Any]:
    global _REPEAT_FORMAL
    if _REPEAT_FORMAL is None:
        raw = read_json(FORMAL_STATE_PATH, {})
        _REPEAT_FORMAL = raw if isinstance(raw, dict) else {}
    return _REPEAT_FORMAL


def _repeat_send_date(doc_id: str, by_id: dict[str, dict[str, Any]]) -> str:
    record = by_id.get(str(doc_id), {})
    # Repeat labels must use the reporting document's sent date, never the
    # event's historical occurrence date extracted by the model.
    return date_pair_value(record, "send_date") or record_date(record)


def _repeat_doc_ids(card: dict[str, Any]) -> list[str]:
    ids: list[str] = []
    for value in card.get("source_doc_ids") or []:
        value = str(value or "")
        if value and value not in ids:
            ids.append(value)
    for source in card.get("sources") or []:
        if isinstance(source, dict):
            value = str(source.get("doc_id") or source.get("source_doc_id") or "")
        else:
            value = str(source or "")
        if value and value not in ids:
            ids.append(value)
    value = str(card.get("doc_id") or "")
    if value and value not in ids:
        ids.insert(0, value)
    return ids


def _repeat_quote(card: dict[str, Any]) -> str:
    quote = card.get("quote") or card.get("quotation") or ""
    if quote:
        return str(quote)
    for source in card.get("sources") or []:
        if isinstance(source, dict):
            quote = source.get("quote") or source.get("quotation") or source.get("source_quote") or ""
            if quote:
                return str(quote)
    return ""


def _repeat_view(
    card: dict[str, Any],
    actor: str,
    by_id: dict[str, dict[str, Any]],
    card_id: str,
    original: dict[str, Any] | None = None,
) -> dict[str, Any]:
    source_ids = _repeat_doc_ids(card)
    doc_id = source_ids[0] if source_ids else str(card.get("doc_id") or "")
    earlier = card.get("earliest_report") if isinstance(card.get("earliest_report"), dict) else {}
    return {
        "id": card_id,
        "title": str(card.get("subtitle") or card.get("title") or card.get("what") or ""),
        "description": str(card.get("description") or ""),
        "quote": _repeat_quote(card),
        "doc_id": doc_id,
        "source_doc_ids": source_ids,
        "date": _repeat_send_date(doc_id, by_id) if doc_id else "",
        "actor": actor,
        "_orig": original,
        # A prior unverified bundle may already have an earliest pointer. Keep
        # that pointer as a root candidate when a later run compares against it.
        "_earliest_report": earlier,
    }


def _repeat_committed_cards(actor: str, by_id: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    events = _repeat_formal_state().get("__events", [])
    out: list[dict[str, Any]] = []
    if not isinstance(events, list):
        return out
    for event in events:
        if not isinstance(event, dict):
            continue
        raw_actor = str(event.get("actor") or "").lower()
        normalized_actor = "emperor" if raw_actor in {"emperor", "皇帝"} else raw_actor
        if normalized_actor != actor:
            continue
        event_id = str(event.get("id") or "")
        if not event_id:
            continue
        source_ids: list[str] = []
        quote = ""
        for source in event.get("sources") or []:
            if isinstance(source, str):
                source = {"doc_id": source}
            if not isinstance(source, dict):
                continue
            sid = str(source.get("doc_id") or "")
            if sid and sid not in source_ids:
                source_ids.append(sid)
            if not quote:
                quote = str(source.get("quote") or source.get("quotation") or "")
        if not source_ids:
            continue
        view = _repeat_view(
            {
                "doc_id": source_ids[0],
                "source_doc_ids": source_ids,
                "subtitle": event.get("subtitle") or event.get("what") or "",
                "description": event.get("description") or "",
                "quote": quote,
            },
            actor,
            by_id,
            event_id,
        )
        view["date"] = _repeat_send_date(source_ids[0], by_id) or str(event.get("dateAr") or event.get("whenAr") or "")
        out.append(view)
    return out


def _repeat_historical_cards(
    actor: str,
    by_id: dict[str, dict[str, Any]],
    current_bundle: str,
) -> list[dict[str, Any]]:
    """Read unverified event cards from earlier official-loop bundles.

    These cards are candidates only; they are never mutated. Exact duplicates
    from rerun bundles are collapsed, while differently worded cards from the
    same document remain available for the LLM to assess.
    """
    seen_exact: set[tuple[str, str, str, str]] = set()
    out: list[dict[str, Any]] = []
    for bundle_dir in sorted(BUNDLES_DIR.iterdir(), key=lambda p: p.name):
        if not bundle_dir.is_dir() or bundle_dir.name == current_bundle:
            continue
        manifest = read_json(bundle_dir / "manifest.json", {})
        chain = manifest.get("chain", []) if isinstance(manifest, dict) else []
        if not isinstance(chain, list):
            chain = []
        has_official_event_chain = (
            "lin-events+source" in chain or
            "qing-actions-all+source" in chain or
            any(str(item).startswith("qing-events-") for item in chain)
        )
        if manifest and not has_official_event_chain:
            continue
        for filename in _REPEAT_EVENT_FILES[actor]:
            rows = read_json(bundle_dir / "outputs" / filename, [])
            if not isinstance(rows, list):
                continue
            for index, row in enumerate(rows):
                if not isinstance(row, dict) or row.get("__skip"):
                    continue
                source_ids = _repeat_doc_ids(row)
                if not source_ids:
                    continue
                title = str(row.get("subtitle") or row.get("title") or row.get("what") or "")
                description = str(row.get("description") or "")
                quote = _repeat_quote(row)
                exact_key = (source_ids[0], title, description, quote)
                if exact_key in seen_exact:
                    continue
                seen_exact.add(exact_key)
                card_id = str(row.get("card_id") or f"{source_ids[0]}#{actor}#{index}")
                # Bundle-qualify historical ids because old reruns reused the
                # same doc#actor#index card id.
                out.append(_repeat_view(row, actor, by_id, f"{bundle_dir.name}::{card_id}"))
    return out


def _repeat_text(card: dict[str, Any]) -> str:
    return "\n".join((card.get("title") or "", card.get("description") or "", card.get("quote") or ""))


def _repeat_bigrams(text: str) -> set[str]:
    text = re.sub(r"\s+", "", str(text or ""))
    return {text[index:index + 2] for index in range(len(text) - 1)}


def _repeat_retrieval_score(left: dict[str, Any], right: dict[str, Any]) -> float:
    a, b = _repeat_bigrams(_repeat_text(left)), _repeat_bigrams(_repeat_text(right))
    return len(a & b) / len(a | b) if a and b else 0.0


def _repeat_rank(card: dict[str, Any]) -> tuple[Any, str, str]:
    raw = str(card.get("date") or "").replace("/", "-")
    parsed = parse_date(raw)
    if parsed is None:
        month = re.fullmatch(r"(\d{4})-(\d{1,2})", raw)
        if month:
            try:
                parsed = datetime(int(month.group(1)), int(month.group(2)), 1).date()
            except ValueError:
                parsed = None
    return (parsed or datetime.max.date(), str(card.get("doc_id") or ""), str(card.get("id") or ""))


def _repeat_trim(card: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": str(card.get("id") or ""),
        "title": str(card.get("title") or "")[:90],
        "description": str(card.get("description") or "")[:180],
        "quote": str(card.get("quote") or "")[:100],
        "doc_id": str(card.get("doc_id") or ""),
        "date": str(card.get("date") or ""),
    }


def _repeat_root(card: dict[str, Any]) -> dict[str, Any]:
    earlier = card.get("_earliest_report")
    if isinstance(earlier, dict) and earlier.get("id") and earlier.get("doc_id"):
        return {
            "id": str(earlier.get("id") or ""),
            "title": str(earlier.get("title") or card.get("title") or ""),
            "doc_id": str(earlier.get("doc_id") or ""),
            "source_doc_ids": [str(earlier.get("doc_id") or "")],
            "date": str(earlier.get("date") or ""),
        }
    return card


def repeat_report_events(
    proxy: str,
    model: str,
    actor: str,
    cards: list[dict[str, Any]],
    by_id: dict[str, dict[str, Any]],
    current_bundle: str,
    timeout: int,
    retries: int,
    retry_sleep: int,
    workers: int = 6,
    top_k: int = 12,
    min_overlap: float = 0.04,
) -> tuple[int, int, int]:
    """Annotate current 林/清 cards with earlier cross-document repeats.

    Returns (annotations, failed_llm_calls, candidate_jobs). Same-document
    matches are intentionally excluded, even when the two cards describe the
    same occurrence.
    """
    views: list[dict[str, Any]] = []
    for index, card in enumerate(cards):
        if not isinstance(card, dict) or card.get("__skip"):
            continue
        # A rerun must not preserve an old verdict produced by a different
        # candidate pool or model.
        for key in ("same_as", "earliest_report", "repeat_candidates", "repeat_verdict", "repeat_reason"):
            card.pop(key, None)
        did = str(card.get("doc_id") or "")
        card_id = str(card.get("card_id") or f"{did}#{actor}#{index}")
        card["card_id"] = card_id
        views.append(_repeat_view(card, actor, by_id, card_id, original=card))
    if not views:
        return 0, 0, 0

    committed = _repeat_committed_cards(actor, by_id)
    historical = _repeat_historical_cards(actor, by_id, current_bundle)
    current = [dict(view, _orig=None) for view in views]
    pool = committed + historical + current

    jobs: list[tuple[dict[str, Any], list[dict[str, Any]]]] = []
    for view in views:
        own_docs = set(view.get("source_doc_ids") or [])
        candidates = [
            candidate for candidate in pool
            if candidate.get("id") != view.get("id")
            and own_docs.isdisjoint(set(candidate.get("source_doc_ids") or ([candidate.get("doc_id")] if candidate.get("doc_id") else [])))
        ]
        scored = sorted(
            ((_repeat_retrieval_score(view, candidate), candidate) for candidate in candidates),
            key=lambda pair: pair[0],
            reverse=True,
        )
        shortlist = [candidate for score, candidate in scored if score >= min_overlap][:top_k]
        if shortlist:
            jobs.append((view, shortlist))

    if not jobs:
        return 0, 0, 0

    def call(job: tuple[dict[str, Any], list[dict[str, Any]]]) -> tuple[str, list[str], bool]:
        view, shortlist = job
        payload = {
            "mode": "repeat_report",
            "model": model,
            "actor": actor,
            "card": _repeat_trim(view),
            "candidates": [_repeat_trim(candidate) for candidate in shortlist],
            "question": skill_prompt("repeat-report"),
        }
        try:
            data = post_json(proxy, payload, timeout, retries, retry_sleep)
        except Exception as exc:
            print(f"    repeat-report failed for {view.get('title') or '(untitled)'}: {exc}")
            return view["id"], [], False
        allowed = {str(candidate.get("id") or "") for candidate in shortlist}
        raw_ids = data.get("same_ids") if isinstance(data, dict) else []
        if not isinstance(raw_ids, list):
            raw_ids = [raw_ids] if raw_ids else []
        same_ids = [str(value) for value in raw_ids if str(value) in allowed]
        return view["id"], same_ids, True

    same_by_id: dict[str, list[str]] = {}
    failed = 0
    with accounting_step("repeat-report"):
        if workers > 1 and len(jobs) > 1:
            from concurrent.futures import ThreadPoolExecutor
            with ThreadPoolExecutor(max_workers=min(workers, len(jobs))) as executor:
                for view_id, same_ids, ok in executor.map(call, jobs):
                    same_by_id[view_id] = same_ids
                    failed += 0 if ok else 1
        else:
            for job in jobs:
                view_id, same_ids, ok = call(job)
                same_by_id[view_id] = same_ids
                failed += 0 if ok else 1

    pool_by_id = {str(candidate.get("id") or ""): candidate for candidate in pool}
    annotated = 0
    for view in sorted(views, key=_repeat_rank):
        matched = [pool_by_id[candidate_id] for candidate_id in same_by_id.get(view["id"], []) if candidate_id in pool_by_id]
        if not matched:
            continue
        own_docs = set(view.get("source_doc_ids") or [])
        roots = [
            _repeat_root(candidate)
            for candidate in matched
            if own_docs.isdisjoint(set(candidate.get("source_doc_ids") or ([candidate.get("doc_id")] if candidate.get("doc_id") else [])))
        ]
        if not roots:
            continue
        earliest = min(roots + [view], key=_repeat_rank)
        if str(earliest.get("id") or "") == str(view.get("id") or ""):
            continue
        original = view.get("_orig")
        if not isinstance(original, dict):
            continue
        original["same_as"] = earliest.get("id") or ""
        original["earliest_report"] = {
            "id": earliest.get("id") or "",
            "doc_id": earliest.get("doc_id") or "",
            "date": earliest.get("date") or "",
            "title": earliest.get("title") or "",
        }
        original["repeat_candidates"] = same_by_id.get(view["id"], [])
        annotated += 1
    return annotated, failed, len(jobs)


def earlier_emperor_actions(exclude_ids: set[str], by_id: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    state = read_json(FORMAL_STATE_PATH, {})
    events = state.get("__events", []) if isinstance(state, dict) else []
    out: list[dict[str, Any]] = []
    for event in events:
        if not isinstance(event, dict):
            continue
        actor = str(event.get("actor") or "").lower()
        if actor not in {"emperor", "皇帝"}:
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
        same = str(raw.get("same_as_event_id") or "")
        if same not in previous_ids:
            same = ""
        prior = next((row for row in previous if row.get("event_id") == same), None)
        description = str(raw.get("description") or raw.get("how") or "")
        origin_doc_id = str(
            raw.get("origin_doc_id")
            or raw.get("originDocId")
            or raw.get("primary_source_doc_id")
            or raw.get("primarySourceDocId")
            or ""
        )
        if origin_doc_id not in allowed:
            origin_doc_id = ""
        origin_type = str(
            raw.get("origin_type")
            or raw.get("originType")
            or raw.get("primary_source_type")
            or raw.get("primarySourceType")
            or ""
        )
        if origin_type not in {"硃批", "上諭"}:
            origin_type = ""
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
            "origin_doc_id": origin_doc_id,
            "origin_type": origin_type,
            "origin_quote": str(raw.get("origin_quote") or raw.get("originQuote") or ""),
            "origin_date": str(raw.get("origin_date") or raw.get("originDate") or ""),
            "same_as_event_id": same,
            "sources": sources,
        }
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
    ap.add_argument("--workers", type=int, default=6, help="Concurrent proxy calls for source chains, repeat-report, and official-response")
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

    # Repeat detection runs after all selected documents have contributed their
    # 林/清 cards, so an earlier/later document in the selected set can be
    # compared in either input order. It is cross-document only and does not
    # touch 皇帝行動 or same-document repeats.
    if not done("__global__", "repeat-report"):
        print("- repeat-report dedup for 林方／清方（跨文書，LLM 判斷；僅標註不合併）")
        lin_annotated, lin_failed, lin_jobs = repeat_report_events(
            args.proxy,
            args.model,
            "lin",
            lin_rows,
            by_id,
            bundle_name,
            args.timeout,
            args.retries,
            args.retry_sleep,
            workers=args.workers,
        )
        qing_annotated, qing_failed, qing_jobs = repeat_report_events(
            args.proxy,
            args.model,
            "qing",
            qing_rows,
            by_id,
            bundle_name,
            args.timeout,
            args.retries,
            args.retry_sleep,
            workers=args.workers,
        )
        write_json(files["lin"], lin_rows)
        write_json(files["qing"], qing_rows)
        total_failed = lin_failed + qing_failed
        print(
            f"  repeats flagged -- 林 {lin_annotated}, 清 {qing_annotated} "
            f"({lin_jobs + qing_jobs} LLM comparison calls)"
        )
        if total_failed:
            print(f"  repeat-report had {total_failed} failed call(s); rerun with --skip-done to retry")
        else:
            mark("__global__", "repeat-report")

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
        "deduplication": "in-loop LLM repeat_report annotates cross-document 林/清 cards with same_as/earliest_report; website offers merge/keep",
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
