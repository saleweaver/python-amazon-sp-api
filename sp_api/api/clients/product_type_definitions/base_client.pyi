from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .product_type_definitions_v_2020_09_01 import \
    ProductTypeDefinitions_V_2020_09_01

class ProductTypeDefinitionsVersion(Enum):
    V_2020_09_01: Literal["2020-09-01"]

class ProductTypeDefinitions(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> ProductTypeDefinitions_V_2020_09_01: ...
    # 2020-09-01 explicit overload
    @overload
    def __new__(
        cls,
        version: Literal[ProductTypeDefinitionsVersion.V_2020_09_01],
        *args,
        **kwargs,
    ) -> ProductTypeDefinitions_V_2020_09_01: ...
    # fallback stub
    def __new__(
        cls, version=..., *args, **kwargs
    ) -> ProductTypeDefinitions_V_2020_09_01: ...
