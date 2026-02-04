from __future__ import annotations

import enum
from typing import Any, Literal, TYPE_CHECKING, overload

from sp_api.asyncio.base import AsyncBaseClient
from sp_api.util.versioned_client import VersionedClientMeta

from .fulfillment_inbound_2024_03_20 import FulfillmentInboundV20240320
from .fulfillment_inbound_v0 import FulfillmentInboundV0


class FulfillmentInboundVersion(str, enum.Enum):
    V0 = "v0"
    V_2024_03_20 = "2024-03-20"
    LATEST = "2024-03-20"


if TYPE_CHECKING:

    class _FulfillmentInboundMeta(VersionedClientMeta):
        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[
                FulfillmentInboundVersion.V_2024_03_20,
                FulfillmentInboundVersion.LATEST,
                "2024-03-20",
            ],
            **kwargs: Any,
        ) -> FulfillmentInboundV20240320: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[FulfillmentInboundVersion.V0, "v0"],
            **kwargs: Any,
        ) -> FulfillmentInboundV0: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> FulfillmentInboundV0: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: str | FulfillmentInboundVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...


else:
    _FulfillmentInboundMeta = VersionedClientMeta


class FulfillmentInbound(AsyncBaseClient, metaclass=_FulfillmentInboundMeta):
    """Fulfillment Inbound API client.

    This class dispatches to a versioned Fulfillment Inbound API client.

    If you do not pass a version, the constructor returns the oldest supported implementation ("v0").
    """

    if TYPE_CHECKING:
        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[
                FulfillmentInboundVersion.V_2024_03_20,
                FulfillmentInboundVersion.LATEST,
                "2024-03-20",
            ],
            **kwargs: Any,
        ) -> FulfillmentInboundV20240320: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[FulfillmentInboundVersion.V0, "v0"],
            **kwargs: Any,
        ) -> FulfillmentInboundV0: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> FulfillmentInboundV0: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: str | FulfillmentInboundVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...

    _DISPATCH = True

    _DEFAULT_VERSION = "v0"

    _VERSION_MAP = {
        "v0": FulfillmentInboundV0,
        "2024-03-20": FulfillmentInboundV20240320,
    }

    _VERSION_ALIASES = {
        "v0": "v0",
        "2024-03-20": "2024-03-20",
    }
