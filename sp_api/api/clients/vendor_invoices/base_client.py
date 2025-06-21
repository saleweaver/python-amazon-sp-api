from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .vendor_invoices_v_v1 import VendorInvoices_V_v1


class VendorInvoicesVersion(Enum):
    V_v1 = "v1"


class VendorInvoices(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> VendorInvoices_V_v1: ...
    @overload
    def __new__(
        cls, version: VendorInvoicesVersion.V_v1, *args, **kwargs
    ) -> VendorInvoices_V_v1: ...
    def __new__(
        cls,
        version: Union[VendorInvoicesVersion, str] = VendorInvoicesVersion.V_v1,
        *args,
        **kwargs,
    ):
        if not isinstance(version, VendorInvoicesVersion):
            try:
                version = VendorInvoicesVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == VendorInvoicesVersion.V_v1:
            return VendorInvoices_V_v1(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
