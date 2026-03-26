# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["CompletionCreateParams", "Input", "LogitBias", "Output", "StreamOptions"]


class CompletionCreateParams(TypedDict, total=False):
    model: Required[str]
    """The chat model to use for generating completions."""

    prompt: Required[Union[str, SequenceNotStr[str]]]
    """The prompt to use for generating completions."""

    frequency_penalty: float
    """
    A value between -2.0 and 2.0, with positive values increasingly penalizing new
    tokens based on their frequency so far in order to decrease further occurrences.
    """

    input: Input
    """Options to affect the input of the request."""

    logit_bias: LogitBias
    """Modifies the likelihood of specified tokens appearing in a response."""

    max_tokens: int
    """The maximum number of tokens in the generated completion."""

    output: Output
    """Options to affect the output of the response."""

    presence_penalty: float
    """
    A value between -2.0 and 2.0, with positive values causing a flat reduction of
    new tokens based on their existing presence so far in order to decrease further
    occurrences.
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

    top_k: int
    """The diversity of the generated text based on top-k sampling."""

    top_p: float
    """The diversity of the generated text based on nucleus sampling.

    Supports a range of 0.0-1.0.
    """


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
