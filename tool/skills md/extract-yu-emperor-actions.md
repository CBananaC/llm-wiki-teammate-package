# Skill: 上諭中皇帝自己的行動（評論＋命令）

**Kind:** yu_emperor_actions

## Purpose

For one `上諭`, extract the emperor's OWN actions stated in the edict: his
comments / judgements (praise, blame, approval, rejection, questions) and his
concrete commands. Because the 上諭 is itself the emperor's document, these are
read directly from its text — not reconstructed from a memorial's 硃批. Relayed
`據某奏` intelligence is context, not an emperor action.

Later official responses to these commands are found separately by the loop via
the existing `official_reply_to_yu` network (see `official-response.md`); this
step only extracts the emperor's actions.

The proxy `yu_emperor_actions` mode carries the full task; this Website Prompt is
a short focus note appended on top.

## Website Prompt

```text
只擷取上諭中皇帝自己的行動：評論／褒獎／責備／准駁／詢問，以及具體命令。先區分（A）皇帝轉述的據奏情報與（B）皇帝自己的話，只輸出（B）。命令、批評、獎懲若對象或功能不同即分項；套語不單獨成項。每項給 title、action_type（comment|command|praise|blame|approve|reject|question）、description、target（受命／受評官員）、quote（皇帝原話逐字）。引文須逐字，不得杜撰。
```

## Used By

- Terminal: `tool/scripts py/run_yu_loop.py`.
- Proxy: `tool/proxy/gemini-proxy/main.py`, `mode: "yu_emperor_actions"`.

## Output (per action)

`title`, `action_type`, `description`, `target[]`, `whenCh`, `whenAr`, `where`,
`who`, `who_loc`, `relations`, `quote`. The loop verifies each `quote` verbatim
against the 上諭 body and drops actions whose quote cannot be located.
