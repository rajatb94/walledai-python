# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from walledai import WalledAI, AsyncWalledAI
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModeration:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: WalledAI) -> None:
        moderation = client.moderation.create(
            text="text",
        )
        assert_matches_type(object, moderation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: WalledAI) -> None:
        response = client.moderation.with_raw_response.create(
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderation = response.parse()
        assert_matches_type(object, moderation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: WalledAI) -> None:
        with client.moderation.with_streaming_response.create(
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            moderation = response.parse()
            assert_matches_type(object, moderation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncModeration:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncWalledAI) -> None:
        moderation = await async_client.moderation.create(
            text="text",
        )
        assert_matches_type(object, moderation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWalledAI) -> None:
        response = await async_client.moderation.with_raw_response.create(
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderation = await response.parse()
        assert_matches_type(object, moderation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWalledAI) -> None:
        async with async_client.moderation.with_streaming_response.create(
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            moderation = await response.parse()
            assert_matches_type(object, moderation, path=["response"])

        assert cast(Any, response.is_closed) is True
