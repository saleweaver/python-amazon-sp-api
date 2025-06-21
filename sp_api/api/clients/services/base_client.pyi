from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .services_v_v1 import Services_V_v1

class ServicesVersion(Enum):
    V_v1: Literal["v1"]

class Services(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> Services_V_v1: ...
    # v1 explicit overload
    @overload
    def __new__(
        cls, version: Literal[ServicesVersion.V_v1], *args, **kwargs
    ) -> Services_V_v1: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> Services_V_v1: ...
