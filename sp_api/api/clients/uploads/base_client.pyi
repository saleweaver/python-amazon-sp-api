from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .uploads_v_2020_11_01 import Uploads_V_2020_11_01

class UploadsVersion(Enum):
    V_2020_11_01: Literal["2020-11-01"]

class Uploads(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> Uploads_V_2020_11_01: ...
    # 2020-11-01 explicit overload
    @overload
    def __new__(
        cls, version: Literal[UploadsVersion.V_2020_11_01], *args, **kwargs
    ) -> Uploads_V_2020_11_01: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> Uploads_V_2020_11_01: ...
