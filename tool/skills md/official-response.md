# Skill: 搜尋官員回應（未來30日）

**Kind:** official_response

## Website Prompt

## Purpose

For one 硃批/諭/皇帝行動事件, scans documents dated in the ~30 days AFTER it
and asks the AI which one is the addressed official's actual response --
with quote-level evidence on both sides (the action's own quote, and the
response document's explicit acknowledgement of it). The proxy's
`official_response` mode already has a full, tuned task description and
JSON schema (including `where`/`who`/`who_loc`/`relations`, used for the
human relation graph and GIS map -- shown only in the resulting event's own
info panel, never on the chat card); this skill file's Website Prompt is
intentionally left empty for now so both the terminal and website use the
proxy's built-in default. Write a standing default focus here later if you
want one applied to every run, not just a typed one-off question.

Candidates are narrowed to the addressed official first (by the source
record's own `author_name`/`recipients` field) whenever a name is known,
and capped/sorted by closeness to the action's date -- a bare 30-day window
on a dense corpus can otherwise pull in 100+ unrelated documents and bury
the real response in noise (see `officialResponseCandidates()` in
stage1-timeline.html / `official_response_candidates()` in
`run_review_bundle_test.py`, kept in sync).

The official-document review loop uses a stricter pair-grounded variant of this
same analysis and card UI. In that variant, candidates are supplied only by
existing `official_reply_to_yu` records for the loop's paired `上諭`, and the
proxy receives `confirmed_pairs_only: true`. It analyzes how those already
confirmed documents respond; it does not run the 30-day candidate search or
re-decide whether the relationship exists.

## Used By

- Website: AI 面板「動作」選單「搜尋官員回應（未來30日）」, the
  `@官員回應` chat shorthand, and the "🔍 搜尋官員回應" button inside a
  committed emperor-action event's own info panel
- Terminal: `tool/scripts py/run_review_bundle_test.py --steps official-response`
  (run after `zhupi`/`edict-match` have produced candidates for the same
  docs, either earlier in the same run or in a previous one)
- Proxy: `tool/proxy/gemini-proxy/main.py`, `mode: "official_response"`

## Output shape and linking (terminal/bundle path)

`run_review_bundle_test.py` writes one row per action (硃批 item or 諭
point) to `outputs/official-response.json`:
`{"doc_id": "<action's own source doc>", "evTitle": "<action title>",
"addressee": "...", "items": [...]}`.

Loading a bundle that contains this file does **not** show it as its own
chat card -- unlike `source-chain.json`, these rows are matched (by source
doc + title/subtitle similarity) against the zhupi/edict-match candidates
loaded from the SAME bundle and attached as `it.__pendingResponses` /
`pt.__pendingResponses` (see `linkOfficialResponses()` in
stage1-timeline.html). The moment a candidate is actually committed as an
emperor-action event (the existing `.zp-addact`/`.em-addact` buttons),
those pending responses move onto the new event's `__suggestedResponses`,
so they show up right there in its info panel -- exactly like a live
"🔍 搜尋官員回應" search would, just already sitting there. Anything left
on a candidate nobody committed is discarded with it, never persisted on
its own -- mirroring the same "don't keep info for events not considered"
rule the source-chain linking already follows.
