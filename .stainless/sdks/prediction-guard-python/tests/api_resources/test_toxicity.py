# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prediction_guard import PredictionGuard, AsyncPredictionGuard
from prediction_guard.types import ToxicityCheckResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestToxicity:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check(self, client: PredictionGuard) -> None:
        toxicity = client.toxicity.check(
            text="Every flight I have is late and I am very angry. I want to hurt someone.",
        )
        assert_matches_type(ToxicityCheckResponse, toxicity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_check(self, client: PredictionGuard) -> None:
        response = client.toxicity.with_raw_response.check(
            text="Every flight I have is late and I am very angry. I want to hurt someone.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toxicity = response.parse()
        assert_matches_type(ToxicityCheckResponse, toxicity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_check(self, client: PredictionGuard) -> None:
        with client.toxicity.with_streaming_response.check(
            text="Every flight I have is late and I am very angry. I want to hurt someone.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toxicity = response.parse()
            assert_matches_type(ToxicityCheckResponse, toxicity, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncToxicity:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check(self, async_client: AsyncPredictionGuard) -> None:
        toxicity = await async_client.toxicity.check(
            text="Every flight I have is late and I am very angry. I want to hurt someone.",
        )
        assert_matches_type(ToxicityCheckResponse, toxicity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_check(self, async_client: AsyncPredictionGuard) -> None:
        response = await async_client.toxicity.with_raw_response.check(
            text="Every flight I have is late and I am very angry. I want to hurt someone.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toxicity = await response.parse()
        assert_matches_type(ToxicityCheckResponse, toxicity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_check(self, async_client: AsyncPredictionGuard) -> None:
        async with async_client.toxicity.with_streaming_response.check(
            text="Every flight I have is late and I am very angry. I want to hurt someone.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toxicity = await response.parse()
            assert_matches_type(ToxicityCheckResponse, toxicity, path=["response"])

        assert cast(Any, response.is_closed) is True
