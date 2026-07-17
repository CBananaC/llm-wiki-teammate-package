# Skill: Hide Duplicate 上奏 Dots

**Kind:** local_dedupe

## Website Prompt

Find records that appear on the same chart date and whose original text is nearly identical despite different titles or document types. For each near-duplicate pair, hide the repeated dot whose document type is 上奏, keeping the non-上奏 record visible for review.

## Purpose

Use this website-only skill to clean the timeline view when a `上奏` and another record, often a `硃批`, preserve almost the same memorial text on the same date. The action does not delete data. It adds the repeated `上奏` record ID to the reversible hidden-dot list.

## Used By

- Website: AI 面板「動作」選單中的「隱藏重複上奏點」 (`duplicateShangzouPairs()` /
  `runHideDuplicateShangzou()` in `stage1-timeline.html`) — produces reviewable
  cards with per-pair 隱藏/keep buttons; only this path can actually hide a
  dot, since the reversible hidden-dot list lives in the browser.
- Terminal: `python3 "tool/scripts py/find_duplicate_shangzou.py"` — read-only report of
  the same candidate pairs, for reviewing/triaging from the command line
  before opening the website. Does not modify any data or hide anything.

## Matching Parameters

Both entry points use the same three parameters, and must be kept in sync if
tuned: date window ±3 days (a 上奏's send date and its 硃批 counterpart's
receive date are naturally offset by mail travel time), text similarity
(Dice coefficient over 8-character shingles) >= 0.72, length ratio >= 0.4.

## Notes

- This is deterministic local text comparison, not an LLM extraction prompt —
  no proxy or network call is involved on either the website or terminal side.
- Hidden records can be restored from the existing `隱藏清單` (website only;
  the terminal script never touches the hidden-dot list).
