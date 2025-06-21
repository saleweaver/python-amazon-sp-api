from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .uploads_v_2020_11_01 import Uploads_V_2020_11_01


class UploadsVersion(Enum):
    V_2020_11_01 = "2020-11-01"


class Uploads(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> Uploads_V_2020_11_01: ...
    @overload
    def __new__(
        cls, version: UploadsVersion.V_2020_11_01, *args, **kwargs
    ) -> Uploads_V_2020_11_01: ...
    def __new__(
        cls,
        version: Union[UploadsVersion, str] = UploadsVersion.V_2020_11_01,
        *args,
        **kwargs,
    ):
        if not isinstance(version, UploadsVersion):
            try:
                version = UploadsVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == UploadsVersion.V_2020_11_01:
            return Uploads_V_2020_11_01(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
