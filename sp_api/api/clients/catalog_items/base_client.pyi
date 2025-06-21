from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .catalog_items_v_2020_12_01 import CatalogItems_V_2020_12_01
from .catalog_items_v_2022_04_01 import CatalogItems_V_2022_04_01
from .catalog_items_v_v0 import CatalogItems_V_v0

class CatalogItemsVersion(Enum):
    V_v0: Literal["v0"]
    V_2020_12_01: Literal["2020-12-01"]
    V_2022_04_01: Literal["2022-04-01"]

class CatalogItems(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> CatalogItems_V_2022_04_01: ...
    # v0 explicit overload
    @overload
    def __new__(
        cls, version: Literal[CatalogItemsVersion.V_v0], *args, **kwargs
    ) -> CatalogItems_V_v0: ...
    # 2020-12-01 explicit overload
    @overload
    def __new__(
        cls, version: Literal[CatalogItemsVersion.V_2020_12_01], *args, **kwargs
    ) -> CatalogItems_V_2020_12_01: ...
    # 2022-04-01 explicit overload
    @overload
    def __new__(
        cls, version: Literal[CatalogItemsVersion.V_2022_04_01], *args, **kwargs
    ) -> CatalogItems_V_2022_04_01: ...
    # fallback stub
    def __new__(
        cls, version=..., *args, **kwargs
    ) -> CatalogItems_V_v0 | CatalogItems_V_2020_12_01 | CatalogItems_V_2022_04_01: ...
