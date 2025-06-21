from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .vendor_direct_fulfillment_sandbox_test_data_v_2021_10_28 import \
    VendorDirectFulfillmentSandboxTestData_V_2021_10_28


class VendorDirectFulfillmentSandboxTestDataVersion(Enum):
    V_2021_10_28 = "2021-10-28"


class VendorDirectFulfillmentSandboxTestData(Client):
    @overload
    def __new__(
        cls, *args, **kwargs
    ) -> VendorDirectFulfillmentSandboxTestData_V_2021_10_28: ...
    @overload
    def __new__(
        cls,
        version: VendorDirectFulfillmentSandboxTestDataVersion.V_2021_10_28,
        *args,
        **kwargs,
    ) -> VendorDirectFulfillmentSandboxTestData_V_2021_10_28: ...
    def __new__(
        cls,
        version: Union[
            VendorDirectFulfillmentSandboxTestDataVersion, str
        ] = VendorDirectFulfillmentSandboxTestDataVersion.V_2021_10_28,
        *args,
        **kwargs,
    ):
        if not isinstance(version, VendorDirectFulfillmentSandboxTestDataVersion):
            try:
                version = VendorDirectFulfillmentSandboxTestDataVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == VendorDirectFulfillmentSandboxTestDataVersion.V_2021_10_28:
            return VendorDirectFulfillmentSandboxTestData_V_2021_10_28(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
