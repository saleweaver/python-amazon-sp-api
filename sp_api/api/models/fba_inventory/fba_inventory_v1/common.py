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

InventoryItems = List["InventoryItem"]
"""List of Inventory to be added"""


"""
AddInventoryRequestBody

The object with the list of Inventory to be added
"""


class AddInventoryRequestBody(SpApiBaseModel):
    """The object with the list of Inventory to be added"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inventory_items: Annotated[
        Optional["InventoryItems"],
        Field(
            None,
            validation_alias=AliasChoices("inventoryItems", "inventory_items"),
            serialization_alias="inventoryItems",
        ),
    ]


"""
AddInventoryRequest

Request parameters for addInventory
"""


class AddInventoryRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for addInventory
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    add_inventory_request_body: Annotated[
        "AddInventoryRequestBody",
        BodyParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "addInventoryRequestBody", "add_inventory_request_body"
            ),
            serialization_alias="addInventoryRequestBody",
            description="[BODY] List of items to add to Sandbox inventory.",
        ),
    ]


ErrorList = List["Error"]
"""A list of error responses returned when a request is unsuccessful."""


"""
AddInventoryResponse

The response schema for the AddInventory operation.
"""


class AddInventoryResponse(SpApiBaseModel):
    """The response schema for the AddInventory operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the AddInventory operation.",
        ),
    ]


"""
CreateInventoryItemRequestBody

An item to be created in the inventory.
"""


class CreateInventoryItemRequestBody(SpApiBaseModel):
    """An item to be created in the inventory."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_sku: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("sellerSku", "seller_sku"),
            serialization_alias="sellerSku",
            description="The seller SKU of the item.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The marketplaceId.",
        ),
    ]

    product_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("productName", "product_name"),
            serialization_alias="productName",
            description="The name of the item.",
        ),
    ]


"""
CreateInventoryItemRequest

Request parameters for createInventoryItem
"""


class CreateInventoryItemRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createInventoryItem
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    create_inventory_item_request_body: Annotated[
        "CreateInventoryItemRequestBody",
        BodyParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "createInventoryItemRequestBody", "create_inventory_item_request_body"
            ),
            serialization_alias="createInventoryItemRequestBody",
            description="[BODY] CreateInventoryItem RequestBody Body Parameter.",
        ),
    ]


"""
CreateInventoryItemResponse

The response schema for the CreateInventoryItem operation.
"""


class CreateInventoryItemResponse(SpApiBaseModel):
    """The response schema for the CreateInventoryItem operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the CreateInventoryItem operation.",
        ),
    ]


"""
DeleteInventoryItemRequest

Request parameters for deleteInventoryItem
"""


class DeleteInventoryItemRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for deleteInventoryItem
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_sku: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("sellerSku", "seller_sku"),
            serialization_alias="sellerSku",
            description="[PATH] A single seller SKU used for querying the specified seller SKU inventory summaries.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The marketplace ID for the marketplace for which the sellerSku is to be deleted.",
        ),
    ]


"""
DeleteInventoryItemResponse

The response schema for the DeleteInventoryItem operation.
"""


class DeleteInventoryItemResponse(SpApiBaseModel):
    """The response schema for the DeleteInventoryItem operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the DeleteInventoryItem operation.",
        ),
    ]


"""
Error

An error response returned when the request is unsuccessful.
"""


class Error(SpApiBaseModel):
    """An error response returned when the request is unsuccessful."""

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
        Optional[str],
        Field(
            None,
            description="A message that describes the error condition in a human-readable form.",
        ),
    ]

    details: Annotated[
        Optional[str],
        Field(
            None,
            description="Additional information that can help the caller understand or fix the issue.",
        ),
    ]


# Enum definitions
class GetInventorySummariesRequestGranularityTypeEnum(str, Enum):
    """Enum for granularityType"""

    MARKETPLACE = "Marketplace"  # Marketplace


"""
GetInventorySummariesRequest

Request parameters for getInventorySummaries
"""


class GetInventorySummariesRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getInventorySummaries
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    details: Annotated[
        Optional[bool],
        QueryParam(),
        Field(
            None,
            description="[QUERY] true to return inventory summaries with additional summarized inventory details and quantities. Otherwise, returns inventory summaries only (default value).",
        ),
    ]

    granularity_type: Annotated[
        GetInventorySummariesRequestGranularityTypeEnum,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("granularityType", "granularity_type"),
            serialization_alias="granularityType",
            description="[QUERY] The granularity type for the inventory aggregation level.",
        ),
    ]

    granularity_id: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("granularityId", "granularity_id"),
            serialization_alias="granularityId",
            description="[QUERY] The granularity ID for the inventory aggregation level.",
        ),
    ]

    start_date_time: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("startDateTime", "start_date_time"),
            serialization_alias="startDateTime",
            description="[QUERY] A start date and time in ISO8601 format. If specified, all inventory summaries that have changed since then are returned. You must specify a date and time that is no earlier than 18 months prior to the date and time when you call the API. Note: Changes in inboundWorkingQuantity, inboundShippedQuantity and inboundReceivingQuantity are not detected.",
        ),
    ]

    seller_skus: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("sellerSkus", "seller_skus"),
            serialization_alias="sellerSkus",
            description="[QUERY] A list of seller SKUs for which to return inventory summaries. You may specify up to 50 SKUs.",
        ),
    ]

    seller_sku: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("sellerSku", "seller_sku"),
            serialization_alias="sellerSku",
            description="[QUERY] A single seller SKU used for querying the specified seller SKU inventory summaries.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="[QUERY] String token returned in the response of your previous request. The string token will expire 30 seconds after being created.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] The marketplace ID for the marketplace for which to return inventory summaries.",
        ),
    ]


"""
Granularity

Describes a granularity at which inventory data can be aggregated. For example, if you use Marketplace granularity, the fulfillable quantity will reflect inventory that could be fulfilled in the given marketplace.
"""


class Granularity(SpApiBaseModel):
    """Describes a granularity at which inventory data can be aggregated. For example, if you use Marketplace granularity, the fulfillable quantity will reflect inventory that could be fulfilled in the given marketplace."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    granularity_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("granularityType", "granularity_type"),
            serialization_alias="granularityType",
            description="The granularity type for the inventory aggregation level.",
        ),
    ]

    granularity_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("granularityId", "granularity_id"),
            serialization_alias="granularityId",
            description="The granularity ID for the specified granularity type. When granularityType is Marketplace, specify the marketplaceId.",
        ),
    ]


InventorySummaries = List["InventorySummary"]
"""A list of inventory summaries."""


"""
GetInventorySummariesResult

The payload schema for the getInventorySummaries operation.
"""


class GetInventorySummariesResult(SpApiBaseModel):
    """The payload schema for the getInventorySummaries operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    granularity: Annotated[
        "Granularity",
        Field(
            ...,
        ),
    ]

    inventory_summaries: Annotated[
        "InventorySummaries",
        Field(
            ...,
            validation_alias=AliasChoices("inventorySummaries", "inventory_summaries"),
            serialization_alias="inventorySummaries",
        ),
    ]


"""
Pagination

The process of returning the results to a request in batches of a defined size called pages. This is done to exercise some control over result size and overall throughput. It's a form of traffic management.
"""


class Pagination(SpApiBaseModel):
    """The process of returning the results to a request in batches of a defined size called pages. This is done to exercise some control over result size and overall throughput. It's a form of traffic management."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    next_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="A generated string used to retrieve the next page of the result. If nextToken is returned, pass the value of nextToken to the next request. If nextToken is not returned, there are no more items to return.",
        ),
    ]


"""
GetInventorySummariesResponse

The Response schema.
"""


class GetInventorySummariesResponse(SpApiBaseModel):
    """The Response schema."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["GetInventorySummariesResult"],
        Field(None, description="The payload for the getInventorySummaries operation."),
    ]

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the getInventorySummaries operation.",
        ),
    ]


# Enum definitions
class ResearchingQuantityEntryNameEnum(str, Enum):
    """Enum for name"""

    RESEARCHING_QUANTITY_IN_SHORT_TERM = (
        "researchingQuantityInShortTerm"  # Short Term for 1-10 days.
    )
    RESEARCHING_QUANTITY_IN_MID_TERM = (
        "researchingQuantityInMidTerm"  # Mid Term for 11-20 days.
    )
    RESEARCHING_QUANTITY_IN_LONG_TERM = (
        "researchingQuantityInLongTerm"  # Long Term for 21 days or longer.
    )


"""
ResearchingQuantityEntry

The misplaced or warehouse damaged inventory that is actively being confirmed at our fulfillment centers.
"""


class ResearchingQuantityEntry(SpApiBaseModel):
    """The misplaced or warehouse damaged inventory that is actively being confirmed at our fulfillment centers."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[
        ResearchingQuantityEntryNameEnum,
        Field(..., description="The duration of the research."),
    ]

    quantity: Annotated[int, Field(..., description="The number of units.")]


"""
ResearchingQuantity

The number of misplaced or warehouse damaged units that are actively being confirmed at our fulfillment centers.
"""


class ResearchingQuantity(SpApiBaseModel):
    """The number of misplaced or warehouse damaged units that are actively being confirmed at our fulfillment centers."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    total_researching_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "totalResearchingQuantity", "total_researching_quantity"
            ),
            serialization_alias="totalResearchingQuantity",
            description="The total number of units currently being researched in Amazon's fulfillment network.",
        ),
    ]

    researching_quantity_breakdown: Annotated[
        Optional[List["ResearchingQuantityEntry"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "researchingQuantityBreakdown", "researching_quantity_breakdown"
            ),
            serialization_alias="researchingQuantityBreakdown",
            description="A list of quantity details for items currently being researched.",
        ),
    ]


"""
ReservedQuantity

The quantity of reserved inventory.
"""


class ReservedQuantity(SpApiBaseModel):
    """The quantity of reserved inventory."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    total_reserved_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "totalReservedQuantity", "total_reserved_quantity"
            ),
            serialization_alias="totalReservedQuantity",
            description="The total number of units in Amazon's fulfillment network that are currently being picked, packed, and shipped; or are sidelined for measurement, sampling, or other internal processes.",
        ),
    ]

    pending_customer_order_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "pendingCustomerOrderQuantity", "pending_customer_order_quantity"
            ),
            serialization_alias="pendingCustomerOrderQuantity",
            description="The number of units reserved for customer orders.",
        ),
    ]

    pending_transshipment_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "pendingTransshipmentQuantity", "pending_transshipment_quantity"
            ),
            serialization_alias="pendingTransshipmentQuantity",
            description="The number of units being transferred from one fulfillment center to another.",
        ),
    ]

    fc_processing_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "fcProcessingQuantity", "fc_processing_quantity"
            ),
            serialization_alias="fcProcessingQuantity",
            description="The number of units that have been sidelined at the fulfillment center for additional processing.",
        ),
    ]


"""
UnfulfillableQuantity

The quantity of unfulfillable inventory.
"""


class UnfulfillableQuantity(SpApiBaseModel):
    """The quantity of unfulfillable inventory."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    total_unfulfillable_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "totalUnfulfillableQuantity", "total_unfulfillable_quantity"
            ),
            serialization_alias="totalUnfulfillableQuantity",
            description="The total number of units in Amazon's fulfillment network in unsellable condition.",
        ),
    ]

    customer_damaged_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "customerDamagedQuantity", "customer_damaged_quantity"
            ),
            serialization_alias="customerDamagedQuantity",
            description="The number of units in customer damaged disposition.",
        ),
    ]

    warehouse_damaged_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "warehouseDamagedQuantity", "warehouse_damaged_quantity"
            ),
            serialization_alias="warehouseDamagedQuantity",
            description="The number of units in warehouse damaged disposition.",
        ),
    ]

    distributor_damaged_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "distributorDamagedQuantity", "distributor_damaged_quantity"
            ),
            serialization_alias="distributorDamagedQuantity",
            description="The number of units in distributor damaged disposition.",
        ),
    ]

    carrier_damaged_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "carrierDamagedQuantity", "carrier_damaged_quantity"
            ),
            serialization_alias="carrierDamagedQuantity",
            description="The number of units in carrier damaged disposition.",
        ),
    ]

    defective_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("defectiveQuantity", "defective_quantity"),
            serialization_alias="defectiveQuantity",
            description="The number of units in defective disposition.",
        ),
    ]

    expired_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("expiredQuantity", "expired_quantity"),
            serialization_alias="expiredQuantity",
            description="The number of units in expired disposition.",
        ),
    ]


"""
InventoryDetails

Summarized inventory details. This object will not appear if the details parameter in the request is false.
"""


class InventoryDetails(SpApiBaseModel):
    """Summarized inventory details. This object will not appear if the details parameter in the request is false."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    fulfillable_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "fulfillableQuantity", "fulfillable_quantity"
            ),
            serialization_alias="fulfillableQuantity",
            description="The item quantity that can be picked, packed, and shipped.",
        ),
    ]

    inbound_working_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "inboundWorkingQuantity", "inbound_working_quantity"
            ),
            serialization_alias="inboundWorkingQuantity",
            description="The number of units in an inbound shipment for which you have notified Amazon.",
        ),
    ]

    inbound_shipped_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "inboundShippedQuantity", "inbound_shipped_quantity"
            ),
            serialization_alias="inboundShippedQuantity",
            description="The number of units in an inbound shipment that you have notified Amazon about and have provided a tracking number.",
        ),
    ]

    inbound_receiving_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "inboundReceivingQuantity", "inbound_receiving_quantity"
            ),
            serialization_alias="inboundReceivingQuantity",
            description="The number of units that have not yet been received at an Amazon fulfillment center for processing, but are part of an inbound shipment with some units that have already been received and processed.",
        ),
    ]

    reserved_quantity: Annotated[
        Optional["ReservedQuantity"],
        Field(
            None,
            validation_alias=AliasChoices("reservedQuantity", "reserved_quantity"),
            serialization_alias="reservedQuantity",
        ),
    ]

    researching_quantity: Annotated[
        Optional["ResearchingQuantity"],
        Field(
            None,
            validation_alias=AliasChoices(
                "researchingQuantity", "researching_quantity"
            ),
            serialization_alias="researchingQuantity",
        ),
    ]

    unfulfillable_quantity: Annotated[
        Optional["UnfulfillableQuantity"],
        Field(
            None,
            validation_alias=AliasChoices(
                "unfulfillableQuantity", "unfulfillable_quantity"
            ),
            serialization_alias="unfulfillableQuantity",
        ),
    ]


"""
InventoryItem

An item in the list of inventory to be added.
"""


class InventoryItem(SpApiBaseModel):
    """An item in the list of inventory to be added."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_sku: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("sellerSku", "seller_sku"),
            serialization_alias="sellerSku",
            description="The seller SKU of the item.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The marketplaceId.",
        ),
    ]

    quantity: Annotated[int, Field(..., description="The quantity of item to add.")]


"""
InventorySummary

Inventory summary for a specific item.
"""


class InventorySummary(SpApiBaseModel):
    """Inventory summary for a specific item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    asin: Annotated[
        Optional[str],
        Field(
            None,
            description="The Amazon Standard Identification Number (ASIN) of an item.",
        ),
    ]

    fn_sku: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("fnSku", "fn_sku"),
            serialization_alias="fnSku",
            description="Amazon's fulfillment network SKU identifier.",
        ),
    ]

    seller_sku: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("sellerSku", "seller_sku"),
            serialization_alias="sellerSku",
            description="The seller SKU of the item.",
        ),
    ]

    condition: Annotated[
        Optional[str],
        Field(
            None,
            description="The condition of the item as described by the seller (for example, New Item).",
        ),
    ]

    inventory_details: Annotated[
        Optional["InventoryDetails"],
        Field(
            None,
            validation_alias=AliasChoices("inventoryDetails", "inventory_details"),
            serialization_alias="inventoryDetails",
        ),
    ]

    last_updated_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("lastUpdatedTime", "last_updated_time"),
            serialization_alias="lastUpdatedTime",
            description="The date and time that any quantity was last updated.",
        ),
    ]

    product_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("productName", "product_name"),
            serialization_alias="productName",
            description="The localized language product title of the item within the specific marketplace.",
        ),
    ]

    total_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("totalQuantity", "total_quantity"),
            serialization_alias="totalQuantity",
            description="The total number of units in an inbound shipment or in Amazon fulfillment centers.",
        ),
    ]

    stores: Annotated[
        Optional[List["str"]],
        Field(
            None,
            description="A list of seller-enrolled stores that apply to this seller SKU.",
        ),
    ]


# Rebuild models to resolve forward references
CreateInventoryItemRequestBody.model_rebuild()
AddInventoryRequestBody.model_rebuild()
InventoryItem.model_rebuild()
CreateInventoryItemResponse.model_rebuild()
DeleteInventoryItemResponse.model_rebuild()
AddInventoryResponse.model_rebuild()
Granularity.model_rebuild()
ReservedQuantity.model_rebuild()
ResearchingQuantityEntry.model_rebuild()
ResearchingQuantity.model_rebuild()
UnfulfillableQuantity.model_rebuild()
InventoryDetails.model_rebuild()
InventorySummary.model_rebuild()
Pagination.model_rebuild()
GetInventorySummariesResult.model_rebuild()
GetInventorySummariesResponse.model_rebuild()
Error.model_rebuild()
GetInventorySummariesRequest.model_rebuild()
CreateInventoryItemRequest.model_rebuild()
DeleteInventoryItemRequest.model_rebuild()
AddInventoryRequest.model_rebuild()
