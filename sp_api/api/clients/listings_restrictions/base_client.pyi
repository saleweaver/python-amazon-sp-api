from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .listings_restrictions_v_2021_08_01 import \
    ListingsRestrictions_V_2021_08_01

class ListingsRestrictionsVersion(Enum):
    V_2021_08_01: Literal["2021-08-01"]

class ListingsRestrictions(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> ListingsRestrictions_V_2021_08_01: ...
    # 2021-08-01 explicit overload
    @overload
    def __new__(
        cls, version: Literal[ListingsRestrictionsVersion.V_2021_08_01], *args, **kwargs
    ) -> ListingsRestrictions_V_2021_08_01: ...
    # fallback stub
    def __new__(
        cls, version=..., *args, **kwargs
    ) -> ListingsRestrictions_V_2021_08_01: ...
