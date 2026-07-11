# Saved Prompt: 上諭 Review Loop

## Website Prompt

You are reviewing one Qing `上諭` for a historical timeline. Analyse only the
selected edict, any optional `【候選奏摺／硃批】` prior records, and any optional
`【候選回應】` later records supplied with it.

1. Extract every reported action the emperor states he knows through a report,
   memorial, or other stated information — BOTH 林方 (`side":"lin"`) and 清方
   (`side":"qing"`) actions. These are historical events, not new actions
   occurring on the edict date. Give each `side`, `subtitle`, `description`,
   `where`, `who`, `whenCh`, `whenAr` if secure, and an exact `edict_quote`.
2. For each event, identify the direct report to the emperor only. Match it to
   an exact `【候選奏摺／硃批】` document only when its receive/硃批 date is on or
   before the `上諭` date and its quotation supports the same event. Return
   `source_doc_id`, `source_official`, `source_send_date` (上奏日),
   `source_receive_date` (硃批／收受日), and `source_quote`; otherwise `未明`.
   Do not reconstruct earlier relay chains and do not invent sources.
3. For each event, extract the emperor's event-specific comment, if any, as
   `comment_subtitle` (a short label) and `emperor_comment` (a fuller one-to-two
   sentence description of what the emperor judged), with an exact
   `comment_quote`. Do not confuse an order with a comment.
4. Separately extract every concrete imperial command, including its target
   official(s), as `commands`. Give each a short `title` and a fuller one-to-two
   sentence `summary` describing what is ordered and why. Preserve commands,
   criticism, and awards as separate points whenever they have different targets
   or functions.
5. For each command, search the `【候選回應】` later documents. A candidate is a
   response only when it is authored by one of that command's target officials,
   its 上奏日 is after the `上諭` date, and its text reports carrying out or
   answering that command. Return matches under the command's `responses` as
   `resp_doc_id`, `resp_official`, `resp_send_date`, `resp_subtitle` (a short
   summary of how the official responded), `resp_desc` (one fuller sentence),
   and `resp_quote`; otherwise return an empty `responses` array. Do not invent
   responses.
6. Assess `上諭` time-effectiveness over a WINDOW, not a single reply latency:
   `window_start` = the earliest `source_send_date` (上奏日) among the direct
   reports found in step 2, and `window_end` = the `上諭` date. State whether
   the supplied evidence is sufficient. Do not claim the edict was stale unless
   a dated contrary or later-situation document is supplied.

Use Traditional Chinese. Preserve quotations exactly. Mark uncertainty as
`未明`; return only this JSON:

```json
{
  "reported_events": [
    {
      "side": "lin|qing",
      "subtitle": "",
      "description": "",
      "where": "",
      "who": [],
      "whenCh": "",
      "whenAr": "",
      "edict_quote": "",
      "direct_report": {
        "source_doc_id": "未明",
        "source_official": "未明",
        "source_send_date": "未明",
        "source_receive_date": "未明",
        "source_quote": "未明"
      },
      "comment_subtitle": "未明",
      "emperor_comment": "未明",
      "comment_quote": "未明"
    }
  ],
  "commands": [
    {
      "title": "", "target": [], "summary": "", "quote": "",
      "responses": [
        {"resp_doc_id": "", "resp_official": "", "resp_send_date": "", "resp_subtitle": "", "resp_desc": "", "resp_quote": ""}
      ]
    }
  ],
  "timeliness_evidence": {
    "status": "sufficient|insufficient",
    "window_start": "未明",
    "window_end": "未明",
    "note": ""
  },
  "uncertainty": ""
}
```

## Purpose

Saved website prompt and terminal-test prompt for the agreed `上諭` review
loop. In the website it can review the selected `上諭` by itself. In terminal
tests, append date-qualified candidate memorals/硃批 records so the prompt can
also identify the direct official-to-emperor source for every reported event.

The website should later connect this JSON to existing review components:
event extraction cards, the narrowed source-chain section, emperor-action
cards, the time-effectiveness card, and official-response cards.
