from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .fba_inbound_eligibility_v_v1 import FbaInboundEligibility_V_v1

class FbaInboundEligibilityVersion(Enum):
    V_v1: Literal["v1"]

class FbaInboundEligibility(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> FbaInboundEligibility_V_v1: ...
    # v1 explicit overload
    @overload
    def __new__(
        cls, version: Literal[FbaInboundEligibilityVersion.V_v1], *args, **kwargs
    ) -> FbaInboundEligibility_V_v1: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> FbaInboundEligibility_V_v1: ...
