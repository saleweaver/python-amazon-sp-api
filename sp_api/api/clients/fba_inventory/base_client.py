from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .fba_inventory_v_v1 import FbaInventory_V_v1


class FbaInventoryVersion(Enum):
    V_v1 = "v1"


class FbaInventory(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> FbaInventory_V_v1: ...
    @overload
    def __new__(
        cls, version: FbaInventoryVersion.V_v1, *args, **kwargs
    ) -> FbaInventory_V_v1: ...
    def __new__(
        cls,
        version: Union[FbaInventoryVersion, str] = FbaInventoryVersion.V_v1,
        *args,
        **kwargs,
    ):
        if not isinstance(version, FbaInventoryVersion):
            try:
                version = FbaInventoryVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == FbaInventoryVersion.V_v1:
            return FbaInventory_V_v1(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
