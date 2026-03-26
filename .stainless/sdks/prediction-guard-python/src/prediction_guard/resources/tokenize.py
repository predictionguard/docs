# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import tokenize_generate_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.tokenize_generate_response import TokenizeGenerateResponse

__all__ = ["TokenizeResource", "AsyncTokenizeResource"]


class TokenizeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TokenizeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return TokenizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokenizeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return TokenizeResourceWithStreamingResponse(self)

    def generate(
        self,
        *,
        input: str,
        model: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenizeGenerateResponse:
        """
        Generates tokens for a string using a model's tokenizer.

        Args:
          input: The text to tokenize.

          model: The name of the model to use for tokenization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tokenize",
            body=maybe_transform(
                {
                    "input": input,
                    "model": model,
                },
                tokenize_generate_params.TokenizeGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenizeGenerateResponse,
        )


class AsyncTokenizeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTokenizeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTokenizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokenizeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return AsyncTokenizeResourceWithStreamingResponse(self)

    async def generate(
        self,
        *,
        input: str,
        model: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenizeGenerateResponse:
        """
        Generates tokens for a string using a model's tokenizer.

        Args:
          input: The text to tokenize.

          model: The name of the model to use for tokenization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tokenize",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "model": model,
                },
                tokenize_generate_params.TokenizeGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenizeGenerateResponse,
        )


class TokenizeResourceWithRawResponse:
    def __init__(self, tokenize: TokenizeResource) -> None:
        self._tokenize = tokenize

        self.generate = to_raw_response_wrapper(
            tokenize.generate,
        )


class AsyncTokenizeResourceWithRawResponse:
    def __init__(self, tokenize: AsyncTokenizeResource) -> None:
        self._tokenize = tokenize

        self.generate = async_to_raw_response_wrapper(
            tokenize.generate,
        )


class TokenizeResourceWithStreamingResponse:
    def __init__(self, tokenize: TokenizeResource) -> None:
        self._tokenize = tokenize

        self.generate = to_streamed_response_wrapper(
            tokenize.generate,
        )


class AsyncTokenizeResourceWithStreamingResponse:
    def __init__(self, tokenize: AsyncTokenizeResource) -> None:
        self._tokenize = tokenize

        self.generate = async_to_streamed_response_wrapper(
            tokenize.generate,
        )
