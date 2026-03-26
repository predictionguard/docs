# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.mcp_server_list_response import McpServerListResponse

__all__ = ["McpServersResource", "AsyncMcpServersResource"]


class McpServersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> McpServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return McpServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> McpServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return McpServersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerListResponse:
        """
        Return available MCP servers and tools included in those servers along with
        relevant metadata.
        """
        return self._get(
            "/mcp_servers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerListResponse,
        )


class AsyncMcpServersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMcpServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMcpServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMcpServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return AsyncMcpServersResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpServerListResponse:
        """
        Return available MCP servers and tools included in those servers along with
        relevant metadata.
        """
        return await self._get(
            "/mcp_servers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpServerListResponse,
        )


class McpServersResourceWithRawResponse:
    def __init__(self, mcp_servers: McpServersResource) -> None:
        self._mcp_servers = mcp_servers

        self.list = to_raw_response_wrapper(
            mcp_servers.list,
        )


class AsyncMcpServersResourceWithRawResponse:
    def __init__(self, mcp_servers: AsyncMcpServersResource) -> None:
        self._mcp_servers = mcp_servers

        self.list = async_to_raw_response_wrapper(
            mcp_servers.list,
        )


class McpServersResourceWithStreamingResponse:
    def __init__(self, mcp_servers: McpServersResource) -> None:
        self._mcp_servers = mcp_servers

        self.list = to_streamed_response_wrapper(
            mcp_servers.list,
        )


class AsyncMcpServersResourceWithStreamingResponse:
    def __init__(self, mcp_servers: AsyncMcpServersResource) -> None:
        self._mcp_servers = mcp_servers

        self.list = async_to_streamed_response_wrapper(
            mcp_servers.list,
        )
