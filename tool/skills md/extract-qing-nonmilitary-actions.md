# Skill: Extract 清方非軍事行動

**Kind:** events
**Actor:** qing
**Category:** nonmil

## Website Prompt

Extract only NON-military actions actually taken by Qing officials/government — administration, pacifying the populace/安撫民番, relief/賑濟, interrogating captives/審訊, provisioning and finance/籌餉, personnel and appointments/人事, aftermath/善後, and official measures that are concrete acts (not mere reporting). Exclude military attack/defence/troop-movement combat actions, and exclude rebel actions.

When the selected document is an `上諭`, keep only completed non-military
Qing measures that the emperor explicitly says he knows about. Do not extract
the emperor's own new command, award, or criticism as a prior Qing action.

## Purpose

Companion to the two military-action skills, but for the Qing side's
non-military governance actions (administration, relief, aftermath, etc.).
Same shared `events` schema and granularity rules apply; only the
classification judgment lives here.

## Used By

- Website: AI 面板「動作」選單「擷取清方非軍事行動」
- Terminal: `tool/scripts py/run_review_bundle_test.py --steps qing-events-nonmil`
- Proxy: `tool/proxy/gemini-proxy/main.py`, `mode: "events"`, `actor: "qing"`,
  `category: "nonmil"`, field `actor_instruction`
