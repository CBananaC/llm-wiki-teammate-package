# Skill: Extract 林方 Military Actions (with Source Evidence)

**Kind:** events
**Actor:** lin

## Website Prompt

Extract only actions actually performed by the 林爽文 side / rebels / anti-Qing forces. Do not extract Qing suppression, defence, troop dispatch, reporting, or official communication actions.

When the selected document is an `上諭`, apply the same action test, but
extract only actions which the emperor explicitly states that he knows about
through a report, memorial, or other stated information. The `上諭` date is
the emperor's knowledge date, not the action date. Quote the `上諭` wording
that conveys the reported action; do not turn the imperial order itself into a
林方 action.

## Purpose

Produces one event dot plus a highlighted quote on the source text for each
action Lin Shuangwen's side actually took. This text is a classification
rule layered on top of the proxy's built-in event-extraction task (episode
granularity, output schema, relation edges, etc.) — it only says *which*
actions count, not how to format or split them.

## Used By

- Terminal: `scripts/run_review_bundle_test.py --steps lin-events`
- Website: AI 面板「動作」選單中的林方行動擷取
- Proxy: `gemini-proxy/main.py`, `mode: "events"`, `actor: "lin"`,
  field `actor_instruction`

## Do Not Change Here

The event granularity rules and output JSON schema (subtitle, description,
where, who, relations, quote, etc.) live in the proxy's `events` mode and are
shared across actors/categories. The website additionally appends its own
fixed date-handling and relationship/GIS-field instructions after this
skill's text (see `extractEventProposals` in `stage1-timeline.html`).
Editing this skill only changes which actions get selected for the `lin`
actor, not the schema, granularity, or those fixed additions.
