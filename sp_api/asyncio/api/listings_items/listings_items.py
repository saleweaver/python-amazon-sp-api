from __future__ import annotations

import enum
from typing import Any, Literal, TYPE_CHECKING, overload

from sp_api.asyncio.base import AsyncBaseClient
from sp_api.util.versioned_client import VersionedClientMeta

from .listings_items_2020_09_01 import ListingsItemsV20200901
from .listings_items_2021_08_01 import ListingsItemsV20210801


class ListingsItemsVersion(str, enum.Enum):
    V_2020_09_01 = "2020-09-01"
    V_2021_08_01 = "2021-08-01"
    LATEST = "2021-08-01"


if TYPE_CHECKING:

    class _ListingsItemsMeta(VersionedClientMeta):
        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[
                ListingsItemsVersion.V_2021_08_01, ListingsItemsVersion.LATEST, "2021-08-01"
            ],
            **kwargs: Any,
        ) -> ListingsItemsV20210801: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[ListingsItemsVersion.V_2020_09_01, "2020-09-01"],
            **kwargs: Any,
        ) -> ListingsItemsV20200901: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> ListingsItemsV20200901: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: str | ListingsItemsVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...


else:
    _ListingsItemsMeta = VersionedClientMeta


class ListingsItems(AsyncBaseClient, metaclass=_ListingsItemsMeta):
    """Listings Items API client.

    This class dispatches to a versioned Listings Items API client.

    If you do not pass a version, the constructor returns the oldest supported implementation ("2020-09-01").
    """

    if TYPE_CHECKING:
        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[
                ListingsItemsVersion.V_2021_08_01, ListingsItemsVersion.LATEST, "2021-08-01"
            ],
            **kwargs: Any,
        ) -> ListingsItemsV20210801: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[ListingsItemsVersion.V_2020_09_01, "2020-09-01"],
            **kwargs: Any,
        ) -> ListingsItemsV20200901: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> ListingsItemsV20200901: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: str | ListingsItemsVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...

    _DISPATCH = True

    _DEFAULT_VERSION = "2021-08-01"

    _VERSION_MAP = {
        "2020-09-01": ListingsItemsV20200901,
        "2021-08-01": ListingsItemsV20210801,
    }

    _VERSION_ALIASES = {
        "2020-09-01": "2020-09-01",
        "2021-08-01": "2021-08-01",
    }
