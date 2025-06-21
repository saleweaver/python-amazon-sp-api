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


"""
ItemQuantity

Details of item quantity.
"""


class ItemQuantity(SpApiBaseModel):
    """Details of item quantity."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amount: Annotated[
        Optional[int],
        Field(None, description="Quantity of units available for a specific item."),
    ]

    unit_of_measure: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("unitOfMeasure", "unit_of_measure"),
            serialization_alias="unitOfMeasure",
            description="Unit of measure for the available quantity.",
        ),
    ]


"""
ItemDetails

Updated inventory details for an item.
"""


class ItemDetails(SpApiBaseModel):
    """Updated inventory details for an item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    buyer_product_identifier: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "buyerProductIdentifier", "buyer_product_identifier"
            ),
            serialization_alias="buyerProductIdentifier",
            description="The buyer selected product identification of the item. Either buyerProductIdentifier or vendorProductIdentifier should be submitted.",
        ),
    ]

    vendor_product_identifier: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "vendorProductIdentifier", "vendor_product_identifier"
            ),
            serialization_alias="vendorProductIdentifier",
            description="The vendor selected product identification of the item. Either buyerProductIdentifier or vendorProductIdentifier should be submitted.",
        ),
    ]

    available_quantity: Annotated[
        "ItemQuantity",
        Field(
            ...,
            validation_alias=AliasChoices("availableQuantity", "available_quantity"),
            serialization_alias="availableQuantity",
            description="Total item quantity available in the warehouse.",
        ),
    ]

    is_obsolete: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("isObsolete", "is_obsolete"),
            serialization_alias="isObsolete",
            description="When true, the item is permanently unavailable.",
        ),
    ]


"""
PartyIdentification

Name, address and tax details of a party.
"""


class PartyIdentification(SpApiBaseModel):
    """Name, address and tax details of a party."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    party_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("partyId", "party_id"),
            serialization_alias="partyId",
            description="Assigned identification for the party.",
        ),
    ]


"""
InventoryUpdate

Inventory details required to update some or all items for the requested warehouse.
"""


class InventoryUpdate(SpApiBaseModel):
    """Inventory details required to update some or all items for the requested warehouse."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    selling_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("sellingParty", "selling_party"),
            serialization_alias="sellingParty",
            description="ID of the selling party or vendor.",
        ),
    ]

    is_full_update: Annotated[
        bool,
        Field(
            ...,
            validation_alias=AliasChoices("isFullUpdate", "is_full_update"),
            serialization_alias="isFullUpdate",
            description="When true, this request contains a full feed. Otherwise, this request contains a partial feed. When sending a full feed, you must send information about all items in the warehouse. Any items not in the full feed are updated as not available. When sending a partial feed, only include the items that need an update to inventory. The status of other items will remain unchanged.",
        ),
    ]

    items: Annotated[
        List["ItemDetails"],
        Field(
            ...,
            description="A list of inventory items with updated details, including quantity available.",
        ),
    ]


"""
SubmitInventoryUpdateRequestBody

The request body for the submitInventoryUpdate operation.
"""


class SubmitInventoryUpdateRequestBody(SpApiBaseModel):
    """The request body for the submitInventoryUpdate operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inventory: Annotated[
        Optional["InventoryUpdate"],
        Field(
            None,
            description="Inventory details required to update some or all items for the requested warehouse.",
        ),
    ]


"""
SubmitInventoryUpdateRequest

Request parameters for submitInventoryUpdate
"""


class SubmitInventoryUpdateRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for submitInventoryUpdate
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "SubmitInventoryUpdateRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The request body containing the inventory update data to submit.",
        ),
    ]

    warehouse_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("warehouseId", "warehouse_id"),
            serialization_alias="warehouseId",
            description="[PATH] Identifier for the warehouse for which to update inventory.",
        ),
    ]


"""
TransactionReference

Response containing the transaction ID.
"""


class TransactionReference(SpApiBaseModel):
    """Response containing the transaction ID."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    transaction_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("transactionId", "transaction_id"),
            serialization_alias="transactionId",
            description="GUID to identify this transaction. This value can be used with the Transaction Status API to return the status of this transaction.",
        ),
    ]


"""
SubmitInventoryUpdateResponse

The response schema for the submitInventoryUpdate operation.
"""


class SubmitInventoryUpdateResponse(SpApiBaseModel):
    """The response schema for the submitInventoryUpdate operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["TransactionReference"],
        Field(
            None,
            description="The response payload for the submitInventoryUpdate operation.",
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


# Rebuild models to resolve forward references
SubmitInventoryUpdateRequestBody.model_rebuild()
InventoryUpdate.model_rebuild()
ItemDetails.model_rebuild()
PartyIdentification.model_rebuild()
ItemQuantity.model_rebuild()
SubmitInventoryUpdateResponse.model_rebuild()
TransactionReference.model_rebuild()
Error.model_rebuild()
SubmitInventoryUpdateRequest.model_rebuild()
