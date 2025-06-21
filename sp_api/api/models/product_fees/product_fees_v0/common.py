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


"""


class Error(SpApiBaseModel):
    """"""

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


IncludedFeeDetailList = List["IncludedFeeDetail"]
"""A list of other fees that contribute to a given fee."""


"""
MoneyType


"""


class MoneyType(SpApiBaseModel):
    """"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    currency_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("CurrencyCode", "currency_code"),
            serialization_alias="CurrencyCode",
            description="The currency code in ISO 4217 format.",
        ),
    ]

    amount: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices("Amount", "amount"),
            serialization_alias="Amount",
            description="The monetary value.",
        ),
    ]


"""
FeeDetail

The type of fee, fee amount, and other details.
"""


class FeeDetail(SpApiBaseModel):
    """The type of fee, fee amount, and other details."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    fee_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("FeeType", "fee_type"),
            serialization_alias="FeeType",
            description="The type of fee charged to a seller.",
        ),
    ]

    fee_amount: Annotated[
        "MoneyType",
        Field(
            ...,
            validation_alias=AliasChoices("FeeAmount", "fee_amount"),
            serialization_alias="FeeAmount",
            description="The amount charged for a given fee.",
        ),
    ]

    fee_promotion: Annotated[
        Optional["MoneyType"],
        Field(
            None,
            validation_alias=AliasChoices("FeePromotion", "fee_promotion"),
            serialization_alias="FeePromotion",
            description="The promotion amount for a given fee.",
        ),
    ]

    tax_amount: Annotated[
        Optional["MoneyType"],
        Field(
            None,
            validation_alias=AliasChoices("TaxAmount", "tax_amount"),
            serialization_alias="TaxAmount",
            description="The tax amount for a given fee.",
        ),
    ]

    final_fee: Annotated[
        "MoneyType",
        Field(
            ...,
            validation_alias=AliasChoices("FinalFee", "final_fee"),
            serialization_alias="FinalFee",
            description="The final fee amount for a given fee.",
        ),
    ]

    included_fee_detail_list: Annotated[
        Optional["IncludedFeeDetailList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "IncludedFeeDetailList", "included_fee_detail_list"
            ),
            serialization_alias="IncludedFeeDetailList",
        ),
    ]


FeeDetailList = List["FeeDetail"]
"""A list of other fees that contribute to a given fee."""


"""
FeesEstimate

The total estimated fees for an item and a list of details.
"""


class FeesEstimate(SpApiBaseModel):
    """The total estimated fees for an item and a list of details."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    time_of_fees_estimation: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices(
                "TimeOfFeesEstimation", "time_of_fees_estimation"
            ),
            serialization_alias="TimeOfFeesEstimation",
            description="The time at which the fees were estimated. This defaults to the time the request is made.",
        ),
    ]

    total_fees_estimate: Annotated[
        Optional["MoneyType"],
        Field(
            None,
            validation_alias=AliasChoices("TotalFeesEstimate", "total_fees_estimate"),
            serialization_alias="TotalFeesEstimate",
            description="Total estimated fees for a given item, price, and fulfillment channel.",
        ),
    ]

    fee_detail_list: Annotated[
        Optional["FeeDetailList"],
        Field(
            None,
            validation_alias=AliasChoices("FeeDetailList", "fee_detail_list"),
            serialization_alias="FeeDetailList",
        ),
    ]


OptionalFulfillmentProgram = str
"""An optional enrollment program to return the estimated fees when the offer is fulfilled by Amazon (IsAmazonFulfilled is set to true)."""


"""
Points


"""


class Points(SpApiBaseModel):
    """"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    points_number: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("PointsNumber", "points_number"),
            serialization_alias="PointsNumber",
        ),
    ]

    points_monetary_value: Annotated[
        Optional["MoneyType"],
        Field(
            None,
            validation_alias=AliasChoices(
                "PointsMonetaryValue", "points_monetary_value"
            ),
            serialization_alias="PointsMonetaryValue",
        ),
    ]


"""
PriceToEstimateFees

Price information for an item, used to estimate fees.
"""


class PriceToEstimateFees(SpApiBaseModel):
    """Price information for an item, used to estimate fees."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    listing_price: Annotated[
        "MoneyType",
        Field(
            ...,
            validation_alias=AliasChoices("ListingPrice", "listing_price"),
            serialization_alias="ListingPrice",
            description="The price of the item.",
        ),
    ]

    shipping: Annotated[
        Optional["MoneyType"],
        Field(
            None,
            validation_alias=AliasChoices("Shipping", "shipping"),
            serialization_alias="Shipping",
            description="The shipping cost.",
        ),
    ]

    points: Annotated[
        Optional["Points"],
        Field(
            None,
            validation_alias=AliasChoices("Points", "points"),
            serialization_alias="Points",
            description="The number of Amazon Points offered with the purchase of an item.",
        ),
    ]


"""
FeesEstimateRequestBody

A product, marketplace, and proposed price used to request estimated fees.
"""


class FeesEstimateRequestBody(SpApiBaseModel):
    """A product, marketplace, and proposed price used to request estimated fees."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceId", "marketplace_id"),
            serialization_alias="MarketplaceId",
            description="A marketplace identifier.",
        ),
    ]

    is_amazon_fulfilled: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("IsAmazonFulfilled", "is_amazon_fulfilled"),
            serialization_alias="IsAmazonFulfilled",
            description="When true, the offer is fulfilled by Amazon.",
        ),
    ]

    price_to_estimate_fees: Annotated[
        "PriceToEstimateFees",
        Field(
            ...,
            validation_alias=AliasChoices(
                "PriceToEstimateFees", "price_to_estimate_fees"
            ),
            serialization_alias="PriceToEstimateFees",
            description="The product price that the fee estimate is based on.",
        ),
    ]

    identifier: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("Identifier", "identifier"),
            serialization_alias="Identifier",
            description="A unique identifier provided by the caller to track this request.",
        ),
    ]

    optional_fulfillment_program: Annotated[
        Optional["OptionalFulfillmentProgram"],
        Field(
            None,
            validation_alias=AliasChoices(
                "OptionalFulfillmentProgram", "optional_fulfillment_program"
            ),
            serialization_alias="OptionalFulfillmentProgram",
        ),
    ]


IdType = str
"""The type of product identifier used in a `FeesEstimateByIdRequest`."""


"""
FeesEstimateByIdRequestBody

A product, marketplace, and proposed price used to request estimated fees.
"""


class FeesEstimateByIdRequestBody(SpApiBaseModel):
    """A product, marketplace, and proposed price used to request estimated fees."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    fees_estimate_request_body: Annotated[
        Optional["FeesEstimateRequestBody"],
        Field(
            None,
            validation_alias=AliasChoices(
                "FeesEstimateRequestBody", "fees_estimate_request_body"
            ),
            serialization_alias="FeesEstimateRequestBody",
        ),
    ]

    id_type: Annotated[
        "IdType",
        Field(
            ...,
            validation_alias=AliasChoices("IdType", "id_type"),
            serialization_alias="IdType",
        ),
    ]

    id_value: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("IdValue", "id_value"),
            serialization_alias="IdValue",
            description="The item identifier.",
        ),
    ]


"""
FeesEstimateErrorDetail

Additional information that can help the caller understand or fix the issue.
"""


class FeesEstimateErrorDetail(SpApiBaseModel):
    """Additional information that can help the caller understand or fix the issue."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
FeesEstimateError

An unexpected error occurred during this operation.
"""


class FeesEstimateError(SpApiBaseModel):
    """An unexpected error occurred during this operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("Type", "type"),
            serialization_alias="Type",
            description="An error type, identifying either the receiver or the sender as the originator of the error.",
        ),
    ]

    code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("Code", "code"),
            serialization_alias="Code",
            description="An error code that identifies the type of error that occurred.",
        ),
    ]

    message: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("Message", "message"),
            serialization_alias="Message",
            description="A message that describes the error condition.",
        ),
    ]

    detail: Annotated[
        "FeesEstimateErrorDetail",
        Field(
            ...,
            validation_alias=AliasChoices("Detail", "detail"),
            serialization_alias="Detail",
        ),
    ]


"""
FeesEstimateIdentifier

An item identifier, marketplace, time of request, and other details that identify an estimate.
"""


class FeesEstimateIdentifier(SpApiBaseModel):
    """An item identifier, marketplace, time of request, and other details that identify an estimate."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceId", "marketplace_id"),
            serialization_alias="MarketplaceId",
            description="A marketplace identifier.",
        ),
    ]

    seller_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SellerId", "seller_id"),
            serialization_alias="SellerId",
            description="The seller identifier.",
        ),
    ]

    id_type: Annotated[
        Optional["IdType"],
        Field(
            None,
            validation_alias=AliasChoices("IdType", "id_type"),
            serialization_alias="IdType",
        ),
    ]

    id_value: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("IdValue", "id_value"),
            serialization_alias="IdValue",
            description="The item identifier.",
        ),
    ]

    is_amazon_fulfilled: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("IsAmazonFulfilled", "is_amazon_fulfilled"),
            serialization_alias="IsAmazonFulfilled",
            description="When true, the offer is fulfilled by Amazon.",
        ),
    ]

    price_to_estimate_fees: Annotated[
        Optional["PriceToEstimateFees"],
        Field(
            None,
            validation_alias=AliasChoices(
                "PriceToEstimateFees", "price_to_estimate_fees"
            ),
            serialization_alias="PriceToEstimateFees",
            description="The item price on which the fee estimate is based.",
        ),
    ]

    seller_input_identifier: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "SellerInputIdentifier", "seller_input_identifier"
            ),
            serialization_alias="SellerInputIdentifier",
            description="A unique identifier provided by the caller to track this request.",
        ),
    ]

    optional_fulfillment_program: Annotated[
        Optional["OptionalFulfillmentProgram"],
        Field(
            None,
            validation_alias=AliasChoices(
                "OptionalFulfillmentProgram", "optional_fulfillment_program"
            ),
            serialization_alias="OptionalFulfillmentProgram",
        ),
    ]


"""
FeesEstimateResult

An item identifier and the estimated fees for the item.
"""


class FeesEstimateResult(SpApiBaseModel):
    """An item identifier and the estimated fees for the item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    status: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("Status", "status"),
            serialization_alias="Status",
            description="The status of the fee request. Possible values: Success, ClientError, ServiceError.",
        ),
    ]

    fees_estimate_identifier: Annotated[
        Optional["FeesEstimateIdentifier"],
        Field(
            None,
            validation_alias=AliasChoices(
                "FeesEstimateIdentifier", "fees_estimate_identifier"
            ),
            serialization_alias="FeesEstimateIdentifier",
            description="Information used to identify a fees estimate request.",
        ),
    ]

    fees_estimate: Annotated[
        Optional["FeesEstimate"],
        Field(
            None,
            validation_alias=AliasChoices("FeesEstimate", "fees_estimate"),
            serialization_alias="FeesEstimate",
            description="The total estimated fees for an item and a list of details.",
        ),
    ]

    error: Annotated[
        Optional["FeesEstimateError"],
        Field(
            None,
            validation_alias=AliasChoices("Error", "error"),
            serialization_alias="Error",
            description="An error object with a type, code, and message.",
        ),
    ]


"""
GetMyFeesEstimateRequestBody

RequestBody schema.
"""


class GetMyFeesEstimateRequestBody(SpApiBaseModel):
    """RequestBody schema."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    fees_estimate_request_body: Annotated[
        Optional["FeesEstimateRequestBody"],
        Field(
            None,
            validation_alias=AliasChoices(
                "FeesEstimateRequestBody", "fees_estimate_request_body"
            ),
            serialization_alias="FeesEstimateRequestBody",
        ),
    ]


"""
GetMyFeesEstimateForASINRequest

Request parameters for getMyFeesEstimateForASIN
"""


class GetMyFeesEstimateForASINRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getMyFeesEstimateForASIN
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "GetMyFeesEstimateRequestBody",
        BodyParam(),
        Field(..., description="[BODY] Parameter"),
    ]

    asin: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("Asin", "asin"),
            serialization_alias="Asin",
            description="[PATH] The Amazon Standard Identification Number (ASIN) of the item.",
        ),
    ]


"""
GetMyFeesEstimateForSKURequest

Request parameters for getMyFeesEstimateForSKU
"""


class GetMyFeesEstimateForSKURequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getMyFeesEstimateForSKU
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "GetMyFeesEstimateRequestBody",
        BodyParam(),
        Field(..., description="[BODY] Parameter"),
    ]

    seller_s_k_u: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("SellerSKU", "seller_s_k_u"),
            serialization_alias="SellerSKU",
            description="[PATH] Used to identify an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.",
        ),
    ]


"""
GetMyFeesEstimateResult

Response schema.
"""


class GetMyFeesEstimateResult(SpApiBaseModel):
    """Response schema."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    fees_estimate_result: Annotated[
        Optional["FeesEstimateResult"],
        Field(
            None,
            validation_alias=AliasChoices("FeesEstimateResult", "fees_estimate_result"),
            serialization_alias="FeesEstimateResult",
            description="The item's estimated fees.",
        ),
    ]


"""
GetMyFeesEstimateResponse


"""


class GetMyFeesEstimateResponse(SpApiBaseModel):
    """"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["GetMyFeesEstimateResult"],
        Field(None, description="The payload for the operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


"""
GetMyFeesEstimatesErrorList

A list of error responses returned when a request is unsuccessful.
"""


class GetMyFeesEstimatesErrorList(SpApiBaseModel):
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


GetMyFeesEstimatesRequestBody = List["FeesEstimateByIdRequestBody"]
"""RequestBody for estimated fees for a list of products."""


"""
GetMyFeesEstimatesRequest

Request parameters for getMyFeesEstimates
"""


class GetMyFeesEstimatesRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getMyFeesEstimates
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "GetMyFeesEstimatesRequestBody",
        BodyParam(),
        Field(..., description="[BODY] Parameter"),
    ]


GetMyFeesEstimatesResponse = List["FeesEstimateResult"]
"""Estimated fees for a list of products."""


"""
IncludedFeeDetail

The type of fee, fee amount, and other details.
"""


class IncludedFeeDetail(SpApiBaseModel):
    """The type of fee, fee amount, and other details."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    fee_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("FeeType", "fee_type"),
            serialization_alias="FeeType",
            description="The type of fee charged to a seller.",
        ),
    ]

    fee_amount: Annotated[
        "MoneyType",
        Field(
            ...,
            validation_alias=AliasChoices("FeeAmount", "fee_amount"),
            serialization_alias="FeeAmount",
            description="The amount charged for a given fee.",
        ),
    ]

    fee_promotion: Annotated[
        Optional["MoneyType"],
        Field(
            None,
            validation_alias=AliasChoices("FeePromotion", "fee_promotion"),
            serialization_alias="FeePromotion",
            description="The promotion amount for a given fee.",
        ),
    ]

    tax_amount: Annotated[
        Optional["MoneyType"],
        Field(
            None,
            validation_alias=AliasChoices("TaxAmount", "tax_amount"),
            serialization_alias="TaxAmount",
            description="The tax amount for a given fee.",
        ),
    ]

    final_fee: Annotated[
        "MoneyType",
        Field(
            ...,
            validation_alias=AliasChoices("FinalFee", "final_fee"),
            serialization_alias="FinalFee",
            description="The final fee amount for a given fee.",
        ),
    ]


# Rebuild models to resolve forward references
GetMyFeesEstimateRequestBody.model_rebuild()
FeesEstimateByIdRequestBody.model_rebuild()
FeesEstimateRequestBody.model_rebuild()
GetMyFeesEstimateResponse.model_rebuild()
GetMyFeesEstimateResult.model_rebuild()
Points.model_rebuild()
GetMyFeesEstimatesErrorList.model_rebuild()
Error.model_rebuild()
FeesEstimateResult.model_rebuild()
FeesEstimateIdentifier.model_rebuild()
PriceToEstimateFees.model_rebuild()
FeesEstimate.model_rebuild()
FeesEstimateError.model_rebuild()
FeesEstimateErrorDetail.model_rebuild()
FeeDetail.model_rebuild()
IncludedFeeDetail.model_rebuild()
MoneyType.model_rebuild()
GetMyFeesEstimateForSKURequest.model_rebuild()
GetMyFeesEstimateForASINRequest.model_rebuild()
GetMyFeesEstimatesRequest.model_rebuild()
