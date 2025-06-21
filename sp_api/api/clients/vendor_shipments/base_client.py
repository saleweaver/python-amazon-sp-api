from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .vendor_shipments_v_v1 import VendorShipments_V_v1


class VendorShipmentsVersion(Enum):
    V_v1 = "v1"


class VendorShipments(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> VendorShipments_V_v1: ...
    @overload
    def __new__(
        cls, version: VendorShipmentsVersion.V_v1, *args, **kwargs
    ) -> VendorShipments_V_v1: ...
    def __new__(
        cls,
        version: Union[VendorShipmentsVersion, str] = VendorShipmentsVersion.V_v1,
        *args,
        **kwargs,
    ):
        if not isinstance(version, VendorShipmentsVersion):
            try:
                version = VendorShipmentsVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == VendorShipmentsVersion.V_v1:
            return VendorShipments_V_v1(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
