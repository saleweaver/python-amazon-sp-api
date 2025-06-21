from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .invoices_v_2024_06_19 import Invoices_V_2024_06_19

class InvoicesVersion(Enum):
    V_2024_06_19: Literal["2024-06-19"]

class Invoices(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> Invoices_V_2024_06_19: ...
    # 2024-06-19 explicit overload
    @overload
    def __new__(
        cls, version: Literal[InvoicesVersion.V_2024_06_19], *args, **kwargs
    ) -> Invoices_V_2024_06_19: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> Invoices_V_2024_06_19: ...
