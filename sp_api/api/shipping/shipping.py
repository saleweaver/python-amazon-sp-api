from __future__ import annotations

import enum
from typing import Any, Literal, TYPE_CHECKING, overload
from sp_api.util.versioned_client import VersionedClientMeta

from sp_api.base import Client

from .shipping_v1 import ShippingV1
from .shipping_v2 import ShippingV2


class ShippingVersion(str, enum.Enum):
    V1 = "v1"
    V2 = "v2"
    LATEST = "v2"


if TYPE_CHECKING:

    class _ShippingMeta(VersionedClientMeta):
        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[ShippingVersion.V2, ShippingVersion.LATEST, "v2"],
            **kwargs: Any,
        ) -> ShippingV2: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[ShippingVersion.V1, "v1"],
            **kwargs: Any,
        ) -> ShippingV1: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> ShippingV1: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: str | ShippingVersion,
            **kwargs: Any,
        ) -> Client: ...


else:
    _ShippingMeta = VersionedClientMeta


class Shipping(Client, metaclass=_ShippingMeta):
    """Shipping API client.

    This class dispatches to a versioned Shipping API client.

    If you do not pass a version, the constructor returns the oldest supported implementation ("v1").
    """

    if TYPE_CHECKING:
        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[ShippingVersion.V2, ShippingVersion.LATEST, "v2"],
            **kwargs: Any,
        ) -> ShippingV2: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[ShippingVersion.V1, "v1"],
            **kwargs: Any,
        ) -> ShippingV1: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> ShippingV1: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: str | ShippingVersion,
            **kwargs: Any,
        ) -> Client: ...

    _DISPATCH = True

    _DEFAULT_VERSION = "v1"

    _VERSION_MAP = {
        "v1": ShippingV1,
        "v2": ShippingV2,
    }

    _VERSION_ALIASES = {
        "v1": "v1",
        "v2": "v2",
    }
