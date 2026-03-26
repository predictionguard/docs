# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ResponseCreateResponse", "Output", "OutputContent"]


class OutputContent(BaseModel):
    """The content for the output object."""

    text: Optional[str] = None
    """The output text."""

    type: Optional[str] = None
    """The type of output content."""


class Output(BaseModel):
    id: Optional[str] = None
    """The ID of the output object."""

    arguments: Optional[str] = None
    """The arguments used for the tool call used in the output."""

    call_id: Optional[str] = None
    """The call_id for the tool call used in the output,"""

    content: Optional[OutputContent] = None
    """The content for the output object."""

    error: Optional[str] = None
    """The error message from the MCP tool call."""

    name: Optional[str] = None
    """The name of the tool used in the output."""

    output: Optional[str] = None
    """The output of the MCP tool call."""

    role: Optional[str] = None
    """The role of the output object."""

    server_label: Optional[str] = None
    """The label of the MCP server used in the output."""

    status: Optional[str] = None
    """The status of the output object."""

    type: Optional[str] = None
    """The type of output object."""


class ResponseCreateResponse(BaseModel):
    id: Optional[str] = None
    """Unique ID for the chat completion."""

    created_at: Optional[int] = None
    """Timestamp of when the chat completion was created."""

    instructions: Optional[str] = None
    """The instructions entered in the request input."""

    max_output_tokens: Optional[int] = None
    """The max_output_tokens value entered in the request input."""

    max_tool_calls: Optional[int] = None
    """The max_tool_calls specified in the request."""

    model: Optional[str] = None
    """The chat model used for generating completions."""

    object: Optional[str] = None
    """Type of object (chat completion)."""

    output: Optional[List[Output]] = None
    """The set of result outputs."""

    parallel_tool_calls: Optional[int] = None
    """The parallel_tool_calls value entered in the request input."""

    status: Optional[str] = None
    """The status of the request."""

    temperature: Optional[float] = None
    """The temperature value entered in the request input."""
