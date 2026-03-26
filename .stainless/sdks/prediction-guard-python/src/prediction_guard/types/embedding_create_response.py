# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["EmbeddingCreateResponse", "Data"]


class Data(BaseModel):
    embedding: Optional[List[float]] = None
    """The array of vector values."""

    index: Optional[int] = None
    """The index position in the collection."""


class EmbeddingCreateResponse(BaseModel):
    id: Optional[str] = None
    """Unique ID for the embeddings."""

    created: Optional[int] = None
    """Timestamp of when the embeddings was created."""

    data: Optional[List[Data]] = None
    """The set of vectorized data."""

    model: Optional[str] = None
    """The embeddings model used."""

    object: Optional[str] = None
    """Type of object (list)."""
