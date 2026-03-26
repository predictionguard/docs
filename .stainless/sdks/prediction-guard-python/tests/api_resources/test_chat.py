# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prediction_guard import PredictionGuard, AsyncPredictionGuard
from prediction_guard.types import ChatGenerateCompletionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_completion(self, client: PredictionGuard) -> None:
        chat = client.chat.generate_completion(
            messages=[
                {
                    "content": "How do you feel about the world in general?",
                    "role": "user",
                }
            ],
            model="{{TEXT_MODEL}}",
        )
        assert_matches_type(ChatGenerateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_completion_with_all_params(self, client: PredictionGuard) -> None:
        chat = client.chat.generate_completion(
            messages=[
                {
                    "content": "How do you feel about the world in general?",
                    "role": "user",
                }
            ],
            model="{{TEXT_MODEL}}",
            frequency_penalty=0.1,
            input={
                "block_prompt_injection": True,
                "entity_list": ["string"],
                "pii": "replace",
                "pii_replace_method": "random",
            },
            logit_bias={"token": "token"},
            max_completion_tokens=1000,
            max_tokens=0,
            output={
                "factuality": True,
                "toxicity": True,
            },
            parallel_tool_calls=False,
            presence_penalty=0.1,
            reasoning_effort="medium",
            stop="hello",
            stream=True,
            stream_options={"include_usage": True},
            temperature=1,
            tool_choice="string",
            tools=[
                {
                    "function": {
                        "description": "description",
                        "name": "name",
                        "parameters": {},
                        "strict": True,
                    },
                    "type": "type",
                }
            ],
            top_k=50,
            top_p=1,
        )
        assert_matches_type(ChatGenerateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate_completion(self, client: PredictionGuard) -> None:
        response = client.chat.with_raw_response.generate_completion(
            messages=[
                {
                    "content": "How do you feel about the world in general?",
                    "role": "user",
                }
            ],
            model="{{TEXT_MODEL}}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatGenerateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate_completion(self, client: PredictionGuard) -> None:
        with client.chat.with_streaming_response.generate_completion(
            messages=[
                {
                    "content": "How do you feel about the world in general?",
                    "role": "user",
                }
            ],
            model="{{TEXT_MODEL}}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatGenerateCompletionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_completion(self, async_client: AsyncPredictionGuard) -> None:
        chat = await async_client.chat.generate_completion(
            messages=[
                {
                    "content": "How do you feel about the world in general?",
                    "role": "user",
                }
            ],
            model="{{TEXT_MODEL}}",
        )
        assert_matches_type(ChatGenerateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_completion_with_all_params(self, async_client: AsyncPredictionGuard) -> None:
        chat = await async_client.chat.generate_completion(
            messages=[
                {
                    "content": "How do you feel about the world in general?",
                    "role": "user",
                }
            ],
            model="{{TEXT_MODEL}}",
            frequency_penalty=0.1,
            input={
                "block_prompt_injection": True,
                "entity_list": ["string"],
                "pii": "replace",
                "pii_replace_method": "random",
            },
            logit_bias={"token": "token"},
            max_completion_tokens=1000,
            max_tokens=0,
            output={
                "factuality": True,
                "toxicity": True,
            },
            parallel_tool_calls=False,
            presence_penalty=0.1,
            reasoning_effort="medium",
            stop="hello",
            stream=True,
            stream_options={"include_usage": True},
            temperature=1,
            tool_choice="string",
            tools=[
                {
                    "function": {
                        "description": "description",
                        "name": "name",
                        "parameters": {},
                        "strict": True,
                    },
                    "type": "type",
                }
            ],
            top_k=50,
            top_p=1,
        )
        assert_matches_type(ChatGenerateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate_completion(self, async_client: AsyncPredictionGuard) -> None:
        response = await async_client.chat.with_raw_response.generate_completion(
            messages=[
                {
                    "content": "How do you feel about the world in general?",
                    "role": "user",
                }
            ],
            model="{{TEXT_MODEL}}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatGenerateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate_completion(self, async_client: AsyncPredictionGuard) -> None:
        async with async_client.chat.with_streaming_response.generate_completion(
            messages=[
                {
                    "content": "How do you feel about the world in general?",
                    "role": "user",
                }
            ],
            model="{{TEXT_MODEL}}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatGenerateCompletionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True
