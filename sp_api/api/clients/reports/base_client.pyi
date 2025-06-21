from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .reports_v_2021_06_30 import Reports_V_2021_06_30

class ReportsVersion(Enum):
    V_2021_06_30: Literal["2021-06-30"]

class Reports(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> Reports_V_2021_06_30: ...
    # 2021-06-30 explicit overload
    @overload
    def __new__(
        cls, version: Literal[ReportsVersion.V_2021_06_30], *args, **kwargs
    ) -> Reports_V_2021_06_30: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> Reports_V_2021_06_30: ...
