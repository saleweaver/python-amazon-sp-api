from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .reports_v_2021_06_30 import Reports_V_2021_06_30


class ReportsVersion(Enum):
    V_2021_06_30 = "2021-06-30"


class Reports(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> Reports_V_2021_06_30: ...
    @overload
    def __new__(
        cls, version: ReportsVersion.V_2021_06_30, *args, **kwargs
    ) -> Reports_V_2021_06_30: ...
    def __new__(
        cls,
        version: Union[ReportsVersion, str] = ReportsVersion.V_2021_06_30,
        *args,
        **kwargs,
    ):
        if not isinstance(version, ReportsVersion):
            try:
                version = ReportsVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == ReportsVersion.V_2021_06_30:
            return Reports_V_2021_06_30(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
