# Skill: 查相關上諭（±3日）

**Kind:** edict_match

## Website Prompt

When the selected document is itself an `上諭`, do not search nearby edicts.
Read this one `上諭` and return its distinct emperor comments and command
points, each with the exact quotation and the target official(s). A comment
may be attached to a reported event as information; a concrete command may be
added as an emperor-action event. Keep these two functions distinct.

## Purpose

For a memorial/rescript with a routine "已有旨" marker (or on demand), scans
every 上諭 within ±3 days and asks the AI which ones are actually responding
to it, with point-by-point evidence quotes from both sides. The proxy's
`edict_match` mode already has a full, tuned task description and JSON
schema; this skill file's Website Prompt is intentionally left empty for now
so both the terminal and website use the proxy's built-in default, exactly
as before. Write a standing default focus here later if you want one applied
to every run, not just a typed one-off question.

## Used By

- Website: AI 面板「動作」選單「查相關上諭（±3日）」, and the automatic
  已有旨 marker button (runEdictMatch)
- Terminal: `scripts/run_review_bundle_test.py --steps edict-match`
- Proxy: `gemini-proxy/main.py`, `mode: "edict_match"`, default value for
  field `question` when the user hasn't typed a live one
