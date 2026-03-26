# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["PiiReplaceParams"]


class PiiReplaceParams(TypedDict, total=False):
    prompt: Required[Union[str, SequenceNotStr[str]]]
    """The prompt to check for personal information."""

    replace: Required[bool]
    """Whether to replace personal information."""

    entity_list: SequenceNotStr[str]
    """An array of entity types that the PII check should ignore."""

    replace_method: str
    """The method to use (random, fake, category, mask)."""
