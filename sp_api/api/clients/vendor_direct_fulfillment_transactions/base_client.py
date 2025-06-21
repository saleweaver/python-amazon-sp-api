from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .vendor_direct_fulfillment_transactions_v_2021_12_28 import \
    VendorDirectFulfillmentTransactions_V_2021_12_28
from .vendor_direct_fulfillment_transactions_v_v1 import \
    VendorDirectFulfillmentTransactions_V_v1


class VendorDirectFulfillmentTransactionsVersion(Enum):
    V_v1 = "v1"
    V_2021_12_28 = "2021-12-28"


class VendorDirectFulfillmentTransactions(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> VendorDirectFulfillmentTransactions_V_v1: ...
    @overload
    def __new__(
        cls, version: VendorDirectFulfillmentTransactionsVersion.V_v1, *args, **kwargs
    ) -> VendorDirectFulfillmentTransactions_V_v1: ...
    @overload
    def __new__(
        cls,
        version: VendorDirectFulfillmentTransactionsVersion.V_2021_12_28,
        *args,
        **kwargs,
    ) -> VendorDirectFulfillmentTransactions_V_2021_12_28: ...
    def __new__(
        cls,
        version: Union[
            VendorDirectFulfillmentTransactionsVersion, str
        ] = VendorDirectFulfillmentTransactionsVersion.V_2021_12_28,
        *args,
        **kwargs,
    ):
        if not isinstance(version, VendorDirectFulfillmentTransactionsVersion):
            try:
                version = VendorDirectFulfillmentTransactionsVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == VendorDirectFulfillmentTransactionsVersion.V_v1:
            return VendorDirectFulfillmentTransactions_V_v1(*args, **kwargs)
        if version == VendorDirectFulfillmentTransactionsVersion.V_2021_12_28:
            return VendorDirectFulfillmentTransactions_V_2021_12_28(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
