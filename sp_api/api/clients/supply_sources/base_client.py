from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .supply_sources_v_2020_07_01 import SupplySources_V_2020_07_01


class SupplySourcesVersion(Enum):
    V_2020_07_01 = "2020-07-01"


class SupplySources(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> SupplySources_V_2020_07_01: ...
    @overload
    def __new__(
        cls, version: SupplySourcesVersion.V_2020_07_01, *args, **kwargs
    ) -> SupplySources_V_2020_07_01: ...
    def __new__(
        cls,
        version: Union[SupplySourcesVersion, str] = SupplySourcesVersion.V_2020_07_01,
        *args,
        **kwargs,
    ):
        if not isinstance(version, SupplySourcesVersion):
            try:
                version = SupplySourcesVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == SupplySourcesVersion.V_2020_07_01:
            return SupplySources_V_2020_07_01(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
