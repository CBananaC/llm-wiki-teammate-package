# Skill: Summarize 硃批 Records

## Website Prompt

Summarize this 硃批 record for the timeline reviewer. Cover both halves: the
official's memorial (who, what situation, what they report or request) and
the emperor's rescript reply (his judgment and any command). Preserve both
the official's send_date and the imperial receive/reply date; do not merge
them into one date. Quote briefly (short phrases, not long blocks) for both
the memorial and the rescript. Flag anything uncertain.

## Purpose

Use this skill to summarize Qing `硃批` records from the 林爽文事件 corpus into structured, evidence-based JSON.

A `硃批` record contains both the official's memorial and the emperor's reply/rescript. The summary must therefore preserve both the official send date and the imperial receive/reply date.

## When To Use

Use this skill when the task asks to summarize `doc_type: "硃批"` records, especially from:

- [[corpora/lin-shuangwen-first-hand-json]]
- `outputs/attempt-002/stage1-date-adjusted.json`

## Input Requirements

Each input record should preserve:

- `doc_id`
- `series`
- `doc_type`
- `author`
- `title`
- `send_date`
- `receive_date`
- `body`
- `rescript_text`

Both `send_date` and `receive_date` should be date pairs:

```json
"send_date": ["乾隆五十一年十二月十日", "1786/12/10"],
"receive_date": ["乾隆五十一年十二月二十七日", "1786/12/27"]
```

## Output Layout

Use a nested layout and place the day count immediately after `receive_date`:

```json
{
  "doc_id": "台22",
  "source_record": {
    "series": "明清臺灣檔案彙編",
    "doc_type": "硃批",
    "author": {
      "position": "福建陸路提督",
      "name": "任承恩"
    },
    "title": "為奏林爽文攻陷彰化已備兵聽候調遣事",
    "send_date": ["乾隆五十一年十二月十日", "1786/12/10"],
    "receive_date": ["乾隆五十一年十二月二十七日", "1786/12/27"],
    "days_between_send_and_receive": 17
  },
  "analysis": {
    "what_info_telling_emperor": "...",
    "sources_of_information": [],
    "responding_to_other_official_messages": [],
    "replying_to_previous_emperor_order": {},
    "official_location_now": {},
    "military_actions_done_reported_by_officials": [],
    "planned_action": {},
    "emperor_reply": {},
    "major_locations": [],
    "uncertainty": "..."
  }
}
```

## Required Analysis Fields

### `what_info_telling_emperor`

Summarize, without direct quotation, what the official is telling the emperor in the memorial portion.

### `sources_of_information`

List all important information sources named in the memorial. Do not collapse multiple sources into one.

### `responding_to_other_official_messages`

Use this field when the memorial is responding to, forwarding, or reporting another official's message.

Include:

- sender of the original message;
- summary of the original message;
- original sent date, if available;
- official received date, if available;
- quotation.

### `replying_to_previous_emperor_order`

Use this field only when the memorial itself is responding to a prior imperial order.

Do not confuse this with the current record's own `rescript_text`.

### `official_location_now`

Summarize where the official appears to be when writing or acting.

### `military_actions_done_reported_by_officials`

List military actions that have already been carried out and are reported by the official in the memorial portion of the `硃批` record.

Do not include actions that appear only in the emperor's reply unless the memorial itself also reports them. Do not put future plans here; use `planned_action` for intended, ordered, pending, or proposed action.

Each item should include:

```json
{
  "actor": "official, unit, local force, or reported actor who carried out the action",
  "action": "what was already done",
  "date": "date if visible, or 未明",
  "location": "place if visible, or 未明",
  "result": "reported result or effect, or 未明",
  "reported_by": "the memorial author or named information source",
  "quotation": "short quote proving the completed action"
}
```

If the memorial reports no completed military action, use an empty list and explain the absence in `uncertainty` if important.

### `planned_action`

Summarize what the official says he will do next.

### `emperor_reply`

Summarize the emperor's reply/rescript.

Required layout:

```json
{
  "summary": "皇帝批示已有旨意。",
  "receive_date": ["乾隆五十一年十二月二十七日", "1786/12/27"],
  "days_between_send_and_receive": 17,
  "quotation": "已有旨了。欽此。"
}
```

### `major_locations`

List major places found in the document and the situation at each place.

## Date Rule

Calculate `days_between_send_and_receive` from the Arabic dates:

```text
receive_date[1] - send_date[1]
```

If either Arabic date is missing or partial, write `未明`.

## Quotation Rules

- Preserve original Chinese wording in Traditional Chinese.
- Provide quotations for evidence-bearing fields except `what_info_telling_emperor`.
- Keep quotations short.

## Common Errors

- Forgetting `receive_date`.
- Forgetting `days_between_send_and_receive`.
- Treating the current 硃批 as a prior imperial order in `replying_to_previous_emperor_order`.
- Summarizing only the emperor's reply while ignoring the official memorial.
- Naming only one information source when the memorial contains several.
- Mixing military actions already done with planned or emperor-commanded future actions.

## Related Outputs

- `outputs/attempt-002/stage1-zhupi-summaries-check5-gemini35.json`
