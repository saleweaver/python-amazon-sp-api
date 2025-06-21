from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .supply_sources_v_2020_07_01 import SupplySources_V_2020_07_01

class SupplySourcesVersion(Enum):
    V_2020_07_01: Literal["2020-07-01"]

class SupplySources(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> SupplySources_V_2020_07_01: ...
    # 2020-07-01 explicit overload
    @overload
    def __new__(
        cls, version: Literal[SupplySourcesVersion.V_2020_07_01], *args, **kwargs
    ) -> SupplySources_V_2020_07_01: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> SupplySources_V_2020_07_01: ...
