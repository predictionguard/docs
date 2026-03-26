# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, PredictionGuardError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        pii,
        chat,
        audio,
        models,
        rerank,
        tokenize,
        toxicity,
        documents,
        injection,
        mcp_tools,
        responses,
        detokenize,
        embeddings,
        factuality,
        completions,
        mcp_servers,
    )
    from .resources.pii import PiiResource, AsyncPiiResource
    from .resources.chat import ChatResource, AsyncChatResource
    from .resources.audio import AudioResource, AsyncAudioResource
    from .resources.models import ModelsResource, AsyncModelsResource
    from .resources.rerank import RerankResource, AsyncRerankResource
    from .resources.tokenize import TokenizeResource, AsyncTokenizeResource
    from .resources.toxicity import ToxicityResource, AsyncToxicityResource
    from .resources.documents import DocumentsResource, AsyncDocumentsResource
    from .resources.injection import InjectionResource, AsyncInjectionResource
    from .resources.mcp_tools import McpToolsResource, AsyncMcpToolsResource
    from .resources.responses import ResponsesResource, AsyncResponsesResource
    from .resources.detokenize import DetokenizeResource, AsyncDetokenizeResource
    from .resources.embeddings import EmbeddingsResource, AsyncEmbeddingsResource
    from .resources.factuality import FactualityResource, AsyncFactualityResource
    from .resources.completions import CompletionsResource, AsyncCompletionsResource
    from .resources.mcp_servers import McpServersResource, AsyncMcpServersResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "PredictionGuard",
    "AsyncPredictionGuard",
    "Client",
    "AsyncClient",
]


class PredictionGuard(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous PredictionGuard client instance.

        This automatically infers the `api_key` argument from the `PREDICTION_GUARD_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("PREDICTION_GUARD_API_KEY")
        if api_key is None:
            raise PredictionGuardError(
                "The api_key client option must be set either by passing api_key to the client or by setting the PREDICTION_GUARD_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("PREDICTION_GUARD_BASE_URL")
        if base_url is None:
            base_url = f"https://api.predictionguard.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def audio(self) -> AudioResource:
        from .resources.audio import AudioResource

        return AudioResource(self)

    @cached_property
    def chat(self) -> ChatResource:
        from .resources.chat import ChatResource

        return ChatResource(self)

    @cached_property
    def completions(self) -> CompletionsResource:
        from .resources.completions import CompletionsResource

        return CompletionsResource(self)

    @cached_property
    def documents(self) -> DocumentsResource:
        from .resources.documents import DocumentsResource

        return DocumentsResource(self)

    @cached_property
    def embeddings(self) -> EmbeddingsResource:
        from .resources.embeddings import EmbeddingsResource

        return EmbeddingsResource(self)

    @cached_property
    def mcp_servers(self) -> McpServersResource:
        from .resources.mcp_servers import McpServersResource

        return McpServersResource(self)

    @cached_property
    def mcp_tools(self) -> McpToolsResource:
        from .resources.mcp_tools import McpToolsResource

        return McpToolsResource(self)

    @cached_property
    def models(self) -> ModelsResource:
        from .resources.models import ModelsResource

        return ModelsResource(self)

    @cached_property
    def rerank(self) -> RerankResource:
        from .resources.rerank import RerankResource

        return RerankResource(self)

    @cached_property
    def responses(self) -> ResponsesResource:
        from .resources.responses import ResponsesResource

        return ResponsesResource(self)

    @cached_property
    def factuality(self) -> FactualityResource:
        from .resources.factuality import FactualityResource

        return FactualityResource(self)

    @cached_property
    def injection(self) -> InjectionResource:
        from .resources.injection import InjectionResource

        return InjectionResource(self)

    @cached_property
    def pii(self) -> PiiResource:
        from .resources.pii import PiiResource

        return PiiResource(self)

    @cached_property
    def toxicity(self) -> ToxicityResource:
        from .resources.toxicity import ToxicityResource

        return ToxicityResource(self)

    @cached_property
    def tokenize(self) -> TokenizeResource:
        from .resources.tokenize import TokenizeResource

        return TokenizeResource(self)

    @cached_property
    def detokenize(self) -> DetokenizeResource:
        from .resources.detokenize import DetokenizeResource

        return DetokenizeResource(self)

    @cached_property
    def with_raw_response(self) -> PredictionGuardWithRawResponse:
        return PredictionGuardWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PredictionGuardWithStreamedResponse:
        return PredictionGuardWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
        }

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncPredictionGuard(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncPredictionGuard client instance.

        This automatically infers the `api_key` argument from the `PREDICTION_GUARD_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("PREDICTION_GUARD_API_KEY")
        if api_key is None:
            raise PredictionGuardError(
                "The api_key client option must be set either by passing api_key to the client or by setting the PREDICTION_GUARD_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("PREDICTION_GUARD_BASE_URL")
        if base_url is None:
            base_url = f"https://api.predictionguard.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def audio(self) -> AsyncAudioResource:
        from .resources.audio import AsyncAudioResource

        return AsyncAudioResource(self)

    @cached_property
    def chat(self) -> AsyncChatResource:
        from .resources.chat import AsyncChatResource

        return AsyncChatResource(self)

    @cached_property
    def completions(self) -> AsyncCompletionsResource:
        from .resources.completions import AsyncCompletionsResource

        return AsyncCompletionsResource(self)

    @cached_property
    def documents(self) -> AsyncDocumentsResource:
        from .resources.documents import AsyncDocumentsResource

        return AsyncDocumentsResource(self)

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResource:
        from .resources.embeddings import AsyncEmbeddingsResource

        return AsyncEmbeddingsResource(self)

    @cached_property
    def mcp_servers(self) -> AsyncMcpServersResource:
        from .resources.mcp_servers import AsyncMcpServersResource

        return AsyncMcpServersResource(self)

    @cached_property
    def mcp_tools(self) -> AsyncMcpToolsResource:
        from .resources.mcp_tools import AsyncMcpToolsResource

        return AsyncMcpToolsResource(self)

    @cached_property
    def models(self) -> AsyncModelsResource:
        from .resources.models import AsyncModelsResource

        return AsyncModelsResource(self)

    @cached_property
    def rerank(self) -> AsyncRerankResource:
        from .resources.rerank import AsyncRerankResource

        return AsyncRerankResource(self)

    @cached_property
    def responses(self) -> AsyncResponsesResource:
        from .resources.responses import AsyncResponsesResource

        return AsyncResponsesResource(self)

    @cached_property
    def factuality(self) -> AsyncFactualityResource:
        from .resources.factuality import AsyncFactualityResource

        return AsyncFactualityResource(self)

    @cached_property
    def injection(self) -> AsyncInjectionResource:
        from .resources.injection import AsyncInjectionResource

        return AsyncInjectionResource(self)

    @cached_property
    def pii(self) -> AsyncPiiResource:
        from .resources.pii import AsyncPiiResource

        return AsyncPiiResource(self)

    @cached_property
    def toxicity(self) -> AsyncToxicityResource:
        from .resources.toxicity import AsyncToxicityResource

        return AsyncToxicityResource(self)

    @cached_property
    def tokenize(self) -> AsyncTokenizeResource:
        from .resources.tokenize import AsyncTokenizeResource

        return AsyncTokenizeResource(self)

    @cached_property
    def detokenize(self) -> AsyncDetokenizeResource:
        from .resources.detokenize import AsyncDetokenizeResource

        return AsyncDetokenizeResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncPredictionGuardWithRawResponse:
        return AsyncPredictionGuardWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPredictionGuardWithStreamedResponse:
        return AsyncPredictionGuardWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
        }

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class PredictionGuardWithRawResponse:
    _client: PredictionGuard

    def __init__(self, client: PredictionGuard) -> None:
        self._client = client

    @cached_property
    def audio(self) -> audio.AudioResourceWithRawResponse:
        from .resources.audio import AudioResourceWithRawResponse

        return AudioResourceWithRawResponse(self._client.audio)

    @cached_property
    def chat(self) -> chat.ChatResourceWithRawResponse:
        from .resources.chat import ChatResourceWithRawResponse

        return ChatResourceWithRawResponse(self._client.chat)

    @cached_property
    def completions(self) -> completions.CompletionsResourceWithRawResponse:
        from .resources.completions import CompletionsResourceWithRawResponse

        return CompletionsResourceWithRawResponse(self._client.completions)

    @cached_property
    def documents(self) -> documents.DocumentsResourceWithRawResponse:
        from .resources.documents import DocumentsResourceWithRawResponse

        return DocumentsResourceWithRawResponse(self._client.documents)

    @cached_property
    def embeddings(self) -> embeddings.EmbeddingsResourceWithRawResponse:
        from .resources.embeddings import EmbeddingsResourceWithRawResponse

        return EmbeddingsResourceWithRawResponse(self._client.embeddings)

    @cached_property
    def mcp_servers(self) -> mcp_servers.McpServersResourceWithRawResponse:
        from .resources.mcp_servers import McpServersResourceWithRawResponse

        return McpServersResourceWithRawResponse(self._client.mcp_servers)

    @cached_property
    def mcp_tools(self) -> mcp_tools.McpToolsResourceWithRawResponse:
        from .resources.mcp_tools import McpToolsResourceWithRawResponse

        return McpToolsResourceWithRawResponse(self._client.mcp_tools)

    @cached_property
    def models(self) -> models.ModelsResourceWithRawResponse:
        from .resources.models import ModelsResourceWithRawResponse

        return ModelsResourceWithRawResponse(self._client.models)

    @cached_property
    def rerank(self) -> rerank.RerankResourceWithRawResponse:
        from .resources.rerank import RerankResourceWithRawResponse

        return RerankResourceWithRawResponse(self._client.rerank)

    @cached_property
    def responses(self) -> responses.ResponsesResourceWithRawResponse:
        from .resources.responses import ResponsesResourceWithRawResponse

        return ResponsesResourceWithRawResponse(self._client.responses)

    @cached_property
    def factuality(self) -> factuality.FactualityResourceWithRawResponse:
        from .resources.factuality import FactualityResourceWithRawResponse

        return FactualityResourceWithRawResponse(self._client.factuality)

    @cached_property
    def injection(self) -> injection.InjectionResourceWithRawResponse:
        from .resources.injection import InjectionResourceWithRawResponse

        return InjectionResourceWithRawResponse(self._client.injection)

    @cached_property
    def pii(self) -> pii.PiiResourceWithRawResponse:
        from .resources.pii import PiiResourceWithRawResponse

        return PiiResourceWithRawResponse(self._client.pii)

    @cached_property
    def toxicity(self) -> toxicity.ToxicityResourceWithRawResponse:
        from .resources.toxicity import ToxicityResourceWithRawResponse

        return ToxicityResourceWithRawResponse(self._client.toxicity)

    @cached_property
    def tokenize(self) -> tokenize.TokenizeResourceWithRawResponse:
        from .resources.tokenize import TokenizeResourceWithRawResponse

        return TokenizeResourceWithRawResponse(self._client.tokenize)

    @cached_property
    def detokenize(self) -> detokenize.DetokenizeResourceWithRawResponse:
        from .resources.detokenize import DetokenizeResourceWithRawResponse

        return DetokenizeResourceWithRawResponse(self._client.detokenize)


class AsyncPredictionGuardWithRawResponse:
    _client: AsyncPredictionGuard

    def __init__(self, client: AsyncPredictionGuard) -> None:
        self._client = client

    @cached_property
    def audio(self) -> audio.AsyncAudioResourceWithRawResponse:
        from .resources.audio import AsyncAudioResourceWithRawResponse

        return AsyncAudioResourceWithRawResponse(self._client.audio)

    @cached_property
    def chat(self) -> chat.AsyncChatResourceWithRawResponse:
        from .resources.chat import AsyncChatResourceWithRawResponse

        return AsyncChatResourceWithRawResponse(self._client.chat)

    @cached_property
    def completions(self) -> completions.AsyncCompletionsResourceWithRawResponse:
        from .resources.completions import AsyncCompletionsResourceWithRawResponse

        return AsyncCompletionsResourceWithRawResponse(self._client.completions)

    @cached_property
    def documents(self) -> documents.AsyncDocumentsResourceWithRawResponse:
        from .resources.documents import AsyncDocumentsResourceWithRawResponse

        return AsyncDocumentsResourceWithRawResponse(self._client.documents)

    @cached_property
    def embeddings(self) -> embeddings.AsyncEmbeddingsResourceWithRawResponse:
        from .resources.embeddings import AsyncEmbeddingsResourceWithRawResponse

        return AsyncEmbeddingsResourceWithRawResponse(self._client.embeddings)

    @cached_property
    def mcp_servers(self) -> mcp_servers.AsyncMcpServersResourceWithRawResponse:
        from .resources.mcp_servers import AsyncMcpServersResourceWithRawResponse

        return AsyncMcpServersResourceWithRawResponse(self._client.mcp_servers)

    @cached_property
    def mcp_tools(self) -> mcp_tools.AsyncMcpToolsResourceWithRawResponse:
        from .resources.mcp_tools import AsyncMcpToolsResourceWithRawResponse

        return AsyncMcpToolsResourceWithRawResponse(self._client.mcp_tools)

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithRawResponse:
        from .resources.models import AsyncModelsResourceWithRawResponse

        return AsyncModelsResourceWithRawResponse(self._client.models)

    @cached_property
    def rerank(self) -> rerank.AsyncRerankResourceWithRawResponse:
        from .resources.rerank import AsyncRerankResourceWithRawResponse

        return AsyncRerankResourceWithRawResponse(self._client.rerank)

    @cached_property
    def responses(self) -> responses.AsyncResponsesResourceWithRawResponse:
        from .resources.responses import AsyncResponsesResourceWithRawResponse

        return AsyncResponsesResourceWithRawResponse(self._client.responses)

    @cached_property
    def factuality(self) -> factuality.AsyncFactualityResourceWithRawResponse:
        from .resources.factuality import AsyncFactualityResourceWithRawResponse

        return AsyncFactualityResourceWithRawResponse(self._client.factuality)

    @cached_property
    def injection(self) -> injection.AsyncInjectionResourceWithRawResponse:
        from .resources.injection import AsyncInjectionResourceWithRawResponse

        return AsyncInjectionResourceWithRawResponse(self._client.injection)

    @cached_property
    def pii(self) -> pii.AsyncPiiResourceWithRawResponse:
        from .resources.pii import AsyncPiiResourceWithRawResponse

        return AsyncPiiResourceWithRawResponse(self._client.pii)

    @cached_property
    def toxicity(self) -> toxicity.AsyncToxicityResourceWithRawResponse:
        from .resources.toxicity import AsyncToxicityResourceWithRawResponse

        return AsyncToxicityResourceWithRawResponse(self._client.toxicity)

    @cached_property
    def tokenize(self) -> tokenize.AsyncTokenizeResourceWithRawResponse:
        from .resources.tokenize import AsyncTokenizeResourceWithRawResponse

        return AsyncTokenizeResourceWithRawResponse(self._client.tokenize)

    @cached_property
    def detokenize(self) -> detokenize.AsyncDetokenizeResourceWithRawResponse:
        from .resources.detokenize import AsyncDetokenizeResourceWithRawResponse

        return AsyncDetokenizeResourceWithRawResponse(self._client.detokenize)


class PredictionGuardWithStreamedResponse:
    _client: PredictionGuard

    def __init__(self, client: PredictionGuard) -> None:
        self._client = client

    @cached_property
    def audio(self) -> audio.AudioResourceWithStreamingResponse:
        from .resources.audio import AudioResourceWithStreamingResponse

        return AudioResourceWithStreamingResponse(self._client.audio)

    @cached_property
    def chat(self) -> chat.ChatResourceWithStreamingResponse:
        from .resources.chat import ChatResourceWithStreamingResponse

        return ChatResourceWithStreamingResponse(self._client.chat)

    @cached_property
    def completions(self) -> completions.CompletionsResourceWithStreamingResponse:
        from .resources.completions import CompletionsResourceWithStreamingResponse

        return CompletionsResourceWithStreamingResponse(self._client.completions)

    @cached_property
    def documents(self) -> documents.DocumentsResourceWithStreamingResponse:
        from .resources.documents import DocumentsResourceWithStreamingResponse

        return DocumentsResourceWithStreamingResponse(self._client.documents)

    @cached_property
    def embeddings(self) -> embeddings.EmbeddingsResourceWithStreamingResponse:
        from .resources.embeddings import EmbeddingsResourceWithStreamingResponse

        return EmbeddingsResourceWithStreamingResponse(self._client.embeddings)

    @cached_property
    def mcp_servers(self) -> mcp_servers.McpServersResourceWithStreamingResponse:
        from .resources.mcp_servers import McpServersResourceWithStreamingResponse

        return McpServersResourceWithStreamingResponse(self._client.mcp_servers)

    @cached_property
    def mcp_tools(self) -> mcp_tools.McpToolsResourceWithStreamingResponse:
        from .resources.mcp_tools import McpToolsResourceWithStreamingResponse

        return McpToolsResourceWithStreamingResponse(self._client.mcp_tools)

    @cached_property
    def models(self) -> models.ModelsResourceWithStreamingResponse:
        from .resources.models import ModelsResourceWithStreamingResponse

        return ModelsResourceWithStreamingResponse(self._client.models)

    @cached_property
    def rerank(self) -> rerank.RerankResourceWithStreamingResponse:
        from .resources.rerank import RerankResourceWithStreamingResponse

        return RerankResourceWithStreamingResponse(self._client.rerank)

    @cached_property
    def responses(self) -> responses.ResponsesResourceWithStreamingResponse:
        from .resources.responses import ResponsesResourceWithStreamingResponse

        return ResponsesResourceWithStreamingResponse(self._client.responses)

    @cached_property
    def factuality(self) -> factuality.FactualityResourceWithStreamingResponse:
        from .resources.factuality import FactualityResourceWithStreamingResponse

        return FactualityResourceWithStreamingResponse(self._client.factuality)

    @cached_property
    def injection(self) -> injection.InjectionResourceWithStreamingResponse:
        from .resources.injection import InjectionResourceWithStreamingResponse

        return InjectionResourceWithStreamingResponse(self._client.injection)

    @cached_property
    def pii(self) -> pii.PiiResourceWithStreamingResponse:
        from .resources.pii import PiiResourceWithStreamingResponse

        return PiiResourceWithStreamingResponse(self._client.pii)

    @cached_property
    def toxicity(self) -> toxicity.ToxicityResourceWithStreamingResponse:
        from .resources.toxicity import ToxicityResourceWithStreamingResponse

        return ToxicityResourceWithStreamingResponse(self._client.toxicity)

    @cached_property
    def tokenize(self) -> tokenize.TokenizeResourceWithStreamingResponse:
        from .resources.tokenize import TokenizeResourceWithStreamingResponse

        return TokenizeResourceWithStreamingResponse(self._client.tokenize)

    @cached_property
    def detokenize(self) -> detokenize.DetokenizeResourceWithStreamingResponse:
        from .resources.detokenize import DetokenizeResourceWithStreamingResponse

        return DetokenizeResourceWithStreamingResponse(self._client.detokenize)


class AsyncPredictionGuardWithStreamedResponse:
    _client: AsyncPredictionGuard

    def __init__(self, client: AsyncPredictionGuard) -> None:
        self._client = client

    @cached_property
    def audio(self) -> audio.AsyncAudioResourceWithStreamingResponse:
        from .resources.audio import AsyncAudioResourceWithStreamingResponse

        return AsyncAudioResourceWithStreamingResponse(self._client.audio)

    @cached_property
    def chat(self) -> chat.AsyncChatResourceWithStreamingResponse:
        from .resources.chat import AsyncChatResourceWithStreamingResponse

        return AsyncChatResourceWithStreamingResponse(self._client.chat)

    @cached_property
    def completions(self) -> completions.AsyncCompletionsResourceWithStreamingResponse:
        from .resources.completions import AsyncCompletionsResourceWithStreamingResponse

        return AsyncCompletionsResourceWithStreamingResponse(self._client.completions)

    @cached_property
    def documents(self) -> documents.AsyncDocumentsResourceWithStreamingResponse:
        from .resources.documents import AsyncDocumentsResourceWithStreamingResponse

        return AsyncDocumentsResourceWithStreamingResponse(self._client.documents)

    @cached_property
    def embeddings(self) -> embeddings.AsyncEmbeddingsResourceWithStreamingResponse:
        from .resources.embeddings import AsyncEmbeddingsResourceWithStreamingResponse

        return AsyncEmbeddingsResourceWithStreamingResponse(self._client.embeddings)

    @cached_property
    def mcp_servers(self) -> mcp_servers.AsyncMcpServersResourceWithStreamingResponse:
        from .resources.mcp_servers import AsyncMcpServersResourceWithStreamingResponse

        return AsyncMcpServersResourceWithStreamingResponse(self._client.mcp_servers)

    @cached_property
    def mcp_tools(self) -> mcp_tools.AsyncMcpToolsResourceWithStreamingResponse:
        from .resources.mcp_tools import AsyncMcpToolsResourceWithStreamingResponse

        return AsyncMcpToolsResourceWithStreamingResponse(self._client.mcp_tools)

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithStreamingResponse:
        from .resources.models import AsyncModelsResourceWithStreamingResponse

        return AsyncModelsResourceWithStreamingResponse(self._client.models)

    @cached_property
    def rerank(self) -> rerank.AsyncRerankResourceWithStreamingResponse:
        from .resources.rerank import AsyncRerankResourceWithStreamingResponse

        return AsyncRerankResourceWithStreamingResponse(self._client.rerank)

    @cached_property
    def responses(self) -> responses.AsyncResponsesResourceWithStreamingResponse:
        from .resources.responses import AsyncResponsesResourceWithStreamingResponse

        return AsyncResponsesResourceWithStreamingResponse(self._client.responses)

    @cached_property
    def factuality(self) -> factuality.AsyncFactualityResourceWithStreamingResponse:
        from .resources.factuality import AsyncFactualityResourceWithStreamingResponse

        return AsyncFactualityResourceWithStreamingResponse(self._client.factuality)

    @cached_property
    def injection(self) -> injection.AsyncInjectionResourceWithStreamingResponse:
        from .resources.injection import AsyncInjectionResourceWithStreamingResponse

        return AsyncInjectionResourceWithStreamingResponse(self._client.injection)

    @cached_property
    def pii(self) -> pii.AsyncPiiResourceWithStreamingResponse:
        from .resources.pii import AsyncPiiResourceWithStreamingResponse

        return AsyncPiiResourceWithStreamingResponse(self._client.pii)

    @cached_property
    def toxicity(self) -> toxicity.AsyncToxicityResourceWithStreamingResponse:
        from .resources.toxicity import AsyncToxicityResourceWithStreamingResponse

        return AsyncToxicityResourceWithStreamingResponse(self._client.toxicity)

    @cached_property
    def tokenize(self) -> tokenize.AsyncTokenizeResourceWithStreamingResponse:
        from .resources.tokenize import AsyncTokenizeResourceWithStreamingResponse

        return AsyncTokenizeResourceWithStreamingResponse(self._client.tokenize)

    @cached_property
    def detokenize(self) -> detokenize.AsyncDetokenizeResourceWithStreamingResponse:
        from .resources.detokenize import AsyncDetokenizeResourceWithStreamingResponse

        return AsyncDetokenizeResourceWithStreamingResponse(self._client.detokenize)


Client = PredictionGuard

AsyncClient = AsyncPredictionGuard
