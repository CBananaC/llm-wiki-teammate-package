# Skill: Divide Document Into Parts

**Kind:** divide

## Website Prompt

將上述『原文』依內容與功能切分為數個連續段落。對每一段給出：label（簡短的段落標題，如『情報來源』『軍事部署』『請旨』）、summary（一句繁體中文短摘要）、excerpt（該段的原文，盡量逐字節錄）。

## Purpose

Segments a document into labeled parts that get highlighted directly on the
original text in the info panel. Same instruction text whether triggered
from the terminal (large scan across many docs) or the website's
「分段標註」button (single doc, during review, to catch anything a large
scan missed).

## Used By

- Terminal: `scripts/run_review_bundle_test.py --steps divide`
- Website: per-document AI panel, 「分段標註」button
- Proxy: `gemini-proxy/main.py`, `mode: "divide"`, field `instruction`

## Do Not Change Here

The output JSON shape (`{"parts":[{"label","summary","excerpt"}]}`) is fixed
inside the proxy so the website's highlighter keeps working. This skill file
only controls the segmenting guidance above the JSON contract, not the
contract itself.
