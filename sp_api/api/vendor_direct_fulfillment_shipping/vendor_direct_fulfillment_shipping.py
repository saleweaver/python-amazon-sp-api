from __future__ import annotations

import enum
from typing import Any, Literal, TYPE_CHECKING, overload
from sp_api.util.versioned_client import VersionedClientMeta

from sp_api.base import Client

from .vendor_direct_fulfillment_shipping_2021_12_28 import (
    VendorDirectFulfillmentShippingV20211228,
)
from .vendor_direct_fulfillment_shipping_v1 import VendorDirectFulfillmentShippingV1


class VendorDirectFulfillmentShippingVersion(str, enum.Enum):
    V1 = "v1"
    V_2021_12_28 = "2021-12-28"
    LATEST = "2021-12-28"


if TYPE_CHECKING:

    class _VendorDirectFulfillmentShippingMeta(VersionedClientMeta):
        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[
                VendorDirectFulfillmentShippingVersion.V_2021_12_28,
                VendorDirectFulfillmentShippingVersion.LATEST,
                "2021-12-28",
            ],
            **kwargs: Any,
        ) -> VendorDirectFulfillmentShippingV20211228: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[VendorDirectFulfillmentShippingVersion.V1, "v1"],
            **kwargs: Any,
        ) -> VendorDirectFulfillmentShippingV1: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> VendorDirectFulfillmentShippingV1: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: str | VendorDirectFulfillmentShippingVersion,
            **kwargs: Any,
        ) -> Client: ...


else:
    _VendorDirectFulfillmentShippingMeta = VersionedClientMeta


class VendorDirectFulfillmentShipping(
    Client, metaclass=_VendorDirectFulfillmentShippingMeta
):
    """Vendor Direct Fulfillment Shipping API client.

    This class dispatches to a versioned Vendor Direct Fulfillment Shipping API client.

    If you do not pass a version, the constructor returns the oldest supported implementation ("v1").
    """

    if TYPE_CHECKING:
        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[
                VendorDirectFulfillmentShippingVersion.V_2021_12_28,
                VendorDirectFulfillmentShippingVersion.LATEST,
                "2021-12-28",
            ],
            **kwargs: Any,
        ) -> VendorDirectFulfillmentShippingV20211228: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[VendorDirectFulfillmentShippingVersion.V1, "v1"],
            **kwargs: Any,
        ) -> VendorDirectFulfillmentShippingV1: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> VendorDirectFulfillmentShippingV1: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: str | VendorDirectFulfillmentShippingVersion,
            **kwargs: Any,
        ) -> Client: ...

    _DISPATCH = True

    _DEFAULT_VERSION = "v1"

    _VERSION_MAP = {
        "v1": VendorDirectFulfillmentShippingV1,
        "2021-12-28": VendorDirectFulfillmentShippingV20211228,
    }

    _VERSION_ALIASES = {
        "v1": "v1",
        "2021-12-28": "2021-12-28",
    }
