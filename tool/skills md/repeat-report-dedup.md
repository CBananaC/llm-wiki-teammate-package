# Skill: 重複回報偵測（跨文書、跨措辭）

**Kind:** repeat_report

## Purpose

Detect when a freshly-extracted card — a 林方 event, a 清方 action, an 皇帝
action, or a 官員回應 — is in fact the same concrete occurrence already recorded
as a committed dot, even when the wording, official, or perspective differ. This
matters most for the `上諭` loop: the memorials a 上諭 was drawn from are usually
reviewed and committed BEFORE the 上諭 itself, so the 上諭's re-report of those
same events would otherwise create duplicate dots.

For each new card the runner pre-filters earlier cards (this run, earlier
official-loop bundles, and committed `formal_all.data`) by cheap topic overlap,
sends the shortlist to the proxy `repeat_report` mode (which judges sameness by
MEANING), names the earliest report by the reporting document's send date, and
annotates the card with `same_as` + `earliest_report`. The official-document
loop applies this pass to 林方 and 清方 cards across documents only.
Nothing is merged — the website turns the annotation into a 合併／保留 choice.

## Sameness rule

Same report only when it is the same specific act/event: same principal
actor(s), same object/target, same place and time referent. Sharing people, the
same battle, or the same broad topic is not enough; 皇帝 actions require the same
object AND the same concrete comment/command.
同一文書內的兩張卡片不得互判為重複回報；重複回報必須來自另一份文書。

## Website Prompt

```text
只判斷『新擷取卡片』與哪些較早候選其實是同一件具體事件／行動的重複回報，允許措辭不同、敘述官員不同或角度不同。同一件＝同一具體動作或事件（同一主體、對象、地點與時間所指），非僅牽涉相同人物或相同大主題；不同日期、地點、動作或主事者即非同一件。皇帝行動須對象與具體評論／命令均相同才算重複。只回傳確屬同一件的候選 id，無則回傳空陣列，不得杜撰。
```

## Used By

- Terminal: `tool/scripts py/run_mass_prompt_chain_test.py` (cross-document
  dedup pass over 林/清) and `tool/scripts py/run_yu_loop.py` (dedup pass over
  林/清/皇帝/回應).
- Proxy: `tool/proxy/gemini-proxy/main.py`, `mode: "repeat_report"`.

## Output (added to each card)

- `same_as` — id of the earliest earlier card judged the same report (a
  `formal_all.data` event id or a within-bundle card id), or absent if none.
- `earliest_report` — `{ id, doc_id, date, title }` describing that report.
- `repeat_candidates` — the ids the model judged equivalent (audit).

The terminal dedup output may also include `repeat_report_doc_id`,
`repeat_report_author`, and `repeat_report_doc_title`. These identify the earlier
reporting document used by the review card label.
