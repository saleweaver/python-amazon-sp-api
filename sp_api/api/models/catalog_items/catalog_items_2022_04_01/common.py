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
BrandRefinement

A brand that you can use to refine your search.
"""


class BrandRefinement(SpApiBaseModel):
    """A brand that you can use to refine your search."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    number_of_results: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("numberOfResults", "number_of_results"),
            serialization_alias="numberOfResults",
            description="The estimated number of results that would be returned if you refine your search by the specified `brandName`.",
        ),
    ]

    brand_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("brandName", "brand_name"),
            serialization_alias="brandName",
            description="The brand name that you can use to refine your search.",
        ),
    ]


"""
ClassificationRefinement

A classification that you can use to refine your search.
"""


class ClassificationRefinement(SpApiBaseModel):
    """A classification that you can use to refine your search."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    number_of_results: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("numberOfResults", "number_of_results"),
            serialization_alias="numberOfResults",
            description="The estimated number of results that would be returned if you refine your search by the specified `classificationId`.",
        ),
    ]

    display_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("displayName", "display_name"),
            serialization_alias="displayName",
            description="Display name for the classification.",
        ),
    ]

    classification_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("classificationId", "classification_id"),
            serialization_alias="classificationId",
            description="The identifier of the classification that you can use to refine your search.",
        ),
    ]


"""
Dimension

The value of an individual dimension for an Amazon catalog item or item package.
"""


class Dimension(SpApiBaseModel):
    """The value of an individual dimension for an Amazon catalog item or item package."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    unit: Annotated[
        Optional[str],
        Field(None, description="Unit of measurement for the dimension value."),
    ]

    value: Annotated[
        Optional[float], Field(None, description="Numeric value of the dimension.")
    ]


"""
Dimensions

Dimensions of an Amazon catalog item or item in its packaging.
"""


class Dimensions(SpApiBaseModel):
    """Dimensions of an Amazon catalog item or item in its packaging."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    height: Annotated[
        Optional["Dimension"],
        Field(None, description="Height of an item or item package."),
    ]

    length: Annotated[
        Optional["Dimension"],
        Field(None, description="Length of an item or item package."),
    ]

    weight: Annotated[
        Optional["Dimension"],
        Field(None, description="Weight of an item or item package."),
    ]

    width: Annotated[
        Optional["Dimension"],
        Field(None, description="Width of an item or item package."),
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


# Enum definitions
class GetCatalogItemRequestIncludedDataEnum(str, Enum):
    """Enum for includedData"""

    ATTRIBUTES = "attributes"  # A JSON object containing structured item attribute data that is keyed by attribute name. Catalog item attributes conform to the related Amazon product type definitions that you can get from the [Product Type Definitions API](https://developer-docs.amazon.com/sp-api/docs/product-type-definitions-api-v2020-09-01-reference).
    CLASSIFICATIONS = "classifications"  # Classifications (browse nodes) for an item in the Amazon catalog.
    DIMENSIONS = "dimensions"  # Dimensions of an item in the Amazon catalog.
    IDENTIFIERS = "identifiers"  # Identifiers that are associated with the item in the Amazon catalog, such as UPC and EA.
    IMAGES = "images"  # Images for an item in the Amazon catalog.
    PRODUCT_TYPES = (
        "productTypes"  # Product types associated with the Amazon catalog item.
    )
    RELATIONSHIPS = "relationships"  # Relationship details of an Amazon catalog item (for example, variations).
    SALES_RANKS = "salesRanks"  # Sales ranks of an Amazon catalog item.
    SUMMARIES = "summaries"  # Summary of an Amazon catalog item. For more information, refer to the `attributes` of an Amazon catalog item.
    VENDOR_DETAILS = "vendorDetails"  # Vendor details associated with an Amazon catalog item. Vendor details are only available to vendors.


"""
GetCatalogItemRequest

Request parameters for getCatalogItem
"""


class GetCatalogItemRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getCatalogItem
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    asin: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            description="[PATH] The Amazon Standard Identification Number (ASIN) of the item.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A comma-delimited list of Amazon marketplace identifiers. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    included_data: Annotated[
        Optional[List["GetCatalogItemRequestIncludedDataEnum"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("includedData", "included_data"),
            serialization_alias="includedData",
            description="[QUERY] A comma-delimited list of datasets to include in the response.",
        ),
    ]

    locale: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            description="[QUERY] The locale for which you want to retrieve localized summaries. Defaults to the primary locale of the marketplace.",
        ),
    ]


ItemAsin = str
"""The unique identifier of an item in the Amazon catalog."""


"""
ItemAttributes

A JSON object containing structured item attribute data that is keyed by attribute name. Catalog item attributes conform to the related Amazon product type definitions that you can get from the [Product Type Definitions API](https://developer-docs.amazon.com/sp-api/docs/product-type-definitions-api-v2020-09-01-reference).
"""


class ItemAttributes(SpApiBaseModel):
    """A JSON object containing structured item attribute data that is keyed by attribute name. Catalog item attributes conform to the related Amazon product type definitions that you can get from the [Product Type Definitions API](https://developer-docs.amazon.com/sp-api/docs/product-type-definitions-api-v2020-09-01-reference)."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


ItemBrowseClassifications = List["ItemBrowseClassificationsByMarketplace"]
"""An array of classifications (browse nodes) that is associated with the item in the Amazon catalog, grouped by `marketplaceId`."""


ItemDimensions = List["ItemDimensionsByMarketplace"]
"""An array of dimensions that are associated with the item in the Amazon catalog, grouped by `marketplaceId`."""


ItemIdentifiers = List["ItemIdentifiersByMarketplace"]
"""Identifiers associated with the item in the Amazon catalog, such as UPC and EAN identifiers."""


ItemImages = List["ItemImagesByMarketplace"]
"""The images for an item in the Amazon catalog."""


ItemProductTypes = List["ItemProductTypeByMarketplace"]
"""Product types that are associated with the Amazon catalog item."""


ItemRelationships = List["ItemRelationshipsByMarketplace"]
"""Relationships grouped by `marketplaceId` for an Amazon catalog item (for example, variations)."""


ItemSalesRanks = List["ItemSalesRanksByMarketplace"]
"""Sales ranks of an Amazon catalog item."""


ItemSummaries = List["ItemSummaryByMarketplace"]
"""Summaries of Amazon catalog items."""


ItemVendorDetails = List["ItemVendorDetailsByMarketplace"]
"""The vendor details that are associated with an Amazon catalog item. Vendor details are only available to vendors."""


"""
Item

An item in the Amazon catalog.
"""


class Item(SpApiBaseModel):
    """An item in the Amazon catalog."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    asin: Annotated[
        "ItemAsin",
        Field(
            ...,
        ),
    ]

    attributes: Annotated[
        Optional["ItemAttributes"],
        Field(
            None,
        ),
    ]

    classifications: Annotated[
        Optional["ItemBrowseClassifications"],
        Field(
            None,
        ),
    ]

    dimensions: Annotated[
        Optional["ItemDimensions"],
        Field(
            None,
        ),
    ]

    identifiers: Annotated[
        Optional["ItemIdentifiers"],
        Field(
            None,
        ),
    ]

    images: Annotated[
        Optional["ItemImages"],
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

    relationships: Annotated[
        Optional["ItemRelationships"],
        Field(
            None,
        ),
    ]

    sales_ranks: Annotated[
        Optional["ItemSalesRanks"],
        Field(
            None,
            validation_alias=AliasChoices("salesRanks", "sales_ranks"),
            serialization_alias="salesRanks",
        ),
    ]

    summaries: Annotated[
        Optional["ItemSummaries"],
        Field(
            None,
        ),
    ]

    vendor_details: Annotated[
        Optional["ItemVendorDetails"],
        Field(
            None,
            validation_alias=AliasChoices("vendorDetails", "vendor_details"),
            serialization_alias="vendorDetails",
        ),
    ]


"""
ItemBrowseClassification

Classification (browse node) for an Amazon catalog item.
"""


class ItemBrowseClassification(SpApiBaseModel):
    """Classification (browse node) for an Amazon catalog item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    display_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("displayName", "display_name"),
            serialization_alias="displayName",
            description="Display name for the classification.",
        ),
    ]

    classification_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("classificationId", "classification_id"),
            serialization_alias="classificationId",
            description="Identifier of the classification.",
        ),
    ]

    parent: Annotated[
        Optional["ItemBrowseClassification"],
        Field(None, description="Parent classification of the current classification."),
    ]


"""
ItemBrowseClassificationsByMarketplace

Classifications (browse nodes) that are associated with the item in the Amazon catalog for the indicated `marketplaceId`.
"""


class ItemBrowseClassificationsByMarketplace(SpApiBaseModel):
    """Classifications (browse nodes) that are associated with the item in the Amazon catalog for the indicated `marketplaceId`."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="Amazon marketplace identifier. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    classifications: Annotated[
        Optional[List["ItemBrowseClassification"]],
        Field(
            None,
            description="Classifications (browse nodes) that are associated with the item in the Amazon catalog.",
        ),
    ]


"""
ItemClassificationSalesRank

Sales rank of an Amazon catalog item.
"""


class ItemClassificationSalesRank(SpApiBaseModel):
    """Sales rank of an Amazon catalog item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    classification_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("classificationId", "classification_id"),
            serialization_alias="classificationId",
            description="Identifier of the classification that is associated with the sales rank.",
        ),
    ]

    title: Annotated[str, Field(..., description="Name of the sales rank.")]

    link: Annotated[
        Optional[str],
        Field(
            None,
            description="Corresponding Amazon retail website URL for the sales category.",
        ),
    ]

    rank: Annotated[int, Field(..., description="Sales rank.")]


"""
ItemContributorRole

Role of an individual contributor in the creation of an item, such as author or actor.
"""


class ItemContributorRole(SpApiBaseModel):
    """Role of an individual contributor in the creation of an item, such as author or actor."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    display_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("displayName", "display_name"),
            serialization_alias="displayName",
            description="Display name of the role in the requested locale, such as `Author` or `Actor`.",
        ),
    ]

    value: Annotated[
        str,
        Field(
            ...,
            description="Role value for the Amazon catalog item, such as `author` or `actor`.",
        ),
    ]


"""
ItemContributor

Individual contributor to the creation of an item, such as an author or actor.
"""


class ItemContributor(SpApiBaseModel):
    """Individual contributor to the creation of an item, such as an author or actor."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    role: Annotated[
        "ItemContributorRole",
        Field(
            ...,
        ),
    ]

    value: Annotated[
        str, Field(..., description="Name of the contributor, such as `Jane Austen`.")
    ]


"""
ItemDimensionsByMarketplace

Dimensions that are associated with the item in the Amazon catalog for the indicated `marketplaceId`.
"""


class ItemDimensionsByMarketplace(SpApiBaseModel):
    """Dimensions that are associated with the item in the Amazon catalog for the indicated `marketplaceId`."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="Amazon marketplace identifier. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    item: Annotated[
        Optional["Dimensions"],
        Field(None, description="Dimensions of an Amazon catalog item."),
    ]

    package: Annotated[
        Optional["Dimensions"],
        Field(
            None,
            description="Dimensions of a package that contains an Amazon catalog item.",
        ),
    ]


"""
ItemDisplayGroupSalesRank

Sales rank of an Amazon catalog item, grouped by website display group.
"""


class ItemDisplayGroupSalesRank(SpApiBaseModel):
    """Sales rank of an Amazon catalog item, grouped by website display group."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    website_display_group: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "websiteDisplayGroup", "website_display_group"
            ),
            serialization_alias="websiteDisplayGroup",
            description="Name of the website display group that is associated with the sales rank",
        ),
    ]

    title: Annotated[str, Field(..., description="Name of the sales rank.")]

    link: Annotated[
        Optional[str],
        Field(
            None,
            description="Corresponding Amazon retail website URL for the sales rank.",
        ),
    ]

    rank: Annotated[int, Field(..., description="Sales rank.")]


"""
ItemIdentifier

The identifier that is associated with the item in the Amazon catalog, such as a UPC or EAN identifier.
"""


class ItemIdentifier(SpApiBaseModel):
    """The identifier that is associated with the item in the Amazon catalog, such as a UPC or EAN identifier."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    identifier_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("identifierType", "identifier_type"),
            serialization_alias="identifierType",
            description="Type of identifier, such as UPC, EAN, or ISBN.",
        ),
    ]

    identifier: Annotated[str, Field(..., description="Identifier of the item.")]


"""
ItemIdentifiersByMarketplace

Identifiers that are associated with the item in the Amazon catalog, grouped by `marketplaceId`.
"""


class ItemIdentifiersByMarketplace(SpApiBaseModel):
    """Identifiers that are associated with the item in the Amazon catalog, grouped by `marketplaceId`."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="Amazon marketplace identifier. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).identifier.",
        ),
    ]

    identifiers: Annotated[
        List["ItemIdentifier"],
        Field(
            ...,
            description="Identifiers associated with the item in the Amazon catalog for the indicated `marketplaceId`.",
        ),
    ]


# Enum definitions
class ItemImageVariantEnum(str, Enum):
    """Enum for variant"""

    MAIN = "MAIN"  # Main image for the item
    PT01 = "PT01"  # Other image #1 for the item
    PT02 = "PT02"  # Other image #2 for the item
    PT03 = "PT03"  # Other image #3 for the item
    PT04 = "PT04"  # Other image #4 for the item
    PT05 = "PT05"  # Other image #5 for the item
    PT06 = "PT06"  # Other image #6 for the item
    PT07 = "PT07"  # Other image #7 for the item
    PT08 = "PT08"  # Other image #8 for the item
    SWCH = "SWCH"  # Swatch image for the item


"""
ItemImage

Image for an item in the Amazon catalog.
"""


class ItemImage(SpApiBaseModel):
    """Image for an item in the Amazon catalog."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    variant: Annotated[
        ItemImageVariantEnum,
        Field(..., description="Variant of the image, such as `MAIN` or `PT01`."),
    ]

    link: Annotated[str, Field(..., description="URL for the image.")]

    height: Annotated[int, Field(..., description="Height of the image in pixels.")]

    width: Annotated[int, Field(..., description="Width of the image in pixels.")]


"""
ItemImagesByMarketplace

Images for an item in the Amazon catalog, grouped by `marketplaceId`.
"""


class ItemImagesByMarketplace(SpApiBaseModel):
    """Images for an item in the Amazon catalog, grouped by `marketplaceId`."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="Amazon marketplace identifier. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    images: Annotated[
        List["ItemImage"],
        Field(
            ...,
            description="Images for an item in the Amazon catalog, grouped by `marketplaceId`.",
        ),
    ]


"""
ItemProductTypeByMarketplace

Product type that is associated with the Amazon catalog item, grouped by `marketplaceId`.
"""


class ItemProductTypeByMarketplace(SpApiBaseModel):
    """Product type that is associated with the Amazon catalog item, grouped by `marketplaceId`."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="Amazon marketplace identifier. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    product_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("productType", "product_type"),
            serialization_alias="productType",
            description="Name of the product type that is associated with the Amazon catalog item.",
        ),
    ]


"""
ItemVariationTheme

The variation theme is a list of Amazon catalog item attributes that define the variation family.
"""


class ItemVariationTheme(SpApiBaseModel):
    """The variation theme is a list of Amazon catalog item attributes that define the variation family."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    attributes: Annotated[
        Optional[List["str"]],
        Field(
            None,
            description="Names of the Amazon catalog item attributes that are associated with the variation theme.",
        ),
    ]

    theme: Annotated[
        Optional[str],
        Field(
            None,
            description="Variation theme that indicates the combination of Amazon catalog item attributes that define the variation family.",
        ),
    ]


# Enum definitions
class ItemRelationshipTypeEnum(str, Enum):
    """Enum for type"""

    VARIATION = "VARIATION"  # The Amazon catalog item in the request is a variation parent or variation child of the related items that are identified by ASIN.
    PACKAGE_HIERARCHY = "PACKAGE_HIERARCHY"  # The Amazon catalog item in the request is a package container or is contained by the related items that are identified by ASIN.


"""
ItemRelationship

Relationship details for an Amazon catalog item.
"""


class ItemRelationship(SpApiBaseModel):
    """Relationship details for an Amazon catalog item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    child_asins: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("childAsins", "child_asins"),
            serialization_alias="childAsins",
            description="ASINs of the related items that are children of this item.",
        ),
    ]

    parent_asins: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("parentAsins", "parent_asins"),
            serialization_alias="parentAsins",
            description="ASINs of the related items that are parents of this item.",
        ),
    ]

    variation_theme: Annotated[
        Optional["ItemVariationTheme"],
        Field(
            None,
            validation_alias=AliasChoices("variationTheme", "variation_theme"),
            serialization_alias="variationTheme",
            description="For `VARIATION` relationships, the variation theme indicates the combination of Amazon catalog item attributes that define the variation family.",
        ),
    ]

    type: Annotated[
        ItemRelationshipTypeEnum, Field(..., description="Type of relationship.")
    ]


"""
ItemRelationshipsByMarketplace

Relationship details for the Amazon catalog item for the specified Amazon `marketplaceId`.
"""


class ItemRelationshipsByMarketplace(SpApiBaseModel):
    """Relationship details for the Amazon catalog item for the specified Amazon `marketplaceId`."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="Amazon marketplace identifier. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    relationships: Annotated[
        List["ItemRelationship"], Field(..., description="Relationships for the item.")
    ]


"""
ItemSalesRanksByMarketplace

Sales ranks of an Amazon catalog item, grouped by `marketplaceId`.
"""


class ItemSalesRanksByMarketplace(SpApiBaseModel):
    """Sales ranks of an Amazon catalog item, grouped by `marketplaceId`."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="Amazon marketplace identifier. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    classification_ranks: Annotated[
        Optional[List["ItemClassificationSalesRank"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "classificationRanks", "classification_ranks"
            ),
            serialization_alias="classificationRanks",
            description="Sales ranks of an Amazon catalog item for a `marketplaceId`, grouped by classification.",
        ),
    ]

    display_group_ranks: Annotated[
        Optional[List["ItemDisplayGroupSalesRank"]],
        Field(
            None,
            validation_alias=AliasChoices("displayGroupRanks", "display_group_ranks"),
            serialization_alias="displayGroupRanks",
            description="Sales ranks of an Amazon catalog item for a `marketplaceId`, grouped by website display group.",
        ),
    ]


"""
Pagination

Pagination occurs when a request produces a response that exceeds the `pageSize`. This means that the response is divided into individual pages. To retrieve the next page or the previous page of results, you must pass the `nextToken` value or the `previousToken` value as the `pageToken` parameter in the next request. There is no `nextToken` in the pagination object on the last page.
"""


class Pagination(SpApiBaseModel):
    """Pagination occurs when a request produces a response that exceeds the `pageSize`. This means that the response is divided into individual pages. To retrieve the next page or the previous page of results, you must pass the `nextToken` value or the `previousToken` value as the `pageToken` parameter in the next request. There is no `nextToken` in the pagination object on the last page."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    next_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="A token that you can use to retrieve the next page.",
        ),
    ]

    previous_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("previousToken", "previous_token"),
            serialization_alias="previousToken",
            description="A token that you can use to retrieve the previous page.",
        ),
    ]


"""
Refinements

Optional fields that you can use to refine your search results.
"""


class Refinements(SpApiBaseModel):
    """Optional fields that you can use to refine your search results."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    brands: Annotated[
        List["BrandRefinement"],
        Field(..., description="A list of brands you can use to refine your search."),
    ]

    classifications: Annotated[
        List["ClassificationRefinement"],
        Field(
            ...,
            description="A list of classifications you can use to refine your search.",
        ),
    ]


"""
ItemSearchResults

Items in the Amazon catalog and search-related metadata.
"""


class ItemSearchResults(SpApiBaseModel):
    """Items in the Amazon catalog and search-related metadata."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    number_of_results: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("numberOfResults", "number_of_results"),
            serialization_alias="numberOfResults",
            description="For searches that are based on `identifiers`, `numberOfResults` is the total number of Amazon catalog items found. For searches that are based on `keywords`, `numberOfResults` is the estimated total number of Amazon catalog items that are matched by the search query. Only results up to the page count limit are returned per request regardless of the number found. **Note:** The maximum number of items (ASINs) that can be returned and paged through is 1,000.",
        ),
    ]

    pagination: Annotated[
        "Pagination",
        Field(
            ...,
            description="The `nextToken` and `previousToken` values that are required to retrieve paginated results.",
        ),
    ]

    refinements: Annotated[
        "Refinements",
        Field(
            ...,
            description="Search refinements for searches that are based on `keywords`.",
        ),
    ]

    items: Annotated[
        List["Item"], Field(..., description="A list of items from the Amazon catalog.")
    ]


# Enum definitions
class ItemSummaryByMarketplaceItemClassificationEnum(str, Enum):
    """Enum for itemClassification"""

    BASE_PRODUCT = "BASE_PRODUCT"  # A product that can be directly purchased. Can be a standalone ASIN or a variation child item in the Amazon catalog.
    OTHER = "OTHER"  # An item in the Amazon catalog that is not `BASE_PRODUCT`, `PRODUCT_BUNDLE`, or `VARIATION_PARENT`.
    PRODUCT_BUNDLE = (
        "PRODUCT_BUNDLE"  # A parent catalog item that represents a bundle of items.
    )
    VARIATION_PARENT = "VARIATION_PARENT"  # A parent catalog item that groups child items into a variation family.


"""
ItemSummaryByMarketplace

Information about an Amazon catalog item for the indicated `marketplaceId`.
"""


class ItemSummaryByMarketplace(SpApiBaseModel):
    """Information about an Amazon catalog item for the indicated `marketplaceId`."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="Amazon marketplace identifier. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    adult_product: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("adultProduct", "adult_product"),
            serialization_alias="adultProduct",
            description="When `true`, the Amazon catalog item is intended for an adult audience or is sexual in nature.",
        ),
    ]

    autographed: Annotated[
        Optional[bool],
        Field(None, description="When `true`, the Amazon catalog item is autographed."),
    ]

    brand: Annotated[
        Optional[str],
        Field(
            None,
            description="Name of the brand that is associated with the Amazon catalog item.",
        ),
    ]

    browse_classification: Annotated[
        Optional["ItemBrowseClassification"],
        Field(
            None,
            validation_alias=AliasChoices(
                "browseClassification", "browse_classification"
            ),
            serialization_alias="browseClassification",
            description="Classification (browse node) that is associated with the Amazon catalog item.",
        ),
    ]

    color: Annotated[
        Optional[str],
        Field(
            None,
            description="The color that is associated with the Amazon catalog item.",
        ),
    ]

    contributors: Annotated[
        Optional[List["ItemContributor"]],
        Field(
            None,
            description="Individual contributors to the creation of the item, such as the authors or actors.",
        ),
    ]

    item_classification: Annotated[
        Optional[ItemSummaryByMarketplaceItemClassificationEnum],
        Field(
            None,
            validation_alias=AliasChoices("itemClassification", "item_classification"),
            serialization_alias="itemClassification",
            description="Classification type that is associated with the Amazon catalog item.",
        ),
    ]

    item_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("itemName", "item_name"),
            serialization_alias="itemName",
            description="The name that is associated with the Amazon catalog item.",
        ),
    ]

    manufacturer: Annotated[
        Optional[str],
        Field(
            None,
            description="The name of the manufacturer that is associated with the Amazon catalog item.",
        ),
    ]

    memorabilia: Annotated[
        Optional[bool],
        Field(None, description="When true, the item is classified as memorabilia."),
    ]

    model_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("modelNumber", "model_number"),
            serialization_alias="modelNumber",
            description="The model number that is associated with the Amazon catalog item.",
        ),
    ]

    package_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("packageQuantity", "package_quantity"),
            serialization_alias="packageQuantity",
            description="The quantity of the Amazon catalog item within one package.",
        ),
    ]

    part_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("partNumber", "part_number"),
            serialization_alias="partNumber",
            description="The part number that is associated with the Amazon catalog item.",
        ),
    ]

    release_date: Annotated[
        Optional[date],
        Field(
            None,
            validation_alias=AliasChoices("releaseDate", "release_date"),
            serialization_alias="releaseDate",
            description="The earliest date on which the Amazon catalog item can be shipped to customers.",
        ),
    ]

    size: Annotated[
        Optional[str],
        Field(None, description="The name of the size of the Amazon catalog item."),
    ]

    style: Annotated[
        Optional[str],
        Field(
            None,
            description="The name of the style that is associated with the Amazon catalog item.",
        ),
    ]

    trade_in_eligible: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("tradeInEligible", "trade_in_eligible"),
            serialization_alias="tradeInEligible",
            description="When true, the Amazon catalog item is eligible for trade-in.",
        ),
    ]

    website_display_group: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "websiteDisplayGroup", "website_display_group"
            ),
            serialization_alias="websiteDisplayGroup",
            description="The identifier of the website display group that is associated with the Amazon catalog item.",
        ),
    ]

    website_display_group_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "websiteDisplayGroupName", "website_display_group_name"
            ),
            serialization_alias="websiteDisplayGroupName",
            description="The display name of the website display group that is associated with the Amazon catalog item.",
        ),
    ]


"""
ItemVendorDetailsCategory

The product category or subcategory that is associated with an Amazon catalog item.
"""


class ItemVendorDetailsCategory(SpApiBaseModel):
    """The product category or subcategory that is associated with an Amazon catalog item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    display_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("displayName", "display_name"),
            serialization_alias="displayName",
            description="The display name of the product category or subcategory.",
        ),
    ]

    value: Annotated[
        Optional[str],
        Field(
            None,
            description="The code that identifies the product category or subcategory.",
        ),
    ]


# Enum definitions
class ItemVendorDetailsByMarketplaceReplenishmentCategoryEnum(str, Enum):
    """Enum for replenishmentCategory"""

    ALLOCATED = "ALLOCATED"  # The vendor allocates the inventory to Amazon and Amazon manually purchases it.
    BASIC_REPLENISHMENT = "BASIC_REPLENISHMENT"  # Inventory is manually purchased.
    IN_SEASON = "IN_SEASON"  # Seasonal item that is manually purchased.
    LIMITED_REPLENISHMENT = "LIMITED_REPLENISHMENT"  # Amazon generates orders for this item automatically based on unfilled demand.
    MANUFACTURER_OUT_OF_STOCK = "MANUFACTURER_OUT_OF_STOCK"  # The vendor is out of stock for an extended period of time and cannot backorder.
    NEW_PRODUCT = "NEW_PRODUCT"  # Amazon does not yet stock this item.
    NON_REPLENISHABLE = "NON_REPLENISHABLE"  # Indicates assortment parent used for detail page display, not actual items.
    NON_STOCKUPABLE = "NON_STOCKUPABLE"  # Drop ship inventory that Amazon does not stock in its fulfillment centers.
    OBSOLETE = "OBSOLETE"  # The item is obsolete and should not be ordered.
    PLANNED_REPLENISHMENT = (
        "PLANNED_REPLENISHMENT"  # Active items that should be automatically ordered.
    )


"""
ItemVendorDetailsByMarketplace

The vendor details that are associated with an Amazon catalog item for the specified `marketplaceId`.
"""


class ItemVendorDetailsByMarketplace(SpApiBaseModel):
    """The vendor details that are associated with an Amazon catalog item for the specified `marketplaceId`."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="Amazon marketplace identifier. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    brand_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("brandCode", "brand_code"),
            serialization_alias="brandCode",
            description="The brand code that is associated with an Amazon catalog item.",
        ),
    ]

    manufacturer_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("manufacturerCode", "manufacturer_code"),
            serialization_alias="manufacturerCode",
            description="The manufacturer code that is associated with an Amazon catalog item.",
        ),
    ]

    manufacturer_code_parent: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "manufacturerCodeParent", "manufacturer_code_parent"
            ),
            serialization_alias="manufacturerCodeParent",
            description="The parent vendor code of the manufacturer code.",
        ),
    ]

    product_category: Annotated[
        Optional["ItemVendorDetailsCategory"],
        Field(
            None,
            validation_alias=AliasChoices("productCategory", "product_category"),
            serialization_alias="productCategory",
            description="The product category that is associated with an Amazon catalog item.",
        ),
    ]

    product_group: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("productGroup", "product_group"),
            serialization_alias="productGroup",
            description="The product group that is associated with an Amazon catalog item.",
        ),
    ]

    product_subcategory: Annotated[
        Optional["ItemVendorDetailsCategory"],
        Field(
            None,
            validation_alias=AliasChoices("productSubcategory", "product_subcategory"),
            serialization_alias="productSubcategory",
            description="The product subcategory that is associated with an Amazon catalog item.",
        ),
    ]

    replenishment_category: Annotated[
        Optional[ItemVendorDetailsByMarketplaceReplenishmentCategoryEnum],
        Field(
            None,
            validation_alias=AliasChoices(
                "replenishmentCategory", "replenishment_category"
            ),
            serialization_alias="replenishmentCategory",
            description="The replenishment category that is associated with an Amazon catalog item.",
        ),
    ]


# Enum definitions
class SearchCatalogItemsRequestIdentifiersTypeEnum(str, Enum):
    """Enum for identifiersType"""

    ASIN = "ASIN"  # Amazon Standard Identification Number
    EAN = "EAN"  # European Article Number
    GTIN = "GTIN"  # Global Trade Item Number
    ISBN = "ISBN"  # International Standard Book Number
    JAN = "JAN"  # Japanese Article Number
    MINSAN = "MINSAN"  # Minsan Code
    SKU = "SKU"  # Stock Keeping Unit, a seller-specified identifier for an Amazon listing. **Note:** Must be accompanied by `sellerId`.
    UPC = "UPC"  # Universal Product Code


class SearchCatalogItemsRequestIncludedDataEnum(str, Enum):
    """Enum for includedData"""

    ATTRIBUTES = "attributes"  # A JSON object containing structured item attribute data that is keyed by attribute name. Catalog item attributes conform to the related Amazon product type definitions that you can get from the [Product Type Definitions API](https://developer-docs.amazon.com/sp-api/docs/product-type-definitions-api-v2020-09-01-reference).
    CLASSIFICATIONS = "classifications"  # Classifications (browse nodes) for an item in the Amazon catalog.
    DIMENSIONS = "dimensions"  # Dimensions of an item in the Amazon catalog.
    IDENTIFIERS = "identifiers"  # Identifiers that are associated with the item in the Amazon catalog, such as UPC and EAN.
    IMAGES = "images"  # Images for an item in the Amazon catalog.
    PRODUCT_TYPES = (
        "productTypes"  # Product types associated with the Amazon catalog item.
    )
    RELATIONSHIPS = "relationships"  # Relationship details of an Amazon catalog item (for example, variations).
    SALES_RANKS = "salesRanks"  # Sales ranks of an Amazon catalog item.
    SUMMARIES = "summaries"  # Summary of an Amazon catalog item. For more information, refer to the `attributes` of an Amazon catalog item.
    VENDOR_DETAILS = "vendorDetails"  # Vendor details associated with an Amazon catalog item. Vendor details are only available to vendors.


"""
SearchCatalogItemsRequest

Request parameters for searchCatalogItems
"""


class SearchCatalogItemsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for searchCatalogItems
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    identifiers: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            description="[QUERY] A comma-delimited list of product identifiers that you can use to search the Amazon catalog. **Note:** You cannot include `identifiers` and `keywords` in the same request.",
        ),
    ]

    identifiers_type: Annotated[
        Optional[SearchCatalogItemsRequestIdentifiersTypeEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("identifiersType", "identifiers_type"),
            serialization_alias="identifiersType",
            description="[QUERY] The type of product identifiers that you can use to search the Amazon catalog. **Note:** `identifiersType` is required when `identifiers` is in the request.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A comma-delimited list of Amazon marketplace identifiers. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    included_data: Annotated[
        Optional[List["SearchCatalogItemsRequestIncludedDataEnum"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("includedData", "included_data"),
            serialization_alias="includedData",
            description="[QUERY] A comma-delimited list of datasets to include in the response.",
        ),
    ]

    locale: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            description="[QUERY] The locale for which you want to retrieve localized summaries. Defaults to the primary locale of the marketplace.",
        ),
    ]

    seller_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("sellerId", "seller_id"),
            serialization_alias="sellerId",
            description="[QUERY] A selling partner identifier, such as a seller account or vendor code. **Note:** Required when `identifiersType` is `SKU`.",
        ),
    ]

    keywords: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            description="[QUERY] A comma-delimited list of keywords that you can use to search the Amazon catalog. **Note:** You cannot include `keywords` and `identifiers` in the same request.",
        ),
    ]

    brand_names: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("brandNames", "brand_names"),
            serialization_alias="brandNames",
            description="[QUERY] A comma-delimited list of brand names that you can use to limit the search in queries based on `keywords`. **Note:** Cannot be used with `identifiers`.",
        ),
    ]

    classification_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("classificationIds", "classification_ids"),
            serialization_alias="classificationIds",
            description="[QUERY] A comma-delimited list of classification identifiers that you can use to limit the search in queries based on `keywords`. **Note:** Cannot be used with `identifiers`.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] The number of results to include on each page.",
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

    keywords_locale: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("keywordsLocale", "keywords_locale"),
            serialization_alias="keywordsLocale",
            description="[QUERY] The language of the keywords that are included in queries based on `keywords`. Defaults to the primary locale of the marketplace. **Note:** Cannot be used with `identifiers`.",
        ),
    ]


# Rebuild models to resolve forward references
Error.model_rebuild()
ErrorList.model_rebuild()
Item.model_rebuild()
ItemAttributes.model_rebuild()
ItemBrowseClassification.model_rebuild()
ItemContributor.model_rebuild()
ItemContributorRole.model_rebuild()
ItemBrowseClassificationsByMarketplace.model_rebuild()
Dimension.model_rebuild()
Dimensions.model_rebuild()
ItemDimensionsByMarketplace.model_rebuild()
ItemIdentifiersByMarketplace.model_rebuild()
ItemIdentifier.model_rebuild()
ItemImagesByMarketplace.model_rebuild()
ItemImage.model_rebuild()
ItemProductTypeByMarketplace.model_rebuild()
ItemSalesRanksByMarketplace.model_rebuild()
ItemClassificationSalesRank.model_rebuild()
ItemDisplayGroupSalesRank.model_rebuild()
ItemSummaryByMarketplace.model_rebuild()
ItemVariationTheme.model_rebuild()
ItemRelationshipsByMarketplace.model_rebuild()
ItemRelationship.model_rebuild()
ItemVendorDetailsCategory.model_rebuild()
ItemVendorDetailsByMarketplace.model_rebuild()
ItemSearchResults.model_rebuild()
Pagination.model_rebuild()
Refinements.model_rebuild()
BrandRefinement.model_rebuild()
ClassificationRefinement.model_rebuild()
SearchCatalogItemsRequest.model_rebuild()
GetCatalogItemRequest.model_rebuild()
