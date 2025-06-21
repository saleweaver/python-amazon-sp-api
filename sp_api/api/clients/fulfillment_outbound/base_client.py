from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .fulfillment_outbound_v_2020_07_01 import FulfillmentOutbound_V_2020_07_01


class FulfillmentOutboundVersion(Enum):
    V_2020_07_01 = "2020-07-01"


class FulfillmentOutbound(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> FulfillmentOutbound_V_2020_07_01: ...
    @overload
    def __new__(
        cls, version: FulfillmentOutboundVersion.V_2020_07_01, *args, **kwargs
    ) -> FulfillmentOutbound_V_2020_07_01: ...
    def __new__(
        cls,
        version: Union[
            FulfillmentOutboundVersion, str
        ] = FulfillmentOutboundVersion.V_2020_07_01,
        *args,
        **kwargs,
    ):
        if not isinstance(version, FulfillmentOutboundVersion):
            try:
                version = FulfillmentOutboundVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == FulfillmentOutboundVersion.V_2020_07_01:
            return FulfillmentOutbound_V_2020_07_01(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
