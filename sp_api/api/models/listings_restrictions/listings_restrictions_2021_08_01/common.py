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


ErrorList = List["Error"]
"""A list of error responses returned when a request is unsuccessful."""


# Enum definitions
class ConditionTypeEnum(str, Enum):
    """Enum for conditionType"""

    NEW_NEW = "new_new"  # New
    NEW_OPEN_BOX = "new_open_box"  # New - Open Box.
    NEW_OEM = "new_oem"  # New - OEM.
    REFURBISHED_REFURBISHED = "refurbished_refurbished"  # Refurbished
    USED_LIKE_NEW = "used_like_new"  # Used - Like New.
    USED_VERY_GOOD = "used_very_good"  # Used - Very Good.
    USED_GOOD = "used_good"  # Used - Good.
    USED_ACCEPTABLE = "used_acceptable"  # Used - Acceptable.
    COLLECTIBLE_LIKE_NEW = "collectible_like_new"  # Collectible - Like New.
    COLLECTIBLE_VERY_GOOD = "collectible_very_good"  # Collectible - Very Good.
    COLLECTIBLE_GOOD = "collectible_good"  # Collectible - Good.
    COLLECTIBLE_ACCEPTABLE = "collectible_acceptable"  # Collectible - Acceptable.
    CLUB_CLUB = "club_club"  # Club


"""
GetListingsRestrictionsRequest

Request parameters for getListingsRestrictions
"""


class GetListingsRestrictionsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getListingsRestrictions
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    asin: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            description="[QUERY] The Amazon Standard Identification Number (ASIN) of the item.",
        ),
    ]

    condition_type: Annotated[
        Optional[ConditionTypeEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("conditionType", "condition_type"),
            serialization_alias="conditionType",
            description="[QUERY] The condition used to filter restrictions.",
        ),
    ]

    seller_id: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("sellerId", "seller_id"),
            serialization_alias="sellerId",
            description="[QUERY] A selling partner identifier, such as a merchant account.",
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

    reason_locale: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("reasonLocale", "reason_locale"),
            serialization_alias="reasonLocale",
            description="[QUERY] A locale for reason text localization. When not provided, the default language code of the first marketplace is used. Examples: 'en_US', 'fr_CA', 'fr_FR'. Localized messages default to 'en_US' when a localization is not available in the specified locale.",
        ),
    ]


# Enum definitions
class VerbEnum(str, Enum):
    """Enum for verb"""

    GET = "GET"  # The provided resource is accessed with the HTTP GET method.


"""
Link

A link to resources related to a listing restriction.
"""


class Link(SpApiBaseModel):
    """A link to resources related to a listing restriction."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    resource: Annotated[str, Field(..., description="The URI of the related resource.")]

    verb: Annotated[
        VerbEnum,
        Field(
            ..., description="The HTTP verb used to interact with the related resource."
        ),
    ]

    title: Annotated[
        Optional[str], Field(None, description="The title of the related resource.")
    ]

    type: Annotated[
        Optional[str],
        Field(None, description="The media type of the related resource."),
    ]


# Enum definitions
class ReasonCodeEnum(str, Enum):
    """Enum for reasonCode"""

    APPROVAL_REQUIRED = "APPROVAL_REQUIRED"  # Approval is required to create a listing for the specified ASIN. A path forward link will be provided that may allow Selling Partners to remove the restriction.
    ASIN_NOT_FOUND = "ASIN_NOT_FOUND"  # The specified ASIN does not exist in the requested marketplace.
    NOT_ELIGIBLE = "NOT_ELIGIBLE"  # Not eligible to create a listing for the specified ASIN. No path forward link will be provided to remove the restriction.


"""
Reason

A reason for the restriction, including path forward links that may allow Selling Partners to remove the restriction, if available.
"""


class Reason(SpApiBaseModel):
    """A reason for the restriction, including path forward links that may allow Selling Partners to remove the restriction, if available."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    message: Annotated[
        str,
        Field(..., description="A message describing the reason for the restriction."),
    ]

    reason_code: Annotated[
        Optional[ReasonCodeEnum],
        Field(
            None,
            validation_alias=AliasChoices("reasonCode", "reason_code"),
            serialization_alias="reasonCode",
            description="A code indicating why the listing is restricted.",
        ),
    ]

    links: Annotated[
        Optional[List["Link"]],
        Field(
            None,
            description="A list of path forward links that may allow Selling Partners to remove the restriction.",
        ),
    ]


# Enum definitions
class ConditionTypeEnum(str, Enum):
    """Enum for conditionType"""

    NEW_NEW = "new_new"  # New
    NEW_OPEN_BOX = "new_open_box"  # New - Open Box.
    NEW_OEM = "new_oem"  # New - OEM.
    REFURBISHED_REFURBISHED = "refurbished_refurbished"  # Refurbished
    USED_LIKE_NEW = "used_like_new"  # Used - Like New.
    USED_VERY_GOOD = "used_very_good"  # Used - Very Good.
    USED_GOOD = "used_good"  # Used - Good.
    USED_ACCEPTABLE = "used_acceptable"  # Used - Acceptable.
    COLLECTIBLE_LIKE_NEW = "collectible_like_new"  # Collectible - Like New.
    COLLECTIBLE_VERY_GOOD = "collectible_very_good"  # Collectible - Very Good.
    COLLECTIBLE_GOOD = "collectible_good"  # Collectible - Good.
    COLLECTIBLE_ACCEPTABLE = "collectible_acceptable"  # Collectible - Acceptable.
    CLUB_CLUB = "club_club"  # Club


"""
Restriction

A listing restriction, optionally qualified by a condition, with a list of reasons for the restriction.
"""


class Restriction(SpApiBaseModel):
    """A listing restriction, optionally qualified by a condition, with a list of reasons for the restriction."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="A marketplace identifier. Identifies the Amazon marketplace where the restriction is enforced.",
        ),
    ]

    condition_type: Annotated[
        Optional[ConditionTypeEnum],
        Field(
            None,
            validation_alias=AliasChoices("conditionType", "condition_type"),
            serialization_alias="conditionType",
            description="The condition that applies to the restriction.",
        ),
    ]

    reasons: Annotated[
        Optional[List["Reason"]],
        Field(None, description="A list of reasons for the restriction."),
    ]


"""
RestrictionList

A list of restrictions for the specified Amazon catalog item.
"""


class RestrictionList(SpApiBaseModel):
    """A list of restrictions for the specified Amazon catalog item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    restrictions: Annotated[
        List["Restriction"],
        Field(
            ...,
        ),
    ]


# Rebuild models to resolve forward references
RestrictionList.model_rebuild()
Restriction.model_rebuild()
Reason.model_rebuild()
Link.model_rebuild()
Error.model_rebuild()
GetListingsRestrictionsRequest.model_rebuild()
