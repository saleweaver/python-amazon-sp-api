from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .vendor_orders_v_v1 import VendorOrders_V_v1

class VendorOrdersVersion(Enum):
    V_v1: Literal["v1"]

class VendorOrders(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> VendorOrders_V_v1: ...
    # v1 explicit overload
    @overload
    def __new__(
        cls, version: Literal[VendorOrdersVersion.V_v1], *args, **kwargs
    ) -> VendorOrders_V_v1: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> VendorOrders_V_v1: ...
