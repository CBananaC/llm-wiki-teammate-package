"""Standalone Cloud Run proxy for ChatGPT through TokenRouter.

The browser / terminal batch runner calls this service with the same
document-oriented /chat contract used by the Gemini proxy. The TokenRouter
credential is server-side only: TOKENROUTER_API_KEY is never read from the
request body.

This proxy is a faithful port of the Gemini proxy's structured-task prompts.
Every /chat mode (summary, daysummary, divide, events, zhupi, edict_match,
official_response, event_one, trace, ask) builds the exact same detailed
instruction + JSON schema the Gemini proxy uses, so the ChatGPT models emit
the same rich fields (subtitle, who_loc, relations, howKnown, source chains,
etc.) the website and terminal runner expect. Only the transport layer
(TokenRouter chat/completions) is ChatGPT-specific.
"""
from __future__ import annotations

import json
import os
from urllib.parse import urlparse

import requests
from flask import Flask, g, jsonify, request


app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = int(os.environ.get("MAX_REQUEST_BYTES", "8388608"))

BASE_URL = os.environ.get("TOKENROUTER_BASE_URL", "https://www.tokenrouter.tech/v1").rstrip("/")
API_KEY = os.environ.get("TOKENROUTER_API_KEY", "")
DEFAULT_MODEL = os.environ.get("TOKENROUTER_DEFAULT_MODEL", "gpt-5.4")
ALLOWED_MODELS = [
    item.strip()
    for item in os.environ.get("TOKENROUTER_ALLOWED_MODELS", DEFAULT_MODEL).split(",")
    if item.strip()
]
# Default high enough that dense event / provenance JSON is never truncated.
MAX_TOKENS = int(os.environ.get("MAX_OUTPUT_TOKENS", "32768"))
REQUEST_TIMEOUT = int(os.environ.get("REQUEST_TIMEOUT_SECONDS", "120"))
ALLOW_ORIGIN = os.environ.get("ALLOW_ORIGIN", "*")
# Some OpenAI-compatible aggregators only accept "max_completion_tokens".
TOKEN_FIELD = os.environ.get("TOKENROUTER_TOKEN_FIELD", "max_tokens")
JSON_MODE = os.environ.get("TOKENROUTER_JSON_MODE", "json_object").lower() == "json_object"

SYSTEM = (
    "你正在協助研究林爽文（林爽文）戰爭（1786-1788）。你閱讀清代奏摺、硃批與上諭，"
    "必須忠於原文，不得杜撰事實。除非使用者另有要求，請使用繁體中文。"
)


# --------------------------------------------------------------------------- #
# CORS / context / JSON parsing helpers (ported from gemini-proxy)
# --------------------------------------------------------------------------- #
def _cors(resp):
    resp.headers["Access-Control-Allow-Origin"] = ALLOW_ORIGIN
    resp.headers["Access-Control-Allow-Headers"] = "Content-Type"
    resp.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    resp.headers["Cache-Control"] = "no-store"
    return resp


def _context(p: dict) -> str:
    parts = []
    if p.get("doc_id"):
        parts.append(f"文書編號：{p['doc_id']}（{p.get('doc_type', '')}）")
    if p.get("title"):
        parts.append(f"標題：{p['title']}")
    if p.get("body"):
        parts.append("原文：\n" + str(p["body"]))
    if p.get("rescript"):
        parts.append("硃批：\n" + str(p["rescript"]))
    if p.get("summary"):
        parts.append("既有結構化摘要（AI）：\n" + json.dumps(p["summary"], ensure_ascii=False))
    return "\n\n".join(parts)


def _defence(text: str) -> str:
    text = str(text or "").strip()
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
        if s < 0 or e < s:
            raise
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


def _find_list(value, key: str) -> list | None:
    aliases = {
        key.lower().replace("_", ""),
        key.rstrip("s").lower().replace("_", ""),
    }
    if key == "events":
        aliases.update({"items", "results", "eventlist", "事件", "事件列表"})
    if isinstance(value, list):
        return value
    if not isinstance(value, dict):
        return None
    for name, item in value.items():
        normalized = str(name).lower().replace("_", "").replace("-", "")
        if normalized in aliases:
            if isinstance(item, list):
                return item
            found = _find_list(item, key)
            if found is not None:
                return found
    for name in ("data", "result", "output", "response", "content"):
        nested = value.get(name)
        found = _find_list(nested, key)
        if found is not None:
            return found
    return None


def _json_list(raw: str, key: str) -> list:
    """Parse common compatible-API JSON shapes, then salvage complete objects."""
    t = _defence(raw)
    candidates = [t]
    for opening, closing in (("{", "}"), ("[", "]")):
        start, end = t.find(opening), t.rfind(closing)
        if start >= 0 and end > start:
            candidates.append(t[start:end + 1])
    for candidate in candidates:
        try:
            found = _find_list(json.loads(candidate), key)
            if found is not None:
                return found
        except json.JSONDecodeError:
            continue
    for alias in (key, "events", "items", "results", "事件", "事件列表"):
        found = _salvage_objects(t, alias)
        if found:
            return found
    return []


def _message_text(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, str):
                parts.append(item)
            elif isinstance(item, dict) and isinstance(item.get("text"), str):
                parts.append(item["text"])
        return "".join(parts)
    return ""


def _record_usage(data) -> None:
    """Stash token usage from a raw provider response on the per-request
    accumulator so /chat can report exact tokens per call."""
    try:
        if not isinstance(data, dict):
            return
        us = data.get("usage")
        if not isinstance(us, dict):
            return
        p = int(us.get("prompt_tokens") or us.get("input_tokens") or 0)
        c = int(us.get("completion_tokens") or us.get("output_tokens") or 0)
        t = int(us.get("total_tokens") or (p + c))
        if not (p or c or t):
            return
        lst = getattr(g, "_usage", None)
        if lst is None:
            lst = []
            g._usage = lst
        lst.append({"prompt": p, "completion": c, "total": t})
    except Exception:
        pass


@app.after_request
def _attach_usage(resp):
    try:
        if request.path.rstrip("/").endswith("/chat") and resp.status_code == 200 and resp.is_json:
            lst = getattr(g, "_usage", None) or []
            if lst:
                body = resp.get_json(silent=True)
                if isinstance(body, dict) and "usage" not in body:
                    body["usage"] = {
                        "prompt_tokens": sum(x["prompt"] for x in lst),
                        "completion_tokens": sum(x["completion"] for x in lst),
                        "total_tokens": sum(x["total"] for x in lst),
                        "calls": len(lst),
                    }
                    resp.set_data(json.dumps(body, ensure_ascii=False))
    except Exception:
        pass
    return resp


def _mt(p: dict):
    """Optional per-request output-token override."""
    try:
        v = int(p.get("max_output_tokens") or 0)
        return v if v > 0 else None
    except (TypeError, ValueError):
        return None


# --------------------------------------------------------------------------- #
# TokenRouter transport
# --------------------------------------------------------------------------- #
def _validated_model(value: str | None) -> str:
    model = str(value or DEFAULT_MODEL).strip()
    if not model or len(model) > 160 or any(ch in model for ch in "\r\n\0"):
        raise ValueError("Invalid model identifier")
    if os.environ.get("ENFORCE_MODEL_ALLOWLIST", "0") == "1" and ALLOWED_MODELS and model not in ALLOWED_MODELS:
        raise ValueError(f"Model is not allowed: {model}")
    return model


def _call(prompt: str, *, json_out: bool = False, model: str | None = None,
          max_tokens: int | None = None) -> str:
    if not API_KEY:
        raise RuntimeError("TokenRouter is not configured: set TOKENROUTER_API_KEY")
    parsed = urlparse(BASE_URL)
    if parsed.scheme != "https" or not parsed.hostname:
        raise RuntimeError("TOKENROUTER_BASE_URL must be an absolute HTTPS URL")
    body = {
        "model": _validated_model(model),
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": prompt},
        ],
        TOKEN_FIELD: max_tokens or MAX_TOKENS,
    }
    if json_out and JSON_MODE:
        body["response_format"] = {"type": "json_object"}
    response = requests.post(
        BASE_URL + "/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json; charset=utf-8",
        },
        data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    data = response.json()
    _record_usage(data)
    choices = data.get("choices") or []
    if not choices:
        raise RuntimeError("TokenRouter returned no completion choices")
    message = choices[0].get("message") or {}
    content = _message_text(message.get("content"))
    if not content:
        content = _message_text(message.get("reasoning_content")) or _message_text(message.get("reasoning"))
    if not content:
        raise RuntimeError("TokenRouter returned an empty completion")
    return content


def _generate(user_text: str, json_out: bool, payload: dict,
              max_tokens: int | None = None) -> str:
    """Signature-compatible with gemini-proxy's _generate so the /chat handler
    below can be a verbatim port. Always routes through TokenRouter."""
    return _call(user_text, json_out=json_out, model=payload.get("model"),
                 max_tokens=max_tokens)


# --------------------------------------------------------------------------- #
# Provider / model discovery
# --------------------------------------------------------------------------- #
@app.route("/providers", methods=["GET", "OPTIONS"])
def providers():
    if request.method == "OPTIONS":
        return _cors(app.make_response(("", 204)))
    return _cors(jsonify({
        "default_provider": "tokenrouter",
        "providers": [{
            "id": "tokenrouter",
            "label": "ChatGPT via TokenRouter",
            "enabled": bool(API_KEY),
            "default_model": DEFAULT_MODEL,
            "models": ALLOWED_MODELS or [DEFAULT_MODEL],
        }],
    }))


@app.route("/models", methods=["POST", "OPTIONS"])
def models():
    if request.method == "OPTIONS":
        return _cors(app.make_response(("", 204)))
    if not API_KEY:
        return _cors(jsonify({
            "provider": "tokenrouter",
            "models": ALLOWED_MODELS or [DEFAULT_MODEL],
            "default_model": DEFAULT_MODEL,
        }))
    try:
        response = requests.get(
            BASE_URL + "/models",
            headers={"Authorization": f"Bearer {API_KEY}"},
            timeout=min(REQUEST_TIMEOUT, 30),
        )
        response.raise_for_status()
        rows = response.json().get("data") or []
        found = [str(row.get("id")) for row in rows if isinstance(row, dict) and row.get("id")]
        return _cors(jsonify({
            "provider": "tokenrouter",
            "models": list(dict.fromkeys(found))[:200] or ALLOWED_MODELS or [DEFAULT_MODEL],
            "default_model": DEFAULT_MODEL,
        }))
    except requests.RequestException:
        return _cors(jsonify({
            "provider": "tokenrouter",
            "models": ALLOWED_MODELS or [DEFAULT_MODEL],
            "default_model": DEFAULT_MODEL,
        }))


# --------------------------------------------------------------------------- #
# /chat  — full structured-task port from gemini-proxy
# --------------------------------------------------------------------------- #
@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():
    if request.method == "OPTIONS":
        return _cors(app.make_response(("", 204)))
    p = request.get_json(force=True, silent=True) or {}
    mode = p.get("mode", "ask")
    ctx = _context(p)

    try:
        if mode == "summary":
            instruction = (p.get("instruction") or "").strip() or (
                "用繁體中文，為上述文書寫一段更精簡、流暢的摘要（約 3-5 句），"
                "突出最關鍵的人、事、時、地，避免逐句翻譯。"
            )
            prompt = ctx + "\n\n任務：" + instruction + "只輸出摘要文字。"
            return _cors(jsonify({"mode": "summary", "text": _generate(prompt, False, p)}))

        if mode == "daysummary":
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
            return _cors(jsonify({"mode": "daysummary", "summary": _generate(prompt, False, p)}))

        if mode == "divide":
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
            parts = _json_list(_generate(prompt, True, p, _mt(p)), "parts")
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
            if p.get("retry_empty"):
                task += (
                    "\n【重新檢查】前一次擷取得到空結果。請逐句重讀原文，特別檢查攻打、進兵、退守、"
                    "調兵、渡海、堵禦、追擊、攻陷、潰散、擒獲、派遣等已發生或本分類要求的具體行動。"
                    "只在全文確實沒有任何符合事件時才回傳空陣列。"
                )
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
            evs = _json_list(_generate(prompt, True, p, _mt(p)), "events")
            return _cors(jsonify({"mode": "events", "events": evs}))

        if mode == "zhupi":
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
            items = _json_list(_generate(prompt, True, p, _mt(p)), "zhupi")
            return _cors(jsonify({"mode": "zhupi", "zhupi": items}))

        if mode == "edict_match":
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
            matches = _json_list(_generate(prompt, True, p, _mt(p)), "matches")
            return _cors(jsonify({"mode": "edict_match", "matches": matches}))

        if mode == "official_response":
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
            data = _strip_json(_generate(prompt, True, p, _mt(p)))
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
                data = _strip_json(_generate(prompt, True, p, _mt(p)))
                ev = data.get("event", data if isinstance(data, dict) else {})
            except json.JSONDecodeError:
                ev = {}
            return _cors(jsonify({"mode": "event_one", "event": ev}))

        if mode == "trace":
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
                "\n\n【連結成單一條鏈】務必把整條情報路徑連成『一條不中斷的鏈』：A→B→C→…→本文書作者。"
                "每一位中繼者都必須同時有『收到』與『傳出』兩個方向（最初來源只有傳出；作者只有收到）。"
                "若甲轉乙、乙再轉丙，必須同時輸出 甲→乙 與 乙→丙 兩個 hop，不可略去中間任何一段，"
                "以致某人憑空成為無來源的『第一手』或無下家的『結尾』。最後一個 hop 的 to_person 必須是撰寫本文書的官員（作者）本人。"
                "\n\n【傳遞方向判定】依原文動詞判定 from→to，切勿弄反："
                "「甲字寄乙」「甲咨乙」「甲移會乙」「甲行乙／行據乙」＝甲（發送方）→乙（接收方）；"
                "「據X稟／據X稱」「准X咨」「奉X諭／奉X行」「接據X」＝X（發送方）→引述此句者（接收方）。"
                "巢狀引述請逐層拆解，例如「據A稟稱：准B咨，奉C行據D稟報：……。」方向為 D→C→B→A→作者。"
                "又如「二十九日彰邑大肚社番字寄淡屬大甲社通事，據稱……」＝彰邑大肚社番→淡屬大甲社通事→（再由大甲社通事轉報）淡水同知。"
                "\n\n【親歷限制】除非原文明確指出某人『親見／目擊／親歷／在場』，否則不要臆斷任何人為親歷者；"
                "對只知其為最初具名來源、卻未載其如何得知者，how 一律填其實際的傳遞動詞（如稟報、字寄、轉述），不要填『親歷』。"
                "特別注意：字寄、稟報、轉述、咨會、行文等皆為『傳遞動作』，不等於親歷；最初來源亦然。"
                "\n\n【完整保留具名者】若一次稟報／咨文由多人聯銜具名（如「淡水同知程峻、北路竹塹營守備董得魁稟報」），"
                "該 hop 的 from_person 必須完整列出所有具名者，不可只取其一或遺漏任何人。"
                "\n\n【人名限用原文所載】from_person／to_person 只能使用原文出現的職銜或姓名；原文只寫職銜（如「福建巡撫」）"
                "而未載姓名時一律照錄該職銜，嚴禁補入原文所無的姓名（即使你知道當時任職者是誰，例如不可自行寫成「福建巡撫徐嗣曾」）。"
                "\n\n【地點限原文】place／who_loc 只填原文明示或可明確推得的地名，不得依你對某人任職地的認識自行補填"
                "（例如身在福建的巡撫不可標到臺灣；大甲社通事在大甲社，不可標到大肚社）；地點不明則留空字串。"
                "\n\n【inferred 僅指推斷的傳遞連結】inferred=true 只用於『傳遞關係由文意推斷』的 hop；"
                "只要該 hop 兩端人物與傳遞事實均為原文明載（即使日期不明），即應 inferred=false，切勿因人物身分或缺日期而標為推斷。"
                "\n\n【中間日期勿臆造】whenCh 只填原文明載於該次傳遞的日期；原文未載者留空字串，不可套用鄰近 hop 的日期或自行推定。"
                "\n\n【模糊時間照錄】遇「十一月初間」「月底」等模糊時間，whenCh 照原文填入，不要轉為單一具體日期。"
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
            chains = _json_list(_generate(prompt, True, p, _mt(p)), "chains")
            return _cors(jsonify({"mode": "trace", "chains": chains}))

        # ask
        q = (p.get("question") or "").strip() or "請解釋這份文書的重點。"
        hl = (p.get("highlight") or "").strip()
        prompt = ctx
        if hl:
            prompt += f"\n\n使用者目前標示的引文：「{hl}」"
        prompt += f"\n\n使用者問題：{q}\n請用繁體中文回答，必要時引用原文。"
        return _cors(jsonify({"mode": "ask", "text": _generate(prompt, False, p)}))

    except ValueError as exc:
        return _cors(jsonify({"error": str(exc)})), 400
    except requests.HTTPError as exc:
        status = exc.response.status_code if exc.response is not None else 502
        detail = (exc.response.text if exc.response is not None else str(exc))[:500]
        return _cors(jsonify({"error": f"TokenRouter upstream error ({status}): {detail}"})), 502
    except Exception as exc:  # noqa: BLE001
        return _cors(jsonify({"error": str(exc) or exc.__class__.__name__})), 500


@app.route("/geocode", methods=["GET", "POST", "OPTIONS"])
def geocode():
    if request.method == "OPTIONS":
        return _cors(app.make_response(("", 204)))
    name = (request.args.get("n") or "").strip()
    source = (request.args.get("src") or "twgis").strip().lower()
    if not name:
        body = request.get_json(force=True, silent=True) or {}
        name = str(body.get("n") or "").strip()
        source = str(body.get("src") or source).strip().lower()
    if not name:
        return _cors(jsonify({"placenames": []}))
    try:
        if source == "chgis":
            response = requests.get(
                "https://chgis.hudci.org/tgaz/placename",
                params={"n": name, "fmt": "json"}, timeout=25,
            )
            response.raise_for_status()
            return _cors(jsonify(response.json()))
        response = requests.get(
            "https://docusky.org.tw/DocuSky/extApi/GeoCode/TWGIS/tw.php",
            params={"n": name}, timeout=20,
        )
        response.raise_for_status()
        # TWGIS returns a UTF-8 BOM + leading blank lines which break .json(); decode with utf-8-sig
        data = json.loads(response.content.decode("utf-8-sig", "replace").strip())
        return _cors(jsonify(data))
    except Exception as exc:  # noqa: BLE001
        return _cors(jsonify({"error": repr(exc), "placenames": []})), 502


@app.route("/", methods=["GET"])
def health():
    return _cors(jsonify({
        "ok": True,
        "provider": "tokenrouter",
        "model": DEFAULT_MODEL,
        "base_url": BASE_URL,
        "configured": bool(API_KEY),
    }))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
