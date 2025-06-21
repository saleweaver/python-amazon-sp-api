from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .replenishment_v_2022_11_07 import Replenishment_V_2022_11_07


class ReplenishmentVersion(Enum):
    V_2022_11_07 = "2022-11-07"


class Replenishment(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> Replenishment_V_2022_11_07: ...
    @overload
    def __new__(
        cls, version: ReplenishmentVersion.V_2022_11_07, *args, **kwargs
    ) -> Replenishment_V_2022_11_07: ...
    def __new__(
        cls,
        version: Union[ReplenishmentVersion, str] = ReplenishmentVersion.V_2022_11_07,
        *args,
        **kwargs,
    ):
        if not isinstance(version, ReplenishmentVersion):
            try:
                version = ReplenishmentVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == ReplenishmentVersion.V_2022_11_07:
            return Replenishment_V_2022_11_07(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
