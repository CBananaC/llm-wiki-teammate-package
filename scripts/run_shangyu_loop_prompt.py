#!/usr/bin/env python3
"""Run the saved 上諭 review-loop prompt against one timeline record.

Example:
  python3 scripts/run_shangyu_loop_prompt.py \
    --proxy https://gemini-proxy-v2ewrxq4sq-de.a.run.app --doc-id 天36
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "outputs" / "attempt-002" / "dual-timeline-data.json"
PROMPT_PATH = ROOT / "skills" / "shangyu-review-loop.md"
PROMPT_RE = re.compile(r"^##\s*Website Prompt[ \t]*\n(.*?)(?=\n##\s|\Z)", re.S | re.M)


def parse_date(value: str | None) -> datetime | None:
    try:
        return datetime.strptime(value or "", "%Y/%m/%d")
    except ValueError:
        return None


def date_at_or_before(value: str | None, cutoff: str | None) -> bool:
    value_date, cutoff_date = parse_date(value), parse_date(cutoff)
    return bool(value_date and cutoff_date and value_date <= cutoff_date)


def website_prompt() -> str:
    match = PROMPT_RE.search(PROMPT_PATH.read_text(encoding="utf-8"))
    if not match:
        raise RuntimeError(f"No Website Prompt in {PROMPT_PATH}")
    return match.group(1).strip()


def report_officials(edict: dict) -> list[str]:
    """Prefer names explicitly introduced by 據…奏; fall back to recipients."""
    text = edict.get("body") or ""
    names = re.findall(r"據([^，。；\s]{2,12})奏", text)
    if not names:
        names = edict.get("recipients") or []
    return list(dict.fromkeys(name.strip() for name in names if name.strip()))


def candidates(records: list[dict], edict: dict) -> list[dict]:
    """Choose direct-report candidates, preferring the edict's own date."""
    deadline = edict.get("annAr")
    officials = report_officials(edict)
    selected = [
        record
        for record in records
        if record.get("type") == "zhupi"
        and date_at_or_before(record.get("recvAr"), deadline)
        and any(name in (record.get("author_name") or "") for name in officials)
    ]
    # The same-day receipt date is strongest evidence that the report was
    # available to the emperor when this edict was issued.  Keep it first;
    # then retain at most four immediately earlier reports if necessary.
    selected.sort(key=lambda record: (record.get("recvAr") != deadline, record.get("recvAr") or ""), reverse=False)
    return selected[:6]


def days_after(value: str | None, cutoff: str | None) -> int | None:
    """Whole days that `value` falls after `cutoff` (negative if before)."""
    value_date, cutoff_date = parse_date(value), parse_date(cutoff)
    if not value_date or not cutoff_date:
        return None
    return (value_date - cutoff_date).days


def command_targets(edict: dict) -> list[str]:
    """Officials the edict commands — its recipients."""
    return [name.strip() for name in (edict.get("recipients") or []) if name.strip()]


# An 上諭 physically has to travel to the front before a recipient can act on it,
# so a memorial sent only a day or two later cannot be a response to it.  Require
# a realistic transit lag: at least 14 days after the edict, and only if nothing
# qualifies, relax to 10 days.
RESPONSE_LAG_DAYS = (14, 10)

# Minimum contiguous character overlap that counts as the memorial quoting the
# edict.  Court boilerplate ("欽此", "臣仰承訓示") is short; a genuine quotation of
# the edict's own wording runs longer, so a 10-char window is a strong signal.
CITATION_MIN_LEN = 10

# Punctuation/formatting stripped before overlap testing so that "，" or line
# breaks between two docs don't hide a real shared phrase.
_CITATION_STRIP = str.maketrans("", "", "，。、；：？！「」『』（）【】〔〕…—\n\r\t 　,.;:?!()[]")


def _normalize_for_citation(text: str | None) -> str:
    return (text or "").translate(_CITATION_STRIP)


# Standardised 廷寄 transmission wrapper and court formulae.  These appear in
# every 廷寄 edict AND in officials' acknowledgements, so an overlap that is only
# this boilerplate does NOT prove the memorial answers THIS particular edict.
_BOILERPLATE_MARKERS = (
    "字寄", "大學士", "廷寄", "廷寄", "遵旨寄信", "奉上諭", "欽此", "承准",
    "阿桂", "和珅", "軍機大臣", "寄信前來", "由六百里", "由五百里", "加緊", "跪讀",
)


def _is_boilerplate(phrase: str) -> bool:
    return any(marker in phrase for marker in _BOILERPLATE_MARKERS)


def citation_overlap(edict_body: str, cand_body: str, min_len: int = CITATION_MIN_LEN) -> str:
    """Longest contiguous SUBSTANTIVE phrase (>= min_len) the two share, else ''.

    This is the citation test: officials quote the edict they are answering, so a
    long shared phrase confirms the memorial is a reply to THIS edict.  Phrases
    that are only 廷寄 transmission boilerplate are rejected, since those recur
    across unrelated edicts and would produce false matches.
    """
    edict_norm = _normalize_for_citation(edict_body)
    cand_norm = _normalize_for_citation(cand_body)
    if len(edict_norm) < min_len or not cand_norm:
        return ""
    best = ""
    i, limit = 0, len(edict_norm) - min_len
    while i <= limit:
        if edict_norm[i:i + min_len] in cand_norm:
            end = i + min_len
            while end <= len(edict_norm) and edict_norm[i:end] in cand_norm:
                end += 1
            phrase = edict_norm[i:end - 1]
            if not _is_boilerplate(phrase) and len(phrase) > len(best):
                best = phrase
            i += max(1, len(phrase) - min_len + 1)
        else:
            i += 1
    return best


def response_candidates(records: list[dict], edict: dict) -> list[dict]:
    """Memorials that are confirmed replies to this edict, by ALL three tests:
    (1) authored by a recipient of the edict (identity),
    (2) sent >=14 days later, else >=10 (timing),
    (3) quoting a >=10-char phrase of the edict's text (citation).
    Each returned record carries `_citation` (the matched phrase) for the prompt.
    """
    edict_date = edict.get("annAr")
    edict_body = edict.get("body") or ""
    targets = command_targets(edict)
    if not targets:
        return []
    by_official = [
        record
        for record in records
        if record.get("id") != edict.get("id")
        and any(name in (record.get("author_name") or "") for name in targets)
    ]
    for min_lag in RESPONSE_LAG_DAYS:
        selected = []
        for record in by_official:
            lag = days_after(record.get("sendAr"), edict_date)
            if lag is None or lag < min_lag:
                continue
            phrase = citation_overlap(edict_body, record.get("body") or "")
            if not phrase:
                continue
            record = dict(record)
            record["_citation"] = phrase
            selected.append(record)
        if selected:
            selected.sort(key=lambda record: record.get("sendAr") or "")
            return selected[:8]
    return []


def candidate_block(records: list[dict]) -> str:
    return "\n\n".join(
        "【候選奏摺／硃批】\n"
        f"doc_id：{record.get('id', '')}\n"
        f"具奏官員：{record.get('author_name', '')}\n"
        f"上奏日：{record.get('sendAr', '') or '未明'}\n"
        f"硃批／收受日：{record.get('recvAr', '') or '未明'}\n"
        f"標題：{record.get('title', '')}\n"
        f"原文：\n{record.get('body', '')}"
        for record in records
    )


def response_block(records: list[dict]) -> str:
    return "\n\n".join(
        "【候選回應】\n"
        f"doc_id：{record.get('id', '')}\n"
        f"具奏官員：{record.get('author_name', '')}\n"
        f"上奏日：{record.get('sendAr', '') or '未明'}\n"
        f"硃批／收受日：{record.get('recvAr', '') or '未明'}\n"
        f"引用上諭文字：{record.get('_citation', '') or '未明'}\n"
        f"標題：{record.get('title', '')}\n"
        f"原文：\n{record.get('body', '')}"
        for record in records
    )


def repair_json(text: str) -> str:
    """Best-effort repair of the model's JSON: strip code fences, trim to the
    outermost braces, and force every closer to match its opener (the model
    sometimes closes an object with ] or vice versa)."""
    s = (text or "").strip()
    if s.startswith("```"):
        s = s.split("\n", 1)[1] if "\n" in s else s
        if s.rstrip().endswith("```"):
            s = s.rstrip()[:-3]
    start, end = s.find("{"), s.rfind("}")
    if start >= 0 and end > start:
        s = s[start:end + 1]
    out: list[str] = []
    stack: list[str] = []
    close = {"{": "}", "[": "]"}
    in_str = escaped = False
    for ch in s:
        if in_str:
            out.append(ch)
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
            out.append(ch)
        elif ch in "{[":
            stack.append(ch)
            out.append(ch)
        elif ch in "}]":
            out.append(close[stack.pop()] if stack else ch)
        else:
            out.append(ch)
    while stack:
        out.append(close[stack.pop()])
    return "".join(out)


def parse_model_json(text: str) -> dict | None:
    for candidate in (text, repair_json(text)):
        try:
            obj = json.loads(candidate)
            if isinstance(obj, dict):
                return obj
        except (json.JSONDecodeError, TypeError):
            continue
    return None


def call_proxy(proxy: str, payload: dict) -> dict:
    request = Request(
        proxy.rstrip("/") + "/chat",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(request, timeout=180) as response:
        return json.loads(response.read().decode("utf-8"))


def write_bundle(result: dict, name: str) -> Path:
    """Package a completed prompt result for the website bundle picker."""
    bundle_root = ROOT / "outputs" / "review-bundles" / name
    output_dir = bundle_root / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)
    response = result.get("response") or {}
    visible_response = response.get("text") if isinstance(response, dict) else response
    if not visible_response:
        visible_response = json.dumps(response, ensure_ascii=False, indent=2)
    parsed = parse_model_json(visible_response) if isinstance(visible_response, str) else None
    row = {
        "doc_id": result.get("doc_id", ""),
        "candidate_doc_ids": result.get("candidate_doc_ids", []),
        "candidate_response_doc_ids": result.get("candidate_response_doc_ids", []),
        "prompt": "上諭審閱迴圈",
        "response": visible_response,
        "model": "saved prompt output",
    }
    if parsed is not None:
        row["parsed"] = parsed
    (output_dir / "shangyu-review-loop.json").write_text(
        json.dumps([row], ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    manifest = {
        "name": name,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "source": "outputs/attempt-002/dual-timeline-data.json",
        "model": "gemini-3.5-flash",
        "doc_ids": [result.get("doc_id", "")],
        "candidate_doc_ids": result.get("candidate_doc_ids", []),
        "candidate_response_doc_ids": result.get("candidate_response_doc_ids", []),
        "chain": ["shangyu-review-loop"],
    }
    (bundle_root / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return bundle_root


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--proxy", default=os.environ.get("GEMINI_PROXY_URL", ""))
    parser.add_argument("--doc-id", default="天36")
    parser.add_argument("--model", default="gemini-3.5-flash")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--bundle-name", default="tian36-shangyu-loop-prompt")
    parser.add_argument("--package-result", type=Path,
                        help="Package an existing result JSON without calling the proxy again.")
    args = parser.parse_args()
    if args.package_result:
        result = json.loads(args.package_result.read_text(encoding="utf-8"))
        print(write_bundle(result, args.bundle_name))
        return 0
    if not args.proxy:
        parser.error("Set GEMINI_PROXY_URL or pass --proxy.")

    records = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    edict = next((record for record in records if record.get("id") == args.doc_id), None)
    if not edict:
        parser.error(f"Document not found: {args.doc_id}")
    if edict.get("type") != "shangyu":
        parser.error(f"{args.doc_id} is not an 上諭 record")

    source_candidates = candidates(records, edict)
    resp_candidates = response_candidates(records, edict)
    body = (edict.get("body") or "") + "\n\n" + candidate_block(source_candidates)
    if resp_candidates:
        body += "\n\n" + response_block(resp_candidates)
    payload = {
        "mode": "ask",
        "model": args.model,
        "doc_id": edict["id"],
        "doc_type": edict["doc_type"],
        "title": edict["title"],
        "body": body,
        "question": website_prompt(),
    }
    result = call_proxy(args.proxy, payload)
    output = {
        "doc_id": edict["id"],
        "edict_date": edict.get("annAr"),
        "candidate_doc_ids": [record["id"] for record in source_candidates],
        "candidate_response_doc_ids": [record["id"] for record in resp_candidates],
        "prompt": website_prompt(),
        "request": payload,
        "response": result,
    }
    target = args.output or ROOT / "outputs" / "attempt-002" / f"{args.doc_id}-shangyu-loop-prompt.json"
    target.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    # Always emit the website-loadable bundle in the same run — a terminal run
    # should never leave output that the site can't display.
    bundle_root = write_bundle(output, args.bundle_name)
    print(target)
    print(bundle_root)
    return 0


if __name__ == "__main__":
    sys.exit(main())
