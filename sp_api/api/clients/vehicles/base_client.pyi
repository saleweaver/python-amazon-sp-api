from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .vehicles_v_2024_11_01 import Vehicles_V_2024_11_01

class VehiclesVersion(Enum):
    V_2024_11_01: Literal["2024-11-01"]

class Vehicles(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> Vehicles_V_2024_11_01: ...
    # 2024-11-01 explicit overload
    @overload
    def __new__(
        cls, version: Literal[VehiclesVersion.V_2024_11_01], *args, **kwargs
    ) -> Vehicles_V_2024_11_01: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> Vehicles_V_2024_11_01: ...
