#!/usr/bin/env python3
"""Build the small, source-linked demonstration overlay from current sample data."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[3]
SAMPLE_DATA = ROOT / "review-tools" / "(2) sample" / "sample_all.data"
BASE_SAMPLE_SPEC = "HEAD:review-tools/(2) sample/sample_all.data"
STAGE1 = ROOT / "review-tools" / "shared data" / "stage1_original_text.json"
OUT = Path(__file__).resolve().parent


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_base_sample_data() -> dict:
    """Read the committed full sample snapshot for the complete dot layer.

    The current working sample state is intentionally reduced to the selected
    硃40/諭24 demonstration records. The committed snapshot supplies the other
    existing event and emperor-action dots without changing that working state.
    """
    result = subprocess.run(
        ["git", "-C", str(ROOT), "show", BASE_SAMPLE_SPEC],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


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


def main() -> None:
    data = read_json(SAMPLE_DATA)
    full_data = read_base_sample_data()
    source_payload = read_json(STAGE1)
    source_documents = source_payload.get("documents", source_payload) if isinstance(source_payload, dict) else source_payload
    source_by_id = {str(doc.get("doc_id")): doc for doc in source_documents}

    events = full_data.get("__events", [])
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

    # Keep every exported 諭24 action-extraction result. The action objects
    # themselves retain the full structured emperorDetail.
    yu_chats = list(data["諭24"].get("chat", []))

    zhu_event_ids = [event["id"] for event in zhu_events]
    yu_action_event_ids = [event["id"] for event in yu_action_events]

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

    clear_data = {
        "__meta": {
            "name": "硃40—諭24 clear demonstration",
            "purpose": "A demonstration export that keeps all existing event and emperor-action dots visible while separating the 硃40 and 諭24 data for later interaction code.",
            "documents": ["硃40", "諭24"],
            "event_dot_sources": ["硃40"],
            "emperor_action_sources": ["諭24"],
            "counts": {
                "all_event_dots": len(events),
                "other_event_and_action_dots": len(events) - len(zhu_events) - len(yu_action_events),
                "zhu40_event_dots": len(zhu_events),
                "yu24_emperor_action_dots": len(yu_action_events),
                "zhu40_ai_output_cards": len(zhu_chats),
                "yu24_ai_output_cards": len(yu_chats),
            },
        },
        "__clearDemo": {
            "version": 1,
            "document_dots": {
                "show_all": True,
                "clickable_document_ids": ["硃40", "諭24"],
                "non_clickable_document_rule": "all other existing document dots",
            },
            "event_dots": {
                "show_all": True,
                "source": "__events",
                "selected_data": {
                    "硃40": {
                        "role": "event_source",
                        "event_ids": zhu_event_ids,
                        "ai_output_path": "硃40.chat",
                    },
                    "諭24": {
                        "role": "emperor_action_source",
                        "event_ids": yu_action_event_ids,
                        "ai_output_path": "諭24.chat",
                    },
                },
            },
        },
        "__events": events,
        "__docPairs": [pair],
        "__sourceDocuments": [source_by_id[doc_id] for doc_id in ["硃40", "諭24"]],
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

    (OUT / "clear-demo.data").write_text(
        json.dumps(clear_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print(json.dumps(clear_data["__meta"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
