#!/usr/bin/env python3
"""Build an interactive Stage 1 timeline HTML from stage1-date-adjusted.json."""

from __future__ import annotations

import json
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any


SOURCE = Path("outputs/attempt-002/stage1-date-adjusted.json")
OUTPUT = Path("outputs/attempt-002/stage1-timeline.html")


def parse_ymd(value: str) -> date | None:
    try:
        return datetime.strptime(value, "%Y/%m/%d").date()
    except Exception:
        return None


def date_pair_value(record: dict[str, Any], field: str) -> tuple[str | None, str | None]:
    value = record.get(field)
    if isinstance(value, list) and len(value) >= 2:
        return value[0], value[1]
    return None, None


def doc_summary(record: dict[str, Any], date_field: str) -> dict[str, Any]:
    chinese, arabic = date_pair_value(record, date_field)
    send_chinese, send_arabic = date_pair_value(record, "send_date")
    receive_chinese, receive_arabic = date_pair_value(record, "receive_date")
    announce_chinese, announce_arabic = date_pair_value(record, "announce_date")
    sent = parse_ymd(send_arabic) if send_arabic else None
    received = parse_ymd(receive_arabic) if receive_arabic else None
    author = record.get("author") if isinstance(record.get("author"), dict) else {}
    return {
        "doc_id": record.get("doc_id"),
        "doc_type": record.get("doc_type"),
        "title": record.get("title"),
        "author_name": author.get("name") or "Unknown",
        "author_position": author.get("position"),
        "date_chinese": chinese,
        "date_arabic": arabic,
        "send_date_chinese": send_chinese,
        "send_date_arabic": send_arabic,
        "receive_date_chinese": receive_chinese,
        "receive_date_arabic": receive_arabic,
        "announce_date_chinese": announce_chinese,
        "announce_date_arabic": announce_arabic,
        "reply_lag_days": (received - sent).days if sent and received else None,
    }


def build_series(records: list[dict[str, Any]]) -> dict[str, Any]:
    events: dict[str, dict[str, list[dict[str, Any]]]] = defaultdict(
        lambda: {"official": [], "reply": [], "order": []}
    )

    for record in records:
        doc_type = record.get("doc_type")

        if doc_type in {"上奏", "硃批"}:
            _, arabic = date_pair_value(record, "send_date")
            if arabic and parse_ymd(arabic):
                events[arabic]["official"].append(doc_summary(record, "send_date"))

        if doc_type == "硃批":
            _, arabic = date_pair_value(record, "receive_date")
            if arabic and parse_ymd(arabic):
                events[arabic]["reply"].append(doc_summary(record, "receive_date"))

        if doc_type == "上諭":
            _, arabic = date_pair_value(record, "announce_date")
            if arabic and parse_ymd(arabic):
                events[arabic]["order"].append(doc_summary(record, "announce_date"))

    all_dates = sorted(parse_ymd(day) for day in events)
    all_dates = [d for d in all_dates if d]
    start = min(all_dates)
    end = max(all_dates)

    days = []
    current = start
    while current <= end:
        key = current.strftime("%Y/%m/%d")
        payload = events.get(key, {"official": [], "reply": [], "order": []})
        days.append(
            {
                "date": key,
                "official": payload["official"],
                "reply": payload["reply"],
                "order": payload["order"],
                "counts": {
                    "official": len(payload["official"]),
                    "reply": len(payload["reply"]),
                    "order": len(payload["order"]),
                },
            }
        )
        current += timedelta(days=1)

    return {
        "source": str(SOURCE),
        "start": start.strftime("%Y/%m/%d"),
        "end": end.strftime("%Y/%m/%d"),
        "days": days,
        "totals": {
            "official": sum(day["counts"]["official"] for day in days),
            "reply": sum(day["counts"]["reply"] for day in days),
            "order": sum(day["counts"]["order"] for day in days),
        },
    }


def main() -> None:
    records = json.loads(SOURCE.read_text(encoding="utf-8"))
    timeline = build_series(records)
    data_json = json.dumps(timeline, ensure_ascii=False)

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>林爽文事件 Stage 1 Timeline</title>
  <style>
    :root {{
      --bg: #f8f5ee;
      --ink: #2d261d;
      --muted: #7a6f63;
      --grid: #ded5c8;
      --official: #2f75b5;
      --reply: #c46a2b;
      --order: #7d4ab8;
      --panel: #fffdf8;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: ui-serif, Georgia, "Times New Roman", "Noto Serif CJK TC", serif;
      color: var(--ink);
      background: radial-gradient(circle at top left, #fffaf1 0, var(--bg) 42%, #efe6d6 100%);
    }}
    header {{
      padding: 28px 32px 14px;
      border-bottom: 1px solid #e0d5c3;
    }}
    h1 {{ margin: 0 0 8px; font-size: 28px; letter-spacing: .01em; }}
    .subtitle {{ color: var(--muted); line-height: 1.5; max-width: 1100px; }}
    main {{ padding: 18px 28px 32px; }}
    .toolbar {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: center;
      margin-bottom: 14px;
    }}
    .pill {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      border: 1px solid #d7cab7;
      background: rgba(255,255,255,.65);
      padding: 8px 10px;
      border-radius: 999px;
      font-size: 14px;
    }}
    .zoom-btn {{
      appearance: none;
      border: 1px solid #cbbba5;
      background: #fffaf1;
      color: var(--ink);
      border-radius: 999px;
      min-width: 34px;
      height: 34px;
      padding: 0 10px;
      font-size: 18px;
      line-height: 1;
      cursor: pointer;
      box-shadow: 0 2px 8px rgba(69, 52, 28, .08);
    }}
    .zoom-btn:hover {{ background: #f4eadb; }}
    .zoom-readout {{
      min-width: 54px;
      text-align: center;
      color: var(--muted);
      font-variant-numeric: tabular-nums;
    }}
    .swatch {{ width: 22px; height: 3px; border-radius: 99px; display: inline-block; }}
    .official {{ background: var(--official); }}
    .reply {{ background: var(--reply); }}
    .order {{ background: var(--order); }}
    .chart-wrap {{
      border: 1px solid #dccfbd;
      background: rgba(255,253,248,.78);
      border-radius: 18px;
      padding: 16px;
      box-shadow: 0 12px 40px rgba(69, 52, 28, .08);
      overflow-x: auto;
    }}
    svg {{ display: block; min-width: 1180px; width: 1320px; height: 520px; transform-origin: top left; }}
    .axis-label {{ fill: var(--muted); font-size: 12px; }}
    .day-hit {{ fill: transparent; cursor: pointer; }}
    .day-hit:hover {{ fill: rgba(47,117,181,.08); }}
    .selected-band {{ fill: rgba(47,117,181,.14); pointer-events: none; }}
    .baseline {{ stroke: #9e8f7b; stroke-width: 1.4; stroke-dasharray: 6 5; }}
    .gridline {{ stroke: var(--grid); stroke-width: 1; }}
    .curve {{ fill: none; stroke-width: 3.2; stroke-linecap: round; stroke-linejoin: round; }}
    .dot {{ stroke: var(--panel); stroke-width: 2; cursor: pointer; }}
    .zero-dot {{ opacity: .15; }}
    .panel {{
      margin-top: 18px;
      display: grid;
      grid-template-columns: minmax(280px, 380px) 1fr;
      gap: 18px;
    }}
    .card {{
      border: 1px solid #dccfbd;
      background: rgba(255,253,248,.9);
      border-radius: 16px;
      padding: 16px;
      box-shadow: 0 8px 26px rgba(69, 52, 28, .06);
    }}
    h2, h3 {{ margin: 0 0 10px; }}
    .big-date {{ font-size: 22px; font-weight: 700; }}
    .counts {{
      display: grid;
      gap: 8px;
      margin-top: 12px;
    }}
    .count-row {{
      display: flex;
      justify-content: space-between;
      gap: 10px;
      border-bottom: 1px dotted #dacbb9;
      padding-bottom: 6px;
    }}
    .section {{
      margin-top: 16px;
      padding-top: 12px;
      border-top: 1px solid #e5dacb;
    }}
    .person {{
      margin: 10px 0;
      padding: 10px;
      border-radius: 12px;
      background: #f8f1e6;
    }}
    .person-title {{
      font-weight: 700;
    }}
    .position {{ color: var(--muted); font-size: 13px; }}
    .doc-list {{ margin: 8px 0 0 18px; padding: 0; }}
    .doc-list li {{ margin: 6px 0; line-height: 1.45; }}
    .doc-id {{ font-family: ui-monospace, SFMono-Regular, Menlo, monospace; color: #5f4b36; }}
    .empty {{ color: var(--muted); font-style: italic; }}
    .tooltip {{
      position: fixed;
      display: none;
      pointer-events: none;
      background: #2d261d;
      color: #fffaf1;
      padding: 8px 10px;
      border-radius: 10px;
      font-size: 13px;
      box-shadow: 0 8px 30px rgba(0,0,0,.22);
      z-index: 20;
      max-width: 280px;
    }}
    @media (max-width: 850px) {{
      .panel {{ grid-template-columns: 1fr; }}
      header {{ padding: 22px 18px 10px; }}
      main {{ padding: 14px; }}
    }}
  </style>
</head>
<body>
  <header>
    <h1>林爽文事件第一階段：文書時間線</h1>
    <div class="subtitle">
      黃仕簡、任承恩分路渡臺階段。Top curve: officials sending memorials upward. Lower curves: emperor replying by 硃批 and issuing 上諭. Click a day to inspect who sent, who received replies, and who received orders.
    </div>
  </header>
  <main>
    <div class="toolbar">
      <span class="pill"><span class="swatch official"></span> Officials sent to emperor</span>
      <span class="pill"><span class="swatch reply"></span> Emperor replied / 硃批</span>
      <span class="pill"><span class="swatch order"></span> Emperor issued 上諭</span>
      <span class="pill" title="Use buttons, or pinch/trackpad zoom over the chart">
        Graph size
        <button class="zoom-btn" id="zoomOut" type="button">−</button>
        <span class="zoom-readout" id="zoomReadout">100%</span>
        <button class="zoom-btn" id="zoomIn" type="button">+</button>
        <button class="zoom-btn" id="zoomReset" type="button" style="font-size:13px;">Reset</button>
      </span>
      <span class="pill" id="rangePill"></span>
    </div>
    <div class="chart-wrap">
      <svg id="chart" role="img" aria-label="Stage 1 document timeline"></svg>
    </div>
    <div class="panel">
      <section class="card" id="daySummary"></section>
      <section class="card" id="dayDetails"></section>
    </div>
  </main>
  <div class="tooltip" id="tooltip"></div>
  <script>
    const TIMELINE = {data_json};

    const svg = document.getElementById('chart');
    const tooltip = document.getElementById('tooltip');
    const daySummary = document.getElementById('daySummary');
    const dayDetails = document.getElementById('dayDetails');
    const rangePill = document.getElementById('rangePill');
    const chartWrap = document.querySelector('.chart-wrap');
    const zoomIn = document.getElementById('zoomIn');
    const zoomOut = document.getElementById('zoomOut');
    const zoomReset = document.getElementById('zoomReset');
    const zoomReadout = document.getElementById('zoomReadout');
    const W = 1320, H = 520;
    const M = {{ left: 62, right: 28, top: 34, bottom: 64 }};
    const baseline = 236;
    const plotW = W - M.left - M.right;
    const maxCount = Math.max(...TIMELINE.days.flatMap(d => [d.counts.official, d.counts.reply, d.counts.order]), 1);
    const scaleY = Math.min(24, 178 / maxCount);
    let selectedDate = null;
    let chartZoom = 1;

    svg.setAttribute('viewBox', `0 0 ${{W}} ${{H}}`);
    applyZoom();
    rangePill.textContent = `${{TIMELINE.start}} → ${{TIMELINE.end}} · official ${{TIMELINE.totals.official}} · reply ${{TIMELINE.totals.reply}} · 上諭 ${{TIMELINE.totals.order}}`;

    const x = i => M.left + (TIMELINE.days.length === 1 ? 0 : i * plotW / (TIMELINE.days.length - 1));
    const yOfficial = d => baseline - d.counts.official * scaleY;
    const yReply = d => baseline + d.counts.reply * scaleY;
    const yOrder = d => baseline + 18 + d.counts.order * scaleY;

    function el(name, attrs = {{}}, parent = svg) {{
      const node = document.createElementNS('http://www.w3.org/2000/svg', name);
      for (const [k, v] of Object.entries(attrs)) node.setAttribute(k, v);
      parent.appendChild(node);
      return node;
    }}

    function smoothPath(points) {{
      if (!points.length) return '';
      if (points.length === 1) return `M ${{points[0][0]}} ${{points[0][1]}}`;
      let d = `M ${{points[0][0]}} ${{points[0][1]}}`;
      for (let i = 0; i < points.length - 1; i++) {{
        const p0 = points[Math.max(0, i - 1)];
        const p1 = points[i];
        const p2 = points[i + 1];
        const p3 = points[Math.min(points.length - 1, i + 2)];
        const cp1x = p1[0] + (p2[0] - p0[0]) / 6;
        const cp1y = p1[1] + (p2[1] - p0[1]) / 6;
        const cp2x = p2[0] - (p3[0] - p1[0]) / 6;
        const cp2y = p2[1] - (p3[1] - p1[1]) / 6;
        d += ` C ${{cp1x}} ${{cp1y}}, ${{cp2x}} ${{cp2y}}, ${{p2[0]}} ${{p2[1]}}`;
      }}
      return d;
    }}

    function nonZeroPoints(kind) {{
      const yFn = kind === 'official' ? yOfficial : kind === 'reply' ? yReply : yOrder;
      return TIMELINE.days.map((day, i) => [x(i), yFn(day)]);
    }}

    function renderChart() {{
      svg.innerHTML = '';
      el('rect', {{ x: 0, y: 0, width: W, height: H, fill: 'transparent' }});
      for (let c = 0; c <= maxCount; c += Math.max(1, Math.ceil(maxCount / 5))) {{
        el('line', {{ x1: M.left, x2: W - M.right, y1: baseline - c * scaleY, y2: baseline - c * scaleY, class: 'gridline' }});
        el('line', {{ x1: M.left, x2: W - M.right, y1: baseline + c * scaleY, y2: baseline + c * scaleY, class: 'gridline' }});
        el('text', {{ x: 18, y: baseline - c * scaleY + 4, class: 'axis-label' }}).textContent = c;
        if (c) el('text', {{ x: 18, y: baseline + c * scaleY + 4, class: 'axis-label' }}).textContent = c;
      }}
      el('line', {{ x1: M.left, x2: W - M.right, y1: baseline, y2: baseline, class: 'baseline' }});
      el('text', {{ x: M.left, y: baseline - 190, class: 'axis-label' }}).textContent = 'officials → emperor';
      el('text', {{ x: M.left, y: baseline + 205, class: 'axis-label' }}).textContent = 'emperor → officials';

      const monthTicks = new Set();
      TIMELINE.days.forEach((day, i) => {{
        const ym = day.date.slice(0, 7);
        if (!monthTicks.has(ym)) {{
          monthTicks.add(ym);
          el('line', {{ x1: x(i), x2: x(i), y1: M.top, y2: H - M.bottom + 8, stroke: '#e8dece', 'stroke-width': 1 }});
          el('text', {{ x: x(i) + 4, y: H - 34, class: 'axis-label' }}).textContent = ym;
        }}
      }});

      el('path', {{ d: smoothPath(nonZeroPoints('official')), class: 'curve', stroke: 'var(--official)' }});
      el('path', {{ d: smoothPath(nonZeroPoints('reply')), class: 'curve', stroke: 'var(--reply)' }});
      el('path', {{ d: smoothPath(nonZeroPoints('order')), class: 'curve', stroke: 'var(--order)' }});

      TIMELINE.days.forEach((day, i) => {{
        const xi = x(i);
        if (day.date === selectedDate) {{
          const bandW = Math.max(8, plotW / TIMELINE.days.length);
          el('rect', {{ x: xi - bandW / 2, y: M.top, width: bandW, height: H - M.top - M.bottom, class: 'selected-band' }});
        }}
        const total = day.counts.official + day.counts.reply + day.counts.order;
        const dotClass = total ? 'dot' : 'dot zero-dot';
        el('circle', {{ cx: xi, cy: yOfficial(day), r: total ? 4 : 2, fill: 'var(--official)', class: dotClass }});
        el('circle', {{ cx: xi, cy: yReply(day), r: total ? 4 : 2, fill: 'var(--reply)', class: dotClass }});
        el('circle', {{ cx: xi, cy: yOrder(day), r: total ? 4 : 2, fill: 'var(--order)', class: dotClass }});
        const hitW = Math.max(7, plotW / TIMELINE.days.length);
        const hit = el('rect', {{ x: xi - hitW / 2, y: M.top, width: hitW, height: H - M.top - M.bottom, class: 'day-hit' }});
        hit.addEventListener('click', () => selectDay(day.date));
        hit.addEventListener('mousemove', ev => showTooltip(ev, day));
        hit.addEventListener('mouseleave', hideTooltip);
      }});
    }}

    function groupByPerson(docs) {{
      const map = new Map();
      docs.forEach(doc => {{
        const key = `${{doc.author_name}}|||${{doc.author_position || ''}}`;
        if (!map.has(key)) map.set(key, {{ name: doc.author_name, position: doc.author_position, docs: [] }});
        map.get(key).docs.push(doc);
      }});
      return [...map.values()].sort((a, b) => b.docs.length - a.docs.length || a.name.localeCompare(b.name, 'zh-Hant'));
    }}

    function setZoom(nextZoom, anchorX = null) {{
      const oldZoom = chartZoom;
      chartZoom = Math.max(0.55, Math.min(3.2, nextZoom));
      if (Math.abs(chartZoom - oldZoom) < 0.001) return;
      const beforeScroll = chartWrap.scrollLeft;
      const relativeX = anchorX === null ? chartWrap.clientWidth / 2 : anchorX - chartWrap.getBoundingClientRect().left;
      const logicalX = (beforeScroll + relativeX) / oldZoom;
      applyZoom();
      chartWrap.scrollLeft = logicalX * chartZoom - relativeX;
    }}

    function applyZoom() {{
      svg.style.width = `${{W * chartZoom}}px`;
      svg.style.height = `${{H * chartZoom}}px`;
      zoomReadout.textContent = `${{Math.round(chartZoom * 100)}}%`;
    }}

    zoomIn.addEventListener('click', () => setZoom(chartZoom * 1.18));
    zoomOut.addEventListener('click', () => setZoom(chartZoom / 1.18));
    zoomReset.addEventListener('click', () => setZoom(1));
    chartWrap.addEventListener('wheel', ev => {{
      if (ev.ctrlKey || ev.metaKey) {{
        ev.preventDefault();
        const factor = ev.deltaY < 0 ? 1.08 : 1 / 1.08;
        setZoom(chartZoom * factor, ev.clientX);
      }}
    }}, {{ passive: false }});
    chartWrap.addEventListener('gesturechange', ev => {{
      ev.preventDefault();
      if (ev.scale) setZoom(chartZoom * (ev.scale > 1 ? 1.03 : 1 / 1.03), ev.clientX || null);
    }});

    function replySuffix(doc) {{
      if (doc.doc_type !== '硃批') return '';
      const sent = doc.send_date_arabic || '?';
      const received = doc.receive_date_arabic || '?';
      const days = doc.reply_lag_days === null || doc.reply_lag_days === undefined ? '?' : doc.reply_lag_days;
      return ` (${{sent}}, ${{received}}, ${{days}} days)`;
    }}

    function renderGroup(title, docs, colorVar, verb) {{
      if (!docs.length) return `<div class="section"><h3>${{title}}</h3><p class="empty">No records.</p></div>`;
      const groups = groupByPerson(docs);
      return `<div class="section"><h3>${{title}}</h3>${{groups.map(g => `
        <div class="person" style="border-left: 4px solid var(${{colorVar}})">
          <div class="person-title">${{g.name}} <span class="position">${{g.position ? '· ' + g.position : ''}}</span></div>
          <div class="position">${{verb}} · ${{g.docs.length}} document${{g.docs.length > 1 ? 's' : ''}}</div>
          <ol class="doc-list">
            ${{g.docs.map(doc => `<li><span class="doc-id">${{doc.doc_id}}</span> · ${{doc.doc_type}} · ${{escapeHtml(doc.title || '')}}${{replySuffix(doc)}}</li>`).join('')}}
          </ol>
        </div>`).join('')}}</div>`;
    }}

    function escapeHtml(text) {{
      return text.replace(/[&<>"']/g, ch => ({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}}[ch]));
    }}

    function selectDay(date) {{
      selectedDate = date;
      const day = TIMELINE.days.find(d => d.date === date);
      renderChart();
      renderDetails(day);
    }}

    function renderDetails(day) {{
      const total = day.counts.official + day.counts.reply + day.counts.order;
      daySummary.innerHTML = `
        <div class="big-date">${{day.date}}</div>
        <div class="position">Total visible events: ${{total}}</div>
        <div class="counts">
          <div class="count-row"><span>Officials sent to emperor</span><strong>${{day.counts.official}}</strong></div>
          <div class="count-row"><span>Emperor replied by 硃批</span><strong>${{day.counts.reply}}</strong></div>
          <div class="count-row"><span>Emperor issued 上諭</span><strong>${{day.counts.order}}</strong></div>
        </div>
      `;
      dayDetails.innerHTML = `
        <h2>Daily actors</h2>
        ${{renderGroup('Officials sending to emperor', day.official, '--official', 'sent upward')}}
        ${{renderGroup('Emperor replying to', day.reply, '--reply', 'received imperial reply')}}
        ${{renderGroup('上諭 directed to', day.order, '--order', 'received imperial order')}}
      `;
    }}

    function showTooltip(ev, day) {{
      tooltip.style.display = 'block';
      tooltip.style.left = `${{ev.clientX + 14}}px`;
      tooltip.style.top = `${{ev.clientY + 14}}px`;
      tooltip.innerHTML = `<strong>${{day.date}}</strong><br>official ${{day.counts.official}} · reply ${{day.counts.reply}} · 上諭 ${{day.counts.order}}`;
    }}
    function hideTooltip() {{ tooltip.style.display = 'none'; }}

    const firstInteresting = TIMELINE.days.find(d => d.counts.official || d.counts.reply || d.counts.order) || TIMELINE.days[0];
    selectedDate = firstInteresting.date;
    renderChart();
    renderDetails(firstInteresting);
  </script>
</body>
</html>
"""
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
