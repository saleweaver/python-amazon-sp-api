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

BarcodeInstruction = str
"""Labeling requirements for the item. For more information about FBA labeling requirements, see the Seller Central Help for your marketplace."""


PrepGuidance = str
"""Item preparation instructions."""


PrepInstructionList = List["PrepInstruction"]
"""A list of preparation instructions to help with item sourcing decisions."""


"""
ASINPrepInstructions

Item preparation instructions to help with item sourcing decisions.
"""


class ASINPrepInstructions(SpApiBaseModel):
    """Item preparation instructions to help with item sourcing decisions."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    a_s_i_n: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ASIN", "a_s_i_n"),
            serialization_alias="ASIN",
            description="The Amazon Standard Identification Number (ASIN) of the item.",
        ),
    ]

    barcode_instruction: Annotated[
        Optional["BarcodeInstruction"],
        Field(
            None,
            validation_alias=AliasChoices("BarcodeInstruction", "barcode_instruction"),
            serialization_alias="BarcodeInstruction",
        ),
    ]

    prep_guidance: Annotated[
        Optional["PrepGuidance"],
        Field(
            None,
            validation_alias=AliasChoices("PrepGuidance", "prep_guidance"),
            serialization_alias="PrepGuidance",
        ),
    ]

    prep_instruction_list: Annotated[
        Optional["PrepInstructionList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "PrepInstructionList", "prep_instruction_list"
            ),
            serialization_alias="PrepInstructionList",
        ),
    ]


ASINPrepInstructionsList = List["ASINPrepInstructions"]
"""A list of item preparation instructions."""


"""
Address

Specific details to identify a place.
"""


class Address(SpApiBaseModel):
    """Specific details to identify a place."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("Name", "name"),
            serialization_alias="Name",
            description="Name of the individual or business.",
        ),
    ]

    address_line1: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("AddressLine1", "address_line1"),
            serialization_alias="AddressLine1",
            description="The street address information.",
        ),
    ]

    address_line2: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("AddressLine2", "address_line2"),
            serialization_alias="AddressLine2",
            description="Additional street address information, if required.",
        ),
    ]

    district_or_county: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("DistrictOrCounty", "district_or_county"),
            serialization_alias="DistrictOrCounty",
            description="The district or county.",
        ),
    ]

    city: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("City", "city"),
            serialization_alias="City",
            description="The city.",
        ),
    ]

    state_or_province_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "StateOrProvinceCode", "state_or_province_code"
            ),
            serialization_alias="StateOrProvinceCode",
            description="The state or province code. If state or province codes are used in your marketplace, it is recommended that you include one with your request. This helps Amazon to select the most appropriate Amazon fulfillment center for your inbound shipment plan.",
        ),
    ]

    country_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("CountryCode", "country_code"),
            serialization_alias="CountryCode",
            description="The country code in two-character ISO 3166-1 alpha-2 format.",
        ),
    ]

    postal_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("PostalCode", "postal_code"),
            serialization_alias="PostalCode",
            description="The postal code. If postal codes are used in your marketplace, we recommended that you include one with your request. This helps Amazon select the most appropriate Amazon fulfillment center for the inbound shipment plan.",
        ),
    ]


BigDecimalType = float
"""Number format that supports decimal."""


CurrencyCode = str
"""The currency code."""


"""
Amount

The monetary value.
"""


class Amount(SpApiBaseModel):
    """The monetary value."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    currency_code: Annotated[
        "CurrencyCode",
        Field(
            ...,
            validation_alias=AliasChoices("CurrencyCode", "currency_code"),
            serialization_alias="CurrencyCode",
        ),
    ]

    value: Annotated[
        "BigDecimalType",
        Field(
            ...,
            validation_alias=AliasChoices("Value", "value"),
            serialization_alias="Value",
            description="The amount.",
        ),
    ]


PrepInstruction = str
"""Preparation instructions for shipping an item to Amazon's fulfillment network. For more information about preparing items for shipment to Amazon's fulfillment network, see the Seller Central Help for your marketplace."""


"""
AmazonPrepFeesDetails

The fees for Amazon to prep goods for shipment.
"""


class AmazonPrepFeesDetails(SpApiBaseModel):
    """The fees for Amazon to prep goods for shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    prep_instruction: Annotated[
        Optional["PrepInstruction"],
        Field(
            None,
            validation_alias=AliasChoices("PrepInstruction", "prep_instruction"),
            serialization_alias="PrepInstruction",
        ),
    ]

    fee_per_unit: Annotated[
        Optional["Amount"],
        Field(
            None,
            validation_alias=AliasChoices("FeePerUnit", "fee_per_unit"),
            serialization_alias="FeePerUnit",
            description="The fee for Amazon to prepare 1 unit.",
        ),
    ]


AmazonPrepFeesDetailsList = List["AmazonPrepFeesDetails"]
"""A list of preparation instructions and fees for Amazon to prep goods for shipment."""


"""
BillOfLadingDownloadURL

Download URL for the bill of lading.
"""


class BillOfLadingDownloadURL(SpApiBaseModel):
    """Download URL for the bill of lading."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    download_u_r_l: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("DownloadURL", "download_u_r_l"),
            serialization_alias="DownloadURL",
            description="URL to download the bill of lading for the package. Note: The URL will only be valid for 15 seconds",
        ),
    ]


Quantity = int
"""The item quantity."""


"""
BoxContentsFeeDetails

The manual processing fee per unit and total fee for a shipment.
"""


class BoxContentsFeeDetails(SpApiBaseModel):
    """The manual processing fee per unit and total fee for a shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    total_units: Annotated[
        Optional["Quantity"],
        Field(
            None,
            validation_alias=AliasChoices("TotalUnits", "total_units"),
            serialization_alias="TotalUnits",
            description="The number of units to ship.",
        ),
    ]

    fee_per_unit: Annotated[
        Optional["Amount"],
        Field(
            None,
            validation_alias=AliasChoices("FeePerUnit", "fee_per_unit"),
            serialization_alias="FeePerUnit",
            description="The manual processing fee per unit.",
        ),
    ]

    total_fee: Annotated[
        Optional["Amount"],
        Field(
            None,
            validation_alias=AliasChoices("TotalFee", "total_fee"),
            serialization_alias="TotalFee",
            description="The total manual processing fee for the shipment.",
        ),
    ]


BoxContentsSource = str
"""Where the seller provided box contents information for a shipment."""


DateStringType = str
"""Type containing date in string format"""


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
            description="An error code that identifies the type of error that occured.",
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
            description="Additional details that can help the caller understand or fix the issue.",
        ),
    ]


ErrorList = List["Error"]
"""A list of error responses returned when a request is unsuccessful."""


ErrorReason = str
"""The reason that the ASIN is invalid."""


"""
GetBillOfLadingRequest

Request parameters for getBillOfLading
"""


class GetBillOfLadingRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getBillOfLading
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] A shipment identifier originally returned by the createInboundShipmentPlan operation.",
        ),
    ]


"""
GetBillOfLadingResponse

The response schema for the getBillOfLading operation.
"""


class GetBillOfLadingResponse(SpApiBaseModel):
    """The response schema for the getBillOfLading operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["BillOfLadingDownloadURL"],
        Field(None, description="The payload for the getBillOfLading operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


# Enum definitions
class PageTypeEnum(str, Enum):
    """Enum for PageType"""

    PACKAGE_LABEL_LETTER_2 = "PackageLabel_Letter_2"  # Two labels per US Letter label sheet. This is the only valid value for Amazon-partnered shipments in the US that use United Parcel Service (UPS) as the carrier. Supported in Canada and the US.
    PACKAGE_LABEL_LETTER_4 = "PackageLabel_Letter_4"  # Four labels per US Letter label sheet. This is the only valid value for non-Amazon-partnered shipments in the US. Supported in Canada and the US.
    PACKAGE_LABEL_LETTER_6 = "PackageLabel_Letter_6"  # Six labels per US Letter label sheet. This is the only valid value for non-Amazon-partnered shipments in the US. Supported in Canada and the US.
    PACKAGE_LABEL_LETTER_6_CARRIER_LEFT = (
        "PackageLabel_Letter_6_CarrierLeft"  # PackageLabel_Letter_6_CarrierLeft
    )
    PACKAGE_LABEL_A4_2 = "PackageLabel_A4_2"  # Two labels per A4 label sheet.
    PACKAGE_LABEL_A4_4 = "PackageLabel_A4_4"  # Four labels per A4 label sheet.
    PACKAGE_LABEL_PLAIN_PAPER = "PackageLabel_Plain_Paper"  # One label per sheet of US Letter paper. Only for non-Amazon-partnered shipments.
    PACKAGE_LABEL_PLAIN_PAPER_CARRIER_BOTTOM = "PackageLabel_Plain_Paper_CarrierBottom"  # PackageLabel_Plain_Paper_CarrierBottom
    PACKAGE_LABEL_THERMAL = "PackageLabel_Thermal"  # For use of a thermal printer. Supports Amazon-partnered shipments with UPS.
    PACKAGE_LABEL_THERMAL_UNIFIED = "PackageLabel_Thermal_Unified"  # For use of a thermal printer. Supports shipments with ATS.
    PACKAGE_LABEL_THERMAL_NON_PCP = "PackageLabel_Thermal_NonPCP"  # For use of a thermal printer. Supports non-Amazon-partnered shipments.
    PACKAGE_LABEL_THERMAL_NO_CARRIER_ROTATION = "PackageLabel_Thermal_No_Carrier_Rotation"  # For use of a thermal printer. Supports Amazon-partnered shipments with DHL.


class LabelTypeEnum(str, Enum):
    """Enum for LabelType"""

    BARCODE_2_D = "BARCODE_2D"  # This option is provided only for shipments where 2D Barcodes will be applied to all packages. Amazon strongly recommends using the UNIQUE option to get package labels instead of the BARCODE_2D option.
    UNIQUE = "UNIQUE"  # Document data for printing unique shipping labels and carrier labels for an inbound shipment.
    PALLET = "PALLET"  # Document data for printing pallet labels for a Less Than Truckload/Full Truckload (LTL/FTL) inbound shipment.


"""
GetLabelsRequest

Request parameters for getLabels
"""


class GetLabelsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getLabels
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] A shipment identifier originally returned by the createInboundShipmentPlan operation.",
        ),
    ]

    page_type: Annotated[
        PageTypeEnum,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("PageType", "page_type"),
            serialization_alias="PageType",
            description="[QUERY] The page type to use to print the labels. Submitting a PageType value that is not supported in your marketplace returns an error.",
        ),
    ]

    label_type: Annotated[
        LabelTypeEnum,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("LabelType", "label_type"),
            serialization_alias="LabelType",
            description="[QUERY] The type of labels requested. ",
        ),
    ]

    number_of_packages: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("NumberOfPackages", "number_of_packages"),
            serialization_alias="NumberOfPackages",
            description="[QUERY] The number of packages in the shipment.",
        ),
    ]

    package_labels_to_print: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "PackageLabelsToPrint", "package_labels_to_print"
            ),
            serialization_alias="PackageLabelsToPrint",
            description="[QUERY] A list of identifiers that specify packages for which you want package labels printed.  If you provide box content information with the [FBA Inbound Shipment Carton Information Feed](https://developer-docs.amazon.com/sp-api/docs/fulfillment-by-amazon-feed-type-values#fba-inbound-shipment-carton-information-feed), then `PackageLabelsToPrint` must match the `CartonId` values you provide through that feed. If you provide box content information with the Fulfillment Inbound API v2024-03-20, then `PackageLabelsToPrint` must match the `boxID` values from the [`listShipmentBoxes`](https://developer-docs.amazon.com/sp-api/docs/fulfillment-inbound-api-v2024-03-20-reference#listshipmentboxes) response. If these values do not match as required, the operation returns the `IncorrectPackageIdentifier` error code.",
        ),
    ]

    number_of_pallets: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("NumberOfPallets", "number_of_pallets"),
            serialization_alias="NumberOfPallets",
            description="[QUERY] The number of pallets in the shipment. This returns four identical labels for each pallet.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("PageSize", "page_size"),
            serialization_alias="PageSize",
            description="[QUERY] The page size for paginating through the total packages' labels. This is a required parameter for Non-Partnered LTL Shipments. Max value:1000.",
        ),
    ]

    page_start_index: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("PageStartIndex", "page_start_index"),
            serialization_alias="PageStartIndex",
            description="[QUERY] The page start index for paginating through the total packages' labels. This is a required parameter for Non-Partnered LTL Shipments.",
        ),
    ]


"""
LabelDownloadURL

Download URL for a label
"""


class LabelDownloadURL(SpApiBaseModel):
    """Download URL for a label"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    download_u_r_l: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("DownloadURL", "download_u_r_l"),
            serialization_alias="DownloadURL",
            description="URL to download the label for the package. Note: The URL will only be valid for 15 seconds",
        ),
    ]


"""
GetLabelsResponse

The response schema for the getLabels operation.
"""


class GetLabelsResponse(SpApiBaseModel):
    """The response schema for the getLabels operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["LabelDownloadURL"],
        Field(None, description="The payload for the getLabels operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


"""
GetPrepInstructionsRequest

Request parameters for getPrepInstructions
"""


class GetPrepInstructionsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getPrepInstructions
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    ship_to_country_code: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("ShipToCountryCode", "ship_to_country_code"),
            serialization_alias="ShipToCountryCode",
            description="[QUERY] The country code of the country to which the items will be shipped. Note that labeling requirements and item preparation instructions can vary by country.",
        ),
    ]

    seller_s_k_u_list: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("SellerSKUList", "seller_s_k_u_list"),
            serialization_alias="SellerSKUList",
            description="[QUERY] A list of SellerSKU values. Used to identify items for which you want labeling requirements and item preparation instructions for shipment to Amazon's fulfillment network. The SellerSKU is qualified by the Seller ID, which is included with every call to the Seller Partner API.  Note: Include seller SKUs that you have used to list items on Amazon's retail website. If you include a seller SKU that you have never used to list an item on Amazon's retail website, the seller SKU is returned in the InvalidSKUList property in the response.",
        ),
    ]

    a_s_i_n_list: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("ASINList", "a_s_i_n_list"),
            serialization_alias="ASINList",
            description="[QUERY] A list of ASIN values. Used to identify items for which you want item preparation instructions to help with item sourcing decisions.  Note: ASINs must be included in the product catalog for at least one of the marketplaces that the seller  participates in. Any ASIN that is not included in the product catalog for at least one of the marketplaces that the seller participates in is returned in the InvalidASINList property in the response. You can find out which marketplaces a seller participates in by calling the getMarketplaceParticipations operation in the Selling Partner API for Sellers.",
        ),
    ]


InvalidASINList = List["InvalidASIN"]
"""A list of invalid ASIN values and the reasons they are invalid."""


InvalidSKUList = List["InvalidSKU"]
"""A list of invalid SKU values and the reason they are invalid."""


SKUPrepInstructionsList = List["SKUPrepInstructions"]
"""A list of SKU labeling requirements and item preparation instructions."""


"""
GetPrepInstructionsResult

Result for the get prep instructions operation
"""


class GetPrepInstructionsResult(SpApiBaseModel):
    """Result for the get prep instructions operation"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    s_k_u_prep_instructions_list: Annotated[
        Optional["SKUPrepInstructionsList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "SKUPrepInstructionsList", "s_k_u_prep_instructions_list"
            ),
            serialization_alias="SKUPrepInstructionsList",
        ),
    ]

    invalid_s_k_u_list: Annotated[
        Optional["InvalidSKUList"],
        Field(
            None,
            validation_alias=AliasChoices("InvalidSKUList", "invalid_s_k_u_list"),
            serialization_alias="InvalidSKUList",
        ),
    ]

    a_s_i_n_prep_instructions_list: Annotated[
        Optional["ASINPrepInstructionsList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ASINPrepInstructionsList", "a_s_i_n_prep_instructions_list"
            ),
            serialization_alias="ASINPrepInstructionsList",
        ),
    ]

    invalid_a_s_i_n_list: Annotated[
        Optional["InvalidASINList"],
        Field(
            None,
            validation_alias=AliasChoices("InvalidASINList", "invalid_a_s_i_n_list"),
            serialization_alias="InvalidASINList",
        ),
    ]


"""
GetPrepInstructionsResponse

The response schema for the getPrepInstructions operation.
"""


class GetPrepInstructionsResponse(SpApiBaseModel):
    """The response schema for the getPrepInstructions operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["GetPrepInstructionsResult"],
        Field(None, description="The payload for the getPrepInstructions operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


"""
GetShipmentItemsByShipmentIdRequest

Request parameters for getShipmentItemsByShipmentId
"""


class GetShipmentItemsByShipmentIdRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getShipmentItemsByShipmentId
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] A shipment identifier used for selecting items in a specific inbound shipment.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceId", "marketplace_id"),
            serialization_alias="MarketplaceId",
            description="[QUERY] Deprecated. Do not use.",
        ),
    ]


# Enum definitions
class QueryTypeEnum(str, Enum):
    """Enum for QueryType"""

    DATE_RANGE = "DATE_RANGE"  # Returns items based on the date range information provided by the LastUpdatedAfter and LastUpdatedBefore parameters.
    NEXT_TOKEN = "NEXT_TOKEN"  # Returns items by using NextToken to continue returning items specified in a previous request.


"""
GetShipmentItemsRequest

Request parameters for getShipmentItems
"""


class GetShipmentItemsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getShipmentItems
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    last_updated_after: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("LastUpdatedAfter", "last_updated_after"),
            serialization_alias="LastUpdatedAfter",
            description="[QUERY] A date used for selecting inbound shipment items that were last updated after (or at) a specified time. The selection includes updates made by Amazon and by the seller.",
        ),
    ]

    last_updated_before: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("LastUpdatedBefore", "last_updated_before"),
            serialization_alias="LastUpdatedBefore",
            description="[QUERY] A date used for selecting inbound shipment items that were last updated before (or at) a specified time. The selection includes updates made by Amazon and by the seller.",
        ),
    ]

    query_type: Annotated[
        QueryTypeEnum,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("QueryType", "query_type"),
            serialization_alias="QueryType",
            description="[QUERY] Indicates whether items are returned using a date range (by providing the LastUpdatedAfter and LastUpdatedBefore parameters), or using NextToken, which continues returning items specified in a previous request.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("NextToken", "next_token"),
            serialization_alias="NextToken",
            description="[QUERY] A string token returned in the response to your previous request.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceId", "marketplace_id"),
            serialization_alias="MarketplaceId",
            description="[QUERY] A marketplace identifier. Specifies the marketplace where the product would be stored.",
        ),
    ]


InboundShipmentItemList = List["InboundShipmentItem"]
"""A list of inbound shipment item information."""


"""
GetShipmentItemsResult

Result for the get shipment items operation
"""


class GetShipmentItemsResult(SpApiBaseModel):
    """Result for the get shipment items operation"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    item_data: Annotated[
        Optional["InboundShipmentItemList"],
        Field(
            None,
            validation_alias=AliasChoices("ItemData", "item_data"),
            serialization_alias="ItemData",
            description="A list of item information for an inbound shipment.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("NextToken", "next_token"),
            serialization_alias="NextToken",
            description="When present and not empty, pass this string token in the next request to return the next response page.",
        ),
    ]


"""
GetShipmentItemsResponse

The response schema for the getShipmentItems operation.
"""


class GetShipmentItemsResponse(SpApiBaseModel):
    """The response schema for the getShipmentItems operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["GetShipmentItemsResult"],
        Field(None, description="The payload for the getShipmentItems operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


# Enum definitions
class ShipmentStatusListEnum(str, Enum):
    """Enum for ShipmentStatusList"""

    WORKING = (
        "WORKING"  # The shipment was created by the seller, but has not yet shipped.
    )
    READY_TO_SHIP = "READY_TO_SHIP"  # The seller has printed box labels (for Small parcel shipments) or pallet labels (for Less Than Truckload shipments).
    SHIPPED = "SHIPPED"  # The shipment was picked up by the carrier.
    RECEIVING = "RECEIVING"  # The shipment has arrived at the fulfillment center, but not all items have been marked as received.
    CANCELLED = "CANCELLED"  # The shipment was cancelled by the seller after the shipment was sent to the fulfillment center.
    DELETED = "DELETED"  # The shipment was cancelled by the seller before the shipment was sent to the  fulfillment center.
    CLOSED = "CLOSED"  # The shipment has arrived at the fulfillment center and all items have been marked as received.
    ERROR = "ERROR"  # There was an error with the shipment and it was not processed by Amazon.
    IN_TRANSIT = "IN_TRANSIT"  # The carrier has notified the fulfillment center that it is aware of the shipment.
    DELIVERED = "DELIVERED"  # The shipment was delivered by the carrier to the fulfillment center.
    CHECKED_IN = "CHECKED_IN"  # The shipment was checked-in at the receiving dock of the fulfillment center.


class QueryTypeEnum(str, Enum):
    """Enum for QueryType"""

    DATE_RANGE = "DATE_RANGE"  # Returns items based on the date range information provided by the LastUpdatedAfter and LastUpdatedBefore parameters.
    NEXT_TOKEN = "NEXT_TOKEN"  # Returns items by using NextToken to continue returning items specified in a previous request.


"""
GetShipmentsRequest

Request parameters for getShipments
"""


class GetShipmentsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getShipments
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_status_list: Annotated[
        Optional[List["ShipmentStatusListEnum"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("ShipmentStatusList", "shipment_status_list"),
            serialization_alias="ShipmentStatusList",
            description="[QUERY] A list of ShipmentStatus values. Used to select shipments with a current status that matches the status values that you specify.",
        ),
    ]

    shipment_id_list: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("ShipmentIdList", "shipment_id_list"),
            serialization_alias="ShipmentIdList",
            description="[QUERY] A list of shipment IDs used to select the shipments that you want. If both ShipmentStatusList and ShipmentIdList are specified, only shipments that match both parameters are returned.",
        ),
    ]

    last_updated_after: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("LastUpdatedAfter", "last_updated_after"),
            serialization_alias="LastUpdatedAfter",
            description="[QUERY] A date used for selecting inbound shipments that were last updated after (or at) a specified time. The selection includes updates made by Amazon and by the seller.",
        ),
    ]

    last_updated_before: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("LastUpdatedBefore", "last_updated_before"),
            serialization_alias="LastUpdatedBefore",
            description="[QUERY] A date used for selecting inbound shipments that were last updated before (or at) a specified time. The selection includes updates made by Amazon and by the seller.",
        ),
    ]

    query_type: Annotated[
        QueryTypeEnum,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("QueryType", "query_type"),
            serialization_alias="QueryType",
            description="[QUERY] Indicates whether shipments are returned using shipment information (by providing the ShipmentStatusList or ShipmentIdList parameters), using a date range (by providing the LastUpdatedAfter and LastUpdatedBefore parameters), or by using NextToken to continue returning items specified in a previous request.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("NextToken", "next_token"),
            serialization_alias="NextToken",
            description="[QUERY] A string token returned in the response to your previous request.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceId", "marketplace_id"),
            serialization_alias="MarketplaceId",
            description="[QUERY] A marketplace identifier. Specifies the marketplace where the product would be stored.",
        ),
    ]


InboundShipmentList = List["InboundShipmentInfo"]
"""A list of inbound shipment information."""


"""
GetShipmentsResult

Result for the get shipments operation
"""


class GetShipmentsResult(SpApiBaseModel):
    """Result for the get shipments operation"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_data: Annotated[
        Optional["InboundShipmentList"],
        Field(
            None,
            validation_alias=AliasChoices("ShipmentData", "shipment_data"),
            serialization_alias="ShipmentData",
            description="Information about your inbound shipments.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("NextToken", "next_token"),
            serialization_alias="NextToken",
            description="When present and not empty, pass this string token in the next request to return the next response page.",
        ),
    ]


"""
GetShipmentsResponse

The response schema for the getShipments operation.
"""


class GetShipmentsResponse(SpApiBaseModel):
    """The response schema for the getShipments operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["GetShipmentsResult"],
        Field(None, description="The payload for the getShipments operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


LabelPrepType = str
"""The type of label preparation that is required for the inbound shipment."""


ShipmentStatus = str
"""Indicates the status of the inbound shipment. When used with the createInboundShipment operation, WORKING is the only valid value. When used with the updateInboundShipment operation, possible values are WORKING, SHIPPED or CANCELLED."""


"""
InboundShipmentInfo

Information about the seller's inbound shipments. Returned by the listInboundShipments operation.
"""


class InboundShipmentInfo(SpApiBaseModel):
    """Information about the seller's inbound shipments. Returned by the listInboundShipments operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ShipmentId", "shipment_id"),
            serialization_alias="ShipmentId",
            description="The shipment identifier submitted in the request.",
        ),
    ]

    shipment_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ShipmentName", "shipment_name"),
            serialization_alias="ShipmentName",
            description="The name for the inbound shipment.",
        ),
    ]

    ship_from_address: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("ShipFromAddress", "ship_from_address"),
            serialization_alias="ShipFromAddress",
            description="The return address.",
        ),
    ]

    destination_fulfillment_center_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "DestinationFulfillmentCenterId", "destination_fulfillment_center_id"
            ),
            serialization_alias="DestinationFulfillmentCenterId",
            description="An Amazon fulfillment center identifier created by Amazon.",
        ),
    ]

    shipment_status: Annotated[
        Optional["ShipmentStatus"],
        Field(
            None,
            validation_alias=AliasChoices("ShipmentStatus", "shipment_status"),
            serialization_alias="ShipmentStatus",
        ),
    ]

    label_prep_type: Annotated[
        Optional["LabelPrepType"],
        Field(
            None,
            validation_alias=AliasChoices("LabelPrepType", "label_prep_type"),
            serialization_alias="LabelPrepType",
        ),
    ]

    are_cases_required: Annotated[
        bool,
        Field(
            ...,
            validation_alias=AliasChoices("AreCasesRequired", "are_cases_required"),
            serialization_alias="AreCasesRequired",
            description="Indicates whether or not an inbound shipment contains case-packed boxes. When AreCasesRequired = true for an inbound shipment, all items in the inbound shipment must be case packed.",
        ),
    ]

    confirmed_need_by_date: Annotated[
        Optional["DateStringType"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ConfirmedNeedByDate", "confirmed_need_by_date"
            ),
            serialization_alias="ConfirmedNeedByDate",
            description="Date by which the shipment must arrive at the Amazon fulfillment center to avoid delivery promise breaks for pre-ordered items.",
        ),
    ]

    box_contents_source: Annotated[
        Optional["BoxContentsSource"],
        Field(
            None,
            validation_alias=AliasChoices("BoxContentsSource", "box_contents_source"),
            serialization_alias="BoxContentsSource",
        ),
    ]

    estimated_box_contents_fee: Annotated[
        Optional["BoxContentsFeeDetails"],
        Field(
            None,
            validation_alias=AliasChoices(
                "EstimatedBoxContentsFee", "estimated_box_contents_fee"
            ),
            serialization_alias="EstimatedBoxContentsFee",
            description="An estimate of the manual processing fee charged by Amazon for boxes without box content information. This is only returned when BoxContentsSource is NONE.",
        ),
    ]


PrepDetailsList = List["PrepDetails"]
"""A list of preparation instructions and who is responsible for that preparation."""


"""
InboundShipmentItem

Item information for an inbound shipment. Submitted with a call to the createInboundShipment or updateInboundShipment operation.
"""


class InboundShipmentItem(SpApiBaseModel):
    """Item information for an inbound shipment. Submitted with a call to the createInboundShipment or updateInboundShipment operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ShipmentId", "shipment_id"),
            serialization_alias="ShipmentId",
            description="A shipment identifier originally returned by the createInboundShipmentPlan operation.",
        ),
    ]

    seller_s_k_u: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("SellerSKU", "seller_s_k_u"),
            serialization_alias="SellerSKU",
            description="The seller SKU of the item.",
        ),
    ]

    fulfillment_network_s_k_u: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "FulfillmentNetworkSKU", "fulfillment_network_s_k_u"
            ),
            serialization_alias="FulfillmentNetworkSKU",
            description="Amazon's fulfillment network SKU of the item.",
        ),
    ]

    quantity_shipped: Annotated[
        "Quantity",
        Field(
            ...,
            validation_alias=AliasChoices("QuantityShipped", "quantity_shipped"),
            serialization_alias="QuantityShipped",
            description="The item quantity that you are shipping.",
        ),
    ]

    quantity_received: Annotated[
        Optional["Quantity"],
        Field(
            None,
            validation_alias=AliasChoices("QuantityReceived", "quantity_received"),
            serialization_alias="QuantityReceived",
            description="The item quantity that has been received at an Amazon fulfillment center.",
        ),
    ]

    quantity_in_case: Annotated[
        Optional["Quantity"],
        Field(
            None,
            validation_alias=AliasChoices("QuantityInCase", "quantity_in_case"),
            serialization_alias="QuantityInCase",
            description="The item quantity in each case, for case-packed items. Note that QuantityInCase multiplied by the number of boxes in the inbound shipment equals QuantityShipped. Also note that all of the boxes of an inbound shipment must either be case packed or individually packed. For that reason, when you submit the createInboundShipment or the updateInboundShipment operation, the value of QuantityInCase must be provided for every item in the shipment or for none of the items in the shipment.",
        ),
    ]

    release_date: Annotated[
        Optional["DateStringType"],
        Field(
            None,
            validation_alias=AliasChoices("ReleaseDate", "release_date"),
            serialization_alias="ReleaseDate",
            description="The date that a pre-order item will be available for sale.",
        ),
    ]

    prep_details_list: Annotated[
        Optional["PrepDetailsList"],
        Field(
            None,
            validation_alias=AliasChoices("PrepDetailsList", "prep_details_list"),
            serialization_alias="PrepDetailsList",
        ),
    ]


"""
InvalidASIN

Contains details about an invalid ASIN
"""


class InvalidASIN(SpApiBaseModel):
    """Contains details about an invalid ASIN"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    a_s_i_n: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ASIN", "a_s_i_n"),
            serialization_alias="ASIN",
            description="The Amazon Standard Identification Number (ASIN) of the item.",
        ),
    ]

    error_reason: Annotated[
        Optional["ErrorReason"],
        Field(
            None,
            validation_alias=AliasChoices("ErrorReason", "error_reason"),
            serialization_alias="ErrorReason",
            description="The reason that the ASIN is invalid.",
        ),
    ]


"""
InvalidSKU

Contains detail about an invalid SKU
"""


class InvalidSKU(SpApiBaseModel):
    """Contains detail about an invalid SKU"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_s_k_u: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SellerSKU", "seller_s_k_u"),
            serialization_alias="SellerSKU",
            description="The seller SKU of the item.",
        ),
    ]

    error_reason: Annotated[
        Optional["ErrorReason"],
        Field(
            None,
            validation_alias=AliasChoices("ErrorReason", "error_reason"),
            serialization_alias="ErrorReason",
            description="The reason why the seller SKU is invalid.",
        ),
    ]


PrepOwner = str
"""Indicates who will prepare the item."""


"""
PrepDetails

Preparation instructions and who is responsible for the preparation.
"""


class PrepDetails(SpApiBaseModel):
    """Preparation instructions and who is responsible for the preparation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    prep_instruction: Annotated[
        "PrepInstruction",
        Field(
            ...,
            validation_alias=AliasChoices("PrepInstruction", "prep_instruction"),
            serialization_alias="PrepInstruction",
        ),
    ]

    prep_owner: Annotated[
        "PrepOwner",
        Field(
            ...,
            validation_alias=AliasChoices("PrepOwner", "prep_owner"),
            serialization_alias="PrepOwner",
        ),
    ]


"""
SKUPrepInstructions

Labeling requirements and item preparation instructions to help you prepare items for shipment to Amazon's fulfillment network.
"""


class SKUPrepInstructions(SpApiBaseModel):
    """Labeling requirements and item preparation instructions to help you prepare items for shipment to Amazon's fulfillment network."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_s_k_u: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SellerSKU", "seller_s_k_u"),
            serialization_alias="SellerSKU",
            description="The seller SKU of the item.",
        ),
    ]

    a_s_i_n: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ASIN", "a_s_i_n"),
            serialization_alias="ASIN",
            description="The Amazon Standard Identification Number (ASIN) of the item.",
        ),
    ]

    barcode_instruction: Annotated[
        Optional["BarcodeInstruction"],
        Field(
            None,
            validation_alias=AliasChoices("BarcodeInstruction", "barcode_instruction"),
            serialization_alias="BarcodeInstruction",
        ),
    ]

    prep_guidance: Annotated[
        Optional["PrepGuidance"],
        Field(
            None,
            validation_alias=AliasChoices("PrepGuidance", "prep_guidance"),
            serialization_alias="PrepGuidance",
        ),
    ]

    prep_instruction_list: Annotated[
        Optional["PrepInstructionList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "PrepInstructionList", "prep_instruction_list"
            ),
            serialization_alias="PrepInstructionList",
        ),
    ]

    amazon_prep_fees_details_list: Annotated[
        Optional["AmazonPrepFeesDetailsList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "AmazonPrepFeesDetailsList", "amazon_prep_fees_details_list"
            ),
            serialization_alias="AmazonPrepFeesDetailsList",
        ),
    ]


# Rebuild models to resolve forward references
Error.model_rebuild()
ASINPrepInstructions.model_rebuild()
Address.model_rebuild()
AmazonPrepFeesDetails.model_rebuild()
Amount.model_rebuild()
BoxContentsFeeDetails.model_rebuild()
GetBillOfLadingResponse.model_rebuild()
LabelDownloadURL.model_rebuild()
BillOfLadingDownloadURL.model_rebuild()
GetLabelsResponse.model_rebuild()
GetPrepInstructionsResult.model_rebuild()
GetPrepInstructionsResponse.model_rebuild()
InboundShipmentInfo.model_rebuild()
InboundShipmentItem.model_rebuild()
InvalidASIN.model_rebuild()
InvalidSKU.model_rebuild()
GetShipmentItemsResult.model_rebuild()
GetShipmentItemsResponse.model_rebuild()
GetShipmentsResult.model_rebuild()
GetShipmentsResponse.model_rebuild()
PrepDetails.model_rebuild()
SKUPrepInstructions.model_rebuild()
GetPrepInstructionsRequest.model_rebuild()
GetLabelsRequest.model_rebuild()
GetBillOfLadingRequest.model_rebuild()
GetShipmentsRequest.model_rebuild()
GetShipmentItemsByShipmentIdRequest.model_rebuild()
GetShipmentItemsRequest.model_rebuild()
