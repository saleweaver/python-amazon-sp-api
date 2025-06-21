from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .merchant_fulfillment_v_v0 import MerchantFulfillment_V_v0


class MerchantFulfillmentVersion(Enum):
    V_v0 = "v0"


class MerchantFulfillment(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> MerchantFulfillment_V_v0: ...
    @overload
    def __new__(
        cls, version: MerchantFulfillmentVersion.V_v0, *args, **kwargs
    ) -> MerchantFulfillment_V_v0: ...
    def __new__(
        cls,
        version: Union[
            MerchantFulfillmentVersion, str
        ] = MerchantFulfillmentVersion.V_v0,
        *args,
        **kwargs,
    ):
        if not isinstance(version, MerchantFulfillmentVersion):
            try:
                version = MerchantFulfillmentVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == MerchantFulfillmentVersion.V_v0:
            return MerchantFulfillment_V_v0(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
