from __future__ import annotations

import enum
from typing import Any, Literal, TYPE_CHECKING, overload

from sp_api.asyncio.base import AsyncBaseClient
from sp_api.util.versioned_client import VersionedClientMeta

from .inventory_2021_01_06 import ExternalFulfillmentInventoryV20210106
from .inventory_2024_09_11 import ExternalFulfillmentInventoryV20240911


class ExternalFulfillmentInventoryVersion(str, enum.Enum):
    V_2021_01_06 = "2021-01-06"
    V_2024_09_11 = "2024-09-11"
    LATEST = "2024-09-11"


if TYPE_CHECKING:

    class _ExternalFulfillmentInventoryMeta(VersionedClientMeta):
        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[
                ExternalFulfillmentInventoryVersion.V_2024_09_11,
                ExternalFulfillmentInventoryVersion.LATEST,
                "2024-09-11",
            ],
            **kwargs: Any,
        ) -> ExternalFulfillmentInventoryV20240911: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[
                ExternalFulfillmentInventoryVersion.V_2021_01_06, "2021-01-06"
            ],
            **kwargs: Any,
        ) -> ExternalFulfillmentInventoryV20210106: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> ExternalFulfillmentInventoryV20210106: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: str | ExternalFulfillmentInventoryVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...


else:
    _ExternalFulfillmentInventoryMeta = VersionedClientMeta


class ExternalFulfillmentInventory(
    AsyncBaseClient, metaclass=_ExternalFulfillmentInventoryMeta
):
    """External Fulfillment Inventory API client.

    This class dispatches to a versioned External Fulfillment Inventory API client.

    If you do not pass a version, the constructor returns the oldest supported implementation ("2021-01-06").
    """

    if TYPE_CHECKING:
        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[
                ExternalFulfillmentInventoryVersion.V_2024_09_11,
                ExternalFulfillmentInventoryVersion.LATEST,
                "2024-09-11",
            ],
            **kwargs: Any,
        ) -> ExternalFulfillmentInventoryV20240911: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[
                ExternalFulfillmentInventoryVersion.V_2021_01_06, "2021-01-06"
            ],
            **kwargs: Any,
        ) -> ExternalFulfillmentInventoryV20210106: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> ExternalFulfillmentInventoryV20210106: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: str | ExternalFulfillmentInventoryVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...

    _DISPATCH = True

    _DEFAULT_VERSION = "2021-01-06"

    _VERSION_MAP = {
        "2021-01-06": ExternalFulfillmentInventoryV20210106,
        "2024-09-11": ExternalFulfillmentInventoryV20240911,
    }

    _VERSION_ALIASES = {
        "2021-01-06": "2021-01-06",
        "2024-09-11": "2024-09-11",
    }
