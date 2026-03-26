# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable

import httpx

from ..types import response_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.response_create_response import ResponseCreateResponse

__all__ = ["ResponsesResource", "AsyncResponsesResource"]


class ResponsesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return ResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return ResponsesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        instructions: str | Omit = omit,
        max_output_tokens: int | Omit = omit,
        max_tool_calls: int | Omit = omit,
        parallel_tool_calls: bool | Omit = omit,
        reasoning: response_create_params.Reasoning | Omit = omit,
        safeguards: response_create_params.Safeguards | Omit = omit,
        stream: bool | Omit = omit,
        stream_options: response_create_params.StreamOptions | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: response_create_params.ToolChoice | Omit = omit,
        tools: Iterable[response_create_params.Tool] | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCreateResponse:
        """
        Generate responses while also allowing for the utilization of various tools.

        Args:
          input: An input string used for generating completions.

          model: The AI model to use for generating responses.

          instructions: A system (or developer) message inserted into the model's context.

          max_output_tokens: The maximum number of tokens in the generated output.

          max_tool_calls: The maximum amount of tool calls the model is able to do.

          parallel_tool_calls: Whether to enable parallel function calling during tool use.

          reasoning: Constrains effort on reasoning for reasoning models.

          safeguards: Safeguards to run on the request.

          stream: Whether to stream back the model response. Not currently supported.

          stream_options: Extra parameters used when streaming the response.

          temperature: The temperature parameter for controlling randomness in completions. Supports a
              range of 0.0-2.0.

          tool_choice: A string representing a tool choice. Options are 'none', 'auto', or 'required'.

          tools: The content of the tool call.

          top_p: The diversity of the generated text based on nucleus sampling. Supports a range
              of 0.0-1.0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/responses",
            body=maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "instructions": instructions,
                    "max_output_tokens": max_output_tokens,
                    "max_tool_calls": max_tool_calls,
                    "parallel_tool_calls": parallel_tool_calls,
                    "reasoning": reasoning,
                    "safeguards": safeguards,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_p": top_p,
                },
                response_create_params.ResponseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseCreateResponse,
        )


class AsyncResponsesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return AsyncResponsesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        instructions: str | Omit = omit,
        max_output_tokens: int | Omit = omit,
        max_tool_calls: int | Omit = omit,
        parallel_tool_calls: bool | Omit = omit,
        reasoning: response_create_params.Reasoning | Omit = omit,
        safeguards: response_create_params.Safeguards | Omit = omit,
        stream: bool | Omit = omit,
        stream_options: response_create_params.StreamOptions | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: response_create_params.ToolChoice | Omit = omit,
        tools: Iterable[response_create_params.Tool] | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCreateResponse:
        """
        Generate responses while also allowing for the utilization of various tools.

        Args:
          input: An input string used for generating completions.

          model: The AI model to use for generating responses.

          instructions: A system (or developer) message inserted into the model's context.

          max_output_tokens: The maximum number of tokens in the generated output.

          max_tool_calls: The maximum amount of tool calls the model is able to do.

          parallel_tool_calls: Whether to enable parallel function calling during tool use.

          reasoning: Constrains effort on reasoning for reasoning models.

          safeguards: Safeguards to run on the request.

          stream: Whether to stream back the model response. Not currently supported.

          stream_options: Extra parameters used when streaming the response.

          temperature: The temperature parameter for controlling randomness in completions. Supports a
              range of 0.0-2.0.

          tool_choice: A string representing a tool choice. Options are 'none', 'auto', or 'required'.

          tools: The content of the tool call.

          top_p: The diversity of the generated text based on nucleus sampling. Supports a range
              of 0.0-1.0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/responses",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "instructions": instructions,
                    "max_output_tokens": max_output_tokens,
                    "max_tool_calls": max_tool_calls,
                    "parallel_tool_calls": parallel_tool_calls,
                    "reasoning": reasoning,
                    "safeguards": safeguards,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_p": top_p,
                },
                response_create_params.ResponseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseCreateResponse,
        )


class ResponsesResourceWithRawResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses

        self.create = to_raw_response_wrapper(
            responses.create,
        )


class AsyncResponsesResourceWithRawResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses

        self.create = async_to_raw_response_wrapper(
            responses.create,
        )


class ResponsesResourceWithStreamingResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses

        self.create = to_streamed_response_wrapper(
            responses.create,
        )


class AsyncResponsesResourceWithStreamingResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses

        self.create = async_to_streamed_response_wrapper(
            responses.create,
        )
