from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .product_fees_v_v0 import ProductFees_V_v0

class ProductFeesVersion(Enum):
    V_v0: Literal["v0"]

class ProductFees(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> ProductFees_V_v0: ...
    # v0 explicit overload
    @overload
    def __new__(
        cls, version: Literal[ProductFeesVersion.V_v0], *args, **kwargs
    ) -> ProductFees_V_v0: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> ProductFees_V_v0: ...
