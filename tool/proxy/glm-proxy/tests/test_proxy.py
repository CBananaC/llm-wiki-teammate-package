import importlib.util
import json
import unittest
from pathlib import Path
from unittest.mock import Mock, patch


MODULE_PATH = Path(__file__).resolve().parents[1] / "main.py"
SPEC = importlib.util.spec_from_file_location("glm_proxy", MODULE_PATH)
proxy = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(proxy)


class GLMProxyTests(unittest.TestCase):
    def test_health(self):
        with patch.object(proxy, "API_KEY", "test-key"):
            response = proxy.app.test_client().get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["model"], "glm-4.5")

    def test_chat_routes_to_tokenrouter(self):
        upstream = Mock()
        upstream.raise_for_status.return_value = None
        upstream.json.return_value = {"choices": [{"message": {"content": "ok"}}]}
        with patch.object(proxy, "API_KEY", "test-key"), patch.object(proxy.requests, "post", return_value=upstream) as post:
            response = proxy.app.test_client().post("/chat", json={"mode": "ask", "question": "你好"})
        self.assertEqual(response.get_json(), {"mode": "ask", "text": "ok"})
        self.assertTrue(post.call_args.args[0].endswith("/chat/completions"))
        self.assertEqual(json.loads(post.call_args.kwargs["data"])["model"], "glm-4.5")

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
