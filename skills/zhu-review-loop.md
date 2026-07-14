# Saved Prompt: 硃批 Period Review Loop

## Website Prompt

This is an orchestration skill for reviewing every `doc_type: "硃批"` selected
by the terminal runner. The runner supplies the date window and the exact
selected document IDs; do not choose, invent, or hard-code a time period in
this skill.

For each selected 硃批, run the existing skills in this order and keep each
stage as a separate reviewable output:

1. `quick-summary.md` — concise summary of the memorial and its context.
2. `divide-into-parts.md` — consecutive labeled sections with original-text
   excerpts.
3. `extract-lin-actions.md` — actions actually carried out by the 林方／rebels.
4. `extract-qing-actions-done.md` — Qing actions already carried out.
5. `extract-qing-actions-planned.md` — Qing actions planned, requested,
   ordered, or intended but not yet carried out.
6. `extract-qing-nonmilitary-actions.md` — non-military Qing administrative,
   legal, personnel, or communication actions when present.
7. `extract-zhupi.md` — every imperial 硃批, including 夾批 and 尾批, with its
   position, exact text, response target, opinion, title, and evidence fields.
8. `edict-match.md` — search nearby `上諭` records and retain only genuine
   responses to the selected 硃批. Preserve every matched point separately.
   Each point must distinguish the memorial quotation from the imperial
   quotation and explain the response.

The `edict-match` points are also the command review: concrete orders become
皇帝行動 candidates, while criticism, judgment, and reported information stay
separate. Do not turn an imperial command into a Qing-side action. The
website's existing `extract-emperor-action.md` behavior is used when the
reviewer adds a 硃批 or 上諭 finding to the fourth 皇帝行動 lane.

Use the exact original text supplied with each record. Preserve Traditional
Chinese quotations, document IDs, official names, and dates. If a stage finds
nothing, write an empty result for that document rather than skipping the
document. Do not merge results from different documents or silently replace a
previous stage's output.

The terminal runner writes the standard loadable files:

- `summary.json`
- `division-parts.json`
- `lin-events.json`
- `qing-events-done.json`
- `qing-events-plan.json`
- `qing-events-nonmil.json`
- `zhupi.json`
- `edict-match.json`

The bundle manifest records the supplied date window and selected 硃批 IDs.

## Purpose

Run the existing single-document skills as one reproducible loop over all
硃批 records in a terminal-supplied date range. This keeps the period out of
the durable skill prompt so the same skill can be reused for any interval.

## Terminal Entry Point

```bash
python3 scripts/run_zhu_review_loop.py \
  --proxy https://example-proxy \
  --date-from 1786-12-01 \
  --date-to 1786-12-31
```

Use `--date-mode any` when the range should include a 硃批 if either its
上奏日 or 硃批／收受日 falls inside the window. The default `primary` mode
uses the 硃批／收受日 first, then the 上奏日.
