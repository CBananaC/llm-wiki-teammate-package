#!/usr/bin/env python3
"""Build the small, source-linked demonstration overlay from current sample data."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SAMPLE_DATA = ROOT / "review-tools" / "(2) sample" / "sample_all.data"
SAMPLE_HTML = ROOT / "review-tools" / "(2) sample" / "index.html"
STAGE1 = ROOT / "review-tools" / "shared data" / "stage1_original_text.json"
OUT = Path(__file__).resolve().parent


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def source_doc_ids(event: dict) -> set[str]:
    ids = {str(source.get("doc_id")) for source in event.get("sources", []) if source.get("doc_id")}
    for provenance in event.get("provenance", []):
        ids.update(
            str(hop.get("doc_id"))
            for hop in provenance.get("hops", [])
            if hop.get("doc_id")
        )
    return ids


def event_has_item(chat: dict, event: dict) -> bool:
    event_id = event.get("id")
    return any(
        isinstance(item, dict)
        and (
            item.get("__evId") == event_id
            or (
                item.get("subtitle") == event.get("subtitle")
                and "硃40" in {str(source.get("doc_id")) for source in item.get("sources", [])}
            )
        )
        for item in chat.get("items", [])
    )


def base_document_ids() -> list[str]:
    html = SAMPLE_HTML.read_text(encoding="utf-8")
    marker = "const AI_DUAL = "
    start = html.index(marker) + len(marker)
    end = html.index("];\n", start) + 1
    records = json.loads(html[start:end])
    return [str(record["id"]) for record in records if record.get("id")]


def main() -> None:
    data = read_json(SAMPLE_DATA)
    source_payload = read_json(STAGE1)
    source_documents = source_payload.get("documents", source_payload) if isinstance(source_payload, dict) else source_payload
    source_by_id = {str(doc.get("doc_id")): doc for doc in source_documents}

    events = data.get("__events", [])
    zhu_events = [
        event
        for event in events
        if event.get("actor") != "emperor" and "硃40" in source_doc_ids(event)
    ]
    yu_action_events = [
        event
        for event in events
        if event.get("actor") == "emperor" and "諭24" in source_doc_ids(event)
    ]
    kept_events = zhu_events + yu_action_events

    # Keep one current AI result card for each retained 硃40 dot. The matching
    # __evId is the strongest link; the subtitle/source fallback preserves the
    # same relation for cards exported before __evId was added.
    zhu_chats = []
    all_zhu_chats = data["硃40"].get("chat", [])
    for event in zhu_events:
        match = next((chat for chat in all_zhu_chats if event_has_item(chat, event)), None)
        if match is not None:
            zhu_chats.append(match)

    # Keep the compact action-extraction output and its first follow-up result
    # set. The action objects themselves retain the full structured emperorDetail.
    yu_chats = [
        chat
        for index, chat in enumerate(data["諭24"].get("chat", []))
        if index in {9, 10, 11, 12, 13, 14, 15, 16, 17}
    ]

    pair = {
        "zhu_doc_id": "硃40",
        "reply_doc_id": "諭24",
        "relation": "official_reply_to_emperor_zhu",
        "match_level": "demonstration",
        "confirmed_at": None,
        "evidence": {
            "relation_note": "Demonstration-only connection requested for this clear dataset; it does not replace confirmed research pairings.",
        },
    }

    visible_documents = {"硃40", "諭24"}
    hidden_documents = [doc_id for doc_id in base_document_ids() if doc_id not in visible_documents]

    clear_data = {
        "__meta": {
            "name": "硃40—諭24 clear demonstration",
            "purpose": "A small demonstration overlay containing only 硃40 event dots, 諭24 emperor-action dots, their retained AI output cards, and the requested demonstration response link.",
            "documents": ["硃40", "諭24"],
            "event_dot_sources": ["硃40"],
            "emperor_action_sources": ["諭24"],
            "counts": {
                "zhu40_event_dots": len(zhu_events),
                "yu24_emperor_action_dots": len(yu_action_events),
                "zhu40_ai_output_cards": len(zhu_chats),
                "yu24_ai_output_cards": len(yu_chats),
            },
        },
        "__hidden": hidden_documents,
        "__events": kept_events,
        "__docPairs": [pair],
        "__workspaceGroups": {
            "硃40|諭24": {
                "doc_ids": ["硃40", "諭24"],
                "notes": "示範用關聯：按要求把諭24連到硃40，作為回應硃40；此關聯不是已確認的研究配對。",
                "answers": [],
                "chat": [],
                "notesList": [],
            }
        },
        "硃40": {
            "overallAdj": data["硃40"].get("overallAdj", ""),
            "divisions": data["硃40"].get("divisions", []),
            "chat": zhu_chats,
        },
        "諭24": {
            "overallAdj": data["諭24"].get("overallAdj", ""),
            "divisions": data["諭24"].get("divisions", []),
            "chat": yu_chats,
        },
    }

    pair_payload = {
        "kind": "confirmed-pairs",
        "exported_at": "2026-07-30 17:23",
        "count": 1,
        "pairs": [pair],
    }
    source_payload = {
        "description": "Only the two canonical Stage 1 source documents used by the clear demonstration.",
        "documents": [source_by_id[doc_id] for doc_id in ["硃40", "諭24"]],
    }

    (OUT / "clear-demo.data").write_text(
        json.dumps(clear_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (OUT / "confirmed-pairs.json").write_text(
        json.dumps(pair_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (OUT / "source-documents.json").write_text(
        json.dumps(source_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print(json.dumps(clear_data["__meta"], ensure_ascii=False, indent=2))
    print(json.dumps({"hidden_document_dots": len(hidden_documents)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
