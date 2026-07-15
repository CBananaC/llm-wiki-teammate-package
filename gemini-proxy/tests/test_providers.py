import importlib.util
import os
import unittest
from pathlib import Path
from unittest.mock import Mock, patch


MODULE_PATH = Path(__file__).resolve().parents[1] / "main.py"
SPEC = importlib.util.spec_from_file_location("timeline_ai_proxy", MODULE_PATH)
proxy = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(proxy)


class ProviderRoutingTests(unittest.TestCase):
    def test_json_list_accepts_nested_compatible_response_shapes(self):
        raw = '{"data":{"result":{"items":[{"title":"event one"}]}}}'
        self.assertEqual(proxy._json_list(raw, "events"), [{"title": "event one"}])

    def test_json_list_accepts_text_before_json_and_chinese_event_key(self):
        raw = '以下是結果：\n{"事件列表":[{"subtitle":"攻城"}]}\n完成。'
        self.assertEqual(proxy._json_list(raw, "events"), [{"subtitle": "攻城"}])

    def test_provider_defaults_are_not_gemini_models(self):
        self.assertEqual(proxy._provider_model("openai", None), "gpt-4.1")
        self.assertEqual(proxy._provider_model("tokenrouter", None), "gpt-5.4")
        self.assertEqual(
            proxy._provider_model("anthropic", None),
            "claude-sonnet-4-20250514",
        )
        self.assertEqual(proxy._provider_model("deepseek", None), "deepseek-chat")

    def test_output_limits_follow_the_selected_provider_and_model(self):
        self.assertEqual(proxy._provider_max_tokens("openai", "gpt-4o", None), 16384)
        self.assertEqual(
            proxy._provider_max_tokens("deepseek", "deepseek-chat", 50000),
            8192,
        )
        self.assertEqual(
            proxy._provider_max_tokens("custom", "vendor-model", 12000),
            12000,
        )

    def test_custom_provider_uses_request_key_and_base_url(self):
        payload = {
            "provider": "custom",
            "model": "vendor-model",
            "api_base": "https://llm.example.com/v1",
            "api_key": "request-secret",
        }
        with (
            patch.object(proxy, "_validated_base_url", side_effect=lambda value: value),
            patch.object(proxy, "_chat_completions", return_value="ok") as completion,
        ):
            result = proxy._generate("hello", False, payload)

        self.assertEqual(result, "ok")
        self.assertEqual(completion.call_args.kwargs["api_key"], "request-secret")
        self.assertEqual(
            completion.call_args.kwargs["base_url"],
            "https://llm.example.com/v1",
        )
        self.assertEqual(completion.call_args.kwargs["model"], "vendor-model")

    def test_custom_provider_falls_back_to_environment_key(self):
        payload = {
            "provider": "custom",
            "model": "vendor-model",
            "api_base": "https://llm.example.com/v1",
        }
        with (
            patch.dict(os.environ, {"CUSTOM_API_KEY": "environment-secret"}),
            patch.object(proxy, "_validated_base_url", side_effect=lambda value: value),
            patch.object(proxy, "_chat_completions", return_value="ok") as completion,
        ):
            proxy._generate("hello", False, payload)

        self.assertEqual(completion.call_args.kwargs["api_key"], "environment-secret")

    def test_tokenrouter_uses_openai_compatible_route_and_token_field(self):
        payload = {"provider": "tokenrouter", "model": "gpt-5.4"}
        with (
            patch.dict(
                os.environ,
                {
                    "TOKENROUTER_API_KEY": "environment-secret",
                    "TOKENROUTER_BASE_URL": "https://www.tokenrouter.tech/v1",
                },
            ),
            patch.object(proxy, "_validated_base_url", side_effect=lambda value: value),
            patch.object(proxy, "_chat_completions", return_value="ok") as completion,
        ):
            result = proxy._generate("hello", True, payload)

        self.assertEqual(result, "ok")
        self.assertEqual(completion.call_args.kwargs["base_url"], "https://www.tokenrouter.tech/v1")
        self.assertEqual(completion.call_args.kwargs["api_key"], "environment-secret")
        self.assertEqual(completion.call_args.kwargs["model"], "gpt-5.4")
        self.assertEqual(completion.call_args.kwargs["token_field"], "max_tokens")
        self.assertTrue(completion.call_args.kwargs["json_mode"])

    def test_model_discovery_uses_request_credentials(self):
        response = Mock()
        response.json.return_value = {
            "data": [{"id": "vendor-alpha"}, {"id": "vendor-beta"}]
        }
        response.raise_for_status.return_value = None
        payload = {
            "provider": "custom",
            "api_base": "https://llm.example.com/v1",
            "api_key": "request-secret",
        }
        with (
            patch.object(proxy, "_validated_base_url", side_effect=lambda value: value),
            patch.object(proxy.requests, "get", return_value=response) as get,
        ):
            models = proxy._list_provider_models(payload)

        self.assertEqual(models, ["vendor-alpha", "vendor-beta"])
        self.assertEqual(
            get.call_args.kwargs["headers"]["Authorization"],
            "Bearer request-secret",
        )


if __name__ == "__main__":
    unittest.main()
