from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .feeds_v_2021_06_30 import Feeds_V_2021_06_30


class FeedsVersion(Enum):
    V_2021_06_30 = "2021-06-30"


class Feeds(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> Feeds_V_2021_06_30: ...
    @overload
    def __new__(
        cls, version: FeedsVersion.V_2021_06_30, *args, **kwargs
    ) -> Feeds_V_2021_06_30: ...
    def __new__(
        cls,
        version: Union[FeedsVersion, str] = FeedsVersion.V_2021_06_30,
        *args,
        **kwargs,
    ):
        if not isinstance(version, FeedsVersion):
            try:
                version = FeedsVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == FeedsVersion.V_2021_06_30:
            return Feeds_V_2021_06_30(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
