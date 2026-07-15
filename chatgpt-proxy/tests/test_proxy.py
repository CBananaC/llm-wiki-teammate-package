import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import Mock, patch


MODULE_PATH = Path(__file__).resolve().parents[1] / "main.py"
SPEC = importlib.util.spec_from_file_location("chatgpt_proxy", MODULE_PATH)
proxy = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(proxy)


class ChatGPTProxyTests(unittest.TestCase):
    def test_health_and_provider_metadata(self):
        client = proxy.app.test_client()
        with patch.object(proxy, "API_KEY", "test-key"):
            health = client.get("/")
            providers = client.get("/providers")
        self.assertEqual(health.status_code, 200)
        self.assertEqual(health.get_json()["model"], "gpt-5.4")
        self.assertTrue(providers.get_json()["providers"][0]["enabled"])


    def test_chat_uses_tokenrouter_chat_completions(self):
        upstream = Mock()
        upstream.raise_for_status.return_value = None
        upstream.json.return_value = {
            "choices": [{"message": {"content": "測試回覆"}}]
        }
        client = proxy.app.test_client()
        with (
            patch.object(proxy, "API_KEY", "test-key"),
            patch.object(proxy.requests, "post", return_value=upstream) as post,
        ):
            response = client.post("/chat", json={"mode": "ask", "question": "你好"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"mode": "ask", "text": "測試回覆"})
        self.assertTrue(post.call_args.args[0].endswith("/chat/completions"))
        body = json.loads(post.call_args.kwargs["data"])
        self.assertEqual(body["model"], "gpt-5.4")
        self.assertEqual(body["max_tokens"], 16384)
        self.assertEqual(post.call_args.kwargs["headers"]["Authorization"], "Bearer test-key")


    def test_request_key_is_not_used(self):
        client = proxy.app.test_client()
        with patch.object(proxy, "API_KEY", ""):
            response = client.post("/chat", json={"mode": "ask", "api_key": "browser-key"})
        self.assertEqual(response.status_code, 500)
        self.assertIn("TOKENROUTER_API_KEY", response.get_json()["error"])


    def test_structured_prompt_uses_skill_actor_instruction_and_schema(self):
        prompt = proxy._structured_prompt(
            "events",
            {
                "actor": "qing",
                "category": "plan",
                "actor_instruction": "只擷取尚未執行的清方計畫。",
            },
            "原文：測試",
        )
        self.assertIn("只擷取尚未執行的清方計畫。", prompt)
        self.assertIn('"subtitle"', prompt)
        self.assertIn('"quote"', prompt)


    def test_zhupi_contract_requires_zhupi_fields(self):
        prompt = proxy._structured_prompt("zhupi", {}, "原文：已有旨了。")
        self.assertIn('"position": "夾批|尾批"', prompt)
        self.assertIn('"responds_to"', prompt)

    def test_trace_uses_strict_nested_source_chain_contract(self):
        payload = {
            "mode": "trace",
            "doc_id": "硃61",
            "body": "據平陽協副將英海稟稱：准福建桐山營遊擊咨，奉福建巡撫行據淡水同知程峻稟報。",
        }
        with patch.object(proxy, "_generate", return_value='{"chains":[]}') as generate:
            response = proxy.app.test_client().post("/chat", json=payload)
        self.assertEqual(response.status_code, 200)
        prompt = generate.call_args.args[0]
        self.assertIn("D→C→B→A→作者", prompt)
        self.assertIn("彰邑大肚社番→淡屬大甲社通事", prompt)
        self.assertIn("不要填『親歷』", prompt)
        self.assertIn("最後一個 hop 的 to_person 必須是撰寫本文書的官員", prompt)
