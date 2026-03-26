# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = ["EmbeddingCreateParams", "InputUnionMember1", "InputUnionMember1UnionMember3"]


class EmbeddingCreateParams(TypedDict, total=False):
    input: Required[Union[str, SequenceNotStr[InputUnionMember1]]]
    """A string of text to be embedded."""

    model: Required[str]
    """The model to use for generating vectors."""

    truncate: bool
    """Boolean setting whether to truncate inputs. Not supported by bridgetower."""

    truncation_direction: str
    """Which direction to truncate, "Left" or "Right". Not supported by bridgetower."""


class InputUnionMember1UnionMember3(TypedDict, total=False):
    """Use this option for multimodal input."""

    image: str
    """The base64 encoding of an image. You can choose to provide this or not."""

    text: str
    """The text to embed. You can choose to provide this or not."""


InputUnionMember1: TypeAlias = Union[str, int, Iterable[int], InputUnionMember1UnionMember3]
