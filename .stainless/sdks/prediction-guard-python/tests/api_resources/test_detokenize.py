# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prediction_guard import PredictionGuard, AsyncPredictionGuard
from prediction_guard.types import DetokenizeCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDetokenize:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: PredictionGuard) -> None:
        detokenize = client.detokenize.create(
            model="{{TEXT_MODEL}}",
            tokens=[1, 851, 349, 264, 6029, 653, 2757, 28723],
        )
        assert_matches_type(DetokenizeCreateResponse, detokenize, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PredictionGuard) -> None:
        response = client.detokenize.with_raw_response.create(
            model="{{TEXT_MODEL}}",
            tokens=[1, 851, 349, 264, 6029, 653, 2757, 28723],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detokenize = response.parse()
        assert_matches_type(DetokenizeCreateResponse, detokenize, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PredictionGuard) -> None:
        with client.detokenize.with_streaming_response.create(
            model="{{TEXT_MODEL}}",
            tokens=[1, 851, 349, 264, 6029, 653, 2757, 28723],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detokenize = response.parse()
            assert_matches_type(DetokenizeCreateResponse, detokenize, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDetokenize:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPredictionGuard) -> None:
        detokenize = await async_client.detokenize.create(
            model="{{TEXT_MODEL}}",
            tokens=[1, 851, 349, 264, 6029, 653, 2757, 28723],
        )
        assert_matches_type(DetokenizeCreateResponse, detokenize, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPredictionGuard) -> None:
        response = await async_client.detokenize.with_raw_response.create(
            model="{{TEXT_MODEL}}",
            tokens=[1, 851, 349, 264, 6029, 653, 2757, 28723],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detokenize = await response.parse()
        assert_matches_type(DetokenizeCreateResponse, detokenize, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPredictionGuard) -> None:
        async with async_client.detokenize.with_streaming_response.create(
            model="{{TEXT_MODEL}}",
            tokens=[1, 851, 349, 264, 6029, 653, 2757, 28723],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detokenize = await response.parse()
            assert_matches_type(DetokenizeCreateResponse, detokenize, path=["response"])

        assert cast(Any, response.is_closed) is True
