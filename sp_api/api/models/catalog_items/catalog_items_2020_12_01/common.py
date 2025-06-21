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

Description of a brand that can be used to get more fine-grained search results.
"""


class BrandRefinement(SpApiBaseModel):
    """Description of a brand that can be used to get more fine-grained search results."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    number_of_results: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("numberOfResults", "number_of_results"),
            serialization_alias="numberOfResults",
            description="The estimated number of results that would still be returned if refinement key applied.",
        ),
    ]

    brand_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("brandName", "brand_name"),
            serialization_alias="brandName",
            description="Brand name. For display and can be used as a search refinement.",
        ),
    ]


"""
ClassificationRefinement

Description of a classification that can be used to get more fine-grained search results.
"""


class ClassificationRefinement(SpApiBaseModel):
    """Description of a classification that can be used to get more fine-grained search results."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    number_of_results: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("numberOfResults", "number_of_results"),
            serialization_alias="numberOfResults",
            description="The estimated number of results that would still be returned if refinement key applied.",
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
            description="Identifier for the classification that can be used for search refinement purposes.",
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


# Enum definitions
class IncludedDataEnum(str, Enum):
    """Enum for includedData"""

    ATTRIBUTES = "attributes"  # A JSON object containing structured item attribute data keyed by attribute name. Catalog item attributes are available only to brand owners and conform to the related Amazon product type definitions available in the Selling Partner API for Product Type Definitions.
    IDENTIFIERS = "identifiers"  # Identifiers associated with the item in the Amazon catalog, such as UPC and EAN identifiers.
    IMAGES = "images"  # Images for an item in the Amazon catalog. All image variants are provided to brand owners. Otherwise, a thumbnail of the "MAIN" image variant is provided.
    PRODUCT_TYPES = (
        "productTypes"  # Product types associated with the Amazon catalog item.
    )
    SALES_RANKS = "salesRanks"  # Sales ranks of an Amazon catalog item.
    SUMMARIES = "summaries"  # Summary details of an Amazon catalog item.
    VARIATIONS = "variations"  # Variation details of an Amazon catalog item (variation relationships).
    VENDOR_DETAILS = "vendorDetails"  # Vendor details associated with an Amazon catalog item. Vendor details are available to vendors only.


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
            description="[QUERY] A comma-delimited list of Amazon marketplace identifiers. Data sets in the response contain data only for the specified marketplaces.",
        ),
    ]

    included_data: Annotated[
        Optional[List["IncludedDataEnum"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("includedData", "included_data"),
            serialization_alias="includedData",
            description="[QUERY] A comma-delimited list of data sets to include in the response. Default: summaries.",
        ),
    ]

    locale: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            description="[QUERY] Locale for retrieving localized summaries. Defaults to the primary locale of the marketplace.",
        ),
    ]


ItemAsin = str
"""Amazon Standard Identification Number (ASIN) is the unique identifier for an item in the Amazon catalog."""


"""
ItemAttributes

A JSON object that contains structured item attribute data keyed by attribute name. Catalog item attributes are available only to brand owners and conform to the related product type definitions available in the Selling Partner API for Product Type Definitions.
"""


class ItemAttributes(SpApiBaseModel):
    """A JSON object that contains structured item attribute data keyed by attribute name. Catalog item attributes are available only to brand owners and conform to the related product type definitions available in the Selling Partner API for Product Type Definitions."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


ItemIdentifiers = List["ItemIdentifiersByMarketplace"]
"""Identifiers associated with the item in the Amazon catalog, such as UPC and EAN identifiers."""


ItemImages = List["ItemImagesByMarketplace"]
"""Images for an item in the Amazon catalog. All image variants are provided to brand owners. Otherwise, a thumbnail of the 'MAIN' image variant is provided."""


ItemProductTypes = List["ItemProductTypeByMarketplace"]
"""Product types associated with the Amazon catalog item."""


ItemSalesRanks = List["ItemSalesRanksByMarketplace"]
"""Sales ranks of an Amazon catalog item."""


ItemSummaries = List["ItemSummaryByMarketplace"]
"""Summary details of an Amazon catalog item."""


ItemVariations = List["ItemVariationsByMarketplace"]
"""Variation details by marketplace for an Amazon catalog item (variation relationships)."""


ItemVendorDetails = List["ItemVendorDetailsByMarketplace"]
"""Vendor details associated with an Amazon catalog item. Vendor details are available to vendors only."""


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

    variations: Annotated[
        Optional["ItemVariations"],
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
ItemIdentifier

Identifier associated with the item in the Amazon catalog, such as a UPC or EAN identifier.
"""


class ItemIdentifier(SpApiBaseModel):
    """Identifier associated with the item in the Amazon catalog, such as a UPC or EAN identifier."""

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

    identifier: Annotated[str, Field(..., description="Identifier.")]


"""
ItemIdentifiersByMarketplace

Identifiers associated with the item in the Amazon catalog for the indicated Amazon marketplace.
"""


class ItemIdentifiersByMarketplace(SpApiBaseModel):
    """Identifiers associated with the item in the Amazon catalog for the indicated Amazon marketplace."""

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

    identifiers: Annotated[
        List["ItemIdentifier"],
        Field(
            ...,
            description="Identifiers associated with the item in the Amazon catalog for the indicated Amazon marketplace.",
        ),
    ]


# Enum definitions
class VariantEnum(str, Enum):
    """Enum for variant"""

    MAIN = "MAIN"  # Main image for the item.
    PT01 = "PT01"  # Other image #1 for the item.
    PT02 = "PT02"  # Other image #2 for the item.
    PT03 = "PT03"  # Other image #3 for the item.
    PT04 = "PT04"  # Other image #4 for the item.
    PT05 = "PT05"  # Other image #5 for the item.
    PT06 = "PT06"  # Other image #6 for the item.
    PT07 = "PT07"  # Other image #7 for the item.
    PT08 = "PT08"  # Other image #8 for the item.
    SWCH = "SWCH"  # Swatch image for the item.


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
        VariantEnum,
        Field(..., description="Variant of the image, such as MAIN or PT01."),
    ]

    link: Annotated[str, Field(..., description="Link, or URL, for the image.")]

    height: Annotated[int, Field(..., description="Height of the image in pixels.")]

    width: Annotated[int, Field(..., description="Width of the image in pixels.")]


"""
ItemImagesByMarketplace

Images for an item in the Amazon catalog for the indicated Amazon marketplace.
"""


class ItemImagesByMarketplace(SpApiBaseModel):
    """Images for an item in the Amazon catalog for the indicated Amazon marketplace."""

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

    images: Annotated[
        List["ItemImage"],
        Field(
            ...,
            description="Images for an item in the Amazon catalog for the indicated Amazon marketplace.",
        ),
    ]


"""
ItemProductTypeByMarketplace

Product type associated with the Amazon catalog item for the indicated Amazon marketplace.
"""


class ItemProductTypeByMarketplace(SpApiBaseModel):
    """Product type associated with the Amazon catalog item for the indicated Amazon marketplace."""

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
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("productType", "product_type"),
            serialization_alias="productType",
            description="Name of the product type associated with the Amazon catalog item.",
        ),
    ]


"""
ItemSalesRank

Sales rank of an Amazon catalog item.
"""


class ItemSalesRank(SpApiBaseModel):
    """Sales rank of an Amazon catalog item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    title: Annotated[str, Field(..., description="Title, or name, of the sales rank.")]

    link: Annotated[
        Optional[str],
        Field(
            None,
            description="Corresponding Amazon retail website link, or URL, for the sales rank.",
        ),
    ]

    rank: Annotated[int, Field(..., description="Sales rank value.")]


"""
ItemSalesRanksByMarketplace

Sales ranks of an Amazon catalog item for the indicated Amazon marketplace.
"""


class ItemSalesRanksByMarketplace(SpApiBaseModel):
    """Sales ranks of an Amazon catalog item for the indicated Amazon marketplace."""

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

    ranks: Annotated[
        List["ItemSalesRank"],
        Field(
            ...,
            description="Sales ranks of an Amazon catalog item for an Amazon marketplace.",
        ),
    ]


"""
Pagination

When a request produces a response that exceeds the pageSize, pagination occurs. This means the response is divided into individual pages. To retrieve the next page or the previous page, you must pass the nextToken value or the previousToken value as the pageToken parameter in the next request. When you receive the last page, there will be no nextToken key in the pagination object.
"""


class Pagination(SpApiBaseModel):
    """When a request produces a response that exceeds the pageSize, pagination occurs. This means the response is divided into individual pages. To retrieve the next page or the previous page, you must pass the nextToken value or the previousToken value as the pageToken parameter in the next request. When you receive the last page, there will be no nextToken key in the pagination object."""

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
Refinements

Search refinements.
"""


class Refinements(SpApiBaseModel):
    """Search refinements."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    brands: Annotated[
        List["BrandRefinement"], Field(..., description="Brand search refinements.")
    ]

    classifications: Annotated[
        List["ClassificationRefinement"],
        Field(..., description="Classification search refinements."),
    ]


"""
ItemSearchResults

Items in the Amazon catalog and search related metadata.
"""


class ItemSearchResults(SpApiBaseModel):
    """Items in the Amazon catalog and search related metadata."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    number_of_results: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("numberOfResults", "number_of_results"),
            serialization_alias="numberOfResults",
            description="The estimated total number of products matched by the search query (only results up to the page count limit will be returned per request regardless of the number found). Note: The maximum number of items (ASINs) that can be returned and paged through is 1000.",
        ),
    ]

    pagination: Annotated[
        "Pagination",
        Field(
            ...,
            description="If available, the nextToken and/or previousToken values required to return paginated results.",
        ),
    ]

    refinements: Annotated[
        "Refinements",
        Field(
            ...,
        ),
    ]

    items: Annotated[
        List["Item"], Field(..., description="A list of items from the Amazon catalog.")
    ]


"""
ItemSummaryByMarketplace

Summary details of an Amazon catalog item for the indicated Amazon marketplace.
"""


class ItemSummaryByMarketplace(SpApiBaseModel):
    """Summary details of an Amazon catalog item for the indicated Amazon marketplace."""

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

    brand_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("brandName", "brand_name"),
            serialization_alias="brandName",
            description="Name of the brand associated with an Amazon catalog item.",
        ),
    ]

    browse_node: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("browseNode", "browse_node"),
            serialization_alias="browseNode",
            description="Identifier of the browse node associated with an Amazon catalog item.",
        ),
    ]

    color_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("colorName", "color_name"),
            serialization_alias="colorName",
            description="Name of the color associated with an Amazon catalog item.",
        ),
    ]

    item_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("itemName", "item_name"),
            serialization_alias="itemName",
            description="Name, or title, associated with an Amazon catalog item.",
        ),
    ]

    manufacturer: Annotated[
        Optional[str],
        Field(
            None,
            description="Name of the manufacturer associated with an Amazon catalog item.",
        ),
    ]

    model_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("modelNumber", "model_number"),
            serialization_alias="modelNumber",
            description="Model number associated with an Amazon catalog item.",
        ),
    ]

    size_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("sizeName", "size_name"),
            serialization_alias="sizeName",
            description="Name of the size associated with an Amazon catalog item.",
        ),
    ]

    style_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("styleName", "style_name"),
            serialization_alias="styleName",
            description="Name of the style associated with an Amazon catalog item.",
        ),
    ]


# Enum definitions
class VariationTypeEnum(str, Enum):
    """Enum for variationType"""

    PARENT = "PARENT"  # The Amazon catalog item in the request is a variation parent of the related item(s) indicated by ASIN.
    CHILD = "CHILD"  # The Amazon catalog item in the request is a variation child of the related item identified by ASIN.


"""
ItemVariationsByMarketplace

Variation details for the Amazon catalog item for the indicated Amazon marketplace.
"""


class ItemVariationsByMarketplace(SpApiBaseModel):
    """Variation details for the Amazon catalog item for the indicated Amazon marketplace."""

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

    asins: Annotated[
        List["str"], Field(..., description="Identifiers (ASINs) of the related items.")
    ]

    variation_type: Annotated[
        VariationTypeEnum,
        Field(
            ...,
            validation_alias=AliasChoices("variationType", "variation_type"),
            serialization_alias="variationType",
            description="Type of variation relationship of the Amazon catalog item in the request to the related item(s): 'PARENT' or 'CHILD'.",
        ),
    ]


# Enum definitions
class ReplenishmentCategoryEnum(str, Enum):
    """Enum for replenishmentCategory"""

    ALLOCATED = "ALLOCATED"  # Indicates non-automated purchasing of inventory that has been allocated to Amazon by the vendor.
    BASIC_REPLENISHMENT = (
        "BASIC_REPLENISHMENT"  # Indicates non-automated purchasing of inventory.
    )
    IN_SEASON = "IN_SEASON"  # Indicates non-automated purchasing of inventory for seasonal items.
    LIMITED_REPLENISHMENT = "LIMITED_REPLENISHMENT"  # Holding queue replenishment status before an item is NEW_PRODUCT.
    MANUFACTURER_OUT_OF_STOCK = "MANUFACTURER_OUT_OF_STOCK"  # Indicates vendor is out of stock for a longer period of time and cannot backorder.
    NEW_PRODUCT = "NEW_PRODUCT"  # Indicates a new item that Amazon does not yet stock in inventory.
    NON_REPLENISHABLE = "NON_REPLENISHABLE"  # Indicates assortment parent used for detail page display, not actual items.
    NON_STOCKUPABLE = "NON_STOCKUPABLE"  # Indicates drop ship inventory that Amazon does not stock in its fulfillment centers.
    OBSOLETE = "OBSOLETE"  # Indicates item is obsolete and should not be ordered.
    PLANNED_REPLENISHMENT = "PLANNED_REPLENISHMENT"  # Indicates active items that should be automatically ordered.


"""
ItemVendorDetailsByMarketplace

Vendor details associated with an Amazon catalog item for the indicated Amazon marketplace.
"""


class ItemVendorDetailsByMarketplace(SpApiBaseModel):
    """Vendor details associated with an Amazon catalog item for the indicated Amazon marketplace."""

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

    brand_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("brandCode", "brand_code"),
            serialization_alias="brandCode",
            description="Brand code associated with an Amazon catalog item.",
        ),
    ]

    category_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("categoryCode", "category_code"),
            serialization_alias="categoryCode",
            description="Product category associated with an Amazon catalog item.",
        ),
    ]

    manufacturer_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("manufacturerCode", "manufacturer_code"),
            serialization_alias="manufacturerCode",
            description="Manufacturer code associated with an Amazon catalog item.",
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
            description="Parent vendor code of the manufacturer code.",
        ),
    ]

    product_group: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("productGroup", "product_group"),
            serialization_alias="productGroup",
            description="Product group associated with an Amazon catalog item.",
        ),
    ]

    replenishment_category: Annotated[
        Optional[ReplenishmentCategoryEnum],
        Field(
            None,
            validation_alias=AliasChoices(
                "replenishmentCategory", "replenishment_category"
            ),
            serialization_alias="replenishmentCategory",
            description="Replenishment category associated with an Amazon catalog item.",
        ),
    ]

    subcategory_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("subcategoryCode", "subcategory_code"),
            serialization_alias="subcategoryCode",
            description="Product subcategory associated with an Amazon catalog item.",
        ),
    ]


# Enum definitions
class IncludedDataEnum(str, Enum):
    """Enum for includedData"""

    ATTRIBUTES = "attributes"  # A JSON object containing structured item attribute data keyed by attribute name. Catalog item attributes are available only to brand owners and conform to the related Amazon product type definitions available in the Selling Partner API for Product Type Definitions.
    IDENTIFIERS = "identifiers"  # Identifiers associated with the item in the Amazon catalog, such as UPC and EAN identifiers.
    IMAGES = "images"  # Images for an item in the Amazon catalog. All image variants are provided to brand owners. Otherwise, a thumbnail of the "MAIN" image variant is provided.
    PRODUCT_TYPES = (
        "productTypes"  # Product types associated with the Amazon catalog item.
    )
    SALES_RANKS = "salesRanks"  # Sales ranks of an Amazon catalog item.
    SUMMARIES = "summaries"  # Summary details of an Amazon catalog item.
    VARIATIONS = "variations"  # Variation details of an Amazon catalog item (variation relationships).
    VENDOR_DETAILS = "vendorDetails"  # Vendor details associated with an Amazon catalog item. Vendor details are available to vendors only.


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

    keywords: Annotated[
        List["str"],
        QueryParam(),
        Field(
            ...,
            description="[QUERY] A comma-delimited list of words or item identifiers to search the Amazon catalog for.",
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
            description="[QUERY] A comma-delimited list of data sets to include in the response. Default: summaries.",
        ),
    ]

    brand_names: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("brandNames", "brand_names"),
            serialization_alias="brandNames",
            description="[QUERY] A comma-delimited list of brand names to limit the search to.",
        ),
    ]

    classification_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("classificationIds", "classification_ids"),
            serialization_alias="classificationIds",
            description="[QUERY] A comma-delimited list of classification identifiers to limit the search to.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] Number of results to be returned per page.",
        ),
    ]

    page_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageToken", "page_token"),
            serialization_alias="pageToken",
            description="[QUERY] A token to fetch a certain page when there are multiple pages worth of results.",
        ),
    ]

    keywords_locale: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("keywordsLocale", "keywords_locale"),
            serialization_alias="keywordsLocale",
            description="[QUERY] The language the keywords are provided in. Defaults to the primary locale of the marketplace.",
        ),
    ]

    locale: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            description="[QUERY] Locale for retrieving localized summaries. Defaults to the primary locale of the marketplace.",
        ),
    ]


# Rebuild models to resolve forward references
Error.model_rebuild()
ErrorList.model_rebuild()
Item.model_rebuild()
ItemAttributes.model_rebuild()
ItemIdentifiersByMarketplace.model_rebuild()
ItemIdentifier.model_rebuild()
ItemImagesByMarketplace.model_rebuild()
ItemImage.model_rebuild()
ItemProductTypeByMarketplace.model_rebuild()
ItemSalesRanksByMarketplace.model_rebuild()
ItemSalesRank.model_rebuild()
ItemSummaryByMarketplace.model_rebuild()
ItemVariationsByMarketplace.model_rebuild()
ItemVendorDetailsByMarketplace.model_rebuild()
ItemSearchResults.model_rebuild()
Pagination.model_rebuild()
Refinements.model_rebuild()
BrandRefinement.model_rebuild()
ClassificationRefinement.model_rebuild()
SearchCatalogItemsRequest.model_rebuild()
GetCatalogItemRequest.model_rebuild()
