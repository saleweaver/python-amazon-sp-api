from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .shipment_invoicing_v_v0 import ShipmentInvoicing_V_v0


class ShipmentInvoicingVersion(Enum):
    V_v0 = "v0"


class ShipmentInvoicing(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> ShipmentInvoicing_V_v0: ...
    @overload
    def __new__(
        cls, version: ShipmentInvoicingVersion.V_v0, *args, **kwargs
    ) -> ShipmentInvoicing_V_v0: ...
    def __new__(
        cls,
        version: Union[ShipmentInvoicingVersion, str] = ShipmentInvoicingVersion.V_v0,
        *args,
        **kwargs,
    ):
        if not isinstance(version, ShipmentInvoicingVersion):
            try:
                version = ShipmentInvoicingVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == ShipmentInvoicingVersion.V_v0:
            return ShipmentInvoicing_V_v0(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
