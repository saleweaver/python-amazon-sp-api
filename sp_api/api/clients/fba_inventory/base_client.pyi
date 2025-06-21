from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .fba_inventory_v_v1 import FbaInventory_V_v1

class FbaInventoryVersion(Enum):
    V_v1: Literal["v1"]

class FbaInventory(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> FbaInventory_V_v1: ...
    # v1 explicit overload
    @overload
    def __new__(
        cls, version: Literal[FbaInventoryVersion.V_v1], *args, **kwargs
    ) -> FbaInventory_V_v1: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> FbaInventory_V_v1: ...
