# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["CompletionCreateResponse", "Choice"]


class Choice(BaseModel):
    index: Optional[int] = None
    """The index position in the collection."""

    text: Optional[str] = None
    """The generated text."""


class CompletionCreateResponse(BaseModel):
    id: Optional[str] = None
    """Unique ID for the completion."""

    choices: Optional[List[Choice]] = None
    """The set of result choices."""

    created: Optional[int] = None
    """Timestamp of when the completion was created."""

    model: Optional[str] = None
    """The model used for generating the result."""

    object: Optional[str] = None
    """Type of object (completion)."""
