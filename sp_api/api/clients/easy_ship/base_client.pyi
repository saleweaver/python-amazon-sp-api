from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .easy_ship_v_2022_03_23 import EasyShip_V_2022_03_23

class EasyShipVersion(Enum):
    V_2022_03_23: Literal["2022-03-23"]

class EasyShip(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> EasyShip_V_2022_03_23: ...
    # 2022-03-23 explicit overload
    @overload
    def __new__(
        cls, version: Literal[EasyShipVersion.V_2022_03_23], *args, **kwargs
    ) -> EasyShip_V_2022_03_23: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> EasyShip_V_2022_03_23: ...
