from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .listings_items_v_2020_09_01 import ListingsItems_V_2020_09_01
from .listings_items_v_2021_08_01 import ListingsItems_V_2021_08_01

class ListingsItemsVersion(Enum):
    V_2020_09_01: Literal["2020-09-01"]
    V_2021_08_01: Literal["2021-08-01"]

class ListingsItems(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> ListingsItems_V_2021_08_01: ...
    # 2020-09-01 explicit overload
    @overload
    def __new__(
        cls, version: Literal[ListingsItemsVersion.V_2020_09_01], *args, **kwargs
    ) -> ListingsItems_V_2020_09_01: ...
    # 2021-08-01 explicit overload
    @overload
    def __new__(
        cls, version: Literal[ListingsItemsVersion.V_2021_08_01], *args, **kwargs
    ) -> ListingsItems_V_2021_08_01: ...
    # fallback stub
    def __new__(
        cls, version=..., *args, **kwargs
    ) -> ListingsItems_V_2020_09_01 | ListingsItems_V_2021_08_01: ...
