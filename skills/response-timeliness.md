# Skill: 回應時效評估

**Kind:** response_timeliness

## Website Prompt

以下是一份奏摺與皇帝硃批的基本資料（`baseline`），以及該奏摺上奏日至硃批受文日之間，其他官員所上呈的奏摺或文書（`change_docs`），另有硃批受文日起至其後三日內頒布或發出的硃批與上諭（`response_docs`）。

請完成兩項判斷：

1. 皇帝寫下硃批或發布上諭時，實際情勢是否已不同於原奏摺所報情況，例如戰況、地點控制或官員對策已經改變。
2. 皇帝回應是否仍切合當時情勢，抑或只針對已過時的舊報告作答。

只能依據所提供文書作答，不得補造戰況、日期或因果關係。所有證據必須保留文書識別碼與逐字引文。只輸出以下 JSON：

```json
{
  "situation": "本奏摺原本回報的情勢摘要",
  "changes": [
    {
      "doc_id": "文書id",
      "subtitle": "此文書所顯示情勢變化的簡短標目",
      "title": "標題",
      "author": "作者",
      "sentAr": "YYYY/M/D",
      "quote": "原文逐字引文",
      "how": "此文書顯示情勢如何改變"
    }
  ],
  "responses": [
    {
      "doc_id": "文書id",
      "type": "硃批或上諭",
      "date": "YYYY/M/D",
      "quote": "皇帝回應的逐字引文",
      "note": "回應內容概述"
    }
  ],
  "verdict": "fits|stale-but-harmless|mismatch",
  "reasoning": "引用 changes 與 responses 的文書識別碼及引文，說明判斷理由"
}
```

`verdict` 只能使用：

- `fits`：回應切合當時實際情勢。
- `stale-but-harmless`：回應雖以舊情勢為基礎，但未造成實質影響。
- `mismatch`：回應與當時實際情勢明顯不符。

## Purpose

保存 AI 對話面板「回應時效」所使用的正式提示詞，使面板不再依賴寫死於 HTML 內的提示文字。執行時，網站會把 `baseline`、`change_docs` 與 `response_docs` 附加在本提示詞之後。

## Used By

- Website：AI 對話面板「動作」選單「回應時效」，以及 `@回應時效` 指令。
- Dispatch：`runSituFit()`。
- Proxy：`mode: "ask"`。
