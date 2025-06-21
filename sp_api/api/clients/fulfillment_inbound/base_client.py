from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .fulfillment_inbound_v_2024_03_20 import FulfillmentInbound_V_2024_03_20
from .fulfillment_inbound_v_v0 import FulfillmentInbound_V_v0


class FulfillmentInboundVersion(Enum):
    V_v0 = "v0"
    V_2024_03_20 = "2024-03-20"


class FulfillmentInbound(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> FulfillmentInbound_V_v0: ...
    @overload
    def __new__(
        cls, version: FulfillmentInboundVersion.V_v0, *args, **kwargs
    ) -> FulfillmentInbound_V_v0: ...
    @overload
    def __new__(
        cls, version: FulfillmentInboundVersion.V_2024_03_20, *args, **kwargs
    ) -> FulfillmentInbound_V_2024_03_20: ...
    def __new__(
        cls,
        version: Union[
            FulfillmentInboundVersion, str
        ] = FulfillmentInboundVersion.V_2024_03_20,
        *args,
        **kwargs,
    ):
        if not isinstance(version, FulfillmentInboundVersion):
            try:
                version = FulfillmentInboundVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == FulfillmentInboundVersion.V_v0:
            return FulfillmentInbound_V_v0(*args, **kwargs)
        if version == FulfillmentInboundVersion.V_2024_03_20:
            return FulfillmentInbound_V_2024_03_20(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
