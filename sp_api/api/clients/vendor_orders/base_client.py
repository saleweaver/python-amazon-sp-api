from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .vendor_orders_v_v1 import VendorOrders_V_v1


class VendorOrdersVersion(Enum):
    V_v1 = "v1"


class VendorOrders(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> VendorOrders_V_v1: ...
    @overload
    def __new__(
        cls, version: VendorOrdersVersion.V_v1, *args, **kwargs
    ) -> VendorOrders_V_v1: ...
    def __new__(
        cls,
        version: Union[VendorOrdersVersion, str] = VendorOrdersVersion.V_v1,
        *args,
        **kwargs,
    ):
        if not isinstance(version, VendorOrdersVersion):
            try:
                version = VendorOrdersVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == VendorOrdersVersion.V_v1:
            return VendorOrders_V_v1(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
