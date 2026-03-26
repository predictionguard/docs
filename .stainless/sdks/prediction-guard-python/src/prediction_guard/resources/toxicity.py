# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import toxicity_check_params
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
from ..types.toxicity_check_response import ToxicityCheckResponse

__all__ = ["ToxicityResource", "AsyncToxicityResource"]


class ToxicityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToxicityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return ToxicityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToxicityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return ToxicityResourceWithStreamingResponse(self)

    def check(
        self,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToxicityCheckResponse:
        """
        Check the toxicity of a given text.

        Args:
          text: The text to check for toxicity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/toxicity",
            body=maybe_transform({"text": text}, toxicity_check_params.ToxicityCheckParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToxicityCheckResponse,
        )


class AsyncToxicityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToxicityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToxicityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToxicityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return AsyncToxicityResourceWithStreamingResponse(self)

    async def check(
        self,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToxicityCheckResponse:
        """
        Check the toxicity of a given text.

        Args:
          text: The text to check for toxicity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/toxicity",
            body=await async_maybe_transform({"text": text}, toxicity_check_params.ToxicityCheckParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToxicityCheckResponse,
        )


class ToxicityResourceWithRawResponse:
    def __init__(self, toxicity: ToxicityResource) -> None:
        self._toxicity = toxicity

        self.check = to_raw_response_wrapper(
            toxicity.check,
        )


class AsyncToxicityResourceWithRawResponse:
    def __init__(self, toxicity: AsyncToxicityResource) -> None:
        self._toxicity = toxicity

        self.check = async_to_raw_response_wrapper(
            toxicity.check,
        )


class ToxicityResourceWithStreamingResponse:
    def __init__(self, toxicity: ToxicityResource) -> None:
        self._toxicity = toxicity

        self.check = to_streamed_response_wrapper(
            toxicity.check,
        )


class AsyncToxicityResourceWithStreamingResponse:
    def __init__(self, toxicity: AsyncToxicityResource) -> None:
        self._toxicity = toxicity

        self.check = async_to_streamed_response_wrapper(
            toxicity.check,
        )
