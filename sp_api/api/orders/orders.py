from __future__ import annotations

import enum
from typing import Any, Literal, TYPE_CHECKING, overload

from sp_api.base import ApiResponse, Client, Marketplaces, deprecated, fill_query_params, sp_endpoint
from sp_api.util import normalize_csv_param

from .orders_2026_01_01 import OrdersV20260101
from .orders_v0 import OrdersV0

class OrdersVersion(str, enum.Enum):
    V0 = "v0"  # legacy
    V_2026_01_01 = "2026-01-01"
    LATEST = "2026-01-01"


class _VersionedClientMeta(type):
    """Metaclass that dispatches construction to a version-specific implementation.

    This keeps the call-site ergonomic (`Orders(version=...)`) while allowing a single
    place to implement the dispatch logic.

    Subclasses should define:
      - `_VERSION_MAP`: mapping of normalized version strings to implementation classes
      - `_VERSION_ALIASES` (optional): mapping of alias strings to normalized versions

    If no version is provided, the default version is used.
    """

    def __call__(cls, *args: Any, **kwargs: Any):
        version = kwargs.pop("version", None)

        # Only dispatch for the public front class itself.
        if cls is Orders:
            # Backwards-compatible default: if no version is provided, return the
            # oldest supported implementation.
            v_raw = version if version is not None else getattr(cls, "_DEFAULT_VERSION", None)
            if v_raw is None:
                return super().__call__(*args, **kwargs)

            v_raw = getattr(v_raw, "value", v_raw)
            v = str(v_raw)
            aliases: dict[str, str] = getattr(cls, "_VERSION_ALIASES", {})
            v_norm = aliases.get(v, v)

            impl_map: dict[str, type] = getattr(cls, "_VERSION_MAP", {})
            impl = impl_map.get(v_norm)
            if impl is not None:
                return impl(*args, **kwargs)

            supported = ", ".join(sorted(impl_map.keys()))
            raise ValueError(f"Unsupported version {v!r}. Supported: {supported}")

        return super().__call__(*args, **kwargs)


if TYPE_CHECKING:

    class _OrdersMeta(_VersionedClientMeta):
        @overload
        def __call__(
            self,
            *args: Any,
            version: Literal[OrdersVersion.V_2026_01_01, OrdersVersion.LATEST, "2026-01-01"],
            **kwargs: Any,
        ) -> OrdersV20260101: ...

        @overload
        def __call__(
            self,
            *args: Any,
            version: Literal[OrdersVersion.V0, "v0"],
            **kwargs: Any,
        ) -> OrdersV0: ...

        @overload
        def __call__(
            self,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> OrdersV0: ...

        @overload
        def __call__(
            self,
            *args: Any,
            version: str | OrdersVersion,
            **kwargs: Any,
        ) -> Client: ...


else:
    _OrdersMeta = _VersionedClientMeta

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

    _DEFAULT_VERSION = "v0"

    _VERSION_MAP = {
        "v0": OrdersV0,
        "2026-01-01": OrdersV20260101,
    }

    _VERSION_ALIASES = {
        "v0": "v0",
        "2026-01-01": "2026-01-01",
    }
