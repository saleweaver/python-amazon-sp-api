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
Attachment

Represents a file that was uploaded to a destination that was created by the Uploads API [`createUploadDestinationForResource`](https://developer-docs.amazon.com/sp-api/docs/uploads-api-reference#post-uploads2020-11-01uploaddestinationsresource) operation.
"""


class Attachment(SpApiBaseModel):
    """Represents a file that was uploaded to a destination that was created by the Uploads API [`createUploadDestinationForResource`](https://developer-docs.amazon.com/sp-api/docs/uploads-api-reference#post-uploads2020-11-01uploaddestinationsresource) operation."""

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
            description="The identifier for the upload destination. To retrieve this value, call the Uploads API [`createUploadDestinationForResource`](https://developer-docs.amazon.com/sp-api/docs/uploads-api-reference#post-uploads2020-11-01uploaddestinationsresource) operation.",
        ),
    ]

    file_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("fileName", "file_name"),
            serialization_alias="fileName",
            description="The name of the file, including the extension. This is the file name that will appear in the message. This does not need to match the file name of the file that you uploaded.",
        ),
    ]


"""
CreateConfirmCustomizationDetailsRequestBody

The request schema for the confirmCustomizationDetails operation.
"""


class CreateConfirmCustomizationDetailsRequestBody(SpApiBaseModel):
    """The request schema for the confirmCustomizationDetails operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    text: Annotated[
        Optional[str],
        Field(
            None,
            description="The text to be sent to the buyer. Only links related to customization details are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.",
        ),
    ]

    attachments: Annotated[
        Optional[List["Attachment"]],
        Field(None, description="Attachments to include in the message to the buyer."),
    ]


"""
ConfirmCustomizationDetailsRequest

Request parameters for confirmCustomizationDetails
"""


class ConfirmCustomizationDetailsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for confirmCustomizationDetails
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("amazonOrderId", "amazon_order_id"),
            serialization_alias="amazonOrderId",
            description="[PATH] An Amazon order identifier. This identifies the order for which a message is sent.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one marketplace.",
        ),
    ]

    body: Annotated[
        "CreateConfirmCustomizationDetailsRequestBody",
        BodyParam(),
        Field(..., description="[BODY] This contains the message body for a message."),
    ]


"""
CreateAmazonMotorsRequestBody

The request schema for the createAmazonMotors operation.
"""


class CreateAmazonMotorsRequestBody(SpApiBaseModel):
    """The request schema for the createAmazonMotors operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    attachments: Annotated[
        Optional[List["Attachment"]],
        Field(
            None,
            description="Attachments to include in the message to the buyer. If any text is included in the attachment, the text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.",
        ),
    ]


"""
CreateAmazonMotorsRequest

Request parameters for CreateAmazonMotors
"""


class CreateAmazonMotorsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for CreateAmazonMotors
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("amazonOrderId", "amazon_order_id"),
            serialization_alias="amazonOrderId",
            description="[PATH] An Amazon order identifier. This identifies the order for which a message is sent.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one marketplace.",
        ),
    ]

    body: Annotated[
        "CreateAmazonMotorsRequestBody",
        BodyParam(),
        Field(..., description="[BODY] This contains the message body for a message."),
    ]


ErrorList = List["Error"]
"""A list of error responses returned when a request is unsuccessful."""


"""
CreateAmazonMotorsResponse

The response schema for the createAmazonMotors operation.
"""


class CreateAmazonMotorsResponse(SpApiBaseModel):
    """The response schema for the createAmazonMotors operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


"""
CreateConfirmCustomizationDetailsResponse

The response schema for the confirmCustomizationDetails operation.
"""


class CreateConfirmCustomizationDetailsResponse(SpApiBaseModel):
    """The response schema for the confirmCustomizationDetails operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


"""
CreateConfirmDeliveryDetailsRequestBody

The request schema for the createConfirmDeliveryDetails operation.
"""


class CreateConfirmDeliveryDetailsRequestBody(SpApiBaseModel):
    """The request schema for the createConfirmDeliveryDetails operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    text: Annotated[
        Optional[str],
        Field(
            None,
            description="The text to be sent to the buyer. Only links related to order delivery are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.",
        ),
    ]


"""
CreateConfirmDeliveryDetailsRequest

Request parameters for createConfirmDeliveryDetails
"""


class CreateConfirmDeliveryDetailsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createConfirmDeliveryDetails
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("amazonOrderId", "amazon_order_id"),
            serialization_alias="amazonOrderId",
            description="[PATH] An Amazon order identifier. This identifies the order for which a message is sent.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one marketplace.",
        ),
    ]

    body: Annotated[
        "CreateConfirmDeliveryDetailsRequestBody",
        BodyParam(),
        Field(..., description="[BODY] This contains the message body for a message."),
    ]


"""
CreateConfirmDeliveryDetailsResponse

The response schema for the createConfirmDeliveryDetails operation.
"""


class CreateConfirmDeliveryDetailsResponse(SpApiBaseModel):
    """The response schema for the createConfirmDeliveryDetails operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


"""
CreateConfirmOrderDetailsRequestBody

The request schema for the createConfirmOrderDetails operation.
"""


class CreateConfirmOrderDetailsRequestBody(SpApiBaseModel):
    """The request schema for the createConfirmOrderDetails operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    text: Annotated[
        Optional[str],
        Field(
            None,
            description="The text to be sent to the buyer. Only links related to order completion are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.",
        ),
    ]


"""
CreateConfirmOrderDetailsRequest

Request parameters for createConfirmOrderDetails
"""


class CreateConfirmOrderDetailsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createConfirmOrderDetails
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("amazonOrderId", "amazon_order_id"),
            serialization_alias="amazonOrderId",
            description="[PATH] An Amazon order identifier. This identifies the order for which a message is sent.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one marketplace.",
        ),
    ]

    body: Annotated[
        "CreateConfirmOrderDetailsRequestBody",
        BodyParam(),
        Field(..., description="[BODY] This contains the message body for a message."),
    ]


"""
CreateConfirmOrderDetailsResponse

The response schema for the createConfirmOrderDetails operation.
"""


class CreateConfirmOrderDetailsResponse(SpApiBaseModel):
    """The response schema for the createConfirmOrderDetails operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


"""
CreateConfirmServiceDetailsRequestBody

The request schema for the createConfirmServiceDetails operation.
"""


class CreateConfirmServiceDetailsRequestBody(SpApiBaseModel):
    """The request schema for the createConfirmServiceDetails operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    text: Annotated[
        Optional[str],
        Field(
            None,
            description="The text to be sent to the buyer. Only links related to Home Service calls are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.",
        ),
    ]


"""
CreateConfirmServiceDetailsRequest

Request parameters for createConfirmServiceDetails
"""


class CreateConfirmServiceDetailsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createConfirmServiceDetails
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("amazonOrderId", "amazon_order_id"),
            serialization_alias="amazonOrderId",
            description="[PATH] An Amazon order identifier. This identifies the order for which a message is sent.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one marketplace.",
        ),
    ]

    body: Annotated[
        "CreateConfirmServiceDetailsRequestBody",
        BodyParam(),
        Field(..., description="[BODY] This contains the message body for a message."),
    ]


"""
CreateConfirmServiceDetailsResponse

The response schema for the createConfirmServiceDetails operation.
"""


class CreateConfirmServiceDetailsResponse(SpApiBaseModel):
    """The response schema for the createConfirmServiceDetails operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


"""
CreateDigitalAccessKeyRequestBody

The request schema for the `createDigitalAccessKey` operation.
"""


class CreateDigitalAccessKeyRequestBody(SpApiBaseModel):
    """The request schema for the `createDigitalAccessKey` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    text: Annotated[
        Optional[str],
        Field(
            None,
            description="The text that is sent to the buyer. Only links that are related to the digital access key are allowed. Do not include HTML or email addresses. The text must be written in the buyer's preferred language, which you can retrieve from the `GetAttributes` operation.",
        ),
    ]

    attachments: Annotated[
        Optional[List["Attachment"]],
        Field(
            None,
            description="Attachments that you want to include in the message to the buyer.",
        ),
    ]


"""
CreateDigitalAccessKeyRequest

Request parameters for createDigitalAccessKey
"""


class CreateDigitalAccessKeyRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createDigitalAccessKey
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("amazonOrderId", "amazon_order_id"),
            serialization_alias="amazonOrderId",
            description="[PATH] An Amazon order identifier. This identifies the order for which a message is sent.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one marketplace.",
        ),
    ]

    body: Annotated[
        "CreateDigitalAccessKeyRequestBody",
        BodyParam(),
        Field(..., description="[BODY] This contains the message body for a message."),
    ]


"""
CreateDigitalAccessKeyResponse

The response schema for the `createDigitalAccessKey` operation.
"""


class CreateDigitalAccessKeyResponse(SpApiBaseModel):
    """The response schema for the `createDigitalAccessKey` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


"""
CreateLegalDisclosureRequestBody

The request schema for the createLegalDisclosure operation.
"""


class CreateLegalDisclosureRequestBody(SpApiBaseModel):
    """The request schema for the createLegalDisclosure operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    attachments: Annotated[
        Optional[List["Attachment"]],
        Field(
            None,
            description="Attachments to include in the message to the buyer. If any text is included in the attachment, the text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.",
        ),
    ]


"""
CreateLegalDisclosureRequest

Request parameters for createLegalDisclosure
"""


class CreateLegalDisclosureRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createLegalDisclosure
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("amazonOrderId", "amazon_order_id"),
            serialization_alias="amazonOrderId",
            description="[PATH] An Amazon order identifier. This identifies the order for which a message is sent.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one marketplace.",
        ),
    ]

    body: Annotated[
        "CreateLegalDisclosureRequestBody",
        BodyParam(),
        Field(..., description="[BODY] This contains the message body for a message."),
    ]


"""
CreateLegalDisclosureResponse

The response schema for the createLegalDisclosure operation.
"""


class CreateLegalDisclosureResponse(SpApiBaseModel):
    """The response schema for the createLegalDisclosure operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


"""
CreateNegativeFeedbackRemovalRequest

Request parameters for createNegativeFeedbackRemoval
"""


class CreateNegativeFeedbackRemovalRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createNegativeFeedbackRemoval
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("amazonOrderId", "amazon_order_id"),
            serialization_alias="amazonOrderId",
            description="[PATH] An Amazon order identifier. This identifies the order for which a message is sent.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one marketplace.",
        ),
    ]


"""
CreateNegativeFeedbackRemovalResponse

The response schema for the createNegativeFeedbackRemoval operation.
"""


class CreateNegativeFeedbackRemovalResponse(SpApiBaseModel):
    """The response schema for the createNegativeFeedbackRemoval operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


"""
CreateUnexpectedProblemRequestBody

The request schema for the createUnexpectedProblem operation.
"""


class CreateUnexpectedProblemRequestBody(SpApiBaseModel):
    """The request schema for the createUnexpectedProblem operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    text: Annotated[
        Optional[str],
        Field(
            None,
            description="The text to be sent to the buyer. Only links related to unexpected problem calls are allowed. Do not include HTML or email addresses. The text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.",
        ),
    ]


"""
CreateUnexpectedProblemRequest

Request parameters for createUnexpectedProblem
"""


class CreateUnexpectedProblemRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createUnexpectedProblem
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("amazonOrderId", "amazon_order_id"),
            serialization_alias="amazonOrderId",
            description="[PATH] An Amazon order identifier. This identifies the order for which a message is sent.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one marketplace.",
        ),
    ]

    body: Annotated[
        "CreateUnexpectedProblemRequestBody",
        BodyParam(),
        Field(..., description="[BODY] This contains the message body for a message."),
    ]


"""
CreateUnexpectedProblemResponse

The response schema for the createUnexpectedProblem operation.
"""


class CreateUnexpectedProblemResponse(SpApiBaseModel):
    """The response schema for the createUnexpectedProblem operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


"""
CreateWarrantyRequestBody

The request schema for the createWarranty operation.
"""


class CreateWarrantyRequestBody(SpApiBaseModel):
    """The request schema for the createWarranty operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    attachments: Annotated[
        Optional[List["Attachment"]],
        Field(
            None,
            description="Attachments to include in the message to the buyer. If any text is included in the attachment, the text must be written in the buyer's language of preference, which can be retrieved from the GetAttributes operation.",
        ),
    ]

    coverage_start_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("coverageStartDate", "coverage_start_date"),
            serialization_alias="coverageStartDate",
            description="The start date of the warranty coverage to include in the message to the buyer.",
        ),
    ]

    coverage_end_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("coverageEndDate", "coverage_end_date"),
            serialization_alias="coverageEndDate",
            description="The end date of the warranty coverage to include in the message to the buyer.",
        ),
    ]


"""
CreateWarrantyRequest

Request parameters for CreateWarranty
"""


class CreateWarrantyRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for CreateWarranty
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("amazonOrderId", "amazon_order_id"),
            serialization_alias="amazonOrderId",
            description="[PATH] An Amazon order identifier. This identifies the order for which a message is sent.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one marketplace.",
        ),
    ]

    body: Annotated[
        "CreateWarrantyRequestBody",
        BodyParam(),
        Field(..., description="[BODY] This contains the message body for a message."),
    ]


"""
CreateWarrantyResponse

The response schema for the createWarranty operation.
"""


class CreateWarrantyResponse(SpApiBaseModel):
    """The response schema for the createWarranty operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
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
GetAttributesRequest

Request parameters for GetAttributes
"""


class GetAttributesRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for GetAttributes
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("amazonOrderId", "amazon_order_id"),
            serialization_alias="amazonOrderId",
            description="[PATH] An Amazon order identifier. This identifies the order for which a message is sent.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one marketplace.",
        ),
    ]


"""
GetAttributesResponse

The response schema for the GetAttributes operation.
"""


class GetAttributesResponse(SpApiBaseModel):
    """The response schema for the GetAttributes operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    buyer: Annotated[
        Optional[Dict[str, Any]],
        Field(None, description="The list of attributes related to the buyer."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


"""
MessagingAction

A simple object containing the name of the template.
"""


class MessagingAction(SpApiBaseModel):
    """A simple object containing the name of the template."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[str, Field(..., description="The name of the template.")]


"""
GetMessagingActionResponse

Describes a messaging action that can be taken for an order. Provides a JSON Hypertext Application Language (HAL) link to the JSON schema document that describes the expected input.
"""


class GetMessagingActionResponse(SpApiBaseModel):
    """Describes a messaging action that can be taken for an order. Provides a JSON Hypertext Application Language (HAL) link to the JSON schema document that describes the expected input."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    links: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            validation_alias=AliasChoices("_links", "links"),
            serialization_alias="_links",
            description="The links response that is associated with the messaging action.",
        ),
    ]

    embedded: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            validation_alias=AliasChoices("_embedded", "embedded"),
            serialization_alias="_embedded",
            description="The embedded response associated with the messaging action.",
        ),
    ]

    payload: Annotated[
        Optional["MessagingAction"],
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


"""
GetMessagingActionsForOrderRequest

Request parameters for getMessagingActionsForOrder
"""


class GetMessagingActionsForOrderRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getMessagingActionsForOrder
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("amazonOrderId", "amazon_order_id"),
            serialization_alias="amazonOrderId",
            description="[PATH] An Amazon order identifier. This specifies the order for which you want a list of available message types.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one marketplace.",
        ),
    ]


"""
GetMessagingActionsForOrderResponse

The response schema for the `getMessagingActionsForOrder` operation.
"""


class GetMessagingActionsForOrderResponse(SpApiBaseModel):
    """The response schema for the `getMessagingActionsForOrder` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    links: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            validation_alias=AliasChoices("_links", "links"),
            serialization_alias="_links",
            description="The links response that is associated with the specified `amazonOrderId`.",
        ),
    ]

    embedded: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            validation_alias=AliasChoices("_embedded", "embedded"),
            serialization_alias="_embedded",
            description="The messaging actions response that is associated with the specified `amazonOrderId`.",
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


"""
Schema

A JSON schema document describing the expected payload of the action. This object can be validated against <a href=http://json-schema.org/draft-04/schema>http://json-schema.org/draft-04/schema</a>.
"""


class Schema(SpApiBaseModel):
    """A JSON schema document describing the expected payload of the action. This object can be validated against <a href=http://json-schema.org/draft-04/schema>http://json-schema.org/draft-04/schema</a>."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
GetSchemaResponse

The `GET` request schema response.
"""


class GetSchemaResponse(SpApiBaseModel):
    """The `GET` request schema response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    links: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            validation_alias=AliasChoices("_links", "links"),
            serialization_alias="_links",
            description="The links response that is associated with the object.",
        ),
    ]

    payload: Annotated[
        Optional["Schema"],
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


"""
InvoiceRequestBody

The request schema for the `sendInvoice` operation.
"""


class InvoiceRequestBody(SpApiBaseModel):
    """The request schema for the `sendInvoice` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    attachments: Annotated[
        Optional[List["Attachment"]],
        Field(None, description="Attachments to include in the message to the buyer."),
    ]


"""
InvoiceResponse

The response schema for the sendInvoice operation.
"""


class InvoiceResponse(SpApiBaseModel):
    """The response schema for the sendInvoice operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


"""
LinkObject

A Link object.
"""


class LinkObject(SpApiBaseModel):
    """A Link object."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    href: Annotated[str, Field(..., description="A URI for this object.")]

    name: Annotated[
        Optional[str], Field(None, description="An identifier for this object.")
    ]


"""
SendInvoiceRequest

Request parameters for sendInvoice
"""


class SendInvoiceRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for sendInvoice
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("amazonOrderId", "amazon_order_id"),
            serialization_alias="amazonOrderId",
            description="[PATH] An Amazon order identifier. This identifies the order for which a message is sent.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one marketplace.",
        ),
    ]

    body: Annotated[
        "InvoiceRequestBody",
        BodyParam(),
        Field(..., description="[BODY] This contains the message body for a message."),
    ]


# Rebuild models to resolve forward references
Attachment.model_rebuild()
LinkObject.model_rebuild()
MessagingAction.model_rebuild()
Schema.model_rebuild()
GetMessagingActionsForOrderResponse.model_rebuild()
GetMessagingActionResponse.model_rebuild()
GetSchemaResponse.model_rebuild()
InvoiceRequestBody.model_rebuild()
InvoiceResponse.model_rebuild()
CreateConfirmCustomizationDetailsRequestBody.model_rebuild()
CreateConfirmCustomizationDetailsResponse.model_rebuild()
CreateConfirmDeliveryDetailsRequestBody.model_rebuild()
CreateConfirmDeliveryDetailsResponse.model_rebuild()
CreateNegativeFeedbackRemovalResponse.model_rebuild()
CreateLegalDisclosureRequestBody.model_rebuild()
CreateLegalDisclosureResponse.model_rebuild()
CreateConfirmOrderDetailsRequestBody.model_rebuild()
CreateConfirmOrderDetailsResponse.model_rebuild()
CreateConfirmServiceDetailsRequestBody.model_rebuild()
CreateConfirmServiceDetailsResponse.model_rebuild()
CreateAmazonMotorsRequestBody.model_rebuild()
CreateAmazonMotorsResponse.model_rebuild()
CreateWarrantyRequestBody.model_rebuild()
CreateWarrantyResponse.model_rebuild()
GetAttributesResponse.model_rebuild()
CreateDigitalAccessKeyRequestBody.model_rebuild()
CreateDigitalAccessKeyResponse.model_rebuild()
CreateUnexpectedProblemRequestBody.model_rebuild()
CreateUnexpectedProblemResponse.model_rebuild()
Error.model_rebuild()
GetMessagingActionsForOrderRequest.model_rebuild()
ConfirmCustomizationDetailsRequest.model_rebuild()
CreateConfirmDeliveryDetailsRequest.model_rebuild()
CreateLegalDisclosureRequest.model_rebuild()
CreateNegativeFeedbackRemovalRequest.model_rebuild()
CreateConfirmOrderDetailsRequest.model_rebuild()
CreateConfirmServiceDetailsRequest.model_rebuild()
CreateAmazonMotorsRequest.model_rebuild()
CreateWarrantyRequest.model_rebuild()
GetAttributesRequest.model_rebuild()
CreateDigitalAccessKeyRequest.model_rebuild()
CreateUnexpectedProblemRequest.model_rebuild()
SendInvoiceRequest.model_rebuild()
