# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["DetokenizeCreateParams"]


class DetokenizeCreateParams(TypedDict, total=False):
    model: Required[str]
    """The name of the model to use for detokenization."""

    tokens: Required[Iterable[int]]
    """The tokens to turn into text."""
