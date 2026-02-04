from __future__ import annotations

import enum
from typing import Any, Literal, TYPE_CHECKING, overload
from sp_api.util.versioned_client import VersionedClientMeta

from sp_api.asyncio.base import AsyncBaseClient

from .seller_wallet_2024_03_01 import SellerWalletV20240301


class SellerWalletVersion(str, enum.Enum):
    V_2024_03_01 = "2024-03-01"
    LATEST = "2024-03-01"


if TYPE_CHECKING:

    class _SellerWalletMeta(VersionedClientMeta):
        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[SellerWalletVersion.V_2024_03_01, SellerWalletVersion.LATEST, "2024-03-01"],
            **kwargs: Any,
        ) -> SellerWalletV20240301: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> SellerWalletV20240301: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: str | SellerWalletVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...


else:
    _SellerWalletMeta = VersionedClientMeta


class SellerWallet(AsyncBaseClient, metaclass=_SellerWalletMeta):
    """SellerWallet API client.

    This class dispatches to a versioned SellerWallet API client.

    If you do not pass a version, the constructor returns the oldest supported implementation ("2024-03-01").
    """

    if TYPE_CHECKING:
        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[SellerWalletVersion.V_2024_03_01, SellerWalletVersion.LATEST, "2024-03-01"],
            **kwargs: Any,
        ) -> SellerWalletV20240301: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> SellerWalletV20240301: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: str | SellerWalletVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...

    _DISPATCH = True

    _DEFAULT_VERSION = "2024-03-01"

    _VERSION_MAP = {
        "2024-03-01": SellerWalletV20240301,
    }

    _VERSION_ALIASES = {
        "2024-03-01": "2024-03-01",
    }
