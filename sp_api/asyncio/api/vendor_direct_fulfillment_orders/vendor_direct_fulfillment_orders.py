from __future__ import annotations

import enum
from typing import Any, Literal, TYPE_CHECKING, overload

from sp_api.asyncio.base import AsyncBaseClient
from sp_api.util.versioned_client import VersionedClientMeta

from .vendor_direct_fulfillment_orders_2021_12_28 import (
    VendorDirectFulfillmentOrdersV20211228,
)
from .vendor_direct_fulfillment_orders_v1 import VendorDirectFulfillmentOrdersV1


class VendorDirectFulfillmentOrdersVersion(str, enum.Enum):
    V1 = "v1"
    V_2021_12_28 = "2021-12-28"
    LATEST = "2021-12-28"


if TYPE_CHECKING:

    class _VendorDirectFulfillmentOrdersMeta(VersionedClientMeta):
        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[
                VendorDirectFulfillmentOrdersVersion.V_2021_12_28,
                VendorDirectFulfillmentOrdersVersion.LATEST,
                "2021-12-28",
            ],
            **kwargs: Any,
        ) -> VendorDirectFulfillmentOrdersV20211228: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[VendorDirectFulfillmentOrdersVersion.V1, "v1"],
            **kwargs: Any,
        ) -> VendorDirectFulfillmentOrdersV1: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> VendorDirectFulfillmentOrdersV1: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: str | VendorDirectFulfillmentOrdersVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...


else:
    _VendorDirectFulfillmentOrdersMeta = VersionedClientMeta


class VendorDirectFulfillmentOrders(
    AsyncBaseClient, metaclass=_VendorDirectFulfillmentOrdersMeta
):
    """Vendor Direct Fulfillment Orders API client.

    This class dispatches to a versioned Vendor Direct Fulfillment Orders API client.

    If you do not pass a version, the constructor returns the oldest supported implementation ("v1").
    """

    if TYPE_CHECKING:
        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[
                VendorDirectFulfillmentOrdersVersion.V_2021_12_28,
                VendorDirectFulfillmentOrdersVersion.LATEST,
                "2021-12-28",
            ],
            **kwargs: Any,
        ) -> VendorDirectFulfillmentOrdersV20211228: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[VendorDirectFulfillmentOrdersVersion.V1, "v1"],
            **kwargs: Any,
        ) -> VendorDirectFulfillmentOrdersV1: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> VendorDirectFulfillmentOrdersV1: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: str | VendorDirectFulfillmentOrdersVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...

    _DISPATCH = True

    _DEFAULT_VERSION = "v1"

    _VERSION_MAP = {
        "v1": VendorDirectFulfillmentOrdersV1,
        "2021-12-28": VendorDirectFulfillmentOrdersV20211228,
    }

    _VERSION_ALIASES = {
        "v1": "v1",
        "2021-12-28": "2021-12-28",
    }
