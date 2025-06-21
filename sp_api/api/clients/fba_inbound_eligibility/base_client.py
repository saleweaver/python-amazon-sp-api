from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .fba_inbound_eligibility_v_v1 import FbaInboundEligibility_V_v1


class FbaInboundEligibilityVersion(Enum):
    V_v1 = "v1"


class FbaInboundEligibility(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> FbaInboundEligibility_V_v1: ...
    @overload
    def __new__(
        cls, version: FbaInboundEligibilityVersion.V_v1, *args, **kwargs
    ) -> FbaInboundEligibility_V_v1: ...
    def __new__(
        cls,
        version: Union[
            FbaInboundEligibilityVersion, str
        ] = FbaInboundEligibilityVersion.V_v1,
        *args,
        **kwargs,
    ):
        if not isinstance(version, FbaInboundEligibilityVersion):
            try:
                version = FbaInboundEligibilityVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == FbaInboundEligibilityVersion.V_v1:
            return FbaInboundEligibility_V_v1(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
