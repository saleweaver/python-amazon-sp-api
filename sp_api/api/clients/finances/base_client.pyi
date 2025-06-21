from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .finances_v_2024_06_01 import Finances_V_2024_06_01
from .finances_v_2024_06_19 import Finances_V_2024_06_19
from .finances_v_v0 import Finances_V_v0

class FinancesVersion(Enum):
    V_v0: Literal["v0"]
    V_2024_06_01: Literal["2024-06-01"]
    V_2024_06_19: Literal["2024-06-19"]

class Finances(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> Finances_V_2024_06_19: ...
    # v0 explicit overload
    @overload
    def __new__(
        cls, version: Literal[FinancesVersion.V_v0], *args, **kwargs
    ) -> Finances_V_v0: ...
    # 2024-06-01 explicit overload
    @overload
    def __new__(
        cls, version: Literal[FinancesVersion.V_2024_06_01], *args, **kwargs
    ) -> Finances_V_2024_06_01: ...
    # 2024-06-19 explicit overload
    @overload
    def __new__(
        cls, version: Literal[FinancesVersion.V_2024_06_19], *args, **kwargs
    ) -> Finances_V_2024_06_19: ...
    # fallback stub
    def __new__(
        cls, version=..., *args, **kwargs
    ) -> Finances_V_v0 | Finances_V_2024_06_01 | Finances_V_2024_06_19: ...
