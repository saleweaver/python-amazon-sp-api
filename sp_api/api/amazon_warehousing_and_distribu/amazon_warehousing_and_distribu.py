from __future__ import annotations

import enum
from typing import Any, Literal, TYPE_CHECKING, overload
from sp_api.util.versioned_client import VersionedClientMeta

from sp_api.base import Client

from .amazon_warehousing_and_distribu_2024_05_09 import (
    AmazonWarehousingAndDistributionV20240509,
)


class AmazonWarehousingAndDistributionVersion(str, enum.Enum):
    V_2024_05_09 = "2024-05-09"
    LATEST = "2024-05-09"


if TYPE_CHECKING:

    class _AmazonWarehousingAndDistributionMeta(VersionedClientMeta):
        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[
                AmazonWarehousingAndDistributionVersion.V_2024_05_09,
                AmazonWarehousingAndDistributionVersion.LATEST,
                "2024-05-09",
            ],
            **kwargs: Any,
        ) -> AmazonWarehousingAndDistributionV20240509: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> AmazonWarehousingAndDistributionV20240509: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: str | AmazonWarehousingAndDistributionVersion,
            **kwargs: Any,
        ) -> Client: ...


else:
    _AmazonWarehousingAndDistributionMeta = VersionedClientMeta


class AmazonWarehousingAndDistribution(
    Client, metaclass=_AmazonWarehousingAndDistributionMeta
):
    """Amazon Warehousing and Distribution API client.

    This class dispatches to a versioned Amazon Warehousing and Distribution API client.

    If you do not pass a version, the constructor returns the oldest supported implementation ("2024-05-09").
    """

    if TYPE_CHECKING:
        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[
                AmazonWarehousingAndDistributionVersion.V_2024_05_09,
                AmazonWarehousingAndDistributionVersion.LATEST,
                "2024-05-09",
            ],
            **kwargs: Any,
        ) -> AmazonWarehousingAndDistributionV20240509: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> AmazonWarehousingAndDistributionV20240509: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: str | AmazonWarehousingAndDistributionVersion,
            **kwargs: Any,
        ) -> Client: ...

    _DISPATCH = True

    _DEFAULT_VERSION = "2024-05-09"

    _VERSION_MAP = {
        "2024-05-09": AmazonWarehousingAndDistributionV20240509,
    }

    _VERSION_ALIASES = {
        "2024-05-09": "2024-05-09",
    }
