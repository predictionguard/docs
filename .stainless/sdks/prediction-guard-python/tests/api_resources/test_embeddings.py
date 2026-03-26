# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prediction_guard import PredictionGuard, AsyncPredictionGuard
from prediction_guard.types import EmbeddingCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmbeddings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: PredictionGuard) -> None:
        embedding = client.embeddings.create(
            input="A person is ironing something while standing on the back of a taxi.",
            model="{{TEXT_EMBED}}",
        )
        assert_matches_type(EmbeddingCreateResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PredictionGuard) -> None:
        embedding = client.embeddings.create(
            input="A person is ironing something while standing on the back of a taxi.",
            model="{{TEXT_EMBED}}",
            truncate=True,
            truncation_direction="Right",
        )
        assert_matches_type(EmbeddingCreateResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PredictionGuard) -> None:
        response = client.embeddings.with_raw_response.create(
            input="A person is ironing something while standing on the back of a taxi.",
            model="{{TEXT_EMBED}}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = response.parse()
        assert_matches_type(EmbeddingCreateResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PredictionGuard) -> None:
        with client.embeddings.with_streaming_response.create(
            input="A person is ironing something while standing on the back of a taxi.",
            model="{{TEXT_EMBED}}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = response.parse()
            assert_matches_type(EmbeddingCreateResponse, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmbeddings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPredictionGuard) -> None:
        embedding = await async_client.embeddings.create(
            input="A person is ironing something while standing on the back of a taxi.",
            model="{{TEXT_EMBED}}",
        )
        assert_matches_type(EmbeddingCreateResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPredictionGuard) -> None:
        embedding = await async_client.embeddings.create(
            input="A person is ironing something while standing on the back of a taxi.",
            model="{{TEXT_EMBED}}",
            truncate=True,
            truncation_direction="Right",
        )
        assert_matches_type(EmbeddingCreateResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPredictionGuard) -> None:
        response = await async_client.embeddings.with_raw_response.create(
            input="A person is ironing something while standing on the back of a taxi.",
            model="{{TEXT_EMBED}}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = await response.parse()
        assert_matches_type(EmbeddingCreateResponse, embedding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPredictionGuard) -> None:
        async with async_client.embeddings.with_streaming_response.create(
            input="A person is ironing something while standing on the back of a taxi.",
            model="{{TEXT_EMBED}}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = await response.parse()
            assert_matches_type(EmbeddingCreateResponse, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True
