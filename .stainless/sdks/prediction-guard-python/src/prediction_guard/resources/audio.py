# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Mapping, Iterable, cast

import httpx

from ..types import audio_transcribe_params
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
from ..types.audio_transcribe_response import AudioTranscribeResponse

__all__ = ["AudioResource", "AsyncAudioResource"]


class AudioResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AudioResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return AudioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AudioResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return AudioResourceWithStreamingResponse(self)

    def transcribe(
        self,
        *,
        file: FileTypes,
        model: str,
        diarization: bool | Omit = omit,
        language: str | Omit = omit,
        prompt: str | Omit = omit,
        response_format: str | Omit = omit,
        temperature: float | Omit = omit,
        timestamps_granularities: Union[str, Iterable[object]] | Omit = omit,
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
    ) -> AudioTranscribeResponse:
        """
        This endpoint allows you to transcribe audio.

        Args:
          file: The audio file to upload.

          model: The transcription model to use.

          diarization: Whether to diarize the audio and return speaker turns. Not currently supported
              in multi-tenant environments.

          language: The language the audio is in.

          prompt: An optional text to guide the model's style or continue a previous audio
              segment.

          response_format: The format for the response object. Defaults to "json" and must be set to
              "verbose_json" when using diarization or timestamp granularities.

          temperature: The temperature parameter for controlling randomness in transcription. Supports
              a range of 0.0-2.0.

          timestamps_granularities: Sets whether timestamps are returned and at what granularity.

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
                "model": model,
                "diarization": diarization,
                "language": language,
                "prompt": prompt,
                "response_format": response_format,
                "temperature": temperature,
                "timestamps_granularities": timestamps_granularities,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/audio/transcriptions",
            body=maybe_transform(body, audio_transcribe_params.AudioTranscribeParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AudioTranscribeResponse,
        )


class AsyncAudioResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAudioResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAudioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAudioResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prediction-guard-python#with_streaming_response
        """
        return AsyncAudioResourceWithStreamingResponse(self)

    async def transcribe(
        self,
        *,
        file: FileTypes,
        model: str,
        diarization: bool | Omit = omit,
        language: str | Omit = omit,
        prompt: str | Omit = omit,
        response_format: str | Omit = omit,
        temperature: float | Omit = omit,
        timestamps_granularities: Union[str, Iterable[object]] | Omit = omit,
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
    ) -> AudioTranscribeResponse:
        """
        This endpoint allows you to transcribe audio.

        Args:
          file: The audio file to upload.

          model: The transcription model to use.

          diarization: Whether to diarize the audio and return speaker turns. Not currently supported
              in multi-tenant environments.

          language: The language the audio is in.

          prompt: An optional text to guide the model's style or continue a previous audio
              segment.

          response_format: The format for the response object. Defaults to "json" and must be set to
              "verbose_json" when using diarization or timestamp granularities.

          temperature: The temperature parameter for controlling randomness in transcription. Supports
              a range of 0.0-2.0.

          timestamps_granularities: Sets whether timestamps are returned and at what granularity.

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
                "model": model,
                "diarization": diarization,
                "language": language,
                "prompt": prompt,
                "response_format": response_format,
                "temperature": temperature,
                "timestamps_granularities": timestamps_granularities,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/audio/transcriptions",
            body=await async_maybe_transform(body, audio_transcribe_params.AudioTranscribeParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AudioTranscribeResponse,
        )


class AudioResourceWithRawResponse:
    def __init__(self, audio: AudioResource) -> None:
        self._audio = audio

        self.transcribe = to_raw_response_wrapper(
            audio.transcribe,
        )


class AsyncAudioResourceWithRawResponse:
    def __init__(self, audio: AsyncAudioResource) -> None:
        self._audio = audio

        self.transcribe = async_to_raw_response_wrapper(
            audio.transcribe,
        )


class AudioResourceWithStreamingResponse:
    def __init__(self, audio: AudioResource) -> None:
        self._audio = audio

        self.transcribe = to_streamed_response_wrapper(
            audio.transcribe,
        )


class AsyncAudioResourceWithStreamingResponse:
    def __init__(self, audio: AsyncAudioResource) -> None:
        self._audio = audio

        self.transcribe = async_to_streamed_response_wrapper(
            audio.transcribe,
        )
