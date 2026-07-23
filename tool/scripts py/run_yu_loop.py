#!/usr/bin/env python3
"""Run the 上諭-first (emperor-document) review loop.

This is the 上諭 sibling of run_mass_prompt_chain_test.py (the official-document
loop). Where the official loop reads a 奏摺／硃批 and reconstructs what happened
on the battlefield, this loop reads a 上諭 and reconstructs what the EMPEROR
KNEW and DID, using only the existing yu-source / official-reply pair network:

  summary -> division
  -> 林方 + 清方 events the emperor states he KNOWS (3-in-1), each traced to the
     source memorial(s) that reported it (via the yu_source network, not a full
     local->military->official relay chain)
  -> the emperor's own actions (comments + commands) stated in the 上諭
  -> later official responses to those commands (via the official_reply_to_yu
     network; no fresh corpus search)
  -> repeat-report dedup: label any 林/清/皇帝/回應 output that duplicates an
     already-committed dot (the source memorials are usually reviewed BEFORE the
     上諭), so the reviewer can merge it into the existing dot or keep it separate.

There is deliberately no 回應時效 (timeliness) stage yet.

Shared low-level helpers are imported from run_review_bundle_test and from the
official loop (run_mass_prompt_chain_test); this file adds only the 上諭-specific
orchestration, so the official loop is left untouched.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
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
    primary_date,
    print_cost_summary,
    read_json,
    skill_prompt,
    write_json,
)
from run_mass_prompt_chain_test import (  # noqa: E402
    FORMAL_STATE_PATH,
    accounting_step,
    author_name,
    body_of,
    doc_id_of,
    imperial_date,
    load_existing_pairs,
    pair_evidence,
    pair_reply_doc_id,
    pair_yu_doc_id,
    parse_date,
    post_json,
    record_date,
    run_division,
    run_summary,
    split_csv,
    verified_quote,
)

DEFAULT_DOC_IDS = "諭13,諭20"
DEFAULT_MODEL = "gemini-3.5-flash"

LOOP_CHAIN = [
    "summary",
    "divide",
    "yu-reported-events (lin+qing+source)",
    "yu-emperor-actions",
    "official-response",
    "repeat-report",
]


# ---- 上諭 pair-network helpers (keyed on the 上諭, not the memorial) ----------
def source_memorials_for_yu(pairs: list[dict[str, Any]], yu_id: str) -> list[str]:
    """Memorials the emperor drew this 上諭 from (yu_source network)."""
    out: list[str] = []
    for pair in pairs:
        if str(pair.get("relation") or "") != "yu_source":
            continue
        if pair_yu_doc_id(pair) != yu_id:
            continue
        rid = pair_reply_doc_id(pair)
        if rid and rid not in out:
            out.append(rid)
    return out


def responders_for_yu(pairs: list[dict[str, Any]], yu_id: str) -> list[str]:
    """Later memorials that respond to this 上諭 (official_reply_to_yu network)."""
    out: list[str] = []
    for pair in pairs:
        if str(pair.get("relation") or "") != "official_reply_to_yu":
            continue
        if pair_yu_doc_id(pair) != yu_id:
            continue
        rid = pair_reply_doc_id(pair)
        if rid and rid not in out:
            out.append(rid)
    return out


def yu_date(record: dict[str, Any]) -> str:
    return date_pair_value(record, "announce_date") or date_pair_value(record, "send_date") or imperial_date(record) or primary_date(record)


def candidate_payload(rec: dict[str, Any]) -> dict[str, Any]:
    return {
        "doc_id": doc_id_of(rec),
        "official": author_name(rec),
        "send_date": date_pair_value(rec, "send_date"),
        "receive_date": date_pair_value(rec, "receive_date") or date_pair_value(rec, "announce_date"),
        "body": body_of(rec) + ("\n" + (rec.get("rescript_text") or rec.get("rescript") or "") if (rec.get("rescript_text") or rec.get("rescript")) else ""),
    }


# ---- proxy calls -------------------------------------------------------------
def run_reported_events(proxy, model, doc, source_recs, timeout, retries, retry_sleep):
    payload = {
        "mode": "yu_reported_events",
        "model": model,
        "actor": "all",
        "edict": {"id": doc_id_of(doc), "date": yu_date(doc), "title": doc.get("title") or "", "body": body_of(doc)},
        "candidates": [candidate_payload(r) for r in source_recs],
        "question": skill_prompt("yu-reported-events"),
    }
    with accounting_step("yu-reported-events"):
        data = post_json(proxy, payload, timeout, retries, retry_sleep)
    events = data.get("events", []) if isinstance(data.get("events"), list) else []
    lin, qing = [], []
    for raw in events:
        if not isinstance(raw, dict):
            continue
        side = str(raw.get("side") or "").lower()
        raw.setdefault("doc_id", doc_id_of(doc))
        # keep only source docs actually supplied by the yu_source network
        allowed = {doc_id_of(r) for r in source_recs}
        raw["source_documents"] = [s for s in (raw.get("source_documents") or []) if isinstance(s, dict) and str(s.get("source_doc_id") or "") in allowed]
        # Populate the standard `sources` the event card renders: the 上諭 line the
        # emperor states it in, then each source memorial (the official doc that
        # reported it to the emperor) with its own quote + relation.
        _REL = {"direct": "官員親報", "corroborating": "他報佐證", "relay": "轉述"}
        srcs = []
        if raw.get("edict_quote"):
            srcs.append({"doc_id": doc_id_of(doc), "quote": raw.get("edict_quote"), "howKnown": "上諭所載"})
        for sd in raw["source_documents"]:
            sq = sd.get("source_quote") or ""
            if not sq:
                continue
            srcs.append({
                "doc_id": sd.get("source_doc_id"), "quote": sq,
                "howKnown": _REL.get(str(sd.get("relation") or ""), sd.get("relation") or "來源"),
                "whenKnown": sd.get("source_receive_date") or sd.get("source_send_date") or "",
            })
        raw["sources"] = srcs
        if side == "lin":
            lin.append(raw)
        else:
            raw["category"] = str(raw.get("category") or "done")
            if raw["category"] not in {"done", "plan", "nonmil"}:
                raw["category"] = "done"
            qing.append(raw)
    return lin, qing


def run_emperor_actions(proxy, model, doc, timeout, retries, retry_sleep):
    """Return ONE combined-emperor row in the exact shape the website already
    renders (combinedEmperor + items[].points[]), so yu emperor actions show as
    their own 皇帝行動 cards. Returns None when nothing verifiable was found."""
    yu_id, title, date, src = doc_id_of(doc), (doc.get("title") or ""), yu_date(doc), body_of(doc)
    payload = {
        "mode": "yu_emperor_actions",
        "model": model,
        "edict": {"id": yu_id, "date": date, "title": title, "body": src},
        "question": skill_prompt("yu-emperor-actions"),
    }
    with accounting_step("yu-emperor-actions"):
        data = post_json(proxy, payload, timeout, retries, retry_sleep)
    points = []
    for raw in (data.get("actions", []) if isinstance(data.get("actions"), list) else []):
        if not isinstance(raw, dict):
            continue
        quote = verified_quote(src, raw.get("quote") or "")
        if not quote:
            continue
        desc = str(raw.get("description") or "")
        atype = raw.get("action_type") or "comment"
        points.append({
            "title": str(raw.get("title") or "皇帝行動"),
            "aspect": atype, "action_type": atype, "how": desc, "description": desc,
            "whenCh": raw.get("whenCh") or "", "whenAr": raw.get("whenAr") or "", "where": raw.get("where") or "",
            "who": raw.get("who") if isinstance(raw.get("who"), list) else [],
            "whoLoc": raw.get("who_loc") or raw.get("whoLoc") or {},
            "relations": raw.get("relations") if isinstance(raw.get("relations"), list) else [],
            "same_as_event_id": "",
            "target": raw.get("target") if isinstance(raw.get("target"), list) else [],
            "quote": quote,
            "sources": [{"doc_id": yu_id, "source_type": "上諭", "quote": quote, "title": title, "date": date}],
        })
    if not points:
        return None
    return {
        "doc_id": yu_id, "memDoc": yu_id, "memTitle": title, "combinedEmperor": True, "marker": "上諭皇帝行動",
        "items": [{
            "edict_id": yu_id, "title": title or "上諭", "date": date, "memDoc": yu_id, "memTitle": title,
            "summary": "上諭中皇帝自己的評論與命令。", "points": points,
        }],
    }


def run_official_responses(proxy, model, doc, actions, pairs, by_id, timeout, retries, retry_sleep):
    yu_id = doc_id_of(doc)
    reply_ids = responders_for_yu(pairs, yu_id)
    candidates = [by_id[r] for r in reply_ids if r in by_id]
    rows = []
    if not candidates:
        return rows
    cand_payload = [{"doc_id": doc_id_of(c), "title": c.get("title") or "", "date": doc_best_ar(c), "body": body_of(c)} for c in candidates]
    valid_ids = {doc_id_of(c) for c in candidates}
    for act in actions:
        if str(act.get("action_type") or "") not in {"command", "approve", "reject", "blame", "praise"}:
            continue  # only actionable commands/judgements draw a later response
        payload = {
            "mode": "official_response",
            "model": model,
            "confirmed_pairs_only": True,
            "action": {"what": act.get("title") or "皇帝行動", "dateAr": act.get("whenAr") or yu_date(doc), "quote": act.get("quote") or ""},
            "addressee": "、".join(act.get("target") or []),
            "candidates": cand_payload,
            "question": skill_prompt("official-response"),
        }
        try:
            with accounting_step("official-response"):
                data = post_json(proxy, payload, timeout, retries, retry_sleep)
        except Exception as exc:
            print(f"    official-response failed for 「{act.get('title')}」: {exc}")
            data = {}
        items = [it for it in (data.get("items", []) if isinstance(data.get("items"), list) else [])
                 if isinstance(it, dict) and str(it.get("doc_id") or "") in valid_ids and it.get("is_response", True)]
        rows.append({
            "doc_id": yu_id, "yu_doc_id": yu_id, "evTitle": act.get("title") or "皇帝行動",
            "addressee": data.get("addressee") or "、".join(act.get("target") or []),
            "items": items, "confirmedPairsOnly": True, "noConfirmedPairs": not bool(candidates),
        })
    return rows


# ---- repeat-report dedup (re-added; parallel) --------------------------------
_COMMITTED: dict[str, list[dict[str, Any]]] = {}
_FORMAL: dict | None = None


def _formal_state() -> dict:
    global _FORMAL
    if _FORMAL is None:
        st = read_json(FORMAL_STATE_PATH, {})
        _FORMAL = st if isinstance(st, dict) else {}
    return _FORMAL


def _rec_date(did: str, by_id) -> str:
    rec = by_id.get(str(did), {})
    return date_pair_value(rec, "send_date") or record_date(rec)


def committed_cards(actor: str, by_id) -> list[dict[str, Any]]:
    if actor in _COMMITTED:
        return _COMMITTED[actor]
    events = _formal_state().get("__events", [])
    out = []
    for e in events if isinstance(events, list) else []:
        if not isinstance(e, dict):
            continue
        raw = str(e.get("actor") or "").lower()
        act = "emperor" if raw in {"emperor", "皇帝"} else raw
        if act != actor:
            continue
        eid = str(e.get("id") or "")
        if not eid:
            continue
        srcs = e.get("sources") or []
        did = ""
        for s in srcs:
            if isinstance(s, dict) and s.get("doc_id"):
                did = str(s["doc_id"]); break
            if isinstance(s, str):
                did = s; break
        quote = (srcs[0].get("quote") if srcs and isinstance(srcs[0], dict) else "") or ""
        out.append({"id": eid, "title": e.get("subtitle") or e.get("what") or "", "description": e.get("description") or "",
                    "quote": quote, "doc_id": did, "date": _rec_date(did, by_id)})
    _COMMITTED[actor] = out
    return out


def _bigrams(t: str) -> set:
    t = re.sub(r"\s+", "", str(t or ""))
    return {t[i:i + 2] for i in range(len(t) - 1)}


def _overlap(a: str, b: str) -> float:
    A, B = _bigrams(a), _bigrams(b)
    return len(A & B) / len(A | B) if A and B else 0.0


def _vtext(v) -> str:
    return "\n".join((v.get("title") or "", v.get("description") or "", v.get("quote") or ""))


def dedup(proxy, model, actor, cards, by_id, timeout, retries, retry_sleep, top_k=10, min_overlap=0.12, workers=6) -> int:
    """Label each yu card that repeats an already-committed dot (or another yu card
    this run) with same_as + earliest_report, for the reviewer to merge or keep."""
    views = []
    for i, card in enumerate(cards):
        did = str(card.get("doc_id") or "")
        cid = card.setdefault("card_id", f"{did}#{actor}#{i}")
        srcs = card.get("sources") or []
        quote = card.get("quote") or card.get("edict_quote") or ((srcs[0].get("quote") if srcs and isinstance(srcs[0], dict) else "") or "")
        views.append({"id": cid, "title": card.get("subtitle") or card.get("title") or "", "description": card.get("description") or "",
                      "quote": quote, "doc_id": did, "date": _rec_date(did, by_id), "_orig": card})
    if not views:
        return 0
    pool = committed_cards(actor, by_id) + [{k: v[k] for k in ("id", "title", "description", "quote", "doc_id", "date")} for v in views]
    jobs = []
    for v in views:
        text = _vtext(v)
        scored = [(c, _overlap(text, _vtext(c))) for c in pool if c.get("id") != v.get("id")]
        shortlist = [c for c, s in sorted(scored, key=lambda x: x[1], reverse=True) if s >= min_overlap][:top_k]
        if shortlist:
            jobs.append((v, shortlist))

    def _trim(x):
        return {"id": x.get("id", ""), "title": (x.get("title") or "")[:60], "description": (x.get("description") or "")[:120],
                "quote": (x.get("quote") or "")[:48], "doc_id": x.get("doc_id", ""), "date": x.get("date", "")}

    def _call(job):
        v, shortlist = job
        payload = {"mode": "repeat_report", "model": model, "actor": actor, "card": _trim(v),
                   "candidates": [_trim(c) for c in shortlist], "question": skill_prompt("repeat-report")}
        try:
            data = post_json(proxy, payload, timeout, retries, retry_sleep)
        except Exception as exc:
            print(f"    repeat-report failed for {v.get('title') or '(untitled)'}: {exc}")
            data = {}
        allowed = {c["id"] for c in shortlist}
        return v["id"], [str(i) for i in (data.get("same_ids") or []) if str(i) in allowed]

    same_by_id = {}
    if jobs:
        with accounting_step("repeat-report"):
            if workers > 1 and len(jobs) > 1:
                from concurrent.futures import ThreadPoolExecutor
                with ThreadPoolExecutor(max_workers=min(workers, len(jobs))) as ex:
                    for vid, sids in ex.map(_call, jobs):
                        same_by_id[vid] = sids
            else:
                for job in jobs:
                    vid, sids = _call(job)
                    same_by_id[vid] = sids

    def _rank(v):
        cid = str(v.get("id") or "")
        tail = cid.rsplit("#", 1)[-1]
        idx = int(tail) if tail.isdigit() else 0
        return (parse_date(v.get("date") or "") or datetime.max.date(), cid.rsplit("#", 1)[0], idx)

    pool_by_id = {c["id"]: c for c in pool}
    views.sort(key=_rank)
    roots, annotated = {}, 0
    for v in views:
        sids = same_by_id.get(v["id"]) or []
        if not sids:
            continue
        matched = [pool_by_id[i] for i in sids if i in pool_by_id]
        resolved = [roots.get(c["id"], c) for c in matched]
        earliest = min(resolved + [pool_by_id[v["id"]]], key=_rank)
        if earliest.get("id") != v.get("id"):
            orig = v["_orig"]
            orig["same_as"] = earliest["id"]
            orig["earliest_report"] = {k: earliest.get(k, "") for k in ("id", "doc_id", "date", "title")}
            orig["repeat_candidates"] = sids
            roots[v["id"]] = earliest
            annotated += 1
    return annotated


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--proxy", default=os.environ.get("GEMINI_PROXY_URL", ""))
    ap.add_argument("--model", default=os.environ.get("GEMINI_MODEL", DEFAULT_MODEL))
    ap.add_argument("--doc-ids", default=DEFAULT_DOC_IDS, help="Comma-separated 上諭 doc ids")
    ap.add_argument("--bundle", default="", help="Short semantic review-bundle name")
    ap.add_argument("--timeout", type=int, default=240)
    ap.add_argument("--retries", type=int, default=4)
    ap.add_argument("--retry-sleep", type=int, default=15)
    ap.add_argument("--skip-done", action="store_true")
    ap.add_argument("--no-dedup", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--input-price-per-million", type=float, default=None)
    ap.add_argument("--output-price-per-million", type=float, default=None)
    args = ap.parse_args()

    records = json.loads(SOURCE.read_text(encoding="utf-8"))
    by_id = {doc_id_of(r): r for r in records}
    wanted = split_csv(args.doc_ids)
    missing = [d for d in wanted if d not in by_id]
    if missing:
        raise SystemExit("Missing doc_id(s): " + ", ".join(missing))
    docs = [by_id[d] for d in wanted]
    non_yu = [doc_id_of(d) for d in docs if d.get("doc_type") != "上諭"]
    if non_yu:
        print(f"warning: these are not 上諭 and will still be treated as edicts: {', '.join(non_yu)}")
    pairs = load_existing_pairs()

    bundle_name = args.bundle or f"yu-review-{wanted[0]}-plus{len(wanted) - 1}-{hashlib.sha1('-'.join(wanted).encode()).hexdigest()[:8]}"
    out_root = BUNDLES_DIR / bundle_name
    out_dir = out_root / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_root / "human-edits").mkdir(parents=True, exist_ok=True)

    if args.dry_run:
        print(f"DRY RUN -- bundle: {out_root.relative_to(ROOT)}\nmodel: {args.model}\nexisting pair rows: {len(pairs)}")
        for doc in docs:
            did = doc_id_of(doc)
            print(f"\n[{did}] {doc.get('doc_type')} {doc.get('title')}  date={yu_date(doc)!r}")
            print(f"  yu_source memorials: {source_memorials_for_yu(pairs, did) or 'none'}")
            print(f"  official_reply_to_yu responders: {responders_for_yu(pairs, did) or 'none'}")
        print("\n(no proxy calls made)")
        return
    if not args.proxy:
        raise SystemExit("Set GEMINI_PROXY_URL or pass --proxy (or use --dry-run).")

    files = {
        "summary": out_dir / "summary.json",
        "divide": out_dir / "division-parts.json",
        "lin": out_dir / "lin-events.json",
        "qing": out_dir / "qing-actions-all.json",
        "emperor": out_dir / "combined-emperor-actions.json",
        "official": out_dir / "official-response.json",
    }
    status_path = out_dir / "_run-status.json"
    status = read_json(status_path, {}) if args.skip_done else {}

    def done(did, step):
        return bool(args.skip_done and status.get(did, {}).get(step))

    def mark(did, step):
        status.setdefault(did, {})[step] = True
        write_json(status_path, status)

    summaries = read_json(files["summary"], []) if args.skip_done else []
    divisions = read_json(files["divide"], []) if args.skip_done else []
    lin_rows = read_json(files["lin"], []) if args.skip_done else []
    qing_rows = read_json(files["qing"], []) if args.skip_done else []
    emperor_rows = read_json(files["emperor"], []) if args.skip_done else []
    official_rows = read_json(files["official"], []) if args.skip_done else []

    for index, doc in enumerate(docs, 1):
        did = doc_id_of(doc)
        print(f"[{index}/{len(docs)}] {did} {doc.get('doc_type')} {doc.get('title')}")
        try:
            if not done(did, "summary"):
                print("  - summary")
                summaries.append(run_summary(args.proxy, args.model, doc, args.timeout, args.retries, args.retry_sleep))
                write_json(files["summary"], summaries); mark(did, "summary")
            if not done(did, "divide"):
                print("  - divide")
                divisions.append(run_division(args.proxy, args.model, doc, args.timeout, args.retries, args.retry_sleep))
                write_json(files["divide"], divisions); mark(did, "divide")

            if not done(did, "yu-reported-events"):
                source_recs = [by_id[m] for m in source_memorials_for_yu(pairs, did) if m in by_id]
                print(f"  - 林/清 events the emperor knows + source trace ({len(source_recs)} yu_source memorial(s))")
                lin_items, qing_items = run_reported_events(args.proxy, args.model, doc, source_recs, args.timeout, args.retries, args.retry_sleep)
                lin_rows.extend(lin_items); qing_rows.extend(qing_items)
                write_json(files["lin"], lin_rows); write_json(files["qing"], qing_rows)
                mark(did, "yu-reported-events")

            if not done(did, "yu-emperor-actions"):
                print("  - 皇帝行動（評論／命令）")
                row = run_emperor_actions(args.proxy, args.model, doc, args.timeout, args.retries, args.retry_sleep)
                if row:
                    emperor_rows.append(row)
                write_json(files["emperor"], emperor_rows); mark(did, "yu-emperor-actions")

            if not done(did, "official-response"):
                doc_acts = [p for r in emperor_rows if str(r.get("doc_id") or "") == did
                            for item in (r.get("items") or []) for p in (item.get("points") or [])]
                print(f"  - 官員回應（既有配對，{len(responders_for_yu(pairs, did))} responder(s)）")
                official_rows.extend(run_official_responses(args.proxy, args.model, doc, doc_acts, pairs, by_id, args.timeout, args.retries, args.retry_sleep))
                write_json(files["official"], official_rows); mark(did, "official-response")
        except Exception as exc:
            print(f"  !! {did} failed ({exc}); rerun with --skip-done to continue")
            continue

    if not args.no_dedup and not done("__global__", "repeat-report"):
        print("- repeat-report dedup vs existing dots (annotate only)")
        emp_points = [p for r in emperor_rows for item in (r.get("items") or []) for p in (item.get("points") or [])]
        resp_points = [{"doc_id": r.get("doc_id"), "title": r.get("evTitle"), "description": "", "sources": [], **({"quote": (r.get("items") or [{}])[0].get("action_quote", "")} if r.get("items") else {})} for r in official_rows]
        n_lin = dedup(args.proxy, args.model, "lin", lin_rows, by_id, args.timeout, args.retries, args.retry_sleep)
        n_qing = dedup(args.proxy, args.model, "qing", qing_rows, by_id, args.timeout, args.retries, args.retry_sleep)
        n_emp = dedup(args.proxy, args.model, "emperor", emp_points, by_id, args.timeout, args.retries, args.retry_sleep)
        n_resp = dedup(args.proxy, args.model, "qing", resp_points, by_id, args.timeout, args.retries, args.retry_sleep)
        write_json(files["lin"], lin_rows); write_json(files["qing"], qing_rows)
        write_json(files["emperor"], emperor_rows); write_json(files["official"], official_rows)
        print(f"    repeats flagged -- 林 {n_lin}, 清 {n_qing}, 皇帝 {n_emp}, 回應 {n_resp}")
        mark("__global__", "repeat-report")

    manifest = {
        "name": bundle_name,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "source": str(SOURCE.relative_to(ROOT)),
        "model": args.model,
        "doc_ids": wanted,
        "kind": "yu_first_loop",
        "chain": LOOP_CHAIN,
        "networks": ["yu_source (source trace)", "official_reply_to_yu (later responses)"],
        "deduplication": "repeat_report annotates same_as/earliest_report on 林/清/皇帝/回應 vs committed dots; website offers merge/keep",
        "excluded_stages": ["回應時效 / timeliness", "date-window corpus search"],
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
