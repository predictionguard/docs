# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["InjectionCreateResponse", "Check"]


class Check(BaseModel):
    index: Optional[int] = None
    """The index position in the collection."""

    probability: Optional[float] = None
    """The probability of a potential injection attack."""

    status: Optional[str] = None
    """The response if this choice was successful."""


class InjectionCreateResponse(BaseModel):
    id: Optional[str] = None
    """Unique ID for the injection check."""

    checks: Optional[List[Check]] = None
    """The set of vectorized data."""

    created: Optional[int] = None
    """Timestamp of when the injection check was created."""

    object: Optional[str] = None
    """Type of object (injection_check)."""
