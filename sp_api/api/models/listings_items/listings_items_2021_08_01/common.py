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
Audience

Buyer segment or program this offer is applicable to.
"""


class Audience(SpApiBaseModel):
    """Buyer segment or program this offer is applicable to."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    value: Annotated[
        Optional[str],
        Field(
            None,
            description="Name of the audience an offer is applicable to. Common values: * 'ALL' - Standard offer audience for buyers on Amazon retail websites. * 'B2B' - Offer audience for Amazon Business website buyers.",
        ),
    ]

    display_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("displayName", "display_name"),
            serialization_alias="displayName",
            description="Localized display name for the audience.",
        ),
    ]


Decimal = str
"""A decimal number with no loss of precision. Useful when precision loss is unnaceptable, as with currencies. Follows RFC7159 for number representation."""


"""
DeleteListingsItemRequest

Request parameters for deleteListingsItem
"""


class DeleteListingsItemRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for deleteListingsItem
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("sellerId", "seller_id"),
            serialization_alias="sellerId",
            description="[PATH] A selling partner identifier, such as a merchant account or vendor code.",
        ),
    ]

    sku: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            description="[PATH] A selling partner provided identifier for an Amazon listing.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A comma-delimited list of Amazon marketplace identifiers for the request.",
        ),
    ]

    issue_locale: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("issueLocale", "issue_locale"),
            serialization_alias="issueLocale",
            description="[QUERY] A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: `en_US`, `fr_CA`, `fr_FR`. Localized messages default to `en_US` when a localization is not available in the specified locale.",
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
        ),
    ]


"""
FulfillmentAvailability

The fulfillment availability details for the listings item.
"""


class FulfillmentAvailability(SpApiBaseModel):
    """The fulfillment availability details for the listings item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    fulfillment_channel_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "fulfillmentChannelCode", "fulfillment_channel_code"
            ),
            serialization_alias="fulfillmentChannelCode",
            description="Designates which fulfillment network is used.",
        ),
    ]

    quantity: Annotated[
        Optional[int],
        Field(
            None,
            description="The quantity of the item you are making available for sale.",
        ),
    ]


# Enum definitions
class IncludedDataEnum(str, Enum):
    """Enum for includedData"""

    SUMMARIES = "summaries"  # Summary details for the listing item.
    ATTRIBUTES = "attributes"  # A JSON object that contains structured listing item attribute data, keyed by attribute name.
    ISSUES = "issues"  # Issues that are associated with the listing item.
    OFFERS = "offers"  # Current offers for the listing item.
    FULFILLMENT_AVAILABILITY = "fulfillmentAvailability"  # Fulfillment availability details for the listing item.
    PROCUREMENT = "procurement"  # Vendor procurement details for the listing item.
    RELATIONSHIPS = "relationships"  # Relationship details for a listing item (for example, variations).
    PRODUCT_TYPES = "productTypes"  # Product types associated with a listing item.


"""
GetListingsItemRequest

Request parameters for getListingsItem
"""


class GetListingsItemRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getListingsItem
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("sellerId", "seller_id"),
            serialization_alias="sellerId",
            description="[PATH] A selling partner identifier, such as a merchant account or vendor code.",
        ),
    ]

    sku: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            description="[PATH] A selling partner provided identifier for an Amazon listing.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A comma-delimited list of Amazon marketplace identifiers for the request.",
        ),
    ]

    issue_locale: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("issueLocale", "issue_locale"),
            serialization_alias="issueLocale",
            description="[QUERY] A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: `en_US`, `fr_CA`, `fr_FR`. Localized messages default to `en_US` when a localization is not available in the specified locale.",
        ),
    ]

    included_data: Annotated[
        Optional[List["IncludedDataEnum"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("includedData", "included_data"),
            serialization_alias="includedData",
            description="[QUERY] A comma-delimited list of data sets to include in the response. Default: `summaries`.",
        ),
    ]


"""
IssueEnforcementAction

The enforcement action taken by Amazon that affect the publishing or status of a listing
"""


class IssueEnforcementAction(SpApiBaseModel):
    """The enforcement action taken by Amazon that affect the publishing or status of a listing"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    action: Annotated[
        str,
        Field(
            ...,
            description="The enforcement action name. Possible values: * `LISTING_SUPPRESSED` - This enforcement takes down the current listing item's buyability. * `ATTRIBUTE_SUPPRESSED` - An attribute's value on the listing item is invalid, which causes it to be rejected by Amazon. * `CATALOG_ITEM_REMOVED` - This catalog item is inactive on Amazon, and all offers against it in the applicable marketplace are non-buyable. * `SEARCH_SUPPRESSED` - This value indicates that the catalog item is hidden from search results.",
        ),
    ]


# Enum definitions
class StatusEnum(str, Enum):
    """Enum for status"""

    ACCEPTED = "ACCEPTED"  # The listings submission was accepted for processing.
    INVALID = "INVALID"  # The listings submission was not valid and was not accepted for processing.
    VALID = "VALID"  # The listings submission was valid. Only returned when the `mode` is `VALIDATION_PREVIEW`.


"""
IssueExemption

Conveying the status of the listed enforcement actions and, if applicable, provides information about the exemption's expiry date.
"""


class IssueExemption(SpApiBaseModel):
    """Conveying the status of the listed enforcement actions and, if applicable, provides information about the exemption's expiry date."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    status: Annotated[
        StatusEnum,
        Field(
            ...,
            description="This field indicates the current exemption status for the listed enforcement actions. It can take values such as `EXEMPT`, signifying permanent exemption, `EXEMPT_UNTIL_EXPIRY_DATE` indicating temporary exemption until a specified date, or `NOT_EXEMPT` signifying no exemptions, and enforcement actions were already applied.",
        ),
    ]

    expiry_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("expiryDate", "expiry_date"),
            serialization_alias="expiryDate",
            description="Represents the timestamp, in ISO 8601 format, that specifies the date when the temporary exemptions expires, and Amazon begins enforcing the listed actions.",
        ),
    ]


"""
IssueEnforcements

This field provides information about the enforcement actions taken by Amazon that affect the publishing or status of a listing. It also includes details about any associated exemptions.
"""


class IssueEnforcements(SpApiBaseModel):
    """This field provides information about the enforcement actions taken by Amazon that affect the publishing or status of a listing. It also includes details about any associated exemptions."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    actions: Annotated[
        List["IssueEnforcementAction"],
        Field(
            ...,
            description="List of enforcement actions taken by Amazon that affect the publishing or status of a listing.",
        ),
    ]

    exemption: Annotated[
        "IssueExemption",
        Field(
            ...,
            description="The 'exemption' field serves to convey the status of enforcement actions by Amazon.",
        ),
    ]


# Enum definitions
class SeverityEnum(str, Enum):
    """Enum for severity"""

    ERROR = "ERROR"  # Indicates an issue has occurred preventing the submission from processing, such as a validation error.
    WARNING = "WARNING"  # Indicates an issue has occurred that should be reviewed, but has not prevented the submission from processing.
    INFO = "INFO"  # Indicates additional information has been provided that should be reviewed.


"""
Issue

An issue with a listings item.
"""


class Issue(SpApiBaseModel):
    """An issue with a listings item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    code: Annotated[
        str, Field(..., description="An issue code that identifies the type of issue.")
    ]

    message: Annotated[
        str, Field(..., description="A message that describes the issue.")
    ]

    severity: Annotated[
        SeverityEnum, Field(..., description="The severity of the issue.")
    ]

    attribute_names: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("attributeNames", "attribute_names"),
            serialization_alias="attributeNames",
            description="The names of the attributes associated with the issue, if applicable.",
        ),
    ]

    categories: Annotated[
        List["str"],
        Field(
            ...,
            description="List of issue categories. Possible values: * 'INVALID_ATTRIBUTE' - Indicating an invalid attribute in the listing. * 'MISSING_ATTRIBUTE' - Highlighting a missing attribute in the listing. * 'INVALID_IMAGE' - Signifying an invalid image in the listing. * 'MISSING_IMAGE' - Noting the absence of an image in the listing. * 'INVALID_PRICE' - Pertaining to issues with the listing's price-related attributes. * 'MISSING_PRICE' - Pointing out the absence of a price attribute in the listing. * 'DUPLICATE' - Identifying listings with potential duplicate problems, such as this ASIN potentially being a duplicate of another ASIN. * 'QUALIFICATION_REQUIRED' - Indicating that the listing requires qualification-related approval.",
        ),
    ]

    enforcements: Annotated[
        Optional["IssueEnforcements"],
        Field(
            None,
            description="This field provides information about the enforcement actions taken by Amazon that affect the publishing or status of a listing. It also includes details about any associated exemptions.",
        ),
    ]


"""
ItemAttributes

A JSON object containing structured listings item attribute data keyed by attribute name.
"""


class ItemAttributes(SpApiBaseModel):
    """A JSON object containing structured listings item attribute data keyed by attribute name."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


ItemIssues = List["Issue"]
"""The issues associated with the listings item."""


ItemOffers = List["ItemOfferByMarketplace"]
"""Offer details for the listings item."""


"""
Money

The currency type and amount.
"""


class Money(SpApiBaseModel):
    """The currency type and amount."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    currency_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("currencyCode", "currency_code"),
            serialization_alias="currencyCode",
            description="Three-digit currency code in ISO 4217 format.",
        ),
    ]

    amount: Annotated["Decimal", Field(..., description="The currency amount.")]


"""
ItemProcurement

The vendor procurement information for the listings item.
"""


class ItemProcurement(SpApiBaseModel):
    """The vendor procurement information for the listings item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    cost_price: Annotated[
        "Money",
        Field(
            ...,
            validation_alias=AliasChoices("costPrice", "cost_price"),
            serialization_alias="costPrice",
            description="The price (numeric value) that you want Amazon to pay you for this product.",
        ),
    ]


ItemProductTypes = List["ItemProductTypeByMarketplace"]
"""Product types for a listing item, by marketplace."""


ItemRelationships = List["ItemRelationshipsByMarketplace"]
"""Relationships for a listing item, by marketplace (for example, variations)."""


ItemSummaries = List["ItemSummaryByMarketplace"]
"""Summary details of a listings item."""


"""
Item

A listings item.
"""


class Item(SpApiBaseModel):
    """A listings item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    sku: Annotated[
        str,
        Field(
            ...,
            description="A selling partner provided identifier for an Amazon listing.",
        ),
    ]

    summaries: Annotated[
        Optional["ItemSummaries"],
        Field(
            None,
        ),
    ]

    attributes: Annotated[
        Optional["ItemAttributes"],
        Field(
            None,
        ),
    ]

    issues: Annotated[
        Optional["ItemIssues"],
        Field(
            None,
        ),
    ]

    offers: Annotated[
        Optional["ItemOffers"],
        Field(
            None,
        ),
    ]

    fulfillment_availability: Annotated[
        Optional[List["FulfillmentAvailability"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "fulfillmentAvailability", "fulfillment_availability"
            ),
            serialization_alias="fulfillmentAvailability",
            description="The fulfillment availability for the listings item.",
        ),
    ]

    procurement: Annotated[
        Optional[List["ItemProcurement"]],
        Field(
            None,
            description="The vendor procurement information for the listings item.",
        ),
    ]

    relationships: Annotated[
        Optional["ItemRelationships"],
        Field(
            None,
        ),
    ]

    product_types: Annotated[
        Optional["ItemProductTypes"],
        Field(
            None,
            validation_alias=AliasChoices("productTypes", "product_types"),
            serialization_alias="productTypes",
        ),
    ]


ItemIdentifiers = List["ItemIdentifiersByMarketplace"]
"""Identity attributes associated with the item in the Amazon catalog, such as the ASIN."""


"""
ItemIdentifiersByMarketplace

Identity attributes associated with the item in the Amazon catalog for the indicated Amazon marketplace.
"""


class ItemIdentifiersByMarketplace(SpApiBaseModel):
    """Identity attributes associated with the item in the Amazon catalog for the indicated Amazon marketplace."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="A marketplace identifier. Identifies the Amazon marketplace for the listings item.",
        ),
    ]

    asin: Annotated[
        Optional[str],
        Field(
            None,
            description="Amazon Standard Identification Number (ASIN) of the listings item.",
        ),
    ]


"""
ItemImage

The image for the listings item.
"""


class ItemImage(SpApiBaseModel):
    """The image for the listings item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    link: Annotated[str, Field(..., description="The link, or URL, to the image.")]

    height: Annotated[int, Field(..., description="The height of the image in pixels.")]

    width: Annotated[int, Field(..., description="The width of the image in pixels.")]


"""
Points

The number of Amazon Points offered with the purchase of an item, and their monetary value. Note that the `Points` element is only returned in Japan (JP).
"""


class Points(SpApiBaseModel):
    """The number of Amazon Points offered with the purchase of an item, and their monetary value. Note that the `Points` element is only returned in Japan (JP)."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    points_number: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("pointsNumber", "points_number"),
            serialization_alias="pointsNumber",
        ),
    ]


# Enum definitions
class OfferTypeEnum(str, Enum):
    """Enum for offerType"""

    B2_C = "B2C"  # The offer on this listings item is available for Business to Consumer purchase, meaning that it is available to shoppers on Amazon retail sites.
    B2_B = "B2B"  # The offer on this listings item is available for Business to Business purchase.


"""
ItemOfferByMarketplace

Offer details of a listings item for an Amazon marketplace.
"""


class ItemOfferByMarketplace(SpApiBaseModel):
    """Offer details of a listings item for an Amazon marketplace."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The Amazon marketplace identifier.",
        ),
    ]

    offer_type: Annotated[
        OfferTypeEnum,
        Field(
            ...,
            validation_alias=AliasChoices("offerType", "offer_type"),
            serialization_alias="offerType",
            description="Type of offer for the listings item.",
        ),
    ]

    price: Annotated[
        "Money", Field(..., description="The purchase price of the listings item")
    ]

    points: Annotated[
        Optional["Points"],
        Field(
            None,
        ),
    ]

    audience: Annotated[
        Optional["Audience"],
        Field(
            None, description="Buyer segment or program this offer is applicable to."
        ),
    ]


"""
ItemProductTypeByMarketplace

Product types that are associated with the listing item for the specified marketplace.
"""


class ItemProductTypeByMarketplace(SpApiBaseModel):
    """Product types that are associated with the listing item for the specified marketplace."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="Amazon marketplace identifier.",
        ),
    ]

    product_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("productType", "product_type"),
            serialization_alias="productType",
            description="The name of the product type that is submitted by the Selling Partner.",
        ),
    ]


"""
ItemVariationTheme

A variation theme that indicates the combination of listing item attributes that define the variation family.
"""


class ItemVariationTheme(SpApiBaseModel):
    """A variation theme that indicates the combination of listing item attributes that define the variation family."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    attributes: Annotated[
        List["str"],
        Field(
            ...,
            description="The names of the listing item attributes that are associated with the variation theme.",
        ),
    ]

    theme: Annotated[
        str,
        Field(
            ...,
            description="The variation theme that indicates the combination of listing item attributes that define the variation family.",
        ),
    ]


# Enum definitions
class TypeEnum(str, Enum):
    """Enum for type"""

    VARIATION = "VARIATION"  # The listing item in the request is a variation parent or variation child of the related listing items, indicated by SKU.
    PACKAGE_HIERARCHY = "PACKAGE_HIERARCHY"  # The listing item in the request is a package container or is contained by the related listing items, indicated by SKU.


"""
ItemRelationship

The relationship details for a listing item.
"""


class ItemRelationship(SpApiBaseModel):
    """The relationship details for a listing item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    child_skus: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("childSkus", "child_skus"),
            serialization_alias="childSkus",
            description="Identifiers (SKUs) of the related items that are children of this listing item.",
        ),
    ]

    parent_skus: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("parentSkus", "parent_skus"),
            serialization_alias="parentSkus",
            description="Identifiers (SKUs) of the related items that are parents of this listing item.",
        ),
    ]

    variation_theme: Annotated[
        Optional["ItemVariationTheme"],
        Field(
            None,
            validation_alias=AliasChoices("variationTheme", "variation_theme"),
            serialization_alias="variationTheme",
            description="For `VARIATION` relationships, the variation theme is the combination of listing item attributes that define the variation family.",
        ),
    ]

    type: Annotated[TypeEnum, Field(..., description="The type of relationship.")]


"""
ItemRelationshipsByMarketplace

Relationship details for the listing item in the specified marketplace.
"""


class ItemRelationshipsByMarketplace(SpApiBaseModel):
    """Relationship details for the listing item in the specified marketplace."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="Amazon marketplace identifier.",
        ),
    ]

    relationships: Annotated[
        List["ItemRelationship"],
        Field(..., description="Relationships for the listing item."),
    ]


"""
Pagination

When a request produces a response that exceeds the `pageSize`, pagination occurs. This means the response is divided into individual pages. To retrieve the next page or the previous page, you must pass the `nextToken` value or the `previousToken` value as the `pageToken` parameter in the next request. When you receive the last page, there is no `nextToken` key in the pagination object.
"""


class Pagination(SpApiBaseModel):
    """When a request produces a response that exceeds the `pageSize`, pagination occurs. This means the response is divided into individual pages. To retrieve the next page or the previous page, you must pass the `nextToken` value or the `previousToken` value as the `pageToken` parameter in the next request. When you receive the last page, there is no `nextToken` key in the pagination object."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    next_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="A token that can be used to fetch the next page.",
        ),
    ]

    previous_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("previousToken", "previous_token"),
            serialization_alias="previousToken",
            description="A token that can be used to fetch the previous page.",
        ),
    ]


"""
ItemSearchResults

Selling partner listings items and search related metadata.
"""


class ItemSearchResults(SpApiBaseModel):
    """Selling partner listings items and search related metadata."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    number_of_results: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("numberOfResults", "number_of_results"),
            serialization_alias="numberOfResults",
            description="The total number of selling partner listings items found for the search criteria (only results up to the page count limit is returned per request regardless of the number found). Note: The maximum number of items (SKUs) that can be returned and paged through is 1000.",
        ),
    ]

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
            description="If available, the `nextToken` and/or `previousToken` values required to return paginated results.",
        ),
    ]

    items: Annotated[List["Item"], Field(..., description="A list of listings items.")]


# Enum definitions
class ConditionTypeEnum(str, Enum):
    """Enum for conditionType"""

    NEW_NEW = "new_new"  # New.
    NEW_OPEN_BOX = "new_open_box"  # New - Open Box.
    NEW_OEM = "new_oem"  # New - OEM.
    REFURBISHED_REFURBISHED = "refurbished_refurbished"  # Refurbished.
    USED_LIKE_NEW = "used_like_new"  # Used - Like New.
    USED_VERY_GOOD = "used_very_good"  # Used - Very Good.
    USED_GOOD = "used_good"  # Used - Good.
    USED_ACCEPTABLE = "used_acceptable"  # Used - Acceptable.
    COLLECTIBLE_LIKE_NEW = "collectible_like_new"  # Collectible - Like New.
    COLLECTIBLE_VERY_GOOD = "collectible_very_good"  # Collectible - Very Good.
    COLLECTIBLE_GOOD = "collectible_good"  # Collectible - Good.
    COLLECTIBLE_ACCEPTABLE = "collectible_acceptable"  # Collectible - Acceptable.
    CLUB_CLUB = "club_club"  # Club.


class StatusEnum(str, Enum):
    """Enum for status"""

    ACCEPTED = "ACCEPTED"  # The listings submission was accepted for processing.
    INVALID = "INVALID"  # The listings submission was not valid and was not accepted for processing.
    VALID = "VALID"  # The listings submission was valid. Only returned when the `mode` is `VALIDATION_PREVIEW`.


"""
ItemSummaryByMarketplace

Summary details of a listings item for an Amazon marketplace.
"""


class ItemSummaryByMarketplace(SpApiBaseModel):
    """Summary details of a listings item for an Amazon marketplace."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="A marketplace identifier. Identifies the Amazon marketplace for the listings item.",
        ),
    ]

    asin: Annotated[
        Optional[str],
        Field(
            None,
            description="Amazon Standard Identification Number (ASIN) of the listings item.",
        ),
    ]

    product_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("productType", "product_type"),
            serialization_alias="productType",
            description="The Amazon product type of the listings item.",
        ),
    ]

    condition_type: Annotated[
        Optional[ConditionTypeEnum],
        Field(
            None,
            validation_alias=AliasChoices("conditionType", "condition_type"),
            serialization_alias="conditionType",
            description="Identifies the condition of the listings item.",
        ),
    ]

    status: Annotated[
        List["StatusEnum"],
        Field(..., description="Statuses that apply to the listings item."),
    ]

    fn_sku: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("fnSku", "fn_sku"),
            serialization_alias="fnSku",
            description="The fulfillment network stock keeping unit is an identifier used by Amazon fulfillment centers to identify each unique item.",
        ),
    ]

    item_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("itemName", "item_name"),
            serialization_alias="itemName",
            description="The name or title associated with an Amazon catalog item.",
        ),
    ]

    created_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("createdDate", "created_date"),
            serialization_alias="createdDate",
            description="The date the listings item was created in ISO 8601 format.",
        ),
    ]

    last_updated_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("lastUpdatedDate", "last_updated_date"),
            serialization_alias="lastUpdatedDate",
            description="The date the listings item was last updated in ISO 8601 format.",
        ),
    ]

    main_image: Annotated[
        Optional["ItemImage"],
        Field(
            None,
            validation_alias=AliasChoices("mainImage", "main_image"),
            serialization_alias="mainImage",
            description="The main image for the listings item.",
        ),
    ]


# Enum definitions
class OpEnum(str, Enum):
    """Enum for op"""

    ADD = "add"  # The `add` operation adds or replaces the target property.
    REPLACE = "replace"  # The `replace` operation adds or replaces the target property.
    MERGE = "merge"  # The `merge` operation merges the target property.
    DELETE = "delete"  # The `delete` operation removes the target property. Not supported for vendors (vendors will receive an HTTP status code 400 response).


"""
PatchOperation

Individual JSON Patch operation for an HTTP PATCH request.
"""


class PatchOperation(SpApiBaseModel):
    """Individual JSON Patch operation for an HTTP PATCH request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    op: Annotated[
        OpEnum,
        Field(
            ...,
            description="Type of JSON Patch operation. Supported JSON Patch operations include `add`, `replace`, `merge` and `delete`. Refer to <https://tools.ietf.org/html/rfc6902>.",
        ),
    ]

    path: Annotated[
        str,
        Field(
            ...,
            description="JSON Pointer path of the element to patch. Refer to [JavaScript Object Notation (JSON) Patch](https://tools.ietf.org/html/rfc6902) for more information.",
        ),
    ]

    value: Annotated[
        Optional[List[Dict[str, Any]]],
        Field(None, description="JSON value to `add`, `replace`, `merge` or `delete`."),
    ]


"""
ListingsItemPatchRequestBody

The request body schema for the `patchListingsItem` operation.
"""


class ListingsItemPatchRequestBody(SpApiBaseModel):
    """The request body schema for the `patchListingsItem` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    product_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("productType", "product_type"),
            serialization_alias="productType",
            description="The Amazon product type of the listings item.",
        ),
    ]

    patches: Annotated[
        List["PatchOperation"],
        Field(
            ...,
            description="One or more JSON Patch operations to perform on the listings item.",
        ),
    ]


# Enum definitions
class RequirementsEnum(str, Enum):
    """Enum for requirements"""

    LISTING = "LISTING"  # Indicates the submitted data contains product facts and sales terms.
    LISTING_PRODUCT_ONLY = "LISTING_PRODUCT_ONLY"  # Indicates the submitted data contains product facts only.
    LISTING_OFFER_ONLY = "LISTING_OFFER_ONLY"  # Indicates the submitted data contains sales terms only. Not supported for vendors (vendors will receive an HTTP status code 400 response).


"""
ListingsItemPutRequestBody

The request body schema for the `putListingsItem` operation.
"""


class ListingsItemPutRequestBody(SpApiBaseModel):
    """The request body schema for the `putListingsItem` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    product_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("productType", "product_type"),
            serialization_alias="productType",
            description="The Amazon product type of the listings item.",
        ),
    ]

    requirements: Annotated[
        Optional[RequirementsEnum],
        Field(
            None, description="The name of the requirements set for the provided data."
        ),
    ]

    attributes: Annotated[
        Dict[str, Any],
        Field(
            ...,
            description="A JSON object containing structured listings item attribute data keyed by attribute name.",
        ),
    ]


# Enum definitions
class StatusEnum(str, Enum):
    """Enum for status"""

    ACCEPTED = "ACCEPTED"  # The listings submission was accepted for processing.
    INVALID = "INVALID"  # The listings submission was not valid and was not accepted for processing.
    VALID = "VALID"  # The listings submission was valid. Only returned when the `mode` is `VALIDATION_PREVIEW`.


"""
ListingsItemSubmissionResponse

Response containing the results of a submission to the Selling Partner API for Listings Items.
"""


class ListingsItemSubmissionResponse(SpApiBaseModel):
    """Response containing the results of a submission to the Selling Partner API for Listings Items."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    sku: Annotated[
        str,
        Field(
            ...,
            description="A selling partner provided identifier for an Amazon listing.",
        ),
    ]

    status: Annotated[
        StatusEnum,
        Field(..., description="The status of the listings item submission."),
    ]

    submission_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("submissionId", "submission_id"),
            serialization_alias="submissionId",
            description="The unique identifier of the listings item submission.",
        ),
    ]

    issues: Annotated[
        Optional[List["Issue"]],
        Field(
            None,
            description="Listings item issues related to the listings item submission.",
        ),
    ]

    identifiers: Annotated[
        Optional["ItemIdentifiers"],
        Field(
            None,
            description="Identity attributes associated with the item in the Amazon catalog, such as the ASIN.",
        ),
    ]


# Enum definitions
class IncludedDataEnum(str, Enum):
    """Enum for includedData"""

    SUMMARIES = "summaries"  # Summary details for the listing item.
    ATTRIBUTES = "attributes"  # A JSON object that contains structured listing item attribute data, keyed by attribute name.
    ISSUES = "issues"  # Issues that are associated with the listing item.
    OFFERS = "offers"  # Current offers for the listing item.
    FULFILLMENT_AVAILABILITY = "fulfillmentAvailability"  # Fulfillment availability details for the listing item.
    PROCUREMENT = "procurement"  # Vendor procurement details for the listing item.
    RELATIONSHIPS = "relationships"  # Relationship details for a listing item (for example, variations).
    PRODUCT_TYPES = "productTypes"  # Product types associated with a listing item.


class ModeEnum(str, Enum):
    """Enum for mode"""

    VALIDATION_PREVIEW = "VALIDATION_PREVIEW"  # Indicates the submitted data should be validated using the values provided in the payload and validation errors the selling partner account may face. This will synchronously perform the same checks that are preformed on submissions after being accepted for processing, but without persisting to the selling partner's catalog.


"""
PatchListingsItemRequest

Request parameters for patchListingsItem
"""


class PatchListingsItemRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for patchListingsItem
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("sellerId", "seller_id"),
            serialization_alias="sellerId",
            description="[PATH] A selling partner identifier, such as a merchant account or vendor code.",
        ),
    ]

    sku: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            description="[PATH] A selling partner provided identifier for an Amazon listing.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A comma-delimited list of Amazon marketplace identifiers for the request.",
        ),
    ]

    included_data: Annotated[
        Optional[List["IncludedDataEnum"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("includedData", "included_data"),
            serialization_alias="includedData",
            description="[QUERY] A comma-delimited list of data sets to include in the response. Default: `issues`.",
        ),
    ]

    mode: Annotated[
        Optional[ModeEnum],
        QueryParam(),
        Field(None, description="[QUERY] The mode of operation for the request."),
    ]

    issue_locale: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("issueLocale", "issue_locale"),
            serialization_alias="issueLocale",
            description="[QUERY] A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: `en_US`, `fr_CA`, `fr_FR`. Localized messages default to `en_US` when a localization is not available in the specified locale.",
        ),
    ]

    body: Annotated[
        "ListingsItemPatchRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The request body schema for the `patchListingsItem` operation.",
        ),
    ]


# Enum definitions
class IncludedDataEnum(str, Enum):
    """Enum for includedData"""

    SUMMARIES = "summaries"  # Summary details for the listing item.
    ATTRIBUTES = "attributes"  # A JSON object that contains structured listing item attribute data, keyed by attribute name.
    ISSUES = "issues"  # Issues that are associated with the listing item.
    OFFERS = "offers"  # Current offers for the listing item.
    FULFILLMENT_AVAILABILITY = "fulfillmentAvailability"  # Fulfillment availability details for the listing item.
    PROCUREMENT = "procurement"  # Vendor procurement details for the listing item.
    RELATIONSHIPS = "relationships"  # Relationship details for a listing item (for example, variations).
    PRODUCT_TYPES = "productTypes"  # Product types associated with a listing item.


class ModeEnum(str, Enum):
    """Enum for mode"""

    VALIDATION_PREVIEW = "VALIDATION_PREVIEW"  # Indicates the submitted data should be validated using the values provided in the payload and validation errors the selling partner account may face. This will synchronously perform the same checks that are preformed on submissions after being accepted for processing, but without persisting to the selling partner's catalog.


"""
PutListingsItemRequest

Request parameters for putListingsItem
"""


class PutListingsItemRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for putListingsItem
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("sellerId", "seller_id"),
            serialization_alias="sellerId",
            description="[PATH] A selling partner identifier, such as a merchant account or vendor code.",
        ),
    ]

    sku: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            description="[PATH] A selling partner provided identifier for an Amazon listing.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A comma-delimited list of Amazon marketplace identifiers for the request.",
        ),
    ]

    included_data: Annotated[
        Optional[List["IncludedDataEnum"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("includedData", "included_data"),
            serialization_alias="includedData",
            description="[QUERY] A comma-delimited list of data sets to include in the response. Default: `issues`.",
        ),
    ]

    mode: Annotated[
        Optional[ModeEnum],
        QueryParam(),
        Field(None, description="[QUERY] The mode of operation for the request."),
    ]

    issue_locale: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("issueLocale", "issue_locale"),
            serialization_alias="issueLocale",
            description="[QUERY] A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: `en_US`, `fr_CA`, `fr_FR`. Localized messages default to `en_US` when a localization is not available in the specified locale.",
        ),
    ]

    body: Annotated[
        "ListingsItemPutRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The request body schema for the `putListingsItem` operation.",
        ),
    ]


# Enum definitions
class IncludedDataEnum(str, Enum):
    """Enum for includedData"""

    SUMMARIES = "summaries"  # Summary details for the listing item.
    ATTRIBUTES = "attributes"  # A JSON object that contains structured listing item attribute data, keyed by attribute name.
    ISSUES = "issues"  # Issues that are associated with the listing item.
    OFFERS = "offers"  # Current offers for the listing item.
    FULFILLMENT_AVAILABILITY = "fulfillmentAvailability"  # Fulfillment availability details for the listing item.
    PROCUREMENT = "procurement"  # Vendor procurement details for the listing item.
    RELATIONSHIPS = "relationships"  # Relationship details for a listing item (for example, variations).
    PRODUCT_TYPES = "productTypes"  # Product types associated with a listing item.


class IdentifiersTypeEnum(str, Enum):
    """Enum for identifiersType"""

    ASIN = "ASIN"  # Amazon Standard Identification Number.
    EAN = "EAN"  # European Article Number.
    FNSKU = "FNSKU"  # Fulfillment Network Stock Keeping Unit.
    GTIN = "GTIN"  # Global Trade Item Number.
    ISBN = "ISBN"  # International Standard Book Number.
    JAN = "JAN"  # Japanese Article Number.
    MINSAN = "MINSAN"  # Minsan Code.
    SKU = "SKU"  # Stock Keeping Unit (SKU): A seller-specified identifier for an Amazon listing.
    UPC = "UPC"  # Universal Product Code.


class WithIssueSeverityEnum(str, Enum):
    """Enum for withIssueSeverity"""

    WARNING = "WARNING"  # Indicates an issue has occurred that should be reviewed, but it has not prevented the submission from processing.
    ERROR = "ERROR"  # Indicates that an issue has occurred, which prevented the submission from processing. For example, a validation error.


class WithStatusEnum(str, Enum):
    """Enum for withStatus"""

    BUYABLE = "BUYABLE"  # The listings item that shoppers can purchase. This status does not apply to vendor listings.
    DISCOVERABLE = "DISCOVERABLE"  # The listings item is visible to shoppers.


class WithoutStatusEnum(str, Enum):
    """Enum for withoutStatus"""

    BUYABLE = "BUYABLE"  # The listings item can be purchased by shoppers. This status does not apply to vendor listings.
    DISCOVERABLE = "DISCOVERABLE"  # The listings item is visible to shoppers.


class SortByEnum(str, Enum):
    """Enum for sortBy"""

    SKU = "sku"  # Stock Keeping Unit, a seller-specified identifier for an Amazon listing.
    CREATED_DATE = "createdDate"  # The date when the listing item was created. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.
    LAST_UPDATED_DATE = "lastUpdatedDate"  # The date when the listing item was last updated. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.


class SortOrderEnum(str, Enum):
    """Enum for sortOrder"""

    ASC = "ASC"  # Ascending order.
    DESC = "DESC"  # Descending order.


"""
SearchListingsItemsRequest

Request parameters for searchListingsItems
"""


class SearchListingsItemsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for searchListingsItems
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("sellerId", "seller_id"),
            serialization_alias="sellerId",
            description="[PATH] A selling partner identifier, such as a merchant account or vendor code.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A comma-delimited list of Amazon marketplace identifiers for the request.",
        ),
    ]

    issue_locale: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("issueLocale", "issue_locale"),
            serialization_alias="issueLocale",
            description="[QUERY] A locale that is used to localize issues. When not provided, the default language code of the first marketplace is used. Examples: 'en_US', 'fr_CA', 'fr_FR'. When a localization is not available in the specified locale, localized messages default to 'en_US'.",
        ),
    ]

    included_data: Annotated[
        Optional[List["IncludedDataEnum"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("includedData", "included_data"),
            serialization_alias="includedData",
            description="[QUERY] A comma-delimited list of datasets that you want to include in the response. Default: `summaries`.",
        ),
    ]

    identifiers: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            description="[QUERY] A comma-delimited list of product identifiers that you can use to search for listings items.   **Note**:  1. This is required when you specify `identifiersType`. 2. You cannot use 'identifiers' if you specify `variationParentSku` or `packageHierarchySku`.",
        ),
    ]

    identifiers_type: Annotated[
        Optional[IdentifiersTypeEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("identifiersType", "identifiers_type"),
            serialization_alias="identifiersType",
            description="[QUERY] A type of product identifiers that you can use to search for listings items.   **Note**:  This is required when `identifiers` is provided.",
        ),
    ]

    variation_parent_sku: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("variationParentSku", "variation_parent_sku"),
            serialization_alias="variationParentSku",
            description="[QUERY] Filters results to include listing items that are variation children of the specified SKU.   **Note**: You cannot use `variationParentSku` if you include `identifiers` or `packageHierarchySku` in your request.",
        ),
    ]

    package_hierarchy_sku: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "packageHierarchySku", "package_hierarchy_sku"
            ),
            serialization_alias="packageHierarchySku",
            description="[QUERY] Filter results to include listing items that contain or are contained by the specified SKU.   **Note**: You cannot use `packageHierarchySku` if you include `identifiers` or `variationParentSku` in your request.",
        ),
    ]

    created_after: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("createdAfter", "created_after"),
            serialization_alias="createdAfter",
            description="[QUERY] A date-time that is used to filter listing items. The response includes listings items that were created at or after this time. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.",
        ),
    ]

    created_before: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("createdBefore", "created_before"),
            serialization_alias="createdBefore",
            description="[QUERY] A date-time that is used to filter listing items. The response includes listings items that were created at or before this time. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.",
        ),
    ]

    last_updated_after: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("lastUpdatedAfter", "last_updated_after"),
            serialization_alias="lastUpdatedAfter",
            description="[QUERY] A date-time that is used to filter listing items. The response includes listings items that were last updated at or after this time. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.",
        ),
    ]

    last_updated_before: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("lastUpdatedBefore", "last_updated_before"),
            serialization_alias="lastUpdatedBefore",
            description="[QUERY] A date-time that is used to filter listing items. The response includes listings items that were last updated at or before this time. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.",
        ),
    ]

    with_issue_severity: Annotated[
        Optional[List["WithIssueSeverityEnum"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("withIssueSeverity", "with_issue_severity"),
            serialization_alias="withIssueSeverity",
            description="[QUERY] Filter results to include only listing items that have issues that match one or more of the specified severity levels.",
        ),
    ]

    with_status: Annotated[
        Optional[List["WithStatusEnum"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("withStatus", "with_status"),
            serialization_alias="withStatus",
            description="[QUERY] Filter results to include only listing items that have the specified status.",
        ),
    ]

    without_status: Annotated[
        Optional[List["WithoutStatusEnum"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("withoutStatus", "without_status"),
            serialization_alias="withoutStatus",
            description="[QUERY] Filter results to include only listing items that don't contain the specified statuses.",
        ),
    ]

    sort_by: Annotated[
        Optional[SortByEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("sortBy", "sort_by"),
            serialization_alias="sortBy",
            description="[QUERY] An attribute by which to sort the returned listing items.",
        ),
    ]

    sort_order: Annotated[
        Optional[SortOrderEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("sortOrder", "sort_order"),
            serialization_alias="sortOrder",
            description="[QUERY] The order in which to sort the result items.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] The number of results that you want to include on each page.",
        ),
    ]

    page_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageToken", "page_token"),
            serialization_alias="pageToken",
            description="[QUERY] A token that you can use to fetch a specific page when there are multiple pages of results.",
        ),
    ]


# Rebuild models to resolve forward references
Error.model_rebuild()
ErrorList.model_rebuild()
ItemSearchResults.model_rebuild()
Item.model_rebuild()
ItemSummaryByMarketplace.model_rebuild()
ItemImage.model_rebuild()
ItemAttributes.model_rebuild()
Issue.model_rebuild()
IssueEnforcements.model_rebuild()
IssueEnforcementAction.model_rebuild()
IssueExemption.model_rebuild()
ItemOfferByMarketplace.model_rebuild()
ItemProcurement.model_rebuild()
ItemRelationshipsByMarketplace.model_rebuild()
ItemRelationship.model_rebuild()
ItemVariationTheme.model_rebuild()
ItemProductTypeByMarketplace.model_rebuild()
FulfillmentAvailability.model_rebuild()
Money.model_rebuild()
Points.model_rebuild()
Audience.model_rebuild()
PatchOperation.model_rebuild()
ListingsItemPatchRequestBody.model_rebuild()
ListingsItemPutRequestBody.model_rebuild()
ListingsItemSubmissionResponse.model_rebuild()
ItemIdentifiersByMarketplace.model_rebuild()
Pagination.model_rebuild()
DeleteListingsItemRequest.model_rebuild()
GetListingsItemRequest.model_rebuild()
PatchListingsItemRequest.model_rebuild()
PutListingsItemRequest.model_rebuild()
SearchListingsItemsRequest.model_rebuild()
