from __future__ import annotations

import enum
from typing import Any, Literal, TYPE_CHECKING, overload
from sp_api.util.versioned_client import VersionedClientMeta

from sp_api.asyncio.base import AsyncBaseClient

from .invoices_2024_06_19 import InvoicesV20240619


class InvoicesVersion(str, enum.Enum):
    V_2024_06_19 = "2024-06-19"
    LATEST = "2024-06-19"


if TYPE_CHECKING:

    class _InvoicesMeta(VersionedClientMeta):
        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[InvoicesVersion.V_2024_06_19, InvoicesVersion.LATEST, "2024-06-19"],
            **kwargs: Any,
        ) -> InvoicesV20240619: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> InvoicesV20240619: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: str | InvoicesVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...


else:
    _InvoicesMeta = VersionedClientMeta


class Invoices(AsyncBaseClient, metaclass=_InvoicesMeta):
    """Invoices API client.

    This class dispatches to a versioned Invoices API client.

    If you do not pass a version, the constructor returns the oldest supported implementation ("2024-06-19").
    """

    if TYPE_CHECKING:
        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[InvoicesVersion.V_2024_06_19, InvoicesVersion.LATEST, "2024-06-19"],
            **kwargs: Any,
        ) -> InvoicesV20240619: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> InvoicesV20240619: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: str | InvoicesVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...

    _DISPATCH = True

    _DEFAULT_VERSION = "2024-06-19"

    _VERSION_MAP = {
        "2024-06-19": InvoicesV20240619,
    }

    _VERSION_ALIASES = {
        "2024-06-19": "2024-06-19",
    }
