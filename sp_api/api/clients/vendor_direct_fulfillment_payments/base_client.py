from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .vendor_direct_fulfillment_payments_v_v1 import \
    VendorDirectFulfillmentPayments_V_v1


class VendorDirectFulfillmentPaymentsVersion(Enum):
    V_v1 = "v1"


class VendorDirectFulfillmentPayments(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> VendorDirectFulfillmentPayments_V_v1: ...
    @overload
    def __new__(
        cls, version: VendorDirectFulfillmentPaymentsVersion.V_v1, *args, **kwargs
    ) -> VendorDirectFulfillmentPayments_V_v1: ...
    def __new__(
        cls,
        version: Union[
            VendorDirectFulfillmentPaymentsVersion, str
        ] = VendorDirectFulfillmentPaymentsVersion.V_v1,
        *args,
        **kwargs,
    ):
        if not isinstance(version, VendorDirectFulfillmentPaymentsVersion):
            try:
                version = VendorDirectFulfillmentPaymentsVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == VendorDirectFulfillmentPaymentsVersion.V_v1:
            return VendorDirectFulfillmentPayments_V_v1(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
