# Skill: Extract 清方軍事行動（已執行）

**Kind:** events
**Actor:** qing
**Category:** done

## Website Prompt

Extract only Qing (official/army) military or security actions that were ACTUALLY CARRIED OUT / already executed (engagements, troop movements done, captures, defences mounted). Exclude actions that are merely planned/requested/ordered-but-not-done, exclude pure reporting, and do not extract rebel actions.

When the selected document is an `上諭`, extract only completed Qing actions
which the emperor explicitly states that he knows about through a report,
memorial, or other stated information. The `上諭` date is the emperor's
knowledge date, not the action date. Do not extract the emperor's own command
as a Qing action.

## Purpose

Companion to `extract-lin-actions.md`, but for the Qing side's already-executed
military/security actions. Same mechanism: this is a classification rule
layered on the proxy's shared `events` task; granularity, schema, date
handling and the relationship/GIS fields are fixed in code (see
`extractEventProposals` in `stage1-timeline.html`), not editable here.

## Used By

- Website: AI 面板「動作」選單「擷取清方軍事行動（已執行）」
- Terminal: `tool/scripts py/run_review_bundle_test.py --steps qing-events-done`
- Proxy: `tool/proxy/gemini-proxy/main.py`, `mode: "events"`, `actor: "qing"`,
  `category: "done"`, field `actor_instruction`
