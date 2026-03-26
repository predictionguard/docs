# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

import httpx

from ..types import completion_create_params
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
from ..types.completion_create_response import CompletionCreateResponse

__all__ = ["CompletionsResource", "AsyncCompletionsResource"]


class CompletionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return CompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return CompletionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model: str,
        prompt: Union[str, SequenceNotStr[str]],
        frequency_penalty: float | Omit = omit,
        input: completion_create_params.Input | Omit = omit,
        logit_bias: completion_create_params.LogitBias | Omit = omit,
        max_tokens: int | Omit = omit,
        output: completion_create_params.Output | Omit = omit,
        presence_penalty: float | Omit = omit,
        stop: Union[str, SequenceNotStr[str]] | Omit = omit,
        stream: bool | Omit = omit,
        stream_options: completion_create_params.StreamOptions | Omit = omit,
        temperature: float | Omit = omit,
        top_k: int | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse:
        """
        Retrieve text completions based on the provided input.

        Args:
          model: The chat model to use for generating completions.

          prompt: The prompt to use for generating completions.

          frequency_penalty: A value between -2.0 and 2.0, with positive values increasingly penalizing new
              tokens based on their frequency so far in order to decrease further occurrences.

          input: Options to affect the input of the request.

          logit_bias: Modifies the likelihood of specified tokens appearing in a response.

          max_tokens: The maximum number of tokens in the generated completion.

          output: Options to affect the output of the response.

          presence_penalty: A value between -2.0 and 2.0, with positive values causing a flat reduction of
              new tokens based on their existing presence so far in order to decrease further
              occurrences.

          stop: A string representing the token to stop generation.

          stream: Whether to stream back the model response.

          stream_options: Extra parameters used when streaming the response.

          temperature: The temperature parameter for controlling randomness in completions. Supports a
              range of 0.0-2.0.

          top_k: The diversity of the generated text based on top-k sampling.

          top_p: The diversity of the generated text based on nucleus sampling. Supports a range
              of 0.0-1.0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/completions",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "frequency_penalty": frequency_penalty,
                    "input": input,
                    "logit_bias": logit_bias,
                    "max_tokens": max_tokens,
                    "output": output,
                    "presence_penalty": presence_penalty,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "top_k": top_k,
                    "top_p": top_p,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionCreateResponse,
        )


class AsyncCompletionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return AsyncCompletionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model: str,
        prompt: Union[str, SequenceNotStr[str]],
        frequency_penalty: float | Omit = omit,
        input: completion_create_params.Input | Omit = omit,
        logit_bias: completion_create_params.LogitBias | Omit = omit,
        max_tokens: int | Omit = omit,
        output: completion_create_params.Output | Omit = omit,
        presence_penalty: float | Omit = omit,
        stop: Union[str, SequenceNotStr[str]] | Omit = omit,
        stream: bool | Omit = omit,
        stream_options: completion_create_params.StreamOptions | Omit = omit,
        temperature: float | Omit = omit,
        top_k: int | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse:
        """
        Retrieve text completions based on the provided input.

        Args:
          model: The chat model to use for generating completions.

          prompt: The prompt to use for generating completions.

          frequency_penalty: A value between -2.0 and 2.0, with positive values increasingly penalizing new
              tokens based on their frequency so far in order to decrease further occurrences.

          input: Options to affect the input of the request.

          logit_bias: Modifies the likelihood of specified tokens appearing in a response.

          max_tokens: The maximum number of tokens in the generated completion.

          output: Options to affect the output of the response.

          presence_penalty: A value between -2.0 and 2.0, with positive values causing a flat reduction of
              new tokens based on their existing presence so far in order to decrease further
              occurrences.

          stop: A string representing the token to stop generation.

          stream: Whether to stream back the model response.

          stream_options: Extra parameters used when streaming the response.

          temperature: The temperature parameter for controlling randomness in completions. Supports a
              range of 0.0-2.0.

          top_k: The diversity of the generated text based on top-k sampling.

          top_p: The diversity of the generated text based on nucleus sampling. Supports a range
              of 0.0-1.0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/completions",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "frequency_penalty": frequency_penalty,
                    "input": input,
                    "logit_bias": logit_bias,
                    "max_tokens": max_tokens,
                    "output": output,
                    "presence_penalty": presence_penalty,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "top_k": top_k,
                    "top_p": top_p,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionCreateResponse,
        )


class CompletionsResourceWithRawResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_raw_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithRawResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_raw_response_wrapper(
            completions.create,
        )


class CompletionsResourceWithStreamingResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_streamed_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithStreamingResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_streamed_response_wrapper(
            completions.create,
        )
