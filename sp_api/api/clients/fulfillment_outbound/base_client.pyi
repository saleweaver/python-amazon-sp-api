from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .fulfillment_outbound_v_2020_07_01 import FulfillmentOutbound_V_2020_07_01

class FulfillmentOutboundVersion(Enum):
    V_2020_07_01: Literal["2020-07-01"]

class FulfillmentOutbound(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> FulfillmentOutbound_V_2020_07_01: ...
    # 2020-07-01 explicit overload
    @overload
    def __new__(
        cls, version: Literal[FulfillmentOutboundVersion.V_2020_07_01], *args, **kwargs
    ) -> FulfillmentOutbound_V_2020_07_01: ...
    # fallback stub
    def __new__(
        cls, version=..., *args, **kwargs
    ) -> FulfillmentOutbound_V_2020_07_01: ...
