from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .merchant_fulfillment_v_v0 import MerchantFulfillment_V_v0

class MerchantFulfillmentVersion(Enum):
    V_v0: Literal["v0"]

class MerchantFulfillment(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> MerchantFulfillment_V_v0: ...
    # v0 explicit overload
    @overload
    def __new__(
        cls, version: Literal[MerchantFulfillmentVersion.V_v0], *args, **kwargs
    ) -> MerchantFulfillment_V_v0: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> MerchantFulfillment_V_v0: ...
