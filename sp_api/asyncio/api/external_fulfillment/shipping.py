from __future__ import annotations

import enum
from typing import Any, Literal, TYPE_CHECKING, overload

from sp_api.asyncio.base import AsyncBaseClient
from sp_api.util.versioned_client import VersionedClientMeta

from .shipping_2021_01_06 import ExternalFulfillmentShippingV20210106
from .shipping_2024_09_11 import ExternalFulfillmentShippingV20240911


class ExternalFulfillmentShippingVersion(str, enum.Enum):
    V_2021_01_06 = "2021-01-06"
    V_2024_09_11 = "2024-09-11"
    LATEST = "2024-09-11"


if TYPE_CHECKING:

    class _ExternalFulfillmentShippingMeta(VersionedClientMeta):
        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[
                ExternalFulfillmentShippingVersion.V_2024_09_11,
                ExternalFulfillmentShippingVersion.LATEST,
                "2024-09-11",
            ],
            **kwargs: Any,
        ) -> ExternalFulfillmentShippingV20240911: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[
                ExternalFulfillmentShippingVersion.V_2021_01_06, "2021-01-06"
            ],
            **kwargs: Any,
        ) -> ExternalFulfillmentShippingV20210106: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> ExternalFulfillmentShippingV20210106: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: str | ExternalFulfillmentShippingVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...


else:
    _ExternalFulfillmentShippingMeta = VersionedClientMeta


class ExternalFulfillmentShipping(AsyncBaseClient, metaclass=_ExternalFulfillmentShippingMeta):
    """External Fulfillment Shipping API client.

    This class dispatches to a versioned External Fulfillment Shipping API client.

    If you do not pass a version, the constructor returns the oldest supported implementation ("2021-01-06").
    """

    if TYPE_CHECKING:
        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[
                ExternalFulfillmentShippingVersion.V_2024_09_11,
                ExternalFulfillmentShippingVersion.LATEST,
                "2024-09-11",
            ],
            **kwargs: Any,
        ) -> ExternalFulfillmentShippingV20240911: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[
                ExternalFulfillmentShippingVersion.V_2021_01_06, "2021-01-06"
            ],
            **kwargs: Any,
        ) -> ExternalFulfillmentShippingV20210106: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> ExternalFulfillmentShippingV20210106: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: str | ExternalFulfillmentShippingVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...

    _DISPATCH = True

    _DEFAULT_VERSION = "2021-01-06"

    _VERSION_MAP = {
        "2021-01-06": ExternalFulfillmentShippingV20210106,
        "2024-09-11": ExternalFulfillmentShippingV20240911,
    }

    _VERSION_ALIASES = {
        "2021-01-06": "2021-01-06",
        "2024-09-11": "2024-09-11",
    }
