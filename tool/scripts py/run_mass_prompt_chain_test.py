#!/usr/bin/env python3
"""Run the current multi-step saved-prompt chain on a small doc set first.

Default test set: 台83, 台90, 台155, 台156.
"""

from __future__ import annotations

import argparse
import http.client
import json
import os
import re
import time
import sys
import urllib.error
from contextlib import contextmanager
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from run_review_bundle_test import (  # noqa: E402
    ROOT,
    SOURCE,
    doc_best_ar,
    official_response_candidates,
    post_json as _post_json,
    primary_date,
    read_json,
    record_payload,
    print_cost_summary,
    skill_prompt,
    within_days,
    write_json,
)


DEFAULT_DOC_IDS = "台83,台90,台155,台156"
QING_STEPS = {
    "qing-events-done": ("done", "extract-qing-actions-done.md"),
    "qing-events-plan": ("plan", "extract-qing-actions-planned.md"),
    "qing-events-nonmil": ("nonmil", "extract-qing-nonmilitary-actions.md"),
}


# The proxy token counter normally groups calls by proxy mode.  These labels
# preserve the loop's actual stages in the terminal table and in
# cost-summary.json (for example, qing events and their source trace are one
# logical stage for this runner).
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


def post_json(url: str, payload: dict[str, Any], timeout: int, retries: int = 3, retry_sleep: int = 12) -> dict[str, Any]:
    """Retry the old proxy helper plus Cloud Run's occasional bare disconnect/502."""
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
        except (urllib.error.URLError, TimeoutError) as exc:
            last = exc
            if attempt >= retries:
                raise
            print(f"    retry {attempt}/{retries} after {exc}")
            time.sleep(retry_sleep * attempt)
    raise last or RuntimeError("request failed")


def doc_id(record: dict[str, Any]) -> str:
    return str(record.get("doc_id") or record.get("id") or "")


def date_pair_value(record: dict[str, Any], key: str) -> str:
    value = record.get(key)
    if isinstance(value, list) and len(value) > 1:
        return value[1] or ""
    return ""


def parse_date(value: str):
    value = (value or "").replace("/", "-")
    if not re.fullmatch(r"\d{4}-\d{1,2}-\d{1,2}", value):
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None


def fmt_date(d) -> str:
    return f"{d.year:04d}/{d.month:02d}/{d.day:02d}"


def dates_within_days(value: str, base: str, days: int, forward_only: bool = False) -> bool:
    dv = parse_date(value)
    db = parse_date(base)
    if not dv or not db:
        return False
    diff = (dv - db).days
    return 0 <= diff <= days if forward_only else abs(diff) <= days


def body_of(record: dict[str, Any]) -> str:
    return record.get("body") or ""


def author_name(record: dict[str, Any]) -> str:
    author = record.get("author") or {}
    return record.get("author_name") or author.get("name") or ""


def rec_type(record: dict[str, Any]) -> str:
    dt = record.get("doc_type")
    if dt == "硃批":
        return "zhupi"
    if dt == "上諭":
        return "shangyu"
    return "shangzou"


def own_emperor_date(record: dict[str, Any]) -> str:
    if record.get("doc_type") == "上諭":
        return date_pair_value(record, "announce_date") or date_pair_value(record, "send_date")
    return date_pair_value(record, "receive_date") or date_pair_value(record, "send_date")


def extract_json_object(text: str) -> dict[str, Any]:
    text = (text or "").strip()
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.S)
    try:
        data = json.loads(text)
        return data if isinstance(data, dict) else {}
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", text, re.S)
        if not m:
            return {}
        try:
            data = json.loads(m.group(0))
            return data if isinstance(data, dict) else {}
        except json.JSONDecodeError:
            return {}


def char_bigrams(value: str) -> list[str]:
    s = re.sub(r"\s+", "", value or "")
    return [s[i : i + 2] for i in range(max(0, len(s) - 1))]


def likely_overlap(a: str, b: str) -> bool:
    aa = re.sub(r"\s+", "", a or "")
    bb = re.sub(r"\s+", "", b or "")
    if not aa or not bb:
        return False
    if aa in bb or bb in aa:
        return True
    a_bi = char_bigrams(aa)
    b_bi = set(char_bigrams(bb))
    return bool(a_bi) and sum(1 for x in a_bi if x in b_bi) / len(a_bi) > 0.35


def annotate_chains(chains: list[dict[str, Any]], did: str) -> list[dict[str, Any]]:
    out = []
    for ch in chains or []:
        ch = dict(ch)
        ch["hops"] = [dict(h, doc_id=str(h.get("doc_id") or did)) for h in (ch.get("hops") or [])]
        ch["events"] = [dict(e, doc_id=str(e.get("doc_id") or did)) for e in (ch.get("events") or [])]
        out.append(ch)
    return out


def add_default_source(item: dict[str, Any], did: str) -> dict[str, Any]:
    item = dict(item)
    item.setdefault("doc_id", did)
    item.setdefault("sources", [{
        "doc_id": did,
        "quote": item.get("quote") or "",
        "howKnown": item.get("howKnown") or "",
        "whenKnown": item.get("whenKnownCh") or "",
    }])
    return item


def run_event_step(proxy: str, model: str, doc: dict[str, Any], actor: str, category: str, step: str, timeout: int, retries: int, retry_sleep: int) -> list[dict[str, Any]]:
    payload = record_payload(doc, "events", model)
    payload.update({"actor": actor, "category": category, "actor_instruction": skill_prompt(step)})
    data = post_json(proxy, payload, timeout, retries, retry_sleep)
    return [add_default_source(it, doc_id(doc)) for it in data.get("events", [])]


def run_doc_trace(proxy: str, model: str, doc: dict[str, Any], actor: str, titles: list[str], timeout: int, retries: int, retry_sleep: int) -> list[dict[str, Any]]:
    if not titles:
        return []
    hint = "已知本文書已擷取出以下事件標題：" + "、".join(f"「{t}」" for t in titles if t) + "。描述每條來源鏈的 events[].subtitle 時，若對應到上述某一事件，請直接沿用該事件標題的原文字（逐字），不要另擬新標題。"
    payload = record_payload(doc, "trace", model)
    payload.update({"actor": actor, "side": actor, "question": hint})
    try:
        data = post_json(proxy, payload, timeout, retries, retry_sleep)
        return annotate_chains(data.get("chains", []), doc_id(doc))
    except Exception as exc:  # noqa: BLE001
        return [{"hops": [], "events": [], "error": str(exc)}]


def info_source_candidates(records: list[dict[str, Any]], base: dict[str, Any], lookback_days: int = 60) -> list[dict[str, Any]]:
    base_date = parse_date(own_emperor_date(base))
    if not base_date:
        return []
    lo = base_date - timedelta(days=lookback_days)
    base_id = doc_id(base)
    out = []
    for rec in records:
        if rec.get("doc_type") == "上諭" or doc_id(rec) == base_id:
            continue
        d = parse_date(date_pair_value(rec, "send_date") or date_pair_value(rec, "receive_date"))
        if d and lo <= d < base_date:
            out.append(rec)
    out.sort(key=lambda r: parse_date(date_pair_value(r, "send_date") or date_pair_value(r, "receive_date")) or base_date)
    return out


def fetch_info_sources(proxy: str, model: str, records: list[dict[str, Any]], base: dict[str, Any], emperor_text: str, timeout: int, retries: int, retry_sleep: int) -> dict[str, Any]:
    cands = info_source_candidates(records, base)
    if not cands or not emperor_text:
        return {"items": [], "candCount": len(cands)}
    payload = [{
        "doc_id": doc_id(r),
        "title": r.get("title") or "",
        "author": author_name(r),
        "type": r.get("doc_type") or "",
        "sendAr": date_pair_value(r, "send_date"),
        "recvAr": date_pair_value(r, "receive_date"),
        "body": body_of(r),
    } for r in cands]
    question = (
        "以下是一份皇帝文書（硃批或上諭）的原文（emperor_text），以及在此文書之前，各官員所上呈的候選奏摺／文書列表（candidates）。"
        "請找出皇帝原文中，皇帝所提及／回應的每一項具體資訊（事實、回報的情況、人名、地名、事件等——不要包含皇帝自己下達的命令或意見），"
        "並針對每一項資訊，判斷它最可能是根據 candidates 中哪一份文書、哪一段引文而來。"
        '請只輸出 JSON，格式：{"items":[{"info":"皇帝提及的這項資訊（一句話概述）","doc_id":"該資訊來源候選文書的id","quote":"該候選文書中的引文（逐字）","emperor_quote":"皇帝文書中引用或提及此資訊的原文（逐字）"}]}。'
        "\n【emperor_text】\n" + emperor_text
        + "\n【candidates】\n" + json.dumps(payload, ensure_ascii=False)
    )
    data = post_json(proxy, {"mode": "ask", "model": model, "question": question, "prompt": question}, timeout, retries, retry_sleep)
    result = data if isinstance(data.get("items"), list) else extract_json_object(data.get("text") or data.get("answer") or "")
    base_date = parse_date(own_emperor_date(base))
    items = []
    by_id = {doc_id(r): r for r in records}
    for it in result.get("items", []) if isinstance(result, dict) else []:
        src = by_id.get(str(it.get("doc_id") or ""))
        src_date = parse_date((date_pair_value(src, "send_date") or date_pair_value(src, "receive_date")) if src else "")
        items.append({
            "info": it.get("info") or "",
            "doc_id": str(it.get("doc_id") or ""),
            "quote": it.get("quote") or "",
            "emperor_quote": it.get("emperor_quote") or "",
            "srcTitle": src.get("title") if src else "",
            "srcAuthor": author_name(src) if src else "",
            "srcSentAr": (date_pair_value(src, "send_date") or date_pair_value(src, "receive_date")) if src else "",
            "daysBeforeEmperor": (base_date - src_date).days if base_date and src_date else None,
            "emperorDocId": doc_id(base),
        })
    return {"items": [x for x in items if x["info"] and x["doc_id"]], "candCount": len(cands)}


def safe_fetch_info_sources(proxy: str, model: str, records: list[dict[str, Any]], base: dict[str, Any], emperor_text: str, timeout: int, retries: int, retry_sleep: int) -> list[dict[str, Any]]:
    try:
        return fetch_info_sources(proxy, model, records, base, emperor_text, timeout, retries, retry_sleep).get("items") or []
    except Exception as exc:  # noqa: BLE001
        print(f"    info-source lookup failed for {doc_id(base)}; continuing without pending sources: {exc}")
        return []


def attach_info_to_zhupi(items: list[dict[str, Any]], info_items: list[dict[str, Any]]) -> None:
    for it in items:
        text = (it.get("text") or "") + (it.get("responds_to") or "") + (it.get("opinion") or "")
        matched = [s for s in info_items if likely_overlap(s.get("emperor_quote") or "", text)]
        if matched:
            it["__pendingInfoSources"] = matched
    if info_items and not any(it.get("__pendingInfoSources") for it in items):
        for it in items:
            it["__pendingInfoSources"] = info_items


def fallback_zhupi_items(doc: dict[str, Any]) -> list[dict[str, Any]]:
    text = (doc.get("rescript_text") or doc.get("rescript") or "").strip()
    if doc.get("doc_type") != "硃批" or not text:
        return []
    marker = text if len(text) <= 16 else ""
    author = author_name(doc)
    title = f"批「{text}」" if marker else f"對{author or '原奏官員'}奏報作出硃批"
    return [{
        "doc_id": doc_id(doc),
        "text": text,
        "position": "尾批",
        "responds_to": doc.get("title") or "",
        "opinion": "皇帝以硃批表示已閱悉並作出簡短回應。",
        "title": title,
        "marker": marker,
        "where": "",
        "who": [author] if author else [],
        "who_loc": {},
        "relations": [],
    }]


def attach_info_to_edicts(matches: list[dict[str, Any]], info_by_edict: dict[str, list[dict[str, Any]]]) -> None:
    for match in matches:
        info_items = info_by_edict.get(str(match.get("edict_id") or ""), [])
        for pt in match.get("points") or []:
            text = (pt.get("edict_quote") or "") + (pt.get("how") or "")
            matched = [s for s in info_items if likely_overlap(s.get("emperor_quote") or "", text)]
            if matched:
                pt["__pendingInfoSources"] = matched


def run_situfit(proxy: str, model: str, records: list[dict[str, Any]], mem: dict[str, Any], timeout: int, retries: int, retry_sleep: int) -> dict[str, Any] | None:
    send = date_pair_value(mem, "send_date")
    recv = date_pair_value(mem, "receive_date")
    ds = parse_date(send)
    dr = parse_date(recv)
    if not ds or not dr:
        return None
    lo, hi = sorted([ds, dr])
    base_id = doc_id(mem)
    change_docs = []
    response_docs = []
    for r in records:
        if doc_id(r) == base_id:
            continue
        if r.get("doc_type") != "上諭":
            d = parse_date(date_pair_value(r, "send_date") or date_pair_value(r, "receive_date"))
            if d and lo <= d <= hi:
                change_docs.append(r)
        if r.get("doc_type") in {"硃批", "上諭"}:
            rd = date_pair_value(r, "announce_date") if r.get("doc_type") == "上諭" else date_pair_value(r, "receive_date")
            if dates_within_days(rd, recv, 3, forward_only=True):
                response_docs.append(r)
    baseline = {"doc_id": base_id, "title": mem.get("title") or "", "author": author_name(mem), "sendAr": send, "recvAr": recv, "body": body_of(mem), "rescript": mem.get("rescript_text") or mem.get("rescript") or "", "summary": mem.get("summary") or {}}
    change_payload = [{"doc_id": doc_id(r), "title": r.get("title") or "", "author": author_name(r), "type": r.get("doc_type") or "", "sendAr": date_pair_value(r, "send_date"), "recvAr": date_pair_value(r, "receive_date"), "body": body_of(r)} for r in change_docs]
    response_payload = [{"doc_id": doc_id(r), "title": r.get("title") or "", "type": r.get("doc_type") or "", "date": date_pair_value(r, "announce_date") if r.get("doc_type") == "上諭" else date_pair_value(r, "receive_date"), "recipients": r.get("recipients") or [], "body": body_of(r), "rescript": r.get("rescript_text") or r.get("rescript") or ""} for r in response_docs]
    question = (
        "以下是一份奏摺（上奏）與皇帝硃批的基本資料（baseline），以及該奏摺上奏日至硃批受文日之間，其他官員所上呈的其他奏摺／文書（change_docs），"
        "還有硃批受文日起至其後 3 日內頒布／發出的所有硃批與上諭（response_docs）。請判斷皇帝回應時實際情勢是否已變，以及回應是否切合當時情勢。"
        '請只輸出 JSON，格式：{"situation":"","changes":[{"doc_id":"","subtitle":"","title":"","author":"","sentAr":"","quote":"","how":""}],"responses":[{"doc_id":"","type":"","date":"","quote":"","note":""}],"verdict":"fits/stale-but-harmless/mismatch","reasoning":""}。'
        "\n【baseline】\n" + json.dumps(baseline, ensure_ascii=False)
        + "\n【change_docs】\n" + json.dumps(change_payload, ensure_ascii=False)
        + "\n【response_docs】\n" + json.dumps(response_payload, ensure_ascii=False)
    )
    data = post_json(proxy, {"mode": "ask", "model": model, "question": question, "prompt": question}, timeout, retries, retry_sleep)
    result = data if data.get("situation") or data.get("verdict") else extract_json_object(data.get("text") or data.get("answer") or "")
    if not result:
        return None
    return {
        "doc_id": base_id,
        "memDoc": base_id,
        "memTitle": mem.get("title") or "",
        "memAuthor": author_name(mem),
        "sendAr": send,
        "recvAr": recv,
        "situation": result.get("situation") or "",
        "changes": result.get("changes") or [],
        "responses": result.get("responses") or [],
        "verdict": result.get("verdict") or "",
        "reasoning": result.get("reasoning") or "",
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--proxy", default=os.environ.get("GEMINI_PROXY_URL", ""))
    ap.add_argument("--model", default=os.environ.get("GEMINI_MODEL", "gemini-2.5-flash"))
    ap.add_argument("--doc-ids", default=DEFAULT_DOC_IDS)
    ap.add_argument("--bundle", default="test-tai83-90-155-156-full-chain")
    ap.add_argument("--timeout", type=int, default=240)
    ap.add_argument("--retries", type=int, default=4)
    ap.add_argument("--retry-sleep", type=int, default=15)
    ap.add_argument("--input-price-per-million", type=float, default=None,
                    help="Override input price in USD per 1M tokens")
    ap.add_argument("--output-price-per-million", type=float, default=None,
                    help="Override output price in USD per 1M tokens")
    ap.add_argument("--skip-done", action="store_true")
    args = ap.parse_args()
    if not args.proxy:
        raise SystemExit("Set GEMINI_PROXY_URL or pass --proxy.")

    records = json.loads(SOURCE.read_text(encoding="utf-8"))
    by_id = {doc_id(r): r for r in records}
    wanted = [s.strip() for s in args.doc_ids.split(",") if s.strip()]
    missing = [x for x in wanted if x not in by_id]
    if missing:
        raise SystemExit("Missing doc_id(s): " + ", ".join(missing))
    docs = [by_id[x] for x in wanted]

    out_root = ROOT / "outputs" / "review-bundles" / args.bundle
    out_dir = out_root / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_root / "human-edits").mkdir(parents=True, exist_ok=True)
    status_path = out_dir / "_run-status.json"
    status = read_json(status_path, {}) if args.skip_done else {}

    def done(did: str, step: str) -> bool:
        return bool(args.skip_done and status.get(did, {}).get(step))

    def mark(did: str, step: str) -> None:
        status.setdefault(did, {})[step] = True
        write_json(status_path, status)

    divisions = read_json(out_dir / "division-parts.json", []) if args.skip_done else []
    lin_events = read_json(out_dir / "lin-events.json", []) if args.skip_done else []
    qing_rows = {step: (read_json(out_dir / f"{step}.json", []) if args.skip_done else []) for step in QING_STEPS}
    source_rows = read_json(out_dir / "source-chain.json", []) if args.skip_done else []
    zhupi_rows = read_json(out_dir / "zhupi.json", []) if args.skip_done else []
    edict_rows = read_json(out_dir / "edict-match.json", []) if args.skip_done else []
    situfit_rows = read_json(out_dir / "situfit.json", []) if args.skip_done else []

    all_edicts = [r for r in records if r.get("doc_type") == "上諭"]

    for idx, doc in enumerate(docs, 1):
        did = doc_id(doc)
        print(f"[{idx}/{len(docs)}] {did} {doc.get('doc_type')} {doc.get('title')}")

        if done(did, "divide"):
            print("  - divide (skip done)")
        else:
            print("  - divide")
            payload = record_payload(doc, "divide", args.model)
            inst = skill_prompt("divide")
            if inst:
                payload["instruction"] = inst
            with accounting_step("divide"):
                data = post_json(args.proxy, payload, args.timeout, args.retries, args.retry_sleep)
            divisions.append({"doc_id": did, "title": doc.get("title") or "", "parts": data.get("parts", []), "_raw": data})
            write_json(out_dir / "division-parts.json", divisions)
            mark(did, "divide")

        if done(did, "lin-events"):
            print("  - lin-events + source (skip done)")
            doc_lin = [x for x in lin_events if str(x.get("doc_id")) == did]
        else:
            print("  - lin-events + source")
            with accounting_step("lin-events + source"):
                doc_lin = run_event_step(args.proxy, args.model, doc, "lin", "", "lin-events", args.timeout, args.retries, args.retry_sleep)
            lin_events.extend(doc_lin)
            with accounting_step("lin-events + source"):
                chains = run_doc_trace(args.proxy, args.model, doc, "lin", [x.get("subtitle") or "" for x in doc_lin], args.timeout, args.retries, args.retry_sleep)
            if chains:
                source_rows.append({"doc_id": did, "evTitle": "全部林方事件來源", "actor": "lin", "chains": chains})
            write_json(out_dir / "lin-events.json", lin_events)
            write_json(out_dir / "source-chain.json", source_rows)
            mark(did, "lin-events")

        if done(did, "qing-events-all"):
            print("  - qing events + source (skip done)")
        else:
            print("  - qing events + source")
            all_qing_titles = []
            for step, (category, _) in QING_STEPS.items():
                with accounting_step("qing events + source"):
                    items = run_event_step(args.proxy, args.model, doc, "qing", category, step, args.timeout, args.retries, args.retry_sleep)
                qing_rows[step].extend(items)
                all_qing_titles.extend(x.get("subtitle") or "" for x in items)
                write_json(out_dir / f"{step}.json", qing_rows[step])
            with accounting_step("qing events + source"):
                chains = run_doc_trace(args.proxy, args.model, doc, "qing", all_qing_titles, args.timeout, args.retries, args.retry_sleep)
            if chains:
                source_rows.append({"doc_id": did, "evTitle": "全部清方事件來源", "actor": "qing", "chains": chains})
                write_json(out_dir / "source-chain.json", source_rows)
            mark(did, "qing-events-all")

        if done(did, "zhupi"):
            print("  - zhupi + info source (skip done)")
        else:
            print("  - zhupi + info source")
            payload = record_payload(doc, "zhupi", args.model)
            extra = skill_prompt("zhupi")
            if extra:
                payload["question"] = extra
            with accounting_step("zhupi + info source"):
                data = post_json(args.proxy, payload, args.timeout, args.retries, args.retry_sleep)
            items = [dict(x, doc_id=did) for x in data.get("zhupi", [])]
            if not items:
                items = fallback_zhupi_items(doc)
            if items:
                with accounting_step("zhupi + info source"):
                    info_items = safe_fetch_info_sources(args.proxy, args.model, records, doc, doc.get("rescript_text") or doc.get("rescript") or body_of(doc), args.timeout, args.retries, args.retry_sleep)
                attach_info_to_zhupi(items, info_items)
            zhupi_rows.extend(items)
            write_json(out_dir / "zhupi.json", zhupi_rows)
            mark(did, "zhupi")

        if done(did, "edict-match"):
            print("  - edict-match + info source (skip done)")
        else:
            print("  - edict-match + info source")
            if doc.get("doc_type") == "上諭":
                print("    - skip 上諭 source document")
                mark(did, "edict-match")
                continue
            base = primary_date(doc)
            cands = [r for r in all_edicts if within_days(primary_date(r), base, 3)][:20] if base else []
            matches_for_doc = []
            for j, ed in enumerate(cands, 1):
                edid = doc_id(ed)
                print(f"    - {j}/{len(cands)} {did} x {edid}")
                payload = {
                    "mode": "edict_match",
                    "model": args.model,
                    "question": skill_prompt("edict-match"),
                    "memorial": {"id": did, "title": doc.get("title") or "", "date": base, "body": body_of(doc)},
                    "edicts": [{"id": edid, "date": primary_date(ed), "title": ed.get("title") or "", "body": body_of(ed)}],
                }
                with accounting_step("edict-match + info source"):
                    data = post_json(args.proxy, payload, args.timeout, args.retries, args.retry_sleep)
                for match in data.get("matches", []):
                    pts = match.get("points") if isinstance(match.get("points"), list) else []
                    if not pts and (match.get("memorial_quote") or match.get("edict_quote") or match.get("how")):
                        pts = [{"aspect": "", "memorial_quote": match.get("memorial_quote") or "", "edict_quote": match.get("edict_quote") or "", "how": match.get("how") or ""}]
                    matches_for_doc.append({"doc_id": did, "memDoc": did, "memTitle": doc.get("title") or "", "edict_id": str(match.get("edict_id") or edid), "title": ed.get("title") or "", "date": primary_date(ed), "summary": match.get("summary") or "", "points": pts})
            info_by_edict = {}
            for eid in sorted({str(x.get("edict_id") or "") for x in matches_for_doc if x.get("edict_id")}):
                ed = by_id.get(eid)
                if ed:
                    with accounting_step("edict-match + info source"):
                        info_by_edict[eid] = safe_fetch_info_sources(args.proxy, args.model, records, ed, body_of(ed), args.timeout, args.retries, args.retry_sleep)
            attach_info_to_edicts(matches_for_doc, info_by_edict)
            edict_rows.extend(matches_for_doc)
            write_json(out_dir / "edict-match.json", edict_rows)
            mark(did, "edict-match")

        if done(did, "situfit"):
            print("  - situfit (skip done)")
        else:
            print("  - situfit")
            with accounting_step("situfit"):
                sf = run_situfit(args.proxy, args.model, records, doc, args.timeout, args.retries, args.retry_sleep)
            if sf:
                situfit_rows.append(sf)
                write_json(out_dir / "situfit.json", situfit_rows)
            mark(did, "situfit")

    print("- official-response")
    official_path = out_dir / "official-response.json"
    official_rows = read_json(official_path, []) if args.skip_done else []
    existing = {(str(r.get("doc_id")), str(r.get("evTitle") or "")) for r in official_rows}
    doc_ids = {doc_id(d) for d in docs}
    actions = []
    for it in zhupi_rows:
        did = str(it.get("doc_id") or "")
        if did not in doc_ids:
            continue
        rec = by_id.get(did) or {}
        actions.append({"doc_id": did, "memDoc": did, "evTitle": it.get("title") or it.get("text") or "硃批", "dateAr": date_pair_value(rec, "receive_date") or date_pair_value(rec, "send_date"), "quote": it.get("text") or it.get("marker") or "", "addressee": [author_name(rec)] if author_name(rec) else []})
    for it in edict_rows:
        eid = str(it.get("edict_id") or "")
        mid = str(it.get("doc_id") or it.get("memDoc") or "")
        if eid not in doc_ids and mid not in doc_ids:
            continue
        ed = by_id.get(eid) or {}
        pts = it.get("points") or []
        for pt in pts or [{}]:
            actions.append({"doc_id": eid, "memDoc": mid, "evTitle": pt.get("title") or pt.get("aspect") or it.get("title") or "上諭", "dateAr": it.get("date") or date_pair_value(ed, "announce_date") or date_pair_value(ed, "send_date"), "quote": pt.get("edict_quote") or "", "addressee": list(ed.get("recipients") or [])})
    for j, act in enumerate(actions, 1):
        key = (act["doc_id"], act["evTitle"])
        if args.skip_done and key in existing:
            print(f"  - {j}/{len(actions)} skip {act['evTitle']}")
            continue
        if not act["dateAr"]:
            continue
        cands = official_response_candidates(records, act["dateAr"], act["doc_id"], act["addressee"])
        payload = {
            "mode": "official_response",
            "model": args.model,
            "action": {"what": act["evTitle"], "dateAr": act["dateAr"], "quote": act["quote"]},
            "addressee": "、".join(act["addressee"]) if act["addressee"] else "",
            "candidates": [{"doc_id": doc_id(c), "title": c.get("title") or "", "date": doc_best_ar(c), "body": body_of(c)} for c in cands],
            "question": skill_prompt("official-response"),
        }
        with accounting_step("official-response"):
            data = post_json(args.proxy, payload, args.timeout, args.retries, args.retry_sleep)
        official_rows.append({"doc_id": act["doc_id"], "memDoc": act.get("memDoc") or act["doc_id"], "evTitle": act["evTitle"], "addressee": data.get("addressee") or payload["addressee"], "items": data.get("items", [])})
        write_json(official_path, official_rows)

    manifest = {
        "name": args.bundle,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "source": str(SOURCE.relative_to(ROOT)),
        "model": args.model,
        "doc_ids": wanted,
        "chain": ["divide", "lin-events+source", "qing-events-done+source", "qing-events-plan+source", "qing-events-nonmil+source", "zhupi+info-source", "edict-match+info-source", "situfit", "official-response"],
    }
    write_json(out_root / "manifest.json", manifest)
    write_json(out_root / "human-edits" / "notes.json", [])
    print(f"\nWrote bundle: {out_root.relative_to(ROOT)}")
    cost_summary = print_cost_summary(
        args.model,
        args.input_price_per_million,
        args.output_price_per_million,
    )
    write_json(out_root / "cost-summary.json", cost_summary)


if __name__ == "__main__":
    main()
