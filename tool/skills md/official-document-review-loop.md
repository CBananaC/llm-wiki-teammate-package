# Skill: 官文優先 AI 審閱迴圈

**Kind:** official_document_loop

## Loop

Run this loop on one or more selected official documents (`奏摺`／`硃批`; not
on an `上諭`). Each document is the centre of the loop.

1. **摘要** — `quick-summary.md`.
2. **分段** — `divide-into-parts.md`.
3. **林方事件** — `extract-lin-actions.md`.
4. **清方行動（三類合一）** — one call to `extract-qing-actions-all.md`.
   Every returned event carries `done`, `plan`, or `nonmil`; do not run three
   independent Qing calls.
5. **重複回報 + 來源鏈（during steps 3-4）** — compare each new event with
   earlier extraction cards across documents, including different officials and
   different wording. Name the earliest report. Offer merge into the earliest
   event or keep separate. Trace every candidate's source chain in the same run.
6. **回應先前上諭** — follow only existing `official_reply_to_yu` pair records
   and run `confirmed-yu-response-analysis.md` to explain how the selected
   document responds. Do not search the corpus again.
7. **皇帝行動（硃批＋上諭）** — follow only existing `yu_source` records from
   the selected document to later `上諭`, then run
   `emperor-actions-confirmed-zhu-yu.md`. Merge semantically equivalent `硃批`
   and `上諭` expressions into one emperor action with multiple sources.
8. **重複皇帝行動** — compare the proposed action with earlier committed
   emperor actions; name the earliest equivalent action and offer merge or keep
   separate. The bundle records `merge_group`/`merge_title`; the review UI
   displays one primary card per merged action and unions its source quotes.
9. **官員回應** — for every extracted emperor action, take the union of the
   existing `official_reply_to_yu` records for its 上諭 sources and
   `official_reply_to_emperor_zhu` records for its 硃批 sources. Analyze only
   those fixed reply documents with the existing `official_response` card/UI.
   Do not run a 30-day corpus search.

The loop deliberately has no `回應時效`／`situfit` stage, and no date-based
edict search.

## Evidence rule

Pair JSON selects which documents participate; AI analyzes what the texts say.
AI must never create a new relationship edge during this loop. Missing confirmed
edges are reported as missing evidence, not replaced with a fresh search.
