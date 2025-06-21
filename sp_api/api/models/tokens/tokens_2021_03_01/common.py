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


# Enum definitions
class MethodEnum(str, Enum):
    """Enum for method"""

    GET = "GET"  # The GET method.
    PUT = "PUT"  # The PUT method.
    POST = "POST"  # The POST method.
    DELETE = "DELETE"  # The DELETE method.


"""
RestrictedResource

Model of a restricted resource.
"""


class RestrictedResource(SpApiBaseModel):
    """Model of a restricted resource."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    method: Annotated[
        MethodEnum,
        Field(..., description="The HTTP method in the restricted resource."),
    ]

    path: Annotated[
        str,
        Field(
            ...,
            description="The path in the restricted resource. Here are some path examples: - ```/orders/v0/orders```. For getting an RDT for the getOrders operation of the Orders API. For bulk orders. - ```/orders/v0/orders/123-1234567-1234567```. For getting an RDT for the getOrder operation of the Orders API. For a specific order. - ```/orders/v0/orders/123-1234567-1234567/orderItems```. For getting an RDT for the getOrderItems operation of the Orders API. For the order items in a specific order. - ```/mfn/v0/shipments/FBA1234ABC5D```. For getting an RDT for the getShipment operation of the Shipping API. For a specific shipment. - ```/mfn/v0/shipments/{shipmentId}```. For getting an RDT for the getShipment operation of the Shipping API. For any of a selling partner's shipments that you specify when you call the getShipment operation.",
        ),
    ]

    data_elements: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("dataElements", "data_elements"),
            serialization_alias="dataElements",
            description="Indicates the type of Personally Identifiable Information requested. This parameter is required only when getting an RDT for use with the getOrder, getOrders, or getOrderItems operation of the Orders API. For more information, see the [Tokens API Use Case Guide](doc:tokens-api-use-case-guide). Possible values include: - **buyerInfo**. On the order level this includes general identifying information about the buyer and tax-related information. On the order item level this includes gift wrap information and custom order information, if available. - **shippingAddress**. This includes information for fulfilling orders. - **buyerTaxInformation**. This includes information for issuing tax invoices.",
        ),
    ]


"""
CreateRestrictedDataTokenRequestBody

The request schema for the createRestrictedDataToken operation.
"""


class CreateRestrictedDataTokenRequestBody(SpApiBaseModel):
    """The request schema for the createRestrictedDataToken operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    target_application: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("targetApplication", "target_application"),
            serialization_alias="targetApplication",
            description="The application ID for the target application to which access is being delegated.",
        ),
    ]

    restricted_resources: Annotated[
        List["RestrictedResource"],
        Field(
            ...,
            validation_alias=AliasChoices(
                "restrictedResources", "restricted_resources"
            ),
            serialization_alias="restrictedResources",
            description="A list of restricted resources. Maximum: 50",
        ),
    ]


"""
CreateRestrictedDataTokenRequest

Request parameters for createRestrictedDataToken
"""


class CreateRestrictedDataTokenRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createRestrictedDataToken
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "CreateRestrictedDataTokenRequestBody",
        BodyParam(),
        Field(..., description="[BODY] The restricted data token request details."),
    ]


"""
CreateRestrictedDataTokenResponse

The response schema for the createRestrictedDataToken operation.
"""


class CreateRestrictedDataTokenResponse(SpApiBaseModel):
    """The response schema for the createRestrictedDataToken operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    restricted_data_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "restrictedDataToken", "restricted_data_token"
            ),
            serialization_alias="restrictedDataToken",
            description="A Restricted Data Token (RDT). This is a short-lived access token that authorizes calls to restricted operations. Pass this value with the x-amz-access-token header when making subsequent calls to these restricted resources.",
        ),
    ]

    expires_in: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("expiresIn", "expires_in"),
            serialization_alias="expiresIn",
            description="The lifetime of the Restricted Data Token, in seconds.",
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
        Optional[List["Error"]],
        Field(
            None,
        ),
    ]


# Rebuild models to resolve forward references
CreateRestrictedDataTokenRequestBody.model_rebuild()
RestrictedResource.model_rebuild()
CreateRestrictedDataTokenResponse.model_rebuild()
Error.model_rebuild()
ErrorList.model_rebuild()
CreateRestrictedDataTokenRequest.model_rebuild()
