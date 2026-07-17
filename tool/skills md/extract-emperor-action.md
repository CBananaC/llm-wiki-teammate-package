# Skill: 擷取皇帝行動（奏／諭）

**Kind:** emperor_action

## Website Prompt

## Purpose

For ONE selected document — a memorial with a vermilion rescript (奏摺／硃批)
or an imperial edict (上諭) — pull out the emperor's own action in a single
review card, then let the user add it to the timeline's 4th (帝行動) lane.

Unlike the `zhupi` skill (which scans a whole memorial for every inline/尾
rescript) or the `edict_match` skill (which searches ±3 days for edicts
responding to a memorial), this skill treats the selected document itself as
the carrier of the emperor's action and extracts it directly:

- 上諭 (edict): the edict IS the emperor's action. Subtitle from its title,
  description from its summary, quotation from its opening clause, and doc
  info (edict id, 受文者, 頒布日) from the record.
- 奏摺／硃批 (memorial + rescript): the emperor's action is the 硃批. Subtitle
  and quotation come from the rescript text, "回應" from the memorial's title,
  and doc info (具奏官員, 硃批日) from the record.

The extraction runs client-side from the record's own fields, so it needs no
proxy call and always produces a card. If you later want an AI-refined
subtitle/summary applied to every run, write a standing focus in the Website
Prompt above — it is passed through as `question` to `runEmperorAction`,
exactly as `extract-zhupi`'s prompt is passed to `runZhupi`.

The review card shows, per the request:
- subtitle (the emperor's action, one line)
- description (what he responded to / the gist)
- quotation (the emperor's own words, click to locate in the source text)
- doc info (source document, 具奏／受文, date)

"加入為皇帝行動" commits it as an `actor:'emperor'` event on the 4th lane via
the shared `commitEmperorAction` / `repairEmperorActionEvent` machinery, and
the done-state button opens the resulting event, mirroring the 硃批／上諭
cards.

## Used By

- Website: AI 面板「動作」選單「皇帝行動（奏／諭）」, and the `皇帝行動` chat
  shorthand token. Dispatches to `runEmperorAction()` in
  `stage1-timeline.html`.
- Proxy: none required (client-side extraction). A `question` focus written
  in the Website Prompt is threaded through for future AI refinement.
