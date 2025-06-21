from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .sales_v_v1 import Sales_V_v1


class SalesVersion(Enum):
    V_v1 = "v1"


class Sales(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> Sales_V_v1: ...
    @overload
    def __new__(cls, version: SalesVersion.V_v1, *args, **kwargs) -> Sales_V_v1: ...
    def __new__(
        cls, version: Union[SalesVersion, str] = SalesVersion.V_v1, *args, **kwargs
    ):
        if not isinstance(version, SalesVersion):
            try:
                version = SalesVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == SalesVersion.V_v1:
            return Sales_V_v1(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
