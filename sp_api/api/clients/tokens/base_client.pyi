from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .tokens_v_2021_03_01 import Tokens_V_2021_03_01

class TokensVersion(Enum):
    V_2021_03_01: Literal["2021-03-01"]

class Tokens(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> Tokens_V_2021_03_01: ...
    # 2021-03-01 explicit overload
    @overload
    def __new__(
        cls, version: Literal[TokensVersion.V_2021_03_01], *args, **kwargs
    ) -> Tokens_V_2021_03_01: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> Tokens_V_2021_03_01: ...
