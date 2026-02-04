from __future__ import annotations

import enum
from typing import Any, Literal, TYPE_CHECKING, overload

from sp_api.asyncio.base import AsyncBaseClient
from sp_api.util.versioned_client import VersionedClientMeta

from .returns_2021_08_19 import ExternalFulfillmentReturnsV20210819
from .returns_2024_09_11 import ExternalFulfillmentReturnsV20240911


class ExternalFulfillmentReturnsVersion(str, enum.Enum):
    V_2021_08_19 = "2021-08-19"
    V_2024_09_11 = "2024-09-11"
    LATEST = "2024-09-11"


if TYPE_CHECKING:

    class _ExternalFulfillmentReturnsMeta(VersionedClientMeta):
        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[
                ExternalFulfillmentReturnsVersion.V_2024_09_11,
                ExternalFulfillmentReturnsVersion.LATEST,
                "2024-09-11",
            ],
            **kwargs: Any,
        ) -> ExternalFulfillmentReturnsV20240911: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[
                ExternalFulfillmentReturnsVersion.V_2021_08_19, "2021-08-19"
            ],
            **kwargs: Any,
        ) -> ExternalFulfillmentReturnsV20210819: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> ExternalFulfillmentReturnsV20210819: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: str | ExternalFulfillmentReturnsVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...


else:
    _ExternalFulfillmentReturnsMeta = VersionedClientMeta


class ExternalFulfillmentReturns(AsyncBaseClient, metaclass=_ExternalFulfillmentReturnsMeta):
    """External Fulfillment Returns API client.

    This class dispatches to a versioned External Fulfillment Returns API client.

    If you do not pass a version, the constructor returns the oldest supported implementation ("2021-08-19").
    """

    if TYPE_CHECKING:
        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[
                ExternalFulfillmentReturnsVersion.V_2024_09_11,
                ExternalFulfillmentReturnsVersion.LATEST,
                "2024-09-11",
            ],
            **kwargs: Any,
        ) -> ExternalFulfillmentReturnsV20240911: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[
                ExternalFulfillmentReturnsVersion.V_2021_08_19, "2021-08-19"
            ],
            **kwargs: Any,
        ) -> ExternalFulfillmentReturnsV20210819: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> ExternalFulfillmentReturnsV20210819: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: str | ExternalFulfillmentReturnsVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...

    _DISPATCH = True

    _DEFAULT_VERSION = "2021-08-19"

    _VERSION_MAP = {
        "2021-08-19": ExternalFulfillmentReturnsV20210819,
        "2024-09-11": ExternalFulfillmentReturnsV20240911,
    }

    _VERSION_ALIASES = {
        "2021-08-19": "2021-08-19",
        "2024-09-11": "2024-09-11",
    }
