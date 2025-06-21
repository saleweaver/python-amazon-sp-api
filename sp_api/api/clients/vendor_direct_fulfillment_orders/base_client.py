from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .vendor_direct_fulfillment_orders_v_2021_12_28 import \
    VendorDirectFulfillmentOrders_V_2021_12_28
from .vendor_direct_fulfillment_orders_v_v1 import \
    VendorDirectFulfillmentOrders_V_v1


class VendorDirectFulfillmentOrdersVersion(Enum):
    V_v1 = "v1"
    V_2021_12_28 = "2021-12-28"


class VendorDirectFulfillmentOrders(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> VendorDirectFulfillmentOrders_V_v1: ...
    @overload
    def __new__(
        cls, version: VendorDirectFulfillmentOrdersVersion.V_v1, *args, **kwargs
    ) -> VendorDirectFulfillmentOrders_V_v1: ...
    @overload
    def __new__(
        cls, version: VendorDirectFulfillmentOrdersVersion.V_2021_12_28, *args, **kwargs
    ) -> VendorDirectFulfillmentOrders_V_2021_12_28: ...
    def __new__(
        cls,
        version: Union[
            VendorDirectFulfillmentOrdersVersion, str
        ] = VendorDirectFulfillmentOrdersVersion.V_2021_12_28,
        *args,
        **kwargs,
    ):
        if not isinstance(version, VendorDirectFulfillmentOrdersVersion):
            try:
                version = VendorDirectFulfillmentOrdersVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == VendorDirectFulfillmentOrdersVersion.V_v1:
            return VendorDirectFulfillmentOrders_V_v1(*args, **kwargs)
        if version == VendorDirectFulfillmentOrdersVersion.V_2021_12_28:
            return VendorDirectFulfillmentOrders_V_2021_12_28(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
