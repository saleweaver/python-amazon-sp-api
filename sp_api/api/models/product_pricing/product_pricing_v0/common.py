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

"""
ASINIdentifier

Schema to identify an item by MarketPlaceId and ASIN.
"""


class ASINIdentifier(SpApiBaseModel):
    """Schema to identify an item by MarketPlaceId and ASIN."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceId", "marketplace_id"),
            serialization_alias="MarketplaceId",
            description="A marketplace identifier.",
        ),
    ]

    a_s_i_n: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("ASIN", "a_s_i_n"),
            serialization_alias="ASIN",
            description="The Amazon Standard Identification Number (ASIN) of the item.",
        ),
    ]


Asin = str
"""The Amazon Standard Identification Number (ASIN) of the item."""


"""
AttributeSetList

A list of product attributes if they are applicable to the product that is returned.
"""


class AttributeSetList(SpApiBaseModel):
    """A list of product attributes if they are applicable to the product that is returned."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


CustomerType = str
"""Indicates whether to request Consumer or Business offers. Default is Consumer."""


ItemCondition = str
"""Filters the offer listings to be considered based on item condition. Possible values: New, Used, Collectible, Refurbished, Club."""


MarketplaceId = str
"""A marketplace identifier. Specifies the marketplace for which prices are returned."""


"""
BatchOffersRequestParams

Common request parameters that can be accepted by `ItemOffersRequest` and `ListingOffersRequest`
"""


class BatchOffersRequestParams(SpApiBaseModel):
    """Common request parameters that can be accepted by `ItemOffersRequest` and `ListingOffersRequest`"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional["MarketplaceId"],
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceId", "marketplace_id"),
            serialization_alias="MarketplaceId",
        ),
    ]

    item_condition: Annotated[
        "ItemCondition",
        Field(
            ...,
            validation_alias=AliasChoices("ItemCondition", "item_condition"),
            serialization_alias="ItemCondition",
            description="Filters the offer listings to be considered based on item condition. Possible values: New, Used, Collectible, Refurbished, Club.",
        ),
    ]

    customer_type: Annotated[
        Optional["CustomerType"],
        Field(
            None,
            validation_alias=AliasChoices("CustomerType", "customer_type"),
            serialization_alias="CustomerType",
            description="Indicates whether to request Consumer or Business offers. Default is Consumer.",
        ),
    ]


"""
GetOffersHttpStatusLine

The HTTP status line associated with the response. For more information, consult [RFC 2616](https://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html).
"""


class GetOffersHttpStatusLine(SpApiBaseModel):
    """The HTTP status line associated with the response. For more information, consult [RFC 2616](https://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html)."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    status_code: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("statusCode", "status_code"),
            serialization_alias="statusCode",
            description="The HTTP response Status Code.",
        ),
    ]

    reason_phrase: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("reasonPhrase", "reason_phrase"),
            serialization_alias="reasonPhrase",
            description="The HTTP response Reason-Phase.",
        ),
    ]


ErrorList = List["Error"]
"""A list of error responses returned when a request is unsuccessful."""


ConditionType = str
"""Indicates the condition of the item. Possible values: New, Used, Collectible, Refurbished, Club."""


"""
ItemIdentifier

Information that identifies an item.
"""


class ItemIdentifier(SpApiBaseModel):
    """Information that identifies an item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceId", "marketplace_id"),
            serialization_alias="MarketplaceId",
            description="A marketplace identifier. Specifies the marketplace from which prices are returned.",
        ),
    ]

    a_s_i_n: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ASIN", "a_s_i_n"),
            serialization_alias="ASIN",
            description="The Amazon Standard Identification Number (ASIN) of the item.",
        ),
    ]

    seller_s_k_u: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SellerSKU", "seller_s_k_u"),
            serialization_alias="SellerSKU",
            description="The seller stock keeping unit (SKU) of the item.",
        ),
    ]

    item_condition: Annotated[
        "ConditionType",
        Field(
            ...,
            validation_alias=AliasChoices("ItemCondition", "item_condition"),
            serialization_alias="ItemCondition",
            description="The condition of the item.",
        ),
    ]


OfferDetailList = List["OfferDetail"]
"""A list of offer details. The list is the same length as the TotalOfferCount in the Summary or 20, whichever is less."""


BuyBoxEligibleOffers = List["OfferCountType"]
"""A list that contains the total number of offers that are eligible for the Buy Box for the given conditions and fulfillment channels."""


BuyBoxPrices = List["BuyBoxPriceType"]
"""A list of the Buy Box prices."""


LowestPrices = List["LowestPriceType"]
"""A list of the lowest prices."""


"""
MoneyType

Currency type and monetary value. Schema for demonstrating pricing info.
"""


class MoneyType(SpApiBaseModel):
    """Currency type and monetary value. Schema for demonstrating pricing info."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    currency_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("CurrencyCode", "currency_code"),
            serialization_alias="CurrencyCode",
            description="The currency code in ISO 4217 format.",
        ),
    ]

    amount: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices("Amount", "amount"),
            serialization_alias="Amount",
            description="The monetary value.",
        ),
    ]


NumberOfOffers = List["OfferCountType"]
"""A list that contains the total number of offers information for given conditions and fulfillment channels."""


SalesRankList = List["SalesRankType"]
"""A list of sales rank information for the item, by category."""


"""
Summary

Contains price information about the product, including the LowestPrices and BuyBoxPrices, the ListPrice, the SuggestedLowerPricePlusShipping, and NumberOfOffers and NumberOfBuyBoxEligibleOffers.
"""


class Summary(SpApiBaseModel):
    """Contains price information about the product, including the LowestPrices and BuyBoxPrices, the ListPrice, the SuggestedLowerPricePlusShipping, and NumberOfOffers and NumberOfBuyBoxEligibleOffers."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    total_offer_count: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("TotalOfferCount", "total_offer_count"),
            serialization_alias="TotalOfferCount",
            description="The number of unique offers contained in NumberOfOffers.",
        ),
    ]

    number_of_offers: Annotated[
        Optional["NumberOfOffers"],
        Field(
            None,
            validation_alias=AliasChoices("NumberOfOffers", "number_of_offers"),
            serialization_alias="NumberOfOffers",
            description="A list that contains the total number of offers for the item for the given conditions and fulfillment channels.",
        ),
    ]

    lowest_prices: Annotated[
        Optional["LowestPrices"],
        Field(
            None,
            validation_alias=AliasChoices("LowestPrices", "lowest_prices"),
            serialization_alias="LowestPrices",
            description="A list of the lowest prices for the item.",
        ),
    ]

    buy_box_prices: Annotated[
        Optional["BuyBoxPrices"],
        Field(
            None,
            validation_alias=AliasChoices("BuyBoxPrices", "buy_box_prices"),
            serialization_alias="BuyBoxPrices",
            description="A list of item prices.",
        ),
    ]

    list_price: Annotated[
        Optional["MoneyType"],
        Field(
            None,
            validation_alias=AliasChoices("ListPrice", "list_price"),
            serialization_alias="ListPrice",
            description="The list price of the item as suggested by the manufacturer.",
        ),
    ]

    competitive_price_threshold: Annotated[
        Optional["MoneyType"],
        Field(
            None,
            validation_alias=AliasChoices(
                "CompetitivePriceThreshold", "competitive_price_threshold"
            ),
            serialization_alias="CompetitivePriceThreshold",
            description="This price is based on competitive prices from other retailers (excluding other Amazon sellers). The offer may be ineligible for the Buy Box if the seller's price + shipping (minus Amazon Points) is greater than this competitive price.",
        ),
    ]

    suggested_lower_price_plus_shipping: Annotated[
        Optional["MoneyType"],
        Field(
            None,
            validation_alias=AliasChoices(
                "SuggestedLowerPricePlusShipping", "suggested_lower_price_plus_shipping"
            ),
            serialization_alias="SuggestedLowerPricePlusShipping",
            description="The suggested lower price of the item, including shipping and Amazon Points. The suggested lower price is based on a range of factors, including historical selling prices, recent Buy Box-eligible prices, and input from customers for your products.",
        ),
    ]

    sales_rankings: Annotated[
        Optional["SalesRankList"],
        Field(
            None,
            validation_alias=AliasChoices("SalesRankings", "sales_rankings"),
            serialization_alias="SalesRankings",
            description="A list that contains the sales rank of the item in the given product categories.",
        ),
    ]

    buy_box_eligible_offers: Annotated[
        Optional["BuyBoxEligibleOffers"],
        Field(
            None,
            validation_alias=AliasChoices(
                "BuyBoxEligibleOffers", "buy_box_eligible_offers"
            ),
            serialization_alias="BuyBoxEligibleOffers",
            description="A list that contains the total number of offers that are eligible for the Buy Box for the given conditions and fulfillment channels.",
        ),
    ]

    offers_available_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "OffersAvailableTime", "offers_available_time"
            ),
            serialization_alias="OffersAvailableTime",
            description="When the status is ActiveButTooSoonForProcessing, this is the time when the offers will be available for processing.",
        ),
    ]


"""
GetOffersResult

The payload for the getListingOffers and getItemOffers operations.
"""


class GetOffersResult(SpApiBaseModel):
    """The payload for the getListingOffers and getItemOffers operations."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_i_d: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceID", "marketplace_i_d"),
            serialization_alias="MarketplaceID",
            description="A marketplace identifier.",
        ),
    ]

    a_s_i_n: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ASIN", "a_s_i_n"),
            serialization_alias="ASIN",
            description="The Amazon Standard Identification Number (ASIN) of the item.",
        ),
    ]

    s_k_u: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SKU", "s_k_u"),
            serialization_alias="SKU",
            description="The stock keeping unit (SKU) of the item.",
        ),
    ]

    item_condition: Annotated[
        "ConditionType",
        Field(
            ...,
            validation_alias=AliasChoices("ItemCondition", "item_condition"),
            serialization_alias="ItemCondition",
            description="The condition of the item.",
        ),
    ]

    status: Annotated[str, Field(..., description="The status of the operation.")]

    identifier: Annotated[
        "ItemIdentifier",
        Field(
            ...,
            validation_alias=AliasChoices("Identifier", "identifier"),
            serialization_alias="Identifier",
            description="Metadata that identifies the item.",
        ),
    ]

    summary: Annotated[
        "Summary",
        Field(
            ...,
            validation_alias=AliasChoices("Summary", "summary"),
            serialization_alias="Summary",
            description="Pricing information about the item.",
        ),
    ]

    offers: Annotated[
        "OfferDetailList",
        Field(
            ...,
            validation_alias=AliasChoices("Offers", "offers"),
            serialization_alias="Offers",
            description="A list of offer details. The list is the same length as the TotalOfferCount in the Summary or 20, whichever is less.",
        ),
    ]


"""
GetOffersResponse

The response schema for the `getListingOffers` and `getItemOffers` operations.
"""


class GetOffersResponse(SpApiBaseModel):
    """The response schema for the `getListingOffers` and `getItemOffers` operations."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["GetOffersResult"],
        Field(
            None,
            description="The payload for the `getListingOffers` and `getItemOffers` operations.",
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the operation.",
        ),
    ]


"""
HttpResponseHeaders

A mapping of additional HTTP headers to send/receive for the individual batch request.
"""


class HttpResponseHeaders(SpApiBaseModel):
    """A mapping of additional HTTP headers to send/receive for the individual batch request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    date: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("Date", "date"),
            serialization_alias="Date",
            description="The timestamp that the API request was received. For more information, consult [RFC 2616 Section 14](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).",
        ),
    ]

    x_amzn_request_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("x-amzn-RequestId", "x_amzn_request_id"),
            serialization_alias="x-amzn-RequestId",
            description="Unique request reference identifier.",
        ),
    ]


"""
BatchOffersResponse

Common schema that present in `ItemOffersResponse` and `ListingOffersResponse`
"""


class BatchOffersResponse(SpApiBaseModel):
    """Common schema that present in `ItemOffersResponse` and `ListingOffersResponse`"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    headers: Annotated[
        Optional["HttpResponseHeaders"],
        Field(
            None,
        ),
    ]

    status: Annotated[
        Optional["GetOffersHttpStatusLine"],
        Field(
            None,
        ),
    ]

    body: Annotated[
        "GetOffersResponse",
        Field(
            ...,
        ),
    ]


HttpMethod = str
"""The HTTP method associated with the individual APIs being called as part of the batch request."""


"""
HttpRequestHeaders

A mapping of additional HTTP headers to send/receive for the individual batch request.
"""


class HttpRequestHeaders(SpApiBaseModel):
    """A mapping of additional HTTP headers to send/receive for the individual batch request."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
BatchRequestBody

Common properties of batch requests against individual APIs.
"""


class BatchRequestBody(SpApiBaseModel):
    """Common properties of batch requests against individual APIs."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    uri: Annotated[
        str,
        Field(
            ...,
            description="The resource path of the operation you are calling in batch without any query parameters. If you are calling `getItemOffersBatch`, supply the path of `getItemOffers`. **Example:** `/products/pricing/v0/items/B000P6Q7MY/offers` If you are calling `getListingOffersBatch`, supply the path of `getListingOffers`. **Example:** `/products/pricing/v0/listings/B000P6Q7MY/offers`",
        ),
    ]

    method: Annotated[
        "HttpMethod",
        Field(
            ...,
        ),
    ]

    headers: Annotated[
        Optional["HttpRequestHeaders"],
        Field(
            None,
        ),
    ]


OfferCustomerType = str
"""Indicates whether the offer is a B2B or B2C offer"""


"""
Points

The number of Amazon Points offered with the purchase of an item, and their monetary value.
"""


class Points(SpApiBaseModel):
    """The number of Amazon Points offered with the purchase of an item, and their monetary value."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    points_number: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("PointsNumber", "points_number"),
            serialization_alias="PointsNumber",
            description="The number of points.",
        ),
    ]

    points_monetary_value: Annotated[
        Optional["MoneyType"],
        Field(
            None,
            validation_alias=AliasChoices(
                "PointsMonetaryValue", "points_monetary_value"
            ),
            serialization_alias="PointsMonetaryValue",
            description="The monetary value of the points.",
        ),
    ]


QuantityDiscountType = str
"""Indicates the type of quantity discount this price applies to."""


"""
BuyBoxPriceType

Schema for an individual buybox price.
"""


class BuyBoxPriceType(SpApiBaseModel):
    """Schema for an individual buybox price."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    condition: Annotated[
        str,
        Field(
            ...,
            description="Indicates the condition of the item. For example: New, Used, Collectible, Refurbished, or Club.",
        ),
    ]

    offer_type: Annotated[
        Optional["OfferCustomerType"],
        Field(
            None,
            validation_alias=AliasChoices("offerType", "offer_type"),
            serialization_alias="offerType",
            description="Indicates the type of customer that the offer is valid for.<br><br>When the offer type is B2C in a quantity discount, the seller is winning the Buy Box because others do not have inventory at that quantity, not because they have a quantity discount on the ASIN.",
        ),
    ]

    quantity_tier: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("quantityTier", "quantity_tier"),
            serialization_alias="quantityTier",
            description="Indicates at what quantity this price becomes active.",
        ),
    ]

    quantity_discount_type: Annotated[
        Optional["QuantityDiscountType"],
        Field(
            None,
            validation_alias=AliasChoices(
                "quantityDiscountType", "quantity_discount_type"
            ),
            serialization_alias="quantityDiscountType",
            description="Indicates the type of quantity discount this price applies to.",
        ),
    ]

    landed_price: Annotated[
        "MoneyType",
        Field(
            ...,
            validation_alias=AliasChoices("LandedPrice", "landed_price"),
            serialization_alias="LandedPrice",
            description="The value calculated by adding ListingPrice + Shipping - Points.",
        ),
    ]

    listing_price: Annotated[
        "MoneyType",
        Field(
            ...,
            validation_alias=AliasChoices("ListingPrice", "listing_price"),
            serialization_alias="ListingPrice",
            description="The price of the item.",
        ),
    ]

    shipping: Annotated[
        "MoneyType",
        Field(
            ...,
            validation_alias=AliasChoices("Shipping", "shipping"),
            serialization_alias="Shipping",
            description="The shipping cost.",
        ),
    ]

    points: Annotated[
        Optional["Points"],
        Field(
            None,
            validation_alias=AliasChoices("Points", "points"),
            serialization_alias="Points",
            description="The number of Amazon Points offered with the purchase of an item.",
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


CompetitivePriceList = List["CompetitivePriceType"]
"""A list of competitive pricing information."""


"""
PriceType

Schema for item's price information, including listing price, shipping price, and Amazon points.
"""


class PriceType(SpApiBaseModel):
    """Schema for item's price information, including listing price, shipping price, and Amazon points."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    landed_price: Annotated[
        Optional["MoneyType"],
        Field(
            None,
            validation_alias=AliasChoices("LandedPrice", "landed_price"),
            serialization_alias="LandedPrice",
            description="The value calculated by adding ListingPrice + Shipping - Points. Note that if the landed price is not returned, the listing price represents the product with the lowest landed price.",
        ),
    ]

    listing_price: Annotated[
        "MoneyType",
        Field(
            ...,
            validation_alias=AliasChoices("ListingPrice", "listing_price"),
            serialization_alias="ListingPrice",
            description="The listing price of the item including any promotions that apply.",
        ),
    ]

    shipping: Annotated[
        Optional["MoneyType"],
        Field(
            None,
            validation_alias=AliasChoices("Shipping", "shipping"),
            serialization_alias="Shipping",
            description="The shipping cost of the product. Note that the shipping cost is not always available.",
        ),
    ]

    points: Annotated[
        Optional["Points"],
        Field(
            None,
            validation_alias=AliasChoices("Points", "points"),
            serialization_alias="Points",
            description="The number of Amazon Points offered with the purchase of an item, and their monetary value.",
        ),
    ]


"""
CompetitivePriceType

Schema for competitive pricing information
"""


class CompetitivePriceType(SpApiBaseModel):
    """Schema for competitive pricing information"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    competitive_price_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("CompetitivePriceId", "competitive_price_id"),
            serialization_alias="CompetitivePriceId",
            description="The pricing model for each price that is returned. Possible values: * 1 - New Buy Box Price. * 2 - Used Buy Box Price.",
        ),
    ]

    price: Annotated[
        "PriceType",
        Field(
            ...,
            validation_alias=AliasChoices("Price", "price"),
            serialization_alias="Price",
            description="Pricing information for a given CompetitivePriceId value.",
        ),
    ]

    condition: Annotated[
        Optional[str],
        Field(
            None,
            description="Indicates the condition of the item whose pricing information is returned. Possible values are: New, Used, Collectible, Refurbished, or Club.",
        ),
    ]

    subcondition: Annotated[
        Optional[str],
        Field(
            None,
            description="Indicates the subcondition of the item whose pricing information is returned. Possible values are: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty, Refurbished, Open Box, or Other.",
        ),
    ]

    offer_type: Annotated[
        Optional["OfferCustomerType"],
        Field(
            None,
            validation_alias=AliasChoices("offerType", "offer_type"),
            serialization_alias="offerType",
            description="Indicates the type of customer that the offer is valid for.<br><br>When the offer type is B2C in a quantity discount, the seller is winning the Buy Box because others do not have inventory at that quantity, not because they have a quantity discount on the ASIN.",
        ),
    ]

    quantity_tier: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("quantityTier", "quantity_tier"),
            serialization_alias="quantityTier",
            description="Indicates at what quantity this price becomes active.",
        ),
    ]

    quantity_discount_type: Annotated[
        Optional["QuantityDiscountType"],
        Field(
            None,
            validation_alias=AliasChoices(
                "quantityDiscountType", "quantity_discount_type"
            ),
            serialization_alias="quantityDiscountType",
            description="Indicates the type of quantity discount this price applies to.",
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

    belongs_to_requester: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("belongsToRequester", "belongs_to_requester"),
            serialization_alias="belongsToRequester",
            description=" Indicates whether or not the pricing information is for an offer listing that belongs to the requester. The requester is the seller associated with the SellerId that was submitted with the request. Possible values are: true and false.",
        ),
    ]


NumberOfOfferListingsList = List["OfferListingCountType"]
"""The number of active offer listings for the item that was submitted. The listing count is returned by condition, one for each listing condition value that is returned."""


"""
CompetitivePricingType

Competitive pricing information for the item.
"""


class CompetitivePricingType(SpApiBaseModel):
    """Competitive pricing information for the item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    competitive_prices: Annotated[
        "CompetitivePriceList",
        Field(
            ...,
            validation_alias=AliasChoices("CompetitivePrices", "competitive_prices"),
            serialization_alias="CompetitivePrices",
        ),
    ]

    number_of_offer_listings: Annotated[
        "NumberOfOfferListingsList",
        Field(
            ...,
            validation_alias=AliasChoices(
                "NumberOfOfferListings", "number_of_offer_listings"
            ),
            serialization_alias="NumberOfOfferListings",
        ),
    ]

    trade_in_value: Annotated[
        Optional["MoneyType"],
        Field(
            None,
            validation_alias=AliasChoices("TradeInValue", "trade_in_value"),
            serialization_alias="TradeInValue",
            description="The trade-in value of the item in the trade-in program.",
        ),
    ]


# Enum definitions
class AvailabilityTypeEnum(str, Enum):
    """Enum for availabilityType"""

    NOW = "NOW"  # The item is available for shipping now.
    FUTURE_WITHOUT_DATE = "FUTURE_WITHOUT_DATE"  # The item will be available for shipping on an unknown date in the future.
    FUTURE_WITH_DATE = "FUTURE_WITH_DATE"  # The item will be available for shipping on a known date in the future.


"""
DetailedShippingTimeType

The time range in which an item will likely be shipped once an order has been placed.
"""


class DetailedShippingTimeType(SpApiBaseModel):
    """The time range in which an item will likely be shipped once an order has been placed."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    minimum_hours: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("minimumHours", "minimum_hours"),
            serialization_alias="minimumHours",
            description="The minimum time, in hours, that the item will likely be shipped after the order has been placed.",
        ),
    ]

    maximum_hours: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("maximumHours", "maximum_hours"),
            serialization_alias="maximumHours",
            description="The maximum time, in hours, that the item will likely be shipped after the order has been placed.",
        ),
    ]

    available_date: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("availableDate", "available_date"),
            serialization_alias="availableDate",
            description="The date when the item will be available for shipping. Only displayed for items that are not currently available for shipping.",
        ),
    ]

    availability_type: Annotated[
        Optional[AvailabilityTypeEnum],
        Field(
            None,
            validation_alias=AliasChoices("availabilityType", "availability_type"),
            serialization_alias="availabilityType",
            description="Indicates whether the item is available for shipping now, or on a known or an unknown date in the future. If known, the availableDate property indicates the date that the item will be available for shipping. Possible values: NOW, FUTURE_WITHOUT_DATE, FUTURE_WITH_DATE.",
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


FulfillmentChannelType = str
"""Indicates whether the item is fulfilled by Amazon or by the seller (merchant)."""


# Enum definitions
class ItemTypeEnum(str, Enum):
    """Enum for ItemType"""

    ASIN = "Asin"  # The Amazon Standard Identification Number (ASIN).
    SKU = "Sku"  # The seller SKU.


class CustomerTypeEnum(str, Enum):
    """Enum for CustomerType"""

    CONSUMER = "Consumer"  # Consumer
    BUSINESS = "Business"  # Business


"""
GetCompetitivePricingRequest

Request parameters for getCompetitivePricing
"""


class GetCompetitivePricingRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getCompetitivePricing
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceId", "marketplace_id"),
            serialization_alias="MarketplaceId",
            description="[QUERY] A marketplace identifier. Specifies the marketplace for which prices are returned.",
        ),
    ]

    asins: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("Asins", "asins"),
            serialization_alias="Asins",
            description="[QUERY] A list of up to twenty Amazon Standard Identification Number (ASIN) values used to identify items in the given marketplace.",
        ),
    ]

    skus: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("Skus", "skus"),
            serialization_alias="Skus",
            description="[QUERY] A list of up to twenty seller SKU values used to identify items in the given marketplace.",
        ),
    ]

    item_type: Annotated[
        ItemTypeEnum,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("ItemType", "item_type"),
            serialization_alias="ItemType",
            description="[QUERY] Indicates whether ASIN values or seller SKU values are used to identify items. If you specify Asin, the information in the response will be dependent on the list of Asins you provide in the Asins parameter. If you specify Sku, the information in the response will be dependent on the list of Skus you provide in the Skus parameter. Possible values: Asin, Sku.",
        ),
    ]

    customer_type: Annotated[
        Optional[CustomerTypeEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("CustomerType", "customer_type"),
            serialization_alias="CustomerType",
            description="[QUERY] Indicates whether to request pricing information from the point of view of Consumer or Business buyers. Default is Consumer.",
        ),
    ]


ItemOffersRequestList = List["ItemOffersRequestBody"]
"""A list of `getListingOffers` batched requests to run."""


"""
GetItemOffersBatchRequestBody

The request associated with the `getItemOffersBatch` API call.
"""


class GetItemOffersBatchRequestBody(SpApiBaseModel):
    """The request associated with the `getItemOffersBatch` API call."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    requests: Annotated[
        Optional["ItemOffersRequestList"],
        Field(
            None,
        ),
    ]


"""
GetItemOffersBatchRequest

Request parameters for getItemOffersBatch
"""


class GetItemOffersBatchRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getItemOffersBatch
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    get_item_offers_batch_request_body: Annotated[
        "GetItemOffersBatchRequestBody",
        BodyParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "getItemOffersBatchRequestBody", "get_item_offers_batch_request_body"
            ),
            serialization_alias="getItemOffersBatchRequestBody",
            description="[BODY] The request associated with the `getItemOffersBatch` API call.",
        ),
    ]


ItemOffersResponseList = List["ItemOffersResponse"]
"""A list of `getItemOffers` batched responses."""


"""
GetItemOffersBatchResponse

The response associated with the `getItemOffersBatch` API call.
"""


class GetItemOffersBatchResponse(SpApiBaseModel):
    """The response associated with the `getItemOffersBatch` API call."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    responses: Annotated[
        Optional["ItemOffersResponseList"],
        Field(
            None,
        ),
    ]


# Enum definitions
class ItemConditionEnum(str, Enum):
    """Enum for ItemCondition"""

    NEW = "New"  # New
    USED = "Used"  # Used
    COLLECTIBLE = "Collectible"  # Collectible
    REFURBISHED = "Refurbished"  # Refurbished
    CLUB = "Club"  # Club


class CustomerTypeEnum(str, Enum):
    """Enum for CustomerType"""

    CONSUMER = "Consumer"  # Consumer
    BUSINESS = "Business"  # Business


"""
GetItemOffersRequest

Request parameters for getItemOffers
"""


class GetItemOffersRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getItemOffers
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceId", "marketplace_id"),
            serialization_alias="MarketplaceId",
            description="[QUERY] A marketplace identifier. Specifies the marketplace for which prices are returned.",
        ),
    ]

    item_condition: Annotated[
        ItemConditionEnum,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("ItemCondition", "item_condition"),
            serialization_alias="ItemCondition",
            description="[QUERY] Filters the offer listings to be considered based on item condition. Possible values: New, Used, Collectible, Refurbished, Club.",
        ),
    ]

    asin: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("Asin", "asin"),
            serialization_alias="Asin",
            description="[PATH] The Amazon Standard Identification Number (ASIN) of the item.",
        ),
    ]

    customer_type: Annotated[
        Optional[CustomerTypeEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("CustomerType", "customer_type"),
            serialization_alias="CustomerType",
            description="[QUERY] Indicates whether to request Consumer or Business offers. Default is Consumer.",
        ),
    ]


ListingOffersRequestList = List["ListingOffersRequestBody"]
"""A list of `getListingOffers` batched requests to run."""


"""
GetListingOffersBatchRequestBody

The request associated with the `getListingOffersBatch` API call.
"""


class GetListingOffersBatchRequestBody(SpApiBaseModel):
    """The request associated with the `getListingOffersBatch` API call."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    requests: Annotated[
        Optional["ListingOffersRequestList"],
        Field(
            None,
        ),
    ]


"""
GetListingOffersBatchRequest

Request parameters for getListingOffersBatch
"""


class GetListingOffersBatchRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getListingOffersBatch
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    get_listing_offers_batch_request_body: Annotated[
        "GetListingOffersBatchRequestBody",
        BodyParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "getListingOffersBatchRequestBody",
                "get_listing_offers_batch_request_body",
            ),
            serialization_alias="getListingOffersBatchRequestBody",
            description="[BODY] The request associated with the `getListingOffersBatch` API call.",
        ),
    ]


ListingOffersResponseList = List["ListingOffersResponse"]
"""A list of `getListingOffers` batched responses."""


"""
GetListingOffersBatchResponse

The response associated with the `getListingOffersBatch` API call.
"""


class GetListingOffersBatchResponse(SpApiBaseModel):
    """The response associated with the `getListingOffersBatch` API call."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    responses: Annotated[
        Optional["ListingOffersResponseList"],
        Field(
            None,
        ),
    ]


# Enum definitions
class ItemConditionEnum(str, Enum):
    """Enum for ItemCondition"""

    NEW = "New"  # New
    USED = "Used"  # Used
    COLLECTIBLE = "Collectible"  # Collectible
    REFURBISHED = "Refurbished"  # Refurbished
    CLUB = "Club"  # Club


class CustomerTypeEnum(str, Enum):
    """Enum for CustomerType"""

    CONSUMER = "Consumer"  # Consumer
    BUSINESS = "Business"  # Business


"""
GetListingOffersRequest

Request parameters for getListingOffers
"""


class GetListingOffersRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getListingOffers
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceId", "marketplace_id"),
            serialization_alias="MarketplaceId",
            description="[QUERY] A marketplace identifier. Specifies the marketplace for which prices are returned.",
        ),
    ]

    item_condition: Annotated[
        ItemConditionEnum,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("ItemCondition", "item_condition"),
            serialization_alias="ItemCondition",
            description="[QUERY] Filters the offer listings based on item condition. Possible values: New, Used, Collectible, Refurbished, Club.",
        ),
    ]

    seller_s_k_u: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("SellerSKU", "seller_s_k_u"),
            serialization_alias="SellerSKU",
            description="[PATH] Identifies an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.",
        ),
    ]

    customer_type: Annotated[
        Optional[CustomerTypeEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("CustomerType", "customer_type"),
            serialization_alias="CustomerType",
            description="[QUERY] Indicates whether to request Consumer or Business offers. Default is Consumer.",
        ),
    ]


# Enum definitions
class ItemTypeEnum(str, Enum):
    """Enum for ItemType"""

    ASIN = "Asin"  # The Amazon Standard Identification Number (ASIN).
    SKU = "Sku"  # The seller SKU.


class ItemConditionEnum(str, Enum):
    """Enum for ItemCondition"""

    NEW = "New"  # New
    USED = "Used"  # Used
    COLLECTIBLE = "Collectible"  # Collectible
    REFURBISHED = "Refurbished"  # Refurbished
    CLUB = "Club"  # Club


class OfferTypeEnum(str, Enum):
    """Enum for OfferType"""

    B2_C = "B2C"  # B2C
    B2_B = "B2B"  # B2B


"""
GetPricingRequest

Request parameters for getPricing
"""


class GetPricingRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getPricing
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceId", "marketplace_id"),
            serialization_alias="MarketplaceId",
            description="[QUERY] A marketplace identifier. Specifies the marketplace for which prices are returned.",
        ),
    ]

    asins: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("Asins", "asins"),
            serialization_alias="Asins",
            description="[QUERY] A list of up to twenty Amazon Standard Identification Number (ASIN) values used to identify items in the given marketplace.",
        ),
    ]

    skus: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("Skus", "skus"),
            serialization_alias="Skus",
            description="[QUERY] A list of up to twenty seller SKU values used to identify items in the given marketplace.",
        ),
    ]

    item_type: Annotated[
        ItemTypeEnum,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("ItemType", "item_type"),
            serialization_alias="ItemType",
            description="[QUERY] Indicates whether ASIN values or seller SKU values are used to identify items. If you specify Asin, the information in the response will be dependent on the list of Asins you provide in the Asins parameter. If you specify Sku, the information in the response will be dependent on the list of Skus you provide in the Skus parameter.",
        ),
    ]

    item_condition: Annotated[
        Optional[ItemConditionEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("ItemCondition", "item_condition"),
            serialization_alias="ItemCondition",
            description="[QUERY] Filters the offer listings based on item condition. Possible values: New, Used, Collectible, Refurbished, Club.",
        ),
    ]

    offer_type: Annotated[
        Optional[OfferTypeEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("OfferType", "offer_type"),
            serialization_alias="OfferType",
            description="[QUERY] Indicates whether to request pricing information for the seller's B2C or B2B offers. Default is B2C.",
        ),
    ]


PriceList = List["Price"]
"""The payload for the `getPricing` and `getCompetitivePricing` operations."""


"""
GetPricingResponse

The response schema for the `getPricing` and `getCompetitivePricing` operations.
"""


class GetPricingResponse(SpApiBaseModel):
    """The response schema for the `getPricing` and `getCompetitivePricing` operations."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["PriceList"],
        Field(
            None,
            description="The payload for the getPricing and getCompetitivePricing operations.",
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the operation.",
        ),
    ]


"""
SellerSKUIdentifier

Schema to identify an item by MarketPlaceId, SellerId, and SellerSKU.
"""


class SellerSKUIdentifier(SpApiBaseModel):
    """Schema to identify an item by MarketPlaceId, SellerId, and SellerSKU."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceId", "marketplace_id"),
            serialization_alias="MarketplaceId",
            description="A marketplace identifier.",
        ),
    ]

    seller_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("SellerId", "seller_id"),
            serialization_alias="SellerId",
            description="The seller identifier submitted for the operation.",
        ),
    ]

    seller_s_k_u: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("SellerSKU", "seller_s_k_u"),
            serialization_alias="SellerSKU",
            description="The seller stock keeping unit (SKU) of the item.",
        ),
    ]


"""
IdentifierType

Specifies the identifiers used to uniquely identify an item.
"""


class IdentifierType(SpApiBaseModel):
    """Specifies the identifiers used to uniquely identify an item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_a_s_i_n: Annotated[
        Optional["ASINIdentifier"],
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceASIN", "marketplace_a_s_i_n"),
            serialization_alias="MarketplaceASIN",
            description="Indicates the item is identified by MarketPlaceId and ASIN.",
        ),
    ]

    s_k_u_identifier: Annotated[
        Optional["SellerSKUIdentifier"],
        Field(
            None,
            validation_alias=AliasChoices("SKUIdentifier", "s_k_u_identifier"),
            serialization_alias="SKUIdentifier",
            description="Indicates the item is identified by MarketPlaceId, SellerId, and SellerSKU.",
        ),
    ]


"""
ItemOffersRequestBody

List of request parameters can be accepted by `ItemOffersRequests` operation
"""


class ItemOffersRequestBody(SpApiBaseModel):
    """List of request parameters can be accepted by `ItemOffersRequests` operation"""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
ItemOffersRequestParams

List of request parameters that can be accepted by `ItemOffersRequest`
"""


class ItemOffersRequestParams(SpApiBaseModel):
    """List of request parameters that can be accepted by `ItemOffersRequest`"""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
ItemOffersResponse

Schema for an individual `ItemOffersResponse`
"""


class ItemOffersResponse(SpApiBaseModel):
    """Schema for an individual `ItemOffersResponse`"""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
ListingOffersRequestBody

List of request parameters that can be accepted by `ListingOffersRequest` operation
"""


class ListingOffersRequestBody(SpApiBaseModel):
    """List of request parameters that can be accepted by `ListingOffersRequest` operation"""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
ListingOffersRequestParams

List of request parameters that can be accepted by `ListingOffersRequest`
"""


class ListingOffersRequestParams(SpApiBaseModel):
    """List of request parameters that can be accepted by `ListingOffersRequest`"""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
ListingOffersResponse

Schema for an individual `ListingOffersResponse`
"""


class ListingOffersResponse(SpApiBaseModel):
    """Schema for an individual `ListingOffersResponse`"""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
LowestPriceType

Schema for an individual lowest price.
"""


class LowestPriceType(SpApiBaseModel):
    """Schema for an individual lowest price."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    condition: Annotated[
        str,
        Field(
            ...,
            description="Indicates the condition of the item. For example: New, Used, Collectible, Refurbished, or Club.",
        ),
    ]

    fulfillment_channel: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("fulfillmentChannel", "fulfillment_channel"),
            serialization_alias="fulfillmentChannel",
            description="Indicates whether the item is fulfilled by Amazon or by the seller.",
        ),
    ]

    offer_type: Annotated[
        Optional["OfferCustomerType"],
        Field(
            None,
            validation_alias=AliasChoices("offerType", "offer_type"),
            serialization_alias="offerType",
            description="Indicates the type of customer that the offer is valid for.",
        ),
    ]

    quantity_tier: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("quantityTier", "quantity_tier"),
            serialization_alias="quantityTier",
            description="Indicates at what quantity this price becomes active.",
        ),
    ]

    quantity_discount_type: Annotated[
        Optional["QuantityDiscountType"],
        Field(
            None,
            validation_alias=AliasChoices(
                "quantityDiscountType", "quantity_discount_type"
            ),
            serialization_alias="quantityDiscountType",
            description="Indicates the type of quantity discount this price applies to.",
        ),
    ]

    landed_price: Annotated[
        Optional["MoneyType"],
        Field(
            None,
            validation_alias=AliasChoices("LandedPrice", "landed_price"),
            serialization_alias="LandedPrice",
            description="The value calculated by adding ListingPrice + Shipping - Points.",
        ),
    ]

    listing_price: Annotated[
        "MoneyType",
        Field(
            ...,
            validation_alias=AliasChoices("ListingPrice", "listing_price"),
            serialization_alias="ListingPrice",
            description="The price of the item.",
        ),
    ]

    shipping: Annotated[
        Optional["MoneyType"],
        Field(
            None,
            validation_alias=AliasChoices("Shipping", "shipping"),
            serialization_alias="Shipping",
            description="The shipping cost.",
        ),
    ]

    points: Annotated[
        Optional["Points"],
        Field(
            None,
            validation_alias=AliasChoices("Points", "points"),
            serialization_alias="Points",
            description="The number of Amazon Points offered with the purchase of an item.",
        ),
    ]


"""
OfferCountType

The total number of offers for the specified condition and fulfillment channel.
"""


class OfferCountType(SpApiBaseModel):
    """The total number of offers for the specified condition and fulfillment channel."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    condition: Annotated[
        Optional[str],
        Field(
            None,
            description="Indicates the condition of the item. For example: New, Used, Collectible, Refurbished, or Club.",
        ),
    ]

    fulfillment_channel: Annotated[
        Optional["FulfillmentChannelType"],
        Field(
            None,
            validation_alias=AliasChoices("fulfillmentChannel", "fulfillment_channel"),
            serialization_alias="fulfillmentChannel",
            description="Indicates whether the item is fulfilled by Amazon or by the seller.",
        ),
    ]

    offer_count: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("OfferCount", "offer_count"),
            serialization_alias="OfferCount",
            description="The number of offers in a fulfillment channel that meet a specific condition.",
        ),
    ]


"""
PrimeInformationType

Amazon Prime information.
"""


class PrimeInformationType(SpApiBaseModel):
    """Amazon Prime information."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    is_prime: Annotated[
        bool,
        Field(
            ...,
            validation_alias=AliasChoices("IsPrime", "is_prime"),
            serialization_alias="IsPrime",
            description="Indicates whether the offer is an Amazon Prime offer.",
        ),
    ]

    is_national_prime: Annotated[
        bool,
        Field(
            ...,
            validation_alias=AliasChoices("IsNationalPrime", "is_national_prime"),
            serialization_alias="IsNationalPrime",
            description="Indicates whether the offer is an Amazon Prime offer throughout the entire marketplace where it is listed.",
        ),
    ]


"""
QuantityDiscountPriceType

Contains pricing information that includes special pricing when buying in bulk.
"""


class QuantityDiscountPriceType(SpApiBaseModel):
    """Contains pricing information that includes special pricing when buying in bulk."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    quantity_tier: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("quantityTier", "quantity_tier"),
            serialization_alias="quantityTier",
            description="Indicates at what quantity this price becomes active.",
        ),
    ]

    quantity_discount_type: Annotated[
        "QuantityDiscountType",
        Field(
            ...,
            validation_alias=AliasChoices(
                "quantityDiscountType", "quantity_discount_type"
            ),
            serialization_alias="quantityDiscountType",
            description="Indicates the type of quantity discount this price applies to.",
        ),
    ]

    listing_price: Annotated[
        "MoneyType",
        Field(
            ...,
            validation_alias=AliasChoices("listingPrice", "listing_price"),
            serialization_alias="listingPrice",
            description="The price at this quantity tier.",
        ),
    ]


"""
SellerFeedbackType

Information about the seller's feedback, including the percentage of positive feedback, and the total number of ratings received.
"""


class SellerFeedbackType(SpApiBaseModel):
    """Information about the seller's feedback, including the percentage of positive feedback, and the total number of ratings received."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_positive_feedback_rating: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "SellerPositiveFeedbackRating", "seller_positive_feedback_rating"
            ),
            serialization_alias="SellerPositiveFeedbackRating",
            description="The percentage of positive feedback for the seller in the past 365 days.",
        ),
    ]

    feedback_count: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("FeedbackCount", "feedback_count"),
            serialization_alias="FeedbackCount",
            description="The number of ratings received about the seller.",
        ),
    ]


"""
ShipsFromType

The state and country from where the item is shipped.
"""


class ShipsFromType(SpApiBaseModel):
    """The state and country from where the item is shipped."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    state: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("State", "state"),
            serialization_alias="State",
            description="The state from where the item is shipped.",
        ),
    ]

    country: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("Country", "country"),
            serialization_alias="Country",
            description="The country from where the item is shipped.",
        ),
    ]


"""
OfferDetail

Schema for an individual offer. Object in `OfferDetailList`.
"""


class OfferDetail(SpApiBaseModel):
    """Schema for an individual offer. Object in `OfferDetailList`."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    my_offer: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("MyOffer", "my_offer"),
            serialization_alias="MyOffer",
            description="When true, this is the seller's offer.",
        ),
    ]

    offer_type: Annotated[
        Optional["OfferCustomerType"],
        Field(
            None,
            validation_alias=AliasChoices("offerType", "offer_type"),
            serialization_alias="offerType",
            description="Indicates the type of customer that the offer is valid for.",
        ),
    ]

    sub_condition: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("SubCondition", "sub_condition"),
            serialization_alias="SubCondition",
            description="The subcondition of the item. Subcondition values: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty, Refurbished, Open Box, or Other.",
        ),
    ]

    seller_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SellerId", "seller_id"),
            serialization_alias="SellerId",
            description="The seller identifier for the offer.",
        ),
    ]

    condition_notes: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ConditionNotes", "condition_notes"),
            serialization_alias="ConditionNotes",
            description="Information about the condition of the item.",
        ),
    ]

    seller_feedback_rating: Annotated[
        Optional["SellerFeedbackType"],
        Field(
            None,
            validation_alias=AliasChoices(
                "SellerFeedbackRating", "seller_feedback_rating"
            ),
            serialization_alias="SellerFeedbackRating",
            description="Information about the seller's feedback, including the percentage of positive feedback, and the total number of ratings received.",
        ),
    ]

    shipping_time: Annotated[
        "DetailedShippingTimeType",
        Field(
            ...,
            validation_alias=AliasChoices("ShippingTime", "shipping_time"),
            serialization_alias="ShippingTime",
            description="The maximum time within which the item will likely be shipped once an order has been placed.",
        ),
    ]

    listing_price: Annotated[
        "MoneyType",
        Field(
            ...,
            validation_alias=AliasChoices("ListingPrice", "listing_price"),
            serialization_alias="ListingPrice",
            description="The price of the item.",
        ),
    ]

    quantity_discount_prices: Annotated[
        Optional[List["QuantityDiscountPriceType"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "quantityDiscountPrices", "quantity_discount_prices"
            ),
            serialization_alias="quantityDiscountPrices",
            description="List of `QuantityDiscountPrice` that contains item's pricing information when buy in bulk.",
        ),
    ]

    points: Annotated[
        Optional["Points"],
        Field(
            None,
            validation_alias=AliasChoices("Points", "points"),
            serialization_alias="Points",
            description="The number of Amazon Points offered with the purchase of an item.",
        ),
    ]

    shipping: Annotated[
        "MoneyType",
        Field(
            ...,
            validation_alias=AliasChoices("Shipping", "shipping"),
            serialization_alias="Shipping",
            description="The shipping cost.",
        ),
    ]

    ships_from: Annotated[
        Optional["ShipsFromType"],
        Field(
            None,
            validation_alias=AliasChoices("ShipsFrom", "ships_from"),
            serialization_alias="ShipsFrom",
            description="The state and country from where the item is shipped.",
        ),
    ]

    is_fulfilled_by_amazon: Annotated[
        bool,
        Field(
            ...,
            validation_alias=AliasChoices(
                "IsFulfilledByAmazon", "is_fulfilled_by_amazon"
            ),
            serialization_alias="IsFulfilledByAmazon",
            description="When true, the offer is fulfilled by Amazon.",
        ),
    ]

    prime_information: Annotated[
        Optional["PrimeInformationType"],
        Field(
            None,
            validation_alias=AliasChoices("PrimeInformation", "prime_information"),
            serialization_alias="PrimeInformation",
            description="Amazon Prime information.",
        ),
    ]

    is_buy_box_winner: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("IsBuyBoxWinner", "is_buy_box_winner"),
            serialization_alias="IsBuyBoxWinner",
            description="When true, the offer is currently in the Buy Box. There can be up to two Buy Box winners at any time per ASIN, one that is eligible for Prime and one that is not eligible for Prime.",
        ),
    ]

    is_featured_merchant: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("IsFeaturedMerchant", "is_featured_merchant"),
            serialization_alias="IsFeaturedMerchant",
            description="When true, the seller of the item is eligible to win the Buy Box.",
        ),
    ]


"""
OfferListingCountType

The number of offer listings with the specified condition.
"""


class OfferListingCountType(SpApiBaseModel):
    """The number of offer listings with the specified condition."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    count: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("Count", "count"),
            serialization_alias="Count",
            description="The number of offer listings.",
        ),
    ]

    condition: Annotated[str, Field(..., description="The condition of the item.")]


"""
OfferType

Schema for an individual offer.
"""


class OfferType(SpApiBaseModel):
    """Schema for an individual offer."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    offer_type: Annotated[
        Optional["OfferCustomerType"],
        Field(
            None,
            validation_alias=AliasChoices("offerType", "offer_type"),
            serialization_alias="offerType",
            description="Indicates the type of customer that the offer is valid for.",
        ),
    ]

    buying_price: Annotated[
        "PriceType",
        Field(
            ...,
            validation_alias=AliasChoices("BuyingPrice", "buying_price"),
            serialization_alias="BuyingPrice",
            description="Contains pricing information that includes promotions and contains the shipping cost.",
        ),
    ]

    regular_price: Annotated[
        "MoneyType",
        Field(
            ...,
            validation_alias=AliasChoices("RegularPrice", "regular_price"),
            serialization_alias="RegularPrice",
            description="The current price excluding any promotions that apply to the product. Excludes the shipping cost.",
        ),
    ]

    business_price: Annotated[
        Optional["MoneyType"],
        Field(
            None,
            validation_alias=AliasChoices("businessPrice", "business_price"),
            serialization_alias="businessPrice",
            description="The current listing price for Business buyers.",
        ),
    ]

    quantity_discount_prices: Annotated[
        Optional[List["QuantityDiscountPriceType"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "quantityDiscountPrices", "quantity_discount_prices"
            ),
            serialization_alias="quantityDiscountPrices",
            description="List of `QuantityDiscountPrice` that contains item's pricing information when buy in bulk.",
        ),
    ]

    fulfillment_channel: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("FulfillmentChannel", "fulfillment_channel"),
            serialization_alias="FulfillmentChannel",
            description="The fulfillment channel for the offer listing. Possible values: * Amazon - Fulfilled by Amazon. * Merchant - Fulfilled by the seller.",
        ),
    ]

    item_condition: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("ItemCondition", "item_condition"),
            serialization_alias="ItemCondition",
            description="The item condition for the offer listing. Possible values: New, Used, Collectible, Refurbished, or Club.",
        ),
    ]

    item_sub_condition: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("ItemSubCondition", "item_sub_condition"),
            serialization_alias="ItemSubCondition",
            description="The item subcondition for the offer listing. Possible values: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty, Refurbished, Open Box, or Other.",
        ),
    ]

    seller_s_k_u: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("SellerSKU", "seller_s_k_u"),
            serialization_alias="SellerSKU",
            description="The seller stock keeping unit (SKU) of the item.",
        ),
    ]


OffersList = List["OfferType"]
"""A list of offers."""


"""
RelationshipList

A list that contains product variation information, if applicable.
"""


class RelationshipList(SpApiBaseModel):
    """A list that contains product variation information, if applicable."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
Product

An item.
"""


class Product(SpApiBaseModel):
    """An item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    identifiers: Annotated[
        "IdentifierType",
        Field(
            ...,
            validation_alias=AliasChoices("Identifiers", "identifiers"),
            serialization_alias="Identifiers",
        ),
    ]

    attribute_sets: Annotated[
        Optional["AttributeSetList"],
        Field(
            None,
            validation_alias=AliasChoices("AttributeSets", "attribute_sets"),
            serialization_alias="AttributeSets",
        ),
    ]

    relationships: Annotated[
        Optional["RelationshipList"],
        Field(
            None,
            validation_alias=AliasChoices("Relationships", "relationships"),
            serialization_alias="Relationships",
        ),
    ]

    competitive_pricing: Annotated[
        Optional["CompetitivePricingType"],
        Field(
            None,
            validation_alias=AliasChoices("CompetitivePricing", "competitive_pricing"),
            serialization_alias="CompetitivePricing",
        ),
    ]

    sales_rankings: Annotated[
        Optional["SalesRankList"],
        Field(
            None,
            validation_alias=AliasChoices("SalesRankings", "sales_rankings"),
            serialization_alias="SalesRankings",
        ),
    ]

    offers: Annotated[
        Optional["OffersList"],
        Field(
            None,
            validation_alias=AliasChoices("Offers", "offers"),
            serialization_alias="Offers",
        ),
    ]


"""
Price

Schema for price info in `getPricing` response
"""


class Price(SpApiBaseModel):
    """Schema for price info in `getPricing` response"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    status: Annotated[str, Field(..., description="The status of the operation.")]

    seller_s_k_u: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SellerSKU", "seller_s_k_u"),
            serialization_alias="SellerSKU",
            description="The seller stock keeping unit (SKU) of the item.",
        ),
    ]

    a_s_i_n: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ASIN", "a_s_i_n"),
            serialization_alias="ASIN",
            description="The Amazon Standard Identification Number (ASIN) of the item.",
        ),
    ]

    product: Annotated[
        Optional["Product"],
        Field(
            None,
            validation_alias=AliasChoices("Product", "product"),
            serialization_alias="Product",
        ),
    ]


"""
SalesRankType

Sales rank information for the item, by category
"""


class SalesRankType(SpApiBaseModel):
    """Sales rank information for the item, by category"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    product_category_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("ProductCategoryId", "product_category_id"),
            serialization_alias="ProductCategoryId",
            description=" Identifies the item category from which the sales rank is taken.",
        ),
    ]

    rank: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("Rank", "rank"),
            serialization_alias="Rank",
            description="The sales rank of the item within the item category.",
        ),
    ]


# Rebuild models to resolve forward references
GetItemOffersBatchRequestBody.model_rebuild()
GetListingOffersBatchRequestBody.model_rebuild()
BatchOffersRequestParams.model_rebuild()
ItemOffersRequestBody.model_rebuild()
ListingOffersRequestBody.model_rebuild()
GetItemOffersBatchResponse.model_rebuild()
GetListingOffersBatchResponse.model_rebuild()
BatchOffersResponse.model_rebuild()
ItemOffersRequestParams.model_rebuild()
ItemOffersResponse.model_rebuild()
ListingOffersRequestParams.model_rebuild()
ListingOffersResponse.model_rebuild()
Errors.model_rebuild()
GetPricingResponse.model_rebuild()
GetOffersResponse.model_rebuild()
GetOffersResult.model_rebuild()
HttpRequestHeaders.model_rebuild()
HttpResponseHeaders.model_rebuild()
GetOffersHttpStatusLine.model_rebuild()
BatchRequestBody.model_rebuild()
Price.model_rebuild()
Product.model_rebuild()
IdentifierType.model_rebuild()
ASINIdentifier.model_rebuild()
SellerSKUIdentifier.model_rebuild()
AttributeSetList.model_rebuild()
RelationshipList.model_rebuild()
CompetitivePricingType.model_rebuild()
CompetitivePriceType.model_rebuild()
OfferListingCountType.model_rebuild()
MoneyType.model_rebuild()
SalesRankType.model_rebuild()
PriceType.model_rebuild()
OfferType.model_rebuild()
QuantityDiscountPriceType.model_rebuild()
Points.model_rebuild()
ItemIdentifier.model_rebuild()
Summary.model_rebuild()
OfferCountType.model_rebuild()
LowestPriceType.model_rebuild()
BuyBoxPriceType.model_rebuild()
OfferDetail.model_rebuild()
PrimeInformationType.model_rebuild()
SellerFeedbackType.model_rebuild()
DetailedShippingTimeType.model_rebuild()
ShipsFromType.model_rebuild()
Error.model_rebuild()
GetPricingRequest.model_rebuild()
GetCompetitivePricingRequest.model_rebuild()
GetListingOffersRequest.model_rebuild()
GetItemOffersRequest.model_rebuild()
GetItemOffersBatchRequest.model_rebuild()
GetListingOffersBatchRequest.model_rebuild()
