#!/usr/bin/env python3
"""Run the website's saved AI prompts / skills as one batch loop over selected
documents, writing a review bundle the timeline page can load back into its AI
chat + chart review interface.

This is the "controlled test first, larger corpus later" runner. By default it
processes a SINGLE document (台297) with gemini-3.5-flash so you can eyeball the
result before scaling up:

    GEMINI_PROXY_URL=https://... \
        python3 scripts/run_saved_prompt_chain_test.py

Per-document question sequence (mirrors the loop the user asked for, and the
order the website's skillBundleFileOrder() renders bundle files in):

  1. divide                     -> division-parts.json      分段標註
  2. lin-events   + source-chain (per event, side=lin)
  3. qing-events-done/plan/nonmil + source-chain (per event, side=qing)
  4. zhupi + edict-match        + info-source (皇帝文書資訊來源) attached
  5. 回應時效 (situ-fit)         -> situfit.json
  6. 官員回應 (official-response) -> official-response.json  (post-loop pass)

Every prompt text comes from llm-wiki/skills/*.md via skill_prompt(), so this
runner and the in-browser buttons always use identical wording. The extraction
steps do NOT contain the source-chain search themselves -- source-chain is its
own skill (trace-source-chain.md, proxy mode "trace") that this loop runs once
per extracted event and attaches, exactly as the website does. See the module
docstring of trace-source-chain.md ("called once per extracted event -- the only
way to give it a specific event to anchor the trace to").

Design notes / how this differs from run_mass_prompt_chain_test.py:
  * source-chain is a PER-EVENT single trace (side + single=True + event=...),
    then merged by hop signature into one row per document. The mass script did
    a whole-document trace scan and never merged, so its chains were not anchored
    to individual events and would not link onto the extracted event cards.
  * emperor material (硃批/上諭) additionally gets an info-source lookup, written
    as zhupi-info-source.json so it groups with the emperor block on load.
  * situ-fit (回應時效) and info-source reuse the EXACT Chinese prompt strings the
    website builds (runSituFit / fetchInfoSources in stage1-timeline.html).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

# Reuse the proven helpers from the single-bundle runner so both scripts stay in
# lockstep on proxy calling, date semantics, candidate selection and chain merge.
from run_review_bundle_test import (  # noqa: E402
    ROOT,
    SOURCE,
    date_pair_value,
    doc_best_ar,
    merge_source_chains_by_signature,
    official_response_candidates,
    parse_date,
    post_json,
    primary_date,
    read_json,
    record_payload,
    skill_prompt,
    split_csv,
    within_days,
    write_json,
)

DEFAULT_DOC_IDS = "台297"
DEFAULT_MODEL = "gemini-3.5-flash"

# qing-events-* steps: proxy mode "events", actor "qing", + a category. Order
# here is the order they run and the order their files sort in on the website.
QING_STEPS = {
    "qing-events-done": "done",
    "qing-events-plan": "plan",
    "qing-events-nonmil": "nonmil",
}

# All steps this runner can produce, in loop order. Also the manifest chain.
ALL_STEPS = [
    "divide",
    "lin-events",
    "qing-events-done",
    "qing-events-plan",
    "qing-events-nonmil",
    "source-chain",
    "zhupi",
    "edict-match",
    "info-source",
    "situfit",
    "official-response",
]


# ---------------------------------------------------------------------------
# small field helpers (source JSON shape: author is a {position,name} dict, and
# dates are ["中曆", "YYYY/M/D"] pairs -- see stage1-date-adjusted.json)
# ---------------------------------------------------------------------------

def doc_id_of(rec: dict[str, Any]) -> str:
    return str(rec.get("doc_id") or rec.get("id") or "")


def author_name(rec: dict[str, Any]) -> str:
    a = rec.get("author")
    if isinstance(a, dict):
        return a.get("name") or ""
    if isinstance(a, str):
        return a
    return rec.get("author_name") or ""


def send_ar(rec: dict[str, Any]) -> str:
    return date_pair_value(rec, "send_date")


def recv_ar(rec: dict[str, Any]) -> str:
    return date_pair_value(rec, "receive_date")


def ann_ar(rec: dict[str, Any]) -> str:
    return date_pair_value(rec, "announce_date")


def body_of(rec: dict[str, Any]) -> str:
    return rec.get("body") or ""


def rescript_of(rec: dict[str, Any]) -> str:
    return rec.get("rescript_text") or rec.get("rescript") or ""


def strip_fences(text: str) -> str:
    """Pull a JSON object/array out of a possibly ```-fenced model reply."""
    if not text:
        return text
    t = text.strip()
    m = re.match(r"^```[a-zA-Z]*\n(.*?)\n```$", t, re.S)
    if m:
        return m.group(1).strip()
    return t


def parse_ask_json(data: dict[str, Any]) -> dict[str, Any] | None:
    """mode:'ask' replies come back as {"text": "...json..."} (sometimes already
    parsed into {situation/items/...}). Return a dict or None. Mirrors the
    website's `if(data.situation||data.verdict) ... else JSON.parse(text)`."""
    if not isinstance(data, dict):
        return None
    if data.get("situation") or data.get("verdict") or isinstance(data.get("items"), list):
        return data
    for key in ("text", "answer"):
        raw = data.get(key)
        if raw:
            try:
                return json.loads(strip_fences(raw))
            except Exception:
                continue
    return None


# ---------------------------------------------------------------------------
# step 4b: 皇帝文書資訊來源 (info-source) -- reverse of edict-match: start from the
# emperor's own text, trace each fact back to an earlier official document.
# Python mirror of infoSourceCandidateDocs()/fetchInfoSources() in the HTML.
# ---------------------------------------------------------------------------

INFO_SOURCE_QUESTION = (
    "以下是一份皇帝文書（硃批或上諭）的原文（emperor_text），以及在此文書之前，各官員所上呈的候選奏摺／文書列表（candidates）。"
    "請找出皇帝原文中，皇帝所提及／回應的每一項具體資訊（事實、回報的情況、人名、地名、事件等——不要包含皇帝自己下達的命令或意見），"
    "並針對每一項資訊，判斷它最可能是根據 candidates 中哪一份文書、哪一段引文而來（同一份候選文書可以對應多項資訊，不同資訊也可以對應到不同的候選文書；若找不到可信的來源文書則不必勉強列出）。"
    "請只輸出 JSON，格式：{\"items\":[{\"info\":\"皇帝提及的這項資訊（一句話概述）\",\"doc_id\":\"該資訊來源候選文書的id\",\"quote\":\"該候選文書中的引文（逐字，來自該文書原文，硃批可用 rescript 欄位文字）\",\"emperor_quote\":\"皇帝文書中引用或提及此資訊的原文（逐字）\"}]}。"
)


def info_source_own_date(rec: dict[str, Any]) -> str:
    if rec.get("doc_type") == "上諭":
        return ann_ar(rec) or send_ar(rec)
    return recv_ar(rec) or send_ar(rec) or ann_ar(rec)


def info_source_candidate_docs(records: list[dict[str, Any]], base: dict[str, Any], lookback_days: int = 60) -> list[dict[str, Any]]:
    base_date = parse_date(info_source_own_date(base))
    if not base_date:
        return []
    base_id = doc_id_of(base)
    out: list[tuple[Any, dict[str, Any]]] = []
    for r in records:
        if r.get("doc_type") == "上諭":
            continue
        if doc_id_of(r) == base_id:
            continue
        d = parse_date(send_ar(r) or recv_ar(r))
        if not d:
            continue
        if (base_date - d).days > 0 and (base_date - d).days <= lookback_days:
            out.append((d, r))
    out.sort(key=lambda x: x[0])
    return [r for _, r in out]


def run_info_source(proxy: str, model: str, records: list[dict[str, Any]], base: dict[str, Any], timeout: int, retries: int, retry_sleep: int) -> dict[str, Any] | None:
    """Returns a bundle row {docId, doc_id, docType, docTitle, targetEvId, items}
    or None if there was nothing to analyse. items[] carry info/quote/doc_id/
    emperor_quote plus resolved source metadata (matching the website's
    committed infoSources shape)."""
    emperor_text = rescript_of(base) if base.get("doc_type") == "硃批" else body_of(base)
    if not emperor_text or not info_source_own_date(base):
        return None
    cands = info_source_candidate_docs(records, base)
    if not cands:
        return None
    cand_payload = [
        {
            "doc_id": doc_id_of(r),
            "title": r.get("title") or "",
            "author": author_name(r),
            "type": r.get("doc_type") or "",
            "sendAr": send_ar(r),
            "recvAr": recv_ar(r),
            "body": body_of(r),
        }
        for r in cands
    ]
    question = (
        INFO_SOURCE_QUESTION
        + "\n【emperor_text】\n" + emperor_text
        + "\n【candidates】\n" + json.dumps(cand_payload, ensure_ascii=False)
    )
    data = post_json(proxy, {"mode": "ask", "model": model, "question": question, "prompt": question}, timeout, retries, retry_sleep)
    result = parse_ask_json(data)
    raw_items = (result or {}).get("items") or []
    by_id = {doc_id_of(r): r for r in records}
    base_date = parse_date(info_source_own_date(base))
    items = []
    for it in raw_items:
        did = str(it.get("doc_id") or "")
        if not it.get("info") or not did:
            continue
        src = by_id.get(did) or {}
        src_date = parse_date(send_ar(src) or recv_ar(src)) if src else None
        days_before = (base_date - src_date).days if (base_date and src_date) else None
        items.append({
            "include": True,
            "info": it.get("info") or "",
            "quote": it.get("quote") or "",
            "doc_id": did,
            "emperor_quote": it.get("emperor_quote") or "",
            "srcTitle": src.get("title") or "",
            "srcAuthor": author_name(src),
            "srcSentAr": send_ar(src) or recv_ar(src),
            "daysBeforeEmperor": days_before,
            "emperorDocId": doc_id_of(base),
        })
    return {
        "docId": doc_id_of(base),
        "doc_id": doc_id_of(base),
        "docType": base.get("doc_type") or "",
        "docTitle": base.get("title") or "",
        "targetEvId": "",
        "items": items,
        "candCount": len(cands),
    }


# ---------------------------------------------------------------------------
# step 5: 回應時效 (situ-fit) -- did the situation move on before the emperor's
# rescript/edicts landed, and does the response fit the real situation?
# Python mirror of situFitWindowDocs/situFitResponseDocs/runSituFit in the HTML.
# ---------------------------------------------------------------------------

SITUFIT_QUESTION = (
    "以下是一份奏摺（上奏）與皇帝硃批的基本資料（baseline），以及該奏摺上奏日至硃批受文日之間，其他官員（不限於本奏摺作者）所上呈的其他奏摺／文書（change_docs，已排除本奏摺本身與上諭），"
    "還有硃批受文日起至其後 3 日內頒布／發出的所有硃批與上諭（response_docs，即皇帝的回應）。"
    "請判斷：在皇帝寫下硃批／發布上諭回應本奏摺時，實際情勢是否已經與本奏摺原本回報的情況不同（例如戰況已改變、地點已易手、官員已提出新對策等）。"
    "再判斷皇帝的回應（response_docs）是否切合當時的實際情勢，或只是針對本奏摺已經過時的舊報告作出回應。"
    "請只輸出 JSON，格式：{\"situation\":\"本奏摺原本回報的情勢摘要\","
    "\"changes\":[{\"doc_id\":\"文書id\",\"subtitle\":\"此文書內容的簡短標目（一句話，如同事件摘要）\",\"title\":\"標題\",\"author\":\"作者\",\"sentAr\":\"YYYY/M/D\",\"quote\":\"引文（逐字，來自該文書原文）\",\"how\":\"此文書顯示情勢如何變化\"}],"
    "\"responses\":[{\"doc_id\":\"文書id\",\"type\":\"硃批或上諭\",\"date\":\"YYYY/M/D\",\"quote\":\"引文（逐字，來自該文書原文，硃批可用 rescript 欄位文字）\",\"note\":\"此回應內容概述\"}],"
    "\"verdict\":\"fits/stale-but-harmless/mismatch\",\"reasoning\":\"詳述理由，並引用 changes／responses 中的 doc_id 與引文\"}。"
    "verdict 三選一：fits＝回應切合實際情勢；stale-but-harmless＝回應雖基於舊情勢但未造成實質影響；mismatch＝回應與實際情勢明顯不符。"
)


def situ_change_docs(records: list[dict[str, Any]], mem: dict[str, Any]) -> list[dict[str, Any]]:
    start, end = parse_date(send_ar(mem)), parse_date(recv_ar(mem))
    if not start or not end:
        return []
    lo, hi = (start, end) if start <= end else (end, start)
    base_id = doc_id_of(mem)
    out: list[tuple[Any, dict[str, Any]]] = []
    for r in records:
        if r.get("doc_type") == "上諭":
            continue
        if doc_id_of(r) == base_id:
            continue
        d = parse_date(send_ar(r) or recv_ar(r))
        if not d:
            continue
        if lo <= d <= hi:
            out.append((d, r))
    out.sort(key=lambda x: x[0])
    return [r for _, r in out]


def situ_response_docs(records: list[dict[str, Any]], mem: dict[str, Any]) -> list[dict[str, Any]]:
    base = recv_ar(mem)
    base_date = parse_date(base)
    if not base_date:
        return []
    base_id = doc_id_of(mem)
    out: list[tuple[Any, dict[str, Any]]] = []
    for r in records:
        dt = r.get("doc_type")
        if dt not in ("硃批", "上諭"):
            continue
        if dt == "硃批" and doc_id_of(r) == base_id:
            continue
        d = parse_date(ann_ar(r)) if dt == "上諭" else parse_date(recv_ar(r))
        if not d or d < base_date:
            continue
        if within_days(d.isoformat(), base, 3):
            out.append((d, r))
    out.sort(key=lambda x: x[0])
    return [r for _, r in out]


def run_situfit(proxy: str, model: str, records: list[dict[str, Any]], mem: dict[str, Any], timeout: int, retries: int, retry_sleep: int) -> dict[str, Any] | None:
    if mem.get("doc_type") != "硃批" or not send_ar(mem) or not recv_ar(mem):
        return None
    change_docs = situ_change_docs(records, mem)
    response_docs = situ_response_docs(records, mem)
    baseline = {
        "doc_id": doc_id_of(mem), "title": mem.get("title") or "", "author": author_name(mem),
        "sendAr": send_ar(mem), "recvAr": recv_ar(mem), "lag": None,
        "body": body_of(mem), "rescript": rescript_of(mem), "summary": "",
    }
    change_payload = [
        {"doc_id": doc_id_of(r), "title": r.get("title") or "", "author": author_name(r),
         "type": r.get("doc_type") or "", "sendAr": send_ar(r), "recvAr": recv_ar(r), "body": body_of(r)}
        for r in change_docs
    ]
    response_payload = [
        {"doc_id": doc_id_of(r), "title": r.get("title") or "", "type": r.get("doc_type") or "",
         "date": (ann_ar(r) if r.get("doc_type") == "上諭" else recv_ar(r)),
         "recipients": r.get("recipients") or [], "body": body_of(r), "rescript": rescript_of(r)}
        for r in response_docs
    ]
    question = (
        SITUFIT_QUESTION
        + "\n【baseline】\n" + json.dumps(baseline, ensure_ascii=False)
        + "\n【change_docs】\n" + json.dumps(change_payload, ensure_ascii=False)
        + "\n【response_docs】\n" + json.dumps(response_payload, ensure_ascii=False)
    )
    data = post_json(proxy, {"mode": "ask", "model": model, "question": question, "prompt": question}, timeout, retries, retry_sleep)
    result = parse_ask_json(data)
    if not result:
        return None
    changes = [{
        "doc_id": str(ch.get("doc_id") or ""), "subtitle": ch.get("subtitle") or "", "title": ch.get("title") or "",
        "author": ch.get("author") or "", "sentAr": ch.get("sentAr") or ch.get("sendAr") or "",
        "quote": ch.get("quote") or "", "how": ch.get("how") or "",
    } for ch in (result.get("changes") or [])]
    responses = [{
        "doc_id": str(rp.get("doc_id") or ""), "type": rp.get("type") or "", "date": rp.get("date") or "",
        "quote": rp.get("quote") or "", "note": rp.get("note") or "",
    } for rp in (result.get("responses") or [])]
    return {
        "doc_id": doc_id_of(mem), "memDoc": doc_id_of(mem), "memTitle": mem.get("title") or "",
        "memAuthor": author_name(mem), "sendAr": send_ar(mem), "recvAr": recv_ar(mem),
        "situation": result.get("situation") or "", "changes": changes, "responses": responses,
        "verdict": result.get("verdict") or "", "reasoning": result.get("reasoning") or "",
        "_meta": {"changeDocs": len(change_docs), "responseDocs": len(response_docs)},
    }


# ---------------------------------------------------------------------------
# per-event source-chain (mode "trace", single=True) -- one call per event.
# ---------------------------------------------------------------------------

def trace_event(proxy: str, model: str, doc: dict[str, Any], item: dict[str, Any], side: str, timeout: int, retries: int, retry_sleep: int) -> dict[str, Any]:
    payload = record_payload(doc, "trace", model)
    extra = skill_prompt("source-chain")
    payload.update({
        "side": side,
        "single": True,
        **({"question": extra} if extra else {}),
        "event": {
            "actor": side,
            "subtitle": item.get("subtitle") or "",
            "description": item.get("description") or "",
            "where": item.get("where") or "",
            "whenCh": item.get("whenCh") or item.get("whenAr") or "",
            "quote": item.get("quote") or "",
        },
    })
    try:
        tr = post_json(proxy, payload, timeout, retries, retry_sleep)
    except Exception as exc:  # keep going; a failed trace shouldn't abort the loop
        print(f"      source-chain failed, saved error and continuing: {exc}")
        tr = {"mode": "trace", "chains": [], "error": str(exc)}
    return {
        "doc_id": doc_id_of(doc),
        "evTitle": item.get("subtitle") or "",
        "actor": side,
        "event": item,
        "chains": tr.get("chains", []),
    }


def run_events(proxy: str, model: str, doc: dict[str, Any], actor: str, category: str, step: str, timeout: int, retries: int, retry_sleep: int) -> list[dict[str, Any]]:
    payload = record_payload(doc, "events", model)
    payload.update({"actor": actor, "category": category, "actor_instruction": skill_prompt(step)})
    data = post_json(proxy, payload, timeout, retries, retry_sleep)
    items = []
    for it in data.get("events", []):
        it.setdefault("doc_id", doc_id_of(doc))
        items.append(it)
    return items


# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--proxy", default=os.environ.get("GEMINI_PROXY_URL", ""), help="Gemini proxy base URL")
    ap.add_argument("--model", default=os.environ.get("GEMINI_MODEL", DEFAULT_MODEL))
    ap.add_argument("--doc-ids", default=DEFAULT_DOC_IDS, help="Comma-separated doc IDs (default 台297)")
    ap.add_argument("--steps", default=",".join(ALL_STEPS), help="Comma-separated subset of: " + ",".join(ALL_STEPS))
    ap.add_argument("--bundle", default="")
    ap.add_argument("--timeout", type=int, default=240)
    ap.add_argument("--retries", type=int, default=4)
    ap.add_argument("--retry-sleep", type=int, default=15)
    ap.add_argument("--skip-done", action="store_true", help="Resume an existing bundle, skip completed doc-level steps")
    ap.add_argument("--dry-run", action="store_true", help="No proxy calls: just resolve docs/candidates and report the plan")
    args = ap.parse_args()

    steps = set(split_csv(args.steps))
    records = json.loads(SOURCE.read_text(encoding="utf-8"))
    by_id = {doc_id_of(r): r for r in records}
    wanted = split_csv(args.doc_ids)
    missing = [d for d in wanted if d not in by_id]
    if missing:
        raise SystemExit("Missing doc_id(s): " + ", ".join(missing))
    docs = [by_id[d] for d in wanted]

    # A bundle name made of every doc id blows past the filesystem's 255-byte name limit once you
    # run more than a handful of docs, so only spell out the ids for small sets; otherwise use the
    # first id + a count + a short hash of the full list (stable, so re-running the same set with
    # --skip-done lands in the same bundle).
    ts = datetime.now().strftime('%Y%m%d-%H%M%S')
    if args.bundle:
        bundle_name = args.bundle
    elif len("-".join(wanted)) <= 60:
        bundle_name = f"saved-prompt-chain-{'-'.join(wanted)}-{ts}"
    else:
        digest = hashlib.sha1("-".join(wanted).encode("utf-8")).hexdigest()[:8]
        bundle_name = f"saved-prompt-chain-{wanted[0]}-plus{len(wanted) - 1}-{digest}-{ts}"
    out_root = ROOT / "outputs" / "review-bundles" / bundle_name
    out_dir = out_root / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_root / "human-edits").mkdir(parents=True, exist_ok=True)

    if args.dry_run:
        print(f"DRY RUN -- bundle would be: {out_root.relative_to(ROOT)}")
        print(f"model: {args.model}   steps: {sorted(steps)}")
        for doc in docs:
            did = doc_id_of(doc)
            print(f"\n[{did}] {doc.get('doc_type')} {doc.get('title')}")
            print(f"  send={send_ar(doc)!r} recv={recv_ar(doc)!r} ann={ann_ar(doc)!r} author={author_name(doc)!r}")
            if doc.get("doc_type") == "硃批":
                print(f"  situfit change_docs={len(situ_change_docs(records, doc))} response_docs={len(situ_response_docs(records, doc))}")
            if doc.get("doc_type") in ("硃批", "上諭"):
                print(f"  info-source candidate docs={len(info_source_candidate_docs(records, doc))}")
        print("\n(no proxy calls made)")
        return

    if not args.proxy:
        raise SystemExit("Set GEMINI_PROXY_URL or pass --proxy (or use --dry-run).")

    # output accumulators / files
    files = {
        "divide": out_dir / "division-parts.json",
        "lin-events": out_dir / "lin-events.json",
        "qing-events-done": out_dir / "qing-events-done.json",
        "qing-events-plan": out_dir / "qing-events-plan.json",
        "qing-events-nonmil": out_dir / "qing-events-nonmil.json",
        "source-chain": out_dir / "source-chain.json",       # merged, written at end
        "source-chain-raw": out_dir / "_source-chain-raw.json",  # per-event, pre-merge
        "zhupi": out_dir / "zhupi.json",
        "edict-match": out_dir / "edict-match.json",
        # named to group with the emperor block on load (skillBundleFileOrder
        # matches "zhupi" -> 80; applySkillChatOutput matches "info-source" first)
        "info-source": out_dir / "zhupi-info-source.json",
        "situfit": out_dir / "situfit.json",
        "official-response": out_dir / "official-response.json",
    }
    status_path = out_dir / "_run-status.json"
    status = read_json(status_path, {}) if args.skip_done else {}

    def load(step: str) -> list:
        return read_json(files[step], []) if args.skip_done else []

    divisions = load("divide")
    lin_events = load("lin-events")
    qing_rows = {s: load(s) for s in QING_STEPS}
    source_raw = read_json(files["source-chain-raw"], []) if args.skip_done else []
    zhupi_rows = load("zhupi")
    edict_rows = load("edict-match")
    info_rows = load("info-source")
    situfit_rows = load("situfit")

    all_edicts = [r for r in records if r.get("doc_type") == "上諭"]

    def is_done(did: str, step: str) -> bool:
        return bool(status.get(did, {}).get(step))

    def mark(did: str, step: str) -> None:
        status.setdefault(did, {})[step] = True
        write_json(status_path, status)

    def flush_source_chain() -> None:
        write_json(files["source-chain-raw"], source_raw)
        write_json(files["source-chain"], merge_source_chains_by_signature(source_raw))

    for i, doc in enumerate(docs, 1):
        did = doc_id_of(doc)
        print(f"[{i}/{len(docs)}] {did} {doc.get('doc_type')} {doc.get('title')}")

        # Any step here can hit an exhausted-retry proxy error (persistent 502 on a big prompt, a
        # dropped connection, etc). Each step writes + marks itself done the instant it succeeds, so
        # a failure part-way through a document just leaves the unfinished steps unmarked: wrap the
        # whole per-doc body so one bad step logs and skips to the NEXT document instead of aborting
        # the entire batch. Re-running with --skip-done then retries exactly the steps that failed.
        try:
            # 1. divide
            if "divide" in steps and not (args.skip_done and is_done(did, "divide")):
                print("  - divide")
                payload = record_payload(doc, "divide", args.model)
                instr = skill_prompt("divide")
                if instr:
                    payload["instruction"] = instr
                d = post_json(args.proxy, payload, args.timeout, args.retries, args.retry_sleep)
                divisions.append({"doc_id": did, "title": doc.get("title"), "parts": d.get("parts", []), "_raw": d})
                write_json(files["divide"], divisions)
                mark(did, "divide")

            # 2. 林方 actions (+ per-event source-chain, side=lin)
            lin_items: list[dict[str, Any]] = []
            if "lin-events" in steps and not (args.skip_done and is_done(did, "lin-events")):
                print("  - 林方行動")
                lin_items = run_events(args.proxy, args.model, doc, "lin", "", "lin-events", args.timeout, args.retries, args.retry_sleep)
                lin_events.extend(lin_items)
                write_json(files["lin-events"], lin_events)
                mark(did, "lin-events")
            elif "source-chain" in steps:
                lin_items = [e for e in lin_events if doc_id_of(e) == did]

            if "source-chain" in steps and not (args.skip_done and is_done(did, "source-chain-lin")):
                for j, item in enumerate(lin_items, 1):
                    print(f"  - 林方來源鏈 {j}/{len(lin_items)}: {item.get('subtitle') or ''}")
                    source_raw.append(trace_event(args.proxy, args.model, doc, item, "lin", args.timeout, args.retries, args.retry_sleep))
                    flush_source_chain()
                mark(did, "source-chain-lin")

            # 3. 清方 actions x3 categories (+ per-event source-chain, side=qing)
            qing_items: list[dict[str, Any]] = []
            for step, category in QING_STEPS.items():
                if step in steps and not (args.skip_done and is_done(did, step)):
                    print(f"  - {step}")
                    items = run_events(args.proxy, args.model, doc, "qing", category, step, args.timeout, args.retries, args.retry_sleep)
                    qing_rows[step].extend(items)
                    write_json(files[step], qing_rows[step])
                    qing_items.extend(items)
                    mark(did, step)
                elif "source-chain" in steps:
                    qing_items.extend(e for e in qing_rows[step] if doc_id_of(e) == did)

            if "source-chain" in steps and not (args.skip_done and is_done(did, "source-chain-qing")):
                for j, item in enumerate(qing_items, 1):
                    print(f"  - 清方來源鏈 {j}/{len(qing_items)}: {item.get('subtitle') or ''}")
                    source_raw.append(trace_event(args.proxy, args.model, doc, item, "qing", args.timeout, args.retries, args.retry_sleep))
                    flush_source_chain()
                mark(did, "source-chain-qing")

            # 4. emperor material: 硃批 + related 上諭 (edict-match), + info-source
            if "zhupi" in steps and not (args.skip_done and is_done(did, "zhupi")):
                print("  - zhupi")
                payload = record_payload(doc, "zhupi", args.model)
                zq = skill_prompt("zhupi")
                if zq:
                    payload["question"] = zq
                z = post_json(args.proxy, payload, args.timeout, args.retries, args.retry_sleep)
                for it in z.get("zhupi", []):
                    it = dict(it)
                    it.setdefault("doc_id", did)
                    zhupi_rows.append(it)
                write_json(files["zhupi"], zhupi_rows)
                mark(did, "zhupi")

            matched_edict_ids: list[str] = []
            if "edict-match" in steps and not (args.skip_done and is_done(did, "edict-match")):
                if doc.get("doc_type") == "上諭":
                    print("  - edict-match (skip 上諭 source)")
                    mark(did, "edict-match")
                else:
                    base = primary_date(doc)
                    cands = [r for r in all_edicts if within_days(primary_date(r), base, 3)][:20] if base else []
                    print(f"  - edict-match ({len(cands)} candidate 上諭)")
                    question = skill_prompt("edict-match")
                    for k, ed in enumerate(cands, 1):
                        ed_id = doc_id_of(ed)
                        print(f"    - {k}/{len(cands)} {did} × {ed_id}")
                        payload = {
                            "mode": "edict_match", "model": args.model, "question": question,
                            "memorial": {"id": did, "title": doc.get("title") or "", "date": base, "body": body_of(doc)},
                            "edicts": [{"id": ed_id, "date": primary_date(ed), "title": ed.get("title") or "", "body": body_of(ed)}],
                        }
                        try:
                            data = post_json(args.proxy, payload, args.timeout, args.retries, args.retry_sleep)
                        except Exception as exc:
                            print(f"      edict-match failed, saved error and continuing: {exc}")
                            data = {"matches": [], "error": str(exc)}
                        for match in data.get("matches", []):
                            pts = match.get("points") if isinstance(match.get("points"), list) else []
                            if not pts and (match.get("memorial_quote") or match.get("edict_quote") or match.get("how")):
                                pts = [{"aspect": "", "memorial_quote": match.get("memorial_quote") or "",
                                        "edict_quote": match.get("edict_quote") or "", "how": match.get("how") or ""}]
                            eid = str(match.get("edict_id") or ed_id)
                            matched_edict_ids.append(eid)
                            edict_rows.append({
                                "doc_id": did, "memDoc": did, "memTitle": doc.get("title") or "",
                                "edict_id": eid, "title": ed.get("title") or "", "date": primary_date(ed),
                                "summary": match.get("summary") or "", "points": pts,
                            })
                    write_json(files["edict-match"], edict_rows)
                    mark(did, "edict-match")

            if "info-source" in steps and not (args.skip_done and is_done(did, "info-source")):
                # the emperor's own text: this 硃批/上諭, plus each distinct matched 上諭
                targets = [doc] if doc.get("doc_type") in ("硃批", "上諭") else []
                seen = {doc_id_of(doc)}
                for eid in matched_edict_ids:
                    if eid not in seen and eid in by_id:
                        targets.append(by_id[eid])
                        seen.add(eid)
                for base in targets:
                    print(f"  - 資訊來源查詢: {doc_id_of(base)} ({base.get('doc_type')})")
                    row = run_info_source(args.proxy, args.model, records, base, args.timeout, args.retries, args.retry_sleep)
                    if row and row["items"]:
                        row.pop("candCount", None)
                        info_rows.append(row)
                        write_json(files["info-source"], info_rows)
                    elif row is not None:
                        print(f"    (no info-source items for {doc_id_of(base)})")
                mark(did, "info-source")

            # 5. 回應時效 (situ-fit) -- 硃批 only
            if "situfit" in steps and not (args.skip_done and is_done(did, "situfit")):
                print("  - 回應時效")
                sf = run_situfit(args.proxy, args.model, records, doc, args.timeout, args.retries, args.retry_sleep)
                if sf:
                    situfit_rows.append(sf)
                    write_json(files["situfit"], situfit_rows)
                else:
                    print("    (回應時效 skipped: not a 硃批 with both 上奏日 and 硃批日)")
                mark(did, "situfit")
        except Exception as exc:
            print(f"  !! {did} step failed ({exc}); skipping rest of this doc, will retry on --skip-done rerun")
            continue

    # 6. 官員回應 (official-response) -- one post-loop pass over the whole corpus,
    #    same as run_review_bundle_test.py (candidates searched across all records).
    if "official-response" in steps:
        doc_ids_in_bundle = {doc_id_of(d) for d in docs}
        actions: list[dict[str, Any]] = []
        for it in zhupi_rows:
            d_id = str(it.get("doc_id") or "")
            if d_id not in doc_ids_in_bundle:
                continue
            rec = by_id.get(d_id) or {}
            date_ar = recv_ar(rec) or send_ar(rec) or ann_ar(rec)
            addressee = [author_name(rec)] if author_name(rec) else []
            actions.append({"doc_id": d_id, "evTitle": it.get("title") or it.get("text") or "硃批",
                            "dateAr": date_ar, "quote": it.get("text") or it.get("marker") or "", "addressee": addressee})
        for it in edict_rows:
            edict_id = str(it.get("edict_id") or "")
            mem_id = str(it.get("doc_id") or it.get("memDoc") or "")
            if not edict_id or (edict_id not in doc_ids_in_bundle and mem_id not in doc_ids_in_bundle):
                continue
            edict_rec = by_id.get(edict_id) or {}
            date_ar = it.get("date") or ann_ar(edict_rec) or send_ar(edict_rec)
            addressee = list(edict_rec.get("recipients") or [])
            pts = it.get("points") or []
            if pts:
                for pt in pts:
                    actions.append({"doc_id": edict_id, "evTitle": pt.get("title") or pt.get("aspect") or it.get("title") or "上諭",
                                    "dateAr": date_ar, "quote": pt.get("edict_quote") or "", "addressee": addressee})
            else:
                actions.append({"doc_id": edict_id, "evTitle": it.get("title") or "上諭", "dateAr": date_ar, "quote": "", "addressee": addressee})

        official_rows = read_json(files["official-response"], []) if args.skip_done else []
        or_question = skill_prompt("official-response")
        print(f"- official-response ({len(actions)} 皇帝行動 candidates)")
        for j, act in enumerate(actions, 1):
            if not act["dateAr"]:
                print(f"  - {j}/{len(actions)}: {act['evTitle']} (無日期，略過)")
                continue
            cands = official_response_candidates(records, act["dateAr"], act["doc_id"], act["addressee"])
            if not cands:
                print(f"  - {j}/{len(actions)}: {act['evTitle']} (30日內找不到候選文書)")
                continue
            print(f"  - {j}/{len(actions)}: {act['evTitle']} ({len(cands)} 份候選文書)")
            payload = {
                "mode": "official_response", "model": args.model,
                "action": {"what": act["evTitle"], "whenCh": "", "dateAr": act["dateAr"], "quote": act["quote"]},
                "addressee": "、".join(act["addressee"]) if act["addressee"] else "",
                "candidates": [{"doc_id": doc_id_of(c), "title": c.get("title") or "", "date": doc_best_ar(c), "body": body_of(c)} for c in cands],
                **({"question": or_question} if or_question else {}),
            }
            try:
                data = post_json(args.proxy, payload, args.timeout, args.retries, args.retry_sleep)
            except Exception as exc:
                print(f"    official-response failed, saved error and continuing: {exc}")
                data = {"items": [], "error": str(exc)}
            official_rows.append({
                "doc_id": act["doc_id"], "evTitle": act["evTitle"],
                "addressee": data.get("addressee") or ("、".join(act["addressee"]) if act["addressee"] else ""),
                "items": data.get("items", []),
            })
            write_json(files["official-response"], official_rows)

    # finalise: merged source-chain + manifest + empty human-edits notes
    if source_raw:
        flush_source_chain()
    manifest = {
        "name": bundle_name,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "source": str(SOURCE.relative_to(ROOT)),
        "model": args.model,
        "doc_ids": wanted,
        "chain": [s for s in ALL_STEPS if s in steps],
    }
    write_json(out_root / "manifest.json", manifest)
    if not (out_root / "human-edits" / "notes.json").exists():
        (out_root / "human-edits" / "notes.json").write_text("[]\n", encoding="utf-8")

    print(f"\nWrote bundle: {out_root.relative_to(ROOT)}")
    print("Open the timeline page and click: 資料 → 載入技能輸出")


if __name__ == "__main__":
    main()
