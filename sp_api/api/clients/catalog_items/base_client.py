from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .catalog_items_v_2020_12_01 import CatalogItems_V_2020_12_01
from .catalog_items_v_2022_04_01 import CatalogItems_V_2022_04_01
from .catalog_items_v_v0 import CatalogItems_V_v0


class CatalogItemsVersion(Enum):
    V_v0 = "v0"
    V_2020_12_01 = "2020-12-01"
    V_2022_04_01 = "2022-04-01"


class CatalogItems(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> CatalogItems_V_v0: ...
    @overload
    def __new__(
        cls, version: CatalogItemsVersion.V_v0, *args, **kwargs
    ) -> CatalogItems_V_v0: ...
    @overload
    def __new__(
        cls, version: CatalogItemsVersion.V_2020_12_01, *args, **kwargs
    ) -> CatalogItems_V_2020_12_01: ...
    @overload
    def __new__(
        cls, version: CatalogItemsVersion.V_2022_04_01, *args, **kwargs
    ) -> CatalogItems_V_2022_04_01: ...
    def __new__(
        cls,
        version: Union[CatalogItemsVersion, str] = CatalogItemsVersion.V_2022_04_01,
        *args,
        **kwargs,
    ):
        if not isinstance(version, CatalogItemsVersion):
            try:
                version = CatalogItemsVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == CatalogItemsVersion.V_v0:
            return CatalogItems_V_v0(*args, **kwargs)
        if version == CatalogItemsVersion.V_2020_12_01:
            return CatalogItems_V_2020_12_01(*args, **kwargs)
        if version == CatalogItemsVersion.V_2022_04_01:
            return CatalogItems_V_2022_04_01(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
