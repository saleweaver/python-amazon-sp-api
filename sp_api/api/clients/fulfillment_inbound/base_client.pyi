from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .fulfillment_inbound_v_2024_03_20 import FulfillmentInbound_V_2024_03_20
from .fulfillment_inbound_v_v0 import FulfillmentInbound_V_v0

class FulfillmentInboundVersion(Enum):
    V_v0: Literal["v0"]
    V_2024_03_20: Literal["2024-03-20"]

class FulfillmentInbound(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> FulfillmentInbound_V_2024_03_20: ...
    # v0 explicit overload
    @overload
    def __new__(
        cls, version: Literal[FulfillmentInboundVersion.V_v0], *args, **kwargs
    ) -> FulfillmentInbound_V_v0: ...
    # 2024-03-20 explicit overload
    @overload
    def __new__(
        cls, version: Literal[FulfillmentInboundVersion.V_2024_03_20], *args, **kwargs
    ) -> FulfillmentInbound_V_2024_03_20: ...
    # fallback stub
    def __new__(
        cls, version=..., *args, **kwargs
    ) -> FulfillmentInbound_V_v0 | FulfillmentInbound_V_2024_03_20: ...
