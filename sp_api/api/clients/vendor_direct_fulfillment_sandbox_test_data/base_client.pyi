from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .vendor_direct_fulfillment_sandbox_test_data_v_2021_10_28 import \
    VendorDirectFulfillmentSandboxTestData_V_2021_10_28

class VendorDirectFulfillmentSandboxTestDataVersion(Enum):
    V_2021_10_28: Literal["2021-10-28"]

class VendorDirectFulfillmentSandboxTestData(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> VendorDirectFulfillmentSandboxTestData_V_2021_10_28: ...
    # 2021-10-28 explicit overload
    @overload
    def __new__(
        cls,
        version: Literal[VendorDirectFulfillmentSandboxTestDataVersion.V_2021_10_28],
        *args,
        **kwargs,
    ) -> VendorDirectFulfillmentSandboxTestData_V_2021_10_28: ...
    # fallback stub
    def __new__(
        cls, version=..., *args, **kwargs
    ) -> VendorDirectFulfillmentSandboxTestData_V_2021_10_28: ...
