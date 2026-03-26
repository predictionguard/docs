# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["McpToolListResponse", "Data"]


class Data(BaseModel):
    """The MCP tool information."""

    id: Optional[str] = None
    """The id of the MCP tool."""

    created: Optional[int] = None
    """The date the MCP tool was added."""

    description: Optional[str] = None
    """A short description of the MCP tool."""

    object: Optional[str] = None
    """The object type (mcp_tool)."""

    owned_by: Optional[str] = None
    """The name of the organization that owns the MCP tool."""

    parameters: Optional[builtins.object] = None
    """The parameters necessary for using the MCP tool."""


class McpToolListResponse(BaseModel):
    data: Optional[Dict[str, List[Data]]] = None
    """The available mcp tools."""

    object: Optional[str] = None
    """Type of object (list)."""
