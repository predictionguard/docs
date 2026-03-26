# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["InjectionCreateParams"]


class InjectionCreateParams(TypedDict, total=False):
    detect: Required[bool]
    """Whether to detect potential injection attacks."""

    prompt: Required[Union[str, SequenceNotStr[str]]]
    """The prompt to check for injection attack."""
