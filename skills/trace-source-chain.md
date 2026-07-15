# Skill: Trace Source / Provenance Chain

**Kind:** source-chain

## Website Prompt

每個 hop 的日期（whenCh）請填「發送方（from_person）實際發出／稟報此消息的日期」，不要填「接收方收到的日期」。例如原文「十二月三十日戌刻，接據臺灣道永福十二月十四日來稟」中，永福→常青這個 hop 的 whenCh 應為永福發稟的「十二月十四日」，而非常青接據的「十二月三十日」。日期一律用原文的中曆（如「十二月十四日」）逐字填入 whenCh；西曆換算交由系統處理，不要自行換算。

For an event extracted from an `上諭`, use the narrowed `皇帝得知` form of
this function. Find only the final evidenced link, `official → emperor`: the
official's exact memorial/硃批 record, its supporting quotation, and its
receive/硃批 date. The date must be on or before the selected `上諭` date.
Do not reconstruct earlier relays unless the researcher explicitly asks for a
full provenance chain. If no qualifying document exists, return no chain;
never infer an unnamed report. Also return the selected `上諭` quotation in
which the emperor comments on this particular event, if present.

## Extraction rules (mirrored in the proxy `trace` task)

These are documented here so the human-readable criteria stay visible; the live
instructions are enforced in `gemini-proxy/main.py` `mode:"trace"`.

- **Connect into one unbroken chain.** Every hop must link A→B→C→…→document
  author. Each relay person has both an incoming and an outgoing hop; only the
  original source lacks an incoming hop, and only the document's author lacks an
  outgoing hop. If 甲 relays to 乙 who relays to 丙, output *both* 甲→乙 and 乙→丙
  — never drop the middle link, or a mid-chain person is wrongly rendered as
  「第一手」/「撰文者」.
- **Relay-verb direction (do not reverse).** 「甲字寄乙」「甲咨乙」「甲移會乙」
  「甲行乙／行據乙」 = 甲→乙. 「據X稟」「准X咨」「奉X諭／行」「接據X」 =
  X→the official quoting that clause. Unwind nested citations layer by layer
  (e.g. 「據A稟稱：准B咨，奉C行據D稟報」 = D→C→B→A→author; 「彰邑大肚社番字寄淡屬大甲社通事，據稱…」
  = 彰邑大肚社番→淡屬大甲社通事→淡水同知).
- **No assumed 親歷.** Only mark 親見／目擊／親歷／在場 when the text explicitly
  says so; otherwise `how` is the actual transmission verb (稟報／字寄／轉述…).
- **Keep all co-named reporters.** A joint report (e.g. 「淡水同知程峻、北路竹塹營守備董得魁稟報」)
  must list every named person in that hop's `from_person` — never drop one.
- **Names only from the text.** Use only the title/name as written; if the source gives just a
  title (「福建巡撫」) with no name, keep the title — never supply a name from outside knowledge
  (no 「福建巡撫徐嗣曾」).
- **Places only from the text.** `place`/`who_loc` come only from the source; don't place a person
  by where you know they served (a Fujian 巡撫 is not in 臺灣; 大甲社通事 is at 大甲社, not 大肚社).
- **`inferred` = an inferred *link* only.** If both people and the transmission are stated, it is
  `inferred:false` even when the date is missing; don't mark a named person inferred.
- **Don't invent middle dates.** A hop's `whenCh` is only a date the text states for that hop;
  otherwise leave it blank — never copy a neighbouring hop's date.
- **Preserve vague dates.** Keep 「十一月初間」/「月底」 verbatim in `whenCh`; don't collapse to one day.
- **Quotation display.** The website reconstructs one continuous verbatim passage
  from the original document body spanning all of a chain's quote fragments, so
  the whole relay reads as a single paragraph rather than disjoint clauses.

## Purpose

Reconstructs how an event's information reached the document's author —
hop by hop, from whoever first witnessed it to the official who wrote it
down. The proxy's `trace` mode already has a long, carefully tuned set of
instructions whose whole point is to avoid inventing unnamed sources
("農民乙" etc.) that aren't actually in the text, so this skill intentionally
does not try to override that core logic.

This file exists mainly so 「source-chain」shows up as a normal, enumerable
step alongside `summary` / `divide` / `lin-events`, and so any *additional*
one-off focus text (e.g. "只看某個地點的鏈") has a single place to be edited
if you ever need to add one, via the Website Prompt above.

## Used By

- Terminal: `scripts/run_review_bundle_test.py --steps source-chain`
- Website: 事件卡片中的「來源鏈追溯」
- Proxy: `gemini-proxy/main.py`, `mode: "trace"`, optional extra focus via
  field `question` (leave the Website Prompt above empty/as-is to use the
  proxy's default behavior unchanged)

## Output shape: merged by chain, not by event

The proxy is called once per extracted event (that's the only way to give it
a specific event to anchor the trace to), so the *raw* per-call result
naturally repeats the exact same chain once for every event that happens to
share it -- e.g. two events both reported by the same official through the
same relay. Left as one record per event, the website would show "event A:
chain 1" and then a separate "event B: chain 1" instead of a single "chain 1:
events A, B" entry, which reads as noisy duplication once a document has more
than a couple of extracted events.

`run_review_bundle_test.py` merges same-signature chains (identical hop
sequence, by `from_person`/`to_person`) within each document before writing
`outputs/source-chain.json`, via `merge_source_chains_by_signature()`. The
final JSON is therefore already **one row per document**, each with a
`chains` array where every distinct chain lists ALL the events it accounts
for in its own `events` array -- not one row per event.

The website's loader (`applySkillChatOutput` in `stage1-timeline.html`) does
the same merge again defensively when importing a bundle, so this is safe
even against an older bundle generated before this contract existed. But any
other producer of `source-chain.json`-shaped data (a different script, a
hand-edited bundle, etc.) should follow the same one-row-per-document,
chains-carry-their-own-events shape to get a clean result rather than relying
on the website to paper over per-event duplication.
