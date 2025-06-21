from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .vendor_transaction_status_v_v1 import VendorTransactionStatus_V_v1


class VendorTransactionStatusVersion(Enum):
    V_v1 = "v1"


class VendorTransactionStatus(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> VendorTransactionStatus_V_v1: ...
    @overload
    def __new__(
        cls, version: VendorTransactionStatusVersion.V_v1, *args, **kwargs
    ) -> VendorTransactionStatus_V_v1: ...
    def __new__(
        cls,
        version: Union[
            VendorTransactionStatusVersion, str
        ] = VendorTransactionStatusVersion.V_v1,
        *args,
        **kwargs,
    ):
        if not isinstance(version, VendorTransactionStatusVersion):
            try:
                version = VendorTransactionStatusVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == VendorTransactionStatusVersion.V_v1:
            return VendorTransactionStatus_V_v1(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
