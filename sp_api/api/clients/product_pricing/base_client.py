from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .product_pricing_v_2022_05_01 import ProductPricing_V_2022_05_01
from .product_pricing_v_v0 import ProductPricing_V_v0


class ProductPricingVersion(Enum):
    V_v0 = "v0"
    V_2022_05_01 = "2022-05-01"


class ProductPricing(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> ProductPricing_V_v0: ...
    @overload
    def __new__(
        cls, version: ProductPricingVersion.V_v0, *args, **kwargs
    ) -> ProductPricing_V_v0: ...
    @overload
    def __new__(
        cls, version: ProductPricingVersion.V_2022_05_01, *args, **kwargs
    ) -> ProductPricing_V_2022_05_01: ...
    def __new__(
        cls,
        version: Union[ProductPricingVersion, str] = ProductPricingVersion.V_2022_05_01,
        *args,
        **kwargs,
    ):
        if not isinstance(version, ProductPricingVersion):
            try:
                version = ProductPricingVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == ProductPricingVersion.V_v0:
            return ProductPricing_V_v0(*args, **kwargs)
        if version == ProductPricingVersion.V_2022_05_01:
            return ProductPricing_V_2022_05_01(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
