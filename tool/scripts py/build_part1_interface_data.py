#!/usr/bin/env python3
"""Build the Part 1 interface-replica demonstration data module.

The introduction website's 第一部分「平台的整體介面」shows an interactive replica of
the sample review tool. The replica must not invent any historical content, so this
script derives every quotation, date, title and AI result from existing project data:

  - review-tools/shared data/stage1_original_text.json   (canonical 硃42 record)
  - review-tools/(2) sample/sample_all.data              (current sample review state)

Output:
  intro Website/Website/storymap/part-1-interface-data.js

The generated file is a plain hand-editable JS module assigned to
window.PART1_INTERFACE_DATA. It is loaded with a normal <script src> tag so the
introduction website keeps working when opened directly from disk. After
generating it you may edit the file by hand; re-running this script overwrites it.

Usage:
    cd "/Users/creamybanana/Downloads/DH Project"
    python3 "tool/scripts py/build_part1_interface_data.py"
"""

from __future__ import annotations

import calendar
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STAGE1 = ROOT / "review-tools" / "shared data" / "stage1_original_text.json"
SAMPLE_STATE = ROOT / "review-tools" / "(2) sample" / "sample_all.data"
CONFIRMED_PAIRS = ROOT / "review-tools" / "(2) sample" / "confirmed-pairs.json"
YU_SOURCE = ROOT / "review-tools" / "(2) sample" / "yu-source.json"
OUT = ROOT / "intro Website" / "Website" / "storymap" / "part-1-interface-data.js"

DOC_ID = "硃42"

# Event subtitles selected from the current sample state. Each one is already a
# human-confirmed dot in the sample tool, so the replica shows real review output.
DOT_EVENT = "賊匪於三坎店交戰稍退"          # 第一線 戰場事件
DOT_EMPEROR = (
    "據柴大紀於三坎店大施火砲擊退賊眾之報研判臺灣郡城防守嚴密且全臺尚無他虞"
)                                          # 第四線 皇帝行動

# AI candidate cards offered for the 「加入」 demonstration in the AI 分析區.
AI_CANDIDATES = [
    "澎湖兵渡海前往臺灣赴援",
    "黃仕簡率兵由廈門放洋",
]


def fail(message: str) -> None:
    raise SystemExit(f"build_part1_interface_data: {message}")


def load_documents() -> list[dict]:
    return json.loads(STAGE1.read_text(encoding="utf-8"))


def load_document(records: list[dict]) -> dict:
    for record in records:
        if record.get("doc_id") == DOC_ID:
            return record
    fail(f"{DOC_ID} not found in {STAGE1}")


def state_path_from_args() -> Path:
    path = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else SAMPLE_STATE
    if not path.is_file():
        fail(f"sample state not found: {path}")
    return path


def load_state(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_events(state: dict) -> list:
    return state.get("__events", [])


def date_parts(value) -> tuple[str, str]:
    """Read the source JSON's [Traditional Chinese, Arabic] date pair."""
    if isinstance(value, list):
        chinese = value[0] if len(value) > 0 else ""
        arabic = value[1] if len(value) > 1 else ""
        return str(chinese or ""), str(arabic or "")
    if isinstance(value, dict):
        return str(value.get("chinese") or value.get("ch") or ""), str(value.get("arabic") or value.get("ar") or "")
    return "", ""


def parse_ar(value: str) -> date | None:
    try:
        year, month, day = (int(part) for part in str(value or "").replace("-", "/").split("/")[:3])
        return date(year, month, day)
    except (ValueError, TypeError):
        return None


def normalise_ar(value: str) -> str:
    parsed = parse_ar(value)
    return parsed.strftime("%Y/%m/%d") if parsed else ""


def doc_type_key(doc_type: str) -> str:
    return {"上奏": "shangzou", "硃批": "zhupi", "上諭": "shangyu"}.get(doc_type, "")


def document_chart_payload(doc: dict) -> dict:
    """Keep the dated document metadata needed by the replica's dot/panel UI."""
    author = doc.get("author") or {}
    send_ch, send_ar = date_parts(doc.get("send_date"))
    recv_ch, recv_ar = date_parts(doc.get("receive_date"))
    ann_ch, ann_ar = date_parts(doc.get("announce_date"))
    return {
        "docId": doc.get("doc_id"),
        "docType": doc.get("doc_type"),
        "type": doc_type_key(doc.get("doc_type")),
        "title": doc.get("title") or "",
        "author": author,
        "authorName": author.get("name") or "",
        "authorPosition": author.get("position") or "",
        "sendCh": send_ch or None,
        "sendAr": normalise_ar(send_ar) or None,
        "recvCh": recv_ch or None,
        "recvAr": normalise_ar(recv_ar) or None,
        "annCh": ann_ch or None,
        "annAr": normalise_ar(ann_ar) or None,
        "rescriptText": doc.get("rescript_text") or "",
    }


def document_panel_payload(doc: dict) -> dict:
    """Keep the source record needed to open any chart document in the panel."""
    return {
        "docId": doc.get("doc_id"),
        "docType": doc.get("doc_type"),
        "title": doc.get("title") or "",
        "author": doc.get("author") or {},
        "series": doc.get("series") or "",
        "compiledIn": doc.get("compiled_in") or {},
        "sendDate": doc.get("send_date"),
        "receiveDate": doc.get("receive_date"),
        "issueDate": doc.get("issue_date"),
        "announceDate": doc.get("announce_date"),
        "subtype": doc.get("subtype"),
        "archiveReference": doc.get("archive_reference"),
        "body": doc.get("body") or "",
        "rescriptText": doc.get("rescript_text") or "",
    }


def find_event(events: list, subtitle: str) -> dict:
    for event in events:
        if event.get("subtitle") == subtitle:
            return event
    fail(f"event not found in sample state: {subtitle}")


def primary_source(event: dict) -> dict:
    sources = event.get("sources") or []
    if not sources:
        fail(f"event has no sources: {event.get('subtitle')}")
    return sources[0]


def event_payload(event: dict) -> dict:
    """Reduce a sample-state event to the fields the replica panel and graph use."""
    source = primary_source(event)
    return {
        "id": event.get("id"),
        "actor": event.get("actor"),
        "subtitle": event.get("subtitle"),
        "what": event.get("what"),
        "description": event.get("description"),
        "where": event.get("where"),
        "who": event.get("who") or [],
        "whoLoc": event.get("whoLoc") or {},
        "relations": event.get("relations") or [],
        "provenance": event.get("provenance") or [],
        "whenCh": event.get("whenCh"),
        "dateAr": normalise_ar(event.get("dateAr")),
        "sources": event.get("sources") or [],
        "hidden": bool(event.get("hidden")),
        "category": event.get("category"),
        "aiFilterLabel": event.get("aiFilterLabel"),
        "groupedFrom": event.get("groupedFrom") or [],
        "respondsToEventId": event.get("respondsToEventId"),
        "alsoRespondsToEventIds": event.get("alsoRespondsToEventIds") or [],
        "emperorDetail": event.get("emperorDetail"),
        "quote": source.get("quote"),
        "quoteDocId": source.get("doc_id"),
    }


def chat_item_payload(item: dict, source_doc_id: str, event_ids: list[str], kind: str) -> dict:
    """Keep the source-backed fields needed to show one saved AI output item."""
    # Keep the review tool's output fields intact so the replica can select the
    # same card type (extract, official response, pair, trace, or emperor
    # action) instead of flattening every result into a generic card.
    payload = {key: value for key, value in item.items() if not key.startswith("__") or key in {"__evId", "__added", "__committed"}}
    title = item.get("subtitle") or item.get("title") or item.get("summary") or "未命名輸出"
    quote = item.get("quote")
    if not quote and item.get("sources"):
        quote = (item.get("sources") or [{}])[0].get("quote")
    payload.update({
        "kind": kind,
        "title": title,
        "description": item.get("description") or item.get("how") or item.get("summary"),
        "where": item.get("where"),
        "who": item.get("who") or [],
        "whenCh": item.get("whenCh"),
        "whenAr": item.get("whenAr") or item.get("date") or item.get("response_date"),
        "quote": quote,
        "sourceDocId": source_doc_id,
        "eventIds": event_ids,
        "responseDocId": item.get("doc_id"),
    })
    if item.get("__traceChains") and not payload.get("chains"):
        payload["chains"] = item.get("__traceChains")
    return payload


def chat_source_projection(state: dict, doc_id: str) -> dict:
    """Project the saved .chat history without copying unrelated review state."""
    doc_state = state.get(doc_id) or {}
    clear_demo = state.get("__clearDemo") or {}
    selected = ((clear_demo.get("event_dots") or {}).get("selected_data") or {}).get(doc_id) or {}
    selected_event_ids = selected.get("event_ids") or []
    event_by_id = {event.get("id"): event for event in state.get("__events", [])}

    event_quotes = {}
    for event_id, event in event_by_id.items():
        quotes = [
            source.get("quote") or ""
            for source in event.get("sources") or []
            if str(source.get("doc_id") or source.get("docId") or "") == str(doc_id)
        ]
        if quotes:
            event_quotes[event_id] = quotes

    def matching_event_ids(item: dict) -> list[str]:
        item_quote = item.get("quote") or ""
        matches = [
            event_id for event_id, quotes in event_quotes.items()
            if item_quote and any(item_quote == quote or item_quote in quote or quote in item_quote for quote in quotes)
        ]
        return list(dict.fromkeys([*selected_event_ids, *matches])) if item.get("__evId") in selected_event_ids else matches

    turns = []
    output_item_count = 0
    for turn_index, turn in enumerate(doc_state.get("chat") or []):
        output_items = []
        turn_kind = turn.get("kind") or "output"
        for item_index, item in enumerate(turn.get("items") or []):
            if turn.get("kind") == "edictmatch" and item.get("points"):
                for point_index, point in enumerate(item.get("points") or []):
                    event_ids = matching_event_ids(point)
                    output_items.append({
                        **chat_item_payload(point, doc_id, event_ids, "emperor_action"),
                        "itemIndex": item_index,
                        "pointIndex": point_index,
                    })
            else:
                output_items.append({
                    **chat_item_payload(item, doc_id, matching_event_ids(item), turn_kind),
                    "itemIndex": item_index,
                })

        # Saved document-pair turns keep their result in `turn.pair` rather
        # than in `turn.items`; preserve it as the pair card's item.
        if not output_items and turn.get("pair"):
            pair_item = {
                "pair": turn.get("pair"),
                "subtitle": turn.get("subtitle"),
                "description": turn.get("description"),
                "where": turn.get("where"),
                "whenCh": turn.get("whenCh"),
                "whenAr": turn.get("whenAr"),
            }
            output_items.append({
                **chat_item_payload(pair_item, doc_id, [], "docpair"),
                "itemIndex": 0,
            })

        # A few saved turns store one result directly on the turn (rather than
        # under `items`). Keep meaningful turn-level output, but skip command
        # configuration responses that have no visible card content.
        if not output_items and any(turn.get(key) for key in ("subtitle", "title", "description", "quote", "sources")):
            output_items.append({
                **chat_item_payload(turn, doc_id, matching_event_ids(turn), turn_kind),
                "itemIndex": 0,
            })

        if not output_items:
            continue
        output_item_count += len(output_items)
        turns.append({
            "turnIndex": turn_index,
            "kind": turn.get("kind"),
            "bundleName": turn.get("__skillBundleName"),
            "runId": turn.get("__skillRunId"),
            "model": turn.get("model"),
            "prompt": turn.get("prompt"),
            "outputItems": output_items,
        })

    return {
        "docId": doc_id,
        "role": selected.get("role"),
        "aiOutputPath": selected.get("ai_output_path") or f"{doc_id}.chat",
        "eventIds": selected_event_ids,
        "turnCount": len(turns),
        "outputItemCount": output_item_count,
        "turns": turns,
    }


def check_quote(body: str, quote: str, label: str) -> None:
    """The replica highlights quotations inside the original text, so every quote
    must be a literal substring of the canonical body."""
    if quote not in body:
        fail(f"quote for {label!r} is not a literal substring of {DOC_ID} body")


def build_chart_preview(documents: list[dict], events: list[dict]) -> dict:
    """Build the sample chart's dated dot projection from source-backed records.

    The sample does not draw one generic dot per document. It draws a document's
    actual dated endpoint(s): 上奏 on the official line, 硃批 at send and receive
    when both dates exist, and 上諭 on the imperial-document line. Events are
    separate squares on the outer event/emperor lines.
    """
    chart_docs = [doc for doc in documents if doc_type_key(doc.get("doc_type"))]
    doc_by_id = {str(doc.get("doc_id")): doc for doc in chart_docs}
    document_nodes: list[dict] = []
    node_by_doc_side: dict[tuple[str, str], dict] = {}
    placement_dates: list[date] = []
    type_colors = {"shangzou": "#2f75b5", "zhupi": "#c46a2b", "shangyu": "#7d4ab8"}

    def add_document_node(doc: dict, side: str, lane: str, date_ch: str, date_ar: str) -> None:
        parsed = parse_ar(date_ar)
        if not parsed:
            return
        type_key = doc_type_key(doc.get("doc_type"))
        payload = document_chart_payload(doc)
        payload["dateAr"] = parsed.strftime("%Y/%m/%d")
        payload["whenCh"] = date_ch or payload.get("sendCh") or payload.get("recvCh") or payload.get("annCh") or payload["dateAr"]
        node = {
            "id": f"doc-{doc.get('doc_id')}-{side}",
            "kind": "document",
            "recordType": type_key,
            "lane": lane,
            "side": side,
            "actor": "official" if lane == "official" else "imperial",
            "dateAr": payload["dateAr"],
            "label": payload["whenCh"],
            "color": type_colors[type_key],
            "radius": 5.4,
            "payload": payload,
        }
        document_nodes.append(node)
        node_by_doc_side[(str(doc.get("doc_id")), side)] = node
        placement_dates.append(parsed)

    for doc in chart_docs:
        type_key = doc_type_key(doc.get("doc_type"))
        send_ch, send_ar = date_parts(doc.get("send_date"))
        recv_ch, recv_ar = date_parts(doc.get("receive_date"))
        ann_ch, ann_ar = date_parts(doc.get("announce_date"))
        if type_key == "shangzou":
            add_document_node(doc, "L", "official", send_ch, send_ar)
        elif type_key == "zhupi":
            add_document_node(doc, "L", "official", send_ch, send_ar)
            add_document_node(doc, "R", "imperial", recv_ch, recv_ar)
        elif type_key == "shangyu":
            add_document_node(doc, "R", "imperial", ann_ch, ann_ar)

    event_nodes: list[dict] = []
    event_colors = {"lin": "#b5462e", "qing": "#3f6f8f", "emperor": "#7d4ab8"}
    for event in events:
        if event.get("hidden"):
            continue
        payload = event_payload(event)
        parsed = parse_ar(payload.get("dateAr"))
        if not parsed:
            continue
        actor = payload.get("actor") or "lin"
        lane = "emperor" if actor == "emperor" else "events"
        side = "R" if lane == "emperor" else "L"
        event_nodes.append({
            "id": f"event-{payload.get('id')}",
            "kind": "event",
            "recordType": "event",
            "lane": lane,
            "side": side,
            "actor": actor,
            "dateAr": payload["dateAr"],
            "label": payload.get("whenCh") or payload["dateAr"],
            "color": event_colors.get(actor, "#8a765a"),
            "radius": 5.2,
            "shape": "square",
            "payload": payload,
        })
        placement_dates.append(parsed)

    links: list[dict] = []
    link_keys: set[tuple[str, str, str]] = set()

    def add_link(from_id: str | None, to_id: str | None, color: str, kind: str, dash: str = "", width: float = 1.5) -> None:
        if not from_id or not to_id or from_id == to_id:
            return
        key = (str(from_id), str(to_id), kind)
        reverse_key = (str(to_id), str(from_id), kind)
        if key in link_keys or reverse_key in link_keys:
            return
        link_keys.add(key)
        link = {"from": str(from_id), "to": str(to_id), "color": color, "width": width, "kind": kind}
        if dash:
            link["dash"] = dash
        links.append(link)

    def node_for_doc(doc_id: str | None, preferred_lane: str) -> dict | None:
        if not doc_id:
            return None
        doc = doc_by_id.get(str(doc_id))
        if not doc:
            return None
        type_key = doc_type_key(doc.get("doc_type"))
        preferred_side = "R" if preferred_lane == "imperial" else "L"
        if type_key == "shangyu":
            preferred_side = "R"
        elif type_key == "shangzou":
            preferred_side = "L"
        node = node_by_doc_side.get((str(doc_id), preferred_side))
        if node:
            return node
        return node_by_doc_side.get((str(doc_id), "R")) or node_by_doc_side.get((str(doc_id), "L"))

    for node in event_nodes:
        payload = node["payload"]
        event_color = event_colors.get(node["actor"], "#8a765a")
        for source in payload.get("sources") or []:
            source_doc_id = source.get("doc_id") or source.get("docId")
            if payload.get("actor") != "emperor" and source.get("howKnown") == "上諭所載" and source.get("viaDoc"):
                source_doc_id = source.get("viaDoc")
            target = node_for_doc(source_doc_id, "imperial" if payload.get("actor") == "emperor" else "official")
            add_link(f"event-{payload.get('id')}", target.get("id") if target else None, event_color, "event-source", "4 4", 1.4)
        detail = payload.get("emperorDetail") or {}
        for source_doc_id in [detail.get("doc_id"), detail.get("edict_id")]:
            target = node_for_doc(source_doc_id, "imperial")
            add_link(f"event-{payload.get('id')}", target.get("id") if target else None, event_color, "event-origin", "4 4", 1.4)
        target = node_for_doc(detail.get("memDoc"), "official")
        add_link(f"event-{payload.get('id')}", target.get("id") if target else None, event_color, "event-source", "4 4", 1.4)
        for source in detail.get("infoSources") or []:
            target = node_for_doc(source.get("doc_id") or source.get("docId"), "official")
            add_link(f"event-{payload.get('id')}", target.get("id") if target else None, event_color, "event-source", "4 4", 1.4)
        for response_id in [payload.get("respondsToEventId"), *(payload.get("alsoRespondsToEventIds") or [])]:
            target = next((item for item in event_nodes if str(item["payload"].get("id")) == str(response_id)), None)
            add_link(f"event-{payload.get('id')}", target.get("id") if target else None, event_color, "event-response", "5 3", 1.5)

    for node in document_nodes:
        if node["recordType"] == "zhupi":
            other_side = "R" if node["side"] == "L" else "L"
            other = node_by_doc_side.get((str(node["payload"].get("docId")), other_side))
            add_link(node["id"], other.get("id") if other else None, "#c46a2b", "document-endpoint", "", 1.4)

    # Confirmed pairs: official_reply_to_yu and official_reply_to_emperor_zhu
    if CONFIRMED_PAIRS.is_file():
        confirmed_data = json.loads(CONFIRMED_PAIRS.read_text(encoding="utf-8"))
        for pair in confirmed_data.get("pairs", []):
            relation = pair.get("relation") or "official_reply_to_yu"
            yu_id = pair.get("yu_doc_id") or pair.get("zhu_doc_id")
            reply_id = pair.get("reply_doc_id")
            yu_node = node_for_doc(yu_id, "imperial")
            reply_node = node_for_doc(reply_id, "official")
            kind = "pair-reply-yu" if relation == "official_reply_to_yu" else "pair-reply-zhu"
            add_link(yu_node.get("id") if yu_node else None, reply_node.get("id") if reply_node else None, "#c07a1e", kind, "2 3", 1.6)

    # Yu source pairs: yu_source
    if YU_SOURCE.is_file():
        yu_source_data = json.loads(YU_SOURCE.read_text(encoding="utf-8"))
        for pair in yu_source_data.get("pairs", []):
            yu_id = pair.get("yu_doc_id")
            reply_id = pair.get("reply_doc_id")
            yu_node = node_for_doc(yu_id, "imperial")
            src_node = node_for_doc(reply_id, "official")
            add_link(yu_node.get("id") if yu_node else None, src_node.get("id") if src_node else None, "#2f8f6b", "yu-source", "4 3", 1.6)

    if not placement_dates:
        fail("sample state contains no dated chart nodes")
    min_date = min(placement_dates)
    max_date = max(placement_dates)

    ruler_labels = []
    cursor = date(min_date.year, min_date.month, 1)
    while cursor <= max_date:
        month_last = calendar.monthrange(cursor.year, cursor.month)[1]
        for day_number in (1, 11, 21):
            if day_number > month_last:
                continue
            tick = date(cursor.year, cursor.month, day_number)
            if tick < min_date and day_number != 1:
                continue
            if tick > max_date:
                continue
            ruler_labels.append(f"{tick.year}/{tick.month}" if day_number == 1 else str(day_number))
        cursor = date(cursor.year + (1 if cursor.month == 12 else 0), 1 if cursor.month == 12 else cursor.month + 1, 1)

    return {
        "startAr": min_date.strftime("%Y/%m/%d"),
        "endAr": max_date.strftime("%Y/%m/%d"),
        "daySpan": (max_date - min_date).days,
        "documentCount": len(chart_docs),
        "documentPlacementCount": len(document_nodes),
        "eventCount": len(event_nodes),
        "rulerLabels": ruler_labels,
        "laneRatios": {"events": 0.38, "official": 0.46, "imperial": 0.54, "emperor": 0.66},
        "nodes": document_nodes + event_nodes,
        "links": links,
    }


def main() -> int:
    documents = load_documents()
    document = load_document(documents)
    state_path = state_path_from_args()
    state = load_state(state_path)
    events = load_events(state)
    body = document["body"]

    dot_event = event_payload(find_event(events, DOT_EVENT))
    dot_emperor = event_payload(find_event(events, DOT_EMPEROR))
    candidates = [event_payload(find_event(events, name)) for name in AI_CANDIDATES]

    # 硃42 is the memorial the replica opens; its own quotations must resolve.
    for item in [dot_event, *candidates]:
        check_quote(body, item["quote"], item["subtitle"])

    # The 皇帝行動 dot quotes 諭24, not 硃42, so it is checked against its own
    # source document rather than the memorial body.
    if dot_emperor["quoteDocId"] != "諭24":
        fail("expected the 皇帝行動 dot to be sourced from 諭24")

    # The chart renderer consumes a compact, source-backed projection rather
    # than the full review export. It contains every dated sample dot and every
    # saved per-document AI chat history used by those dots.
    chart_preview = build_chart_preview(documents, events)
    chart_documents = [
        document_panel_payload(record)
        for record in documents
        if doc_type_key(record.get("doc_type"))
    ]
    chart_document_ids = {str(record.get("doc_id")) for record in documents if doc_type_key(record.get("doc_type"))}
    ai_chat_sources = [
        chat_source_projection(state, doc_id)
        for doc_id in state
        if str(doc_id) in chart_document_ids and isinstance(state.get(doc_id), dict) and isinstance(state.get(doc_id, {}).get("chat"), list)
    ]

    try:
        state_source = str(state_path.relative_to(ROOT))
    except ValueError:
        state_source = state_path.name

    payload = {
        "_generated_by": "tool/scripts py/build_part1_interface_data.py",
        "_sources": [
            "review-tools/shared data/stage1_original_text.json",
            "review-tools/(2) sample/confirmed-pairs.json",
            "review-tools/(2) sample/yu-source.json",
            state_source,
        ],
        "document": {
            "docId": document["doc_id"],
            "docType": document["doc_type"],
            "title": document["title"],
            "author": document["author"],
            "series": document["series"],
            "compiledIn": document["compiled_in"],
            "sendDate": document["send_date"],
            "receiveDate": document["receive_date"],
            "body": body,
            "rescriptText": document.get("rescript_text"),
        },
        # Full source records for documents represented by chart dots. This
        # lets the replica open the clicked dot's own original text without
        # making the browser fetch the review tool's server-only source route.
        "documents": chart_documents,
        # Lane labels exactly as they appear in review-tools/(2) sample/index.html.
        "lanes": [
            {"key": "events", "label": "戰場事件", "short": "事件"},
            {"key": "official", "label": "官員上奏", "short": "上奏"},
            {"key": "imperial", "label": "皇帝硃批下旨", "short": "硃批下旨"},
            {"key": "emperor", "label": "皇帝行動", "short": "皇帝行動"},
        ],
        "chartPreview": chart_preview,
        "dots": {
            "events": dot_event,
            "official": {
                "docId": document["doc_id"],
                "title": document["title"],
                "whenCh": document["send_date"][0],
                "dateAr": document["send_date"][1],
            },
            "imperial": {
                "docId": document["doc_id"],
                "title": document["title"],
                "whenCh": document["receive_date"][0],
                "dateAr": document["receive_date"][1],
                "rescriptText": document.get("rescript_text"),
            },
            "emperor": dot_emperor,
        },
        "aiCandidates": candidates,
        "aiChatSources": ai_chat_sources,
    }

    header = (
        "/* Part 1 「平台的整體介面」replica demonstration data.\n"
        " *\n"
        " * GENERATED FILE — regenerate with:\n"
        " *   cd \"/Users/creamybanana/Downloads/DH Project\"\n"
        " *   python3 \"tool/scripts py/build_part1_interface_data.py\"\n"
        " *\n"
        " * Every quotation, date and AI result below is copied from the canonical\n"
        " * Stage 1 source file and the selected sample review export. Do not hand-write\n"
        " * new historical content here; add it to the review tool first, then rebuild.\n"
        " * Presentation-only fields (labels, ordering) are safe to edit by hand.\n"
        " */\n"
    )
    body_js = json.dumps(payload, ensure_ascii=False, indent=2)
    OUT.write_text(f"{header}window.PART1_INTERFACE_DATA = {body_js};\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
    print(f"  document: {DOC_ID} ({len(body)} chars)")
    print(f"  chart documents: {chart_preview['documentCount']} records / {chart_preview['documentPlacementCount']} dated placements")
    print(f"  chart events: {chart_preview['eventCount']} squares")
    print(f"  chart links: {len(chart_preview['links'])}")
    print(f"  dots: {', '.join(payload['dots'].keys())}")
    print(f"  ai candidates: {len(candidates)}")
    print(f"  saved AI chat sources: {len(ai_chat_sources)} documents / {sum(source['outputItemCount'] for source in ai_chat_sources)} cards")
    return 0


if __name__ == "__main__":
    sys.exit(main())
