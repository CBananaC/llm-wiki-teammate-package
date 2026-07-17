#!/usr/bin/env python3
"""Summarize Stage 1 上奏 records with Google Gemini.

Output:
  outputs/attempt-002/stage1-shangzou-summaries.json

The script is resumable: existing doc_id summaries are kept unless --overwrite
is passed.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import time
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any


SOURCE = Path("outputs/attempt-002/stage1_original_text.json")
OUTPUT = Path("outputs/attempt-002/stage1-shangzou-summaries.json")
DEFAULT_MODELS = [
    "gemini-2.5-flash",
    "gemini-2.0-flash-001",
    "gemini-1.5-flash-002",
]
ENV_LOCAL = Path(".env.local")


SYSTEM_INSTRUCTION = """You are helping with historical research on the Lin Shuangwen war.
Read one Qing official memorial (上奏) and produce a compact JSON summary.
Do not invent facts. If the text does not say something, write "未明" and explain briefly.
Use Traditional Chinese for Chinese terms and quotations.
Quotation requirements:
- For every evidence-bearing field, include a short direct quotation from the source.
- For what_info_telling_emperor, do not include a quotation; summarize in your own words.
- Keep each quotation short, ideally under 40 Chinese characters.
Important:
- Do not collapse multiple sources of information into one. If the memorial names several sources, list all important sources separately.
- For locations, identify major places mentioned and summarize what is happening there.
- For 上奏 and 硃批 records, identify military actions that have already been done and reported by officials in the document. Keep these separate from planned, proposed, pending, or emperor-commanded future actions.
- For 上奏 records, explicitly check whether the text itself contains an emperor's 硃批/rescript or imperial reply, and do not confuse that with the official replying to a previous 上諭.
Return JSON only."""


def run_text(cmd: list[str]) -> str:
    return subprocess.check_output(cmd, text=True).strip()


def get_token() -> str:
    return run_text(["gcloud", "auth", "print-access-token"])


def get_project() -> str:
    return run_text(["gcloud", "config", "get-value", "project"])


def load_env_key(name: str) -> str | None:
    if name in os.environ:
        return os.environ[name]
    if not ENV_LOCAL.exists():
        return None
    for line in ENV_LOCAL.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        if key == name:
            return value.strip().strip('"').strip("'")
    return None


def build_prompt(record: dict[str, Any]) -> str:
    doc_type = record.get("doc_type")
    payload = {
        "doc_id": record.get("doc_id"),
        "series": record.get("series"),
        "doc_type": doc_type,
        "author": record.get("author"),
        "title": record.get("title"),
        "send_date": record.get("send_date"),
        "receive_date": record.get("receive_date"),
        "announce_date": record.get("announce_date"),
        "body": record.get("body"),
        "rescript_text": record.get("rescript_text"),
    }
    if doc_type == "上諭":
        return f"""Summarize this Stage 1 上諭 record.

Output schema:
{{
  "doc_id": "...",
  "source_record": {{
    "series": "...",
    "doc_type": "上諭",
    "author": {{"position": "...", "name": "..."}},
    "title": "...",
    "yu_written_by": {{"answer": "大學士...字寄...", "quotation": "short quote from opening formula"}},
    "announce_date": ["Chinese date", "Arabic date"]
  }},
  "analysis": {{
    "key_info": "What key information or situation is the emperor addressing?",
    "responding_to_message": {{
      "answer": "What report/message/memorial is the emperor responding to?",
      "source_actor": "who sent or supplied the message, if visible",
      "message_summary": "summarize the original message/report",
      "message_sent_date": "date of original message if visible, or 未明",
      "emperor_received_or_responded_date": "date emperor is responding/announcing, if visible",
      "quotation": "short quote proving the responding-to relationship"
    }},
    "emperor_opinion": {{
      "summary": "emperor's judgment/opinion on the message or situation",
      "quotation": "short quote showing the emperor's opinion"
    }},
    "emperor_command": {{
      "summary": "what the emperor commands should be done",
      "target": "who the order is directed to, often author.name",
      "quotation": "short quote showing the command"
    }},
    "major_locations": [
      {{
        "place": "place name",
        "situation": "what is happening there in this 上諭",
        "quotation": "short quote proving this location/situation"
      }}
    ],
    "uncertainty": "Any important uncertainty or missing evidence."
  }}
}}

Record:
{json.dumps(payload, ensure_ascii=False, indent=2)}
"""

    emperor_reply_schema = ""
    if doc_type == "硃批":
        emperor_reply_schema = """    "emperor_reply": {
      "summary": "summarize the emperor's reply/rescript",
      "receive_date": ["Chinese date", "Arabic date"],
      "days_between_send_and_receive": 0,
      "quotation": "short quote from rescript_text or 硃批 text"
    },
"""
    embedded_rescript_schema = ""
    if doc_type == "上奏":
        embedded_rescript_schema = """    "emperor_rescript_inside_memorial": {
      "answer": "yes/no/unclear + explanation. Check whether this 上奏 text itself contains an emperor's 硃批/rescript or similar imperial reply.",
      "what_info_emperor_is_replying_to": "the specific report, claim, request, or situation in the memorial that the emperor's 硃批 addresses, or 未明. If the emperor writes 已有旨了, identify what matter already received an order.",
      "rescript_summary": "summarize the emperor's reply if present, or 未明",
      "rescript_date": "date of the rescript if visible, or 未明",
      "quotation": "short quote proving the embedded 硃批/rescript if present; if absent, use 未明 unless a brief ending phrase proves absence"
    },
"""

    return f"""Summarize this Stage 1 {doc_type} record.

Output schema:
{{
  "doc_id": "...",
    "source_record": {{
    "series": "...",
    "doc_type": "{doc_type}",
    "author": {{"position": "...", "name": "..."}},
    "title": "...",
    "send_date": ["Chinese date", "Arabic date"],
    "receive_date": ["Chinese date", "Arabic date"],
    "days_between_send_and_receive": 0
  }},
  "analysis": {{
    "what_info_telling_emperor": "What information is the official telling the emperor? No quotation here.",
    "sources_of_information": [
      {{
        "source_actor": "person/office/source named in the memorial",
        "source_type": "稟報/札/咨/探報/訪聞/奏報/other/未明",
        "message_summary": "summarize the information from this source",
        "source_message_sent_date": "date the source message was sent, or 未明",
        "official_received_date": "date the memorial author received this source message, or 未明",
        "quotation": "short quote proving this source"
      }}
    ],
    "responding_to_other_official_messages": [
      {{
        "answer": "yes/no/unclear + explanation",
        "other_official_sender": "official/person who sent the original message, or 未明",
        "original_message_summary": "summarize the original message from the other official",
        "original_message_sent_date": "date when that original message was sent, or 未明",
        "official_received_date": "date when the memorial author received it, or 未明",
        "quotation": "short quote proving this relationship"
      }}
    ],
    "replying_to_previous_emperor_order": {{
      "answer": "yes/no/unclear + explanation",
      "original_emperor_message_summary": "summarize the emperor's previous order/message if any",
      "emperor_order_sent_date": "date of emperor order/message, or 未明",
      "official_received_date": "date when official received the emperor order/message, or 未明",
      "quotation": "short quote proving this relationship"
    }},
{embedded_rescript_schema}
    "official_location_now": {{"answer": "...", "quotation": "..."}},
    "military_actions_done_reported_by_officials": [
      {{
        "actor": "official, unit, local force, or reported actor who carried out the action",
        "action": "what was already done, not a future plan",
        "date": "date if visible, or 未明",
        "location": "place if visible, or 未明",
        "result": "reported result or effect, or 未明",
        "reported_by": "the memorial author or named information source",
        "quotation": "short quote proving the completed action"
      }}
    ],
    "planned_action": {{"answer": "What the official says he will do next.", "quotation": "..."}},
{emperor_reply_schema}
    "major_locations": [
      {{
        "place": "place name",
        "situation": "what is happening there in this document",
        "quotation": "short quote proving this location/situation"
      }}
    ],
    "uncertainty": "Any important uncertainty or missing evidence."
  }}
}}

Record:
{json.dumps(payload, ensure_ascii=False, indent=2)}
"""


def extract_json(text: str) -> dict[str, Any]:
    text = text.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip().startswith("```"):
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start >= 0 and end > start:
            return json.loads(text[start : end + 1])
        raise


def call_vertex(project: str, location: str, model: str, token: str, prompt: str, timeout: int, max_output_tokens: int) -> dict[str, Any]:
    url = f"https://aiplatform.googleapis.com/v1/projects/{project}/locations/{location}/publishers/google/models/{model}:generateContent"
    body = {
        "systemInstruction": {
            "parts": [{"text": SYSTEM_INSTRUCTION}]
        },
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}],
            }
        ],
        "generationConfig": {
            "temperature": 0.1,
            "topP": 0.8,
            "maxOutputTokens": max_output_tokens,
            "responseMimeType": "application/json",
        },
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    text = data["candidates"][0]["content"]["parts"][0]["text"]
    return extract_json(text)


def call_genai_api_key(model: str, api_key: str, prompt: str, timeout: int, max_output_tokens: int) -> dict[str, Any]:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    body = {
        "systemInstruction": {
            "parts": [{"text": SYSTEM_INSTRUCTION}]
        },
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}],
            }
        ],
        "generationConfig": {
            "temperature": 0.1,
            "topP": 0.8,
            "maxOutputTokens": max_output_tokens,
            "responseMimeType": "application/json",
        },
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    text = data["candidates"][0]["content"]["parts"][0]["text"]
    return extract_json(text)


def load_existing(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def save(path: Path, rows: list[dict[str, Any]]) -> None:
    path.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def days_between(send_date: Any, receive_date: Any) -> int | None:
    if not (isinstance(send_date, list) and isinstance(receive_date, list)):
        return None
    if len(send_date) < 2 or len(receive_date) < 2:
        return None
    try:
        sent = datetime.strptime(send_date[1], "%Y/%m/%d")
        received = datetime.strptime(receive_date[1], "%Y/%m/%d")
    except Exception:
        return None
    return (received - sent).days


def extract_yu_written_by(body: Any) -> dict[str, str] | None:
    if not isinstance(body, str) or not body:
        return None
    head = body[:260]
    if "奉上諭" not in head:
        return None
    before = head.split("奉上諭", 1)[0]
    if "乾隆" in before:
        before = before.split("乾隆", 1)[0].rstrip("，, ")
    before = before.strip("，, ：:")
    if not before or before.startswith("正文見"):
        return None
    return {"answer": before, "quotation": before}


def enforce_source_record(summary: dict[str, Any], source: dict[str, Any]) -> None:
    source_record: dict[str, Any] = {
        "series": source.get("series"),
        "doc_type": source.get("doc_type"),
        "author": source.get("author"),
        "title": source.get("title"),
    }
    if source.get("doc_type") == "上諭":
        yu_written_by = extract_yu_written_by(source.get("body"))
        if yu_written_by:
            source_record["yu_written_by"] = yu_written_by
        source_record["announce_date"] = source.get("announce_date")
    else:
        source_record["send_date"] = source.get("send_date")
    if source.get("receive_date") is not None:
        source_record["receive_date"] = source.get("receive_date")
        delta = days_between(source.get("send_date"), source.get("receive_date"))
        if delta is not None:
            source_record["days_between_send_and_receive"] = delta
    summary["source_record"] = source_record
    if source.get("doc_type") == "硃批":
        analysis = summary.setdefault("analysis", {})
        emperor_reply = analysis.setdefault("emperor_reply", {})
        emperor_reply.setdefault("receive_date", source.get("receive_date"))
        delta = days_between(source.get("send_date"), source.get("receive_date"))
        if delta is not None:
            emperor_reply["days_between_send_and_receive"] = delta


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--location", default="global")
    parser.add_argument("--model", action="append", dest="models")
    parser.add_argument("--provider", choices=["vertex", "genai"], default="vertex")
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--max-output-tokens", type=int, default=4096)
    parser.add_argument("--sleep", type=float, default=1.0)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--doc-type", default="上奏")
    args = parser.parse_args()

    project = get_project() if args.provider == "vertex" else None
    token = get_token() if args.provider == "vertex" else None
    api_key = load_env_key("GOOGLE_API_KEY") if args.provider == "genai" else None
    if args.provider == "genai" and not api_key:
        raise RuntimeError("GOOGLE_API_KEY not found in environment or .env.local")
    models = args.models or DEFAULT_MODELS

    records = [row for row in json.loads(SOURCE.read_text(encoding="utf-8")) if row.get("doc_type") == args.doc_type]
    if args.offset:
        records = records[args.offset :]
    if args.limit:
        records = records[: args.limit]

    output_path = args.output
    existing = [] if args.overwrite else load_existing(output_path)
    by_id = {row.get("doc_id"): row for row in existing}
    results = existing[:]

    selected_model: str | None = None
    for idx, record in enumerate(records, start=1):
        doc_id = record.get("doc_id")
        if doc_id in by_id:
            print(f"skip existing {doc_id}")
            continue
        prompt = build_prompt(record)
        last_error = None
        summary = None
        candidate_models = [selected_model] if selected_model else models
        for model in candidate_models:
            if model is None:
                continue
            for attempt in range(1, args.retries + 1):
                try:
                    if args.provider == "vertex":
                        summary = call_vertex(project, args.location, model, token, prompt, args.timeout, args.max_output_tokens)
                    else:
                        summary = call_genai_api_key(model, api_key, prompt, args.timeout, args.max_output_tokens)
                    selected_model = model
                    break
                except urllib.error.HTTPError as e:
                    err = e.read().decode("utf-8", errors="replace")
                    last_error = f"HTTP {e.code}: {err[:700]}"
                    if e.code == 429 and attempt < args.retries:
                        wait = min(90, 12 * attempt)
                        print(f"429 for {doc_id}; sleeping {wait}s before retry {attempt + 1}/{args.retries}")
                        time.sleep(wait)
                        continue
                    if selected_model:
                        raise RuntimeError(last_error)
                    break
                except Exception as e:
                    last_error = repr(e)
                    if attempt >= args.retries:
                        if selected_model:
                            raise
                        break
                    time.sleep(0.8 * attempt)
            if summary is not None:
                break
        else:
            raise RuntimeError(f"all models failed for {doc_id}: {last_error}")

        summary.setdefault("doc_id", doc_id)
        enforce_source_record(summary, record)
        summary["_model"] = selected_model
        results.append(summary)
        by_id[doc_id] = summary
        save(output_path, results)
        print(f"{idx}/{len(records)} summarized {doc_id} with {selected_model}")
        time.sleep(args.sleep)

    print(json.dumps({"output": str(output_path), "count": len(results), "model": selected_model}, ensure_ascii=False))


if __name__ == "__main__":
    main()
