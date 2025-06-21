from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .vehicles_v_2024_11_01 import Vehicles_V_2024_11_01


class VehiclesVersion(Enum):
    V_2024_11_01 = "2024-11-01"


class Vehicles(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> Vehicles_V_2024_11_01: ...
    @overload
    def __new__(
        cls, version: VehiclesVersion.V_2024_11_01, *args, **kwargs
    ) -> Vehicles_V_2024_11_01: ...
    def __new__(
        cls,
        version: Union[VehiclesVersion, str] = VehiclesVersion.V_2024_11_01,
        *args,
        **kwargs,
    ):
        if not isinstance(version, VehiclesVersion):
            try:
                version = VehiclesVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == VehiclesVersion.V_2024_11_01:
            return Vehicles_V_2024_11_01(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
