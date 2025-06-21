from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .finances_v_2024_06_01 import Finances_V_2024_06_01
from .finances_v_2024_06_19 import Finances_V_2024_06_19
from .finances_v_v0 import Finances_V_v0


class FinancesVersion(Enum):
    V_v0 = "v0"
    V_2024_06_01 = "2024-06-01"
    V_2024_06_19 = "2024-06-19"


class Finances(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> Finances_V_v0: ...
    @overload
    def __new__(
        cls, version: FinancesVersion.V_v0, *args, **kwargs
    ) -> Finances_V_v0: ...
    @overload
    def __new__(
        cls, version: FinancesVersion.V_2024_06_01, *args, **kwargs
    ) -> Finances_V_2024_06_01: ...
    @overload
    def __new__(
        cls, version: FinancesVersion.V_2024_06_19, *args, **kwargs
    ) -> Finances_V_2024_06_19: ...
    def __new__(
        cls,
        version: Union[FinancesVersion, str] = FinancesVersion.V_2024_06_19,
        *args,
        **kwargs,
    ):
        if not isinstance(version, FinancesVersion):
            try:
                version = FinancesVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == FinancesVersion.V_v0:
            return Finances_V_v0(*args, **kwargs)
        if version == FinancesVersion.V_2024_06_01:
            return Finances_V_2024_06_01(*args, **kwargs)
        if version == FinancesVersion.V_2024_06_19:
            return Finances_V_2024_06_19(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
