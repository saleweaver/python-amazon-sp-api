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
AppointmentTimeInput

The input appointment time details.
"""


class AppointmentTimeInput(SpApiBaseModel):
    """The input appointment time details."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    start_time: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("startTime", "start_time"),
            serialization_alias="startTime",
            description="The date, time in UTC for the start time of an appointment in ISO 8601 format.",
        ),
    ]

    duration_in_minutes: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("durationInMinutes", "duration_in_minutes"),
            serialization_alias="durationInMinutes",
            description="The duration of an appointment in minutes.",
        ),
    ]


"""
AddAppointmentRequestBody

Input for add appointment operation.
"""


class AddAppointmentRequestBody(SpApiBaseModel):
    """Input for add appointment operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    appointment_time: Annotated[
        "AppointmentTimeInput",
        Field(
            ...,
            validation_alias=AliasChoices("appointmentTime", "appointment_time"),
            serialization_alias="appointmentTime",
            description="Input appointment time details.",
        ),
    ]


"""
AddAppointmentForServiceJobByServiceJobIdRequest

Request parameters for addAppointmentForServiceJobByServiceJobId
"""


class AddAppointmentForServiceJobByServiceJobIdRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for addAppointmentForServiceJobByServiceJobId
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    service_job_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("serviceJobId", "service_job_id"),
            serialization_alias="serviceJobId",
            description="[PATH] An Amazon defined service job identifier.",
        ),
    ]

    body: Annotated[
        "AddAppointmentRequestBody",
        BodyParam(),
        Field(..., description="[BODY] Add appointment operation input details."),
    ]


"""
Address

The shipping address for the service job.
"""


class Address(SpApiBaseModel):
    """The shipping address for the service job."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[
        str, Field(..., description="The name of the person, business, or institution.")
    ]

    address_line1: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("addressLine1", "address_line1"),
            serialization_alias="addressLine1",
            description="The first line of the address.",
        ),
    ]

    address_line2: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("addressLine2", "address_line2"),
            serialization_alias="addressLine2",
            description="Additional address information, if required.",
        ),
    ]

    address_line3: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("addressLine3", "address_line3"),
            serialization_alias="addressLine3",
            description="Additional address information, if required.",
        ),
    ]

    city: Annotated[Optional[str], Field(None, description="The city.")]

    county: Annotated[Optional[str], Field(None, description="The county.")]

    district: Annotated[Optional[str], Field(None, description="The district.")]

    state_or_region: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("stateOrRegion", "state_or_region"),
            serialization_alias="stateOrRegion",
            description="The state or region.",
        ),
    ]

    postal_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("postalCode", "postal_code"),
            serialization_alias="postalCode",
            description="The postal code. This can contain letters, digits, spaces, and/or punctuation.",
        ),
    ]

    country_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
            description="The two digit country code, in ISO 3166-1 alpha-2 format.",
        ),
    ]

    phone: Annotated[Optional[str], Field(None, description="The phone number.")]


AppointmentId = str
"""The appointment identifier."""


"""
AppointmentTime

The time of the appointment window.
"""


class AppointmentTime(SpApiBaseModel):
    """The time of the appointment window."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    start_time: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("startTime", "start_time"),
            serialization_alias="startTime",
            description="The date and time of the start of the appointment window in ISO 8601 format.",
        ),
    ]

    duration_in_minutes: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("durationInMinutes", "duration_in_minutes"),
            serialization_alias="durationInMinutes",
            description="The duration of the appointment window, in minutes.",
        ),
    ]


"""
Technician

A technician who is assigned to perform the service job in part or in full.
"""


class Technician(SpApiBaseModel):
    """A technician who is assigned to perform the service job in part or in full."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    technician_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("technicianId", "technician_id"),
            serialization_alias="technicianId",
            description="The technician identifier.",
        ),
    ]

    name: Annotated[
        Optional[str], Field(None, description="The name of the technician.")
    ]


# Enum definitions
class PoaTypeEnum(str, Enum):
    """Enum for poaType"""

    NO_SIGNATURE_DUMMY_POS = "NO_SIGNATURE_DUMMY_POS"  # Indicates that the type of proof of appointment uploaded is a dummy signature.
    CUSTOMER_SIGNATURE = "CUSTOMER_SIGNATURE"  # Indicates that the type of proof of appointment uploaded is a customer signature.
    DUMMY_RECEIPT = "DUMMY_RECEIPT"  # Indicates that the type of proof of appointment uploaded is a dummy receipt.
    POA_RECEIPT = (
        "POA_RECEIPT"  # Indicates that the type of proof of appointment is a receipt.
    )


"""
Poa

Proof of Appointment (POA) details.
"""


class Poa(SpApiBaseModel):
    """Proof of Appointment (POA) details."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    appointment_time: Annotated[
        Optional["AppointmentTime"],
        Field(
            None,
            validation_alias=AliasChoices("appointmentTime", "appointment_time"),
            serialization_alias="appointmentTime",
            description="The time of the appointment window.",
        ),
    ]

    technicians: Annotated[
        Optional[List["Technician"]], Field(None, description="A list of technicians.")
    ]

    uploading_technician: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "uploadingTechnician", "uploading_technician"
            ),
            serialization_alias="uploadingTechnician",
            description="The identifier of the technician who uploaded the POA.",
        ),
    ]

    upload_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("uploadTime", "upload_time"),
            serialization_alias="uploadTime",
            description="The date and time when the POA was uploaded in ISO 8601 format.",
        ),
    ]

    poa_type: Annotated[
        Optional[PoaTypeEnum],
        Field(
            None,
            validation_alias=AliasChoices("poaType", "poa_type"),
            serialization_alias="poaType",
            description="The type of POA uploaded.",
        ),
    ]


# Enum definitions
class AppointmentStatusEnum(str, Enum):
    """Enum for appointmentStatus"""

    ACTIVE = "ACTIVE"  # Indicates that an appointment is scheduled.
    CANCELLED = "CANCELLED"  # Indicates that the appointment is cancelled.
    COMPLETED = "COMPLETED"  # Indicates that the appointment is completed.


"""
Appointment

The details of an appointment.
"""


class Appointment(SpApiBaseModel):
    """The details of an appointment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    appointment_id: Annotated[
        Optional["AppointmentId"],
        Field(
            None,
            validation_alias=AliasChoices("appointmentId", "appointment_id"),
            serialization_alias="appointmentId",
            description="The appointment identifier.",
        ),
    ]

    appointment_status: Annotated[
        Optional[AppointmentStatusEnum],
        Field(
            None,
            validation_alias=AliasChoices("appointmentStatus", "appointment_status"),
            serialization_alias="appointmentStatus",
            description="The status of the appointment.",
        ),
    ]

    appointment_time: Annotated[
        Optional["AppointmentTime"],
        Field(
            None,
            validation_alias=AliasChoices("appointmentTime", "appointment_time"),
            serialization_alias="appointmentTime",
            description="The time of the appointment window.",
        ),
    ]

    assigned_technicians: Annotated[
        Optional[List["Technician"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "assignedTechnicians", "assigned_technicians"
            ),
            serialization_alias="assignedTechnicians",
            description="A list of technicians assigned to the service job.",
        ),
    ]

    rescheduled_appointment_id: Annotated[
        Optional["AppointmentId"],
        Field(
            None,
            validation_alias=AliasChoices(
                "rescheduledAppointmentId", "rescheduled_appointment_id"
            ),
            serialization_alias="rescheduledAppointmentId",
            description="The identifier of a rescheduled appointment.",
        ),
    ]

    poa: Annotated[
        Optional["Poa"], Field(None, description="Proof of Appointment (POA) details.")
    ]


"""
AppointmentResource

The resource that performs or performed appointment fulfillment.
"""


class AppointmentResource(SpApiBaseModel):
    """The resource that performs or performed appointment fulfillment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    resource_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("resourceId", "resource_id"),
            serialization_alias="resourceId",
            description="The resource identifier.",
        ),
    ]


AppointmentResources = List["AppointmentResource"]
"""List of resources that performs or performed job appointment fulfillment."""


"""
AppointmentSlot

A time window along with associated capacity in which the service can be performed.
"""


class AppointmentSlot(SpApiBaseModel):
    """A time window along with associated capacity in which the service can be performed."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    start_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("startTime", "start_time"),
            serialization_alias="startTime",
            description="Time window start time in ISO 8601 format.",
        ),
    ]

    end_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("endTime", "end_time"),
            serialization_alias="endTime",
            description="Time window end time in ISO 8601 format.",
        ),
    ]

    capacity: Annotated[
        Optional[int],
        Field(
            None, description="Number of resources for which a slot can be reserved."
        ),
    ]


# Enum definitions
class SchedulingTypeEnum(str, Enum):
    """Enum for schedulingType"""

    REAL_TIME_SCHEDULING = "REAL_TIME_SCHEDULING"  # The slots provided are backed by inventory in inventory management system.
    NON_REAL_TIME_SCHEDULING = "NON_REAL_TIME_SCHEDULING"  # The slots provided are based on working hours defined in seller management system.


"""
AppointmentSlotReport

Availability information as per the service context queried.
"""


class AppointmentSlotReport(SpApiBaseModel):
    """Availability information as per the service context queried."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    scheduling_type: Annotated[
        Optional[SchedulingTypeEnum],
        Field(
            None,
            validation_alias=AliasChoices("schedulingType", "scheduling_type"),
            serialization_alias="schedulingType",
            description="Defines the type of slots.",
        ),
    ]

    start_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("startTime", "start_time"),
            serialization_alias="startTime",
            description="Start Time from which the appointment slots are generated in ISO 8601 format.",
        ),
    ]

    end_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("endTime", "end_time"),
            serialization_alias="endTime",
            description="End Time up to which the appointment slots are generated in ISO 8601 format.",
        ),
    ]

    appointment_slots: Annotated[
        Optional[List["AppointmentSlot"]],
        Field(
            None,
            validation_alias=AliasChoices("appointmentSlots", "appointment_slots"),
            serialization_alias="appointmentSlots",
            description="A list of time windows along with associated capacity in which the service can be performed.",
        ),
    ]


"""
AssignAppointmentResourcesRequestBody

RequestBody schema for the `assignAppointmentResources` operation.
"""


class AssignAppointmentResourcesRequestBody(SpApiBaseModel):
    """RequestBody schema for the `assignAppointmentResources` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    resources: Annotated[
        "AppointmentResources",
        Field(..., description="List of resource objects to be assigned."),
    ]


"""
AssignAppointmentResourcesRequest

Request parameters for assignAppointmentResources
"""


class AssignAppointmentResourcesRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for assignAppointmentResources
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    service_job_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("serviceJobId", "service_job_id"),
            serialization_alias="serviceJobId",
            description="[PATH] An Amazon-defined service job identifier. Get this value by calling the `getServiceJobs` operation of the Services API.",
        ),
    ]

    appointment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("appointmentId", "appointment_id"),
            serialization_alias="appointmentId",
            description="[PATH] An Amazon-defined identifier of active service job appointment.",
        ),
    ]

    body: Annotated[
        "AssignAppointmentResourcesRequestBody",
        BodyParam(),
        Field(..., description="[BODY] Parameter"),
    ]


ErrorList = List["Error"]
"""A list of error responses returned when a request is unsuccessful."""


"""
AssignAppointmentResourcesResponse

Response schema for the `assignAppointmentResources` operation.
"""


class AssignAppointmentResourcesResponse(SpApiBaseModel):
    """Response schema for the `assignAppointmentResources` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            description="The payload for the `assignAppointmentResource` operation.",
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="Errors occurred during during the `assignAppointmentResources` operation.",
        ),
    ]


"""
ItemDeliveryPromise

Promised delivery information for the item.
"""


class ItemDeliveryPromise(SpApiBaseModel):
    """Promised delivery information for the item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    start_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("startTime", "start_time"),
            serialization_alias="startTime",
            description="The date and time of the start of the promised delivery window in ISO 8601 format.",
        ),
    ]

    end_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("endTime", "end_time"),
            serialization_alias="endTime",
            description="The date and time of the end of the promised delivery window in ISO 8601 format.",
        ),
    ]


"""
ItemDelivery

Delivery information for the item.
"""


class ItemDelivery(SpApiBaseModel):
    """Delivery information for the item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    estimated_delivery_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "estimatedDeliveryDate", "estimated_delivery_date"
            ),
            serialization_alias="estimatedDeliveryDate",
            description="The date and time of the latest Estimated Delivery Date (EDD) of all the items with an EDD. In ISO 8601 format.",
        ),
    ]

    item_delivery_promise: Annotated[
        Optional["ItemDeliveryPromise"],
        Field(
            None,
            validation_alias=AliasChoices(
                "itemDeliveryPromise", "item_delivery_promise"
            ),
            serialization_alias="itemDeliveryPromise",
            description="Promised delivery information for the item.",
        ),
    ]


OrderId = str
"""The Amazon-defined identifier for an order placed by the buyer, in 3-7-7 format."""


# Enum definitions
class ItemStatusEnum(str, Enum):
    """Enum for itemStatus"""

    ACTIVE = "ACTIVE"  # Indicates the item is yet to be shipped.
    CANCELLED = "CANCELLED"  # Indicates the item has been cancelled.
    SHIPPED = "SHIPPED"  # Indicates the item is shipped but not delivered.
    DELIVERED = "DELIVERED"  # Indicates the item is delivered.


"""
AssociatedItem

Information about an item associated with the service job.
"""


class AssociatedItem(SpApiBaseModel):
    """Information about an item associated with the service job."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    asin: Annotated[
        Optional[str],
        Field(
            None,
            description="The Amazon Standard Identification Number (ASIN) of the item.",
        ),
    ]

    title: Annotated[Optional[str], Field(None, description="The title of the item.")]

    quantity: Annotated[
        Optional[int],
        Field(None, description="The total number of items included in the order."),
    ]

    order_id: Annotated[
        Optional["OrderId"],
        Field(
            None,
            validation_alias=AliasChoices("orderId", "order_id"),
            serialization_alias="orderId",
            description="The Amazon-defined identifier for an order placed by the buyer in 3-7-7 format.",
        ),
    ]

    item_status: Annotated[
        Optional[ItemStatusEnum],
        Field(
            None,
            validation_alias=AliasChoices("itemStatus", "item_status"),
            serialization_alias="itemStatus",
            description="The status of the item.",
        ),
    ]

    brand_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("brandName", "brand_name"),
            serialization_alias="brandName",
            description="The brand name of the item.",
        ),
    ]

    item_delivery: Annotated[
        Optional["ItemDelivery"],
        Field(
            None,
            validation_alias=AliasChoices("itemDelivery", "item_delivery"),
            serialization_alias="itemDelivery",
            description="Delivery information for the item.",
        ),
    ]


DayOfWeek = str
"""The day of the week."""


"""
Recurrence

Repeated occurrence of an event in a time range.
"""


class Recurrence(SpApiBaseModel):
    """Repeated occurrence of an event in a time range."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    end_time: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("endTime", "end_time"),
            serialization_alias="endTime",
            description="End time of the recurrence.",
        ),
    ]

    days_of_week: Annotated[
        Optional[List["DayOfWeek"]],
        Field(
            None,
            validation_alias=AliasChoices("daysOfWeek", "days_of_week"),
            serialization_alias="daysOfWeek",
            description="Days of the week when recurrence is valid. If the schedule is valid every Monday, input will only contain `MONDAY` in the list.",
        ),
    ]

    days_of_month: Annotated[
        Optional[List["int"]],
        Field(
            None,
            validation_alias=AliasChoices("daysOfMonth", "days_of_month"),
            serialization_alias="daysOfMonth",
            description="Days of the month when recurrence is valid.",
        ),
    ]


"""
AvailabilityRecord

`AvailabilityRecord` to represent the capacity of a resource over a time range.
"""


class AvailabilityRecord(SpApiBaseModel):
    """`AvailabilityRecord` to represent the capacity of a resource over a time range."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    start_time: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("startTime", "start_time"),
            serialization_alias="startTime",
            description="Denotes the time from when the resource is available in a day in ISO-8601 format.",
        ),
    ]

    end_time: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("endTime", "end_time"),
            serialization_alias="endTime",
            description="Denotes the time till when the resource is available in a day in ISO-8601 format.",
        ),
    ]

    recurrence: Annotated[
        Optional["Recurrence"],
        Field(
            None,
            description="Recurrence object containing the recurrence pattern of schedule.",
        ),
    ]

    capacity: Annotated[
        Optional[int],
        Field(
            None, description="Signifies the capacity of a resource which is available."
        ),
    ]


AvailabilityRecords = List["AvailabilityRecord"]
"""List of `AvailabilityRecord`s to represent the capacity of a resource over a time range."""


"""
Buyer

Information about the buyer.
"""


class Buyer(SpApiBaseModel):
    """Information about the buyer."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    buyer_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("buyerId", "buyer_id"),
            serialization_alias="buyerId",
            description="The identifier of the buyer.",
        ),
    ]

    name: Annotated[Optional[str], Field(None, description="The name of the buyer.")]

    phone: Annotated[
        Optional[str], Field(None, description="The phone number of the buyer.")
    ]

    is_prime_member: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("isPrimeMember", "is_prime_member"),
            serialization_alias="isPrimeMember",
            description="When true, the service is for an Amazon Prime buyer.",
        ),
    ]


"""
CancelReservationRequest

Request parameters for cancelReservation
"""


class CancelReservationRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for cancelReservation
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    reservation_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("reservationId", "reservation_id"),
            serialization_alias="reservationId",
            description="[PATH] Reservation Identifier",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] An identifier for the marketplace in which the resource operates.",
        ),
    ]


"""
CancelReservationResponse

Response schema for the `cancelReservation` operation.
"""


class CancelReservationResponse(SpApiBaseModel):
    """Response schema for the `cancelReservation` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"], Field(None, description="Errors encountered, if any")
    ]


"""
CancelServiceJobByServiceJobIdRequest

Request parameters for cancelServiceJobByServiceJobId
"""


class CancelServiceJobByServiceJobIdRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for cancelServiceJobByServiceJobId
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    service_job_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("serviceJobId", "service_job_id"),
            serialization_alias="serviceJobId",
            description="[PATH] An Amazon defined service job identifier.",
        ),
    ]

    cancellation_reason_code: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "cancellationReasonCode", "cancellation_reason_code"
            ),
            serialization_alias="cancellationReasonCode",
            description="[QUERY] A cancel reason code that specifies the reason for cancelling a service job.",
        ),
    ]


"""
CancelServiceJobByServiceJobIdResponse

Response schema for the `cancelServiceJobByServiceJobId` operation.
"""


class CancelServiceJobByServiceJobIdResponse(SpApiBaseModel):
    """Response schema for the `cancelServiceJobByServiceJobId` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="Encountered errors for the `cancelServiceJobByServiceJobId` operation.",
        ),
    ]


CapacityType = str
"""Type of capacity"""


"""
CompleteServiceJobByServiceJobIdRequest

Request parameters for completeServiceJobByServiceJobId
"""


class CompleteServiceJobByServiceJobIdRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for completeServiceJobByServiceJobId
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    service_job_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("serviceJobId", "service_job_id"),
            serialization_alias="serviceJobId",
            description="[PATH] An Amazon defined service job identifier.",
        ),
    ]


"""
CompleteServiceJobByServiceJobIdResponse

Response schema for the `completeServiceJobByServiceJobId` operation.
"""


class CompleteServiceJobByServiceJobIdResponse(SpApiBaseModel):
    """Response schema for the `completeServiceJobByServiceJobId` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="Encountered errors for the `completeServiceJobByServiceJobId` operation.",
        ),
    ]


# Enum definitions
class TypeEnum(str, Enum):
    """Enum for type"""

    APPOINTMENT = (
        "APPOINTMENT"  # Reduce resource (store) capacity because of an appointment.
    )
    TRAVEL = "TRAVEL"  # Reduce resource (store) capacity because technician(s) are travelling.
    VACATION = "VACATION"  # Reduce resource (store) capacity because technician(s) are on vacation.
    BREAK = (
        "BREAK"  # Reduce resource (store) capacity because technician(s) are on break.
    )
    TRAINING = "TRAINING"  # Reduce resource (store) capacity because technician(s) are in training.


"""
Reservation

Reservation object reduces the capacity of a resource.
"""


class Reservation(SpApiBaseModel):
    """Reservation object reduces the capacity of a resource."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    reservation_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("reservationId", "reservation_id"),
            serialization_alias="reservationId",
            description="Unique identifier for a reservation. If present, it is treated as an update reservation request and will update the corresponding reservation. Otherwise, it is treated as a new create reservation request.",
        ),
    ]

    type: Annotated[TypeEnum, Field(..., description="Type of reservation.")]

    availability: Annotated[
        "AvailabilityRecord",
        Field(
            ...,
            description="`AvailabilityRecord` to represent the capacity of a resource over a time range.",
        ),
    ]


WarningList = List["Warning"]
"""A list of warnings returned in the sucessful execution response of an API request."""


"""
CreateReservationRecord

`CreateReservationRecord` entity contains the `Reservation` if there is an error/warning while performing the requested operation on it, otherwise it will contain the new `reservationId`.
"""


class CreateReservationRecord(SpApiBaseModel):
    """`CreateReservationRecord` entity contains the `Reservation` if there is an error/warning while performing the requested operation on it, otherwise it will contain the new `reservationId`."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    reservation: Annotated[
        Optional["Reservation"],
        Field(
            None,
            description="Reservation record if the operation failed. It will only contain the new `reservationId` if the operation is successful.",
        ),
    ]

    warnings: Annotated[
        Optional["WarningList"],
        Field(None, description="Warnings encountered, if any."),
    ]

    errors: Annotated[
        Optional["ErrorList"], Field(None, description="Errors encountered, if any.")
    ]


"""
CreateReservationRequestBody

RequestBody schema for the `createReservation` operation.
"""


class CreateReservationRequestBody(SpApiBaseModel):
    """RequestBody schema for the `createReservation` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    resource_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("resourceId", "resource_id"),
            serialization_alias="resourceId",
            description="Resource (store) identifier.",
        ),
    ]

    reservation: Annotated[
        "Reservation",
        Field(
            ...,
            description="`Reservation` object to reduce the capacity of a resource.",
        ),
    ]


"""
CreateReservationRequest

Request parameters for createReservation
"""


class CreateReservationRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createReservation
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "CreateReservationRequestBody",
        BodyParam(),
        Field(..., description="[BODY] Reservation details"),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] An identifier for the marketplace in which the resource operates.",
        ),
    ]


"""
CreateReservationResponse

Response schema for the `createReservation` operation.
"""


class CreateReservationResponse(SpApiBaseModel):
    """Response schema for the `createReservation` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["CreateReservationRecord"],
        Field(
            None,
            description="`CreateReservationRecord` contains only the new `reservationId` if the operation was successful. Otherwise it will contain the reservation entity with warnings/errors.",
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"], Field(None, description="Errors encountered, if any.")
    ]


# Enum definitions
class StandardEnum(str, Enum):
    """Enum for standard"""

    AES = "AES"  # The Advanced Encryption Standard (AES).


"""
EncryptionDetails

Encryption details for required client-side encryption and decryption of document contents.
"""


class EncryptionDetails(SpApiBaseModel):
    """Encryption details for required client-side encryption and decryption of document contents."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    standard: Annotated[
        StandardEnum,
        Field(
            ...,
            description="The encryption standard required to encrypt or decrypt the document contents.",
        ),
    ]

    initialization_vector: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "initializationVector", "initialization_vector"
            ),
            serialization_alias="initializationVector",
            description="The vector to encrypt or decrypt the document contents using Cipher Block Chaining (CBC).",
        ),
    ]

    key: Annotated[
        str,
        Field(
            ...,
            description="The encryption key used to encrypt or decrypt the document contents.",
        ),
    ]


"""
ServiceDocumentUploadDestination

Information about an upload destination.
"""


class ServiceDocumentUploadDestination(SpApiBaseModel):
    """Information about an upload destination."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    upload_destination_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "uploadDestinationId", "upload_destination_id"
            ),
            serialization_alias="uploadDestinationId",
            description="The unique identifier to be used by APIs that reference the upload destination.",
        ),
    ]

    url: Annotated[str, Field(..., description="The URL to which to upload the file.")]

    encryption_details: Annotated[
        "EncryptionDetails",
        Field(
            ...,
            validation_alias=AliasChoices("encryptionDetails", "encryption_details"),
            serialization_alias="encryptionDetails",
        ),
    ]

    headers: Annotated[
        Optional[Dict[str, Any]],
        Field(None, description="The headers to include in the upload request."),
    ]


"""
CreateServiceDocumentUploadDestination

The response schema for the `createServiceDocumentUploadDestination` operation.
"""


class CreateServiceDocumentUploadDestination(SpApiBaseModel):
    """The response schema for the `createServiceDocumentUploadDestination` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["ServiceDocumentUploadDestination"],
        Field(
            None,
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


# Enum definitions
class ContentTypeEnum(str, Enum):
    """Enum for contentType"""

    TIFF = "TIFF"  # To be uploaded POA is of type image/tiff.
    JPG = "JPG"  # To be uploaded POA is of type image/jpg.
    PNG = "PNG"  # To be uploaded POA is of type image/png.
    JPEG = "JPEG"  # To be uploaded POA is of type image/jpeg.
    GIF = "GIF"  # To be uploaded POA is of type image/gif.
    PDF = "PDF"  # To be uploaded POA is of type application/pdf.


"""
ServiceUploadDocument

Input for to be uploaded document.
"""


class ServiceUploadDocument(SpApiBaseModel):
    """Input for to be uploaded document."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    content_type: Annotated[
        ContentTypeEnum,
        Field(
            ...,
            validation_alias=AliasChoices("contentType", "content_type"),
            serialization_alias="contentType",
            description="The content type of the to-be-uploaded file",
        ),
    ]

    content_length: Annotated[
        float,
        Field(
            ...,
            validation_alias=AliasChoices("contentLength", "content_length"),
            serialization_alias="contentLength",
            description="The content length of the to-be-uploaded file",
        ),
    ]

    content_m_d5: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("contentMD5", "content_m_d5"),
            serialization_alias="contentMD5",
            description="An MD5 hash of the content to be submitted to the upload destination. This value is used to determine if the data has been corrupted or tampered with during transit.",
        ),
    ]


"""
CreateServiceDocumentUploadDestinationRequest

Request parameters for createServiceDocumentUploadDestination
"""


class CreateServiceDocumentUploadDestinationRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createServiceDocumentUploadDestination
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "ServiceUploadDocument",
        BodyParam(),
        Field(..., description="[BODY] Upload document operation input details."),
    ]


"""
DateTimeRange

A range of time.
"""


class DateTimeRange(SpApiBaseModel):
    """A range of time."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    start_time: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("startTime", "start_time"),
            serialization_alias="startTime",
            description="The beginning of the time range. Must be in UTC in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format.",
        ),
    ]

    end_time: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("endTime", "end_time"),
            serialization_alias="endTime",
            description="The end of the time range. Must be in UTC in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format.",
        ),
    ]


# Enum definitions
class ErrorLevelEnum(str, Enum):
    """Enum for errorLevel"""

    ERROR = "ERROR"  # Error
    WARNING = "WARNING"  # Warning


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

    error_level: Annotated[
        Optional[ErrorLevelEnum],
        Field(
            None,
            validation_alias=AliasChoices("errorLevel", "error_level"),
            serialization_alias="errorLevel",
            description="The type of error.",
        ),
    ]


"""
FixedSlot

In this slot format each slot only has the requested capacity types. This slot size is as specified by slot duration.
"""


class FixedSlot(SpApiBaseModel):
    """In this slot format each slot only has the requested capacity types. This slot size is as specified by slot duration."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    start_date_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("startDateTime", "start_date_time"),
            serialization_alias="startDateTime",
            description="Start date time of slot in ISO 8601 format with precision of seconds.",
        ),
    ]

    scheduled_capacity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("scheduledCapacity", "scheduled_capacity"),
            serialization_alias="scheduledCapacity",
            description="Scheduled capacity corresponding to the slot. This capacity represents the originally allocated capacity as per resource schedule.",
        ),
    ]

    available_capacity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("availableCapacity", "available_capacity"),
            serialization_alias="availableCapacity",
            description="Available capacity corresponding to the slot. This capacity represents the capacity available for allocation to reservations.",
        ),
    ]

    encumbered_capacity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("encumberedCapacity", "encumbered_capacity"),
            serialization_alias="encumberedCapacity",
            description="Encumbered capacity corresponding to the slot. This capacity represents the capacity allocated for Amazon Jobs/Appointments/Orders.",
        ),
    ]

    reserved_capacity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("reservedCapacity", "reserved_capacity"),
            serialization_alias="reservedCapacity",
            description="Reserved capacity corresponding to the slot. This capacity represents the capacity made unavailable due to events like Breaks/Leaves/Lunch.",
        ),
    ]


"""
FixedSlotCapacity

Response schema for the `getFixedSlotCapacity` operation.
"""


class FixedSlotCapacity(SpApiBaseModel):
    """Response schema for the `getFixedSlotCapacity` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    resource_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("resourceId", "resource_id"),
            serialization_alias="resourceId",
            description="Resource Identifier.",
        ),
    ]

    slot_duration: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices("slotDuration", "slot_duration"),
            serialization_alias="slotDuration",
            description="The duration of each slot which is returned. This value will be a multiple of 5 and fall in the following range: 5 <= `slotDuration` <= 360.",
        ),
    ]

    capacities: Annotated[
        Optional[List["FixedSlot"]],
        Field(None, description="Array of capacity slots in fixed slot format."),
    ]

    next_page_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nextPageToken", "next_page_token"),
            serialization_alias="nextPageToken",
            description="Next page token, if there are more pages.",
        ),
    ]


"""
FixedSlotCapacityErrors

The error response schema for the `getFixedSlotCapacity` operation.
"""


class FixedSlotCapacityErrors(SpApiBaseModel):
    """The error response schema for the `getFixedSlotCapacity` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="Errors encountered during the `getFixedSlotCapacity` operation.",
        ),
    ]


"""
FixedSlotCapacityQuery

RequestBody schema for the `getFixedSlotCapacity` operation. This schema is used to define the time range, capacity types and slot duration which are being queried.
"""


class FixedSlotCapacityQuery(SpApiBaseModel):
    """RequestBody schema for the `getFixedSlotCapacity` operation. This schema is used to define the time range, capacity types and slot duration which are being queried."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    capacity_types: Annotated[
        Optional[List["CapacityType"]],
        Field(
            None,
            validation_alias=AliasChoices("capacityTypes", "capacity_types"),
            serialization_alias="capacityTypes",
            description="An array of capacity types which are being requested. Default value is `[SCHEDULED_CAPACITY]`.",
        ),
    ]

    slot_duration: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices("slotDuration", "slot_duration"),
            serialization_alias="slotDuration",
            description="Size in which slots are being requested. This value should be a multiple of 5 and fall in the range: 5 <= `slotDuration` <= 360.",
        ),
    ]

    start_date_time: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("startDateTime", "start_date_time"),
            serialization_alias="startDateTime",
            description="Start date time from which the capacity slots are being requested in ISO 8601 format.",
        ),
    ]

    end_date_time: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("endDateTime", "end_date_time"),
            serialization_alias="endDateTime",
            description="End date time up to which the capacity slots are being requested in ISO 8601 format.",
        ),
    ]


"""
FulfillmentDocument

Document that captured during service appointment fulfillment that portrays proof of completion
"""


class FulfillmentDocument(SpApiBaseModel):
    """Document that captured during service appointment fulfillment that portrays proof of completion"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    upload_destination_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "uploadDestinationId", "upload_destination_id"
            ),
            serialization_alias="uploadDestinationId",
            description="The identifier of the upload destination. Get this value by calling the `createServiceDocumentUploadDestination` operation of the Services API.",
        ),
    ]

    content_sha256: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("contentSha256", "content_sha256"),
            serialization_alias="contentSha256",
            description="Sha256 hash of the file content. This value is used to determine if the file has been corrupted or tampered with during transit.",
        ),
    ]


FulfillmentDocuments = List["FulfillmentDocument"]
"""List of documents captured during service appointment fulfillment."""


"""
FulfillmentTime

Input for fulfillment time details
"""


class FulfillmentTime(SpApiBaseModel):
    """Input for fulfillment time details"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    start_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("startTime", "start_time"),
            serialization_alias="startTime",
            description="The date, time in UTC of the fulfillment start time in ISO 8601 format.",
        ),
    ]

    end_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("endTime", "end_time"),
            serialization_alias="endTime",
            description="The date, time in UTC of the fulfillment end time in ISO 8601 format.",
        ),
    ]


"""
GetAppointmentSlotsRequest

Request parameters for getAppointmentSlots
"""


class GetAppointmentSlotsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getAppointmentSlots
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    asin: Annotated[
        str,
        QueryParam(),
        Field(..., description="[QUERY] ASIN associated with the service."),
    ]

    store_id: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("storeId", "store_id"),
            serialization_alias="storeId",
            description="[QUERY] Store identifier defining the region scope to retrive appointment slots.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] An identifier for the marketplace for which appointment slots are queried",
        ),
    ]

    start_time: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("startTime", "start_time"),
            serialization_alias="startTime",
            description="[QUERY] A time from which the appointment slots will be retrieved. The specified time must be in ISO 8601 format. If `startTime` is provided, `endTime` should also be provided. Default value is as per business configuration.",
        ),
    ]

    end_time: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("endTime", "end_time"),
            serialization_alias="endTime",
            description="[QUERY] A time up to which the appointment slots will be retrieved. The specified time must be in ISO 8601 format. If `endTime` is provided, `startTime` should also be provided. Default value is as per business configuration. Maximum range of appointment slots can be 90 days.",
        ),
    ]


"""
GetAppointmentSlotsResponse

The response of fetching appointment slots based on service context.
"""


class GetAppointmentSlotsResponse(SpApiBaseModel):
    """The response of fetching appointment slots based on service context."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["AppointmentSlotReport"],
        Field(
            None, description="The appointment slots fetched based on service context."
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(None, description="Errors occurred in getting schedule."),
    ]


"""
GetAppointmmentSlotsByJobIdRequest

Request parameters for getAppointmmentSlotsByJobId
"""


class GetAppointmmentSlotsByJobIdRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getAppointmmentSlotsByJobId
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    service_job_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("serviceJobId", "service_job_id"),
            serialization_alias="serviceJobId",
            description="[PATH] A service job identifier to retrive appointment slots for associated service.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] An identifier for the marketplace in which the resource operates.",
        ),
    ]

    start_time: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("startTime", "start_time"),
            serialization_alias="startTime",
            description="[QUERY] A time from which the appointment slots will be retrieved. The specified time must be in ISO 8601 format. If `startTime` is provided, `endTime` should also be provided. Default value is as per business configuration.",
        ),
    ]

    end_time: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("endTime", "end_time"),
            serialization_alias="endTime",
            description="[QUERY] A time up to which the appointment slots will be retrieved. The specified time must be in ISO 8601 format. If `endTime` is provided, `startTime` should also be provided. Default value is as per business configuration. Maximum range of appointment slots can be 90 days.",
        ),
    ]


"""
GetFixedSlotCapacityRequest

Request parameters for getFixedSlotCapacity
"""


class GetFixedSlotCapacityRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getFixedSlotCapacity
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    resource_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("resourceId", "resource_id"),
            serialization_alias="resourceId",
            description="[PATH] Resource Identifier.",
        ),
    ]

    body: Annotated[
        "FixedSlotCapacityQuery",
        BodyParam(),
        Field(..., description="[BODY] RequestBody body."),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] An identifier for the marketplace in which the resource operates.",
        ),
    ]

    next_page_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("nextPageToken", "next_page_token"),
            serialization_alias="nextPageToken",
            description="[QUERY] Next page token returned in the response of your previous request.",
        ),
    ]


"""
RangeSlotCapacityQuery

RequestBody schema for the `getRangeSlotCapacity` operation. This schema is used to define the time range and capacity types that are being queried.
"""


class RangeSlotCapacityQuery(SpApiBaseModel):
    """RequestBody schema for the `getRangeSlotCapacity` operation. This schema is used to define the time range and capacity types that are being queried."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    capacity_types: Annotated[
        Optional[List["CapacityType"]],
        Field(
            None,
            validation_alias=AliasChoices("capacityTypes", "capacity_types"),
            serialization_alias="capacityTypes",
            description="An array of capacity types which are being requested. Default value is `[SCHEDULED_CAPACITY]`.",
        ),
    ]

    start_date_time: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("startDateTime", "start_date_time"),
            serialization_alias="startDateTime",
            description="Start date time from which the capacity slots are being requested in ISO 8601 format.",
        ),
    ]

    end_date_time: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("endDateTime", "end_date_time"),
            serialization_alias="endDateTime",
            description="End date time up to which the capacity slots are being requested in ISO 8601 format.",
        ),
    ]


"""
GetRangeSlotCapacityRequest

Request parameters for getRangeSlotCapacity
"""


class GetRangeSlotCapacityRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getRangeSlotCapacity
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    resource_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("resourceId", "resource_id"),
            serialization_alias="resourceId",
            description="[PATH] Resource Identifier.",
        ),
    ]

    body: Annotated[
        "RangeSlotCapacityQuery",
        BodyParam(),
        Field(..., description="[BODY] RequestBody body."),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] An identifier for the marketplace in which the resource operates.",
        ),
    ]

    next_page_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("nextPageToken", "next_page_token"),
            serialization_alias="nextPageToken",
            description="[QUERY] Next page token returned in the response of your previous request.",
        ),
    ]


"""
GetServiceJobByServiceJobIdRequest

Request parameters for getServiceJobByServiceJobId
"""


class GetServiceJobByServiceJobIdRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getServiceJobByServiceJobId
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    service_job_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("serviceJobId", "service_job_id"),
            serialization_alias="serviceJobId",
            description="[PATH] A service job identifier.",
        ),
    ]


"""
ScopeOfWork

The scope of work for the order.
"""


class ScopeOfWork(SpApiBaseModel):
    """The scope of work for the order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    asin: Annotated[
        Optional[str],
        Field(
            None,
            description="The Amazon Standard Identification Number (ASIN) of the service job.",
        ),
    ]

    title: Annotated[
        Optional[str], Field(None, description="The title of the service job.")
    ]

    quantity: Annotated[
        Optional[int], Field(None, description="The number of service jobs.")
    ]

    required_skills: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("requiredSkills", "required_skills"),
            serialization_alias="requiredSkills",
            description="A list of skills required to perform the job.",
        ),
    ]


"""
Seller

Information about the seller of the service job.
"""


class Seller(SpApiBaseModel):
    """Information about the seller of the service job."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("sellerId", "seller_id"),
            serialization_alias="sellerId",
            description="The identifier of the seller of the service job.",
        ),
    ]


ServiceJobId = str
"""Amazon identifier for the service job."""


"""
ServiceJobProvider

Information about the service job provider.
"""


class ServiceJobProvider(SpApiBaseModel):
    """Information about the service job provider."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    service_job_provider_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "serviceJobProviderId", "service_job_provider_id"
            ),
            serialization_alias="serviceJobProviderId",
            description="The identifier of the service job provider.",
        ),
    ]


# Enum definitions
class ServiceLocationTypeEnum(str, Enum):
    """Enum for serviceLocationType"""

    IN_HOME = "IN_HOME"  # Indicates the service for the service job is performed at the customers home address.
    IN_STORE = "IN_STORE"  # Indicates the service for the service job is performed at the service providers store.
    ONLINE = (
        "ONLINE"  # Indicates the service for the service job is performed remotely.
    )


"""
ServiceLocation

Information about the location of the service job.
"""


class ServiceLocation(SpApiBaseModel):
    """Information about the location of the service job."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    service_location_type: Annotated[
        Optional[ServiceLocationTypeEnum],
        Field(
            None,
            validation_alias=AliasChoices(
                "serviceLocationType", "service_location_type"
            ),
            serialization_alias="serviceLocationType",
            description="The location of the service job.",
        ),
    ]

    address: Annotated[
        Optional["Address"],
        Field(None, description="The shipping address for the service job."),
    ]


# Enum definitions
class ServiceJobStatusEnum(str, Enum):
    """Enum for serviceJobStatus"""

    NOT_SERVICED = "NOT_SERVICED"  # Jobs which are not serviced.
    CANCELLED = "CANCELLED"  # Jobs which are cancelled.
    COMPLETED = "COMPLETED"  # Jobs successfully completed.
    PENDING_SCHEDULE = "PENDING_SCHEDULE"  # Jobs which are pending schedule.
    NOT_FULFILLABLE = "NOT_FULFILLABLE"  # Jobs which are not fulfillable.
    HOLD = "HOLD"  # Jobs which are on hold.
    PAYMENT_DECLINED = "PAYMENT_DECLINED"  # Jobs for which payment was declined.


"""
ServiceJob

The job details of a service.
"""


class ServiceJob(SpApiBaseModel):
    """The job details of a service."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    create_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("createTime", "create_time"),
            serialization_alias="createTime",
            description="The date and time of the creation of the job in ISO 8601 format.",
        ),
    ]

    service_job_id: Annotated[
        Optional["ServiceJobId"],
        Field(
            None,
            validation_alias=AliasChoices("serviceJobId", "service_job_id"),
            serialization_alias="serviceJobId",
            description="The service job identifier.",
        ),
    ]

    service_job_status: Annotated[
        Optional[ServiceJobStatusEnum],
        Field(
            None,
            validation_alias=AliasChoices("serviceJobStatus", "service_job_status"),
            serialization_alias="serviceJobStatus",
            description="The status of the service job.",
        ),
    ]

    scope_of_work: Annotated[
        Optional["ScopeOfWork"],
        Field(
            None,
            validation_alias=AliasChoices("scopeOfWork", "scope_of_work"),
            serialization_alias="scopeOfWork",
            description="The scope of work for the order.",
        ),
    ]

    seller: Annotated[
        Optional["Seller"],
        Field(None, description="Information about the seller of the service job."),
    ]

    service_job_provider: Annotated[
        Optional["ServiceJobProvider"],
        Field(
            None,
            validation_alias=AliasChoices("serviceJobProvider", "service_job_provider"),
            serialization_alias="serviceJobProvider",
            description="Information about the service job provider.",
        ),
    ]

    preferred_appointment_times: Annotated[
        Optional[List["AppointmentTime"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "preferredAppointmentTimes", "preferred_appointment_times"
            ),
            serialization_alias="preferredAppointmentTimes",
            description="A list of appointment windows preferred by the buyer. Included only if the buyer selected appointment windows when creating the order.",
        ),
    ]

    appointments: Annotated[
        Optional[List["Appointment"]],
        Field(None, description="A list of appointments."),
    ]

    service_order_id: Annotated[
        Optional["OrderId"],
        Field(
            None,
            validation_alias=AliasChoices("serviceOrderId", "service_order_id"),
            serialization_alias="serviceOrderId",
            description="The Amazon-defined identifier for an order placed by the buyer in 3-7-7 format.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The marketplace identifier.",
        ),
    ]

    store_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("storeId", "store_id"),
            serialization_alias="storeId",
            description="The Amazon-defined identifier for the region scope.",
        ),
    ]

    buyer: Annotated[
        Optional["Buyer"], Field(None, description="Information about the buyer.")
    ]

    associated_items: Annotated[
        Optional[List["AssociatedItem"]],
        Field(
            None,
            validation_alias=AliasChoices("associatedItems", "associated_items"),
            serialization_alias="associatedItems",
            description="A list of items associated with the service job.",
        ),
    ]

    service_location: Annotated[
        Optional["ServiceLocation"],
        Field(
            None,
            validation_alias=AliasChoices("serviceLocation", "service_location"),
            serialization_alias="serviceLocation",
            description="Information about the location of the service job.",
        ),
    ]


"""
GetServiceJobByServiceJobIdResponse

The response schema for the `getServiceJobByServiceJobId` operation.
"""


class GetServiceJobByServiceJobIdResponse(SpApiBaseModel):
    """The response schema for the `getServiceJobByServiceJobId` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["ServiceJob"],
        Field(
            None,
            description="The payload for the `getServiceJobByServiceJobId` operation.",
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="An unexpected condition occurred during the `getServiceJobByServiceJobId` operation.",
        ),
    ]


# Enum definitions
class ServiceJobStatusEnum(str, Enum):
    """Enum for serviceJobStatus"""

    NOT_SERVICED = "NOT_SERVICED"  # Jobs which are not serviced.
    CANCELLED = "CANCELLED"  # Jobs which are cancelled.
    COMPLETED = "COMPLETED"  # Jobs successfully completed.
    PENDING_SCHEDULE = "PENDING_SCHEDULE"  # Jobs which are pending schedule.
    NOT_FULFILLABLE = "NOT_FULFILLABLE"  # Jobs which are not fulfillable.
    HOLD = "HOLD"  # Jobs which are on hold.
    PAYMENT_DECLINED = "PAYMENT_DECLINED"  # Jobs for which payment was declined.


class SortFieldEnum(str, Enum):
    """Enum for sortField"""

    JOB_DATE = "JOB_DATE"  # Sort on job date.
    JOB_STATUS = "JOB_STATUS"  # Sort on job status.


class SortOrderEnum(str, Enum):
    """Enum for sortOrder"""

    ASC = "ASC"  # Sort in ascending order.
    DESC = "DESC"  # Sort in descending order.


"""
GetServiceJobsRequest

Request parameters for getServiceJobs
"""


class GetServiceJobsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getServiceJobs
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    service_order_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("serviceOrderIds", "service_order_ids"),
            serialization_alias="serviceOrderIds",
            description="[QUERY] List of service order ids for the query you want to perform.Max values supported 20.",
        ),
    ]

    service_job_status: Annotated[
        Optional[List["ServiceJobStatusEnum"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("serviceJobStatus", "service_job_status"),
            serialization_alias="serviceJobStatus",
            description="[QUERY] A list of one or more job status by which to filter the list of jobs.",
        ),
    ]

    page_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageToken", "page_token"),
            serialization_alias="pageToken",
            description="[QUERY] String returned in the response of your previous request.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] A non-negative integer that indicates the maximum number of jobs to return in the list, Value must be 1 - 20. Default 20.",
        ),
    ]

    sort_field: Annotated[
        Optional[SortFieldEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("sortField", "sort_field"),
            serialization_alias="sortField",
            description="[QUERY] Sort fields on which you want to sort the output.",
        ),
    ]

    sort_order: Annotated[
        Optional[SortOrderEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("sortOrder", "sort_order"),
            serialization_alias="sortOrder",
            description="[QUERY] Sort order for the query you want to perform.",
        ),
    ]

    created_after: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("createdAfter", "created_after"),
            serialization_alias="createdAfter",
            description="[QUERY] A date used for selecting jobs created at or after a specified time. Must be in ISO 8601 format. Required if `LastUpdatedAfter` is not specified. Specifying both `CreatedAfter` and `LastUpdatedAfter` returns an error.",
        ),
    ]

    created_before: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("createdBefore", "created_before"),
            serialization_alias="createdBefore",
            description="[QUERY] A date used for selecting jobs created at or before a specified time. Must be in ISO 8601 format.",
        ),
    ]

    last_updated_after: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("lastUpdatedAfter", "last_updated_after"),
            serialization_alias="lastUpdatedAfter",
            description="[QUERY] A date used for selecting jobs updated at or after a specified time. Must be in ISO 8601 format. Required if `createdAfter` is not specified. Specifying both `CreatedAfter` and `LastUpdatedAfter` returns an error.",
        ),
    ]

    last_updated_before: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("lastUpdatedBefore", "last_updated_before"),
            serialization_alias="lastUpdatedBefore",
            description="[QUERY] A date used for selecting jobs updated at or before a specified time. Must be in ISO 8601 format.",
        ),
    ]

    schedule_start_date: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("scheduleStartDate", "schedule_start_date"),
            serialization_alias="scheduleStartDate",
            description="[QUERY] A date used for filtering jobs schedules at or after a specified time. Must be in ISO 8601 format. Schedule end date should not be earlier than schedule start date.",
        ),
    ]

    schedule_end_date: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("scheduleEndDate", "schedule_end_date"),
            serialization_alias="scheduleEndDate",
            description="[QUERY] A date used for filtering jobs schedules at or before a specified time. Must be in ISO 8601 format. Schedule end date should not be earlier than schedule start date.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] Used to select jobs that were placed in the specified marketplaces.",
        ),
    ]

    asins: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            description="[QUERY] List of Amazon Standard Identification Numbers (ASIN) of the items. Max values supported is 20.",
        ),
    ]

    required_skills: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("requiredSkills", "required_skills"),
            serialization_alias="requiredSkills",
            description="[QUERY] A defined set of related knowledge, skills, experience, tools, materials, and work processes common to service delivery for a set of products and/or service scenarios. Max values supported is 20.",
        ),
    ]

    store_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("storeIds", "store_ids"),
            serialization_alias="storeIds",
            description="[QUERY] List of Amazon-defined identifiers for the region scope. Max values supported is 50.",
        ),
    ]


"""
JobListing

The payload for the `getServiceJobs` operation.
"""


class JobListing(SpApiBaseModel):
    """The payload for the `getServiceJobs` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    total_result_size: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("totalResultSize", "total_result_size"),
            serialization_alias="totalResultSize",
            description="Total result size of the query result.",
        ),
    ]

    next_page_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nextPageToken", "next_page_token"),
            serialization_alias="nextPageToken",
            description="A generated string used to pass information to your next request. If `nextPageToken` is returned, pass the value of `nextPageToken` to the `pageToken` to get next results.",
        ),
    ]

    previous_page_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("previousPageToken", "previous_page_token"),
            serialization_alias="previousPageToken",
            description="A generated string used to pass information to your next request. If `previousPageToken` is returned, pass the value of `previousPageToken` to the `pageToken` to get previous page results.",
        ),
    ]

    jobs: Annotated[
        Optional[List["ServiceJob"]],
        Field(None, description="List of job details for the given input."),
    ]


"""
GetServiceJobsResponse

Response schema for the `getServiceJobs` operation.
"""


class GetServiceJobsResponse(SpApiBaseModel):
    """Response schema for the `getServiceJobs` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["JobListing"],
        Field(None, description="The payload for the `getServiceJobs` operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="An unexpected condition occurred during the `getServiceJobs` operation.",
        ),
    ]


"""
RangeSlot

Capacity slots represented in a format similar to availability rules.
"""


class RangeSlot(SpApiBaseModel):
    """Capacity slots represented in a format similar to availability rules."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    start_date_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("startDateTime", "start_date_time"),
            serialization_alias="startDateTime",
            description="Start date time of slot in ISO 8601 format with precision of seconds.",
        ),
    ]

    end_date_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("endDateTime", "end_date_time"),
            serialization_alias="endDateTime",
            description="End date time of slot in ISO 8601 format with precision of seconds.",
        ),
    ]

    capacity: Annotated[Optional[int], Field(None, description="Capacity of the slot.")]


"""
RangeCapacity

Range capacity entity where each entry has a capacity type and corresponding slots.
"""


class RangeCapacity(SpApiBaseModel):
    """Range capacity entity where each entry has a capacity type and corresponding slots."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    capacity_type: Annotated[
        Optional["CapacityType"],
        Field(
            None,
            validation_alias=AliasChoices("capacityType", "capacity_type"),
            serialization_alias="capacityType",
            description="Capacity type corresponding to the slots.",
        ),
    ]

    slots: Annotated[
        Optional[List["RangeSlot"]],
        Field(None, description="Array of capacity slots in range slot format."),
    ]


"""
RangeSlotCapacity

Response schema for the `getRangeSlotCapacity` operation.
"""


class RangeSlotCapacity(SpApiBaseModel):
    """Response schema for the `getRangeSlotCapacity` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    resource_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("resourceId", "resource_id"),
            serialization_alias="resourceId",
            description="Resource Identifier.",
        ),
    ]

    capacities: Annotated[
        Optional[List["RangeCapacity"]],
        Field(
            None,
            description="Array of range capacities where each entry is for a specific capacity type.",
        ),
    ]

    next_page_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nextPageToken", "next_page_token"),
            serialization_alias="nextPageToken",
            description="Next page token, if there are more pages.",
        ),
    ]


"""
RangeSlotCapacityErrors

The error response schema for the `getRangeSlotCapacity` operation.
"""


class RangeSlotCapacityErrors(SpApiBaseModel):
    """The error response schema for the `getRangeSlotCapacity` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="Errors encountered during the `getRangeSlotCapacity` operation.",
        ),
    ]


RescheduleReasonCode = str
"""The appointment reschedule reason code."""


"""
RescheduleAppointmentRequestBody

Input for rescheduled appointment operation.
"""


class RescheduleAppointmentRequestBody(SpApiBaseModel):
    """Input for rescheduled appointment operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    appointment_time: Annotated[
        "AppointmentTimeInput",
        Field(
            ...,
            validation_alias=AliasChoices("appointmentTime", "appointment_time"),
            serialization_alias="appointmentTime",
            description="Input appointment time details.",
        ),
    ]

    reschedule_reason_code: Annotated[
        "RescheduleReasonCode",
        Field(
            ...,
            validation_alias=AliasChoices(
                "rescheduleReasonCode", "reschedule_reason_code"
            ),
            serialization_alias="rescheduleReasonCode",
            description="Input appointment reschedule reason.",
        ),
    ]


"""
RescheduleAppointmentForServiceJobByServiceJobIdRequest

Request parameters for rescheduleAppointmentForServiceJobByServiceJobId
"""


class RescheduleAppointmentForServiceJobByServiceJobIdRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for rescheduleAppointmentForServiceJobByServiceJobId
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    service_job_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("serviceJobId", "service_job_id"),
            serialization_alias="serviceJobId",
            description="[PATH] An Amazon defined service job identifier.",
        ),
    ]

    appointment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("appointmentId", "appointment_id"),
            serialization_alias="appointmentId",
            description="[PATH] An existing appointment identifier for the Service Job.",
        ),
    ]

    body: Annotated[
        "RescheduleAppointmentRequestBody",
        BodyParam(),
        Field(
            ..., description="[BODY] Reschedule appointment operation input details."
        ),
    ]


"""
SetAppointmentFulfillmentDataRequestBody

Input for set appointment fulfillment data operation.
"""


class SetAppointmentFulfillmentDataRequestBody(SpApiBaseModel):
    """Input for set appointment fulfillment data operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    estimated_arrival_time: Annotated[
        Optional["DateTimeRange"],
        Field(
            None,
            validation_alias=AliasChoices(
                "estimatedArrivalTime", "estimated_arrival_time"
            ),
            serialization_alias="estimatedArrivalTime",
            description="The range of time when the technician is expected to arrive at the fulfillment location.",
        ),
    ]

    fulfillment_time: Annotated[
        Optional["FulfillmentTime"],
        Field(
            None,
            validation_alias=AliasChoices("fulfillmentTime", "fulfillment_time"),
            serialization_alias="fulfillmentTime",
            description="Input appointment time details.",
        ),
    ]

    appointment_resources: Annotated[
        Optional["AppointmentResources"],
        Field(
            None,
            validation_alias=AliasChoices(
                "appointmentResources", "appointment_resources"
            ),
            serialization_alias="appointmentResources",
            description="Resources involved in appointment fulfillment.",
        ),
    ]

    fulfillment_documents: Annotated[
        Optional["FulfillmentDocuments"],
        Field(
            None,
            validation_alias=AliasChoices(
                "fulfillmentDocuments", "fulfillment_documents"
            ),
            serialization_alias="fulfillmentDocuments",
            description="Documents specific to appointment fulfillment.",
        ),
    ]


"""
SetAppointmentFulfillmentDataRequest

Request parameters for setAppointmentFulfillmentData
"""


class SetAppointmentFulfillmentDataRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for setAppointmentFulfillmentData
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    service_job_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("serviceJobId", "service_job_id"),
            serialization_alias="serviceJobId",
            description="[PATH] An Amazon-defined service job identifier. Get this value by calling the `getServiceJobs` operation of the Services API.",
        ),
    ]

    appointment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("appointmentId", "appointment_id"),
            serialization_alias="appointmentId",
            description="[PATH] An Amazon-defined identifier of active service job appointment.",
        ),
    ]

    body: Annotated[
        "SetAppointmentFulfillmentDataRequestBody",
        BodyParam(),
        Field(
            ..., description="[BODY] Appointment fulfillment data collection details."
        ),
    ]


"""
SetAppointmentResponse

Response schema for the `addAppointmentForServiceJobByServiceJobId` and `rescheduleAppointmentForServiceJobByServiceJobId` operations.
"""


class SetAppointmentResponse(SpApiBaseModel):
    """Response schema for the `addAppointmentForServiceJobByServiceJobId` and `rescheduleAppointmentForServiceJobByServiceJobId` operations."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    appointment_id: Annotated[
        Optional["AppointmentId"],
        Field(
            None,
            validation_alias=AliasChoices("appointmentId", "appointment_id"),
            serialization_alias="appointmentId",
            description="New appointment identifier generated during the `addAppointmentForServiceJobByServiceJobId` or `rescheduleAppointmentForServiceJobByServiceJobId` operations.",
        ),
    ]

    warnings: Annotated[
        Optional["WarningList"],
        Field(
            None,
            description="Warnings generated during the `addAppointmentForServiceJobByServiceJobId` or `rescheduleAppointmentForServiceJobByServiceJobId` operations.",
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="Errors occurred during during the `addAppointmentForServiceJobByServiceJobId` or `rescheduleAppointmentForServiceJobByServiceJobId` operations.",
        ),
    ]


"""
UpdateReservationRecord

`UpdateReservationRecord` entity contains the `Reservation` if there is an error/warning while performing the requested operation on it, otherwise it will contain the new `reservationId`.
"""


class UpdateReservationRecord(SpApiBaseModel):
    """`UpdateReservationRecord` entity contains the `Reservation` if there is an error/warning while performing the requested operation on it, otherwise it will contain the new `reservationId`."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    reservation: Annotated[
        Optional["Reservation"],
        Field(
            None,
            description="Reservation record if the operation failed. It will only contain the new `reservationId` if the operation is successful.",
        ),
    ]

    warnings: Annotated[
        Optional["WarningList"],
        Field(None, description="Warnings encountered, if any."),
    ]

    errors: Annotated[
        Optional["ErrorList"], Field(None, description="Errors encountered, if any.")
    ]


"""
UpdateReservationRequestBody

RequestBody schema for the `updateReservation` operation.
"""


class UpdateReservationRequestBody(SpApiBaseModel):
    """RequestBody schema for the `updateReservation` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    resource_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("resourceId", "resource_id"),
            serialization_alias="resourceId",
            description="Resource (store) identifier.",
        ),
    ]

    reservation: Annotated[
        "Reservation",
        Field(
            ...,
            description="`Reservation` object to reduce the capacity of a resource.",
        ),
    ]


"""
UpdateReservationRequest

Request parameters for updateReservation
"""


class UpdateReservationRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for updateReservation
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    reservation_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("reservationId", "reservation_id"),
            serialization_alias="reservationId",
            description="[PATH] Reservation Identifier",
        ),
    ]

    body: Annotated[
        "UpdateReservationRequestBody",
        BodyParam(),
        Field(..., description="[BODY] Reservation details"),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] An identifier for the marketplace in which the resource operates.",
        ),
    ]


"""
UpdateReservationResponse

Response schema for the `updateReservation` operation.
"""


class UpdateReservationResponse(SpApiBaseModel):
    """Response schema for the `updateReservation` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["UpdateReservationRecord"],
        Field(
            None,
            description="`UpdateReservationRecord` contains only the new `reservationId` if the operation was successful. Otherwise it will contain the reservation entity with warnings/errors.",
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"], Field(None, description="Errors encountered, if any.")
    ]


"""
UpdateScheduleRecord

`UpdateScheduleRecord` entity contains the `AvailabilityRecord` if there is an error/warning while performing the requested operation on it.
"""


class UpdateScheduleRecord(SpApiBaseModel):
    """`UpdateScheduleRecord` entity contains the `AvailabilityRecord` if there is an error/warning while performing the requested operation on it."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    availability: Annotated[
        Optional["AvailabilityRecord"],
        Field(None, description="Availability record if the operation failed."),
    ]

    warnings: Annotated[
        Optional["WarningList"],
        Field(None, description="Warnings encountered, if any."),
    ]

    errors: Annotated[
        Optional["ErrorList"], Field(None, description="Errors encountered, if any.")
    ]


"""
UpdateScheduleRequestBody

RequestBody schema for the `updateSchedule` operation.
"""


class UpdateScheduleRequestBody(SpApiBaseModel):
    """RequestBody schema for the `updateSchedule` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    schedules: Annotated[
        "AvailabilityRecords",
        Field(
            ...,
            description="List of schedule objects to define the normal working hours of a resource.",
        ),
    ]


"""
UpdateScheduleRequest

Request parameters for updateSchedule
"""


class UpdateScheduleRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for updateSchedule
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    resource_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("resourceId", "resource_id"),
            serialization_alias="resourceId",
            description="[PATH] Resource (store) Identifier",
        ),
    ]

    body: Annotated[
        "UpdateScheduleRequestBody",
        BodyParam(),
        Field(..., description="[BODY] Schedule details"),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] An identifier for the marketplace in which the resource operates.",
        ),
    ]


"""
UpdateScheduleResponse

Response schema for the `updateSchedule` operation.
"""


class UpdateScheduleResponse(SpApiBaseModel):
    """Response schema for the `updateSchedule` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional[List["UpdateScheduleRecord"]],
        Field(
            None,
            description="Contains the `UpdateScheduleRecords` for which the error/warning has occurred.",
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"], Field(None, description="Errors encountered, if any.")
    ]


"""
Warning

Warning returned when the request is successful, but there are important callouts based on which API clients should take defined actions.
"""


class Warning(SpApiBaseModel):
    """Warning returned when the request is successful, but there are important callouts based on which API clients should take defined actions."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    code: Annotated[
        str,
        Field(
            ...,
            description="An warning code that identifies the type of warning that occurred.",
        ),
    ]

    message: Annotated[
        str,
        Field(
            ...,
            description="A message that describes the warning condition in a human-readable form.",
        ),
    ]

    details: Annotated[
        Optional[str],
        Field(
            None,
            description="Additional details that can help the caller understand or address the warning.",
        ),
    ]


# Rebuild models to resolve forward references
GetServiceJobByServiceJobIdResponse.model_rebuild()
CancelServiceJobByServiceJobIdResponse.model_rebuild()
CompleteServiceJobByServiceJobIdResponse.model_rebuild()
GetServiceJobsResponse.model_rebuild()
SetAppointmentResponse.model_rebuild()
AssignAppointmentResourcesResponse.model_rebuild()
AssignAppointmentResourcesRequestBody.model_rebuild()
JobListing.model_rebuild()
ServiceJob.model_rebuild()
ScopeOfWork.model_rebuild()
Seller.model_rebuild()
ServiceJobProvider.model_rebuild()
Buyer.model_rebuild()
AppointmentTime.model_rebuild()
Appointment.model_rebuild()
Technician.model_rebuild()
Poa.model_rebuild()
AssociatedItem.model_rebuild()
ItemDelivery.model_rebuild()
ItemDeliveryPromise.model_rebuild()
ServiceLocation.model_rebuild()
Address.model_rebuild()
AddAppointmentRequestBody.model_rebuild()
RescheduleAppointmentRequestBody.model_rebuild()
AppointmentTimeInput.model_rebuild()
Error.model_rebuild()
Warning.model_rebuild()
RangeSlotCapacityErrors.model_rebuild()
RangeSlotCapacity.model_rebuild()
RangeCapacity.model_rebuild()
RangeSlot.model_rebuild()
FixedSlotCapacityErrors.model_rebuild()
FixedSlotCapacity.model_rebuild()
FixedSlot.model_rebuild()
UpdateScheduleResponse.model_rebuild()
SetAppointmentFulfillmentDataRequestBody.model_rebuild()
FulfillmentTime.model_rebuild()
DateTimeRange.model_rebuild()
FulfillmentDocument.model_rebuild()
AppointmentResource.model_rebuild()
CreateReservationResponse.model_rebuild()
UpdateReservationResponse.model_rebuild()
CancelReservationResponse.model_rebuild()
Recurrence.model_rebuild()
AvailabilityRecord.model_rebuild()
Reservation.model_rebuild()
UpdateScheduleRecord.model_rebuild()
CreateReservationRecord.model_rebuild()
UpdateReservationRecord.model_rebuild()
RangeSlotCapacityQuery.model_rebuild()
FixedSlotCapacityQuery.model_rebuild()
UpdateScheduleRequestBody.model_rebuild()
CreateReservationRequestBody.model_rebuild()
UpdateReservationRequestBody.model_rebuild()
GetAppointmentSlotsResponse.model_rebuild()
AppointmentSlotReport.model_rebuild()
AppointmentSlot.model_rebuild()
ServiceUploadDocument.model_rebuild()
CreateServiceDocumentUploadDestination.model_rebuild()
ServiceDocumentUploadDestination.model_rebuild()
EncryptionDetails.model_rebuild()
GetServiceJobByServiceJobIdRequest.model_rebuild()
CancelServiceJobByServiceJobIdRequest.model_rebuild()
CompleteServiceJobByServiceJobIdRequest.model_rebuild()
GetServiceJobsRequest.model_rebuild()
AddAppointmentForServiceJobByServiceJobIdRequest.model_rebuild()
RescheduleAppointmentForServiceJobByServiceJobIdRequest.model_rebuild()
AssignAppointmentResourcesRequest.model_rebuild()
SetAppointmentFulfillmentDataRequest.model_rebuild()
GetRangeSlotCapacityRequest.model_rebuild()
GetFixedSlotCapacityRequest.model_rebuild()
UpdateScheduleRequest.model_rebuild()
CreateReservationRequest.model_rebuild()
UpdateReservationRequest.model_rebuild()
CancelReservationRequest.model_rebuild()
GetAppointmmentSlotsByJobIdRequest.model_rebuild()
GetAppointmentSlotsRequest.model_rebuild()
CreateServiceDocumentUploadDestinationRequest.model_rebuild()
