from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .solicitations_v_v1 import Solicitations_V_v1

class SolicitationsVersion(Enum):
    V_v1: Literal["v1"]

class Solicitations(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> Solicitations_V_v1: ...
    # v1 explicit overload
    @overload
    def __new__(
        cls, version: Literal[SolicitationsVersion.V_v1], *args, **kwargs
    ) -> Solicitations_V_v1: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> Solicitations_V_v1: ...
