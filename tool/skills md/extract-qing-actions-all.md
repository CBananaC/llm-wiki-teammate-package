# Skill: 清方行動（三類合一）

**Kind:** events
**Actor:** qing
**Category:** all

## Website Prompt

```text
只擷取本文書中清方（官員、官軍、義民、鄉勇或清朝行政機構）的具體行動，並在同一次輸出中分成三類：`done`＝已實際執行的軍事／防剿行動；`plan`＝計畫、奏請、命令、擬議或預備但尚未證實已執行的軍事／防剿行動；`nonmil`＝已實際執行的非軍事行政、安撫、賑濟、審訊、籌餉、人事、善後或其他實質措施。每則事件必須有 category，且只能是 done、plan、nonmil 之一。不要擷取林方行動、純粹的奏報／聞報／轉述動作，也不要把舊奏、舊諭或據某官文書中已先前報告的行動當作本文新事件。若同一段同時含已做與計畫，分成相應事件。每則保留支持該事件的原文逐字 quote，並填寫完整 subtitle、description、where、who、who_loc、relations、whenCh、whenAr、howKnown、whenKnownCh；不可由文書收發日期推造事件日期。subtitle 必須是完整的「主語＋動詞＋對象／目標」短標題，不能只寫「進兵」「籌議」或「攻陷彰化縣城」；例如應寫「黃仕簡帶領官兵渡臺」或「程峻等募集鄉勇防禦」。主語與對象須取自原文、`who` 或 `relations`，不得杜撰。只輸出 JSON：{"events":[{"category":"done|plan|nonmil","subtitle":"","description":"","side":"qing","where":"","who":[],"who_loc":{},"relations":[],"whenCh":"","whenAr":"","quote":"","howKnown":"","whenKnownCh":""}]}。沒有符合事件時輸出 {"events":[]}。所有引文必須逐字來自本文書原文，不得杜撰。
```

## Purpose

This is one proxy call, not three separate category calls. The category is a
classification on each returned event, so one passage can be represented once
without producing three overlapping copies. The terminal loop traces each
returned event separately with `trace-source-chain.md`.

The existing bundle loader compares these event cards against earlier 林方 or
清方 extraction cards across documents. It names the earliest matching report
and presents the existing merge/separate choice; no second model deduplication
call is needed.

## Output rules

- Preserve exact original-text quotations.
- Exclude actions found only inside a quoted or cited earlier report.
- Keep done, plan, and nonmil distinct even when their subject is the same.
- Use Traditional Chinese and leave uncertain dates or locations blank.
