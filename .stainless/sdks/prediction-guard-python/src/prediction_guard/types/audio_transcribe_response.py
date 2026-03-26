# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AudioTranscribeResponse", "Segment", "Word"]


class Segment(BaseModel):
    id: Optional[int] = None
    """The id of the segment."""

    end: Optional[float] = None
    """The end time of the segment in seconds."""

    speaker: Optional[str] = None
    """The speaker of the segment."""

    start: Optional[float] = None
    """The start time of the segment in seconds."""

    text: Optional[str] = None
    """The text for the segment."""


class Word(BaseModel):
    end: Optional[float] = None
    """The end time of the word in seconds."""

    speaker: Optional[str] = None
    """The speaker of the word."""

    start: Optional[float] = None
    """The start time of the word in seconds."""

    text: Optional[str] = None
    """The text for the word."""


class AudioTranscribeResponse(BaseModel):
    duration: Optional[float] = None
    """The duration of the audio file in seconds."""

    language: Optional[str] = None
    """The language of the audio file."""

    segments: Optional[List[Segment]] = None
    """An array containing objects with segment level data."""

    task: Optional[str] = None
    """The task used in the request."""

    text: Optional[str] = None
    """The transcribed audio."""

    words: Optional[List[Word]] = None
    """An array containing objects with word level data."""
