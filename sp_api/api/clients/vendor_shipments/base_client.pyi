from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .vendor_shipments_v_v1 import VendorShipments_V_v1

class VendorShipmentsVersion(Enum):
    V_v1: Literal["v1"]

class VendorShipments(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> VendorShipments_V_v1: ...
    # v1 explicit overload
    @overload
    def __new__(
        cls, version: Literal[VendorShipmentsVersion.V_v1], *args, **kwargs
    ) -> VendorShipments_V_v1: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> VendorShipments_V_v1: ...
