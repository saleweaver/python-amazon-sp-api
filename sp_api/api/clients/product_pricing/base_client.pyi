from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .product_pricing_v_2022_05_01 import ProductPricing_V_2022_05_01
from .product_pricing_v_v0 import ProductPricing_V_v0

class ProductPricingVersion(Enum):
    V_v0: Literal["v0"]
    V_2022_05_01: Literal["2022-05-01"]

class ProductPricing(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> ProductPricing_V_2022_05_01: ...
    # v0 explicit overload
    @overload
    def __new__(
        cls, version: Literal[ProductPricingVersion.V_v0], *args, **kwargs
    ) -> ProductPricing_V_v0: ...
    # 2022-05-01 explicit overload
    @overload
    def __new__(
        cls, version: Literal[ProductPricingVersion.V_2022_05_01], *args, **kwargs
    ) -> ProductPricing_V_2022_05_01: ...
    # fallback stub
    def __new__(
        cls, version=..., *args, **kwargs
    ) -> ProductPricing_V_v0 | ProductPricing_V_2022_05_01: ...
