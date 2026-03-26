# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["TokenizeGenerateResponse", "Token"]


class Token(BaseModel):
    id: Optional[int] = None
    """The converted token."""

    start: Optional[int] = None
    """The index the token starts at."""

    stop: Optional[int] = None
    """The index the token ends at."""

    text: Optional[str] = None
    """The token as text."""


class TokenizeGenerateResponse(BaseModel):
    id: Optional[str] = None
    """Unique ID for the token."""

    created: Optional[int] = None
    """Timestamp of when the tokens were generated."""

    model: Optional[str] = None
    """The name of the model used."""

    object: Optional[str] = None
    """Type of object (tokens)."""

    tokens: Optional[List[Token]] = None
    """An array of token data."""
