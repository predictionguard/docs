# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FactualityCheckParams"]


class FactualityCheckParams(TypedDict, total=False):
    reference: Required[str]
    """The reference text for comparison."""

    text: Required[str]
    """The text to be checked for factuality."""
