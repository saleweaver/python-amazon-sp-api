from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .orders_v_v0 import Orders_V_v0


class OrdersVersion(Enum):
    V_v0 = "v0"


class Orders(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> Orders_V_v0: ...
    @overload
    def __new__(cls, version: OrdersVersion.V_v0, *args, **kwargs) -> Orders_V_v0: ...
    def __new__(
        cls, version: Union[OrdersVersion, str] = OrdersVersion.V_v0, *args, **kwargs
    ):
        if not isinstance(version, OrdersVersion):
            try:
                version = OrdersVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == OrdersVersion.V_v0:
            return Orders_V_v0(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
