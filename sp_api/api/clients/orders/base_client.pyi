from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .orders_v_v0 import Orders_V_v0

class OrdersVersion(Enum):
    V_v0: Literal["v0"]

class Orders(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> Orders_V_v0: ...
    # v0 explicit overload
    @overload
    def __new__(
        cls, version: Literal[OrdersVersion.V_v0], *args, **kwargs
    ) -> Orders_V_v0: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> Orders_V_v0: ...
