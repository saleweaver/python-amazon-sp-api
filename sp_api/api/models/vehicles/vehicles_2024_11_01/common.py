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

EngineOutputUnit = str
"""Unit for measuring engine power."""


"""
EngineOutput

Engine power output of vehicle.
"""


class EngineOutput(SpApiBaseModel):
    """Engine power output of vehicle."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    value: Annotated[
        float, Field(..., description="Engine power value in specified unit.")
    ]

    unit: Annotated[
        "EngineOutputUnit", Field(..., description="Unit for measuring engine power.")
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

    errors: Annotated[List["Error"], Field(..., description="array of errors")]


# Enum definitions
class VehicleTypeEnum(str, Enum):
    """Enum for vehicleType"""

    CAR = "CAR"  # Selecting this will return the list of cars.
    MOTORBIKE = (
        "MOTORBIKE"  # Selecting this will return the list of motorbikes/motorcycles.
    )


"""
GetVehiclesRequest

Request parameters for getVehicles
"""


class GetVehiclesRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getVehicles
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

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

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] An identifier for the marketplace in which the resource operates.",
        ),
    ]

    vehicle_type: Annotated[
        VehicleTypeEnum,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("vehicleType", "vehicle_type"),
            serialization_alias="vehicleType",
            description="[QUERY] An identifier for vehicle type.",
        ),
    ]

    updated_after: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("updatedAfter", "updated_after"),
            serialization_alias="updatedAfter",
            description="[QUERY] Date in ISO 8601 format, if provided only vehicles which are modified/added to Amazon's catalog after this date will be returned.",
        ),
    ]


Month = float
"""Month in MM format"""


Year = float
"""Year in YYYY format"""


"""
MonthAndYear

Represents a month in a specific year.
"""


class MonthAndYear(SpApiBaseModel):
    """Represents a month in a specific year."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    year: Annotated[
        Optional["Year"],
        Field(
            None,
        ),
    ]

    month: Annotated[
        Optional["Month"],
        Field(
            None,
        ),
    ]


"""
Pagination

When a request produces a response that exceeds the `pageSize`, pagination occurs. This means the response is divided into individual pages. To retrieve the next page or the previous page, you must pass the `nextToken` value or the `previousToken` value as the `pageToken` parameter in the next request. When you receive the last page, there will be no `nextToken` key in the pagination object.
"""


class Pagination(SpApiBaseModel):
    """When a request produces a response that exceeds the `pageSize`, pagination occurs. This means the response is divided into individual pages. To retrieve the next page or the previous page, you must pass the `nextToken` value or the `previousToken` value as the `pageToken` parameter in the next request. When you receive the last page, there will be no `nextToken` key in the pagination object."""

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


VehicleStandard = str
"""Standard followed to uniquely identify a vehicle."""


"""
VehicleIdentifiers

Combination of vehicle standard and id that can uniquely identify a vehicle from Amazon's catalog.
"""


class VehicleIdentifiers(SpApiBaseModel):
    """Combination of vehicle standard and id that can uniquely identify a vehicle from Amazon's catalog."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    standard: Annotated[
        "VehicleStandard",
        Field(..., description="Vehicle standard used to uniquely identify a vehicle."),
    ]

    value: Annotated[
        str,
        Field(
            ...,
            description="Id that can uniquely identify a vehicle based the vehicle identification standard.",
        ),
    ]


VehicleStatusInCatalog = str
"""Status of vehicle in Amazon's catalog."""


"""
Vehicle

Combinations of attributes and unique identifier that represents a vehicle in vehicle list.
"""


class Vehicle(SpApiBaseModel):
    """Combinations of attributes and unique identifier that represents a vehicle in vehicle list."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    make: Annotated[str, Field(..., description="Vehicle Brand.")]

    model: Annotated[str, Field(..., description="Specific model of a vehicle.")]

    variant_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("variantName", "variant_name"),
            serialization_alias="variantName",
            description="Name of the vehicle variant.",
        ),
    ]

    body_style: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("bodyStyle", "body_style"),
            serialization_alias="bodyStyle",
            description="Body style of vehicle (example: Hatchback, Cabriolet).",
        ),
    ]

    drive_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("driveType", "drive_type"),
            serialization_alias="driveType",
            description="Drive type of vehicle(example: Rear wheel drive).",
        ),
    ]

    energy: Annotated[
        Optional[str],
        Field(None, description="Energy Source for the vehicle(example: Petrol)"),
    ]

    engine_output: Annotated[
        Optional[List["EngineOutput"]],
        Field(
            None,
            validation_alias=AliasChoices("engineOutput", "engine_output"),
            serialization_alias="engineOutput",
            description="Engine output of vehicle.",
        ),
    ]

    manufacturing_start_date: Annotated[
        Optional["MonthAndYear"],
        Field(
            None,
            validation_alias=AliasChoices(
                "manufacturingStartDate", "manufacturing_start_date"
            ),
            serialization_alias="manufacturingStartDate",
            description="Vehicle manufacturing start date.",
        ),
    ]

    manufacturing_stop_date: Annotated[
        Optional["MonthAndYear"],
        Field(
            None,
            validation_alias=AliasChoices(
                "manufacturingStopDate", "manufacturing_stop_date"
            ),
            serialization_alias="manufacturingStopDate",
            description="Vehicle manufacturing stop date. If it is empty, then the vehicle is still being manufactured.",
        ),
    ]

    last_processed_date: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("lastProcessedDate", "last_processed_date"),
            serialization_alias="lastProcessedDate",
            description="The date on which the vehicle was last updated, in ISO-8601 date/time format.",
        ),
    ]

    status: Annotated[
        Optional["VehicleStatusInCatalog"],
        Field(
            None,
            description="Denotes if the vehicle is active or deleted from Amazon's catalog.",
        ),
    ]

    identifiers: Annotated[
        List["VehicleIdentifiers"],
        Field(
            ...,
            description="Identifiers that can be used to identify the vehicle uniquely",
        ),
    ]


"""
VehiclesResponse

Get paginated list of vehicle from Amazon's catalog
"""


class VehiclesResponse(SpApiBaseModel):
    """Get paginated list of vehicle from Amazon's catalog"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
            description="If available, the `nextToken` and/or `previousToken` values required to return paginated results.",
        ),
    ]

    vehicles: Annotated[
        List["Vehicle"],
        Field(..., description="List of vehicles from Amazon's catalog."),
    ]


# Rebuild models to resolve forward references
VehiclesResponse.model_rebuild()
Pagination.model_rebuild()
Vehicle.model_rebuild()
EngineOutput.model_rebuild()
VehicleIdentifiers.model_rebuild()
ErrorList.model_rebuild()
Error.model_rebuild()
MonthAndYear.model_rebuild()
GetVehiclesRequest.model_rebuild()
