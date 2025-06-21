from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .shipping_v_v1 import Shipping_V_v1
from .shipping_v_v2 import Shipping_V_v2


class ShippingVersion(Enum):
    V_v1 = "v1"
    V_v2 = "v2"


class Shipping(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> Shipping_V_v1: ...
    @overload
    def __new__(
        cls, version: ShippingVersion.V_v1, *args, **kwargs
    ) -> Shipping_V_v1: ...
    @overload
    def __new__(
        cls, version: ShippingVersion.V_v2, *args, **kwargs
    ) -> Shipping_V_v2: ...
    def __new__(
        cls,
        version: Union[ShippingVersion, str] = ShippingVersion.V_v2,
        *args,
        **kwargs,
    ):
        if not isinstance(version, ShippingVersion):
            try:
                version = ShippingVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == ShippingVersion.V_v1:
            return Shipping_V_v1(*args, **kwargs)
        if version == ShippingVersion.V_v2:
            return Shipping_V_v2(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
