from __future__ import annotations

import enum
from typing import Any, Literal, TYPE_CHECKING, overload
from sp_api.util.versioned_client import VersionedClientMeta

from sp_api.base import ApiResponse, Client, Marketplaces, deprecated, fill_query_params, sp_endpoint
from sp_api.util import normalize_csv_param

from .orders_2026_01_01 import OrdersV20260101
from .orders_v0 import OrdersV0

class OrdersVersion(str, enum.Enum):
    V0 = "v0"  # legacy
    V_2026_01_01 = "2026-01-01"
    LATEST = "2026-01-01"


if TYPE_CHECKING:

    class _OrdersMeta(VersionedClientMeta):
        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[OrdersVersion.V_2026_01_01, OrdersVersion.LATEST, "2026-01-01"],
            **kwargs: Any,
        ) -> OrdersV20260101: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[OrdersVersion.V0, "v0"],
            **kwargs: Any,
        ) -> OrdersV0: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> OrdersV0: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: str | OrdersVersion,
            **kwargs: Any,
        ) -> Client: ...


else:
    _OrdersMeta = VersionedClientMeta

class Orders(Client, metaclass=_OrdersMeta):
    """Orders API client.

    This class dispatches to a versioned Orders API client.

    If you do not pass a version, the constructor returns the oldest supported implementation ("v0").

    :link: https://github.com/amzn/selling-partner-api-docs/tree/main/references/orders-api
    """

    if TYPE_CHECKING:
        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[OrdersVersion.V_2026_01_01, OrdersVersion.LATEST, "2026-01-01"],
            **kwargs: Any,
        ) -> OrdersV20260101: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[OrdersVersion.V0, "v0"],
            **kwargs: Any,
        ) -> OrdersV0: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> OrdersV0: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: str | OrdersVersion,
            **kwargs: Any,
        ) -> Client: ...

    _DISPATCH = True

    _DEFAULT_VERSION = "v0"

    _VERSION_MAP = {
        "v0": OrdersV0,
        "2026-01-01": OrdersV20260101,
    }

    _VERSION_ALIASES = {
        "v0": "v0",
        "2026-01-01": "2026-01-01",
    }
