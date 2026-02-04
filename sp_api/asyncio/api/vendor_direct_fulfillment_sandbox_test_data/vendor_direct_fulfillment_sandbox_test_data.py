from __future__ import annotations

import enum
from typing import Any, Literal, TYPE_CHECKING, overload
from sp_api.util.versioned_client import VersionedClientMeta

from sp_api.asyncio.base import AsyncBaseClient

from .vendor_direct_fulfillment_sandbox_test_data_2021_10_28 import VendorDirectFulfillmentSandboxTestDataV20211028


class VendorDirectFulfillmentSandboxTestDataVersion(str, enum.Enum):
    V_2021_10_28 = "2021-10-28"
    LATEST = "2021-10-28"


if TYPE_CHECKING:

    class _VendorDirectFulfillmentSandboxTestDataMeta(VersionedClientMeta):
        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[VendorDirectFulfillmentSandboxTestDataVersion.V_2021_10_28, VendorDirectFulfillmentSandboxTestDataVersion.LATEST, "2021-10-28"],
            **kwargs: Any,
        ) -> VendorDirectFulfillmentSandboxTestDataV20211028: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> VendorDirectFulfillmentSandboxTestDataV20211028: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: str | VendorDirectFulfillmentSandboxTestDataVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...


else:
    _VendorDirectFulfillmentSandboxTestDataMeta = VersionedClientMeta


class VendorDirectFulfillmentSandboxTestData(AsyncBaseClient, metaclass=_VendorDirectFulfillmentSandboxTestDataMeta):
    """VendorDirectFulfillmentSandboxTestData API client.

    This class dispatches to a versioned VendorDirectFulfillmentSandboxTestData API client.

    If you do not pass a version, the constructor returns the oldest supported implementation ("2021-10-28").
    """

    if TYPE_CHECKING:
        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[VendorDirectFulfillmentSandboxTestDataVersion.V_2021_10_28, VendorDirectFulfillmentSandboxTestDataVersion.LATEST, "2021-10-28"],
            **kwargs: Any,
        ) -> VendorDirectFulfillmentSandboxTestDataV20211028: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> VendorDirectFulfillmentSandboxTestDataV20211028: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: str | VendorDirectFulfillmentSandboxTestDataVersion,
            **kwargs: Any,
        ) -> AsyncBaseClient: ...

    _DISPATCH = True

    _DEFAULT_VERSION = "2021-10-28"

    _VERSION_MAP = {
        "2021-10-28": VendorDirectFulfillmentSandboxTestDataV20211028,
    }

    _VERSION_ALIASES = {
        "2021-10-28": "2021-10-28",
    }
