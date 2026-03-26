# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prediction_guard import PredictionGuard, AsyncPredictionGuard
from prediction_guard.types import FactualityCheckResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFactuality:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check(self, client: PredictionGuard) -> None:
        factuality = client.factuality.check(
            reference="The President shall receive in full for his services during the term for which he shall have been elected compensation in the aggregate amount of 400,000 a year, to be paid monthly, and in addition an expense allowance of 50,000 to assist in defraying expenses relating to or resulting from the discharge of his official duties.",
            text="The president of the united states can take a salary of one million dollars",
        )
        assert_matches_type(FactualityCheckResponse, factuality, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_check(self, client: PredictionGuard) -> None:
        response = client.factuality.with_raw_response.check(
            reference="The President shall receive in full for his services during the term for which he shall have been elected compensation in the aggregate amount of 400,000 a year, to be paid monthly, and in addition an expense allowance of 50,000 to assist in defraying expenses relating to or resulting from the discharge of his official duties.",
            text="The president of the united states can take a salary of one million dollars",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        factuality = response.parse()
        assert_matches_type(FactualityCheckResponse, factuality, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_check(self, client: PredictionGuard) -> None:
        with client.factuality.with_streaming_response.check(
            reference="The President shall receive in full for his services during the term for which he shall have been elected compensation in the aggregate amount of 400,000 a year, to be paid monthly, and in addition an expense allowance of 50,000 to assist in defraying expenses relating to or resulting from the discharge of his official duties.",
            text="The president of the united states can take a salary of one million dollars",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            factuality = response.parse()
            assert_matches_type(FactualityCheckResponse, factuality, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFactuality:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check(self, async_client: AsyncPredictionGuard) -> None:
        factuality = await async_client.factuality.check(
            reference="The President shall receive in full for his services during the term for which he shall have been elected compensation in the aggregate amount of 400,000 a year, to be paid monthly, and in addition an expense allowance of 50,000 to assist in defraying expenses relating to or resulting from the discharge of his official duties.",
            text="The president of the united states can take a salary of one million dollars",
        )
        assert_matches_type(FactualityCheckResponse, factuality, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_check(self, async_client: AsyncPredictionGuard) -> None:
        response = await async_client.factuality.with_raw_response.check(
            reference="The President shall receive in full for his services during the term for which he shall have been elected compensation in the aggregate amount of 400,000 a year, to be paid monthly, and in addition an expense allowance of 50,000 to assist in defraying expenses relating to or resulting from the discharge of his official duties.",
            text="The president of the united states can take a salary of one million dollars",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        factuality = await response.parse()
        assert_matches_type(FactualityCheckResponse, factuality, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_check(self, async_client: AsyncPredictionGuard) -> None:
        async with async_client.factuality.with_streaming_response.check(
            reference="The President shall receive in full for his services during the term for which he shall have been elected compensation in the aggregate amount of 400,000 a year, to be paid monthly, and in addition an expense allowance of 50,000 to assist in defraying expenses relating to or resulting from the discharge of his official duties.",
            text="The president of the united states can take a salary of one million dollars",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            factuality = await response.parse()
            assert_matches_type(FactualityCheckResponse, factuality, path=["response"])

        assert cast(Any, response.is_closed) is True
