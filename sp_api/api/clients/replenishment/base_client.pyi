from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .replenishment_v_2022_11_07 import Replenishment_V_2022_11_07

class ReplenishmentVersion(Enum):
    V_2022_11_07: Literal["2022-11-07"]

class Replenishment(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> Replenishment_V_2022_11_07: ...
    # 2022-11-07 explicit overload
    @overload
    def __new__(
        cls, version: Literal[ReplenishmentVersion.V_2022_11_07], *args, **kwargs
    ) -> Replenishment_V_2022_11_07: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> Replenishment_V_2022_11_07: ...
