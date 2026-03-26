# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prediction_guard import PredictionGuard, AsyncPredictionGuard
from prediction_guard.types import ResponseCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResponses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: PredictionGuard) -> None:
        response = client.responses.create(
            input="Tell me a joke.",
            model="{{TEXT_MODEL}}",
        )
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: PredictionGuard) -> None:
        response = client.responses.create(
            input="Tell me a joke.",
            model="{{TEXT_MODEL}}",
            instructions="instructions",
            max_output_tokens=0,
            max_tool_calls=0,
            parallel_tool_calls=True,
            reasoning={"effort": "effort"},
            safeguards={
                "block_prompt_injection": True,
                "entity_list": ["string"],
                "factuality": True,
                "pii": "replace",
                "pii_replace_method": "random",
                "toxicity": True,
            },
            stream=True,
            stream_options={"include_usage": True},
            temperature=0,
            tool_choice="string",
            tools=[
                {
                    "allowed_tools": [{}],
                    "authorization": "authorization",
                    "description": "description",
                    "headers": {},
                    "initials": "initials",
                    "name": "name",
                    "parameters": {},
                    "server_description": "server_description",
                    "server_label": "server_label",
                    "server_url": "server_url",
                    "strict": True,
                    "type": "type",
                }
            ],
            top_p=0,
        )
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: PredictionGuard) -> None:
        http_response = client.responses.with_raw_response.create(
            input="Tell me a joke.",
            model="{{TEXT_MODEL}}",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: PredictionGuard) -> None:
        with client.responses.with_streaming_response.create(
            input="Tell me a joke.",
            model="{{TEXT_MODEL}}",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = http_response.parse()
            assert_matches_type(ResponseCreateResponse, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True


class TestAsyncResponses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPredictionGuard) -> None:
        response = await async_client.responses.create(
            input="Tell me a joke.",
            model="{{TEXT_MODEL}}",
        )
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPredictionGuard) -> None:
        response = await async_client.responses.create(
            input="Tell me a joke.",
            model="{{TEXT_MODEL}}",
            instructions="instructions",
            max_output_tokens=0,
            max_tool_calls=0,
            parallel_tool_calls=True,
            reasoning={"effort": "effort"},
            safeguards={
                "block_prompt_injection": True,
                "entity_list": ["string"],
                "factuality": True,
                "pii": "replace",
                "pii_replace_method": "random",
                "toxicity": True,
            },
            stream=True,
            stream_options={"include_usage": True},
            temperature=0,
            tool_choice="string",
            tools=[
                {
                    "allowed_tools": [{}],
                    "authorization": "authorization",
                    "description": "description",
                    "headers": {},
                    "initials": "initials",
                    "name": "name",
                    "parameters": {},
                    "server_description": "server_description",
                    "server_label": "server_label",
                    "server_url": "server_url",
                    "strict": True,
                    "type": "type",
                }
            ],
            top_p=0,
        )
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPredictionGuard) -> None:
        http_response = await async_client.responses.with_raw_response.create(
            input="Tell me a joke.",
            model="{{TEXT_MODEL}}",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = await http_response.parse()
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPredictionGuard) -> None:
        async with async_client.responses.with_streaming_response.create(
            input="Tell me a joke.",
            model="{{TEXT_MODEL}}",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = await http_response.parse()
            assert_matches_type(ResponseCreateResponse, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True
