# Skill: 上諭中皇帝所知的林／清事件＋來源追溯

**Kind:** yu_reported_events

## Purpose

For one `上諭`, extract the 林方 and 清方 events the **emperor states he knows
through reports** — historical events he learned of, NOT battlefield fact and NOT
new actions dated to the edict. For each event, trace it back to the memorial(s)
that reported it to the emperor, using ONLY the documents supplied from the
existing `yu_source` network (the memorials this 上諭 was drawn from). This
replaces the official-doc loop's full local→military→official information chain
with a single "who told the emperor, in which doc" attribution.

The proxy `yu_reported_events` mode carries the full task; this file's Website
Prompt is a short focus note appended on top, so you can nudge behaviour without
editing the proxy.

## Website Prompt

```text
只擷取本上諭中『皇帝透過奏報得知』的既往林方（side=lin）與清方（side=qing）事件，非上諭發布日的新行動；清方每條標 category（done|plan|nonmil）。每條給 edict_quote（上諭逐字）。來源只在所給候選奏摺／硃批中比對：列出所有支持該事件的候選為 source_documents，標 relation（direct｜corroborating｜relay）與逐字 source_quote，且候選收受日須早於上諭日；無則留空。不得杜撰來源或重建未載的傳遞鏈。
```

## Used By

- Terminal: `tool/scripts py/run_yu_loop.py` (one call per 上諭, all actors + source).
- Proxy: `tool/proxy/gemini-proxy/main.py`, `mode: "yu_reported_events"`.

## Output (per event)

`side`, `category` (qing only), `subtitle`, `description`, `where`, `who`,
`who_loc`, `whenCh`, `whenAr`, `edict_quote`, and `source_documents[]`
(`source_doc_id`, `relation`, `source_official`, `source_send_date`,
`source_receive_date`, `source_quote`). The loop keeps only source_doc_ids that
were actually supplied from the `yu_source` network.
