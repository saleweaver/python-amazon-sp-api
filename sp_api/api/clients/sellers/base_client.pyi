from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .sellers_v_v1 import Sellers_V_v1

class SellersVersion(Enum):
    V_v1: Literal["v1"]

class Sellers(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> Sellers_V_v1: ...
    # v1 explicit overload
    @overload
    def __new__(
        cls, version: Literal[SellersVersion.V_v1], *args, **kwargs
    ) -> Sellers_V_v1: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> Sellers_V_v1: ...
