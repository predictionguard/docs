# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prediction_guard import PredictionGuard, AsyncPredictionGuard
from prediction_guard.types import McpServerListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMcpServers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: PredictionGuard) -> None:
        mcp_server = client.mcp_servers.list()
        assert_matches_type(McpServerListResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: PredictionGuard) -> None:
        response = client.mcp_servers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = response.parse()
        assert_matches_type(McpServerListResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: PredictionGuard) -> None:
        with client.mcp_servers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = response.parse()
            assert_matches_type(McpServerListResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMcpServers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPredictionGuard) -> None:
        mcp_server = await async_client.mcp_servers.list()
        assert_matches_type(McpServerListResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPredictionGuard) -> None:
        response = await async_client.mcp_servers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_server = await response.parse()
        assert_matches_type(McpServerListResponse, mcp_server, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPredictionGuard) -> None:
        async with async_client.mcp_servers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_server = await response.parse()
            assert_matches_type(McpServerListResponse, mcp_server, path=["response"])

        assert cast(Any, response.is_closed) is True
