# Skill: 合併同一皇帝行動（跨硃批／上諭／文書）

**Kind:** merge_emperor_actions

## Purpose

After `emperor-actions-confirmed-zhu-yu` has extracted the per-document emperor
action points, this pass groups the points that express **the same concrete
imperial action** so the website renders one card carrying every source
(硃批 A, 上諭 B, 上諭 C, …) instead of several near-duplicate cards.

It is needed because one imperial action can surface more than once:

- a memorial's 硃批 and its paired 上諭 stating the same command in different
  wording, and
- several memorials that share the same 上諭 (e.g. 硃25 and 硃26 both linked to
  諭13), each producing its own copy of that 上諭-derived action.

The pass groups by meaning; it never rewrites the quotations. The runner unions
the grouped points' sources deterministically (dedup by doc_id + quote) and tags
each point with a shared `merge_group`, so the merge is auditable and reversible.

## Sameness rule

Group only points that are the **same concrete action**: same object and same
specific comment / reply / command, even when wording, person, or the underlying
硃批/上諭 differ. Different objects, or genuinely different instructions, stay in
separate groups — matching the "split multi-topic points" rule the extraction
prompt already applies.

## Website Prompt

```text
把表達同一個具體皇帝行動者歸為一組：同一對象且同一具體評論、答覆或命令，即使措辭、人稱或所依據的硃批／上諭不同（例如硃批『汝辦理甚好』與上諭『某官辦理妥善』屬同一件）。僅主題相近、對象不同或屬不同指示者不可歸為一組。每組給 members（該組所有 idx）、title（合併後最貼切標題）、action_type。members 只能用出現過的 idx，不得杜撰。
```

## Used By

- Terminal: `tool/scripts py/run_mass_prompt_chain_test.py` — post-loop, over all
  extracted emperor points across the run's documents.
- Proxy: `tool/proxy/gemini-proxy/main.py`, `mode: "merge_emperor_actions"`.

## Output (added to each emperor point)

- `merge_group` — the card_id of the group's primary (earliest by the reporting
  document's send date); every point in the group carries the same value, and a
  singleton carries its own card_id.
- `merge_primary` — `true` on the group's representative point.
- `merge_members` — on the primary, the card_ids of all points in the group.

The website groups points by `merge_group` and shows one card whose sources are
the union of the members' 硃批 / 上諭 quotations.
