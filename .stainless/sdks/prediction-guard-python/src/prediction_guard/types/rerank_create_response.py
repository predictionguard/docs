# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["RerankCreateResponse", "Result"]


class Result(BaseModel):
    index: Optional[int] = None
    """The index position in the collection."""

    relevance_score: Optional[float] = None
    """The relevance ranking score."""

    text: Optional[str] = None
    """The returned document"""


class RerankCreateResponse(BaseModel):
    id: Optional[str] = None
    """Unique ID for the rerank response."""

    created: Optional[int] = None
    """Timestamp of when the rerank response was created."""

    model: Optional[str] = None
    """The rerank model used."""

    object: Optional[str] = None
    """Type of object (list)."""

    results: Optional[List[Result]] = None
    """The set of rankings."""
