# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["DetokenizeCreateResponse"]


class DetokenizeCreateResponse(BaseModel):
    id: Optional[str] = None
    """Unique ID for the token."""

    created: Optional[int] = None
    """Timestamp of when the tokens were generated."""

    model: Optional[str] = None
    """The name of the model used."""

    object: Optional[str] = None
    """Type of object (tokens)."""

    text: Optional[str] = None
    """The converted tokens"""
