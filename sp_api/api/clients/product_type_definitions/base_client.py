from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .product_type_definitions_v_2020_09_01 import \
    ProductTypeDefinitions_V_2020_09_01


class ProductTypeDefinitionsVersion(Enum):
    V_2020_09_01 = "2020-09-01"


class ProductTypeDefinitions(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> ProductTypeDefinitions_V_2020_09_01: ...
    @overload
    def __new__(
        cls, version: ProductTypeDefinitionsVersion.V_2020_09_01, *args, **kwargs
    ) -> ProductTypeDefinitions_V_2020_09_01: ...
    def __new__(
        cls,
        version: Union[
            ProductTypeDefinitionsVersion, str
        ] = ProductTypeDefinitionsVersion.V_2020_09_01,
        *args,
        **kwargs,
    ):
        if not isinstance(version, ProductTypeDefinitionsVersion):
            try:
                version = ProductTypeDefinitionsVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == ProductTypeDefinitionsVersion.V_2020_09_01:
            return ProductTypeDefinitions_V_2020_09_01(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
