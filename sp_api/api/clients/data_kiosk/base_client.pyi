from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .data_kiosk_v_2023_11_15 import DataKiosk_V_2023_11_15

class DataKioskVersion(Enum):
    V_2023_11_15: Literal["2023-11-15"]

class DataKiosk(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> DataKiosk_V_2023_11_15: ...
    # 2023-11-15 explicit overload
    @overload
    def __new__(
        cls, version: Literal[DataKioskVersion.V_2023_11_15], *args, **kwargs
    ) -> DataKiosk_V_2023_11_15: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> DataKiosk_V_2023_11_15: ...
