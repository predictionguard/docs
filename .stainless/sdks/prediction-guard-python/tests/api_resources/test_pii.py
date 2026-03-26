# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prediction_guard import PredictionGuard, AsyncPredictionGuard
from prediction_guard.types import PiiReplaceResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPii:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace(self, client: PredictionGuard) -> None:
        pii = client.pii.replace(
            prompt="My email is frodo@predictionguard.com and my number is 954-123-4567.",
            replace=True,
        )
        assert_matches_type(PiiReplaceResponse, pii, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace_with_all_params(self, client: PredictionGuard) -> None:
        pii = client.pii.replace(
            prompt="My email is frodo@predictionguard.com and my number is 954-123-4567.",
            replace=True,
            entity_list=["string"],
            replace_method="mask",
        )
        assert_matches_type(PiiReplaceResponse, pii, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replace(self, client: PredictionGuard) -> None:
        response = client.pii.with_raw_response.replace(
            prompt="My email is frodo@predictionguard.com and my number is 954-123-4567.",
            replace=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pii = response.parse()
        assert_matches_type(PiiReplaceResponse, pii, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replace(self, client: PredictionGuard) -> None:
        with client.pii.with_streaming_response.replace(
            prompt="My email is frodo@predictionguard.com and my number is 954-123-4567.",
            replace=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pii = response.parse()
            assert_matches_type(PiiReplaceResponse, pii, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPii:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace(self, async_client: AsyncPredictionGuard) -> None:
        pii = await async_client.pii.replace(
            prompt="My email is frodo@predictionguard.com and my number is 954-123-4567.",
            replace=True,
        )
        assert_matches_type(PiiReplaceResponse, pii, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncPredictionGuard) -> None:
        pii = await async_client.pii.replace(
            prompt="My email is frodo@predictionguard.com and my number is 954-123-4567.",
            replace=True,
            entity_list=["string"],
            replace_method="mask",
        )
        assert_matches_type(PiiReplaceResponse, pii, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncPredictionGuard) -> None:
        response = await async_client.pii.with_raw_response.replace(
            prompt="My email is frodo@predictionguard.com and my number is 954-123-4567.",
            replace=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pii = await response.parse()
        assert_matches_type(PiiReplaceResponse, pii, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncPredictionGuard) -> None:
        async with async_client.pii.with_streaming_response.replace(
            prompt="My email is frodo@predictionguard.com and my number is 954-123-4567.",
            replace=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pii = await response.parse()
            assert_matches_type(PiiReplaceResponse, pii, path=["response"])

        assert cast(Any, response.is_closed) is True
