from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .feeds_v_2021_06_30 import Feeds_V_2021_06_30

class FeedsVersion(Enum):
    V_2021_06_30: Literal["2021-06-30"]

class Feeds(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> Feeds_V_2021_06_30: ...
    # 2021-06-30 explicit overload
    @overload
    def __new__(
        cls, version: Literal[FeedsVersion.V_2021_06_30], *args, **kwargs
    ) -> Feeds_V_2021_06_30: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> Feeds_V_2021_06_30: ...
