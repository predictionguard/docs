# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "ChatGenerateCompletionParams",
    "MessagesUnionMember1",
    "MessagesUnionMember1ContentUnionMember1",
    "MessagesUnionMember1ContentUnionMember1ImageURL",
    "Input",
    "LogitBias",
    "Output",
    "StreamOptions",
    "ToolChoice",
    "ToolChoiceUnionMember1",
    "ToolChoiceUnionMember1Function",
    "Tool",
    "ToolFunction",
]


class ChatGenerateCompletionParams(TypedDict, total=False):
    messages: Required[Union[str, Iterable[MessagesUnionMember1]]]
    """A string of the message used for generating completions."""

    model: Required[str]
    """The chat model to use for generating completions."""

    frequency_penalty: float
    """
    A value between -2.0 and 2.0, with positive values increasingly penalizing new
    tokens based on their frequency so far in order to decrease further occurrences.
    """

    input: Input
    """Options to affect the input of the request."""

    logit_bias: LogitBias
    """Modifies the likelihood of specified tokens appearing in a response."""

    max_completion_tokens: int
    """The maximum number of tokens in the generated completion."""

    max_tokens: int
    """Deprecated. Please use max_completion_tokens."""

    output: Output
    """Options to affect the output of the response."""

    parallel_tool_calls: bool
    """Whether to enable parallel function calling during tool use."""

    presence_penalty: float
    """
    A value between -2.0 and 2.0, with positive values causing a flat reduction of
    new tokens based on their existing presence so far in order to decrease further
    occurrences.
    """

    reasoning_effort: str
    """Constrains effort on reasoning for reasoning models.

    Currently supported values are `low`, `medium`, and `high`. Reducing reasoning
    effort can result in faster responses and fewer tokens used on reasoning in a
    response. Only supported by reasoning models.
    """

    stop: Union[str, SequenceNotStr[str]]
    """A string representing the token to stop generation."""

    stream: bool
    """Whether to stream back the model response."""

    stream_options: StreamOptions
    """Extra parameters used when streaming the response."""

    temperature: float
    """The temperature parameter for controlling randomness in completions.

    Supports a range of 0.0-2.0.
    """

    tool_choice: ToolChoice
    """A string representing a tool choice. Options are 'none', 'auto', or 'required'."""

    tools: Iterable[Tool]
    """The content of the tool call."""

    top_k: int
    """The diversity of the generated text based on top-k sampling."""

    top_p: float
    """The diversity of the generated text based on nucleus sampling.

    Supports a range of 0.0-1.0.
    """


class MessagesUnionMember1ContentUnionMember1ImageURL(TypedDict, total=False):
    detail: str
    """Specifies the detail level of the image. Defaults to `auto`."""

    url: str
    """The base64 content with this prefix `data:image/jpeg;base64,`"""


class MessagesUnionMember1ContentUnionMember1(TypedDict, total=False):
    image_url: MessagesUnionMember1ContentUnionMember1ImageURL

    text: str
    """The text to provide."""

    type: str
    """The type of content ('text', 'image_url')."""


class MessagesUnionMember1(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessagesUnionMember1ContentUnionMember1]]]
    """A string of the message content"""

    role: Required[str]
    """The role of the sender (user or assistant)."""


class Input(TypedDict, total=False):
    """Options to affect the input of the request."""

    block_prompt_injection: bool
    """Set to true to detect prompt injection attacks."""

    entity_list: SequenceNotStr[str]
    """An array of entity types that the PII check should ignore."""

    pii: str
    """Set to either 'block' or 'replace'."""

    pii_replace_method: str
    """Set to either 'random', 'fake', 'category', 'mask'."""


class LogitBias(TypedDict, total=False):
    """Modifies the likelihood of specified tokens appearing in a response."""

    token: str
    """A string of the chosen token ID. Value is an int from -100 to 100."""


class Output(TypedDict, total=False):
    """Options to affect the output of the response."""

    factuality: bool
    """Set to true to turn on factuality processing."""

    toxicity: bool
    """Set to true to turn on toxicity processing."""


class StreamOptions(TypedDict, total=False):
    """Extra parameters used when streaming the response."""

    include_usage: bool
    """Whether to include tokens used in the stream response objects."""


class ToolChoiceUnionMember1Function(TypedDict, total=False):
    """An object containing the name of the function"""

    name: str


class ToolChoiceUnionMember1(TypedDict, total=False):
    """An object representing the tool to be chosen"""

    function: ToolChoiceUnionMember1Function
    """An object containing the name of the function"""

    type: str
    """The type of tool."""


ToolChoice: TypeAlias = Union[str, ToolChoiceUnionMember1]


class ToolFunction(TypedDict, total=False):
    """The tool information."""

    description: str
    """A description of what the function does."""

    name: str
    """The name of the function to be called."""

    parameters: object
    """The parameters the function accepts, described as a JSON Schema object."""

    strict: bool
    """Whether to enable strict schema adherence when generating the function call."""


class Tool(TypedDict, total=False):
    function: ToolFunction
    """The tool information."""

    type: str
    """The type of tool to call. Only 'function' is currently supported."""
