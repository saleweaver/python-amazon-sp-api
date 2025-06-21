from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .aplus_content_v_2020_11_01 import AplusContent_V_2020_11_01


class AplusContentVersion(Enum):
    V_2020_11_01 = "2020-11-01"


class AplusContent(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> AplusContent_V_2020_11_01: ...
    @overload
    def __new__(
        cls, version: AplusContentVersion.V_2020_11_01, *args, **kwargs
    ) -> AplusContent_V_2020_11_01: ...
    def __new__(
        cls,
        version: Union[AplusContentVersion, str] = AplusContentVersion.V_2020_11_01,
        *args,
        **kwargs,
    ):
        if not isinstance(version, AplusContentVersion):
            try:
                version = AplusContentVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == AplusContentVersion.V_2020_11_01:
            return AplusContent_V_2020_11_01(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
