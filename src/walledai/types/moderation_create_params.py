# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ModerationCreateParams"]


class ModerationCreateParams(TypedDict, total=False):
    text: Required[str]
