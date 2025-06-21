from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .tokens_v_2021_03_01 import Tokens_V_2021_03_01


class TokensVersion(Enum):
    V_2021_03_01 = "2021-03-01"


class Tokens(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> Tokens_V_2021_03_01: ...
    @overload
    def __new__(
        cls, version: TokensVersion.V_2021_03_01, *args, **kwargs
    ) -> Tokens_V_2021_03_01: ...
    def __new__(
        cls,
        version: Union[TokensVersion, str] = TokensVersion.V_2021_03_01,
        *args,
        **kwargs,
    ):
        if not isinstance(version, TokensVersion):
            try:
                version = TokensVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == TokensVersion.V_2021_03_01:
            return Tokens_V_2021_03_01(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
