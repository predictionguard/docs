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
from ..types.mcp_tool_list_response import McpToolListResponse

__all__ = ["McpToolsResource", "AsyncMcpToolsResource"]


class McpToolsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> McpToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return McpToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> McpToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return McpToolsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpToolListResponse:
        """Return available MCP tools by server with parameters and any relevant metadata."""
        return self._get(
            "/mcp_tools",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpToolListResponse,
        )


class AsyncMcpToolsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMcpToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMcpToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMcpToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return AsyncMcpToolsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpToolListResponse:
        """Return available MCP tools by server with parameters and any relevant metadata."""
        return await self._get(
            "/mcp_tools",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=McpToolListResponse,
        )


class McpToolsResourceWithRawResponse:
    def __init__(self, mcp_tools: McpToolsResource) -> None:
        self._mcp_tools = mcp_tools

        self.list = to_raw_response_wrapper(
            mcp_tools.list,
        )


class AsyncMcpToolsResourceWithRawResponse:
    def __init__(self, mcp_tools: AsyncMcpToolsResource) -> None:
        self._mcp_tools = mcp_tools

        self.list = async_to_raw_response_wrapper(
            mcp_tools.list,
        )


class McpToolsResourceWithStreamingResponse:
    def __init__(self, mcp_tools: McpToolsResource) -> None:
        self._mcp_tools = mcp_tools

        self.list = to_streamed_response_wrapper(
            mcp_tools.list,
        )


class AsyncMcpToolsResourceWithStreamingResponse:
    def __init__(self, mcp_tools: AsyncMcpToolsResource) -> None:
        self._mcp_tools = mcp_tools

        self.list = async_to_streamed_response_wrapper(
            mcp_tools.list,
        )
