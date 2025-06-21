from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .seller_wallet_v_2024_03_01 import SellerWallet_V_2024_03_01


class SellerWalletVersion(Enum):
    V_2024_03_01 = "2024-03-01"


class SellerWallet(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> SellerWallet_V_2024_03_01: ...
    @overload
    def __new__(
        cls, version: SellerWalletVersion.V_2024_03_01, *args, **kwargs
    ) -> SellerWallet_V_2024_03_01: ...
    def __new__(
        cls,
        version: Union[SellerWalletVersion, str] = SellerWalletVersion.V_2024_03_01,
        *args,
        **kwargs,
    ):
        if not isinstance(version, SellerWalletVersion):
            try:
                version = SellerWalletVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == SellerWalletVersion.V_2024_03_01:
            return SellerWallet_V_2024_03_01(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
