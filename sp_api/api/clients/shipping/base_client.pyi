from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .shipping_v_v1 import Shipping_V_v1
from .shipping_v_v2 import Shipping_V_v2

class ShippingVersion(Enum):
    V_v1: Literal["v1"]
    V_v2: Literal["v2"]

class Shipping(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> Shipping_V_v2: ...
    # v1 explicit overload
    @overload
    def __new__(
        cls, version: Literal[ShippingVersion.V_v1], *args, **kwargs
    ) -> Shipping_V_v1: ...
    # v2 explicit overload
    @overload
    def __new__(
        cls, version: Literal[ShippingVersion.V_v2], *args, **kwargs
    ) -> Shipping_V_v2: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> Shipping_V_v1 | Shipping_V_v2: ...
