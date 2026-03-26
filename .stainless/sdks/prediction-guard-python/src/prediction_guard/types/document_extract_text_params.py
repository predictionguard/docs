# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes, SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["DocumentExtractTextParams"]


class DocumentExtractTextParams(TypedDict, total=False):
    file: Required[FileTypes]
    """The document file to upload."""

    chunk_document: Annotated[bool, PropertyInfo(alias="chunkDocument")]
    """Whether to separate the document into chunks."""

    chunk_size: Annotated[int, PropertyInfo(alias="chunkSize")]
    """The size of chunks for the documents."""

    embed_images: Annotated[bool, PropertyInfo(alias="embedImages")]
    """Whether to embed images from the document."""

    enable_ocr: Annotated[bool, PropertyInfo(alias="enableOCR")]
    """Whether to enable OCR for document parsing."""

    output_format: Annotated[str, PropertyInfo(alias="outputFormat")]
    """The output format for the content of the document."""

    entity_list: Annotated[SequenceNotStr[str], PropertyInfo(alias="Entity-List")]

    injection: Annotated[bool, PropertyInfo(alias="Injection")]

    pii: Annotated[str, PropertyInfo(alias="Pii")]

    replace_method: Annotated[str, PropertyInfo(alias="Replace-Method")]

    toxicity: Annotated[bool, PropertyInfo(alias="Toxicity")]
