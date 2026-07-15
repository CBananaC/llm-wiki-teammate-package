#!/usr/bin/env python3
"""Refresh the full timeline HTML's embedded DUAL document dataset.

The review page is a self-contained HTML file. Its JavaScript looks up bundle
pair IDs in the embedded ``const DUAL`` array, so the array must be refreshed
whenever ``dual-timeline-data.json`` receives corrected document IDs.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "outputs" / "attempt-002" / "dual-timeline-data.json"
HTML_PATH = ROOT / "outputs" / "attempt-002" / "stage1-timeline.html"


def replace_const(html: str, name: str, value: object) -> str:
    marker = f"const {name} = "
    start = html.find(marker)
    if start < 0:
        raise ValueError(f"Could not find {marker!r} in {HTML_PATH}")
    value_start = start + len(marker)
    end = html.find(";", value_start)
    if end < 0:
        raise ValueError(f"Could not find the end of {marker!r}")
    encoded = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    return html[:value_start] + encoded + html[end:]


def replace_once(html: str, old: str, new: str, label: str) -> str:
    count = html.count(old)
    if count != 1:
        raise ValueError(f"Expected one {label} occurrence, found {count}")
    return html.replace(old, new, 1)


def replace_if_present(html: str, old: str, new: str, label: str) -> str:
    if old not in html:
        return html
    return replace_once(html, old, new, label)


def main() -> None:
    records = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    if not isinstance(records, list) or not records:
        raise ValueError(f"Expected a non-empty list in {DATA_PATH}")

    ids = [str(record.get("id") or "") for record in records]
    stale = [doc_id for doc_id in ids if doc_id.startswith("天")]
    if stale:
        raise ValueError(
            "The source dataset still contains old 上諭 IDs: "
            + ", ".join(stale[:10])
        )

    html = HTML_PATH.read_text(encoding="utf-8")
    refreshed = replace_const(html, "DUAL", records)
    refreshed = replace_if_present(
        refreshed,
        "const yuRecips=(yr&&yr.recipients)||[];",
        "const yuRecips=(yr&&Array.isArray(yr.recipients)&&yr.recipients.length?yr.recipients:(yr&&yr.summary&&yr.summary.emperor_command&&yr.summary.emperor_command.target?[yr.summary.emperor_command.target]:[]))||[];",
        "Yu recipient lookup",
    )
    refreshed = replace_if_present(
        refreshed,
        "'<div class=\"dp-l2\">受命：'+dpFld(yuId,'recipients',yuRecips.join('、'))+'</div>'",
        "'<div class=\"dp-l2\">'+dpFld(yuId,'recipients',yuRecips.join('、'))+'</div>'",
        "Yu recipient label",
    )
    refreshed = replace_if_present(
        refreshed,
        "const yuTitle=(yr&&yr.title)||'';",
        "const yuTitle=(yr&&yr.title)||'';\n        const yuSender=(isZhu&&yr&&yr.author_name)||'';",
        "Zhu sender lookup",
    )
    refreshed = replace_if_present(
        refreshed,
        "(isZhu?'・硃批':(isPrior?'・前奏':''))",
        "(isPrior?'・前奏':'')",
        "Zhu title suffix",
    )
    refreshed = replace_if_present(
        refreshed,
        "</span></div>'+((isZhu||isPrior)?'':(yuRecips.length?'<div class=\"dp-l2\">'+dpFld(yuId,'recipients',yuRecips.join('、'))+'</div>':''))",
        "</span></div>' +(isZhu&&yuSender?'<div class=\"dp-l2\">'+dpFld(yuId,'author_name',yuSender)+'</div>':'') + ((isZhu||isPrior)?'':(yuRecips.length?'<div class=\"dp-l2\">'+dpFld(yuId,'recipients',yuRecips.join('、'))+'</div>':''))",
        "Zhu sender line",
    )
    refreshed = replace_if_present(
        refreshed,
        "+(yuDate?'<div class=\"dp-l3 dp-date-sent\">'+dpFld(yuId,yuDateField,yuDate)+'</div>':'')+'</div>'",
        "+(yuDate?'<div class=\"dp-l3 dp-date-sent\">'+(isZhu&&yr&&yr.sendAr&&yr.recvAr?(dpFld(yuId,'sendAr',yr.sendAr)+'-'+dpFld(yuId,'recvAr',yr.recvAr)):dpFld(yuId,yuDateField,yuDate))+'</div>':'')+'</div>'",
        "Zhu date range",
    )
    refreshed = replace_if_present(
        refreshed,
        "(yuDate?'<div class=\"dp-l3 dp-date-sent\">'+(isPrior?'前奏日：':(isZhu?'硃批／收受日：':'發布日：'))+dpFld(yuId,yuDateField,yuDate)+'</div>':'')",
        "(yuDate?'<div class=\"dp-l3 dp-date-sent\">'+dpFld(yuId,yuDateField,yuDate)+'</div>':'')",
        "Yu date label",
    )
    HTML_PATH.write_text(refreshed, encoding="utf-8")
    print(f"Refreshed embedded DUAL data in {HTML_PATH}")
    print(f"Embedded documents: {len(records)}")


if __name__ == "__main__":
    main()
