from __future__ import annotations

import enum
from typing import Any, Literal, TYPE_CHECKING, overload
from sp_api.util.versioned_client import VersionedClientMeta

from sp_api.asyncio.base import AsyncBaseClient

from .delivery_by_amazon_2022_07_01 import DeliveryByAmazonV20220701


class DeliveryByAmazonVersion(str, enum.Enum):
    V_2022_07_01 = "2022-07-01"
    LATEST = "2022-07-01"


if TYPE_CHECKING:

    class _DeliveryByAmazonMeta(VersionedClientMeta):
        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[DeliveryByAmazonVersion.V_2022_07_01, DeliveryByAmazonVersion.LATEST, "2022-07-01"],
            **kwargs: Any,
        ) -> DeliveryByAmazonV20220701: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> DeliveryByAmazonV20220701: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: str | DeliveryByAmazonVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...


else:
    _DeliveryByAmazonMeta = VersionedClientMeta


class DeliveryByAmazon(AsyncBaseClient, metaclass=_DeliveryByAmazonMeta):
    """DeliveryByAmazon API client.

    This class dispatches to a versioned DeliveryByAmazon API client.

    If you do not pass a version, the constructor returns the oldest supported implementation ("2022-07-01").
    """

    if TYPE_CHECKING:
        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[DeliveryByAmazonVersion.V_2022_07_01, DeliveryByAmazonVersion.LATEST, "2022-07-01"],
            **kwargs: Any,
        ) -> DeliveryByAmazonV20220701: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> DeliveryByAmazonV20220701: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: str | DeliveryByAmazonVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...

    _DISPATCH = True

    _DEFAULT_VERSION = "2022-07-01"

    _VERSION_MAP = {
        "2022-07-01": DeliveryByAmazonV20220701,
    }

    _VERSION_ALIASES = {
        "2022-07-01": "2022-07-01",
    }
