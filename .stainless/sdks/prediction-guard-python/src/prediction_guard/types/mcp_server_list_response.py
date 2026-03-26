# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["McpServerListResponse", "Data"]


class Data(BaseModel):
    available_tools: Optional[List[str]] = None
    """An array containing the available tools included in the MCP server."""

    created: Optional[int] = None
    """The date the MCP server was added."""

    object: Optional[str] = None
    """The object type (mcp_server)."""

    owned_by: Optional[str] = None
    """The name of the organization that owns the MCP server."""

    server_description: Optional[str] = None
    """A short description of the MCP server."""

    server_label: Optional[str] = None
    """The id of the MCP server."""


class McpServerListResponse(BaseModel):
    data: Optional[List[Data]] = None
    """The available MCP servers."""

    object: Optional[str] = None
    """Type of object (list)."""
