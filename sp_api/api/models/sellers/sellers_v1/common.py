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
Address

Represents an address
"""


class Address(SpApiBaseModel):
    """Represents an address"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    address_line1: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("addressLine1", "address_line1"),
            serialization_alias="addressLine1",
            description="Street address information.",
        ),
    ]

    address_line2: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("addressLine2", "address_line2"),
            serialization_alias="addressLine2",
            description="Additional street address information.",
        ),
    ]

    country_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
            description="The country code in two-character ISO 3166-1 alpha-2 format.",
        ),
    ]

    state_or_province_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "stateOrProvinceCode", "state_or_province_code"
            ),
            serialization_alias="stateOrProvinceCode",
            description="The state or province code.",
        ),
    ]

    city: Annotated[Optional[str], Field(None, description="The city.")]

    postal_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("postalCode", "postal_code"),
            serialization_alias="postalCode",
            description="The postal code.",
        ),
    ]


"""
Business

Information about the seller's business. Certain fields may be omitted depending on the seller's `businessType`.
"""


class Business(SpApiBaseModel):
    """Information about the seller's business. Certain fields may be omitted depending on the seller's `businessType`."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[str, Field(..., description="The registered business name.")]

    registered_business_address: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices(
                "registeredBusinessAddress", "registered_business_address"
            ),
            serialization_alias="registeredBusinessAddress",
            description="The registered business address.",
        ),
    ]

    company_registration_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "companyRegistrationNumber", "company_registration_number"
            ),
            serialization_alias="companyRegistrationNumber",
            description="The seller's company registration number, if applicable. This field will be absent for individual sellers and sole proprietorships.",
        ),
    ]

    company_tax_identification_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "companyTaxIdentificationNumber", "company_tax_identification_number"
            ),
            serialization_alias="companyTaxIdentificationNumber",
            description="The seller's company tax identification number, if applicable. This field will be present for certain business types only, such as sole proprietorships.",
        ),
    ]

    non_latin_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nonLatinName", "non_latin_name"),
            serialization_alias="nonLatinName",
            description="The non-Latin script version of the registered business name, if applicable.",
        ),
    ]


MarketplaceParticipationList = List["MarketplaceParticipation"]
"""List of marketplace participations."""


"""
PrimaryContact

Information about the seller's primary contact.
"""


class PrimaryContact(SpApiBaseModel):
    """Information about the seller's primary contact."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[
        str, Field(..., description="The full name of the seller's primary contact.")
    ]

    address: Annotated[
        "Address", Field(..., description="The primary contact's residential address.")
    ]

    non_latin_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nonLatinName", "non_latin_name"),
            serialization_alias="nonLatinName",
            description="The non-Latin script version of the primary contact's name, if applicable.",
        ),
    ]


# Enum definitions
class AccountBusinessTypeEnum(str, Enum):
    """Enum for businessType"""

    CHARITY = "CHARITY"  # The business is registered as a charity.
    CRAFTSMAN = "CRAFTSMAN"  # The business is registered as a craftsman.
    NATURAL_PERSON_COMPANY = (
        "NATURAL_PERSON_COMPANY"  # The business is a natural person company.
    )
    PUBLIC_LISTED = "PUBLIC_LISTED"  # The business is a publicly listed company.
    PRIVATE_LIMITED = "PRIVATE_LIMITED"  # The business is a private limited company.
    SOLE_PROPRIETORSHIP = (
        "SOLE_PROPRIETORSHIP"  # The business is a sole proprietorship.
    )
    STATE_OWNED = "STATE_OWNED"  # The business is state-owned.
    INDIVIDUAL = "INDIVIDUAL"  # The entity is not a business but an individual.


class AccountSellingPlanEnum(str, Enum):
    """Enum for sellingPlan"""

    PROFESSIONAL = "PROFESSIONAL"  # The seller has a professional selling plan.
    INDIVIDUAL = "INDIVIDUAL"  # The seller has an individual selling plan.


"""
Account

The response schema for the `getAccount` operation.
"""


class Account(SpApiBaseModel):
    """The response schema for the `getAccount` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_participation_list: Annotated[
        Optional["MarketplaceParticipationList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "marketplaceParticipationList", "marketplace_participation_list"
            ),
            serialization_alias="marketplaceParticipationList",
        ),
    ]

    business_type: Annotated[
        AccountBusinessTypeEnum,
        Field(
            ...,
            validation_alias=AliasChoices("businessType", "business_type"),
            serialization_alias="businessType",
            description="The type of business registered for the seller account.",
        ),
    ]

    selling_plan: Annotated[
        AccountSellingPlanEnum,
        Field(
            ...,
            validation_alias=AliasChoices("sellingPlan", "selling_plan"),
            serialization_alias="sellingPlan",
            description="The selling plan details.",
        ),
    ]

    business: Annotated[
        Optional["Business"],
        Field(
            None,
        ),
    ]

    primary_contact: Annotated[
        Optional["PrimaryContact"],
        Field(
            None,
            validation_alias=AliasChoices("primaryContact", "primary_contact"),
            serialization_alias="primaryContact",
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
            description="Additional details that can help you understand or fix the issue.",
        ),
    ]


ErrorList = List["Error"]
"""A list of error responses returned when a request is unsuccessful."""


"""
GetAccountResponse

The response schema for the `getAccount` operation.
"""


class GetAccountResponse(SpApiBaseModel):
    """The response schema for the `getAccount` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["Account"],
        Field(
            None,
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None, description="The errors encountered by the `getAccount` operation."
        ),
    ]


"""
GetMarketplaceParticipationsResponse

The response schema for the `getMarketplaceParticipations` operation.
"""


class GetMarketplaceParticipationsResponse(SpApiBaseModel):
    """The response schema for the `getMarketplaceParticipations` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["MarketplaceParticipationList"],
        Field(
            None,
            description="The payload for the `getMarketplaceParticipations` operation.",
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="The errors encountered by the `getMarketplaceParticipations` operation.",
        ),
    ]


"""
Marketplace

Information about an Amazon marketplace where a seller can list items and customers can view and purchase items.
"""


class Marketplace(SpApiBaseModel):
    """Information about an Amazon marketplace where a seller can list items and customers can view and purchase items."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    id: Annotated[str, Field(..., description="The encrypted marketplace value.")]

    name: Annotated[str, Field(..., description="The marketplace name.")]

    country_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
            description="The ISO 3166-1 alpha-2 format country code of the marketplace.",
        ),
    ]

    default_currency_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "defaultCurrencyCode", "default_currency_code"
            ),
            serialization_alias="defaultCurrencyCode",
            description="The ISO 4217 format currency code of the marketplace.",
        ),
    ]

    default_language_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "defaultLanguageCode", "default_language_code"
            ),
            serialization_alias="defaultLanguageCode",
            description="The ISO 639-1 format language code of the marketplace.",
        ),
    ]

    domain_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("domainName", "domain_name"),
            serialization_alias="domainName",
            description="The domain name of the marketplace.",
        ),
    ]


"""
Participation

Information that is specific to a seller in a marketplace.
"""


class Participation(SpApiBaseModel):
    """Information that is specific to a seller in a marketplace."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    is_participating: Annotated[
        bool,
        Field(
            ...,
            validation_alias=AliasChoices("isParticipating", "is_participating"),
            serialization_alias="isParticipating",
            description="If `true`, the seller participates in the marketplace. Otherwise `false`.",
        ),
    ]

    has_suspended_listings: Annotated[
        bool,
        Field(
            ...,
            validation_alias=AliasChoices(
                "hasSuspendedListings", "has_suspended_listings"
            ),
            serialization_alias="hasSuspendedListings",
            description="Specifies if the seller has suspended listings. `true` if the seller Listing Status is set to Inactive, otherwise `false`.",
        ),
    ]


"""
MarketplaceParticipation


"""


class MarketplaceParticipation(SpApiBaseModel):
    """"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace: Annotated[
        Optional["Marketplace"],
        Field(
            None,
        ),
    ]

    participation: Annotated[
        "Participation",
        Field(
            ...,
        ),
    ]

    store_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("storeName", "store_name"),
            serialization_alias="storeName",
            description="The name of the seller's store as displayed in the marketplace.",
        ),
    ]


# Rebuild models to resolve forward references
Error.model_rebuild()
MarketplaceParticipation.model_rebuild()
GetMarketplaceParticipationsResponse.model_rebuild()
Marketplace.model_rebuild()
Participation.model_rebuild()
GetAccountResponse.model_rebuild()
Account.model_rebuild()
Business.model_rebuild()
Address.model_rebuild()
PrimaryContact.model_rebuild()
