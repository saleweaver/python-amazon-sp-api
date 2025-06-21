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

AmazonOrderId = str
"""An Amazon-defined order identifier. Identifies the order that the seller wants to deliver using Amazon Easy Ship."""


Code = str
"""An error code that identifies the type of error that occurred. The error codes listed below are specific to the Easy Ship section."""


LabelFormat = str
"""The file format in which the shipping label will be created."""


Items = List["Item"]
"""A list of items contained in the package."""


PackageIdentifier = str
"""Optional seller-created identifier that is printed on the shipping label to help the seller identify the package."""


DateTime = str
"""A datetime value in ISO 8601 format."""


HandoverMethod = str
"""Identifies the method by which a seller will hand a package over to Amazon Logistics."""


String = str
"""A string of up to 255 characters."""


"""
TimeSlot

A time window to hand over an Easy Ship package to Amazon Logistics.
"""


class TimeSlot(SpApiBaseModel):
    """A time window to hand over an Easy Ship package to Amazon Logistics."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    slot_id: Annotated[
        "String",
        Field(
            ...,
            validation_alias=AliasChoices("slotId", "slot_id"),
            serialization_alias="slotId",
            description="An Amazon-defined identifier for a time slot.",
        ),
    ]

    start_time: Annotated[
        Optional["DateTime"],
        Field(
            None,
            validation_alias=AliasChoices("startTime", "start_time"),
            serialization_alias="startTime",
            description="The start date and time of the time slot.",
        ),
    ]

    end_time: Annotated[
        Optional["DateTime"],
        Field(
            None,
            validation_alias=AliasChoices("endTime", "end_time"),
            serialization_alias="endTime",
            description="The end date and time of the time slot.",
        ),
    ]

    handover_method: Annotated[
        Optional["HandoverMethod"],
        Field(
            None,
            validation_alias=AliasChoices("handoverMethod", "handover_method"),
            serialization_alias="handoverMethod",
            description="The method by which a seller will hand a package over to Amazon Logistics.",
        ),
    ]


"""
PackageDetails

Package details. Includes `packageItems`, `packageTimeSlot`, and `packageIdentifier`.
"""


class PackageDetails(SpApiBaseModel):
    """Package details. Includes `packageItems`, `packageTimeSlot`, and `packageIdentifier`."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    package_items: Annotated[
        Optional["Items"],
        Field(
            None,
            validation_alias=AliasChoices("packageItems", "package_items"),
            serialization_alias="packageItems",
        ),
    ]

    package_time_slot: Annotated[
        "TimeSlot",
        Field(
            ...,
            validation_alias=AliasChoices("packageTimeSlot", "package_time_slot"),
            serialization_alias="packageTimeSlot",
        ),
    ]

    package_identifier: Annotated[
        Optional["PackageIdentifier"],
        Field(
            None,
            validation_alias=AliasChoices("packageIdentifier", "package_identifier"),
            serialization_alias="packageIdentifier",
        ),
    ]


"""
OrderScheduleDetails

This object allows users to specify an order to be scheduled. Only the amazonOrderId is required. 
"""


class OrderScheduleDetails(SpApiBaseModel):
    """This object allows users to specify an order to be scheduled. Only the amazonOrderId is required."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        "AmazonOrderId",
        Field(
            ...,
            validation_alias=AliasChoices("amazonOrderId", "amazon_order_id"),
            serialization_alias="amazonOrderId",
        ),
    ]

    package_details: Annotated[
        Optional["PackageDetails"],
        Field(
            None,
            validation_alias=AliasChoices("packageDetails", "package_details"),
            serialization_alias="packageDetails",
        ),
    ]


"""
CreateScheduledPackagesRequestBody

The request body for the POST /easyShip/2022-03-23/packages/bulk API.
"""


class CreateScheduledPackagesRequestBody(SpApiBaseModel):
    """The request body for the POST /easyShip/2022-03-23/packages/bulk API."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional["String"],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
        ),
    ]

    order_schedule_details_list: Annotated[
        List["OrderScheduleDetails"],
        Field(
            ...,
            validation_alias=AliasChoices(
                "orderScheduleDetailsList", "order_schedule_details_list"
            ),
            serialization_alias="orderScheduleDetailsList",
            description="An array allowing users to specify orders to be scheduled.",
        ),
    ]

    label_format: Annotated[
        "LabelFormat",
        Field(
            ...,
            validation_alias=AliasChoices("labelFormat", "label_format"),
            serialization_alias="labelFormat",
        ),
    ]


"""
CreateScheduledPackageBulkRequest

Request parameters for createScheduledPackageBulk
"""


class CreateScheduledPackageBulkRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createScheduledPackageBulk
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    create_scheduled_packages_request_body: Annotated[
        "CreateScheduledPackagesRequestBody",
        BodyParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "CreateScheduledPackagesRequestBody",
                "create_scheduled_packages_request_body",
            ),
            serialization_alias="CreateScheduledPackagesRequestBody",
            description="[BODY] The request schema for the `createScheduledPackageBulk` operation.",
        ),
    ]


"""
CreateScheduledPackageRequestBody

The request schema for the `createScheduledPackage` operation.
"""


class CreateScheduledPackageRequestBody(SpApiBaseModel):
    """The request schema for the `createScheduledPackage` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        "AmazonOrderId",
        Field(
            ...,
            validation_alias=AliasChoices("amazonOrderId", "amazon_order_id"),
            serialization_alias="amazonOrderId",
        ),
    ]

    marketplace_id: Annotated[
        Optional["String"],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
        ),
    ]

    package_details: Annotated[
        "PackageDetails",
        Field(
            ...,
            validation_alias=AliasChoices("packageDetails", "package_details"),
            serialization_alias="packageDetails",
        ),
    ]


"""
CreateScheduledPackageRequest

Request parameters for createScheduledPackage
"""


class CreateScheduledPackageRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createScheduledPackage
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    create_scheduled_package_request_body: Annotated[
        "CreateScheduledPackageRequestBody",
        BodyParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "CreateScheduledPackageRequestBody",
                "create_scheduled_package_request_body",
            ),
            serialization_alias="CreateScheduledPackageRequestBody",
            description="[BODY] The request schema for the `createScheduledPackage` operation.",
        ),
    ]


Dimension = float
"""The numerical value of the specified dimension."""


UnitOfLength = str
"""The unit of measurement used to measure the length."""


"""
Dimensions

The dimensions of the scheduled package.
"""


class Dimensions(SpApiBaseModel):
    """The dimensions of the scheduled package."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    length: Annotated[
        Optional["Dimension"], Field(None, description="The length dimension.")
    ]

    width: Annotated[
        Optional["Dimension"], Field(None, description="The width dimension.")
    ]

    height: Annotated[
        Optional["Dimension"], Field(None, description="The height dimension.")
    ]

    unit: Annotated[
        Optional["UnitOfLength"],
        Field(
            None,
        ),
    ]

    identifier: Annotated[
        Optional["String"],
        Field(None, description="Identifier for custom package dimensions."),
    ]


"""
InvoiceData

Invoice number and date.
"""


class InvoiceData(SpApiBaseModel):
    """Invoice number and date."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    invoice_number: Annotated[
        "String",
        Field(
            ...,
            validation_alias=AliasChoices("invoiceNumber", "invoice_number"),
            serialization_alias="invoiceNumber",
            description="The invoice number.",
        ),
    ]

    invoice_date: Annotated[
        Optional["DateTime"],
        Field(
            None,
            validation_alias=AliasChoices("invoiceDate", "invoice_date"),
            serialization_alias="invoiceDate",
            description="The date that the invoice was generated.",
        ),
    ]


PackageStatus = str
"""The status of the package."""


PackageId = str
"""An Amazon-defined identifier for the scheduled package."""


"""
ScheduledPackageId

Identifies the scheduled package to be updated.
"""


class ScheduledPackageId(SpApiBaseModel):
    """Identifies the scheduled package to be updated."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        "AmazonOrderId",
        Field(
            ...,
            validation_alias=AliasChoices("amazonOrderId", "amazon_order_id"),
            serialization_alias="amazonOrderId",
        ),
    ]

    package_id: Annotated[
        Optional["PackageId"],
        Field(
            None,
            validation_alias=AliasChoices("packageId", "package_id"),
            serialization_alias="packageId",
        ),
    ]


"""
TrackingDetails

Representation of tracking metadata.
"""


class TrackingDetails(SpApiBaseModel):
    """Representation of tracking metadata."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    tracking_id: Annotated[
        Optional["String"],
        Field(
            None,
            validation_alias=AliasChoices("trackingId", "tracking_id"),
            serialization_alias="trackingId",
            description="The tracking identifier for the scheduled package.",
        ),
    ]


UnitOfWeight = str
"""The unit of measurement used to measure the weight."""


WeightValue = float
"""The weight of the package."""


"""
Weight

The weight of the scheduled package
"""


class Weight(SpApiBaseModel):
    """The weight of the scheduled package"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    value: Annotated[
        Optional["WeightValue"],
        Field(
            None,
        ),
    ]

    unit: Annotated[
        Optional["UnitOfWeight"],
        Field(
            None,
        ),
    ]


"""
Package

This object contains all the details of the scheduled Easy Ship package.
"""


class Package(SpApiBaseModel):
    """This object contains all the details of the scheduled Easy Ship package."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    scheduled_package_id: Annotated[
        "ScheduledPackageId",
        Field(
            ...,
            validation_alias=AliasChoices("scheduledPackageId", "scheduled_package_id"),
            serialization_alias="scheduledPackageId",
        ),
    ]

    package_dimensions: Annotated[
        "Dimensions",
        Field(
            ...,
            validation_alias=AliasChoices("packageDimensions", "package_dimensions"),
            serialization_alias="packageDimensions",
        ),
    ]

    package_weight: Annotated[
        "Weight",
        Field(
            ...,
            validation_alias=AliasChoices("packageWeight", "package_weight"),
            serialization_alias="packageWeight",
        ),
    ]

    package_items: Annotated[
        Optional["Items"],
        Field(
            None,
            validation_alias=AliasChoices("packageItems", "package_items"),
            serialization_alias="packageItems",
        ),
    ]

    package_time_slot: Annotated[
        "TimeSlot",
        Field(
            ...,
            validation_alias=AliasChoices("packageTimeSlot", "package_time_slot"),
            serialization_alias="packageTimeSlot",
        ),
    ]

    package_identifier: Annotated[
        Optional["PackageIdentifier"],
        Field(
            None,
            validation_alias=AliasChoices("packageIdentifier", "package_identifier"),
            serialization_alias="packageIdentifier",
        ),
    ]

    invoice: Annotated[
        Optional["InvoiceData"],
        Field(
            None,
        ),
    ]

    package_status: Annotated[
        Optional["PackageStatus"],
        Field(
            None,
            validation_alias=AliasChoices("packageStatus", "package_status"),
            serialization_alias="packageStatus",
        ),
    ]

    tracking_details: Annotated[
        Optional["TrackingDetails"],
        Field(
            None,
            validation_alias=AliasChoices("trackingDetails", "tracking_details"),
            serialization_alias="trackingDetails",
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
RejectedOrder

A order which we couldn't schedule on your behalf. It contains its id, and information on the error.
"""


class RejectedOrder(SpApiBaseModel):
    """A order which we couldn't schedule on your behalf. It contains its id, and information on the error."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        "AmazonOrderId",
        Field(
            ...,
            validation_alias=AliasChoices("amazonOrderId", "amazon_order_id"),
            serialization_alias="amazonOrderId",
        ),
    ]

    error: Annotated[
        Optional["Error"],
        Field(
            None,
        ),
    ]


URL = str
"""A pre-signed URL for the zip document containing the shipping labels and the documents enabled for your marketplace."""


"""
CreateScheduledPackagesResponse

The response schema for the bulk scheduling API. It returns by the bulk scheduling API containing an array of the scheduled packtages, an optional list of orders we couldn't schedule with the reason, and a pre-signed URL for a ZIP file containing the associated shipping labels plus the documents enabled for your marketplace.
"""


class CreateScheduledPackagesResponse(SpApiBaseModel):
    """The response schema for the bulk scheduling API. It returns by the bulk scheduling API containing an array of the scheduled packtages, an optional list of orders we couldn't schedule with the reason, and a pre-signed URL for a ZIP file containing the associated shipping labels plus the documents enabled for your marketplace."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    scheduled_packages: Annotated[
        Optional[List["Package"]],
        Field(
            None,
            validation_alias=AliasChoices("scheduledPackages", "scheduled_packages"),
            serialization_alias="scheduledPackages",
            description="A list of packages. Refer to the `Package` object.",
        ),
    ]

    rejected_orders: Annotated[
        Optional[List["RejectedOrder"]],
        Field(
            None,
            validation_alias=AliasChoices("rejectedOrders", "rejected_orders"),
            serialization_alias="rejectedOrders",
            description="A list of orders we couldn't scheduled on your behalf. Each element contains the reason and details on the error.",
        ),
    ]

    printable_documents_url: Annotated[
        Optional["URL"],
        Field(
            None,
            validation_alias=AliasChoices(
                "printableDocumentsUrl", "printable_documents_url"
            ),
            serialization_alias="printableDocumentsUrl",
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
            description="A list of error responses returned when a request is unsuccessful.",
        ),
    ]


"""
GetScheduledPackageRequest

Request parameters for getScheduledPackage
"""


class GetScheduledPackageRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getScheduledPackage
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("amazonOrderId", "amazon_order_id"),
            serialization_alias="amazonOrderId",
            description="[QUERY] An Amazon-defined order identifier. Identifies the order that the seller wants to deliver using Amazon Easy Ship.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] An identifier for the marketplace in which the seller is selling.",
        ),
    ]


OrderItemId = str
"""The Amazon-defined order item identifier."""


OrderItemSerialNumbers = List["OrderItemSerialNumber"]
"""A list of serial numbers for the items associated with the `OrderItemId` value."""


"""
Item

Item identifier and serial number information.
"""


class Item(SpApiBaseModel):
    """Item identifier and serial number information."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    order_item_id: Annotated[
        Optional["OrderItemId"],
        Field(
            None,
            validation_alias=AliasChoices("orderItemId", "order_item_id"),
            serialization_alias="orderItemId",
        ),
    ]

    order_item_serial_numbers: Annotated[
        Optional["OrderItemSerialNumbers"],
        Field(
            None,
            validation_alias=AliasChoices(
                "orderItemSerialNumbers", "order_item_serial_numbers"
            ),
            serialization_alias="orderItemSerialNumbers",
        ),
    ]


"""
ListHandoverSlotsRequestBody

The request schema for the `listHandoverSlots` operation.
"""


class ListHandoverSlotsRequestBody(SpApiBaseModel):
    """The request schema for the `listHandoverSlots` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional["String"],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
        ),
    ]

    amazon_order_id: Annotated[
        "AmazonOrderId",
        Field(
            ...,
            validation_alias=AliasChoices("amazonOrderId", "amazon_order_id"),
            serialization_alias="amazonOrderId",
        ),
    ]

    package_dimensions: Annotated[
        "Dimensions",
        Field(
            ...,
            validation_alias=AliasChoices("packageDimensions", "package_dimensions"),
            serialization_alias="packageDimensions",
        ),
    ]

    package_weight: Annotated[
        "Weight",
        Field(
            ...,
            validation_alias=AliasChoices("packageWeight", "package_weight"),
            serialization_alias="packageWeight",
        ),
    ]


"""
ListHandoverSlotsRequest

Request parameters for listHandoverSlots
"""


class ListHandoverSlotsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listHandoverSlots
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    list_handover_slots_request_body: Annotated[
        Optional["ListHandoverSlotsRequestBody"],
        BodyParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "ListHandoverSlotsRequestBody", "list_handover_slots_request_body"
            ),
            serialization_alias="ListHandoverSlotsRequestBody",
            description="[BODY] The request schema for the `listHandoverSlots` operation.",
        ),
    ]


TimeSlots = List["TimeSlot"]
"""A list of time slots."""


"""
ListHandoverSlotsResponse

The response schema for the `listHandoverSlots` operation.
"""


class ListHandoverSlotsResponse(SpApiBaseModel):
    """The response schema for the `listHandoverSlots` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        "AmazonOrderId",
        Field(
            ...,
            validation_alias=AliasChoices("amazonOrderId", "amazon_order_id"),
            serialization_alias="amazonOrderId",
        ),
    ]

    time_slots: Annotated[
        "TimeSlots",
        Field(
            ...,
            validation_alias=AliasChoices("timeSlots", "time_slots"),
            serialization_alias="timeSlots",
        ),
    ]


OrderItemSerialNumber = str
"""A serial number for an item associated with the `OrderItemId` value."""


"""
Packages

A list of packages.
"""


class Packages(SpApiBaseModel):
    """A list of packages."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    packages: Annotated[List["Package"], Field(..., description="A list of packages.")]


"""
UpdatePackageDetails

RequestBody to update the time slot of a package.
"""


class UpdatePackageDetails(SpApiBaseModel):
    """RequestBody to update the time slot of a package."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    scheduled_package_id: Annotated[
        "ScheduledPackageId",
        Field(
            ...,
            validation_alias=AliasChoices("scheduledPackageId", "scheduled_package_id"),
            serialization_alias="scheduledPackageId",
        ),
    ]

    package_time_slot: Annotated[
        "TimeSlot",
        Field(
            ...,
            validation_alias=AliasChoices("packageTimeSlot", "package_time_slot"),
            serialization_alias="packageTimeSlot",
        ),
    ]


UpdatePackageDetailsList = List["UpdatePackageDetails"]
"""A list of package update details."""


"""
UpdateScheduledPackagesRequestBody

The request schema for the `updateScheduledPackages` operation.
"""


class UpdateScheduledPackagesRequestBody(SpApiBaseModel):
    """The request schema for the `updateScheduledPackages` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional["String"],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
        ),
    ]

    update_package_details_list: Annotated[
        "UpdatePackageDetailsList",
        Field(
            ...,
            validation_alias=AliasChoices(
                "updatePackageDetailsList", "update_package_details_list"
            ),
            serialization_alias="updatePackageDetailsList",
        ),
    ]


"""
UpdateScheduledPackagesRequest

Request parameters for updateScheduledPackages
"""


class UpdateScheduledPackagesRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for updateScheduledPackages
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    update_scheduled_packages_request_body: Annotated[
        Optional["UpdateScheduledPackagesRequestBody"],
        BodyParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "UpdateScheduledPackagesRequestBody",
                "update_scheduled_packages_request_body",
            ),
            serialization_alias="UpdateScheduledPackagesRequestBody",
            description="[BODY] The request schema for the `updateScheduledPackages` operation.",
        ),
    ]


# Rebuild models to resolve forward references
TrackingDetails.model_rebuild()
OrderScheduleDetails.model_rebuild()
Dimensions.model_rebuild()
ListHandoverSlotsRequestBody.model_rebuild()
ListHandoverSlotsResponse.model_rebuild()
InvoiceData.model_rebuild()
Item.model_rebuild()
Package.model_rebuild()
Packages.model_rebuild()
PackageDetails.model_rebuild()
RejectedOrder.model_rebuild()
TimeSlot.model_rebuild()
ScheduledPackageId.model_rebuild()
CreateScheduledPackageRequestBody.model_rebuild()
UpdateScheduledPackagesRequestBody.model_rebuild()
UpdatePackageDetails.model_rebuild()
CreateScheduledPackagesRequestBody.model_rebuild()
CreateScheduledPackagesResponse.model_rebuild()
Weight.model_rebuild()
ErrorList.model_rebuild()
Error.model_rebuild()
ListHandoverSlotsRequest.model_rebuild()
GetScheduledPackageRequest.model_rebuild()
CreateScheduledPackageRequest.model_rebuild()
UpdateScheduledPackagesRequest.model_rebuild()
CreateScheduledPackageBulkRequest.model_rebuild()
