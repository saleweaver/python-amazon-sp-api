from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .easy_ship_v_2022_03_23 import EasyShip_V_2022_03_23


class EasyShipVersion(Enum):
    V_2022_03_23 = "2022-03-23"


class EasyShip(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> EasyShip_V_2022_03_23: ...
    @overload
    def __new__(
        cls, version: EasyShipVersion.V_2022_03_23, *args, **kwargs
    ) -> EasyShip_V_2022_03_23: ...
    def __new__(
        cls,
        version: Union[EasyShipVersion, str] = EasyShipVersion.V_2022_03_23,
        *args,
        **kwargs,
    ):
        if not isinstance(version, EasyShipVersion):
            try:
                version = EasyShipVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == EasyShipVersion.V_2022_03_23:
            return EasyShip_V_2022_03_23(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
