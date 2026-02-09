from typing import TYPE_CHECKING

from .base_client import BaseClient
from .helpers import (
    fill_query_params,
    sp_endpoint,
    create_md5,
    nest_dict,
    _nest_dict_rec,
    deprecated,
)
from .marketplaces import Marketplaces
from .exceptions import SellingApiException
from .exceptions import SellingApiBadRequestException
from .exceptions import SellingApiNotFoundException
from .exceptions import SellingApiForbiddenException
from .exceptions import SellingApiRequestThrottledException
from .exceptions import SellingApiServerException
from .exceptions import SellingApiTemporarilyUnavailableException
from .exceptions import SellingApiTooLargeException
from .exceptions import SellingApiStateConflictException
from .exceptions import SellingApiUnsupportedFormatException
from .schedules import Schedules
from .report_status import ReportStatus
from .sales_enum import FirstDayOfWeek, Granularity, BuyerType
from .fulfillment_channel import FulfillmentChannel
from .identifiersType import IdentifiersType
from .InventoryEnums import InventoryGranularity
from .included_data import (
    IncludedData,
    ListingItemsIncludedData,
    CatalogItemsIncludedData,
)
from .notifications import NotificationType
from .credential_provider import CredentialProvider, MissingCredentials
from .ApiResponse import ApiResponse
from .processing_status import ProcessingStatus
from .reportTypes import ReportType
from .feedTypes import FeedType
from sp_api.base.inegibility_reasons import IneligibilityReasonList
from .marketplaces import AwsEnv

if TYPE_CHECKING:
    from .client import Client
    from sp_api.auth import AccessTokenClient, Credentials
    from sp_api.auth.exceptions import AuthorizationError


__all__ = [
    "Credentials",
    "AuthorizationError",
    "AccessTokenClient",
    "ReportType",
    "FeedType",
    "FeedTypes",
    "ProcessingStatus",
    "ApiResponse",
    "Client",
    "BaseClient",
    "Marketplaces",
    "fill_query_params",
    "sp_endpoint",
    "SellingApiException",
    "SellingApiBadRequestException",
    "SellingApiNotFoundException",
    "SellingApiServerException",
    "SellingApiForbiddenException",
    "SellingApiBadRequestException",
    "SellingApiRequestThrottledException",
    "SellingApiTemporarilyUnavailableException",
    "SellingApiTooLargeException",
    "SellingApiStateConflictException",
    "SellingApiUnsupportedFormatException",
    "Schedules",
    "ReportStatus",
    "FirstDayOfWeek",
    "Granularity",
    "BuyerType",
    "FulfillmentChannel",
    "FulfillmentChannels",
    "IdentifiersType",
    "InventoryGranularity",
    "deprecated",
    "NotificationType",
    "CredentialProvider",
    "MissingCredentials",
    "nest_dict",
    "_nest_dict_rec",
    "IneligibilityReasonList",
    "IncludedData",
    "ListingItemsIncludedData",
    "CatalogItemsIncludedData",
    "AwsEnv",
]

# Backward-compatibility aliases for docs and legacy imports.
FeedTypes = FeedType
FulfillmentChannels = FulfillmentChannel


def __getattr__(name):
    if name == "Client":
        from .client import Client

        globals()[name] = Client
        return Client
    if name in {"AccessTokenClient", "Credentials"}:
        from sp_api.auth import AccessTokenClient, Credentials

        exports = {"AccessTokenClient": AccessTokenClient, "Credentials": Credentials}
        globals()[name] = exports[name]
        return exports[name]
    if name == "AuthorizationError":
        from sp_api.auth.exceptions import AuthorizationError

        globals()[name] = AuthorizationError
        return AuthorizationError
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
