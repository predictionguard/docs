# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["PiiReplaceResponse", "Check", "CheckPiiTypeAndPosition"]


class CheckPiiTypeAndPosition(BaseModel):
    end: Optional[int] = None
    """The ending index of the pii item."""

    start: Optional[int] = None
    """The starting index of the pii item."""

    type: Optional[str] = None
    """The type of the pii item."""


class Check(BaseModel):
    index: Optional[int] = None
    """The index position in the collection."""

    new_prompt: Optional[str] = None
    """The new prompt with the replaced information."""

    pii_type_and_positions: Optional[List[CheckPiiTypeAndPosition]] = None
    """An array of PII metadata objects"""

    prompt: Optional[str] = None
    """The prompt that was checked for PII. Only returned if no PII is present."""

    status: Optional[str] = None
    """The response if this choice was successful."""


class PiiReplaceResponse(BaseModel):
    id: Optional[str] = None
    """Unique ID for the PII check."""

    checks: Optional[List[Check]] = None
    """The set of vectorized data."""

    created: Optional[int] = None
    """Timestamp of when the PII check was created."""

    object: Optional[str] = None
    """Type of object (pii_check)."""
