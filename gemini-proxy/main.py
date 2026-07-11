"""Cloud Run proxy: lets the local timeline page ask Gemini (Vertex AI) about a
document, without exposing any API key to the browser.

It authenticates to Vertex AI using the Cloud Run service account (Application
Default Credentials) and exposes one POST endpoint, /chat, with CORS enabled.

Request JSON:
  {
    "mode": "summary" | "divide" | "ask",
    "doc_id": "台26",
    "doc_type": "硃批",
    "title": "...",
    "body": "<original memorial text>",
    "rescript": "<硃批 text, optional>",
    "summary": { ...Gemini structured summary... },   # optional context
    "highlight": "currently highlighted quotation",     # optional
    "question": "free-text question"                    # for mode=ask
  }

Response JSON:
  mode summary | ask -> { "mode": "...", "text": "..." }
  mode divide        -> { "mode": "divide", "parts": [ {label, summary, excerpt}, ... ] }
"""
import json
import os

import google.auth
import google.auth.transport.requests
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

LOCATION = os.environ.get("VERTEX_LOCATION", "global")
MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
ALLOW_ORIGIN = os.environ.get("ALLOW_ORIGIN", "*")
# Default to each model's true max output so dense event/provenance JSON is never truncated.
MAX_TOKENS = int(os.environ.get("MAX_OUTPUT_TOKENS", "65536"))
# Per-model output ceilings (Vertex rejects requests above these).
MODEL_MAX_OUT = {
    "gemini-1.5-flash-002": 8192, "gemini-1.5-pro-002": 8192,
    "gemini-2.0-flash-001": 8192,
    "gemini-2.5-flash": 65536, "gemini-2.5-pro": 65536,
    "gemini-3.5-flash": 65536, "gemini-3.1-pro-preview": 65536,
}

_CREDS, _ADC_PROJECT = google.auth.default(
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)
PROJECT = os.environ.get("GCP_PROJECT") or _ADC_PROJECT

SYSTEM = (
    "You are assisting historical research on the Lin Shuangwen (林爽文) war of "
    "1786-1788. You read Qing dynasty memorials (上奏), vermilion rescripts (硃批) "
    "and imperial edicts (上諭) in classical Chinese. Be faithful to the source, "
    "never invent facts, and answer in Traditional Chinese unless asked otherwise."
)


def _token() -> str:
    _CREDS.refresh(google.auth.transport.requests.Request())
    return _CREDS.token


ALLOWED_MODELS = {
    "gemini-3.1-pro-preview", "gemini-3.5-flash",
    "gemini-2.5-flash", "gemini-2.5-pro",
    "gemini-2.0-flash-001", "gemini-1.5-flash-002", "gemini-1.5-pro-002",
}


def _vertex(user_text: str, json_out: bool, model: str | None = None,
            max_tokens: int | None = None) -> str:
    use_model = model if (model in ALLOWED_MODELS) else MODEL
    if LOCATION == "global":
        host = "aiplatform.googleapis.com"
        loc = "global"
    else:
        host = f"{LOCATION}-aiplatform.googleapis.com"
        loc = LOCATION
    url = (
        f"https://{host}/v1/projects/{PROJECT}/locations/{loc}"
        f"/publishers/google/models/{use_model}:generateContent"
    )
    want = max_tokens or MAX_TOKENS
    out_tokens = min(want, MODEL_MAX_OUT.get(use_model, 65536))
    gen_cfg = {"temperature": 0.2, "topP": 0.9, "maxOutputTokens": out_tokens}
    if json_out:
        gen_cfg["responseMimeType"] = "application/json"
    body = {
        "systemInstruction": {"parts": [{"text": SYSTEM}]},
        "contents": [{"role": "user", "parts": [{"text": user_text}]}],
        "generationConfig": gen_cfg,
    }
    r = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {_token()}",
            "Content-Type": "application/json; charset=utf-8",
        },
        data=json.dumps(body).encode("utf-8"),
        timeout=120,
    )
    r.raise_for_status()
    data = r.json()
    return data["candidates"][0]["content"]["parts"][0]["text"]


def _context(p: dict) -> str:
    parts = []
    if p.get("doc_id"):
        parts.append(f"文書編號：{p['doc_id']}（{p.get('doc_type','')}）")
    if p.get("title"):
        parts.append(f"標題：{p['title']}")
    if p.get("body"):
        parts.append("原文：\n" + p["body"])
    if p.get("rescript"):
        parts.append("硃批：\n" + p["rescript"])
    if p.get("summary"):
        parts.append(
            "既有結構化摘要（Gemini）：\n"
            + json.dumps(p["summary"], ensure_ascii=False)
        )
    return "\n\n".join(parts)


def _defence(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        text = text.split("```", 2)[1]
        if text.lower().startswith("json"):
            text = text[4:]
    return text.strip()


def _strip_json(text: str):
    text = _defence(text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        s, e = text.find("{"), text.rfind("}")
        return json.loads(text[s : e + 1])


def _salvage_objects(text: str, key: str) -> list:
    """Recover every COMPLETE object inside the `key` array, even when the model's
    output was cut off by the token limit mid-array (so we never lose the whole batch)."""
    marker = '"' + key + '"'
    start = text.find("[", text.find(marker) + 1 if marker in text else 0)
    if start < 0:
        return []
    s = text[start + 1:]
    out, depth, obj_start, in_str, esc = [], 0, -1, False, False
    for i, ch in enumerate(s):
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch == "{":
            if depth == 0:
                obj_start = i
            depth += 1
        elif ch == "}":
            if depth > 0:
                depth -= 1
                if depth == 0 and obj_start >= 0:
                    try:
                        out.append(json.loads(s[obj_start:i + 1]))
                    except json.JSONDecodeError:
                        pass
                    obj_start = -1
        elif ch == "]" and depth == 0:
            break
    return out


def _json_list(raw: str, key: str) -> list:
    """Parse a {key: [...]} response robustly: clean parse first, then salvage."""
    t = _defence(raw)
    try:
        d = json.loads(t)
        if isinstance(d, dict) and isinstance(d.get(key), list):
            return d[key]
        if isinstance(d, list):
            return d
    except json.JSONDecodeError:
        pass
    return _salvage_objects(t, key)


def _cors(resp):
    resp.headers["Access-Control-Allow-Origin"] = ALLOW_ORIGIN
    resp.headers["Access-Control-Allow-Headers"] = "Content-Type"
    resp.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    return resp


def _mt(p: dict):
    """Optional per-request output-token override; clamped to the model ceiling in _vertex."""
    try:
        v = int(p.get("max_output_tokens") or 0)
        return v if v > 0 else None
    except (TypeError, ValueError):
        return None


@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():
    if request.method == "OPTIONS":
        return _cors(app.make_response(("", 204)))
    p = request.get_json(force=True, silent=True) or {}
    mode = p.get("mode", "ask")
    ctx = _context(p)

    try:
        if mode == "summary":
            # `instruction` lets a caller (terminal batch runner or the website,
            # both reading the same llm-wiki skill file) supply the actual task
            # wording. Falls back to the default so old callers keep working.
            instruction = (p.get("instruction") or "").strip() or (
                "用繁體中文，為上述文書寫一段更精簡、流暢的摘要（約 3-5 句），"
                "突出最關鍵的人、事、時、地，避免逐句翻譯。"
            )
            prompt = ctx + "\n\n任務：" + instruction + "只輸出摘要文字。"
            return _cors(jsonify({"mode": "summary", "text": _vertex(prompt, False, p.get("model"))}))

        if mode == "daysummary":
            # Summarize a fixed-length window of the timeline using ONLY the already-extracted
            # 林方/清方 field-event line (never the raw archive text) -- the client sends a plain
            # list of {actor, date, where, subtitle, description} lines for events falling inside
            # [period_start, period_end], already sorted by date. No document context applies here.
            period_start = (p.get("period_start") or "").strip()
            period_end = (p.get("period_end") or "").strip()
            events_text = (p.get("events_text") or "").strip()
            label = period_start if period_start == period_end else f"{period_start} 至 {period_end}"
            prompt = (
                f"以下是時間軸上「{label}」期間，已擷取的林爽文方與清方行動事件列表（依日期排列，"
                "每行一則，格式為【陣營】日期／地點：標題——說明）：\n\n"
                + (events_text or "（無事件）")
                + "\n\n任務：根據以上事件，用繁體中文寫一段連貫的敘事摘要（約3-6句），"
                "說明這段期間內林爽文方與清方各自做了什麼、雙方情勢如何演變，"
                "並在合理時指出因果或呼應關係（例如清方的部署是否針對林方某一行動）。"
                "只根據上述事件列表内容，不得杜撰列表之外的事實。只輸出摘要文字，不要加標題或項目符號。"
            )
            return _cors(jsonify({"mode": "daysummary", "summary": _vertex(prompt, False, p.get("model"))}))

        if mode == "divide":
            # same pattern: `instruction` is skill-sourced; the required JSON
            # output contract stays fixed here so the website's existing
            # parser/highlighter never breaks.
            instruction = (p.get("instruction") or "").strip() or (
                "將上述『原文』依內容與功能切分為數個連續段落。"
                "對每一段給出：label（簡短的段落標題，如『情報來源』『軍事部署』『請旨』）、"
                "summary（一句繁體中文短摘要）、excerpt（該段的原文，盡量逐字節錄）。"
            )
            prompt = (
                ctx
                + "\n\n任務：" + instruction
                + '請只輸出 JSON，格式：{"parts":[{"label":"...","summary":"...","excerpt":"..."}]}'
            )
            parts = _json_list(_vertex(prompt, True, p.get("model"), _mt(p)), "parts")
            return _cors(jsonify({"mode": "divide", "parts": parts}))

        if mode == "events":
            actor = p.get("actor", "lin")
            category = (p.get("category") or "").strip()   # for qing: 'done' | 'plan' | 'nonmil'
            if actor == "lin":
                who = "林爽文等民變一方（叛軍）的軍事行動"
            elif category == "plan":
                who = "清朝官方（官員、官軍）『計畫、奏請、奉命但尚未執行』的軍事或防剿行動"
            elif category == "nonmil":
                who = "清朝官方（官員、官軍）所實際採取的『非軍事』作為（行政、安撫民番、賑濟、審訊、籌餉、人事、善後等）"
            else:
                who = "清朝官方（官員、官軍）『已實際執行』的軍事或防剿行動"
            actor_instruction = (p.get("actor_instruction") or "").strip()
            question = (p.get("question") or "").strip()
            chat_context = (p.get("chat_context") or "").strip()
            focus = ""
            if question or chat_context:
                focus = (
                    "\n\n【使用者聚焦 / FOCUS（最高優先）】\n"
                    + (("使用者要求：" + question + "\n") if question else "")
                    + (("被回覆訊息脈絡（僅供辨識，勿逐條擷取）：\n" + chat_context + "\n") if chat_context else "")
                    + "上述聚焦通常指向『一件』特定事件（往往是使用者引用的某一句話，例如某官員遇害、某地失陷）。"
                      "請在本文書中找出『與該聚焦句意義相符』的那一件事件並回傳；若聚焦含引號內或具體字句，"
                      "務必在原文中定位該句並作為 quote。"
                      "請忽略脈絡中其他僅作背景的人事物（例如脈絡大量提到林爽文，但聚焦其實是某官員遇害時，"
                      "應回傳『官員遇害』那件，而非林爽文的其他行動）。"
                      "通常只回傳 1 件（最多 2-3 件緊密相關子事件）。"
                      "若聚焦事件的行動方與預設類別不同，仍以聚焦事件為準照常回傳。\n"
                )
            if focus:
                task = ("\n\n任務：請『依 FOCUS』在上述文書中找出使用者所指的那一件事件並回傳"
                        "（以聚焦為準，不受行動方分類限制；該事件可能是某官員遇害、某地失陷等）。"
                        "在原文中定位對應字句作為 quote。重點是實地發生的行動本身，而非奏報這個動作。"
                        "對每個事件給出：")
            elif actor == "qing" and category == "plan":
                task = (f"\n\n任務：從上述文書中，擷取屬於「{who}」——即清方『尚未執行、僅屬計畫／奏請／奉命／擬議／預備』的軍事或防剿行動，不要遺漏。"
                        "例如：某官奏請調兵、命某將前往剿辦、擬於某日出兵、預備堵禦、籌議進剿方略等，但文中未敘其已執行。"
                        "【切分顆粒度，不設上限】以『一項連貫的計畫／部署』為一條事件，依文意劃分；相近而連貫的部署可合為一條並於 description 概述。"
                        "請『勿納入已實際執行的行動』（那屬於另一類），也勿納入純粹的奏報、聞報動作。"
                        "對每個事件給出：")
            elif actor == "qing" and category == "nonmil":
                task = (f"\n\n任務：從上述文書中，擷取屬於「{who}」——即清方『實際採取的非軍事作為』，不要遺漏。"
                        "涵蓋：行政措施、安撫民番、賑濟撫卹、審訊俘犯、籌措糧餉、人事任免、善後處置、出榜曉諭等具體作為。"
                        "【切分顆粒度，不設上限】以『一項連貫的具體作為』為一條事件，依文意劃分，相近而連貫者可合為一條並於 description 概述。"
                        "【排除】軍事攻防、調兵、交戰等軍事行動（那屬於另一類）；也排除純粹的奏報、聞報、轉述等文書動作（除非該文書行為本身即是一項實質措施，如出榜曉諭、頒給）。"
                        "對每個事件給出：")
            else:
                task = (f"\n\n任務：從上述文書中，擷取屬於「{who}」、在戰場或地方上『實際發生（已執行）』的軍事行動，不要遺漏。"
                        "【切分顆粒度，不設上限】請以『一個連貫的軍事行動或戰鬥段落（episode）』作為一條事件，依你自己對戰事敘述的理解來劃分，"
                        "就像你用結構化條列概述本文書軍事經過時，每一個要點就是一條事件。"
                        "判準：一段『連貫的同一波交戰／同一個機動』即使跨越一兩天，也合併為同一條（例如連日同地的同一波激戰可合為一條，並在 description 概述其經過與起訖時間）；"
                        "但『不同的戰術階段、不同目標、或明顯不同的行動』則分開。"
                        "切勿以『時辰』或單一的前進／後退／紮營動作為單位拆分。"
                        "以本類奏摺為例，理想的切分大致是：攻陷彰化、佔據諸羅、分路進攻府城（北門陸路與西門海路）、鹽埕海路進攻、陸路萬人連日激戰、牛車棉被陣攻營、三面合圍、中伏潰敗——各為一條，而非把每次進退、每個時辰各拆一條。"
                        "【排除】背景或成因說明（例如為何能聚集數萬、漳民附從、羅漢腳加入、衙役多係賊黨等兵源分析）不是一次具體行動，不要輸出為事件；也勿納入僅屬計畫而尚未執行者。"
                        "重點是被奏報的實地行動本身，而非奏報這個動作。對每個事件給出：")
            prompt = (
                ctx
                + (("\n\n【分類規則】" + actor_instruction) if actor_instruction else "")
                + focus
                + task
                + "subtitle（簡短小標題，繁體中文，5-12字，如「匪徒攻陷彰化縣城」）、"
                "description（較完整的繁體中文敘述，1-3句，說明發生了什麼）、"
                'side（由你判斷此事件的『行動方』屬於哪一方，不要靠關鍵字，而是依文意理解：'
                '叛軍／民變一方（林爽文等）所執行的行動填 "lin"；清朝官方（官員、官軍、義民、鄉勇）所執行的行動填 "qing"；'
                '若確實無法判斷則填 "other"）、'
                "where（發生地點，盡量是具體地名）、"
                "who（涉及的人物或部隊，字串陣列；無則空陣列）、"
                "who_loc（物件，將 who 中每個人物對應到他此刻所在的單一地名；該地名可能與事件地點 where 不同，例如下令者在廈門、受令者在渡臺途中。"
                "只用原文中明示或可明確推得的地名；某人位置不明則略過或填空字串。只給地名，切勿杜撰經緯度）、"
                "relations（陣列，列出本事件人物之間『有方向』的關係邊；原文未明言則回傳空陣列）。"
                '每條邊為 {"source":來源人物,"target":目標人物,"relation":原文中的關係動詞或詞（如 派遣、委令、稟報、協同、攻打、擒拿、隸屬），'
                '"relation_type":必為 "command"|"report"|"ally"|"conflict"|"kinship"|"other" 之一,"evidence":支持此邊的簡短原文片段}、'
                "whenCh（事件發生的中曆日期，如「十一月二十六日」，若文中有）、"
                "whenAr（對應西曆 yyyy/mm/dd，若能合理推得，否則留空字串）、"
                "quote（從『原文』中盡量逐字節錄、可作為此事件依據的一段引文）、"
                "howKnown（此官員如何得知，如親歷、探報、轉述、訪聞）、"
                "whenKnownCh（官員得知的中曆日期，若有）。"
                '只輸出 JSON：{"events":[{"subtitle":"","description":"","side":"","where":"","who":[],"who_loc":{},"relations":[{"source":"","target":"","relation":"","relation_type":"","evidence":""}],"whenCh":"","whenAr":"","quote":"","howKnown":"","whenKnownCh":""}]}。'
                '若無相關事件，輸出 {"events":[]}。'
            )
            evs = _json_list(_vertex(prompt, True, p.get("model"), _mt(p)), "events")
            return _cors(jsonify({"mode": "events", "events": evs}))

        if mode == "zhupi":
            # extract every vermilion rescript (硃批): interlinear 夾批 + end 尾批; what it responds to + the emperor's view
            task = (
                "\n\n任務：找出本文書中『皇帝以硃筆批示』的所有硃批文字，包含："
                "（1）夾在奏摺正文中的『夾批』，與（2）文末的『尾批』。"
                "硃批常以特定語氣或套語出現（如『覽』『知道了』『該部議奏』『所辦甚是』『已有旨』『即有諭旨』『另有旨』等），請仔細辨識，不要把臣工奏報的內容誤判為硃批。"
                "對每一條硃批給出："
                "text（硃批原文，逐字）、"
                "position（此硃批的位置：『夾批』或『尾批』）、"
                "responds_to（此硃批所針對／回應的奏摺內容；盡量逐字引述該段原文，若無法明確對應則簡述）、"
                "opinion（皇帝在此硃批中所表達的態度、意見或指示之意涵，以繁體中文簡述）、"
                "title（可直接作為事件標題的一句話，繁體中文，約12-20字，須說明皇帝『對誰』表達了『什麼態度或指示』——"
                "盡量點名奏摺原奏之人（用原文中的姓名或職銜均可，勿用泛稱），而非只重複套語。"
                "例如「高度讚賞徐嗣曾要求地方官員不動聲色的穩妥做法」「申飭黃仕簡調度遲緩」。"
                "若該硃批僅為例行套語（marker 有值）,title 可簡述為「批『該部議奏』」之類，仍須完整、不可留空）、"
                "marker（若該硃批僅為例行套語，例如『已有旨』或『即有諭旨』『另有旨』之類，請在此填入該套語原文；否則留空字串）、"
                "where（此硃批所涉事件發生或相關的地點，盡量是具體地名；無則空字串）、"
                "who（涉及的人物或部隊，字串陣列；無則空陣列）、"
                "who_loc（物件，將 who 中每個人物對應到他此刻所在的單一地名；只用原文中明示或可明確推得的地名，只給地名，切勿杜撰經緯度；不明則略過或留空字串）、"
                "relations（陣列，列出 who 中人物之間『有方向』的關係邊；原文未明言則回傳空陣列，每條邊為 "
                '{"source":來源人物,"target":目標人物,"relation":原文中的關係動詞或詞（如 飭、諭、奏報、協同、攻打）,'
                '"relation_type":必為 "command"|"report"|"ally"|"conflict"|"kinship"|"other" 之一,"evidence":支持此邊的簡短原文片段}）。'
                "規則：若 marker 有值（屬例行套語），responds_to 與 opinion 可從簡或留空，不需深入分析，但 title 仍須填寫；"
                "where/who/who_loc/relations 這幾項用於製作人物關係圖與地圖，即使 marker 有值也請盡量依原文填寫，而非一併留空。"
                '\n\n只輸出 JSON：{"zhupi":[{"text":"","position":"","responds_to":"","opinion":"","title":"","marker":"",'
                '"where":"","who":[],"who_loc":{},"relations":[{"source":"","target":"","relation":"","relation_type":"","evidence":""}]}]}。'
                '若文中無硃批，輸出 {"zhupi":[]}。'
            )
            extra = (p.get("question") or "").strip()
            prompt = ctx + (("\n\n【使用者額外聚焦／要求（最高優先）】\n" + extra) if extra else "") + task
            items = _json_list(_vertex(prompt, True, p.get("model"), _mt(p)), "zhupi")
            return _cors(jsonify({"mode": "zhupi", "zhupi": items}))

        if mode == "edict_match":
            # given one memorial + several candidate 上諭, find which edicts respond to the memorial
            mem = p.get("memorial") or {}
            edicts = p.get("edicts") or []
            mem_block = (
                "【奏摺】\n編號：%s　標題：%s　日期：%s\n%s\n"
                % (mem.get("id", ""), mem.get("title", ""), mem.get("date", ""), mem.get("body", ""))
            )
            ed_block = "\n\n【候選上諭（請逐一判斷是否在回應上述奏摺）】\n"
            for e in edicts:
                ed_block += (
                    "──── edict_id=%s ｜ 日期：%s ｜ 標題：%s\n%s\n\n"
                    % (e.get("id", ""), e.get("date", ""), e.get("title", ""), e.get("body", ""))
                )
            task = (
                "\n\n任務：上面是一份奏摺，以及日期相近的一則或數則上諭。請判斷哪些上諭在回應這份奏摺"
                "（針對此奏摺所奏之事而發的指示、批答、駁斥或處置）。"
                "若有回應，請『詳盡且分面向地』分析，仿照史家逐項梳理的方式，切勿只給一句概述。"
                "對每一則確實回應此奏摺的上諭，給出："
                "edict_id（務必是上面標示的該則上諭 id）、"
                "summary（此上諭對該奏摺整體回應的概述，繁體中文 1-3 句）、"
                "points（回應要點陣列：把上諭對奏摺的回應拆成各個面向，例如『批評官員張皇失措』『對親渡臺的看法』"
                "『駁斥水陸提督俱渡重洋／簡派重臣之請』『申飭洩露軍情』『最終處置傳旨申飭』等）。"
                "每個要點給 aspect（該面向的簡短標題）、"
                "title（可直接作為事件標題的一句話，繁體中文，約12-20字，須說明皇帝『對誰』『針對什麼』做出『何種回應』——"
                "盡量點名奏摺原奏之人或事由，而非只重複 aspect 的泛稱分類。例如「駁斥福康安請自行赴臺之議」「申飭常青調度張皇」）、"
                "memorial_quote（奏摺中被回應的那段內容，逐字引文）、"
                "edict_quote（上諭中針對該內容回應的逐字引文，即皇帝原話，不可留空）、how（說明此面向如何回應，繁體中文）、"
                "where（此面向所涉事件發生或相關的地點，盡量是具體地名；無則空字串）、"
                "who（涉及的人物或部隊，字串陣列；無則空陣列）、"
                "who_loc（物件，將 who 中每個人物對應到他此刻所在的單一地名；只用原文中明示或可明確推得的地名，只給地名，切勿杜撰經緯度；不明則略過或留空字串）、"
                "relations（陣列，列出 who 中人物之間『有方向』的關係邊；原文未明言則回傳空陣列，每條邊為 "
                '{"source":來源人物,"target":目標人物,"relation":原文中的關係動詞或詞（如 飭、諭、奏報、協同、攻打）,'
                '"relation_type":必為 "command"|"report"|"ally"|"conflict"|"kinship"|"other" 之一,"evidence":支持此邊的簡短原文片段}）。'
                "務求完整，涵蓋上諭對此奏摺的所有重要回應點；每個要點都必須有 memorial_quote 與 edict_quote 的對應引文，且 title 不可留空。"
                "where/who/who_loc/relations 用於製作人物關係圖與地圖，請盡量依原文填寫。"
                "只列出確實回應這份奏摺者；無關的上諭不要列出。"
                '\n\n只輸出 JSON：{"matches":[{"edict_id":"","summary":"","points":[{"aspect":"","title":"","memorial_quote":"","edict_quote":"","how":"",'
                '"where":"","who":[],"who_loc":{},"relations":[{"source":"","target":"","relation":"","relation_type":"","evidence":""}]}]}]}。'
                '若皆無關，輸出 {"matches":[]}。'
            )
            extra = (p.get("question") or "").strip()
            prompt = mem_block + ed_block + (("\n\n【使用者額外要求】" + extra) if extra else "") + task
            matches = _json_list(_vertex(prompt, True, p.get("model"), _mt(p)), "matches")
            return _cors(jsonify({"mode": "edict_match", "matches": matches}))

        if mode == "official_response":
            # given one emperor action (硃批 or 諭) + several candidate documents dated in the
            # ~30 days after it, find which candidate is the addressed official's response.
            act = p.get("action") or {}
            addressee = (p.get("addressee") or "").strip()
            cands = p.get("candidates") or []
            act_block = (
                "【皇帝行動（硃批／諭）】\n日期：%s　標題／概要：%s\n原文引文：%s\n"
                % (act.get("dateAr") or act.get("whenCh") or "", act.get("what", ""), act.get("quote", ""))
            )
            addr_block = (
                ("\n指定回應官員：%s（僅在候選文書明確為此人所作、或明確代表此人回應時才判定為回應）\n" % addressee)
                if addressee else
                "\n請先從上面的硃批／諭原文判斷：皇帝此處是對『哪一位官員』（姓名或職銜）而發；"
                "將你的判斷填入回傳的 addressee 欄位。\n"
            )
            cand_block = "\n【候選文書（皆為此行動之後約30日內的文書，請逐一判斷是否為對此行動的回應】\n"
            for c in cands:
                cand_block += (
                    "──── doc_id=%s ｜ 日期：%s ｜ 標題：%s\n%s\n\n"
                    % (c.get("doc_id", ""), c.get("date", ""), c.get("title", ""), c.get("body", ""))
                )
            extra = (p.get("question") or "").strip()
            task = (
                "\n\n任務：判斷候選文書中，哪些是『被指定官員（或皇帝硃批／諭所針對之官員）』對上述硃批／諭的實際回應。"
                "只有當候選文書內文『明確』表明是在回應此硃批／諭（例如引述其內容、明言「奉旨」「欽遵」「硃批」「upon receiving...」之類，"
                "或談及與該行動高度吻合的具體事由）時才視為回應；不要僅因日期相近就判定。"
                "對每一則確實回應者，給出："
                "doc_id（務必是上面標示的候選文書 doc_id）、"
                "subtitle（可直接作為事件標題的一句話，繁體中文，約12-20字，須說明『此官員對此事做了什麼回應』——"
                "與 how 不同：subtitle 是精簡標題，how 才是完整敘述，兩者不可只是彼此的截斷或重複。"
                "例如「常青嚴查綠營諸將虛報戰功」，而非重複整句 how 的內容）、"
                "how（此官員如何回應的完整敘述，繁體中文，2-4句，須包含 subtitle 未能涵蓋的細節）、"
                "receive_date（此官員在文中提及自己收到該硃批／諭的日期，中曆或西曆皆可，若原文未提及則留空字串）、"
                "response_date（此回應文書本身發出／具奏的日期）、"
                "action_quote（原硃批／諭中，與此回應對應的引文——只需精簡摘出『被回應的那一句核心指示或問責』，"
                "通常一句話、至多兩句即可，不要整段照抄；若上面提供的引文本身已經很精簡則可直接使用）、"
                "response_quote（回應文書中，明確表明其在回應該硃批／諭的引文——盡量『完整』節錄整段相關文字"
                "（含前後語境，通常3-6句），而不是只摘一句，讓讀者不需查閱原文就能掌握完整回應內容，不可留空）、"
                "where（此回應所涉事件發生或相關的地點，盡量是具體地名；無則空字串）、"
                "who（涉及的人物或部隊，字串陣列；無則空陣列）、"
                "who_loc（物件，將 who 中每個人物對應到他此刻所在的單一地名；只用原文中明示或可明確推得的地名，只給地名，切勿杜撰經緯度；不明則略過或留空字串）、"
                "relations（陣列，列出 who 中人物之間『有方向』的關係邊；原文未明言則回傳空陣列，每條邊為 "
                '{"source":來源人物,"target":目標人物,"relation":原文中的關係動詞或詞（如 飭、諭、奏報、協同、攻打）,'
                '"relation_type":必為 "command"|"report"|"ally"|"conflict"|"kinship"|"other" 之一,"evidence":支持此邊的簡短原文片段}）。'
                "where/who/who_loc/relations 用於製作人物關係圖與地圖，請盡量依原文填寫。"
                '\n\n只輸出 JSON：{"addressee":"","items":[{"doc_id":"","subtitle":"","how":"","receive_date":"","response_date":"","action_quote":"","response_quote":"",'
                '"where":"","who":[],"who_loc":{},"relations":[{"source":"","target":"","relation":"","relation_type":"","evidence":""}]}]}。'
                '若皆無回應，輸出 {"addressee":"","items":[]}，但仍請填寫你判斷出的 addressee。'
            )
            prompt = act_block + addr_block + cand_block + (("\n\n【使用者額外要求】" + extra) if extra else "") + task
            data = _strip_json(_vertex(prompt, True, p.get("model"), _mt(p)))
            items = data.get("items", []) if isinstance(data, dict) else []
            guessed_addressee = (data.get("addressee", "") if isinstance(data, dict) else "") or addressee
            return _cors(jsonify({"mode": "official_response", "addressee": guessed_addressee, "items": items}))

        if mode == "event_one":
            text = (p.get("text") or "").strip()
            prompt = (
                "以下『描述文字』描述了一件史事（多為先前 AI 的摘要或使用者的說明）。"
                "請將它整理成『單一』事件的結構化資料。\n\n【描述文字】\n" + text + "\n\n"
                + (("【可供查證的原文（若包含支持此事件的句子，請取為 quote 並標明 doc_id）】\n" + ctx + "\n\n") if ctx else "")
                + '只輸出 JSON：{"event":{"subtitle":"","description":"","where":"","who":[],"who_loc":{},"relations":[{"source":"","target":"","relation":"","relation_type":"","evidence":""}],"whenCh":"","whenAr":"","quote":"","doc_id":"","howKnown":"","whenKnownCh":""}}。'
                "subtitle 為 5-12 字繁體中文小標題；description 為 1-3 句繁體中文敘述；where 為地點；who 為人物字串陣列；"
                "who_loc 為物件，將每位 who 對應到其所在地名（只給地名，勿杜撰經緯度，位置不明則略）；"
                'relations 為人物間有方向的關係邊陣列，每條為 {"source","target","relation":原文關係動詞,"relation_type":"command"|"report"|"ally"|"conflict"|"kinship"|"other","evidence":原文片段}，原文未明言則為空陣列；'
                "whenCh 為事件發生的中曆日期（若描述中有，如「十一月二十七日」）；whenAr 為西曆 yyyy/mm/dd（僅在能合理確定時，否則留空）；"
                "quote：若上述原文包含支持此事件的句子，填入逐字引文並於 doc_id 標明該文書編號；若無可用原文則留空。"
            )
            try:
                data = _strip_json(_vertex(prompt, True, p.get("model"), _mt(p)))
                ev = data.get("event", data if isinstance(data, dict) else {})
            except json.JSONDecodeError:
                ev = {}
            return _cors(jsonify({"mode": "event_one", "event": ev}))

        if mode == "trace":
            # reconstruct the information-transmission chain (情報傳遞鏈) behind ONE event
            ev = p.get("event") or {}
            subtitle = (ev.get("subtitle") or p.get("subtitle") or "").strip()
            desc = (ev.get("description") or "").strip()
            equote = (ev.get("quote") or "").strip()
            ewhere = (ev.get("where") or "").strip()
            ewhen = (ev.get("whenCh") or ev.get("whenAr") or "").strip()
            extra = (p.get("question") or "").strip()
            side = (p.get("side") or ev.get("actor") or "").strip()   # 'lin' | 'qing' | '' (both)
            side_label = "林爽文等民變一方（叛軍）" if side == "lin" else ("清朝官方（官員、官軍）" if side == "qing" else "")
            scan_all = not (subtitle or desc or equote)   # no target event → scan the whole document
            if scan_all:
                focus = (
                    "\n\n【任務範圍】請就整份文書，找出其中『所有』情報傳遞鏈。"
                    + (("\n使用者補充：" + extra + "\n") if extra else "")
                )
            else:
                focus = (
                    "\n\n【目標事件（需追溯其情報來源）】\n"
                    + ("小標題：" + subtitle + "\n" if subtitle else "")
                    + ("敘述：" + desc + "\n" if desc else "")
                    + ("地點：" + ewhere + "\n" if ewhere else "")
                    + ("事件日期：" + ewhen + "\n" if ewhen else "")
                    + ("文書中相關引文：" + equote + "\n" if equote else "")
                    + (("使用者補充：" + extra + "\n") if extra else "")
                )
            aim = ("\n\n任務：根據上述文書原文，找出文書中『所有』情報傳遞鏈（provenance / 情報傳遞鏈）。"
                   if scan_all else
                   "\n\n任務：根據上述文書原文，重建此事件『情報如何被得知與傳遞』的來源鏈（provenance / 情報傳遞鏈）。")
            task = (
                aim
                + "把每一條鏈建成一連串『傳遞動作（hop）』：每一個 hop 代表『某人在某時某地、以某種方式，把消息告知下一個人』，"
                "直到撰寫此文書的官員為止。"
                "範例：農民丙於十二月初五在臺灣親見此事 → 在臺灣告知營兵甲 → 甲於十二月初十在福建稟報官員乙（本文書作者）。"
                "這會產生兩個 hop：hop1 = 丙→甲；hop2 = 甲→乙。"
                "\n\n【重要：只用原文真正提到的人】只納入原文中『實際出現或明確指涉』的傳遞者與來源人物（具名者，或文中點明的具體身分如『某汛把總』『被擒賊目』『該縣典史』）。"
                "嚴禁為了補足第一手而虛構一個籠統、未具名的來源（例如沒有根據地填入『地方百姓』『探子』『難民』並標為『訪聞』）。"
                "若原文並未說明最初的第一手來源是誰，就讓該鏈『從原文點名的最早一位傳遞者開始』，不要再往下杜撰一層。"
                "寧可鏈短而可靠，也不要加入無原文依據的人物。"
                + "\n\n每個 hop 請給：from_person、to_person、place（傳遞動作發生的地點）、whenCh（中曆時間）、"
                "whenAr（西曆 yyyy/mm/dd，能合理推得才填，否則空字串）、how（傳遞方式：親見／目擊／口述／探報／訪聞／稟報／移會／咨會／轉述／傳聞 等）、"
                "quote（原文明載此次傳遞的逐字片段，否則空字串）、"
                "inferred（布林值：此 hop 若由文意脈絡『合理推斷』而非原文明載，填 true；但仍須有原文依據，不可純屬虛構）。"
                "layer 從 1 開始：layer 1 = 最接近本文書／最後一手，數字越大越接近第一手來源。"
            )
            task += (
                "\n\n把每一條獨立的傳遞路徑包成『一條來源鏈（chain）』。若情報透過『兩條以上互不相干的路徑』傳來，就輸出多條 chain。"
                "每條 chain 包含：hops（如上的傳遞動作陣列）、events（此鏈所報告或帶來的事件陣列）。"
                "每個 event 給：subtitle（簡短小標題）、reporter（此鏈中『實際報告或帶來此事件』的那一位人物姓名，必須是本鏈 hops 中出現的某個 from_person）、"
                "whenCh（事件中曆日期）、where（事件地點）、quote（原文中報告此事件的逐字佐證片段）。"
                "同一條鏈中不同人物可能各自報告不同事件，請逐一以 reporter 標明是誰報告的。"
                "務必為 hops 附上傳遞引文、為 events 附上事件引文。"
            )
            if side_label:
                task += (
                    "\n\n【側別限定】本次只關注『" + side_label + "』的事件："
                    "每條 chain 的 events 只列出屬於該方的事件（其他方的事件不要列入 events）。"
                    "若一條鏈同時傳遞了其他方的事件，仍可保留該鏈，但 events 僅放該方事件；"
                    "若一條鏈完全不涉及該方事件，則不需輸出該鏈。"
                )
            if (not scan_all) and p.get("single"):
                task += (
                    "\n\n【單一事件】本次只追溯上述『目標事件』本身："
                    "每條 chain 的 events 只放該目標事件一項，不要列出其他事件；"
                    "只輸出『確實傳遞了該目標事件』的來源鏈，與該目標事件無關的鏈不要輸出。"
                )
            prompt = (
                ctx + focus + task
                + '\n\n只輸出 JSON：{"chains":[{"hops":[{"layer":1,"from_person":"","to_person":"",'
                '"place":"","whenCh":"","whenAr":"","how":"","quote":"","inferred":false}],'
                '"events":[{"subtitle":"","reporter":"","whenCh":"","where":"","quote":""}]}]}。'
                '若文書中完全無從判斷來源，輸出 {"chains":[]}。'
            )
            chains = _json_list(_vertex(prompt, True, p.get("model"), _mt(p)), "chains")
            return _cors(jsonify({"mode": "trace", "chains": chains}))

        # ask
        q = p.get("question", "").strip() or "請解釋這份文書的重點。"
        hl = p.get("highlight")
        prompt = ctx
        if hl:
            prompt += f"\n\n使用者目前標示的引文：「{hl}」"
        prompt += f"\n\n使用者問題：{q}\n請用繁體中文回答，必要時引用原文。"
        return _cors(jsonify({"mode": "ask", "text": _vertex(prompt, False, p.get("model"))}))

    except requests.HTTPError as e:
        return _cors(jsonify({"error": f"Vertex error: {e.response.text[:500]}"})), 502
    except Exception as e:  # noqa: BLE001
        return _cors(jsonify({"error": repr(e)})), 500


@app.route("/geocode", methods=["GET", "POST", "OPTIONS"])
def geocode():
    # server-side passthrough to historical-placename gazetteers (avoids browser CORS).
    # src=twgis → NTU 臺灣歷史地名 (Taiwan); src=chgis → Harvard/Fudan CHGIS TGAZ (China)
    if request.method == "OPTIONS":
        return _cors(app.make_response(("", 204)))
    name = (request.args.get("n") or "").strip()
    src = (request.args.get("src") or "twgis").strip().lower()
    if not name:
        body = request.get_json(force=True, silent=True) or {}
        name = (body.get("n") or "").strip()
        src = (body.get("src") or src).strip().lower()
    if not name:
        return _cors(jsonify({"placenames": []}))
    try:
        if src == "chgis":
            r = requests.get(
                "https://chgis.hudci.org/tgaz/placename",
                params={"n": name, "fmt": "json"}, timeout=25,
            )
        else:
            r = requests.get(
                "https://docusky.org.tw/DocuSky/extApi/GeoCode/TWGIS/tw.php",
                params={"n": name}, timeout=20,
            )
        r.raise_for_status()
        # TWGIS returns a UTF-8 BOM + leading blank lines which break r.json(); decode with utf-8-sig
        data = json.loads(r.content.decode("utf-8-sig", "replace").strip())
        return _cors(jsonify(data))
    except Exception as e:  # noqa: BLE001
        return _cors(jsonify({"error": repr(e), "placenames": []})), 502


@app.route("/", methods=["GET"])
def health():
    return _cors(jsonify({"ok": True, "model": MODEL, "project": PROJECT, "location": LOCATION}))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
