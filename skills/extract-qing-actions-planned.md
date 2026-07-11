# Skill: Extract 清方軍事行動（待執行）

**Kind:** events
**Actor:** qing
**Category:** plan

## Website Prompt

Extract only Qing (official/army) military or security actions that are PLANNED, ordered, requested, proposed, or intended but NOT yet actually carried out (e.g. an official memorialising to request troops, ordering a commander to proceed, proposing to attack on a future date, preparing/擬於某日出兵). Do NOT extract actions already executed, and do not extract rebel actions.

When the selected document is an `上諭`, keep only a reported Qing plan that
the emperor explicitly says he knows about. Do not mistake a new command in
the `上諭` for a previously reported Qing plan; imperial commands belong to
the emperor-action review.

## Purpose

Companion to `extract-qing-actions-done.md`, but for actions that are only
planned/ordered/requested — not yet carried out. Same shared `events` schema
and granularity rules apply; only the classification judgment lives here.

## Used By

- Website: AI 面板「動作」選單「擷取清方軍事行動（待執行）」
- Terminal: `scripts/run_review_bundle_test.py --steps qing-events-plan`
- Proxy: `gemini-proxy/main.py`, `mode: "events"`, `actor: "qing"`,
  `category: "plan"`, field `actor_instruction`
