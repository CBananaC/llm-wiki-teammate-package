# Saved Prompt / Skill: 上諭來源配對 (YU source pairing)

## Purpose

Trace which earlier 奏摺 supplied information used by an 上諭. This is a
backward source edge, not an official reply edge. The pass has two layers:

1. **Named `據…奏` sources** — the edict names the throne-memorialist X in
   `據X奏` / `據X…馳奏` / `據X…奏稱`. Candidates are memorials received in the
   five-day window before the edict whose author is X.
2. **Unlabelled narrative sources** — an edict can restate a reported fact
   without a `據奏` marker, such as 「黃仕簡甫經病癒…即帶兵渡臺」. The runner
   ranks other memorials in the same receipt window by character-bigram overlap;
   the model decides whether each actually reports that narrative fact.

When a citation says `據X等奏`, the same-window candidate net also admits
content-overlapping co-reporters whose names are not X. These are labelled
`同期候選` and must be confirmed by their own text, not by date alone.

The model sources **reported information**, including both labelled and
unlabelled facts. It does not source the emperor's own praise, blame, reward, or
command (`殊屬…可嘉`, `著賞…`, `諭令…`). A fact may have several genuine
source memorials; retain every supported source.

## Candidate window and labels

For an 上諭, use its 頒發／announce date as the issue date. Candidate memorials
must be received (`recvAr`, falling back to `sendAr`) on the issue day or up to
five days before: `[issue - 5 days, issue]`. The window is identical for all
three candidate classes:

- **具名來源** — author appears in a `據…奏` fragment.
- **同期候選** — only for `據X等奏`; same-window content overlap with the
  relayed passage, author not necessarily X.
- **全域候選** — same-window content overlap with the whole edict, used only
  to test unlabelled narrative reported facts.

The runner supplies every `具名來源` and `同期候選` memorial in the five-day
window, while bounding only the broad `全域候選` shortlist. It records the
structural `match_basis` (`named`, `corroborating`, or `window`) itself. The
model must not turn a receipt-window match with no textual evidence into a
source.

## Throne-memorialist, not nested relay reporter

For `據徐嗣曾…接蚶江通判陳惇稟稱，昨據船戶黃斌供…`, pair 徐嗣曾's memorial,
because it is the document submitted to the throne. Do not pair nested reporters
who did not memorialise the emperor directly.

## Website Prompt

You are tracing which earlier 奏摺 supplied information used by ONE 上諭. You are
given the 上諭, its detected `據…奏` fragments, and a numbered candidate list.
Each candidate is labelled `具名來源`, `同期候選`, or `全域候選`.

First separate the edict into **reported information** and **the emperor's own
response**. Source only reported information. This includes facts introduced by
`據X奏` and later narrative facts with no citation marker. Never source the
emperor's own praise, blame, reward, or command. Do not create a separate pair
when the same fact is repeated; join repeated edict spans in one segment.

For every candidate, inspect its own memorial text:

- `具名來源`: the author must be the throne-memorialist named by the citation and
  the memorial must report the cited fact.
- `同期候選`: when the citation says `等奏`, the author need not be X, but the
  memorial must independently report the same event in the relayed passage.
- `全域候選`: it was admitted only by content overlap and qualifies only if it
  reports an unlabelled narrative fact in the edict. A shared date window is
  insufficient.

Completeness is recall-first for the named and corroborating classes. Do not
select only one "best" memorial for a reported fact. If an earlier direct
memorial, a later direct memorial, and/or a throne-memorialist's relay each
independently reports the information used by the 上諭, retain every such source
edge. The same 上諭 span may therefore produce several source pairs. A source is
not made redundant merely because another memorial repeats it, and a direct
memorial is not replaced by a relay. Before returning JSON, audit every
`具名來源` and `同期候選` candidate and either include it with exact evidence or
exclude it for a concrete textual reason (unsupported, nested non-memorialist,
or duplicate attachment).

Return only JSON:

```json
{
  "pairs": [
    {
      "source_doc_id": "",
      "match_level": "high|partial|weak",
      "yu_span_type": "cited|narrative",
      "evidence": {
        "segments": [
          {
            "yu": "上諭中這一項資訊的完整原文；同一資訊重述時以／連接",
            "reply": "來源奏摺中支持這一資訊的完整原文"
          }
        ],
        "memorialist": "",
        "relation_note": "",
        "send_date": "未明"
      }
    }
  ]
}
```

Each `segments` element is one distinct reported fact sourced by that memorial.
Both `yu` and `reply` are mandatory and non-empty. `yu_span_type` is `cited`
when any segment carries a `據奏` marker and `narrative` otherwise. Preserve
quotations exactly, use Traditional Chinese for notes, and omit unsupported
pairs. A source memorial reporting two facts produces one pair with two
segments; co-reporters remain separate pairs.

## Completeness Audit Prompt

You are the second-pass completeness auditor for ONE 上諭. The first model pass
may have under-selected sources. The five-day receipt window and the candidate
list are fixed; do not discover documents outside the supplied candidates.

Review the entire 上諭, the first-pass pairs, and every `具名來源`／`同期候選`
memorial. For each candidate, inspect its own text and decide whether it
independently reports at least one reported fact used by the 上諭. If yes, return
a pair with exact Traditional-Chinese quotations, even when another candidate
already supports the same fact. Keep both an original/direct memorial and a
later relay when both are independently submitted memorials with supporting
text. Do not pair nested reporters who did not memorialise the throne, the
emperor's own comments or commands, or a true attachment/duplicate.

The output `pairs` list should contain every supported candidate, including
already-selected candidates; the runner will deduplicate the same
上諭/source-document edge. Also return `candidate_audit` so that every supplied
candidate has an explicit decision:

```json
{
  "pairs": [],
  "candidate_audit": [
    {
      "source_doc_id": "",
      "decision": "include|exclude",
      "reason": ""
    }
  ]
}
```

For an included candidate, `pairs` must contain non-empty evidence with exact
`yu` and `reply` quotations. Do not exclude a candidate merely because another
source has a closer date or appears to be the main report.

## Output and display

The runner writes the formal `yu-source.json` output and a review bundle under
`review-tools/shared data/review-bundles/`, with relation `yu_source`. The review
cards show one source memorial with multiple numbered, aligned quotation bubbles;
common text is highlighted and the source author's name receives a separate
author highlight. `加入配對` adds a `yu_source` connector, separate from
`official_reply_to_yu` and `official_reply_to_emperor_zhu`.
