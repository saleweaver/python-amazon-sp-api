from __future__ import annotations

import enum
from typing import Any, Literal, TYPE_CHECKING, overload
from sp_api.util.versioned_client import VersionedClientMeta

from sp_api.asyncio.base import AsyncBaseClient

from .shipment_invoicing_v0 import ShipmentInvoicingV0


class ShipmentInvoicingVersion(str, enum.Enum):
    V0 = "v0"
    LATEST = "v0"


if TYPE_CHECKING:

    class _ShipmentInvoicingMeta(VersionedClientMeta):
        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[ShipmentInvoicingVersion.V0, ShipmentInvoicingVersion.LATEST, "v0"],
            **kwargs: Any,
        ) -> ShipmentInvoicingV0: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> ShipmentInvoicingV0: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: str | ShipmentInvoicingVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...


else:
    _ShipmentInvoicingMeta = VersionedClientMeta


class ShipmentInvoicing(AsyncBaseClient, metaclass=_ShipmentInvoicingMeta):
    """ShipmentInvoicing API client.

    This class dispatches to a versioned ShipmentInvoicing API client.

    If you do not pass a version, the constructor returns the oldest supported implementation ("v0").
    """

    if TYPE_CHECKING:
        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[ShipmentInvoicingVersion.V0, ShipmentInvoicingVersion.LATEST, "v0"],
            **kwargs: Any,
        ) -> ShipmentInvoicingV0: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> ShipmentInvoicingV0: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: str | ShipmentInvoicingVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...

    _DISPATCH = True

    _DEFAULT_VERSION = "v0"

    _VERSION_MAP = {
        "v0": ShipmentInvoicingV0,
    }

    _VERSION_ALIASES = {
        "v0": "v0",
    }
