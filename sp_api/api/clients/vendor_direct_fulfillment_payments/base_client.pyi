from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .vendor_direct_fulfillment_payments_v_v1 import \
    VendorDirectFulfillmentPayments_V_v1

class VendorDirectFulfillmentPaymentsVersion(Enum):
    V_v1: Literal["v1"]

class VendorDirectFulfillmentPayments(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> VendorDirectFulfillmentPayments_V_v1: ...
    # v1 explicit overload
    @overload
    def __new__(
        cls,
        version: Literal[VendorDirectFulfillmentPaymentsVersion.V_v1],
        *args,
        **kwargs,
    ) -> VendorDirectFulfillmentPayments_V_v1: ...
    # fallback stub
    def __new__(
        cls, version=..., *args, **kwargs
    ) -> VendorDirectFulfillmentPayments_V_v1: ...
