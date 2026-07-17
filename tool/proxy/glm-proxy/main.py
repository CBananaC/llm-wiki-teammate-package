"""Standalone GLM proxy using the same OpenAI-compatible provider as GPT."""
from __future__ import annotations

import json
import os
from urllib.parse import urlparse

import requests
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = int(os.environ.get("MAX_REQUEST_BYTES", "8388608"))

BASE_URL = os.environ.get("GLM_BASE_URL", "https://www.tokenrouter.tech/v1").rstrip("/")
API_KEY = os.environ.get("GLM_API_KEY") or os.environ.get("TOKENROUTER_API_KEY", "")
DEFAULT_MODEL = os.environ.get("GLM_MODEL", "glm-5.2")
ALLOWED_MODELS = [
    item.strip() for item in os.environ.get("GLM_ALLOWED_MODELS", DEFAULT_MODEL).split(",") if item.strip()
]
MAX_TOKENS = int(os.environ.get("MAX_OUTPUT_TOKENS", "16384"))
REQUEST_TIMEOUT = int(os.environ.get("REQUEST_TIMEOUT_SECONDS", "120"))
ALLOW_ORIGIN = os.environ.get("ALLOW_ORIGIN", "*")
JSON_MODE = os.environ.get("GLM_JSON_MODE", "1") == "1"

SYSTEM = (
    "你正在協助研究林爽文（林爽文）戰爭（1786-1788）。你閱讀清代奏摺、硃批與上諭，"
    "必須忠於原文，不得杜撰事實。除非使用者另有要求，請使用繁體中文。"
)

SHAPES = {
    "events": {"events": [{"subtitle": "", "description": "", "side": "", "where": "", "who": [], "quote": "", "whenCh": "", "whenAr": ""}]},
    "zhupi": {"zhupi": [{"text": "", "position": "", "responds_to": "", "opinion": "", "title": "", "where": "", "who": []}]},
    "edict_match": {"matches": []},
    "official_response": {"addressee": "", "items": []},
    "event_one": {"event": {}},
    "trace": {"chains": []},
}


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
        parts.append("既有摘要：\n" + json.dumps(p["summary"], ensure_ascii=False))
    return "\n\n".join(parts)


def _json_value(text: str):
    text = str(text or "").strip()
    if text.startswith("```"):
        text = text.split("```", 2)[1]
        if text.lower().startswith("json"):
            text = text[4:]
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError:
        starts = [x for x in (text.find("{"), text.find("[")) if x >= 0]
        start, end = min(starts, default=-1), max(text.rfind("}"), text.rfind("]"))
        if start < 0 or end < start:
            raise
        return json.loads(text[start:end + 1])


def _model(value: str | None) -> str:
    model = str(value or DEFAULT_MODEL).strip()
    if not model or len(model) > 160 or any(ch in model for ch in "\r\n\0"):
        raise ValueError("Invalid model identifier")
    if os.environ.get("ENFORCE_MODEL_ALLOWLIST", "0") == "1" and ALLOWED_MODELS and model not in ALLOWED_MODELS:
        raise ValueError(f"Model is not allowed: {model}")
    return model


def _tokens(value) -> int:
    try:
        number = int(value)
        return number if number > 0 else MAX_TOKENS
    except (TypeError, ValueError):
        return MAX_TOKENS


def _call(prompt: str, *, json_out=False, model=None, max_tokens=None) -> str:
    if not API_KEY:
        raise RuntimeError("GLM is not configured: set GLM_API_KEY")
    parsed = urlparse(BASE_URL)
    if parsed.scheme != "https" or not parsed.hostname:
        raise RuntimeError("GLM_BASE_URL must be an absolute HTTPS URL")
    body = {
        "model": _model(model),
        "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}],
        "max_tokens": _tokens(max_tokens),
    }
    if json_out and JSON_MODE:
        body["response_format"] = {"type": "json_object"}
    response = requests.post(
        BASE_URL + "/chat/completions",
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json; charset=utf-8"},
        data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    choices = response.json().get("choices") or []
    if not choices:
        raise RuntimeError("GLM provider returned no completion choices")
    message = choices[0].get("message") or {}
    text = message.get("content") or message.get("reasoning_content") or message.get("reasoning")
    if isinstance(text, list):
        text = "".join(item if isinstance(item, str) else str(item.get("text", "")) for item in text if isinstance(item, (str, dict)))
    if not text:
        raise RuntimeError("GLM provider returned an empty completion")
    return text


def _structured_prompt(mode: str, p: dict, ctx: str) -> str:
    instruction = "\n\n".join(str(p.get(k) or "").strip() for k in ("actor_instruction", "instruction", "question") if p.get(k))
    safe_fields = {k: v for k, v in p.items() if k not in {"api_key", "body", "summary", "rescript", "actor_instruction", "instruction", "question"}}
    return (
        ctx + "\n\n任務：根據原文完成此結構化研究工作，只使用原文支持的資訊，不得杜撰。"
        + ("\n補充規則：\n" + instruction if instruction else "")
        + "\n只輸出 JSON，不要 Markdown。外層格式必須是："
        + json.dumps(SHAPES[mode], ensure_ascii=False)
        + "\n工作模式：" + mode + "\n請保留逐字 quote；無證據時填空。"
        + "\n請求欄位：" + json.dumps(safe_fields, ensure_ascii=False)
    )


def _trace_prompt(p: dict, ctx: str) -> str:
    """Use the same strict provenance contract as the Gemini proxy."""
    event = p.get("event") or {}
    subtitle = str(event.get("subtitle") or p.get("subtitle") or "").strip()
    description = str(event.get("description") or "").strip()
    event_quote = str(event.get("quote") or "").strip()
    event_where = str(event.get("where") or "").strip()
    event_when = str(event.get("whenCh") or event.get("whenAr") or "").strip()
    extra = str(p.get("question") or "").strip()
    scan_all = not (subtitle or description or event_quote)
    if scan_all:
        focus = "\n\n【任務範圍】請就整份文書，找出其中『所有』情報傳遞鏈。"
    else:
        fields = [
            ("小標題", subtitle), ("敘述", description), ("地點", event_where),
            ("事件日期", event_when), ("文書中相關引文", event_quote),
        ]
        focus = "\n\n【目標事件（需追溯其情報來源）】\n" + "".join(
            f"{label}：{value}\n" for label, value in fields if value
        )
    if extra:
        focus += "使用者補充：" + extra + "\n"
    task = (
        "\n\n任務：根據上述文書原文，重建情報如何被得知與傳遞的來源鏈。"
        "每個 hop 代表某人把消息傳給下一人，整條路徑必須不中斷地連成 A→B→C→…→本文書作者；"
        "中繼者必須同時有收到與傳出，最後一個 hop 的 to_person 必須是本文書作者。"
        "\n\n【只用原文人物】只納入原文實際出現或明確指涉的人；不得虛構百姓、探子、難民等來源。"
        "原文未載最初來源時，從最早具名傳遞者開始。多人聯銜具名必須全部保留。"
        "from_person／to_person 只能照錄原文職銜或姓名，不得補入原文未載姓名。"
        "\n\n【作者引介來源的完整引文】若本文作者先寫明如何取得或查訊該來源，再以「據供／據稱／供稱」引出事件，"
        "該 hop 的 quote 應優先從同一段作者引介句開始，保留如「茲於本月十六日據防卡官兵拿獲奸細僧人西葉、心向、新法三名」的來源辨識語。"
        "這只是完整證據引文，不要因此虛構防卡官兵為額外傳遞者；只有原文確實說其傳遞消息時才新增 hop。若無法定位作者引介句，quote 可只保留據供／據稱後的逐字內容。"
        "\n\n【方向】「甲字寄乙」「甲咨乙」「甲移會乙」「甲行乙／行據乙」＝甲→乙；"
        "「據X稟／據X稱」「准X咨」「奉X諭／奉X行」「接據X」＝X→引述者。"
        "巢狀的「據A稟稱：准B咨，奉C行據D稟報」必須拆成 D→C→B→A→作者。"
        "「彰邑大肚社番字寄淡屬大甲社通事，據稱」必須是彰邑大肚社番→淡屬大甲社通事→淡水同知。"
        "\n\n【角色】只有整條鏈最後收到消息並撰寫本文書的人才是撰文者；"
        "福建巡撫、福建桐山營遊擊等只要仍把消息向後轉送，就是中繼者，不得標成撰文者或第一手。"
        "\n\n【親歷】只有原文明寫親見、目擊、親歷或在場才可填親歷。"
        "字寄、稟報、轉述、咨會、行文及最初具名來源均不等於親歷；how 應填實際傳遞動詞。"
        "\n\n【日期】whenCh 只填原文明載於該次傳遞的日期；事件日期或收文日期不可冒充發送日期，"
        "也不可套用鄰近 hop 日期。原文未載則留空；十一月初間、月底等模糊時間照錄，不得具體化。"
        "\n\n【地點與推斷】place 只填原文明示或可由該句明確推得的傳遞地點；不明留空。"
        "inferred=true 只表示傳遞連結由文意推斷；缺日期不等於推斷。"
        "\n\n每個 hop 給 layer、from_person、to_person、place、whenCh、whenAr、how、quote、inferred。"
        "layer 1 最接近本文書作者，數字越大越接近最早來源。quote 必須是原文明載該次傳遞的逐字片段。"
        "每條 chain 另給 events；每個 event 給 subtitle、reporter、whenCh、where、quote，reporter 必須出現在該鏈。"
    )
    side = str(p.get("side") or event.get("actor") or "").strip()
    if side in {"lin", "qing"}:
        label = "林爽文等民變一方（叛軍）" if side == "lin" else "清朝官方（官員、官軍）"
        task += f"\n\n【側別限定】events 只列屬於{label}的事件；完全不涉及該方的鏈不要輸出。"
    if not scan_all and p.get("single"):
        task += "\n\n【單一事件】只追溯目標事件；每條 chain 的 events 只放該事件，無關鏈不要輸出。"
    schema = (
        '{"chains":[{"hops":[{"layer":1,"from_person":"","to_person":"",'
        '"place":"","whenCh":"","whenAr":"","how":"","quote":"","inferred":false}],'
        '"events":[{"subtitle":"","reporter":"","whenCh":"","where":"","quote":""}]}]}'
    )
    return ctx + focus + task + "\n\n只輸出 JSON，不要 Markdown。外層格式必須是：" + schema + "。無法判斷時輸出 {\"chains\":[]}。"


@app.route("/", methods=["GET"])
def health():
    return _cors(jsonify({"ok": True, "provider": "glm", "model": DEFAULT_MODEL, "base_url": BASE_URL, "configured": bool(API_KEY)}))


@app.route("/providers", methods=["GET", "OPTIONS"])
def providers():
    if request.method == "OPTIONS":
        return _cors(app.make_response(("", 204)))
    return _cors(jsonify({"default_provider": "glm", "providers": [{
        "id": "glm", "label": "GLM via TokenRouter", "enabled": bool(API_KEY),
        "default_model": DEFAULT_MODEL, "models": ALLOWED_MODELS or [DEFAULT_MODEL],
    }]}))


@app.route("/models", methods=["POST", "OPTIONS"])
def models():
    if request.method == "OPTIONS":
        return _cors(app.make_response(("", 204)))
    if not API_KEY:
        return _cors(jsonify({"provider": "glm", "models": ALLOWED_MODELS, "default_model": DEFAULT_MODEL}))
    try:
        r = requests.get(BASE_URL + "/models", headers={"Authorization": f"Bearer {API_KEY}"}, timeout=min(REQUEST_TIMEOUT, 30))
        r.raise_for_status()
        found = [str(row.get("id")) for row in (r.json().get("data") or []) if isinstance(row, dict) and row.get("id")]
        return _cors(jsonify({"provider": "glm", "models": list(dict.fromkeys(found))[:200] or ALLOWED_MODELS, "default_model": DEFAULT_MODEL}))
    except requests.RequestException:
        return _cors(jsonify({"provider": "glm", "models": ALLOWED_MODELS, "default_model": DEFAULT_MODEL}))


@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():
    if request.method == "OPTIONS":
        return _cors(app.make_response(("", 204)))
    p = request.get_json(force=True, silent=True) or {}
    mode, ctx = str(p.get("mode") or "ask"), _context(p)
    try:
        if mode == "summary":
            instruction = str(p.get("instruction") or "用繁體中文寫一段 3-5 句摘要，突出最關鍵的人、事、時、地。")
            return _cors(jsonify({"mode": mode, "text": _call(ctx + "\n\n任務：" + instruction + "只輸出摘要文字。", model=p.get("model"))}))
        if mode == "daysummary":
            label = str(p.get("period_start") or "")
            if p.get("period_end") and p.get("period_end") != p.get("period_start"):
                label += " 至 " + str(p["period_end"])
            prompt = f"時間軸期間：{label}\n事件列表：\n{p.get('events_text') or '（無事件）'}\n\n請寫 3-6 句繁體中文敘事摘要，只根據列表。"
            return _cors(jsonify({"mode": mode, "summary": _call(prompt, model=p.get("model"))}))
        if mode == "divide":
            prompt = ctx + "\n\n任務：將原文切分為連續段落，提供 label、summary、excerpt。只輸出 JSON：{\"parts\":[{\"label\":\"\",\"summary\":\"\",\"excerpt\":\"\"}]}"
            data = _json_value(_call(prompt, json_out=True, model=p.get("model"), max_tokens=p.get("max_output_tokens")))
            parts = data.get("parts", []) if isinstance(data, dict) else data if isinstance(data, list) else []
            return _cors(jsonify({"mode": mode, "parts": parts}))
        if mode == "trace":
            data = _json_value(_call(_trace_prompt(p, ctx), json_out=True, model=p.get("model"), max_tokens=p.get("max_output_tokens")))
            chains = data.get("chains", []) if isinstance(data, dict) else []
            return _cors(jsonify({"mode": mode, "chains": chains}))
        if mode in SHAPES:
            data = _json_value(_call(_structured_prompt(mode, p, ctx), json_out=True, model=p.get("model"), max_tokens=p.get("max_output_tokens")))
            return _cors(jsonify({"mode": mode, **(data if isinstance(data, dict) else SHAPES[mode])}))
        question = str(p.get("question") or "請解釋這份文書的重點。")
        highlight = str(p.get("highlight") or "")
        prompt = ctx + ("\n\n使用者標示引文：「" + highlight + "」" if highlight else "") + f"\n\n使用者問題：{question}\n請用繁體中文回答。"
        return _cors(jsonify({"mode": "ask", "text": _call(prompt, model=p.get("model"))}))
    except ValueError as exc:
        return _cors(jsonify({"error": str(exc)})), 400
    except requests.HTTPError as exc:
        status = exc.response.status_code if exc.response is not None else 502
        detail = (exc.response.text if exc.response is not None else str(exc))[:500]
        return _cors(jsonify({"error": f"GLM upstream error ({status}): {detail}"})), 502
    except Exception as exc:  # noqa: BLE001
        return _cors(jsonify({"error": str(exc) or exc.__class__.__name__})), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
