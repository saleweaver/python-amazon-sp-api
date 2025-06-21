from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .sellers_v_v1 import Sellers_V_v1


class SellersVersion(Enum):
    V_v1 = "v1"


class Sellers(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> Sellers_V_v1: ...
    @overload
    def __new__(cls, version: SellersVersion.V_v1, *args, **kwargs) -> Sellers_V_v1: ...
    def __new__(
        cls, version: Union[SellersVersion, str] = SellersVersion.V_v1, *args, **kwargs
    ):
        if not isinstance(version, SellersVersion):
            try:
                version = SellersVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == SellersVersion.V_v1:
            return Sellers_V_v1(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
