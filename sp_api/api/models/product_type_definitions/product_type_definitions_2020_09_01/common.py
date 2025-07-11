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
class GetDefinitionsProductTypeRequestRequirementsEnum(str, Enum):
    """Enum for requirements"""

    LISTING = "LISTING"  # RequestBody schema containing product facts and sales terms.
    LISTING_PRODUCT_ONLY = (
        "LISTING_PRODUCT_ONLY"  # RequestBody schema containing product facts only.
    )
    LISTING_OFFER_ONLY = (
        "LISTING_OFFER_ONLY"  # RequestBody schema containing sales terms only.
    )


class GetDefinitionsProductTypeRequestRequirementsEnforcedEnum(str, Enum):
    """Enum for requirementsEnforced"""

    ENFORCED = "ENFORCED"  # RequestBody schema with required and conditionally required attributes enforced (used for full payload validation).
    NOT_ENFORCED = "NOT_ENFORCED"  # RequestBody schema with required and conditionally required attributes not enforced (used for partial payload validation, such as for single attributes).


class GetDefinitionsProductTypeRequestLocaleEnum(str, Enum):
    """Enum for locale"""

    DEFAULT = "DEFAULT"  # Default locale of the requested Amazon marketplace.
    AR = "ar"  # Arabic
    AR_AE = "ar_AE"  # Arabic (U.A.E.)
    DE = "de"  # German
    DE_DE = "de_DE"  # German (Germany)
    EN = "en"  # English
    EN_AE = "en_AE"  # English (U.A.E.)
    EN_AU = "en_AU"  # English (Australia)
    EN_CA = "en_CA"  # English (Canada)
    EN_GB = "en_GB"  # English (United Kingdom)
    EN_IN = "en_IN"  # English (India)
    EN_SG = "en_SG"  # English (Singapore)
    EN_US = "en_US"  # English (United States)
    ES = "es"  # Spanish
    ES_ES = "es_ES"  # Spanish (Spain)
    ES_MX = "es_MX"  # Spanish (Mexico)
    ES_US = "es_US"  # Spanish (United States)
    FR = "fr"  # French
    FR_CA = "fr_CA"  # French (Canada)
    FR_FR = "fr_FR"  # French (France)
    IT = "it"  # Italian
    IT_IT = "it_IT"  # Italian (Italy)
    JA = "ja"  # Japanese
    JA_JP = "ja_JP"  # Japanese (Japan)
    NL = "nl"  # Dutch
    NL_NL = "nl_NL"  # Dutch (Netherlands)
    PL = "pl"  # Polish
    PL_PL = "pl_PL"  # Polish (Poland)
    PT = "pt"  # Portuguese
    PT_BR = "pt_BR"  # Portuguese (Brazil)
    PT_PT = "pt_PT"  # Portuguese (Portugal)
    SV = "sv"  # Swedish
    SV_SE = "sv_SE"  # Swedish (Sweden)
    TR = "tr"  # Turkish
    TR_TR = "tr_TR"  # Turkish (Turkey)
    ZH = "zh"  # Chinese
    ZH_CN = "zh_CN"  # Chinese (Simplified)
    ZH_TW = "zh_TW"  # Chinese (Traditional)


"""
GetDefinitionsProductTypeRequest

Request parameters for getDefinitionsProductType
"""


class GetDefinitionsProductTypeRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getDefinitionsProductType
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    product_type: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("productType", "product_type"),
            serialization_alias="productType",
            description="[PATH] The Amazon product type name.",
        ),
    ]

    seller_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("sellerId", "seller_id"),
            serialization_alias="sellerId",
            description="[QUERY] A selling partner identifier. When provided, seller-specific requirements and values are populated within the product type definition schema, such as brand names associated with the selling partner.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A comma-delimited list of Amazon marketplace identifiers for the request. Note: This parameter is limited to one marketplaceId at this time.",
        ),
    ]

    product_type_version: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("productTypeVersion", "product_type_version"),
            serialization_alias="productTypeVersion",
            description="[QUERY] The version of the Amazon product type to retrieve. Defaults to 'LATEST',. Prerelease versions of product type definitions may be retrieved with 'RELEASE_CANDIDATE'. If no prerelease version is currently available, the 'LATEST' live version will be provided.",
        ),
    ]

    requirements: Annotated[
        Optional[GetDefinitionsProductTypeRequestRequirementsEnum],
        QueryParam(),
        Field(
            None,
            description="[QUERY] The name of the requirements set to retrieve requirements for.",
        ),
    ]

    requirements_enforced: Annotated[
        Optional[GetDefinitionsProductTypeRequestRequirementsEnforcedEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "requirementsEnforced", "requirements_enforced"
            ),
            serialization_alias="requirementsEnforced",
            description="[QUERY] Identifies if the required attributes for a requirements set are enforced by the product type definition schema. Non-enforced requirements enable structural validation of individual attributes without all the required attributes being present (such as for partial updates).",
        ),
    ]

    locale: Annotated[
        Optional[GetDefinitionsProductTypeRequestLocaleEnum],
        QueryParam(),
        Field(
            None,
            description="[QUERY] Locale for retrieving display labels and other presentation details. Defaults to the default language of the first marketplace in the request.",
        ),
    ]


"""
ProductType

An Amazon product type with a definition available.
"""


class ProductType(SpApiBaseModel):
    """An Amazon product type with a definition available."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[str, Field(..., description="The name of the Amazon product type.")]

    display_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("displayName", "display_name"),
            serialization_alias="displayName",
            description="The human-readable and localized description of the Amazon product type.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="The Amazon marketplace identifiers for which the product type definition is available.",
        ),
    ]


"""
ProductTypeVersion

The version details for an Amazon product type.
"""


class ProductTypeVersion(SpApiBaseModel):
    """The version details for an Amazon product type."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    version: Annotated[str, Field(..., description="Version identifier.")]

    latest: Annotated[
        bool,
        Field(
            ...,
            description="When true, the version indicated by the version identifier is the latest available for the Amazon product type.",
        ),
    ]

    release_candidate: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("releaseCandidate", "release_candidate"),
            serialization_alias="releaseCandidate",
            description="When true, the version indicated by the version identifier is the prerelease (release candidate) for the Amazon product type.",
        ),
    ]


"""
SchemaLink


"""


class SchemaLink(SpApiBaseModel):
    """"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    link: Annotated[
        Dict[str, Any], Field(..., description="Link to retrieve the schema.")
    ]

    checksum: Annotated[
        str,
        Field(
            ...,
            description="Checksum hash of the schema (Base64 MD5). Can be used to verify schema contents, identify changes between schema versions, and for caching.",
        ),
    ]


# Enum definitions
class ProductTypeDefinitionRequirementsEnum(str, Enum):
    """Enum for requirements"""

    LISTING = "LISTING"  # Indicates the schema contains product facts and sales terms.
    LISTING_PRODUCT_ONLY = (
        "LISTING_PRODUCT_ONLY"  # Indicates the schema data contains product facts only.
    )
    LISTING_OFFER_ONLY = (
        "LISTING_OFFER_ONLY"  # Indicates the schema data contains sales terms only.
    )


class ProductTypeDefinitionRequirementsEnforcedEnum(str, Enum):
    """Enum for requirementsEnforced"""

    ENFORCED = "ENFORCED"  # Schema enforces required and conditionally required attributes (used for full payload validation).
    NOT_ENFORCED = "NOT_ENFORCED"  # Schema does not enforce required and conditionally required attributes (used for partial payload validation, such as for single attributes).


"""
ProductTypeDefinition

A product type definition represents the attributes and data requirements for a product type in the Amazon catalog. Product type definitions are used interchangeably between the Selling Partner API for Listings Items, Selling Partner API for Catalog Items, and JSON-based listings feeds in the Selling Partner API for Feeds.
"""


class ProductTypeDefinition(SpApiBaseModel):
    """A product type definition represents the attributes and data requirements for a product type in the Amazon catalog. Product type definitions are used interchangeably between the Selling Partner API for Listings Items, Selling Partner API for Catalog Items, and JSON-based listings feeds in the Selling Partner API for Feeds."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    meta_schema: Annotated[
        Optional["SchemaLink"],
        Field(
            None,
            validation_alias=AliasChoices("metaSchema", "meta_schema"),
            serialization_alias="metaSchema",
            description="Link to meta-schema describing the vocabulary used by the product type schema.",
        ),
    ]

    schema: Annotated[
        "SchemaLink",
        Field(
            ...,
            description="Link to schema describing the attributes and requirements for the product type.",
        ),
    ]

    requirements: Annotated[
        ProductTypeDefinitionRequirementsEnum,
        Field(
            ...,
            description="Name of the requirements set represented in this product type definition.",
        ),
    ]

    requirements_enforced: Annotated[
        ProductTypeDefinitionRequirementsEnforcedEnum,
        Field(
            ...,
            validation_alias=AliasChoices(
                "requirementsEnforced", "requirements_enforced"
            ),
            serialization_alias="requirementsEnforced",
            description="Identifies if the required attributes for a requirements set are enforced by the product type definition schema. Non-enforced requirements enable structural validation of individual attributes without all of the required attributes being present (such as for partial updates).",
        ),
    ]

    property_groups: Annotated[
        Dict[str, Any],
        Field(
            ...,
            validation_alias=AliasChoices("propertyGroups", "property_groups"),
            serialization_alias="propertyGroups",
            description="Mapping of property group names to property groups. Property groups represent logical groupings of schema properties that can be used for display or informational purposes.",
        ),
    ]

    locale: Annotated[
        str,
        Field(
            ...,
            description="Locale of the display elements contained in the product type definition.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="Amazon marketplace identifiers for which the product type definition is applicable.",
        ),
    ]

    product_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("productType", "product_type"),
            serialization_alias="productType",
            description="The name of the Amazon product type that this product type definition applies to.",
        ),
    ]

    display_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("displayName", "display_name"),
            serialization_alias="displayName",
            description="Human-readable and localized description of the Amazon product type.",
        ),
    ]

    product_type_version: Annotated[
        "ProductTypeVersion",
        Field(
            ...,
            validation_alias=AliasChoices("productTypeVersion", "product_type_version"),
            serialization_alias="productTypeVersion",
            description="The version details for the Amazon product type.",
        ),
    ]


"""
ProductTypeList

A list of Amazon product types with definitions available.
"""


class ProductTypeList(SpApiBaseModel):
    """A list of Amazon product types with definitions available."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    product_types: Annotated[
        List["ProductType"],
        Field(
            ...,
            validation_alias=AliasChoices("productTypes", "product_types"),
            serialization_alias="productTypes",
        ),
    ]

    product_type_version: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("productTypeVersion", "product_type_version"),
            serialization_alias="productTypeVersion",
            description="Amazon product type version identifier.",
        ),
    ]


"""
PropertyGroup

A property group represents a logical grouping of schema properties that can be used for display or informational purposes.
"""


class PropertyGroup(SpApiBaseModel):
    """A property group represents a logical grouping of schema properties that can be used for display or informational purposes."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    title: Annotated[
        Optional[str],
        Field(None, description="The display label of the property group."),
    ]

    description: Annotated[
        Optional[str], Field(None, description="The description of the property group.")
    ]

    property_names: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("propertyNames", "property_names"),
            serialization_alias="propertyNames",
            description="The names of the schema properties for the property group.",
        ),
    ]


"""
SearchDefinitionsProductTypesRequest

Request parameters for searchDefinitionsProductTypes
"""


class SearchDefinitionsProductTypesRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for searchDefinitionsProductTypes
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    keywords: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            description="[QUERY] A comma-delimited list of keywords to search product types. **Note:** Cannot be used with `itemName`.",
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

    item_name: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("itemName", "item_name"),
            serialization_alias="itemName",
            description="[QUERY] The title of the ASIN to get the product type recommendation. **Note:** Cannot be used with `keywords`.",
        ),
    ]

    locale: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            description="[QUERY] The locale for the display names in the response. Defaults to the primary locale of the marketplace.",
        ),
    ]

    search_locale: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("searchLocale", "search_locale"),
            serialization_alias="searchLocale",
            description="[QUERY] The locale used for the `keywords` and `itemName` parameters. Defaults to the primary locale of the marketplace.",
        ),
    ]


# Rebuild models to resolve forward references
Error.model_rebuild()
ErrorList.model_rebuild()
SchemaLink.model_rebuild()
ProductTypeDefinition.model_rebuild()
PropertyGroup.model_rebuild()
ProductTypeVersion.model_rebuild()
ProductType.model_rebuild()
ProductTypeList.model_rebuild()
SearchDefinitionsProductTypesRequest.model_rebuild()
GetDefinitionsProductTypeRequest.model_rebuild()
