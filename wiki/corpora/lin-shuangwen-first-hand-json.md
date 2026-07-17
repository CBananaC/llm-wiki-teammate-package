# 林爽文 First-Hand Corpus

## Canonical dataset

`../../review-tools/shared data/stage1_original_text.json`

The broader checked corpus contained 1,834 structured records: 1,396 from `明清台灣檔案匯編` and 438 from `天地會`. Document types included 上奏, 硃批, 上諭, 移咨, and 其他. The review tools use the canonical Stage 1 subset named above.

## Core fields

- identity: `doc_id`, `series`, `doc_type`, `subtype`
- source description: `compiled_in`, `archive_reference`, `author`, `title`
- chronology: `send_date`, `receive_date`, `announce_date`, remaining `issue_date`
- evidence: `body`, `rescript_text`

Date values may contain paired Chinese and Arabic forms. Do not collapse distinct date meanings into one generic date.

## Use and limitations

Use the corpus for search, grouping, chronology, source selection, and reviewed extraction. Do not treat it automatically as verified quotation text. Formal quotations and page references require checking the underlying compilation.

