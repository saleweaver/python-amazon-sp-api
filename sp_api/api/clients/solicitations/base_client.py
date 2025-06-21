from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .solicitations_v_v1 import Solicitations_V_v1


class SolicitationsVersion(Enum):
    V_v1 = "v1"


class Solicitations(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> Solicitations_V_v1: ...
    @overload
    def __new__(
        cls, version: SolicitationsVersion.V_v1, *args, **kwargs
    ) -> Solicitations_V_v1: ...
    def __new__(
        cls,
        version: Union[SolicitationsVersion, str] = SolicitationsVersion.V_v1,
        *args,
        **kwargs,
    ):
        if not isinstance(version, SolicitationsVersion):
            try:
                version = SolicitationsVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == SolicitationsVersion.V_v1:
            return Solicitations_V_v1(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
