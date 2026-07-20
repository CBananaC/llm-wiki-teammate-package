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

Routine markers such as `已有旨` or `另有旨` do not become invented standalone
actions. They may be retained only as a supporting source when a linked `上諭`
supplies the clearly corresponding substantive action.

Compare each proposed emperor action with earlier committed emperor-action
events supplied by the website. If the same concrete imperial action has already
appeared, return the earliest existing event id and its title. The review card
then offers either:

- combine the new sources into the earliest emperor action; or
- keep the new action as a separate event.

Cards use the existing `相關上諭` layout and preserve a clickable quotation and
document citation for every `硃批` and `上諭` source.

## Proxy

`tool/proxy/gemini-proxy/main.py`, mode `combined_emperor_actions`.

```json
{
  "actions": [
    {
      "title": "嘉許某官辦理妥善",
      "description": "",
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
