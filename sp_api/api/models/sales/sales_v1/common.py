"""
Common models generated from Swagger/OpenAPI specification.

This file was auto-generated. Do not edit manually.

"""

from datetime import date, datetime
from enum import Enum, auto
from typing import Annotated, Any, Dict, List, Optional, Union
from uuid import UUID

from pydantic import AliasChoices, BaseModel, ConfigDict, Field

from .base_models import (BodyParam, GetRequestSerializer, PathParam,
                          QueryParam, RequestsBaseModel, SpApiBaseModel)

Decimal = str
"""A decimal number with no loss of precision. Useful when precision loss is unnaceptable, as with currencies. Follows RFC7159 for number representation."""


"""
Error

Error response returned when the request is unsuccessful.
"""


class Error(SpApiBaseModel):
    """Error response returned when the request is unsuccessful."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    code: Annotated[
        str,
        Field(
            ...,
            description="An error code that identifies the type of error that occured.",
        ),
    ]

    message: Annotated[
        str,
        Field(
            ...,
            description="A message that describes the error condition in a human-readable form.",
        ),
    ]

    details: Annotated[
        Optional[str],
        Field(
            None,
            description="Additional details that can help the caller understand or fix the issue.",
        ),
    ]


ErrorList = List["Error"]
"""A list of error responses returned when a request is unsuccessful."""


# Enum definitions
class GetOrderMetricsRequestGranularityEnum(str, Enum):
    """Enum for granularity"""

    HOUR = "Hour"  # Hour
    DAY = "Day"  # Day
    WEEK = "Week"  # Week
    MONTH = "Month"  # Month
    YEAR = "Year"  # Year
    TOTAL = "Total"  # Total


class GetOrderMetricsRequestBuyerTypeEnum(str, Enum):
    """Enum for buyerType"""

    B2_B = "B2B"  # Business to business.
    B2_C = "B2C"  # Business to customer.
    ALL = "All"  # Business to business and business to customer.


class GetOrderMetricsRequestFirstDayOfWeekEnum(str, Enum):
    """Enum for firstDayOfWeek"""

    MONDAY = "Monday"  # Monday
    SUNDAY = "Sunday"  # Sunday


class GetOrderMetricsRequestAmazonProgramEnum(str, Enum):
    """Enum for amazonProgram"""

    AMAZON_HAUL = "AmazonHaul"  # Amazon Haul sales


"""
GetOrderMetricsRequest

Request parameters for getOrderMetrics
"""


class GetOrderMetricsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getOrderMetrics
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.  For example, ATVPDKIKX0DER indicates the US marketplace.",
        ),
    ]

    interval: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            description="[QUERY] A time interval used for selecting order metrics. This takes the form of two dates separated by two hyphens (first date is inclusive; second date is exclusive). Dates are in ISO8601 format and must represent absolute time (either Z notation or offset notation). Example: 2018-09-01T00:00:00-07:00--2018-09-04T00:00:00-07:00 requests order metrics for Sept 1st, 2nd and 3rd in the -07:00 zone.",
        ),
    ]

    granularity_time_zone: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "granularityTimeZone", "granularity_time_zone"
            ),
            serialization_alias="granularityTimeZone",
            description="[QUERY] An IANA-compatible time zone for determining the day boundary. Required when specifying a granularity value greater than Hour. The granularityTimeZone value must align with the offset of the specified interval value. For example, if the interval value uses Z notation, then granularityTimeZone must be UTC. If the interval value uses an offset, then granularityTimeZone must be an IANA-compatible time zone that matches the offset. Example: US/Pacific to compute day boundaries, accounting for daylight time savings, for US/Pacific zone.",
        ),
    ]

    granularity: Annotated[
        GetOrderMetricsRequestGranularityEnum,
        QueryParam(),
        Field(
            ...,
            description="[QUERY] The granularity of the grouping of order metrics, based on a unit of time. Specifying granularity=Hour results in a successful request only if the interval specified is less than or equal to 30 days from now. For all other granularities, the interval specified must be less or equal to 2 years from now. Specifying granularity=Total results in order metrics that are aggregated over the entire interval that you specify. If the interval start and end date don’t align with the specified granularity, the head and tail end of the response interval will contain partial data. Example: Day to get a daily breakdown of the request interval, where the day boundary is defined by the granularityTimeZone.",
        ),
    ]

    buyer_type: Annotated[
        Optional[GetOrderMetricsRequestBuyerTypeEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("buyerType", "buyer_type"),
            serialization_alias="buyerType",
            description="[QUERY] Filters the results by the buyer type that you specify, B2B (business to business) or B2C (business to customer). Example: B2B, if you want the response to include order metrics for only B2B buyers.",
        ),
    ]

    fulfillment_network: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("fulfillmentNetwork", "fulfillment_network"),
            serialization_alias="fulfillmentNetwork",
            description="[QUERY] Filters the results by the fulfillment network that you specify, MFN (merchant fulfillment network) or AFN (Amazon fulfillment network). Do not include this filter if you want the response to include order metrics for all fulfillment networks. Example: AFN, if you want the response to include order metrics for only Amazon fulfillment network.",
        ),
    ]

    first_day_of_week: Annotated[
        Optional[GetOrderMetricsRequestFirstDayOfWeekEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("firstDayOfWeek", "first_day_of_week"),
            serialization_alias="firstDayOfWeek",
            description="[QUERY] Specifies the day that the week starts on when granularity=Week, either Monday or Sunday. Default: Monday. Example: Sunday, if you want the week to start on a Sunday.",
        ),
    ]

    asin: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            description="[QUERY] Filters the results by the ASIN that you specify. Specifying both ASIN and SKU returns an error. Do not include this filter if you want the response to include order metrics for all ASINs. Example: B0792R1RSN, if you want the response to include order metrics for only ASIN B0792R1RSN.",
        ),
    ]

    sku: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            description="[QUERY] Filters the results by the SKU that you specify. Specifying both ASIN and SKU returns an error. Do not include this filter if you want the response to include order metrics for all SKUs. Example: TestSKU, if you want the response to include order metrics for only SKU TestSKU.",
        ),
    ]

    amazon_program: Annotated[
        Optional[GetOrderMetricsRequestAmazonProgramEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("amazonProgram", "amazon_program"),
            serialization_alias="amazonProgram",
            description="[QUERY] Filters the results by the Amazon program that you specify. Do not include this filter if you want the response to include order metrics for all programs. **Example:** `AmazonHaul` returns order metrics for the Amazon Haul program only.",
        ),
    ]


OrderMetricsList = List["OrderMetricsInterval"]
"""A set of order metrics, each scoped to a particular time interval."""


"""
GetOrderMetricsResponse

The response schema for the getOrderMetrics operation.
"""


class GetOrderMetricsResponse(SpApiBaseModel):
    """The response schema for the getOrderMetrics operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["OrderMetricsList"],
        Field(None, description="The payload for the getOrderMetrics operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None, description="Encountered errors for the getOrderMetrics operation."
        ),
    ]


"""
Money

The currency type and the amount.
"""


class Money(SpApiBaseModel):
    """The currency type and the amount."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    currency_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("currencyCode", "currency_code"),
            serialization_alias="currencyCode",
            description="Three-digit currency code. In ISO 4217 format.",
        ),
    ]

    amount: Annotated["Decimal", Field(..., description="The currency amount.")]


"""
OrderMetricsInterval

Contains order metrics.
"""


class OrderMetricsInterval(SpApiBaseModel):
    """Contains order metrics."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    interval: Annotated[
        str,
        Field(
            ...,
            description="The interval of time based on requested granularity (ex. Hour, Day, etc.) If this is the first or the last interval from the list, it might contain incomplete data if the requested interval doesn't align with the requested granularity (ex. request interval 2018-09-01T02:00:00Z--2018-09-04T19:00:00Z and granularity day will result in Sept 1st UTC day and Sept 4th UTC days having partial data).",
        ),
    ]

    unit_count: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("unitCount", "unit_count"),
            serialization_alias="unitCount",
            description="The number of units in orders based on the specified filters.",
        ),
    ]

    order_item_count: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("orderItemCount", "order_item_count"),
            serialization_alias="orderItemCount",
            description="The number of order items based on the specified filters.",
        ),
    ]

    order_count: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("orderCount", "order_count"),
            serialization_alias="orderCount",
            description="The number of orders based on the specified filters.",
        ),
    ]

    average_unit_price: Annotated[
        "Money",
        Field(
            ...,
            validation_alias=AliasChoices("averageUnitPrice", "average_unit_price"),
            serialization_alias="averageUnitPrice",
            description="The average price for an item based on the specified filters. Formula is totalSales/unitCount.",
        ),
    ]

    total_sales: Annotated[
        "Money",
        Field(
            ...,
            validation_alias=AliasChoices("totalSales", "total_sales"),
            serialization_alias="totalSales",
            description="The total ordered product sales for all orders based on the specified filters.",
        ),
    ]


# Rebuild models to resolve forward references
GetOrderMetricsResponse.model_rebuild()
OrderMetricsInterval.model_rebuild()
Error.model_rebuild()
Money.model_rebuild()
GetOrderMetricsRequest.model_rebuild()
