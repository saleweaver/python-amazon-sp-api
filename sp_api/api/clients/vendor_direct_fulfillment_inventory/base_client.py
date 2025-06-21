from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .vendor_direct_fulfillment_inventory_v_v1 import \
    VendorDirectFulfillmentInventory_V_v1


class VendorDirectFulfillmentInventoryVersion(Enum):
    V_v1 = "v1"


class VendorDirectFulfillmentInventory(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> VendorDirectFulfillmentInventory_V_v1: ...
    @overload
    def __new__(
        cls, version: VendorDirectFulfillmentInventoryVersion.V_v1, *args, **kwargs
    ) -> VendorDirectFulfillmentInventory_V_v1: ...
    def __new__(
        cls,
        version: Union[
            VendorDirectFulfillmentInventoryVersion, str
        ] = VendorDirectFulfillmentInventoryVersion.V_v1,
        *args,
        **kwargs,
    ):
        if not isinstance(version, VendorDirectFulfillmentInventoryVersion):
            try:
                version = VendorDirectFulfillmentInventoryVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == VendorDirectFulfillmentInventoryVersion.V_v1:
            return VendorDirectFulfillmentInventory_V_v1(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
