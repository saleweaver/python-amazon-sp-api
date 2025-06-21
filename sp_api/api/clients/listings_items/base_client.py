from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .listings_items_v_2020_09_01 import ListingsItems_V_2020_09_01
from .listings_items_v_2021_08_01 import ListingsItems_V_2021_08_01


class ListingsItemsVersion(Enum):
    V_2020_09_01 = "2020-09-01"
    V_2021_08_01 = "2021-08-01"


class ListingsItems(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> ListingsItems_V_2020_09_01: ...
    @overload
    def __new__(
        cls, version: ListingsItemsVersion.V_2020_09_01, *args, **kwargs
    ) -> ListingsItems_V_2020_09_01: ...
    @overload
    def __new__(
        cls, version: ListingsItemsVersion.V_2021_08_01, *args, **kwargs
    ) -> ListingsItems_V_2021_08_01: ...
    def __new__(
        cls,
        version: Union[ListingsItemsVersion, str] = ListingsItemsVersion.V_2021_08_01,
        *args,
        **kwargs,
    ):
        if not isinstance(version, ListingsItemsVersion):
            try:
                version = ListingsItemsVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == ListingsItemsVersion.V_2020_09_01:
            return ListingsItems_V_2020_09_01(*args, **kwargs)
        if version == ListingsItemsVersion.V_2021_08_01:
            return ListingsItems_V_2021_08_01(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
