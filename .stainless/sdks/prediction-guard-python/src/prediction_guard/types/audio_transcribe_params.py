# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes, SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AudioTranscribeParams"]


class AudioTranscribeParams(TypedDict, total=False):
    file: Required[FileTypes]
    """The audio file to upload."""

    model: Required[str]
    """The transcription model to use."""

    diarization: bool
    """Whether to diarize the audio and return speaker turns.

    Not currently supported in multi-tenant environments.
    """

    language: str
    """The language the audio is in."""

    prompt: str
    """
    An optional text to guide the model's style or continue a previous audio
    segment.
    """

    response_format: str
    """The format for the response object.

    Defaults to "json" and must be set to "verbose_json" when using diarization or
    timestamp granularities.
    """

    temperature: float
    """The temperature parameter for controlling randomness in transcription.

    Supports a range of 0.0-2.0.
    """

    timestamps_granularities: Annotated[Union[str, Iterable[object]], PropertyInfo(alias="timestamps_granularities[]")]
    """Sets whether timestamps are returned and at what granularity."""

    entity_list: Annotated[SequenceNotStr[str], PropertyInfo(alias="Entity-List")]

    injection: Annotated[bool, PropertyInfo(alias="Injection")]

    pii: Annotated[str, PropertyInfo(alias="Pii")]

    replace_method: Annotated[str, PropertyInfo(alias="Replace-Method")]

    toxicity: Annotated[bool, PropertyInfo(alias="Toxicity")]
