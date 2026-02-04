from __future__ import annotations

import enum
from typing import Any, Literal, TYPE_CHECKING, overload
from sp_api.util.versioned_client import VersionedClientMeta

from sp_api.base import Client

from .vendor_direct_fulfillment_transactions_2021_12_28 import (
    VendorDirectFulfillmentTransactionsV20211228,
)
from .vendor_direct_fulfillment_transactions_v1 import (
    VendorDirectFulfillmentTransactionsV1,
)


class VendorDirectFulfillmentTransactionsVersion(str, enum.Enum):
    V1 = "v1"
    V_2021_12_28 = "2021-12-28"
    LATEST = "2021-12-28"


if TYPE_CHECKING:

    class _VendorDirectFulfillmentTransactionsMeta(VersionedClientMeta):
        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[
                VendorDirectFulfillmentTransactionsVersion.V_2021_12_28,
                VendorDirectFulfillmentTransactionsVersion.LATEST,
                "2021-12-28",
            ],
            **kwargs: Any,
        ) -> VendorDirectFulfillmentTransactionsV20211228: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[VendorDirectFulfillmentTransactionsVersion.V1, "v1"],
            **kwargs: Any,
        ) -> VendorDirectFulfillmentTransactionsV1: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> VendorDirectFulfillmentTransactionsV1: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: str | VendorDirectFulfillmentTransactionsVersion,
            **kwargs: Any,
        ) -> Client: ...


else:
    _VendorDirectFulfillmentTransactionsMeta = VersionedClientMeta


class VendorDirectFulfillmentTransactions(
    Client, metaclass=_VendorDirectFulfillmentTransactionsMeta
):
    """Vendor Direct Fulfillment Transactions API client.

    This class dispatches to a versioned Vendor Direct Fulfillment Transactions API client.

    If you do not pass a version, the constructor returns the oldest supported implementation ("v1").
    """

    if TYPE_CHECKING:
        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[
                VendorDirectFulfillmentTransactionsVersion.V_2021_12_28,
                VendorDirectFulfillmentTransactionsVersion.LATEST,
                "2021-12-28",
            ],
            **kwargs: Any,
        ) -> VendorDirectFulfillmentTransactionsV20211228: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[VendorDirectFulfillmentTransactionsVersion.V1, "v1"],
            **kwargs: Any,
        ) -> VendorDirectFulfillmentTransactionsV1: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> VendorDirectFulfillmentTransactionsV1: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: str | VendorDirectFulfillmentTransactionsVersion,
            **kwargs: Any,
        ) -> Client: ...

    _DISPATCH = True

    _DEFAULT_VERSION = "v1"

    _VERSION_MAP = {
        "v1": VendorDirectFulfillmentTransactionsV1,
        "2021-12-28": VendorDirectFulfillmentTransactionsV20211228,
    }

    _VERSION_ALIASES = {
        "v1": "v1",
        "2021-12-28": "2021-12-28",
    }
