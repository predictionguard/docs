# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable

import httpx

from ..types import chat_generate_completion_params
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
from ..types.chat_generate_completion_response import ChatGenerateCompletionResponse

__all__ = ["ChatResource", "AsyncChatResource"]


class ChatResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return ChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return ChatResourceWithStreamingResponse(self)

    def generate_completion(
        self,
        *,
        messages: Union[str, Iterable[chat_generate_completion_params.MessagesUnionMember1]],
        model: str,
        frequency_penalty: float | Omit = omit,
        input: chat_generate_completion_params.Input | Omit = omit,
        logit_bias: chat_generate_completion_params.LogitBias | Omit = omit,
        max_completion_tokens: int | Omit = omit,
        max_tokens: int | Omit = omit,
        output: chat_generate_completion_params.Output | Omit = omit,
        parallel_tool_calls: bool | Omit = omit,
        presence_penalty: float | Omit = omit,
        reasoning_effort: str | Omit = omit,
        stop: Union[str, SequenceNotStr[str]] | Omit = omit,
        stream: bool | Omit = omit,
        stream_options: chat_generate_completion_params.StreamOptions | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: chat_generate_completion_params.ToolChoice | Omit = omit,
        tools: Iterable[chat_generate_completion_params.Tool] | Omit = omit,
        top_k: int | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatGenerateCompletionResponse:
        """
        Generate chat completions based on a conversation history.

        Args:
          messages: A string of the message used for generating completions.

          model: The chat model to use for generating completions.

          frequency_penalty: A value between -2.0 and 2.0, with positive values increasingly penalizing new
              tokens based on their frequency so far in order to decrease further occurrences.

          input: Options to affect the input of the request.

          logit_bias: Modifies the likelihood of specified tokens appearing in a response.

          max_completion_tokens: The maximum number of tokens in the generated completion.

          max_tokens: Deprecated. Please use max_completion_tokens.

          output: Options to affect the output of the response.

          parallel_tool_calls: Whether to enable parallel function calling during tool use.

          presence_penalty: A value between -2.0 and 2.0, with positive values causing a flat reduction of
              new tokens based on their existing presence so far in order to decrease further
              occurrences.

          reasoning_effort: Constrains effort on reasoning for reasoning models. Currently supported values
              are `low`, `medium`, and `high`. Reducing reasoning effort can result in faster
              responses and fewer tokens used on reasoning in a response. Only supported by
              reasoning models.

          stop: A string representing the token to stop generation.

          stream: Whether to stream back the model response.

          stream_options: Extra parameters used when streaming the response.

          temperature: The temperature parameter for controlling randomness in completions. Supports a
              range of 0.0-2.0.

          tool_choice: A string representing a tool choice. Options are 'none', 'auto', or 'required'.

          tools: The content of the tool call.

          top_k: The diversity of the generated text based on top-k sampling.

          top_p: The diversity of the generated text based on nucleus sampling. Supports a range
              of 0.0-1.0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/chat/completions",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "frequency_penalty": frequency_penalty,
                    "input": input,
                    "logit_bias": logit_bias,
                    "max_completion_tokens": max_completion_tokens,
                    "max_tokens": max_tokens,
                    "output": output,
                    "parallel_tool_calls": parallel_tool_calls,
                    "presence_penalty": presence_penalty,
                    "reasoning_effort": reasoning_effort,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_p": top_p,
                },
                chat_generate_completion_params.ChatGenerateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatGenerateCompletionResponse,
        )


class AsyncChatResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return AsyncChatResourceWithStreamingResponse(self)

    async def generate_completion(
        self,
        *,
        messages: Union[str, Iterable[chat_generate_completion_params.MessagesUnionMember1]],
        model: str,
        frequency_penalty: float | Omit = omit,
        input: chat_generate_completion_params.Input | Omit = omit,
        logit_bias: chat_generate_completion_params.LogitBias | Omit = omit,
        max_completion_tokens: int | Omit = omit,
        max_tokens: int | Omit = omit,
        output: chat_generate_completion_params.Output | Omit = omit,
        parallel_tool_calls: bool | Omit = omit,
        presence_penalty: float | Omit = omit,
        reasoning_effort: str | Omit = omit,
        stop: Union[str, SequenceNotStr[str]] | Omit = omit,
        stream: bool | Omit = omit,
        stream_options: chat_generate_completion_params.StreamOptions | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: chat_generate_completion_params.ToolChoice | Omit = omit,
        tools: Iterable[chat_generate_completion_params.Tool] | Omit = omit,
        top_k: int | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatGenerateCompletionResponse:
        """
        Generate chat completions based on a conversation history.

        Args:
          messages: A string of the message used for generating completions.

          model: The chat model to use for generating completions.

          frequency_penalty: A value between -2.0 and 2.0, with positive values increasingly penalizing new
              tokens based on their frequency so far in order to decrease further occurrences.

          input: Options to affect the input of the request.

          logit_bias: Modifies the likelihood of specified tokens appearing in a response.

          max_completion_tokens: The maximum number of tokens in the generated completion.

          max_tokens: Deprecated. Please use max_completion_tokens.

          output: Options to affect the output of the response.

          parallel_tool_calls: Whether to enable parallel function calling during tool use.

          presence_penalty: A value between -2.0 and 2.0, with positive values causing a flat reduction of
              new tokens based on their existing presence so far in order to decrease further
              occurrences.

          reasoning_effort: Constrains effort on reasoning for reasoning models. Currently supported values
              are `low`, `medium`, and `high`. Reducing reasoning effort can result in faster
              responses and fewer tokens used on reasoning in a response. Only supported by
              reasoning models.

          stop: A string representing the token to stop generation.

          stream: Whether to stream back the model response.

          stream_options: Extra parameters used when streaming the response.

          temperature: The temperature parameter for controlling randomness in completions. Supports a
              range of 0.0-2.0.

          tool_choice: A string representing a tool choice. Options are 'none', 'auto', or 'required'.

          tools: The content of the tool call.

          top_k: The diversity of the generated text based on top-k sampling.

          top_p: The diversity of the generated text based on nucleus sampling. Supports a range
              of 0.0-1.0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/chat/completions",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "frequency_penalty": frequency_penalty,
                    "input": input,
                    "logit_bias": logit_bias,
                    "max_completion_tokens": max_completion_tokens,
                    "max_tokens": max_tokens,
                    "output": output,
                    "parallel_tool_calls": parallel_tool_calls,
                    "presence_penalty": presence_penalty,
                    "reasoning_effort": reasoning_effort,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_p": top_p,
                },
                chat_generate_completion_params.ChatGenerateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatGenerateCompletionResponse,
        )


class ChatResourceWithRawResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.generate_completion = to_raw_response_wrapper(
            chat.generate_completion,
        )


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.generate_completion = async_to_raw_response_wrapper(
            chat.generate_completion,
        )


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.generate_completion = to_streamed_response_wrapper(
            chat.generate_completion,
        )


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.generate_completion = async_to_streamed_response_wrapper(
            chat.generate_completion,
        )
