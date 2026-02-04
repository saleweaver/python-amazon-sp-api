from __future__ import annotations

import enum
from typing import Any, Literal, TYPE_CHECKING, overload

from sp_api.asyncio.base import AsyncBaseClient
from sp_api.util.versioned_client import VersionedClientMeta

from .catalog_items_2020_12_01 import CatalogItemsV20201201
from .catalog_items_2022_04_01 import CatalogItemsV20220401


class CatalogItemsVersion(str, enum.Enum):
    V_2020_12_01 = "2020-12-01"
    V_2022_04_01 = "2022-04-01"
    LATEST = "2022-04-01"


if TYPE_CHECKING:

    class _CatalogItemsMeta(VersionedClientMeta):
        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[
                CatalogItemsVersion.V_2022_04_01, CatalogItemsVersion.LATEST, "2022-04-01"
            ],
            **kwargs: Any,
        ) -> CatalogItemsV20220401: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[CatalogItemsVersion.V_2020_12_01, "2020-12-01"],
            **kwargs: Any,
        ) -> CatalogItemsV20201201: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> CatalogItemsV20201201: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: str | CatalogItemsVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...


else:
    _CatalogItemsMeta = VersionedClientMeta


class CatalogItems(AsyncBaseClient, metaclass=_CatalogItemsMeta):
    """Catalog Items API client.

    This class dispatches to a versioned Catalog Items API client.

    If you do not pass a version, the constructor returns the oldest supported implementation ("2020-12-01").
    """

    if TYPE_CHECKING:
        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[
                CatalogItemsVersion.V_2022_04_01, CatalogItemsVersion.LATEST, "2022-04-01"
            ],
            **kwargs: Any,
        ) -> CatalogItemsV20220401: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[CatalogItemsVersion.V_2020_12_01, "2020-12-01"],
            **kwargs: Any,
        ) -> CatalogItemsV20201201: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> CatalogItemsV20201201: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: str | CatalogItemsVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...

    _DISPATCH = True

    _DEFAULT_VERSION = "2020-12-01"

    _VERSION_MAP = {
        "2020-12-01": CatalogItemsV20201201,
        "2022-04-01": CatalogItemsV20220401,
    }

    _VERSION_ALIASES = {
        "2020-12-01": "2020-12-01",
        "2022-04-01": "2022-04-01",
    }
