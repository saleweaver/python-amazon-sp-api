from __future__ import annotations

import enum
from typing import Any, Literal, TYPE_CHECKING, overload
from sp_api.util.versioned_client import VersionedClientMeta

from sp_api.base import Client

from .vehicles_2024_11_01 import VehiclesV20241101


class VehiclesVersion(str, enum.Enum):
    V_2024_11_01 = "2024-11-01"
    LATEST = "2024-11-01"


if TYPE_CHECKING:

    class _VehiclesMeta(VersionedClientMeta):
        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[VehiclesVersion.V_2024_11_01, VehiclesVersion.LATEST, "2024-11-01"],
            **kwargs: Any,
        ) -> VehiclesV20241101: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> VehiclesV20241101: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: str | VehiclesVersion,
            **kwargs: Any,
        ) -> Client: ...


else:
    _VehiclesMeta = VersionedClientMeta


class Vehicles(Client, metaclass=_VehiclesMeta):
    """Vehicles API client.

    This class dispatches to a versioned Vehicles API client.

    If you do not pass a version, the constructor returns the oldest supported implementation ("2024-11-01").
    """

    if TYPE_CHECKING:
        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[VehiclesVersion.V_2024_11_01, VehiclesVersion.LATEST, "2024-11-01"],
            **kwargs: Any,
        ) -> VehiclesV20241101: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> VehiclesV20241101: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: str | VehiclesVersion,
            **kwargs: Any,
        ) -> Client: ...

    _DISPATCH = True

    _DEFAULT_VERSION = "2024-11-01"

    _VERSION_MAP = {
        "2024-11-01": VehiclesV20241101,
    }

    _VERSION_ALIASES = {
        "2024-11-01": "2024-11-01",
    }
