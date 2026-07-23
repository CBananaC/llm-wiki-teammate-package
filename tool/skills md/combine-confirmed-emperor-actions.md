# Skill: 合併硃批與已配對上諭為皇帝行動

**Kind:** combined_emperor_actions

## Purpose

For one selected official document, combine the emperor's own action expressed
in its `硃批` with the emperor's own action expressed in `上諭` already linked to
that document by `yu_source` records. Do not search all `上諭`.

Only output the emperor's comment, reply, praise, blame, approval, rejection,
question, or command. An `上諭`'s relayed `據…奏` intelligence is context, not an
emperor action. If a `硃批` and an `上諭` express the same action in different
wording or person (for example `汝辦理甚好` and `某官辦理甚好`), output one
action with both documents as sources. Keep substantively different actions
separate.

The selected memorial is the relevance boundary. A `yu_source` link only makes
an 上諭 eligible as a source; it does not make every command in that 上諭 a
response to the memorial. Judge each action semantically as `direct`,
`contextual`, or `unrelated`; emit only `direct`. A contextual action may be
genuinely related to the same incident or 上諭 network while responding to a
different memorial, official, or problem, and must still be omitted. This is
not an exact-quote or simple name-matching test. Return a one-sentence
`relevance_reason`; an exact memorial quotation is optional.

Routine markers such as `已有旨` or `另有旨` do not become invented standalone
actions and are not listed as an action source. If a linked `上諭` supplies the
clearly corresponding substantive action, list the `上諭` source only.

Compare each proposed emperor action with earlier committed emperor-action
events supplied by the website. If the same concrete imperial action has already
appeared, return the earliest existing event id and its title. The review card
then offers either:

- combine the new sources into the earliest emperor action; or
- keep the new action as a separate event.

Cards use the existing `相關上諭` layout and preserve a clickable quotation and
document citation for every `硃批` and `上諭` source.

Each returned `title` is the subtitle of one concrete action, not the title of
the whole linked 上諭. If one 上諭 contains several commands, give every point
its own specific title naming its object and action; never repeat a generic
`諭閩浙總督…` wrapper title for unrelated points. Keep `same_as_event_id` only
for an exact same action, not merely the same 上諭, official, or broad topic.

## Proxy

`tool/proxy/gemini-proxy/main.py`, mode `combined_emperor_actions`.

```json
{
  "actions": [
    {
      "title": "嘉許某官辦理妥善",
      "description": "",
      "memorial_relation": "direct|contextual|unrelated",
      "relevance_reason": "",
      "action_type": "comment|reply|praise|blame|approve|reject|question|command",
      "whenCh": "",
      "whenAr": "",
      "where": "",
      "who": [],
      "who_loc": {},
      "relations": [],
      "same_as_event_id": "",
      "sources": [
        {"doc_id": "硃…", "source_type": "硃批", "quote": "", "title": "", "date": ""},
        {"doc_id": "諭…", "source_type": "上諭", "quote": "", "title": "", "date": ""}
      ]
    }
  ]
}
```

Never name a `same_as_event_id` outside the supplied earlier-action registry.
