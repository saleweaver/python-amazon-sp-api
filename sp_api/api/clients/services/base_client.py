from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .services_v_v1 import Services_V_v1


class ServicesVersion(Enum):
    V_v1 = "v1"


class Services(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> Services_V_v1: ...
    @overload
    def __new__(
        cls, version: ServicesVersion.V_v1, *args, **kwargs
    ) -> Services_V_v1: ...
    def __new__(
        cls,
        version: Union[ServicesVersion, str] = ServicesVersion.V_v1,
        *args,
        **kwargs,
    ):
        if not isinstance(version, ServicesVersion):
            try:
                version = ServicesVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == ServicesVersion.V_v1:
            return Services_V_v1(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
