from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .data_kiosk_v_2023_11_15 import DataKiosk_V_2023_11_15


class DataKioskVersion(Enum):
    V_2023_11_15 = "2023-11-15"


class DataKiosk(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> DataKiosk_V_2023_11_15: ...
    @overload
    def __new__(
        cls, version: DataKioskVersion.V_2023_11_15, *args, **kwargs
    ) -> DataKiosk_V_2023_11_15: ...
    def __new__(
        cls,
        version: Union[DataKioskVersion, str] = DataKioskVersion.V_2023_11_15,
        *args,
        **kwargs,
    ):
        if not isinstance(version, DataKioskVersion):
            try:
                version = DataKioskVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == DataKioskVersion.V_2023_11_15:
            return DataKiosk_V_2023_11_15(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
