# Skill: Quick Document Summary

**Kind:** summary

## Website Prompt

用繁體中文，為上述文書寫一段更精簡、流暢的摘要（約 3-5 句），突出最關鍵的人、事、時、地，避免逐句翻譯。

## Purpose

Fast, generic prose summary of any single document (上奏／硃批／上諭). This is
the *same* instruction used both by the terminal batch runner's `summary`
step and by the website's 「進一步摘要」button — one skill file, one prompt,
two ways to trigger it (large scan on many docs from the terminal, or a
single doc from the website when reviewing).

This is intentionally a lighter, non-schema summary. For the richer
per-doc-type structured analysis (with quoted evidence per field), use
`summarize-shangyu.md` / `summarize-shangzou.md` / `summarize-zhupi.md`
instead — those are a separate, more detailed skill family.

## Used By

- Terminal: `scripts/run_review_bundle_test.py --steps summary` (reads this
  file's Website Prompt and sends it as the `instruction` field)
- Website: per-document AI panel, 「進一步摘要」button
- Proxy: `gemini-proxy/main.py`, `mode: "summary"`, field `instruction`
  (falls back to its own default text if this field is empty)
