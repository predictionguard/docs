# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

import httpx

from ..types import injection_create_params
from .._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
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
from ..types.injection_create_response import InjectionCreateResponse

__all__ = ["InjectionResource", "AsyncInjectionResource"]


class InjectionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InjectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return InjectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InjectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return InjectionResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        detect: bool,
        prompt: Union[str, SequenceNotStr[str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InjectionCreateResponse:
        """
        Injection detects potential prompt injection attacks.

        Args:
          detect: Whether to detect potential injection attacks.

          prompt: The prompt to check for injection attack.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/injection",
            body=maybe_transform(
                {
                    "detect": detect,
                    "prompt": prompt,
                },
                injection_create_params.InjectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InjectionCreateResponse,
        )


class AsyncInjectionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInjectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInjectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInjectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return AsyncInjectionResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        detect: bool,
        prompt: Union[str, SequenceNotStr[str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InjectionCreateResponse:
        """
        Injection detects potential prompt injection attacks.

        Args:
          detect: Whether to detect potential injection attacks.

          prompt: The prompt to check for injection attack.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/injection",
            body=await async_maybe_transform(
                {
                    "detect": detect,
                    "prompt": prompt,
                },
                injection_create_params.InjectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InjectionCreateResponse,
        )


class InjectionResourceWithRawResponse:
    def __init__(self, injection: InjectionResource) -> None:
        self._injection = injection

        self.create = to_raw_response_wrapper(
            injection.create,
        )


class AsyncInjectionResourceWithRawResponse:
    def __init__(self, injection: AsyncInjectionResource) -> None:
        self._injection = injection

        self.create = async_to_raw_response_wrapper(
            injection.create,
        )


class InjectionResourceWithStreamingResponse:
    def __init__(self, injection: InjectionResource) -> None:
        self._injection = injection

        self.create = to_streamed_response_wrapper(
            injection.create,
        )


class AsyncInjectionResourceWithStreamingResponse:
    def __init__(self, injection: AsyncInjectionResource) -> None:
        self._injection = injection

        self.create = async_to_streamed_response_wrapper(
            injection.create,
        )
