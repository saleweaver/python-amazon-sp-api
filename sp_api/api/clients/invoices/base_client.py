from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .invoices_v_2024_06_19 import Invoices_V_2024_06_19


class InvoicesVersion(Enum):
    V_2024_06_19 = "2024-06-19"


class Invoices(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> Invoices_V_2024_06_19: ...
    @overload
    def __new__(
        cls, version: InvoicesVersion.V_2024_06_19, *args, **kwargs
    ) -> Invoices_V_2024_06_19: ...
    def __new__(
        cls,
        version: Union[InvoicesVersion, str] = InvoicesVersion.V_2024_06_19,
        *args,
        **kwargs,
    ):
        if not isinstance(version, InvoicesVersion):
            try:
                version = InvoicesVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == InvoicesVersion.V_2024_06_19:
            return Invoices_V_2024_06_19(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
