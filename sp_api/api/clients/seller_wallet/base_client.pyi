from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .seller_wallet_v_2024_03_01 import SellerWallet_V_2024_03_01

class SellerWalletVersion(Enum):
    V_2024_03_01: Literal["2024-03-01"]

class SellerWallet(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> SellerWallet_V_2024_03_01: ...
    # 2024-03-01 explicit overload
    @overload
    def __new__(
        cls, version: Literal[SellerWalletVersion.V_2024_03_01], *args, **kwargs
    ) -> SellerWallet_V_2024_03_01: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> SellerWallet_V_2024_03_01: ...
