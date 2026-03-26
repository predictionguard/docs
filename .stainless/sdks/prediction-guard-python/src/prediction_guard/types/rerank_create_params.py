# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["RerankCreateParams"]


class RerankCreateParams(TypedDict, total=False):
    documents: Required[SequenceNotStr[str]]
    """Array of documents to rank."""

    model: Required[str]
    """The model to use for reranking."""

    query: Required[str]
    """The query to rank against."""

    return_documents: bool
    """Boolean setting whether to return documents in output."""
