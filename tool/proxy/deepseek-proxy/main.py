"""Standalone Google Cloud Vertex/MaaS proxy for DeepSeek."""
from __future__ import annotations

import json
import os

import google.auth
import google.auth.transport.requests
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = int(os.environ.get("MAX_REQUEST_BYTES", "8388608"))

PROJECT = os.environ.get("GCP_PROJECT", "")
LOCATION = os.environ.get("VERTEX_LOCATION", "global")
MODEL = os.environ.get("DEEPSEEK_MODEL", "deepseek-v3.2-maas")
MAX_TOKENS = int(os.environ.get("MAX_OUTPUT_TOKENS", "8192"))
REQUEST_TIMEOUT = int(os.environ.get("REQUEST_TIMEOUT_SECONDS", "600"))
ALLOW_ORIGIN = os.environ.get("ALLOW_ORIGIN", "*")
_CREDS = None

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


def _credentials():
    global _CREDS, PROJECT
    if _CREDS is None:
        _CREDS, adc_project = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
        PROJECT = PROJECT or adc_project or ""
    if not PROJECT:
        raise RuntimeError("Set GCP_PROJECT or configure Application Default Credentials")
    return _CREDS


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


def _tokens(value) -> int:
    try:
        number = int(value)
        return number if number > 0 else MAX_TOKENS
    except (TypeError, ValueError):
        return MAX_TOKENS


def _call(prompt: str, *, json_out=False, model=None, max_tokens=None) -> str:
    creds = _credentials()
    creds.refresh(google.auth.transport.requests.Request())
    model_name = str(model or MODEL).strip()
    if model_name.removeprefix("deepseek-ai/") != "deepseek-v3.2-maas":
        raise ValueError("Google Cloud DeepSeek model must be deepseek-v3.2-maas")
    url = (
        f"https://aiplatform.googleapis.com/v1/projects/{PROJECT}/locations/global"
        "/endpoints/openapi/chat/completions"
    )
    body = {
        "model": "deepseek-ai/deepseek-v3.2-maas",
        "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}],
        "temperature": 0.2,
        "top_p": 0.9,
        "max_tokens": _tokens(max_tokens),
        "chat_template_kwargs": {"thinking": False},
    }
    if json_out:
        body["response_format"] = {"type": "json_object"}
    response = requests.post(
        url,
        headers={"Authorization": f"Bearer {creds.token}", "Content-Type": "application/json; charset=utf-8"},
        data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    choices = response.json().get("choices") or []
    if not choices:
        raise RuntimeError("Google Cloud DeepSeek returned no completion choices")
    message = choices[0].get("message") or {}
    text = message.get("content") or message.get("reasoning_content") or message.get("reasoning")
    if isinstance(text, list):
        text = "".join(item if isinstance(item, str) else str(item.get("text", "")) for item in text if isinstance(item, (str, dict)))
    if not text:
        raise RuntimeError("Google Cloud DeepSeek returned an empty completion")
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


def _edict_match_prompt(p: dict) -> tuple[str, str, dict[str, str]]:
    mem = p.get("memorial") or {}
    edicts = p.get("edicts") or []
    memorial_body = str(mem.get("body") or "")
    edict_bodies = {
        str(e.get("id") or "").strip(): str(e.get("body") or "")
        for e in edicts if e.get("id")
    }
    mem_block = (
        "【奏摺】\n編號：%s　標題：%s　日期：%s\n%s\n"
        % (mem.get("id", ""), mem.get("title", ""), mem.get("date", ""), mem.get("body", ""))
    )
    ed_block = "\n\n【候選上諭（請逐一判斷是否在回應上述奏摺）】\n"
    for edict in edicts:
        ed_block += (
            "──── edict_id=%s ｜ 日期：%s ｜ 標題：%s\n%s\n\n"
            % (edict.get("id", ""), edict.get("date", ""), edict.get("title", ""), edict.get("body", ""))
        )
    extra = str(p.get("question") or "").strip()
    task = (
        "\n\n任務：判斷候選上諭中哪些確實在回應上述奏摺。日期相近、人物相同或主題相似本身不足以構成回應；"
        "必須能在奏摺與上諭之間找到具體、逐字可核對的內容對應。"
        "每則確實相關的上諭只輸出一個 match，給出 edict_id、summary，以及 points。"
        "每個 point 必須包含 aspect、title、memorial_quote、edict_quote、how、where、who、who_loc、relations。"
        "memorial_quote 必須逐字引自奏摺；edict_quote 必須逐字引自該上諭；兩者不可留空。"
        "若沒有至少一組可核對的雙邊引文，該上諭不得列為相關。不要為無關候選輸出空物件或佔位 match。"
        "title 請用繁體中文，約12至20字，說明皇帝對誰、針對何事、作出何種回應。"
        "relations 的 relation_type 只可為 command、report、ally、conflict、kinship、other。"
        "\n\n只輸出 JSON：{\"matches\":[{\"edict_id\":\"\",\"summary\":\"\",\"points\":[{"
        "\"aspect\":\"\",\"title\":\"\",\"memorial_quote\":\"\",\"edict_quote\":\"\",\"how\":\"\","
        "\"where\":\"\",\"who\":[],\"who_loc\":{},\"relations\":[{\"source\":\"\",\"target\":\"\","
        "\"relation\":\"\",\"relation_type\":\"\",\"evidence\":\"\"}]}]}]}。"
        "若皆無關，輸出 {\"matches\":[]}。"
    )
    prompt = mem_block + ed_block
    if extra:
        prompt += "\n\n【使用者額外要求】" + extra
    return prompt + task, memorial_body, edict_bodies


def _quote_in_source(quote: str, source: str) -> bool:
    normalized_quote = "".join(str(quote or "").split())
    normalized_source = "".join(str(source or "").split())
    return bool(normalized_quote) and normalized_quote in normalized_source


def _validated_edict_matches(data, memorial_body: str, edict_bodies: dict[str, str]) -> list[dict]:
    raw_matches = data.get("matches", []) if isinstance(data, dict) else []
    matches = []
    for item in raw_matches:
        if not isinstance(item, dict):
            continue
        edict_id = str(item.get("edict_id") or "").strip()
        if not edict_id or edict_id not in edict_bodies:
            continue
        points = []
        for point in item.get("points") or []:
            if not isinstance(point, dict):
                continue
            memorial_quote = str(point.get("memorial_quote") or "").strip()
            edict_quote = str(point.get("edict_quote") or "").strip()
            if not _quote_in_source(memorial_quote, memorial_body):
                continue
            if not _quote_in_source(edict_quote, edict_bodies[edict_id]):
                continue
            points.append(point)
        if not points:
            continue
        matches.append({
            "edict_id": edict_id,
            "summary": str(item.get("summary") or "").strip(),
            "points": points,
        })
    return matches


@app.route("/", methods=["GET"])
def health():
    return _cors(jsonify({"ok": True, "provider": "deepseek-vertex", "model": MODEL, "location": LOCATION, "project": PROJECT or None}))


@app.route("/providers", methods=["GET", "OPTIONS"])
def providers():
    if request.method == "OPTIONS":
        return _cors(app.make_response(("", 204)))
    return _cors(jsonify({"default_provider": "deepseek", "providers": [{
        "id": "deepseek", "label": "DeepSeek via Google Cloud", "enabled": True,
        "default_model": MODEL, "models": [MODEL],
    }]}))


@app.route("/models", methods=["POST", "OPTIONS"])
def models():
    if request.method == "OPTIONS":
        return _cors(app.make_response(("", 204)))
    return _cors(jsonify({"provider": "deepseek", "models": [MODEL], "default_model": MODEL}))


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
        if mode == "edict_match":
            prompt, memorial_body, edict_bodies = _edict_match_prompt(p)
            data = _json_value(_call(prompt, json_out=True, model=p.get("model"), max_tokens=p.get("max_output_tokens")))
            matches = _validated_edict_matches(data, memorial_body, edict_bodies)
            return _cors(jsonify({"mode": mode, "matches": matches}))
        if mode == "trace":
            data = _json_value(_call(_trace_prompt(p, ctx), json_out=True, model=p.get("model"), max_tokens=p.get("max_output_tokens")))
            chains = data.get("chains", []) if isinstance(data, dict) else []
            return _cors(jsonify({"mode": mode, "chains": chains}))
        if mode in SHAPES:
            data = _json_value(_call(_structured_prompt(mode, p, ctx), json_out=True, model=p.get("model"), max_tokens=p.get("max_output_tokens")))
            return _cors(jsonify({"mode": mode, **(data if isinstance(data, dict) else SHAPES[mode])}))
        question = str(p.get("question") or "請解釋這份文書的重點。")
        prompt = ctx + f"\n\n使用者問題：{question}\n請用繁體中文回答。"
        return _cors(jsonify({"mode": "ask", "text": _call(prompt, model=p.get("model"))}))
    except ValueError as exc:
        return _cors(jsonify({"error": str(exc)})), 400
    except requests.HTTPError as exc:
        status = exc.response.status_code if exc.response is not None else 502
        detail = (exc.response.text if exc.response is not None else str(exc))[:500]
        client_status = status if status in {429, 500, 502, 503, 504} else 502
        return _cors(jsonify({"error": f"DeepSeek upstream error ({status}): {detail}"})), client_status
    except Exception as exc:  # noqa: BLE001
        return _cors(jsonify({"error": str(exc) or exc.__class__.__name__})), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
