from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .vendor_direct_fulfillment_inventory_v_v1 import \
    VendorDirectFulfillmentInventory_V_v1

class VendorDirectFulfillmentInventoryVersion(Enum):
    V_v1: Literal["v1"]

class VendorDirectFulfillmentInventory(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> VendorDirectFulfillmentInventory_V_v1: ...
    # v1 explicit overload
    @overload
    def __new__(
        cls,
        version: Literal[VendorDirectFulfillmentInventoryVersion.V_v1],
        *args,
        **kwargs,
    ) -> VendorDirectFulfillmentInventory_V_v1: ...
    # fallback stub
    def __new__(
        cls, version=..., *args, **kwargs
    ) -> VendorDirectFulfillmentInventory_V_v1: ...
