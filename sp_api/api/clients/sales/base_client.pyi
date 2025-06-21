from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .sales_v_v1 import Sales_V_v1

class SalesVersion(Enum):
    V_v1: Literal["v1"]

class Sales(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> Sales_V_v1: ...
    # v1 explicit overload
    @overload
    def __new__(
        cls, version: Literal[SalesVersion.V_v1], *args, **kwargs
    ) -> Sales_V_v1: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> Sales_V_v1: ...
