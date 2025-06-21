from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .vendor_direct_fulfillment_shipping_v_2021_12_28 import \
    VendorDirectFulfillmentShipping_V_2021_12_28
from .vendor_direct_fulfillment_shipping_v_v1 import \
    VendorDirectFulfillmentShipping_V_v1

class VendorDirectFulfillmentShippingVersion(Enum):
    V_v1: Literal["v1"]
    V_2021_12_28: Literal["2021-12-28"]

class VendorDirectFulfillmentShipping(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> VendorDirectFulfillmentShipping_V_2021_12_28: ...
    # v1 explicit overload
    @overload
    def __new__(
        cls,
        version: Literal[VendorDirectFulfillmentShippingVersion.V_v1],
        *args,
        **kwargs,
    ) -> VendorDirectFulfillmentShipping_V_v1: ...
    # 2021-12-28 explicit overload
    @overload
    def __new__(
        cls,
        version: Literal[VendorDirectFulfillmentShippingVersion.V_2021_12_28],
        *args,
        **kwargs,
    ) -> VendorDirectFulfillmentShipping_V_2021_12_28: ...
    # fallback stub
    def __new__(
        cls, version=..., *args, **kwargs
    ) -> (
        VendorDirectFulfillmentShipping_V_v1
        | VendorDirectFulfillmentShipping_V_2021_12_28
    ): ...
