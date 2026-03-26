# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import detokenize_create_params
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
from ..types.detokenize_create_response import DetokenizeCreateResponse

__all__ = ["DetokenizeResource", "AsyncDetokenizeResource"]


class DetokenizeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DetokenizeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return DetokenizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DetokenizeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return DetokenizeResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model: str,
        tokens: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DetokenizeCreateResponse:
        """
        Generates text from tokens using a model's tokenizer.

        Args:
          model: The name of the model to use for detokenization.

          tokens: The tokens to turn into text.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/detokenize",
            body=maybe_transform(
                {
                    "model": model,
                    "tokens": tokens,
                },
                detokenize_create_params.DetokenizeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetokenizeCreateResponse,
        )


class AsyncDetokenizeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDetokenizeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDetokenizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDetokenizeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return AsyncDetokenizeResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model: str,
        tokens: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DetokenizeCreateResponse:
        """
        Generates text from tokens using a model's tokenizer.

        Args:
          model: The name of the model to use for detokenization.

          tokens: The tokens to turn into text.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/detokenize",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "tokens": tokens,
                },
                detokenize_create_params.DetokenizeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetokenizeCreateResponse,
        )


class DetokenizeResourceWithRawResponse:
    def __init__(self, detokenize: DetokenizeResource) -> None:
        self._detokenize = detokenize

        self.create = to_raw_response_wrapper(
            detokenize.create,
        )


class AsyncDetokenizeResourceWithRawResponse:
    def __init__(self, detokenize: AsyncDetokenizeResource) -> None:
        self._detokenize = detokenize

        self.create = async_to_raw_response_wrapper(
            detokenize.create,
        )


class DetokenizeResourceWithStreamingResponse:
    def __init__(self, detokenize: DetokenizeResource) -> None:
        self._detokenize = detokenize

        self.create = to_streamed_response_wrapper(
            detokenize.create,
        )


class AsyncDetokenizeResourceWithStreamingResponse:
    def __init__(self, detokenize: AsyncDetokenizeResource) -> None:
        self._detokenize = detokenize

        self.create = async_to_streamed_response_wrapper(
            detokenize.create,
        )
