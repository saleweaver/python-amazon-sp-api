from __future__ import annotations

import enum
from typing import Any, Literal, TYPE_CHECKING, overload

from sp_api.asyncio.base import AsyncBaseClient
from sp_api.util.versioned_client import VersionedClientMeta

from .finances_2024_06_01 import FinancesV20240601
from .finances_2024_06_19 import FinancesV20240619
from .finances_v0 import FinancesV0


class FinancesVersion(str, enum.Enum):
    V0 = "v0"
    V_2024_06_01 = "2024-06-01"
    V_2024_06_19 = "2024-06-19"
    LATEST = "2024-06-19"


if TYPE_CHECKING:

    class _FinancesMeta(VersionedClientMeta):
        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[FinancesVersion.V_2024_06_19, FinancesVersion.LATEST, "2024-06-19"],
            **kwargs: Any,
        ) -> FinancesV20240619: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[FinancesVersion.V_2024_06_01, "2024-06-01"],
            **kwargs: Any,
        ) -> FinancesV20240601: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[FinancesVersion.V0, "v0"],
            **kwargs: Any,
        ) -> FinancesV0: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> FinancesV0: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: str | FinancesVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...


else:
    _FinancesMeta = VersionedClientMeta


class Finances(AsyncBaseClient, metaclass=_FinancesMeta):
    """Finances API client.

    This class dispatches to a versioned Finances API client.

    If you do not pass a version, the constructor returns the oldest supported implementation ("v0").
    """

    if TYPE_CHECKING:
        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[FinancesVersion.V_2024_06_19, FinancesVersion.LATEST, "2024-06-19"],
            **kwargs: Any,
        ) -> FinancesV20240619: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[FinancesVersion.V_2024_06_01, "2024-06-01"],
            **kwargs: Any,
        ) -> FinancesV20240601: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[FinancesVersion.V0, "v0"],
            **kwargs: Any,
        ) -> FinancesV0: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> FinancesV0: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: str | FinancesVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...

    _DISPATCH = True

    _DEFAULT_VERSION = "v0"

    _VERSION_MAP = {
        "v0": FinancesV0,
        "2024-06-01": FinancesV20240601,
        "2024-06-19": FinancesV20240619,
    }

    _VERSION_ALIASES = {
        "v0": "v0",
        "2024-06-01": "2024-06-01",
        "2024-06-19": "2024-06-19",
    }
