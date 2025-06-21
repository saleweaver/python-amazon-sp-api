from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .vendor_direct_fulfillment_orders_v_2021_12_28 import \
    VendorDirectFulfillmentOrders_V_2021_12_28
from .vendor_direct_fulfillment_orders_v_v1 import \
    VendorDirectFulfillmentOrders_V_v1

class VendorDirectFulfillmentOrdersVersion(Enum):
    V_v1: Literal["v1"]
    V_2021_12_28: Literal["2021-12-28"]

class VendorDirectFulfillmentOrders(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> VendorDirectFulfillmentOrders_V_2021_12_28: ...
    # v1 explicit overload
    @overload
    def __new__(
        cls,
        version: Literal[VendorDirectFulfillmentOrdersVersion.V_v1],
        *args,
        **kwargs,
    ) -> VendorDirectFulfillmentOrders_V_v1: ...
    # 2021-12-28 explicit overload
    @overload
    def __new__(
        cls,
        version: Literal[VendorDirectFulfillmentOrdersVersion.V_2021_12_28],
        *args,
        **kwargs,
    ) -> VendorDirectFulfillmentOrders_V_2021_12_28: ...
    # fallback stub
    def __new__(
        cls, version=..., *args, **kwargs
    ) -> (
        VendorDirectFulfillmentOrders_V_v1 | VendorDirectFulfillmentOrders_V_2021_12_28
    ): ...
