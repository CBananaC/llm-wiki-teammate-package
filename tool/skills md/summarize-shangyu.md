# Skill: Summarize 上諭 Records

## Website Prompt

Summarize this 上諭 record for the timeline reviewer. State: what report/memorial
the emperor is responding to (source_actor, message_summary, or 未明 if not
named), the emperor's opinion/judgment of the situation, his command and its
target(s), and the major locations mentioned with the situation at each. Use
announce_date, not send_date or receive_date. Note the transmitting official
(the 字寄 formula) separately from the command's target. Quote briefly (short
phrases, not long blocks) to support each field. Flag anything uncertain.

## Purpose

Use this skill to summarize Qing `上諭` records from the 林爽文事件 corpus into structured, evidence-based JSON.

This skill is designed for Stage 1 research, but the schema can be reused for later stages if the source JSON follows the same date and metadata conventions.

## When To Use

Use this skill when the task asks to summarize `doc_type: "上諭"` records, especially from:

- [[corpora/lin-shuangwen-first-hand-json]]
- `outputs/attempt-002/stage1_original_text.json`

## Input Requirements

Each input record should preserve:

- `doc_id`
- `series`
- `doc_type`
- `author`
- `title`
- `announce_date`
- `body`

The `announce_date` value should be a pair:

```json
["乾隆五十二年一月十三日", "1787/01/13"]
```

Use `announce_date` for `上諭`. Do not substitute `send_date`, `receive_date`, or `issue_date` unless the source record has not yet been normalized; if a non-normalized field is used, mark that clearly in `uncertainty`.

## Output Layout

Use a nested layout so documents are easy to distinguish:

```json
{
  "doc_id": "天43",
  "source_record": {
    "series": "天地會",
    "doc_type": "上諭",
    "author": {
      "position": null,
      "name": "孫士毅"
    },
    "title": "諭兩廣總督孫士毅毋庸親往潮州",
    "yu_written_by": {
      "answer": "大學士公阿桂、大學士和珅字寄兩廣總督孫士毅",
      "quotation": "大學士公阿桂、大學士和珅字寄兩廣總督孫士毅"
    },
    "announce_date": ["乾隆五十二年一月十三日", "1787/01/13"]
  },
  "analysis": {
    "key_info": "...",
    "responding_to_message": {},
    "emperor_opinion": {},
    "emperor_command": {},
    "major_locations": [],
    "uncertainty": "..."
  }
}
```

## Required Analysis Fields

### `key_info`

Summarize, without direct quotation, the main situation, report, or problem the emperor is addressing.

### `responding_to_message`

Use this field when the `上諭` responds to a memorial, report, consultation, confession, previous communication, or other named information source.

Include:

```json
{
  "answer": "What report/message/memorial the emperor is responding to, or 未明",
  "source_actor": "who sent or supplied the message, if visible",
  "message_summary": "...",
  "message_sent_date": "date of original message if visible, or 未明",
  "emperor_received_or_responded_date": "date emperor is responding/announcing, if visible",
  "quotation": "據孫士毅奏..."
}
```

Do not assume that every `上諭` responds to one memorial only. If several reports or information channels are named, list them in the summary and preserve the important distinctions.

### `emperor_opinion`

Summarize the emperor's judgment, criticism, approval, concern, or interpretation of the reported situation.

Include:

```json
{
  "summary": "...",
  "quotation": "short quote showing the emperor's opinion"
}
```

### `emperor_command`

Summarize what the emperor orders to be done.

Include:

```json
{
  "summary": "...",
  "target": "official, office, or group receiving the command",
  "quotation": "著傳諭..."
}
```

If the command has multiple targets, preserve them instead of collapsing everything into one generic command.

### `major_locations`

List major places found in the document and the situation at each place.

Each item should include:

```json
{
  "place": "潮州",
  "situation": "孫士毅原擬親赴此地，皇帝命其毋庸前往。",
  "quotation": "潮州現有彭承堯在彼"
}
```

### `yu_written_by`

Record the opening transmission formula when visible, especially patterns such as `大學士...字寄...奉上諭`.

This field is not the same as the emperor's command target:

- `yu_written_by` records the transmission/writing channel.
- `emperor_command.target` records who is being ordered or informed.

If the transmission formula is missing, write `未明` and explain the missing evidence in `uncertainty`.

## Quotation Rules

- Preserve original Chinese wording in Traditional Chinese.
- Provide quotations for every evidence-bearing field except `key_info`.
- Keep quotations short.
- Do not quote large blocks when a short phrase proves the point.

## Common Errors

- Using `send_date` or `receive_date` for `上諭` after the corpus has normalized the field to `announce_date`.
- Treating the transmitting 大學士 as the same as the target official.
- Collapsing several command recipients into one target.
- Summarizing the order but omitting the emperor's opinion or criticism.
- Treating a reported memorial as eyewitness fact without marking that the emperor is responding to a report.
- Dropping key locations such as 臺灣、潮州、南澳、府城、彰化、鹿仔港、諸羅, or 鳳山 when they shape the order.
- Confusing `上諭` records with `上奏` records that merely say the official has received an 上諭.

## Related Outputs

- `outputs/attempt-002/stage1-shangyu-summaries-check5-gemini35.json`
