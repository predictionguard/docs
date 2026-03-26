# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TokenizeGenerateParams"]


class TokenizeGenerateParams(TypedDict, total=False):
    input: Required[str]
    """The text to tokenize."""

    model: Required[str]
    """The name of the model to use for tokenization."""
