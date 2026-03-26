# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

import httpx

from ..types import pii_replace_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.pii_replace_response import PiiReplaceResponse

__all__ = ["PiiResource", "AsyncPiiResource"]


class PiiResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PiiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return PiiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PiiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return PiiResourceWithStreamingResponse(self)

    def replace(
        self,
        *,
        prompt: Union[str, SequenceNotStr[str]],
        replace: bool,
        entity_list: SequenceNotStr[str] | Omit = omit,
        replace_method: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PiiReplaceResponse:
        """
        Replace personal information such as names, SSNs, and emails in a given text.

        Args:
          prompt: The prompt to check for personal information.

          replace: Whether to replace personal information.

          entity_list: An array of entity types that the PII check should ignore.

          replace_method: The method to use (random, fake, category, mask).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/PII",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "replace": replace,
                    "entity_list": entity_list,
                    "replace_method": replace_method,
                },
                pii_replace_params.PiiReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PiiReplaceResponse,
        )


class AsyncPiiResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPiiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPiiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPiiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return AsyncPiiResourceWithStreamingResponse(self)

    async def replace(
        self,
        *,
        prompt: Union[str, SequenceNotStr[str]],
        replace: bool,
        entity_list: SequenceNotStr[str] | Omit = omit,
        replace_method: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PiiReplaceResponse:
        """
        Replace personal information such as names, SSNs, and emails in a given text.

        Args:
          prompt: The prompt to check for personal information.

          replace: Whether to replace personal information.

          entity_list: An array of entity types that the PII check should ignore.

          replace_method: The method to use (random, fake, category, mask).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/PII",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "replace": replace,
                    "entity_list": entity_list,
                    "replace_method": replace_method,
                },
                pii_replace_params.PiiReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PiiReplaceResponse,
        )


class PiiResourceWithRawResponse:
    def __init__(self, pii: PiiResource) -> None:
        self._pii = pii

        self.replace = to_raw_response_wrapper(
            pii.replace,
        )


class AsyncPiiResourceWithRawResponse:
    def __init__(self, pii: AsyncPiiResource) -> None:
        self._pii = pii

        self.replace = async_to_raw_response_wrapper(
            pii.replace,
        )


class PiiResourceWithStreamingResponse:
    def __init__(self, pii: PiiResource) -> None:
        self._pii = pii

        self.replace = to_streamed_response_wrapper(
            pii.replace,
        )


class AsyncPiiResourceWithStreamingResponse:
    def __init__(self, pii: AsyncPiiResource) -> None:
        self._pii = pii

        self.replace = async_to_streamed_response_wrapper(
            pii.replace,
        )
