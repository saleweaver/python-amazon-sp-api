from __future__ import annotations

import enum
from typing import Any, Literal, TYPE_CHECKING, overload

from sp_api.asyncio.base import AsyncBaseClient
from sp_api.util.versioned_client import VersionedClientMeta

from .feeds_2021_06_30 import FeedsV20210630


class FeedsVersion(str, enum.Enum):
    V_2021_06_30 = "2021-06-30"
    LATEST = "2021-06-30"


if TYPE_CHECKING:

    class _FeedsMeta(VersionedClientMeta):
        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[FeedsVersion.V_2021_06_30, FeedsVersion.LATEST, "2021-06-30"],
            **kwargs: Any,
        ) -> FeedsV20210630: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> FeedsV20210630: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: str | FeedsVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...


else:
    _FeedsMeta = VersionedClientMeta


class Feeds(AsyncBaseClient, metaclass=_FeedsMeta):
    """Feeds API client.

    This class dispatches to a versioned Feeds API client.

    If you do not pass a version, the constructor returns the oldest supported implementation ("2021-06-30").
    """

    if TYPE_CHECKING:
        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[FeedsVersion.V_2021_06_30, FeedsVersion.LATEST, "2021-06-30"],
            **kwargs: Any,
        ) -> FeedsV20210630: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> FeedsV20210630: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: str | FeedsVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...

    _DISPATCH = True

    _DEFAULT_VERSION = "2021-06-30"

    _VERSION_MAP = {
        "2021-06-30": FeedsV20210630,
    }

    _VERSION_ALIASES = {
        "2021-06-30": "2021-06-30",
    }
