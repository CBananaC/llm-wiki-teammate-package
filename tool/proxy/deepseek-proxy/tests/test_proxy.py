import importlib.util
import json
import unittest
from pathlib import Path
from unittest.mock import Mock, patch


MODULE_PATH = Path(__file__).resolve().parents[1] / "main.py"
SPEC = importlib.util.spec_from_file_location("deepseek_proxy", MODULE_PATH)
proxy = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(proxy)


class DeepSeekProxyTests(unittest.TestCase):
    def test_health_and_models(self):
        client = proxy.app.test_client()
        self.assertEqual(client.get("/").status_code, 200)
        self.assertEqual(client.post("/models", json={}).get_json()["models"], ["deepseek-v3.2-maas"])

    def test_chat_uses_vertex_openai_endpoint(self):
        creds = Mock(token="vertex-token")
        upstream = Mock()
        upstream.raise_for_status.return_value = None
        upstream.json.return_value = {"choices": [{"message": {"content": "ok"}}]}
        with (
            patch.object(proxy, "PROJECT", "test-project"),
            patch.object(proxy, "_credentials", return_value=creds),
            patch.object(proxy.requests, "post", return_value=upstream) as post,
        ):
            response = proxy.app.test_client().post("/chat", json={"mode": "ask", "question": "你好"})
        self.assertEqual(response.get_json(), {"mode": "ask", "text": "ok"})
        self.assertIn("projects/test-project/locations/global/endpoints/openapi/chat/completions", post.call_args.args[0])
        body = json.loads(post.call_args.kwargs["data"])
        self.assertEqual(body["model"], "deepseek-ai/deepseek-v3.2-maas")
        self.assertEqual(post.call_args.kwargs["headers"]["Authorization"], "Bearer vertex-token")

    def test_edict_match_requires_paired_evidence_and_known_id(self):
        completion = json.dumps({
            "matches": [
                {
                    "edict_id": "諭84",
                    "summary": "上諭直接回應奏摺。",
                    "points": [{
                        "aspect": "濱海截拿",
                        "title": "命徐嗣曾嚴查濱海口岸",
                        "memorial_quote": "尤宜嚴密截拿",
                        "edict_quote": "尤應於濱海各縣口岸汊港，嚴密截拿",
                        "how": "上諭重申並批准奏摺所陳措施。",
                    }],
                },
                {"edict_id": "諭84", "summary": "empty", "points": []},
                {
                    "edict_id": "諭999",
                    "summary": "unknown",
                    "points": [{"memorial_quote": "甲", "edict_quote": "乙"}],
                },
            ]
        }, ensure_ascii=False)
        payload = {
            "mode": "edict_match",
            "model": "deepseek-v3.2-maas",
            "memorial": {"id": "硃125", "title": "奏摺", "date": "1787/02/01", "body": "尤宜嚴密截拿"},
            "edicts": [{"id": "諭84", "date": "1787/02/01", "title": "上諭", "body": "尤應嚴密截拿"}],
        }
        with patch.object(proxy, "_call", return_value=completion) as call:
            response = proxy.app.test_client().post("/chat", json=payload)
        self.assertEqual(response.status_code, 200)
        matches = response.get_json()["matches"]
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["edict_id"], "諭84")
        self.assertEqual(len(matches[0]["points"]), 1)
        prompt = call.call_args.args[0]
        self.assertIn("尤宜嚴密截拿", prompt)
        self.assertIn("尤應嚴密截拿", prompt)

    def test_trace_prompt_matches_strict_nested_source_chain_contract(self):
        prompt = proxy._trace_prompt(
            {"event": {"subtitle": "彰化失陷"}, "single": True},
            "原文：據A稟稱：准B咨，奉C行據D稟報。",
        )
        self.assertIn("D→C→B→A→作者", prompt)
        self.assertIn("彰邑大肚社番→淡屬大甲社通事→淡水同知", prompt)
        self.assertIn("才可填親歷", prompt)
        self.assertIn("只有整條鏈最後收到消息並撰寫本文書的人才是撰文者", prompt)
        self.assertIn("事件日期或收文日期不可冒充發送日期", prompt)


if __name__ == "__main__":
    unittest.main()
