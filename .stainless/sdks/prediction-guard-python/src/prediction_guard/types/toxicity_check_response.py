# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ToxicityCheckResponse", "Check"]


class Check(BaseModel):
    index: Optional[int] = None
    """The index position in the collection."""

    score: Optional[float] = None
    """The toxicity score."""


class ToxicityCheckResponse(BaseModel):
    id: Optional[str] = None
    """Unique ID for the toxicity check."""

    checks: Optional[List[Check]] = None
    """The set of vectorized data."""

    created: Optional[int] = None
    """Timestamp of when the toxicity check was created."""

    object: Optional[str] = None
    """Type of object (toxicity.check)."""
