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

Asin = str
"""The ASIN of the item."""


"""
HttpBody

Additional HTTP body information that is associated with an individual request within a batch.
"""


class HttpBody(SpApiBaseModel):
    """Additional HTTP body information that is associated with an individual request within a batch."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
HttpHeaders

A mapping of additional HTTP headers to send or receive for an individual request within a batch.
"""


class HttpHeaders(SpApiBaseModel):
    """A mapping of additional HTTP headers to send or receive for an individual request within a batch."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


HttpMethod = str
"""The HTTP method associated with an individual request within a batch."""


"""
BatchRequestBody

The common properties for individual requests within a batch.
"""


class BatchRequestBody(SpApiBaseModel):
    """The common properties for individual requests within a batch."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    uri: Annotated[
        str,
        Field(
            ...,
            description="The URI associated with an individual request within a batch. For `FeaturedOfferExpectedPrice`, this is `/products/pricing/2022-05-01/offer/featuredOfferExpectedPrice`.",
        ),
    ]

    method: Annotated[
        "HttpMethod",
        Field(
            ...,
        ),
    ]

    body: Annotated[
        Optional["HttpBody"],
        Field(
            None,
        ),
    ]

    headers: Annotated[
        Optional["HttpHeaders"],
        Field(
            None,
        ),
    ]


"""
HttpStatusLine

The HTTP status line associated with the response for an individual request within a batch. For more information, refer to [RFC 2616](https://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html).
"""


class HttpStatusLine(SpApiBaseModel):
    """The HTTP status line associated with the response for an individual request within a batch. For more information, refer to [RFC 2616](https://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html)."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    status_code: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("statusCode", "status_code"),
            serialization_alias="statusCode",
            description="The HTTP response status code.",
        ),
    ]

    reason_phrase: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("reasonPhrase", "reason_phrase"),
            serialization_alias="reasonPhrase",
            description="The HTTP response reason phrase.",
        ),
    ]


"""
BatchResponse

The common properties for responses to individual requests within a batch.
"""


class BatchResponse(SpApiBaseModel):
    """The common properties for responses to individual requests within a batch."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    headers: Annotated[
        "HttpHeaders",
        Field(
            ...,
        ),
    ]

    status: Annotated[
        "HttpStatusLine",
        Field(
            ...,
        ),
    ]


CompetitiveSummaryRequestList = List["CompetitiveSummaryRequestBody"]
"""A batched list of `competitiveSummary` requests."""


"""
CompetitiveSummaryBatchRequestBody

The `competitiveSummary` batch request data.
"""


class CompetitiveSummaryBatchRequestBody(SpApiBaseModel):
    """The `competitiveSummary` batch request data."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    requests: Annotated[
        "CompetitiveSummaryRequestList",
        Field(..., description="A batched list of `competitiveSummary` requests."),
    ]


CompetitiveSummaryResponseList = List["CompetitiveSummaryResponse"]
"""The response list for the `competitiveSummaryBatch` operation."""


"""
CompetitiveSummaryBatchResponse

The response schema for the `competitiveSummaryBatch` operation.
"""


class CompetitiveSummaryBatchResponse(SpApiBaseModel):
    """The response schema for the `competitiveSummaryBatch` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    responses: Annotated[
        "CompetitiveSummaryResponseList",
        Field(
            ...,
            description="The response list for the `competitiveSummaryBatch` operation.",
        ),
    ]


CompetitiveSummaryIncludedData = str
"""The supported data types in the `getCompetitiveSummary` API."""


HttpUri = str
"""The URI associated with the individual APIs that are called as part of the batch request."""


Condition = str
"""The condition of the item."""


# Enum definitions
class LowestPricedOffersInputOfferTypeEnum(str, Enum):
    """Enum for offerType"""

    CONSUMER = "Consumer"  # An offer that is available to all Amazon customers.


"""
LowestPricedOffersInput

The input required for building `LowestPricedOffers` data in the response.
"""


class LowestPricedOffersInput(SpApiBaseModel):
    """The input required for building `LowestPricedOffers` data in the response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    item_condition: Annotated[
        "Condition",
        Field(
            ...,
            validation_alias=AliasChoices("itemCondition", "item_condition"),
            serialization_alias="itemCondition",
            description="The input parameter specifies the `itemCondition` of the offer that is requested for `LowestPricedOffers`. `New` is the default value for `itemCondition`.",
        ),
    ]

    offer_type: Annotated[
        LowestPricedOffersInputOfferTypeEnum,
        Field(
            ...,
            validation_alias=AliasChoices("offerType", "offer_type"),
            serialization_alias="offerType",
            description="The input parameter specifies the type of offers requested for `LowestPricedOffers`. This applies to `Consumer` and `Business` offers. `Consumer` is the default `offerType`.",
        ),
    ]


MarketplaceId = str
"""The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids)."""


"""
CompetitiveSummaryRequestBody

An individual `competitiveSummary` request for an ASIN and `marketplaceId`.
"""


class CompetitiveSummaryRequestBody(SpApiBaseModel):
    """An individual `competitiveSummary` request for an ASIN and `marketplaceId`."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    asin: Annotated[
        "Asin",
        Field(
            ..., description="The Amazon Standard Identification Number for the item."
        ),
    ]

    marketplace_id: Annotated[
        Optional["MarketplaceId"],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="A marketplace identifier.",
        ),
    ]

    included_data: Annotated[
        List["CompetitiveSummaryIncludedData"],
        Field(
            ...,
            validation_alias=AliasChoices("includedData", "included_data"),
            serialization_alias="includedData",
            description="The list of requested competitive pricing data for the product.",
        ),
    ]

    lowest_priced_offers_inputs: Annotated[
        Optional[List["LowestPricedOffersInput"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "lowestPricedOffersInputs", "lowest_priced_offers_inputs"
            ),
            serialization_alias="lowestPricedOffersInputs",
            description="The list of `lowestPricedOffersInput` parameters that are used to build `lowestPricedOffers` in the response. This attribute is only valid if `lowestPricedOffers` is requested in `includedData`",
        ),
    ]

    method: Annotated["HttpMethod", Field(..., description="HTTP method type")]

    uri: Annotated[
        "HttpUri",
        Field(
            ...,
            description="The URI associated with the individual APIs that are called as part of the batch request. For `getCompetitiveSummary`, this is `/products/pricing/2022-05-01/items/competitiveSummary`.",
        ),
    ]


ErrorList = List["Error"]
"""A list of error responses that are returned when a request is unsuccessful."""


"""
SegmentedFeaturedOffer

A product offer with segment information indicating where it's featured.
"""


class SegmentedFeaturedOffer(SpApiBaseModel):
    """A product offer with segment information indicating where it's featured."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


# Enum definitions
class FeaturedBuyingOptionBuyingOptionTypeEnum(str, Enum):
    """Enum for buyingOptionType"""

    NEW = "New"  # New


"""
FeaturedBuyingOption

Describes a featured buying option, which includes a list of segmented featured offers for a particular item condition.
"""


class FeaturedBuyingOption(SpApiBaseModel):
    """Describes a featured buying option, which includes a list of segmented featured offers for a particular item condition."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    buying_option_type: Annotated[
        FeaturedBuyingOptionBuyingOptionTypeEnum,
        Field(
            ...,
            validation_alias=AliasChoices("buyingOptionType", "buying_option_type"),
            serialization_alias="buyingOptionType",
            description="The buying option type for the featured offer. `buyingOptionType` represents the buying options that a customer receives on the detail page, such as `B2B`, `Fresh`, and `Subscribe n Save`. `buyingOptionType` currently supports `NEW` as a value.",
        ),
    ]

    segmented_featured_offers: Annotated[
        List["SegmentedFeaturedOffer"],
        Field(
            ...,
            validation_alias=AliasChoices(
                "segmentedFeaturedOffers", "segmented_featured_offers"
            ),
            serialization_alias="segmentedFeaturedOffers",
            description="A list of segmented featured offers for the current buying option type. A segment can be considered as a group of regional contexts that all have the same featured offer. A regional context is a combination of factors such as customer type, region, or postal code and buying option.",
        ),
    ]


FulfillmentType = str
"""Indicates whether the item is fulfilled by Amazon or by the seller (merchant)."""


"""
MoneyType

Currency type and monetary value schema to demonstrate pricing information.
"""


class MoneyType(SpApiBaseModel):
    """Currency type and monetary value schema to demonstrate pricing information."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    currency_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("currencyCode", "currency_code"),
            serialization_alias="currencyCode",
            description="The currency code in ISO 4217 format.",
        ),
    ]

    amount: Annotated[Optional[float], Field(None, description="The monetary value.")]


"""
Points

The number of Amazon Points that are offered with the purchase of an item and the monetary value of these points.
"""


class Points(SpApiBaseModel):
    """The number of Amazon Points that are offered with the purchase of an item and the monetary value of these points."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    points_number: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("pointsNumber", "points_number"),
            serialization_alias="pointsNumber",
            description="The number of Amazon Points.",
        ),
    ]

    points_monetary_value: Annotated[
        Optional["MoneyType"],
        Field(
            None,
            validation_alias=AliasChoices(
                "pointsMonetaryValue", "points_monetary_value"
            ),
            serialization_alias="pointsMonetaryValue",
            description="The monetary value of the Amazon Points.",
        ),
    ]


# Enum definitions
class PrimeDetailsEligibilityEnum(str, Enum):
    """Enum for eligibility"""

    NATIONAL = "NATIONAL"  # Indicates that this offer has Amazon Prime eligibility in all regions within the marketplace.
    REGIONAL = "REGIONAL"  # Indicates that this offer has Amazon Prime eligibility in some (but not all) regions within the marketplace.
    NONE = "NONE"  # Indicates that this offer is not an Amazon Prime offer in any region within the marketplace.


"""
PrimeDetails

Amazon Prime details.
"""


class PrimeDetails(SpApiBaseModel):
    """Amazon Prime details."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    eligibility: Annotated[
        PrimeDetailsEligibilityEnum,
        Field(..., description="Indicates whether the offer is an Amazon Prime offer."),
    ]


# Enum definitions
class ShippingOptionShippingOptionTypeEnum(str, Enum):
    """Enum for shippingOptionType"""

    DEFAULT = "DEFAULT"  # The estimated shipping cost of the product. Note that the shipping cost is not always available.


"""
ShippingOption

The shipping option available for the offer.
"""


class ShippingOption(SpApiBaseModel):
    """The shipping option available for the offer."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipping_option_type: Annotated[
        ShippingOptionShippingOptionTypeEnum,
        Field(
            ...,
            validation_alias=AliasChoices("shippingOptionType", "shipping_option_type"),
            serialization_alias="shippingOptionType",
            description="The type of shipping option.",
        ),
    ]

    price: Annotated[
        "MoneyType", Field(..., description="Shipping price for the offer.")
    ]


# Enum definitions
class OfferSubConditionEnum(str, Enum):
    """Enum for subCondition"""

    NEW = "New"  # New
    MINT = "Mint"  # Mint
    VERY_GOOD = "VeryGood"  # VeryGood
    GOOD = "Good"  # Good
    ACCEPTABLE = "Acceptable"  # Acceptable
    POOR = "Poor"  # Poor
    CLUB = "Club"  # Club
    OEM = "OEM"  # OEM
    WARRANTY = "Warranty"  # Warranty
    REFURBISHED_WARRANTY = "RefurbishedWarranty"  # RefurbishedWarranty
    REFURBISHED = "Refurbished"  # Refurbished
    OPEN_BOX = "OpenBox"  # OpenBox
    OTHER = "Other"  # Other


"""
Offer

The offer data of a product.
"""


class Offer(SpApiBaseModel):
    """The offer data of a product."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("sellerId", "seller_id"),
            serialization_alias="sellerId",
            description="The seller identifier for the offer.",
        ),
    ]

    condition: Annotated["Condition", Field(..., description="Item Condition.")]

    sub_condition: Annotated[
        Optional[OfferSubConditionEnum],
        Field(
            None,
            validation_alias=AliasChoices("subCondition", "sub_condition"),
            serialization_alias="subCondition",
            description="The item subcondition of the offer.",
        ),
    ]

    fulfillment_type: Annotated[
        "FulfillmentType",
        Field(
            ...,
            validation_alias=AliasChoices("fulfillmentType", "fulfillment_type"),
            serialization_alias="fulfillmentType",
            description="The fulfillment type for the offer. Possible values are `AFN` (Amazon Fulfillment Network) and `MFN` (Merchant Fulfillment Network).",
        ),
    ]

    listing_price: Annotated[
        "MoneyType",
        Field(
            ...,
            validation_alias=AliasChoices("listingPrice", "listing_price"),
            serialization_alias="listingPrice",
            description="The offer buying price. This doesn't include shipping, points, or applicable promotions.",
        ),
    ]

    shipping_options: Annotated[
        Optional[List["ShippingOption"]],
        Field(
            None,
            validation_alias=AliasChoices("shippingOptions", "shipping_options"),
            serialization_alias="shippingOptions",
            description="A list of shipping options associated with this offer",
        ),
    ]

    points: Annotated[
        Optional["Points"],
        Field(
            None,
            description="The number of Amazon Points that are offered with the purchase of an item and the monetary value of these points. Note that the Points element is only returned in Japan (JP).",
        ),
    ]

    prime_details: Annotated[
        Optional["PrimeDetails"],
        Field(
            None,
            validation_alias=AliasChoices("primeDetails", "prime_details"),
            serialization_alias="primeDetails",
            description="Amazon Prime details.",
        ),
    ]


"""
LowestPricedOffer

Describes the lowest priced offers for the specified item condition and offer type.
"""


class LowestPricedOffer(SpApiBaseModel):
    """Describes the lowest priced offers for the specified item condition and offer type."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    lowest_priced_offers_input: Annotated[
        "LowestPricedOffersInput",
        Field(
            ...,
            validation_alias=AliasChoices(
                "lowestPricedOffersInput", "lowest_priced_offers_input"
            ),
            serialization_alias="lowestPricedOffersInput",
            description="The filtering criteria that are used to retrieve the lowest priced offers that correspond to the `lowestPricedOffersInputs` request.",
        ),
    ]

    offers: Annotated[
        List["Offer"],
        Field(
            ...,
            description="A list of up to 20 lowest priced offers that match the criteria specified in `lowestPricedOffersInput`.",
        ),
    ]


"""
ReferencePrice

The reference price for the specified ASIN `marketplaceId` combination.
"""


class ReferencePrice(SpApiBaseModel):
    """The reference price for the specified ASIN `marketplaceId` combination."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[
        str,
        Field(
            ...,
            description="Reference price type (e.g., `CompetitivePriceThreshold`, `WasPrice`, `CompetitivePrice`). For definitions, see the [Product Pricing API Use Case Guide](https://developer-docs.amazon.com/sp-api/docs/product-pricing-api-v2022-05-01-use-case-guide).",
        ),
    ]

    price: Annotated[
        "MoneyType",
        Field(
            ...,
            description="The reference price for the ASIN `marketplaceId` combination.",
        ),
    ]


"""
CompetitiveSummaryResponseBody

The `competitiveSummaryResponse` body for a requested ASIN and `marketplaceId`.
"""


class CompetitiveSummaryResponseBody(SpApiBaseModel):
    """The `competitiveSummaryResponse` body for a requested ASIN and `marketplaceId`."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    asin: Annotated[
        "Asin", Field(..., description="The Amazon identifier for the item.")
    ]

    marketplace_id: Annotated[
        Optional["MarketplaceId"],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="A marketplace identifier.",
        ),
    ]

    featured_buying_options: Annotated[
        Optional[List["FeaturedBuyingOption"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "featuredBuyingOptions", "featured_buying_options"
            ),
            serialization_alias="featuredBuyingOptions",
            description="A list of featured buying options for the specified ASIN `marketplaceId` combination.",
        ),
    ]

    lowest_priced_offers: Annotated[
        Optional[List["LowestPricedOffer"]],
        Field(
            None,
            validation_alias=AliasChoices("lowestPricedOffers", "lowest_priced_offers"),
            serialization_alias="lowestPricedOffers",
            description="A list of lowest priced offers for the specified ASIN `marketplaceId` combination.",
        ),
    ]

    reference_prices: Annotated[
        Optional[List["ReferencePrice"]],
        Field(
            None,
            validation_alias=AliasChoices("referencePrices", "reference_prices"),
            serialization_alias="referencePrices",
            description="A list of reference prices for the specified ASIN `marketplaceId` combination.",
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"], Field(None, description="A list of errors")
    ]


"""
CompetitiveSummaryResponse

The response for the individual `competitiveSummary` request in the batch operation.
"""


class CompetitiveSummaryResponse(SpApiBaseModel):
    """The response for the individual `competitiveSummary` request in the batch operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    status: Annotated[
        "HttpStatusLine",
        Field(
            ...,
            description="The HTTP status line associated with the response. For more information, refer to [RFC 2616](https://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html).",
        ),
    ]

    body: Annotated[
        "CompetitiveSummaryResponseBody",
        Field(
            ...,
            description="The `competitiveSummaryResponse` body for a requested ASIN and `marketplaceId`.",
        ),
    ]


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
Errors

A list of error responses returned when a request is unsuccessful.
"""


class Errors(SpApiBaseModel):
    """A list of error responses returned when a request is unsuccessful."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        "ErrorList",
        Field(
            ...,
            description="One or more unexpected errors occurred during the operation.",
        ),
    ]


"""
OfferIdentifier

Identifies an offer from a particular seller for a specified ASIN.
"""


class OfferIdentifier(SpApiBaseModel):
    """Identifies an offer from a particular seller for a specified ASIN."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional["MarketplaceId"],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="A marketplace identifier.",
        ),
    ]

    seller_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("sellerId", "seller_id"),
            serialization_alias="sellerId",
            description="The seller identifier for the offer.",
        ),
    ]

    sku: Annotated[
        Optional[str],
        Field(
            None,
            description="The seller SKU of the item. This will only be present for the target offer, which belongs to the requesting seller.",
        ),
    ]

    asin: Annotated[
        "Asin", Field(..., description="The Amazon identifier for the item.")
    ]

    fulfillment_type: Annotated[
        Optional["FulfillmentType"],
        Field(
            None,
            validation_alias=AliasChoices("fulfillmentType", "fulfillment_type"),
            serialization_alias="fulfillmentType",
            description="The fulfillment type for the offer.",
        ),
    ]


"""
Price

The schema for item's price information, including listing price, shipping price, and Amazon Points.
"""


class Price(SpApiBaseModel):
    """The schema for item's price information, including listing price, shipping price, and Amazon Points."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    listing_price: Annotated[
        "MoneyType",
        Field(
            ...,
            validation_alias=AliasChoices("listingPrice", "listing_price"),
            serialization_alias="listingPrice",
            description="The listing price for the item, excluding any promotions.",
        ),
    ]

    shipping_price: Annotated[
        Optional["MoneyType"],
        Field(
            None,
            validation_alias=AliasChoices("shippingPrice", "shipping_price"),
            serialization_alias="shippingPrice",
            description="The shipping cost of the product. Note that the shipping cost is not always available.",
        ),
    ]

    points: Annotated[
        Optional["Points"],
        Field(
            None,
            description="The number of Amazon Points that are offered with the purchase of an item and the monetary value of these points.",
        ),
    ]


"""
FeaturedOffer

Schema for `currentFeaturedOffer` or `competingFeaturedOffer`.
"""


class FeaturedOffer(SpApiBaseModel):
    """Schema for `currentFeaturedOffer` or `competingFeaturedOffer`."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    offer_identifier: Annotated[
        "OfferIdentifier",
        Field(
            ...,
            validation_alias=AliasChoices("offerIdentifier", "offer_identifier"),
            serialization_alias="offerIdentifier",
            description="An offer identifier used to identify the merchant of the featured offer. Since this may not belong to the requester, the SKU field is omitted.",
        ),
    ]

    condition: Annotated[
        Optional["Condition"], Field(None, description="The item condition.")
    ]

    price: Annotated[
        Optional["Price"],
        Field(None, description="The current active price of the offer."),
    ]


"""
FeaturedOfferExpectedPrice

The item price at or below which the target offer may be featured.
"""


class FeaturedOfferExpectedPrice(SpApiBaseModel):
    """The item price at or below which the target offer may be featured."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    listing_price: Annotated[
        "MoneyType",
        Field(
            ...,
            validation_alias=AliasChoices("listingPrice", "listing_price"),
            serialization_alias="listingPrice",
            description="A computed listing price at or below which a seller can expect to become the featured offer (before applicable promotions).",
        ),
    ]

    points: Annotated[
        Optional["Points"],
        Field(
            None,
            description="The number of Amazon Points that are offered with the purchase of an item and the monetary value of these points.",
        ),
    ]


"""
FeaturedOfferExpectedPriceRequestBody

An individual FOEP request for a particular SKU.
"""


class FeaturedOfferExpectedPriceRequestBody(SpApiBaseModel):
    """An individual FOEP request for a particular SKU."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


FeaturedOfferExpectedPriceRequestList = List["FeaturedOfferExpectedPriceRequestBody"]
"""A batched list of FOEP requests."""


"""
PostalCode

Postal code value with country code
"""


class PostalCode(SpApiBaseModel):
    """Postal code value with country code"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    country_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
            description="Country code value",
        ),
    ]

    value: Annotated[Optional[str], Field(None, description="Postal code value ")]


"""
SampleLocation

Information about a location. It uses a postal code to identify the location.
"""


class SampleLocation(SpApiBaseModel):
    """Information about a location. It uses a postal code to identify the location."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    postal_code: Annotated[
        Optional["PostalCode"],
        Field(
            None,
            validation_alias=AliasChoices("postalCode", "postal_code"),
            serialization_alias="postalCode",
        ),
    ]


"""
SegmentDetails

The details about the segment. The FeaturedOfferExpectedPrice API uses only the sampleLocation portion as input.
"""


class SegmentDetails(SpApiBaseModel):
    """The details about the segment. The FeaturedOfferExpectedPrice API uses only the sampleLocation portion as input."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    glance_view_weight_percentage: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "glanceViewWeightPercentage", "glance_view_weight_percentage"
            ),
            serialization_alias="glanceViewWeightPercentage",
            description="The glance view weighted percentage for this segment, which is the glance views for this segment as a percentage of total glance views across all segments for the ASIN. A higher percentage indicates that more Amazon customers receive this offer as the Featured Offer.",
        ),
    ]

    sample_location: Annotated[
        Optional["SampleLocation"],
        Field(
            None,
            validation_alias=AliasChoices("sampleLocation", "sample_location"),
            serialization_alias="sampleLocation",
            description="The representative location that features the offer for the segment.",
        ),
    ]


"""
Segment

Input segment for featured offer expected price. The segment contains the location information for which featured offer expected price is requested.
"""


class Segment(SpApiBaseModel):
    """Input segment for featured offer expected price. The segment contains the location information for which featured offer expected price is requested."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    segment_details: Annotated[
        Optional["SegmentDetails"],
        Field(
            None,
            validation_alias=AliasChoices("segmentDetails", "segment_details"),
            serialization_alias="segmentDetails",
            description="Segment details",
        ),
    ]


Sku = str
"""The seller SKU of the item."""


"""
FeaturedOfferExpectedPriceRequestParams

The parameters for an individual request.
"""


class FeaturedOfferExpectedPriceRequestParams(SpApiBaseModel):
    """The parameters for an individual request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional["MarketplaceId"],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
        ),
    ]

    sku: Annotated[
        "Sku",
        Field(
            ...,
        ),
    ]

    segment: Annotated[
        Optional["Segment"],
        Field(
            None,
        ),
    ]


"""
FeaturedOfferExpectedPriceResponse

Schema for an individual FOEP response.
"""


class FeaturedOfferExpectedPriceResponse(SpApiBaseModel):
    """Schema for an individual FOEP response."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


FeaturedOfferExpectedPriceResultList = List["FeaturedOfferExpectedPriceResult"]
"""A list of FOEP results for the requested offer."""


"""
FeaturedOfferExpectedPriceResponseBody

The FOEP response data for a requested SKU.
"""


class FeaturedOfferExpectedPriceResponseBody(SpApiBaseModel):
    """The FOEP response data for a requested SKU."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    offer_identifier: Annotated[
        Optional["OfferIdentifier"],
        Field(
            None,
            validation_alias=AliasChoices("offerIdentifier", "offer_identifier"),
            serialization_alias="offerIdentifier",
            description="Metadata that identifies the target offer for which the FOEP result data was computed.",
        ),
    ]

    featured_offer_expected_price_results: Annotated[
        Optional["FeaturedOfferExpectedPriceResultList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "featuredOfferExpectedPriceResults",
                "featured_offer_expected_price_results",
            ),
            serialization_alias="featuredOfferExpectedPriceResults",
            description="The FOEP results for the requested target offer.",
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="The errors that occurred if the operation wasn't successful (HTTP status code non-200).",
        ),
    ]


FeaturedOfferExpectedPriceResponseList = List["FeaturedOfferExpectedPriceResponse"]
"""A batched list of FOEP responses."""


"""
FeaturedOfferExpectedPriceResult

The FOEP result data for the requested offer.
"""


class FeaturedOfferExpectedPriceResult(SpApiBaseModel):
    """The FOEP result data for the requested offer."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    featured_offer_expected_price: Annotated[
        Optional["FeaturedOfferExpectedPrice"],
        Field(
            None,
            validation_alias=AliasChoices(
                "featuredOfferExpectedPrice", "featured_offer_expected_price"
            ),
            serialization_alias="featuredOfferExpectedPrice",
        ),
    ]

    result_status: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("resultStatus", "result_status"),
            serialization_alias="resultStatus",
            description="The status of the FOEP computation. Possible values include `VALID_FOEP`, `NO_COMPETING_OFFER`, `OFFER_NOT_ELIGIBLE`, `OFFER_NOT_FOUND`, and `ASIN_NOT_ELIGIBLE`. Additional values might be added in the future.",
        ),
    ]

    competing_featured_offer: Annotated[
        Optional["FeaturedOffer"],
        Field(
            None,
            validation_alias=AliasChoices(
                "competingFeaturedOffer", "competing_featured_offer"
            ),
            serialization_alias="competingFeaturedOffer",
            description="The offer that will likely be the featured offer if the target offer is priced above its FOEP. If the target offer is currently the featured offer, this property will be different than `currentFeaturedOffer`.",
        ),
    ]

    current_featured_offer: Annotated[
        Optional["FeaturedOffer"],
        Field(
            None,
            validation_alias=AliasChoices(
                "currentFeaturedOffer", "current_featured_offer"
            ),
            serialization_alias="currentFeaturedOffer",
            description="The offer that is currently the featured offer. If the target offer is not currently featured, then this property will be equal to `competingFeaturedOffer`.",
        ),
    ]


# Enum definitions
class FeaturedOfferSegmentCustomerMembershipEnum(str, Enum):
    """Enum for customerMembership"""

    PRIME = "PRIME"  # Customers that are Prime members.
    NON_PRIME = "NON_PRIME"  # Customers that are not Prime members.
    DEFAULT = "DEFAULT"  # Customers whose Prime membership status is unknown.


"""
FeaturedOfferSegment

Describes the segment in which the offer is featured.
"""


class FeaturedOfferSegment(SpApiBaseModel):
    """Describes the segment in which the offer is featured."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    customer_membership: Annotated[
        FeaturedOfferSegmentCustomerMembershipEnum,
        Field(
            ...,
            validation_alias=AliasChoices("customerMembership", "customer_membership"),
            serialization_alias="customerMembership",
            description="The customer membership type that makes up this segment",
        ),
    ]

    segment_details: Annotated[
        "SegmentDetails",
        Field(
            ...,
            validation_alias=AliasChoices("segmentDetails", "segment_details"),
            serialization_alias="segmentDetails",
            description="The details about the segment.",
        ),
    ]


"""
GetCompetitiveSummaryRequest

Request parameters for getCompetitiveSummary
"""


class GetCompetitiveSummaryRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getCompetitiveSummary
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    requests: Annotated[
        "CompetitiveSummaryBatchRequestBody",
        BodyParam(),
        Field(..., description="[BODY] The batch of `getCompetitiveSummary` requests."),
    ]


"""
GetFeaturedOfferExpectedPriceBatchRequestBody

The request body for the `getFeaturedOfferExpectedPriceBatch` operation.
"""


class GetFeaturedOfferExpectedPriceBatchRequestBody(SpApiBaseModel):
    """The request body for the `getFeaturedOfferExpectedPriceBatch` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    requests: Annotated[
        Optional["FeaturedOfferExpectedPriceRequestList"],
        Field(
            None,
        ),
    ]


"""
GetFeaturedOfferExpectedPriceBatchRequest

Request parameters for getFeaturedOfferExpectedPriceBatch
"""


class GetFeaturedOfferExpectedPriceBatchRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getFeaturedOfferExpectedPriceBatch
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    get_featured_offer_expected_price_batch_request_body: Annotated[
        "GetFeaturedOfferExpectedPriceBatchRequestBody",
        BodyParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "getFeaturedOfferExpectedPriceBatchRequestBody",
                "get_featured_offer_expected_price_batch_request_body",
            ),
            serialization_alias="getFeaturedOfferExpectedPriceBatchRequestBody",
            description="[BODY] The batch of `getFeaturedOfferExpectedPrice` requests.",
        ),
    ]


"""
GetFeaturedOfferExpectedPriceBatchResponse

The response schema for the `getFeaturedOfferExpectedPriceBatch` operation.
"""


class GetFeaturedOfferExpectedPriceBatchResponse(SpApiBaseModel):
    """The response schema for the `getFeaturedOfferExpectedPriceBatch` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    responses: Annotated[
        Optional["FeaturedOfferExpectedPriceResponseList"],
        Field(
            None,
        ),
    ]


# Rebuild models to resolve forward references
GetFeaturedOfferExpectedPriceBatchRequestBody.model_rebuild()
FeaturedOfferExpectedPriceRequestBody.model_rebuild()
FeaturedOfferExpectedPriceRequestParams.model_rebuild()
GetFeaturedOfferExpectedPriceBatchResponse.model_rebuild()
FeaturedOfferExpectedPriceResponse.model_rebuild()
CompetitiveSummaryBatchRequestBody.model_rebuild()
CompetitiveSummaryRequestBody.model_rebuild()
LowestPricedOffersInput.model_rebuild()
CompetitiveSummaryBatchResponse.model_rebuild()
CompetitiveSummaryResponse.model_rebuild()
CompetitiveSummaryResponseBody.model_rebuild()
ReferencePrice.model_rebuild()
FeaturedBuyingOption.model_rebuild()
SegmentedFeaturedOffer.model_rebuild()
LowestPricedOffer.model_rebuild()
Offer.model_rebuild()
PrimeDetails.model_rebuild()
ShippingOption.model_rebuild()
FeaturedOfferSegment.model_rebuild()
SegmentDetails.model_rebuild()
SampleLocation.model_rebuild()
PostalCode.model_rebuild()
Errors.model_rebuild()
FeaturedOfferExpectedPriceResponseBody.model_rebuild()
FeaturedOfferExpectedPriceResult.model_rebuild()
FeaturedOfferExpectedPrice.model_rebuild()
FeaturedOffer.model_rebuild()
HttpHeaders.model_rebuild()
HttpStatusLine.model_rebuild()
HttpBody.model_rebuild()
BatchRequestBody.model_rebuild()
BatchResponse.model_rebuild()
OfferIdentifier.model_rebuild()
MoneyType.model_rebuild()
Price.model_rebuild()
Points.model_rebuild()
Segment.model_rebuild()
Error.model_rebuild()
GetFeaturedOfferExpectedPriceBatchRequest.model_rebuild()
GetCompetitiveSummaryRequest.model_rebuild()
