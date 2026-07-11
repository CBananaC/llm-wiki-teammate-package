# Skill: Summarize 上奏 Records

## Website Prompt

Summarize this 上奏 memorial for the timeline reviewer. State who is reporting,
what situation or event they are reporting on, what request or recommendation
they make (if any), and the major locations involved with the situation at
each. Use send_date. Quote briefly (short phrases, not long blocks) to
support each field, in original Traditional Chinese wording. Flag anything
uncertain rather than guessing.

## Purpose

Use this skill to summarize Qing `上奏` records from the 林爽文事件 corpus into structured, evidence-based JSON.

This skill is designed for Stage 1 research, but the schema can be reused for later stages if the source JSON follows the same date and metadata conventions.

## When To Use

Use this skill when the task asks to summarize `doc_type: "上奏"` records, especially from:

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
- `body`

The `send_date` value should be a pair:

```json
["乾隆五十一年十二月十日", "1786/12/10"]
```

## Output Layout

Use a nested layout so documents are easy to distinguish:

```json
{
  "doc_id": "台2",
  "source_record": {
    "series": "明清臺灣檔案彙編",
    "doc_type": "上奏",
    "author": {
      "position": "福建陸路提督",
      "name": "任承恩"
    },
    "title": "為奏林爽文結黨失陷彰城事",
    "send_date": ["乾隆五十一年十二月十日", "1786/12/10"]
  },
  "analysis": {
    "what_info_telling_emperor": "...",
    "sources_of_information": [],
    "responding_to_other_official_messages": [],
    "replying_to_previous_emperor_order": {},
    "emperor_rescript_inside_memorial": {},
    "official_location_now": {},
    "military_actions_done_reported_by_officials": [],
    "planned_action": {},
    "major_locations": [],
    "uncertainty": "..."
  }
}
```

## Required Analysis Fields

### `what_info_telling_emperor`

Summarize, without direct quotation, what the official is telling the emperor.

### `sources_of_information`

List all important information sources named in the document. Do not collapse multiple sources into one.

Each item should include:

```json
{
  "source_actor": "署臺灣府淡水同知程峻、竹塹營守備董得魁",
  "source_type": "稟報",
  "message_summary": "...",
  "source_message_sent_date": "未明",
  "official_received_date": "乾隆五十一年十二月初九日亥刻",
  "quotation": "接據署臺灣府淡水同知程峻、竹塹營守備董得魁..."
}
```

### `responding_to_other_official_messages`

Use this field when the `上奏` is responding to, forwarding, or reporting a message from another official, such as a `稟`, `札`, `咨`, or reported message.

Include:

- whether the memorial is responding to another official message;
- sender of that original message;
- summary of the original message;
- original sent date, if available;
- received date, if available;
- quotation.

### `replying_to_previous_emperor_order`

Use this field when the memorial appears to respond to an earlier imperial order.

Include:

- whether it is replying to the emperor;
- summary of the original emperor order, if visible;
- emperor order sent date, if available;
- official received date, if available;
- quotation.

If there is no evidence, write `未明` rather than inventing a prior order.

### `emperor_rescript_inside_memorial`

Use this field to check whether the `上奏` record itself contains an emperor's `硃批`, rescript, or similar imperial reply embedded in the text.

This is separate from `replying_to_previous_emperor_order`:

- `replying_to_previous_emperor_order` records whether the official is answering an earlier imperial order.
- `emperor_rescript_inside_memorial` records whether the current `上奏` text contains a later/current imperial reply, such as `奉硃批`, `硃批`, `欽此`, or a parenthetical imperial comment.

Include:

```json
{
  "answer": "yes/no/unclear + explanation",
  "what_info_emperor_is_replying_to": "the specific report, claim, request, or situation in the memorial that the emperor's 硃批 addresses, or 未明",
  "rescript_summary": "summarize the emperor's reply if present, or 未明",
  "rescript_date": "date of the rescript if visible, or 未明",
  "quotation": "short quote proving the presence or absence of the rescript"
}
```

For `what_info_emperor_is_replying_to`, tie the emperor's reply back to the memorial content. For example, if the emperor writes `已有旨了`, identify the reported matter that already received an imperial order, not only the phrase `已有旨了`.

If there is no embedded 硃批 or imperial reply, write `no` and use a short quotation only if the absence can be tied to the document ending or metadata. Do not quote the whole ending merely to prove absence.

### `official_location_now`

Summarize where the official appears to be when writing or acting.

If the location is only inferred from office or route, mark the uncertainty.

### `military_actions_done_reported_by_officials`

List military actions that have already been carried out and are reported by the official in the document.

Do not put future plans here; use `planned_action` for intended, ordered, pending, or proposed action.

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

If the document reports no completed military action, use an empty list and explain the absence in `uncertainty` if important.

### `planned_action`

Summarize what the official says he will do next.

### `major_locations`

List major places found in the document and the situation at each place.

Each item should include:

```json
{
  "place": "彰化縣城",
  "situation": "遭林爽文匪徒攻陷竊踞。",
  "quotation": "彰城失陷"
}
```

## Quotation Rules

- Preserve original Chinese wording in Traditional Chinese.
- Provide quotations for every evidence-bearing field except `what_info_telling_emperor`.
- Keep quotations short.
- Do not quote large blocks when a short phrase proves the point.

## Common Errors

- Naming only one information source when the memorial contains several.
- Treating a reported official message as the memorial author's own eyewitness knowledge.
- Claiming the official is replying to an imperial order when the text only contains a later 硃批.
- Failing to check whether an `上奏` record contains an embedded imperial 硃批 or reply.
- Confusing an embedded/current 硃批 with a previous 上諭 being answered by the official.
- Mixing military actions already done with planned or proposed actions.
- Omitting major places such as 彰化、淡水、鹿仔港、府城、諸羅, or 鳳山.
- Confusing event location with author location.

## Related Outputs

- `outputs/attempt-002/stage1-shangzou-summaries-check5-gemini35-v2.json`
- `outputs/attempt-002/stage1-shangzou-summaries-check10-gemini35.json`
- `outputs/attempt-002/stage1-shangzou-summaries-check10.json`
