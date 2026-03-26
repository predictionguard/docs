# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prediction_guard import PredictionGuard, AsyncPredictionGuard
from prediction_guard.types import TokenizeGenerateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokenize:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate(self, client: PredictionGuard) -> None:
        tokenize = client.tokenize.generate(
            input="Tell me a joke.",
            model="{{TEXT_MODEL}}",
        )
        assert_matches_type(TokenizeGenerateResponse, tokenize, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate(self, client: PredictionGuard) -> None:
        response = client.tokenize.with_raw_response.generate(
            input="Tell me a joke.",
            model="{{TEXT_MODEL}}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenize = response.parse()
        assert_matches_type(TokenizeGenerateResponse, tokenize, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate(self, client: PredictionGuard) -> None:
        with client.tokenize.with_streaming_response.generate(
            input="Tell me a joke.",
            model="{{TEXT_MODEL}}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenize = response.parse()
            assert_matches_type(TokenizeGenerateResponse, tokenize, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTokenize:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate(self, async_client: AsyncPredictionGuard) -> None:
        tokenize = await async_client.tokenize.generate(
            input="Tell me a joke.",
            model="{{TEXT_MODEL}}",
        )
        assert_matches_type(TokenizeGenerateResponse, tokenize, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncPredictionGuard) -> None:
        response = await async_client.tokenize.with_raw_response.generate(
            input="Tell me a joke.",
            model="{{TEXT_MODEL}}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenize = await response.parse()
        assert_matches_type(TokenizeGenerateResponse, tokenize, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncPredictionGuard) -> None:
        async with async_client.tokenize.with_streaming_response.generate(
            input="Tell me a joke.",
            model="{{TEXT_MODEL}}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenize = await response.parse()
            assert_matches_type(TokenizeGenerateResponse, tokenize, path=["response"])

        assert cast(Any, response.is_closed) is True
