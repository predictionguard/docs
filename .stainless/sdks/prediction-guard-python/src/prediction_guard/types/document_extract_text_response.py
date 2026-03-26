# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["DocumentExtractTextResponse"]


class DocumentExtractTextResponse(BaseModel):
    contents: Optional[str] = None
    """The parsed document contents."""

    count: Optional[int] = None
    """The word count for the document."""

    title: Optional[str] = None
    """The parsed document title."""
