from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .vendor_invoices_v_v1 import VendorInvoices_V_v1

class VendorInvoicesVersion(Enum):
    V_v1: Literal["v1"]

class VendorInvoices(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> VendorInvoices_V_v1: ...
    # v1 explicit overload
    @overload
    def __new__(
        cls, version: Literal[VendorInvoicesVersion.V_v1], *args, **kwargs
    ) -> VendorInvoices_V_v1: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> VendorInvoices_V_v1: ...
