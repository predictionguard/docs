# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prediction_guard import PredictionGuard, AsyncPredictionGuard
from prediction_guard.types import CompletionCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: PredictionGuard) -> None:
        completion = client.completions.create(
            model="{{TEXT_MODEL}}",
            prompt="Will I lose my hair?",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PredictionGuard) -> None:
        completion = client.completions.create(
            model="{{TEXT_MODEL}}",
            prompt="Will I lose my hair?",
            frequency_penalty=0.1,
            input={
                "block_prompt_injection": True,
                "entity_list": ["string"],
                "pii": "replace",
                "pii_replace_method": "random",
            },
            logit_bias={"token": "token"},
            max_tokens=1000,
            output={
                "factuality": True,
                "toxicity": True,
            },
            presence_penalty=0.1,
            stop="hello",
            stream=True,
            stream_options={"include_usage": True},
            temperature=1,
            top_k=50,
            top_p=1,
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PredictionGuard) -> None:
        response = client.completions.with_raw_response.create(
            model="{{TEXT_MODEL}}",
            prompt="Will I lose my hair?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PredictionGuard) -> None:
        with client.completions.with_streaming_response.create(
            model="{{TEXT_MODEL}}",
            prompt="Will I lose my hair?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPredictionGuard) -> None:
        completion = await async_client.completions.create(
            model="{{TEXT_MODEL}}",
            prompt="Will I lose my hair?",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPredictionGuard) -> None:
        completion = await async_client.completions.create(
            model="{{TEXT_MODEL}}",
            prompt="Will I lose my hair?",
            frequency_penalty=0.1,
            input={
                "block_prompt_injection": True,
                "entity_list": ["string"],
                "pii": "replace",
                "pii_replace_method": "random",
            },
            logit_bias={"token": "token"},
            max_tokens=1000,
            output={
                "factuality": True,
                "toxicity": True,
            },
            presence_penalty=0.1,
            stop="hello",
            stream=True,
            stream_options={"include_usage": True},
            temperature=1,
            top_k=50,
            top_p=1,
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPredictionGuard) -> None:
        response = await async_client.completions.with_raw_response.create(
            model="{{TEXT_MODEL}}",
            prompt="Will I lose my hair?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPredictionGuard) -> None:
        async with async_client.completions.with_streaming_response.create(
            model="{{TEXT_MODEL}}",
            prompt="Will I lose my hair?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True
