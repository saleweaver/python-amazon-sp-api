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

AggregationFrequency = str
"""The time period used to group data in the response. Note that this is only valid for the `PERFORMANCE` time period type."""


AutoEnrollmentPreference = str
"""The auto-enrollment preference indicates whether the offer is opted-in to or opted-out of Amazon's auto-enrollment feature."""


"""
DiscountFunding

The discount funding on the offer.
"""


class DiscountFunding(SpApiBaseModel):
    """The discount funding on the offer."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    percentage: Annotated[
        Optional[List["float"]],
        Field(
            None,
            description="Filters the results to only include offers with the percentage specified.",
        ),
    ]


EligibilityStatus = str
"""The current eligibility status of an offer."""


EnrollmentMethod = str
"""The enrollment method used to enroll the offer into the program."""


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
            description="An error code that identifies the type of error that occurred.",
        ),
    ]

    message: Annotated[
        str, Field(..., description="A message that describes the error condition.")
    ]

    details: Annotated[
        Optional[str],
        Field(
            None,
            description="Additional details that can help the caller understand or fix the issue.",
        ),
    ]


"""
ErrorList

A list of error responses returned when a request is unsuccessful.
"""


class ErrorList(SpApiBaseModel):
    """A list of error responses returned when a request is unsuccessful."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        List["Error"],
        Field(
            ...,
            description="A list of error responses returned when a request is unsuccessful.",
        ),
    ]


MarketplaceId = str
"""The marketplace identifier. The supported marketplaces for both sellers and vendors are US, CA, ES, UK, FR, IT, IN, DE and JP. The supported marketplaces for vendors only are BR, AU, MX, AE and NL. Refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids) to find the identifier for the marketplace."""


Metric = str
"""The metric name and description."""


ProgramTypes = List["ProgramType"]
"""A list of replenishment program types."""


"""
TimeInterval

A date-time interval in ISO 8601 format which is used to compute metrics. Only the date is required, but you must pass the complete date and time value. For example, November 11, 2022 should be passed as '2022-11-07T00:00:00Z'. Note that only data for the trailing 2 years is supported. **Note**: The `listOfferMetrics` operation only supports a time interval which covers a single unit of the aggregation frequency. For example, for a MONTH aggregation frequency, the duration of the interval between the startDate and endDate can not be more than 1 month.
"""


class TimeInterval(SpApiBaseModel):
    """A date-time interval in ISO 8601 format which is used to compute metrics. Only the date is required, but you must pass the complete date and time value. For example, November 11, 2022 should be passed as '2022-11-07T00:00:00Z'. Note that only data for the trailing 2 years is supported. **Note**: The `listOfferMetrics` operation only supports a time interval which covers a single unit of the aggregation frequency. For example, for a MONTH aggregation frequency, the duration of the interval between the startDate and endDate can not be more than 1 month."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    start_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("startDate", "start_date"),
            serialization_alias="startDate",
            description="When this object is used as a request parameter, the specified `startDate` is adjusted based on the aggregation frequency. * For `WEEK` the metric is computed from the first day of the week (Sunday, based on ISO 8601) that contains the `startDate`. * For `MONTH` the metric is computed from the first day of the month that contains the `startDate`. * For `QUARTER` the metric is computed from the first day of the quarter that contains the `startDate`. * For `YEAR` the metric is computed from the first day of the year that contains the `startDate`.",
        ),
    ]

    end_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("endDate", "end_date"),
            serialization_alias="endDate",
            description="When this object is used as a request parameter, the specified `endDate` is adjusted based on the aggregation frequency. * For `WEEK` the metric is computed up to the last day of the week (Sunday, based on ISO 8601) that contains the `endDate`. * For `MONTH`, the metric is computed up to the last day that contains the `endDate`. * For `QUARTER` the metric is computed up to the last day of the quarter that contains the `endDate`. * For `YEAR` the metric is computed up to the last day of the year that contains the `endDate`. Note: The end date may be adjusted to a lower value based on the data available in our system.",
        ),
    ]


TimePeriodType = str
"""The time period type that determines whether the metrics requested are backward-looking (performance) or forward-looking (forecast)."""


"""
GetSellingPartnerMetricsRequestBody

The request body for the `getSellingPartnerMetrics` operation.
"""


class GetSellingPartnerMetricsRequestBody(SpApiBaseModel):
    """The request body for the `getSellingPartnerMetrics` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    aggregation_frequency: Annotated[
        Optional["AggregationFrequency"],
        Field(
            None,
            validation_alias=AliasChoices(
                "aggregationFrequency", "aggregation_frequency"
            ),
            serialization_alias="aggregationFrequency",
        ),
    ]

    time_interval: Annotated[
        "TimeInterval",
        Field(
            ...,
            validation_alias=AliasChoices("timeInterval", "time_interval"),
            serialization_alias="timeInterval",
            description="A time interval used to compute metrics.",
        ),
    ]

    metrics: Annotated[
        Optional[List["Metric"]],
        Field(
            None,
            description="The list of metrics requested. If no metric value is provided, data for all of the metrics will be returned.",
        ),
    ]

    time_period_type: Annotated[
        "TimePeriodType",
        Field(
            ...,
            validation_alias=AliasChoices("timePeriodType", "time_period_type"),
            serialization_alias="timePeriodType",
        ),
    ]

    marketplace_id: Annotated[
        Optional["MarketplaceId"],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The marketplace identifier. The supported marketplaces for both sellers and vendors are US, CA, ES, UK, FR, IT, IN, DE and JP. The supported marketplaces for vendors only are BR, AU, MX, AE and NL. Refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids) to find the identifier for the marketplace.",
        ),
    ]

    program_types: Annotated[
        "ProgramTypes",
        Field(
            ...,
            validation_alias=AliasChoices("programTypes", "program_types"),
            serialization_alias="programTypes",
            description="The list of replenishment program types for which to return metrics.",
        ),
    ]


"""
GetSellingPartnerMetricsRequest

Request parameters for getSellingPartnerMetrics
"""


class GetSellingPartnerMetricsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getSellingPartnerMetrics
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        Optional["GetSellingPartnerMetricsRequestBody"],
        BodyParam(),
        Field(
            None,
            description="[BODY] The request body for the `getSellingPartnerMetrics` operation.",
        ),
    ]


"""
GetSellingPartnerMetricsResponseMetric

An object which contains metric data for a selling partner.
"""


class GetSellingPartnerMetricsResponseMetric(SpApiBaseModel):
    """An object which contains metric data for a selling partner."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    not_delivered_due_to_o_o_s: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "notDeliveredDueToOOS", "not_delivered_due_to_o_o_s"
            ),
            serialization_alias="notDeliveredDueToOOS",
            description="The percentage of items that were not shipped out of the total shipped units over a period of time due to being out of stock. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    total_subscriptions_revenue: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "totalSubscriptionsRevenue", "total_subscriptions_revenue"
            ),
            serialization_alias="totalSubscriptionsRevenue",
            description="The revenue generated from subscriptions over a period of time. Applicable for both the PERFORMANCE and FORECAST timePeriodType.",
        ),
    ]

    shipped_subscription_units: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "shippedSubscriptionUnits", "shipped_subscription_units"
            ),
            serialization_alias="shippedSubscriptionUnits",
            description="The number of units shipped to the subscribers over a period of time. Applicable for both the PERFORMANCE and FORECAST timePeriodType.",
        ),
    ]

    active_subscriptions: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "activeSubscriptions", "active_subscriptions"
            ),
            serialization_alias="activeSubscriptions",
            description="The number of active subscriptions present at the end of the period. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    subscriber_average_revenue: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "subscriberAverageRevenue", "subscriber_average_revenue"
            ),
            serialization_alias="subscriberAverageRevenue",
            description="The average revenue per subscriber of the program over a period of past 12 months for sellers and 6 months for vendors. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    non_subscriber_average_revenue: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "nonSubscriberAverageRevenue", "non_subscriber_average_revenue"
            ),
            serialization_alias="nonSubscriberAverageRevenue",
            description="The average revenue per non-subscriber of the program over a period of past 12 months for sellers and 6 months for vendors. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    lost_revenue_due_to_o_o_s: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "lostRevenueDueToOOS", "lost_revenue_due_to_o_o_s"
            ),
            serialization_alias="lostRevenueDueToOOS",
            description="The revenue that would have been generated had there not been out of stock. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    subscriber_average_reorders: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "subscriberAverageReorders", "subscriber_average_reorders"
            ),
            serialization_alias="subscriberAverageReorders",
            description="The average reorders per subscriber of the program over a period of 12 months. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    non_subscriber_average_reorders: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "nonSubscriberAverageReorders", "non_subscriber_average_reorders"
            ),
            serialization_alias="nonSubscriberAverageReorders",
            description="The average reorders per non-subscriber of the program over a period of past 12 months. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    coupons_revenue_penetration: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "couponsRevenuePenetration", "coupons_revenue_penetration"
            ),
            serialization_alias="couponsRevenuePenetration",
            description="The percentage of revenue from ASINs with coupons out of total revenue from all ASINs. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    revenue_from_subscriptions_with_multiple_deliveries: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "revenueFromSubscriptionsWithMultipleDeliveries",
                "revenue_from_subscriptions_with_multiple_deliveries",
            ),
            serialization_alias="revenueFromSubscriptionsWithMultipleDeliveries",
            description="The subscription revenue generated from subscriptions with over two deliveries over the past 12 months. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    revenue_from_active_subscriptions_with_single_delivery: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "revenueFromActiveSubscriptionsWithSingleDelivery",
                "revenue_from_active_subscriptions_with_single_delivery",
            ),
            serialization_alias="revenueFromActiveSubscriptionsWithSingleDelivery",
            description="The subscription revenue generated from active subscriptions with one delivery over the past 12 months. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    revenue_from_cancelled_subscriptions_after_single_delivery: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "revenueFromCancelledSubscriptionsAfterSingleDelivery",
                "revenue_from_cancelled_subscriptions_after_single_delivery",
            ),
            serialization_alias="revenueFromCancelledSubscriptionsAfterSingleDelivery",
            description="The subscription revenue generated from subscriptions which are cancelled after one delivery over the past 12 months. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    subscriber_retention_for30_days: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "subscriberRetentionFor30Days", "subscriber_retention_for30_days"
            ),
            serialization_alias="subscriberRetentionFor30Days",
            description="The percentage of subscriptions retained after 30 days of subscription creation. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    subscriber_retention_for90_days: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "subscriberRetentionFor90Days", "subscriber_retention_for90_days"
            ),
            serialization_alias="subscriberRetentionFor90Days",
            description="The percentage of subscriptions retained after 90 days of subscription creation. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    revenue_penetration_for0_percent_seller_funding: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "revenuePenetrationFor0PercentSellerFunding",
                "revenue_penetration_for0_percent_seller_funding",
            ),
            serialization_alias="revenuePenetrationFor0PercentSellerFunding",
            description="The percentage of subscription revenue generated by offers with 0% seller-funded discount over the last 12 months. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    revenue_penetration_for5_percent_seller_funding: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "revenuePenetrationFor5PercentSellerFunding",
                "revenue_penetration_for5_percent_seller_funding",
            ),
            serialization_alias="revenuePenetrationFor5PercentSellerFunding",
            description="[Applicable only for Sellers] The percentage of subscription revenue generated by offers with 5% seller-funded discount over the last 12 months. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    revenue_penetration_for10_percent_seller_funding: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "revenuePenetrationFor10PercentSellerFunding",
                "revenue_penetration_for10_percent_seller_funding",
            ),
            serialization_alias="revenuePenetrationFor10PercentSellerFunding",
            description="[Applicable only for Sellers] The percentage of subscription revenue generated by offers with 10% seller-funded discount over the last 12 months. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    revenue_penetration_for5_plus_percent_seller_funding: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "revenuePenetrationFor5PlusPercentSellerFunding",
                "revenue_penetration_for5_plus_percent_seller_funding",
            ),
            serialization_alias="revenuePenetrationFor5PlusPercentSellerFunding",
            description="[Applicable only for vendors] The percentage of subscription revenue generated by offers with 5% or above seller-funded discount over the last 12 months. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    share_of_coupon_subscriptions: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "shareOfCouponSubscriptions", "share_of_coupon_subscriptions"
            ),
            serialization_alias="shareOfCouponSubscriptions",
            description="The percentage of new subscriptions acquired through coupons. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    time_interval: Annotated[
        Optional["TimeInterval"],
        Field(
            None,
            validation_alias=AliasChoices("timeInterval", "time_interval"),
            serialization_alias="timeInterval",
            description="A time interval used to compute metrics.",
        ),
    ]

    currency_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("currencyCode", "currency_code"),
            serialization_alias="currencyCode",
            description="The currency code in ISO 4217 format.",
        ),
    ]


"""
GetSellingPartnerMetricsResponse

The response schema for the `getSellingPartnerMetrics` operation.
"""


class GetSellingPartnerMetricsResponse(SpApiBaseModel):
    """The response schema for the `getSellingPartnerMetrics` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    metrics: Annotated[
        Optional[List["GetSellingPartnerMetricsResponseMetric"]],
        Field(None, description="A list of metrics data for the selling partner."),
    ]


"""
ListOfferMetricsRequestFilters

Use these parameters to filter results. Any result must match all provided parameters. For any parameter that is an array, the result must match at least one element in the provided array.
"""


class ListOfferMetricsRequestFilters(SpApiBaseModel):
    """Use these parameters to filter results. Any result must match all provided parameters. For any parameter that is an array, the result must match at least one element in the provided array."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    aggregation_frequency: Annotated[
        Optional["AggregationFrequency"],
        Field(
            None,
            validation_alias=AliasChoices(
                "aggregationFrequency", "aggregation_frequency"
            ),
            serialization_alias="aggregationFrequency",
        ),
    ]

    time_interval: Annotated[
        "TimeInterval",
        Field(
            ...,
            validation_alias=AliasChoices("timeInterval", "time_interval"),
            serialization_alias="timeInterval",
            description="A time interval used to compute metrics.",
        ),
    ]

    time_period_type: Annotated[
        "TimePeriodType",
        Field(
            ...,
            validation_alias=AliasChoices("timePeriodType", "time_period_type"),
            serialization_alias="timePeriodType",
        ),
    ]

    marketplace_id: Annotated[
        Optional["MarketplaceId"],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The marketplace identifier. The supported marketplaces for both sellers and vendors are US, CA, ES, UK, FR, IT, IN, DE and JP. The supported marketplaces for vendors only are BR, AU, MX, AE and NL. Refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids) to find the identifier for the marketplace.",
        ),
    ]

    program_types: Annotated[
        "ProgramTypes",
        Field(
            ...,
            validation_alias=AliasChoices("programTypes", "program_types"),
            serialization_alias="programTypes",
        ),
    ]

    asins: Annotated[
        Optional[List["str"]],
        Field(
            None,
            description="A list of Amazon Standard Identification Numbers (ASINs).",
        ),
    ]


"""
ListOfferMetricsRequestPagination

Use these parameters to paginate through the response.
"""


class ListOfferMetricsRequestPagination(SpApiBaseModel):
    """Use these parameters to paginate through the response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    limit: Annotated[
        int,
        Field(
            ..., description="The maximum number of results to return in the response."
        ),
    ]

    offset: Annotated[
        int,
        Field(
            ...,
            description="The offset from which to retrieve the number of results specified by the `limit` value. The first result is at offset 0.",
        ),
    ]


ListOfferMetricsSortKey = str
"""The attribute to use to sort the results."""


SortOrder = str
"""The sort order."""


"""
ListOfferMetricsRequestSort

Use these parameters to sort the response.
"""


class ListOfferMetricsRequestSort(SpApiBaseModel):
    """Use these parameters to sort the response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    order: Annotated["SortOrder", Field(..., description="The sort order.")]

    key: Annotated[
        "ListOfferMetricsSortKey",
        Field(
            ...,
        ),
    ]


"""
ListOfferMetricsRequestBody

The request body for the `listOfferMetrics` operation.
"""


class ListOfferMetricsRequestBody(SpApiBaseModel):
    """The request body for the `listOfferMetrics` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    pagination: Annotated[
        "ListOfferMetricsRequestPagination",
        Field(
            ..., description="Use these parameters to paginate through the response."
        ),
    ]

    sort: Annotated[
        Optional["ListOfferMetricsRequestSort"],
        Field(None, description="Use these parameters to sort the response."),
    ]

    filters: Annotated[
        "ListOfferMetricsRequestFilters",
        Field(
            ...,
            description="Use these parameters to filter results. Any result must match all provided parameters. For any parameter that is an array, the result must match at least one element in the provided array.",
        ),
    ]


"""
ListOfferMetricsRequest

Request parameters for listOfferMetrics
"""


class ListOfferMetricsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listOfferMetrics
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        Optional["ListOfferMetricsRequestBody"],
        BodyParam(),
        Field(
            None,
            description="[BODY] The request body for the `listOfferMetrics` operation.",
        ),
    ]


"""
ListOfferMetricsResponseOffer

An object which contains offer metrics.
"""


class ListOfferMetricsResponseOffer(SpApiBaseModel):
    """An object which contains offer metrics."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    asin: Annotated[
        Optional[str],
        Field(None, description="The Amazon Standard Identification Number (ASIN)."),
    ]

    not_delivered_due_to_o_o_s: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "notDeliveredDueToOOS", "not_delivered_due_to_o_o_s"
            ),
            serialization_alias="notDeliveredDueToOOS",
            description="The percentage of items that were not shipped out of the total shipped units over a period of time due to being out of stock. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    total_subscriptions_revenue: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "totalSubscriptionsRevenue", "total_subscriptions_revenue"
            ),
            serialization_alias="totalSubscriptionsRevenue",
            description="The revenue generated from subscriptions over a period of time. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    shipped_subscription_units: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "shippedSubscriptionUnits", "shipped_subscription_units"
            ),
            serialization_alias="shippedSubscriptionUnits",
            description="The number of units shipped to the subscribers over a period of time. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    active_subscriptions: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "activeSubscriptions", "active_subscriptions"
            ),
            serialization_alias="activeSubscriptions",
            description="The number of active subscriptions present at the end of the period. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    revenue_penetration: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices("revenuePenetration", "revenue_penetration"),
            serialization_alias="revenuePenetration",
            description="The percentage of total program revenue out of total product revenue. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    lost_revenue_due_to_o_o_s: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "lostRevenueDueToOOS", "lost_revenue_due_to_o_o_s"
            ),
            serialization_alias="lostRevenueDueToOOS",
            description="The revenue that would have been generated had there not been out of stock. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    coupons_revenue_penetration: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "couponsRevenuePenetration", "coupons_revenue_penetration"
            ),
            serialization_alias="couponsRevenuePenetration",
            description="The percentage of revenue from ASINs with coupons out of total revenue from all ASINs. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    share_of_coupon_subscriptions: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "shareOfCouponSubscriptions", "share_of_coupon_subscriptions"
            ),
            serialization_alias="shareOfCouponSubscriptions",
            description="The percentage of new subscriptions acquired through coupons. Applicable to PERFORMANCE timePeriodType.",
        ),
    ]

    next30_day_total_subscriptions_revenue: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "next30DayTotalSubscriptionsRevenue",
                "next30_day_total_subscriptions_revenue",
            ),
            serialization_alias="next30DayTotalSubscriptionsRevenue",
            description="The forecasted total subscription revenue for the next 30 days. Applicable to FORECAST timePeriodType.",
        ),
    ]

    next60_day_total_subscriptions_revenue: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "next60DayTotalSubscriptionsRevenue",
                "next60_day_total_subscriptions_revenue",
            ),
            serialization_alias="next60DayTotalSubscriptionsRevenue",
            description="The forecasted total subscription revenue for the next 60 days. Applicable to FORECAST timePeriodType.",
        ),
    ]

    next90_day_total_subscriptions_revenue: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "next90DayTotalSubscriptionsRevenue",
                "next90_day_total_subscriptions_revenue",
            ),
            serialization_alias="next90DayTotalSubscriptionsRevenue",
            description="The forecasted total subscription revenue for the next 90 days. Applicable to FORECAST timePeriodType.",
        ),
    ]

    next30_day_shipped_subscription_units: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "next30DayShippedSubscriptionUnits",
                "next30_day_shipped_subscription_units",
            ),
            serialization_alias="next30DayShippedSubscriptionUnits",
            description="The forecasted shipped subscription units for the next 30 days. Applicable to FORECAST timePeriodType.",
        ),
    ]

    next60_day_shipped_subscription_units: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "next60DayShippedSubscriptionUnits",
                "next60_day_shipped_subscription_units",
            ),
            serialization_alias="next60DayShippedSubscriptionUnits",
            description="The forecasted shipped subscription units for the next 60 days. Applicable to FORECAST timePeriodType.",
        ),
    ]

    next90_day_shipped_subscription_units: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "next90DayShippedSubscriptionUnits",
                "next90_day_shipped_subscription_units",
            ),
            serialization_alias="next90DayShippedSubscriptionUnits",
            description="The forecasted shipped subscription units for the next 90 days. Applicable to FORECAST timePeriodType.",
        ),
    ]

    time_interval: Annotated[
        Optional["TimeInterval"],
        Field(
            None,
            validation_alias=AliasChoices("timeInterval", "time_interval"),
            serialization_alias="timeInterval",
            description="A time interval used to compute metrics.",
        ),
    ]

    currency_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("currencyCode", "currency_code"),
            serialization_alias="currencyCode",
            description="The currency code in ISO 4217 format.",
        ),
    ]


"""
PaginationResponse

Use these parameters to paginate through the response.
"""


class PaginationResponse(SpApiBaseModel):
    """Use these parameters to paginate through the response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    total_results: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("totalResults", "total_results"),
            serialization_alias="totalResults",
            description="Total number of results matching the given filter criteria.",
        ),
    ]


"""
ListOfferMetricsResponse

The response schema for the `listOfferMetrics` operation.
"""


class ListOfferMetricsResponse(SpApiBaseModel):
    """The response schema for the `listOfferMetrics` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    offers: Annotated[
        Optional[List["ListOfferMetricsResponseOffer"]],
        Field(None, description="A list of offers and associated metrics."),
    ]

    pagination: Annotated[
        Optional["PaginationResponse"],
        Field(
            None, description="Use these parameters to paginate through the response."
        ),
    ]


"""
Preference

Offer preferences that you can include in the result filter criteria.
"""


class Preference(SpApiBaseModel):
    """Offer preferences that you can include in the result filter criteria."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    auto_enrollment: Annotated[
        Optional[List["AutoEnrollmentPreference"]],
        Field(
            None,
            validation_alias=AliasChoices("autoEnrollment", "auto_enrollment"),
            serialization_alias="autoEnrollment",
            description="Filters the results to only include offers with the auto-enrollment preference specified.",
        ),
    ]


"""
Promotion

Offer promotions to include in the result filter criteria.
"""


class Promotion(SpApiBaseModel):
    """Offer promotions to include in the result filter criteria."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    selling_partner_funded_base_discount: Annotated[
        Optional["DiscountFunding"],
        Field(
            None,
            validation_alias=AliasChoices(
                "sellingPartnerFundedBaseDiscount",
                "selling_partner_funded_base_discount",
            ),
            serialization_alias="sellingPartnerFundedBaseDiscount",
            description="A base discount set by the selling partner on the offer.",
        ),
    ]

    selling_partner_funded_tiered_discount: Annotated[
        Optional["DiscountFunding"],
        Field(
            None,
            validation_alias=AliasChoices(
                "sellingPartnerFundedTieredDiscount",
                "selling_partner_funded_tiered_discount",
            ),
            serialization_alias="sellingPartnerFundedTieredDiscount",
            description="A tiered discount set by the selling partner on the offer.",
        ),
    ]

    amazon_funded_base_discount: Annotated[
        Optional["DiscountFunding"],
        Field(
            None,
            validation_alias=AliasChoices(
                "amazonFundedBaseDiscount", "amazon_funded_base_discount"
            ),
            serialization_alias="amazonFundedBaseDiscount",
            description="A base discount set by Amazon on the offer.",
        ),
    ]

    amazon_funded_tiered_discount: Annotated[
        Optional["DiscountFunding"],
        Field(
            None,
            validation_alias=AliasChoices(
                "amazonFundedTieredDiscount", "amazon_funded_tiered_discount"
            ),
            serialization_alias="amazonFundedTieredDiscount",
            description="A tiered discount set by Amazon on the offer.",
        ),
    ]


"""
ListOffersRequestFilters

Use these parameters to filter results. Any result must match all of the provided parameters. For any parameter that is an array, the result must match at least one element in the provided array.
"""


class ListOffersRequestFilters(SpApiBaseModel):
    """Use these parameters to filter results. Any result must match all of the provided parameters. For any parameter that is an array, the result must match at least one element in the provided array."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional["MarketplaceId"],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The marketplace identifier. The supported marketplaces for both sellers and vendors are US, CA, ES, UK, FR, IT, IN, DE and JP. The supported marketplaces for vendors only are BR, AU, MX, AE and NL. Refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids) to find the identifier for the marketplace.",
        ),
    ]

    skus: Annotated[
        Optional[List["str"]],
        Field(
            None,
            description="A list of SKUs to filter. This filter is only supported for sellers and not for vendors.",
        ),
    ]

    asins: Annotated[
        Optional[List["str"]],
        Field(
            None,
            description="A list of Amazon Standard Identification Numbers (ASINs).",
        ),
    ]

    eligibilities: Annotated[
        Optional[List["EligibilityStatus"]],
        Field(None, description="A list of eligibilities associated with an offer."),
    ]

    preferences: Annotated[
        Optional["Preference"],
        Field(
            None,
            description="Offer preferences to include in the result filter criteria.",
        ),
    ]

    promotions: Annotated[
        Optional["Promotion"],
        Field(
            None,
            description="Offer promotions to include in the result filter criteria.",
        ),
    ]

    program_types: Annotated[
        "ProgramTypes",
        Field(
            ...,
            validation_alias=AliasChoices("programTypes", "program_types"),
            serialization_alias="programTypes",
        ),
    ]


"""
ListOffersRequestPagination

Use these parameters to paginate through the response.
"""


class ListOffersRequestPagination(SpApiBaseModel):
    """Use these parameters to paginate through the response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    limit: Annotated[
        int,
        Field(
            ..., description="The maximum number of results to return in the response."
        ),
    ]

    offset: Annotated[
        int,
        Field(
            ...,
            description="The offset from which to retrieve the number of results specified by the `limit` value. The first result is at offset 0.",
        ),
    ]


ListOffersSortKey = str
"""The attribute to use to sort the results."""


"""
ListOffersRequestSort

Use these parameters to sort the response.
"""


class ListOffersRequestSort(SpApiBaseModel):
    """Use these parameters to sort the response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    order: Annotated["SortOrder", Field(..., description="The sort order.")]

    key: Annotated[
        "ListOffersSortKey",
        Field(..., description="The attribute to use to sort the results."),
    ]


"""
ListOffersRequestBody

The request body for the `listOffers` operation.
"""


class ListOffersRequestBody(SpApiBaseModel):
    """The request body for the `listOffers` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    pagination: Annotated[
        "ListOffersRequestPagination",
        Field(
            ..., description="Use these parameters to paginate through the response."
        ),
    ]

    filters: Annotated[
        "ListOffersRequestFilters",
        Field(
            ...,
            description="Use these parameters to filter results. Any result must match all provided parameters. For any parameter that is an array, the result must match at least one element in the provided array.",
        ),
    ]

    sort: Annotated[
        Optional["ListOffersRequestSort"],
        Field(None, description="Use these parameters to sort the response."),
    ]


"""
ListOffersRequest

Request parameters for listOffers
"""


class ListOffersRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listOffers
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        Optional["ListOffersRequestBody"],
        BodyParam(),
        Field(
            None, description="[BODY] The request body for the `listOffers` operation."
        ),
    ]


"""
OfferProgramConfigurationPreferences

An object which contains the preferences applied to the offer.
"""


class OfferProgramConfigurationPreferences(SpApiBaseModel):
    """An object which contains the preferences applied to the offer."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    auto_enrollment: Annotated[
        Optional["AutoEnrollmentPreference"],
        Field(
            None,
            validation_alias=AliasChoices("autoEnrollment", "auto_enrollment"),
            serialization_alias="autoEnrollment",
            description="The auto-enrollment preference indicates whether the offer is opted-in to or opted-out of Amazon's auto-enrollment feature.",
        ),
    ]


"""
OfferProgramConfigurationPromotionsDiscountFunding

A promotional percentage discount applied to the offer.
"""


class OfferProgramConfigurationPromotionsDiscountFunding(SpApiBaseModel):
    """A promotional percentage discount applied to the offer."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    percentage: Annotated[
        Optional[float],
        Field(None, description="The percentage discount on the offer."),
    ]


"""
OfferProgramConfigurationPromotions

An object which represents all promotions applied to an offer.
"""


class OfferProgramConfigurationPromotions(SpApiBaseModel):
    """An object which represents all promotions applied to an offer."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    selling_partner_funded_base_discount: Annotated[
        Optional["OfferProgramConfigurationPromotionsDiscountFunding"],
        Field(
            None,
            validation_alias=AliasChoices(
                "sellingPartnerFundedBaseDiscount",
                "selling_partner_funded_base_discount",
            ),
            serialization_alias="sellingPartnerFundedBaseDiscount",
            description="A base discount set by the selling partner on the offer.",
        ),
    ]

    selling_partner_funded_tiered_discount: Annotated[
        Optional["OfferProgramConfigurationPromotionsDiscountFunding"],
        Field(
            None,
            validation_alias=AliasChoices(
                "sellingPartnerFundedTieredDiscount",
                "selling_partner_funded_tiered_discount",
            ),
            serialization_alias="sellingPartnerFundedTieredDiscount",
            description="A tiered discount set by the selling partner on the offer.",
        ),
    ]

    amazon_funded_base_discount: Annotated[
        Optional["OfferProgramConfigurationPromotionsDiscountFunding"],
        Field(
            None,
            validation_alias=AliasChoices(
                "amazonFundedBaseDiscount", "amazon_funded_base_discount"
            ),
            serialization_alias="amazonFundedBaseDiscount",
            description="A base discount set by Amazon on the offer.",
        ),
    ]

    amazon_funded_tiered_discount: Annotated[
        Optional["OfferProgramConfigurationPromotionsDiscountFunding"],
        Field(
            None,
            validation_alias=AliasChoices(
                "amazonFundedTieredDiscount", "amazon_funded_tiered_discount"
            ),
            serialization_alias="amazonFundedTieredDiscount",
            description="A tiered discount set by Amazon on the offer.",
        ),
    ]


"""
OfferProgramConfiguration

The offer program configuration contains a set of program properties for an offer.
"""


class OfferProgramConfiguration(SpApiBaseModel):
    """The offer program configuration contains a set of program properties for an offer."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    preferences: Annotated[
        Optional["OfferProgramConfigurationPreferences"],
        Field(
            None,
            description="An object which contains the preferences applied to the offer.",
        ),
    ]

    promotions: Annotated[
        Optional["OfferProgramConfigurationPromotions"],
        Field(
            None,
            description="An object which contains the promotions applied to the offer.",
        ),
    ]

    enrollment_method: Annotated[
        Optional["EnrollmentMethod"],
        Field(
            None,
            validation_alias=AliasChoices("enrollmentMethod", "enrollment_method"),
            serialization_alias="enrollmentMethod",
            description="Determines whether the offer was automatically or manually enrolled in the program. This property is only supported for sellers and not vendors.",
        ),
    ]


ProgramType = str
"""The replenishment program type."""


"""
ListOffersResponseOffer

An object which contains details about an offer.
"""


class ListOffersResponseOffer(SpApiBaseModel):
    """An object which contains details about an offer."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    sku: Annotated[
        Optional[str],
        Field(
            None,
            description="The SKU. This property is only supported for sellers and not for vendors.",
        ),
    ]

    asin: Annotated[
        Optional[str],
        Field(None, description="The Amazon Standard Identification Number (ASIN)."),
    ]

    marketplace_id: Annotated[
        Optional["MarketplaceId"],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The marketplace identifier. The supported marketplaces for both sellers and vendors are US, CA, ES, UK, FR, IT, IN, DE and JP. The supported marketplaces for vendors only are BR, AU, MX, AE and NL. Refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids) to find the identifier for the marketplace.",
        ),
    ]

    eligibility: Annotated[
        Optional["EligibilityStatus"],
        Field(None, description="The offer eligibility status."),
    ]

    offer_program_configuration: Annotated[
        Optional["OfferProgramConfiguration"],
        Field(
            None,
            validation_alias=AliasChoices(
                "offerProgramConfiguration", "offer_program_configuration"
            ),
            serialization_alias="offerProgramConfiguration",
        ),
    ]

    program_type: Annotated[
        Optional["ProgramType"],
        Field(
            None,
            validation_alias=AliasChoices("programType", "program_type"),
            serialization_alias="programType",
            description="The replenishment program for the offer.",
        ),
    ]

    vendor_codes: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("vendorCodes", "vendor_codes"),
            serialization_alias="vendorCodes",
            description="A list of vendor codes associated with the offer.",
        ),
    ]


"""
ListOffersResponse

The response schema for the `listOffers` operation.
"""


class ListOffersResponse(SpApiBaseModel):
    """The response schema for the `listOffers` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    offers: Annotated[
        Optional[List["ListOffersResponseOffer"]],
        Field(None, description="A list of offers."),
    ]

    pagination: Annotated[
        Optional["PaginationResponse"],
        Field(
            None, description="Use these parameters to paginate through the response."
        ),
    ]


# Rebuild models to resolve forward references
GetSellingPartnerMetricsRequestBody.model_rebuild()
ListOfferMetricsRequestBody.model_rebuild()
ListOffersRequestBody.model_rebuild()
Preference.model_rebuild()
Promotion.model_rebuild()
DiscountFunding.model_rebuild()
OfferProgramConfiguration.model_rebuild()
OfferProgramConfigurationPreferences.model_rebuild()
OfferProgramConfigurationPromotions.model_rebuild()
OfferProgramConfigurationPromotionsDiscountFunding.model_rebuild()
ListOfferMetricsRequestPagination.model_rebuild()
ListOfferMetricsRequestFilters.model_rebuild()
ListOfferMetricsRequestSort.model_rebuild()
ListOffersRequestPagination.model_rebuild()
ListOffersRequestFilters.model_rebuild()
ListOffersRequestSort.model_rebuild()
TimeInterval.model_rebuild()
GetSellingPartnerMetricsResponse.model_rebuild()
GetSellingPartnerMetricsResponseMetric.model_rebuild()
ListOfferMetricsResponse.model_rebuild()
ListOffersResponse.model_rebuild()
ListOffersResponseOffer.model_rebuild()
PaginationResponse.model_rebuild()
ListOfferMetricsResponseOffer.model_rebuild()
ErrorList.model_rebuild()
Error.model_rebuild()
GetSellingPartnerMetricsRequest.model_rebuild()
ListOfferMetricsRequest.model_rebuild()
ListOffersRequest.model_rebuild()
