from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .shipment_invoicing_v_v0 import ShipmentInvoicing_V_v0

class ShipmentInvoicingVersion(Enum):
    V_v0: Literal["v0"]

class ShipmentInvoicing(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> ShipmentInvoicing_V_v0: ...
    # v0 explicit overload
    @overload
    def __new__(
        cls, version: Literal[ShipmentInvoicingVersion.V_v0], *args, **kwargs
    ) -> ShipmentInvoicing_V_v0: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> ShipmentInvoicing_V_v0: ...
