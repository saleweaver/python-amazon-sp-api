from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .aplus_content_v_2020_11_01 import AplusContent_V_2020_11_01

class AplusContentVersion(Enum):
    V_2020_11_01: Literal["2020-11-01"]

class AplusContent(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> AplusContent_V_2020_11_01: ...
    # 2020-11-01 explicit overload
    @overload
    def __new__(
        cls, version: Literal[AplusContentVersion.V_2020_11_01], *args, **kwargs
    ) -> AplusContent_V_2020_11_01: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> AplusContent_V_2020_11_01: ...
