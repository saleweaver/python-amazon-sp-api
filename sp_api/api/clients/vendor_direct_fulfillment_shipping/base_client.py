from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .vendor_direct_fulfillment_shipping_v_2021_12_28 import \
    VendorDirectFulfillmentShipping_V_2021_12_28
from .vendor_direct_fulfillment_shipping_v_v1 import \
    VendorDirectFulfillmentShipping_V_v1


class VendorDirectFulfillmentShippingVersion(Enum):
    V_v1 = "v1"
    V_2021_12_28 = "2021-12-28"


class VendorDirectFulfillmentShipping(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> VendorDirectFulfillmentShipping_V_v1: ...
    @overload
    def __new__(
        cls, version: VendorDirectFulfillmentShippingVersion.V_v1, *args, **kwargs
    ) -> VendorDirectFulfillmentShipping_V_v1: ...
    @overload
    def __new__(
        cls,
        version: VendorDirectFulfillmentShippingVersion.V_2021_12_28,
        *args,
        **kwargs,
    ) -> VendorDirectFulfillmentShipping_V_2021_12_28: ...
    def __new__(
        cls,
        version: Union[
            VendorDirectFulfillmentShippingVersion, str
        ] = VendorDirectFulfillmentShippingVersion.V_2021_12_28,
        *args,
        **kwargs,
    ):
        if not isinstance(version, VendorDirectFulfillmentShippingVersion):
            try:
                version = VendorDirectFulfillmentShippingVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == VendorDirectFulfillmentShippingVersion.V_v1:
            return VendorDirectFulfillmentShipping_V_v1(*args, **kwargs)
        if version == VendorDirectFulfillmentShippingVersion.V_2021_12_28:
            return VendorDirectFulfillmentShipping_V_2021_12_28(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
