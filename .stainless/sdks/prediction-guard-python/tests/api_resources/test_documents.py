# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prediction_guard import PredictionGuard, AsyncPredictionGuard
from prediction_guard.types import DocumentExtractTextResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_text(self, client: PredictionGuard) -> None:
        document = client.documents.extract_text(
            file=b"Example data",
        )
        assert_matches_type(DocumentExtractTextResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_text_with_all_params(self, client: PredictionGuard) -> None:
        document = client.documents.extract_text(
            file=b"Example data",
            chunk_document=True,
            chunk_size=1000,
            embed_images=False,
            enable_ocr=True,
            output_format="markdown",
            entity_list=["ADDRESS"],
            injection=True,
            pii="replace",
            replace_method="category",
            toxicity=True,
        )
        assert_matches_type(DocumentExtractTextResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_extract_text(self, client: PredictionGuard) -> None:
        response = client.documents.with_raw_response.extract_text(
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentExtractTextResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_extract_text(self, client: PredictionGuard) -> None:
        with client.documents.with_streaming_response.extract_text(
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentExtractTextResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDocuments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_text(self, async_client: AsyncPredictionGuard) -> None:
        document = await async_client.documents.extract_text(
            file=b"Example data",
        )
        assert_matches_type(DocumentExtractTextResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_text_with_all_params(self, async_client: AsyncPredictionGuard) -> None:
        document = await async_client.documents.extract_text(
            file=b"Example data",
            chunk_document=True,
            chunk_size=1000,
            embed_images=False,
            enable_ocr=True,
            output_format="markdown",
            entity_list=["ADDRESS"],
            injection=True,
            pii="replace",
            replace_method="category",
            toxicity=True,
        )
        assert_matches_type(DocumentExtractTextResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_extract_text(self, async_client: AsyncPredictionGuard) -> None:
        response = await async_client.documents.with_raw_response.extract_text(
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentExtractTextResponse, document, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_extract_text(self, async_client: AsyncPredictionGuard) -> None:
        async with async_client.documents.with_streaming_response.extract_text(
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentExtractTextResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True
