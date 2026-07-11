# Skill: Extract 硃批（皇帝批示）

**Kind:** zhupi

## Website Prompt

## Purpose

Finds every vermilion rescript (硃批) in a document — both inline (夾批) and
end-of-document (尾批) — with what each responds to and the emperor's view.
The proxy's `zhupi` mode already has a full, tuned task description and JSON
schema; this skill file's Website Prompt is intentionally left empty for now
so both the terminal and website use the proxy's built-in default, exactly
as before. If you ever want a standing default focus/refinement applied to
every run of this skill (not just a one-off typed question), write it here —
it's passed through the existing `question` field alongside (or in place of)
whatever the user types live.

## Used By

- Website: AI 面板「動作」選單「擷取硃批（皇帝批示）」
- Terminal: `scripts/run_review_bundle_test.py --steps zhupi`
- Proxy: `gemini-proxy/main.py`, `mode: "zhupi"`, default value for field
  `question` when the user hasn't typed a live one
