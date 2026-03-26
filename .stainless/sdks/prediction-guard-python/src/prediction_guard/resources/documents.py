# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..types import document_extract_text_params
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from .._utils import is_given, extract_files, maybe_transform, strip_not_given, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.document_extract_text_response import DocumentExtractTextResponse

__all__ = ["DocumentsResource", "AsyncDocumentsResource"]


class DocumentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return DocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return DocumentsResourceWithStreamingResponse(self)

    def extract_text(
        self,
        *,
        file: FileTypes,
        chunk_document: bool | Omit = omit,
        chunk_size: int | Omit = omit,
        embed_images: bool | Omit = omit,
        enable_ocr: bool | Omit = omit,
        output_format: str | Omit = omit,
        entity_list: SequenceNotStr[str] | Omit = omit,
        injection: bool | Omit = omit,
        pii: str | Omit = omit,
        replace_method: str | Omit = omit,
        toxicity: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentExtractTextResponse:
        """
        This endpoint allows you to parse text from documents using OCR.

        Args:
          file: The document file to upload.

          chunk_document: Whether to separate the document into chunks.

          chunk_size: The size of chunks for the documents.

          embed_images: Whether to embed images from the document.

          enable_ocr: Whether to enable OCR for document parsing.

          output_format: The output format for the content of the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Entity-List": ",".join(entity_list) if is_given(entity_list) else not_given,
                    "Injection": ("true" if injection else "false") if is_given(injection) else not_given,
                    "Pii": pii,
                    "Replace-Method": replace_method,
                    "Toxicity": ("true" if toxicity else "false") if is_given(toxicity) else not_given,
                }
            ),
            **(extra_headers or {}),
        }
        body = deepcopy_minimal(
            {
                "file": file,
                "chunk_document": chunk_document,
                "chunk_size": chunk_size,
                "embed_images": embed_images,
                "enable_ocr": enable_ocr,
                "output_format": output_format,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/documents/extract",
            body=maybe_transform(body, document_extract_text_params.DocumentExtractTextParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentExtractTextResponse,
        )


class AsyncDocumentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return AsyncDocumentsResourceWithStreamingResponse(self)

    async def extract_text(
        self,
        *,
        file: FileTypes,
        chunk_document: bool | Omit = omit,
        chunk_size: int | Omit = omit,
        embed_images: bool | Omit = omit,
        enable_ocr: bool | Omit = omit,
        output_format: str | Omit = omit,
        entity_list: SequenceNotStr[str] | Omit = omit,
        injection: bool | Omit = omit,
        pii: str | Omit = omit,
        replace_method: str | Omit = omit,
        toxicity: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentExtractTextResponse:
        """
        This endpoint allows you to parse text from documents using OCR.

        Args:
          file: The document file to upload.

          chunk_document: Whether to separate the document into chunks.

          chunk_size: The size of chunks for the documents.

          embed_images: Whether to embed images from the document.

          enable_ocr: Whether to enable OCR for document parsing.

          output_format: The output format for the content of the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Entity-List": ",".join(entity_list) if is_given(entity_list) else not_given,
                    "Injection": ("true" if injection else "false") if is_given(injection) else not_given,
                    "Pii": pii,
                    "Replace-Method": replace_method,
                    "Toxicity": ("true" if toxicity else "false") if is_given(toxicity) else not_given,
                }
            ),
            **(extra_headers or {}),
        }
        body = deepcopy_minimal(
            {
                "file": file,
                "chunk_document": chunk_document,
                "chunk_size": chunk_size,
                "embed_images": embed_images,
                "enable_ocr": enable_ocr,
                "output_format": output_format,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/documents/extract",
            body=await async_maybe_transform(body, document_extract_text_params.DocumentExtractTextParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentExtractTextResponse,
        )


class DocumentsResourceWithRawResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.extract_text = to_raw_response_wrapper(
            documents.extract_text,
        )


class AsyncDocumentsResourceWithRawResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.extract_text = async_to_raw_response_wrapper(
            documents.extract_text,
        )


class DocumentsResourceWithStreamingResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.extract_text = to_streamed_response_wrapper(
            documents.extract_text,
        )


class AsyncDocumentsResourceWithStreamingResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.extract_text = async_to_streamed_response_wrapper(
            documents.extract_text,
        )
