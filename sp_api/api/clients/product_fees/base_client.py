from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .product_fees_v_v0 import ProductFees_V_v0


class ProductFeesVersion(Enum):
    V_v0 = "v0"


class ProductFees(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> ProductFees_V_v0: ...
    @overload
    def __new__(
        cls, version: ProductFeesVersion.V_v0, *args, **kwargs
    ) -> ProductFees_V_v0: ...
    def __new__(
        cls,
        version: Union[ProductFeesVersion, str] = ProductFeesVersion.V_v0,
        *args,
        **kwargs,
    ):
        if not isinstance(version, ProductFeesVersion):
            try:
                version = ProductFeesVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == ProductFeesVersion.V_v0:
            return ProductFees_V_v0(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
