from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .vendor_transaction_status_v_v1 import VendorTransactionStatus_V_v1

class VendorTransactionStatusVersion(Enum):
    V_v1: Literal["v1"]

class VendorTransactionStatus(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> VendorTransactionStatus_V_v1: ...
    # v1 explicit overload
    @overload
    def __new__(
        cls, version: Literal[VendorTransactionStatusVersion.V_v1], *args, **kwargs
    ) -> VendorTransactionStatus_V_v1: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> VendorTransactionStatus_V_v1: ...
