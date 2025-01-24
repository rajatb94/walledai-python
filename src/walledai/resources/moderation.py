# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import moderation_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["ModerationResource", "AsyncModerationResource"]


class ModerationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ModerationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rajatb94/walledai-python#accessing-raw-response-data-eg-headers
        """
        return ModerationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModerationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rajatb94/walledai-python#with_streaming_response
        """
        return ModerationResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Moderate

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/guardrail",
            body=maybe_transform({"text": text}, moderation_create_params.ModerationCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncModerationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncModerationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rajatb94/walledai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModerationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModerationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rajatb94/walledai-python#with_streaming_response
        """
        return AsyncModerationResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Moderate

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/guardrail",
            body=await async_maybe_transform({"text": text}, moderation_create_params.ModerationCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ModerationResourceWithRawResponse:
    def __init__(self, moderation: ModerationResource) -> None:
        self._moderation = moderation

        self.create = to_raw_response_wrapper(
            moderation.create,
        )


class AsyncModerationResourceWithRawResponse:
    def __init__(self, moderation: AsyncModerationResource) -> None:
        self._moderation = moderation

        self.create = async_to_raw_response_wrapper(
            moderation.create,
        )


class ModerationResourceWithStreamingResponse:
    def __init__(self, moderation: ModerationResource) -> None:
        self._moderation = moderation

        self.create = to_streamed_response_wrapper(
            moderation.create,
        )


class AsyncModerationResourceWithStreamingResponse:
    def __init__(self, moderation: AsyncModerationResource) -> None:
        self._moderation = moderation

        self.create = async_to_streamed_response_wrapper(
            moderation.create,
        )
