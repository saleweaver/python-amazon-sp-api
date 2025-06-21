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
AttributeOption

The definition of the attribute option.
"""


class AttributeOption(SpApiBaseModel):
    """The definition of the attribute option."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    description: Annotated[
        Optional[str],
        Field(None, description="The description of the attribute value."),
    ]

    value: Annotated[
        Optional[str],
        Field(None, description="The possible values for the attribute option."),
    ]


FileFormat = str
"""Supported invoice file extensions."""


"""
TransactionIdentifier

The identifier for a transaction.
"""


class TransactionIdentifier(SpApiBaseModel):
    """The identifier for a transaction."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[
        Optional[str],
        Field(
            None,
            description="The transaction identifier name. Use the `getInvoicesAttributes` operation to check `transactionIdentifierName` options.",
        ),
    ]

    id: Annotated[Optional[str], Field(None, description="The transaction identifier.")]


"""
ExportInvoicesRequestBody

The information required to create the export request.
"""


class ExportInvoicesRequestBody(SpApiBaseModel):
    """The information required to create the export request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    date_end: Annotated[
        Optional[date],
        Field(
            None,
            validation_alias=AliasChoices("dateEnd", "date_end"),
            serialization_alias="dateEnd",
            description="The latest invoice creation date for invoices that you want to include in the response. Dates are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default is the time of the request.",
        ),
    ]

    date_start: Annotated[
        Optional[date],
        Field(
            None,
            validation_alias=AliasChoices("dateStart", "date_start"),
            serialization_alias="dateStart",
            description="The earliest invoice creation date for invoices that you want to include in the response. Dates are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default is 24 hours prior to the time of the request.",
        ),
    ]

    external_invoice_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("externalInvoiceId", "external_invoice_id"),
            serialization_alias="externalInvoiceId",
            description="The external ID of the invoices you want included in the response.",
        ),
    ]

    file_format: Annotated[
        Optional["FileFormat"],
        Field(
            None,
            validation_alias=AliasChoices("fileFormat", "file_format"),
            serialization_alias="fileFormat",
        ),
    ]

    invoice_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("invoiceType", "invoice_type"),
            serialization_alias="invoiceType",
            description="The marketplace-specific classification of the invoice type. Use the `getInvoicesAttributes` operation to check `invoiceType` options.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The ID of the marketplace from which you want the invoices.",
        ),
    ]

    series: Annotated[
        Optional[str],
        Field(
            None,
            description="The series number of the invoices you want included in the response.",
        ),
    ]

    statuses: Annotated[
        Optional[List["str"]],
        Field(
            None,
            description="A list of statuses that you can use to filter invoices. Use the `getInvoicesAttributes` operation to check invoice status options. Min count: 1",
        ),
    ]

    transaction_identifier: Annotated[
        Optional["TransactionIdentifier"],
        Field(
            None,
            validation_alias=AliasChoices(
                "transactionIdentifier", "transaction_identifier"
            ),
            serialization_alias="transactionIdentifier",
        ),
    ]

    transaction_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("transactionType", "transaction_type"),
            serialization_alias="transactionType",
            description="The marketplace-specific classification of the transaction type for which the invoice was created. Use the `getInvoicesAttributes` operation to check `transactionType` options",
        ),
    ]


"""
CreateInvoicesExportRequest

Request parameters for createInvoicesExport
"""


class CreateInvoicesExportRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createInvoicesExport
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "ExportInvoicesRequestBody",
        BodyParam(),
        Field(
            ..., description="[BODY] Information required to create the export request."
        ),
    ]


"""
Error

The error response that is returned when the request is unsuccessful.
"""


class Error(SpApiBaseModel):
    """The error response that is returned when the request is unsuccessful."""

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

    details: Annotated[
        Optional[str],
        Field(
            None,
            description="Additional details that can help the caller understand or fix the issue.",
        ),
    ]

    message: Annotated[
        str, Field(..., description="A message that describes the error condition.")
    ]


"""
ErrorList

A list of error responses that are returned when a request is unsuccessful.
"""


class ErrorList(SpApiBaseModel):
    """A list of error responses that are returned when a request is unsuccessful."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[List["Error"], Field(..., description="List of errors.")]


ExportStatus = str
"""The current status of the request."""


"""
Export

Detailed information about the export.
"""


class Export(SpApiBaseModel):
    """Detailed information about the export."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    error_message: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("errorMessage", "error_message"),
            serialization_alias="errorMessage",
            description="When the export generation fails, this attribute contains a description of the error.",
        ),
    ]

    export_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("exportId", "export_id"),
            serialization_alias="exportId",
            description="The export identifier.",
        ),
    ]

    generate_export_finished_at: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "generateExportFinishedAt", "generate_export_finished_at"
            ),
            serialization_alias="generateExportFinishedAt",
            description="The date and time when the export generation finished. Vales are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.",
        ),
    ]

    generate_export_started_at: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "generateExportStartedAt", "generate_export_started_at"
            ),
            serialization_alias="generateExportStartedAt",
            description="The date and time when the export generation started. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.",
        ),
    ]

    invoices_document_ids: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "invoicesDocumentIds", "invoices_document_ids"
            ),
            serialization_alias="invoicesDocumentIds",
            description="The identifier for the export documents. To get the information required to retrieve the export document's contents, pass each ID in the `getInvoicesDocument` operation. This list is empty until the status is `DONE`.",
        ),
    ]

    status: Annotated[
        Optional["ExportStatus"],
        Field(
            None,
        ),
    ]


"""
ExportInvoicesResponse

Success.
"""


class ExportInvoicesResponse(SpApiBaseModel):
    """Success."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    export_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("exportId", "export_id"),
            serialization_alias="exportId",
            description="The export identifier.",
        ),
    ]


"""
GetInvoiceRequest

Request parameters for getInvoice
"""


class GetInvoiceRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getInvoice
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The marketplace from which you want the invoice.",
        ),
    ]

    invoice_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("invoiceId", "invoice_id"),
            serialization_alias="invoiceId",
            description="[PATH] The invoice identifier.",
        ),
    ]


"""
Invoice

Provides detailed information about an invoice.
"""


class Invoice(SpApiBaseModel):
    """Provides detailed information about an invoice."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    date: Annotated[
        Optional[datetime],
        Field(
            None,
            description="The date and time the invoice is issued. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.",
        ),
    ]

    error_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("errorCode", "error_code"),
            serialization_alias="errorCode",
            description="If the invoice is in an error state, this attribute displays the error code.",
        ),
    ]

    external_invoice_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("externalInvoiceId", "external_invoice_id"),
            serialization_alias="externalInvoiceId",
            description="The invoice identifier that is used by an external party. This is typically the government agency that authorized the invoice.",
        ),
    ]

    gov_response: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("govResponse", "gov_response"),
            serialization_alias="govResponse",
            description="The response message from the government authority when there is an error during invoice issuance.",
        ),
    ]

    id: Annotated[Optional[str], Field(None, description="The invoice identifier.")]

    invoice_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("invoiceType", "invoice_type"),
            serialization_alias="invoiceType",
            description="The classification of the invoice type. This varies across marketplaces. Use the `getInvoicesAttributes` operation to check `invoiceType` options.",
        ),
    ]

    series: Annotated[
        Optional[str],
        Field(
            None,
            description="Use this identifier in conjunction with `externalInvoiceId` to identify invoices from the same seller.",
        ),
    ]

    status: Annotated[
        Optional[str],
        Field(
            None,
            description="The invoice status classification. Use the `getInvoicesAttributes` operation to check invoice status options.",
        ),
    ]

    transaction_ids: Annotated[
        Optional[List["TransactionIdentifier"]],
        Field(
            None,
            validation_alias=AliasChoices("transactionIds", "transaction_ids"),
            serialization_alias="transactionIds",
            description="List with identifiers for the transactions associated to the invoice.",
        ),
    ]

    transaction_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("transactionType", "transaction_type"),
            serialization_alias="transactionType",
            description="Classification of the transaction that originated this invoice. Use the `getInvoicesAttributes` operation to check `transactionType` options.",
        ),
    ]


"""
GetInvoiceResponse

Success.
"""


class GetInvoiceResponse(SpApiBaseModel):
    """Success."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    invoice: Annotated[
        Optional["Invoice"],
        Field(
            None,
        ),
    ]


"""
GetInvoicesAttributesRequest

Request parameters for getInvoicesAttributes
"""


class GetInvoicesAttributesRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getInvoicesAttributes
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The marketplace identifier.",
        ),
    ]


"""
InvoicesAttributes

An object that contains the invoice attributes definition.
"""


class InvoicesAttributes(SpApiBaseModel):
    """An object that contains the invoice attributes definition."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    invoice_status_options: Annotated[
        Optional[List["AttributeOption"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "invoiceStatusOptions", "invoice_status_options"
            ),
            serialization_alias="invoiceStatusOptions",
            description="A list of all the options that are available for the invoice status attribute.",
        ),
    ]

    invoice_type_options: Annotated[
        Optional[List["AttributeOption"]],
        Field(
            None,
            validation_alias=AliasChoices("invoiceTypeOptions", "invoice_type_options"),
            serialization_alias="invoiceTypeOptions",
            description="A list of all the options that are available for the invoice type attribute.",
        ),
    ]

    transaction_identifier_name_options: Annotated[
        Optional[List["AttributeOption"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "transactionIdentifierNameOptions",
                "transaction_identifier_name_options",
            ),
            serialization_alias="transactionIdentifierNameOptions",
            description="A list of all the options that are available for the transaction identifier name attribute.",
        ),
    ]

    transaction_type_options: Annotated[
        Optional[List["AttributeOption"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "transactionTypeOptions", "transaction_type_options"
            ),
            serialization_alias="transactionTypeOptions",
            description="A list of all the options that are available for the transaction type attribute.",
        ),
    ]


"""
GetInvoicesAttributesResponse

Success.
"""


class GetInvoicesAttributesResponse(SpApiBaseModel):
    """Success."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    invoices_attributes: Annotated[
        Optional["InvoicesAttributes"],
        Field(
            None,
            validation_alias=AliasChoices("invoicesAttributes", "invoices_attributes"),
            serialization_alias="invoicesAttributes",
        ),
    ]


"""
GetInvoicesDocumentRequest

Request parameters for getInvoicesDocument
"""


class GetInvoicesDocumentRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getInvoicesDocument
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    invoices_document_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("invoicesDocumentId", "invoices_document_id"),
            serialization_alias="invoicesDocumentId",
            description="[PATH] The export document identifier.",
        ),
    ]


"""
InvoicesDocument

An object that contains the `documentId` and an S3 pre-signed URL that you can use to download the specified file.
"""


class InvoicesDocument(SpApiBaseModel):
    """An object that contains the `documentId` and an S3 pre-signed URL that you can use to download the specified file."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    invoices_document_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("invoicesDocumentId", "invoices_document_id"),
            serialization_alias="invoicesDocumentId",
            description="The identifier of the export document.",
        ),
    ]

    invoices_document_url: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "invoicesDocumentUrl", "invoices_document_url"
            ),
            serialization_alias="invoicesDocumentUrl",
            description="A pre-signed URL that you can use to download the invoices document in zip format. This URL expires after 30 seconds.",
        ),
    ]


"""
GetInvoicesDocumentResponse

Success.
"""


class GetInvoicesDocumentResponse(SpApiBaseModel):
    """Success."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    invoices_document: Annotated[
        Optional["InvoicesDocument"],
        Field(
            None,
            validation_alias=AliasChoices("invoicesDocument", "invoices_document"),
            serialization_alias="invoicesDocument",
        ),
    ]


"""
GetInvoicesExportRequest

Request parameters for getInvoicesExport
"""


class GetInvoicesExportRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getInvoicesExport
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    export_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("exportId", "export_id"),
            serialization_alias="exportId",
            description="[PATH] The unique identifier for the export.",
        ),
    ]


"""
GetInvoicesExportResponse

Success.
"""


class GetInvoicesExportResponse(SpApiBaseModel):
    """Success."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    export: Annotated[
        Optional["Export"],
        Field(
            None,
        ),
    ]


# Enum definitions
class StatusEnum(str, Enum):
    """Enum for status"""

    REQUESTED = "REQUESTED"  # The export request was created, but has not started yet.
    PROCESSING = "PROCESSING"  # The export request is being processed
    DONE = "DONE"  # The export request is finished with success. Use the document IDs to download the output documents.
    ERROR = "ERROR"  # The export request resulted in an error. Check the `errorMessage` attribute for more details.


"""
GetInvoicesExportsRequest

Request parameters for getInvoicesExports
"""


class GetInvoicesExportsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getInvoicesExports
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The returned exports match the specified marketplace.",
        ),
    ]

    date_start: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("dateStart", "date_start"),
            serialization_alias="dateStart",
            description="[QUERY] The earliest export creation date and time for exports that you want to include in the response. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default is 30 days ago.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="[QUERY] The response includes `nextToken` when the number of results exceeds the specified `pageSize` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] The maximum number of invoices to return in a single call.  Minimum: 1  Maximum: 100",
        ),
    ]

    date_end: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("dateEnd", "date_end"),
            serialization_alias="dateEnd",
            description="[QUERY] The latest export creation date and time for exports that you want to include in the response. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default value is the time of the request.",
        ),
    ]

    status: Annotated[
        Optional[StatusEnum],
        QueryParam(),
        Field(
            None, description="[QUERY] Return exports matching the status specified. "
        ),
    ]


"""
GetInvoicesExportsResponse

Success.
"""


class GetInvoicesExportsResponse(SpApiBaseModel):
    """Success."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    exports: Annotated[
        Optional[List["Export"]], Field(None, description="A list of exports.")
    ]

    next_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="This token is returned when the number of results exceeds the specified `pageSize` value. To get the next page of results, call the `getInvoices` operation and include this token with the previous call parameters.",
        ),
    ]


# Enum definitions
class SortOrderEnum(str, Enum):
    """Enum for sortOrder"""

    DESC = "DESC"  # Sort in descending order.
    ASC = "ASC"  # Sort in ascending order.


class SortByEnum(str, Enum):
    """Enum for sortBy"""

    START_DATE_TIME = "START_DATE_TIME"  # Sort by date time.


"""
GetInvoicesRequest

Request parameters for getInvoices
"""


class GetInvoicesRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getInvoices
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    transaction_identifier_name: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "transactionIdentifierName", "transaction_identifier_name"
            ),
            serialization_alias="transactionIdentifierName",
            description="[QUERY] The name of the transaction identifier filter. If you provide a value for this field, you must also provide a value for the `transactionIdentifierId` field.Use the `getInvoicesAttributes` operation to check `transactionIdentifierName` options.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] The maximum number of invoices you want to return in a single call.  Minimum: 1  Maximum: 200",
        ),
    ]

    date_end: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("dateEnd", "date_end"),
            serialization_alias="dateEnd",
            description="[QUERY] The latest invoice creation date for invoices that you want to include in the response. Dates are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default is the current date-time.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The response includes only the invoices that match the specified marketplace.",
        ),
    ]

    transaction_type: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("transactionType", "transaction_type"),
            serialization_alias="transactionType",
            description="[QUERY] The marketplace-specific classification of the transaction type for which the invoice was created. Use the `getInvoicesAttributes` operation to check `transactionType` options.",
        ),
    ]

    transaction_identifier_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "transactionIdentifierId", "transaction_identifier_id"
            ),
            serialization_alias="transactionIdentifierId",
            description="[QUERY] The ID of the transaction identifier filter. If you provide a value for this field, you must also provide a value for the `transactionIdentifierName` field.",
        ),
    ]

    date_start: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("dateStart", "date_start"),
            serialization_alias="dateStart",
            description="[QUERY] The earliest invoice creation date for invoices that you want to include in the response. Dates are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default is 24 hours prior to the time of the request.",
        ),
    ]

    series: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            description="[QUERY] Return invoices with the specified series number.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="[QUERY] The response includes `nextToken` when the number of results exceeds the specified `pageSize` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages.",
        ),
    ]

    sort_order: Annotated[
        Optional[SortOrderEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("sortOrder", "sort_order"),
            serialization_alias="sortOrder",
            description="[QUERY] Sort the invoices in the response in ascending or descending order.",
        ),
    ]

    invoice_type: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("invoiceType", "invoice_type"),
            serialization_alias="invoiceType",
            description="[QUERY] The marketplace-specific classification of the invoice type. Use the `getInvoicesAttributes` operation to check `invoiceType` options.",
        ),
    ]

    statuses: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            description="[QUERY] A list of statuses that you can use to filter invoices. Use the `getInvoicesAttributes` operation to check invoice status options.  Min count: 1",
        ),
    ]

    external_invoice_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("externalInvoiceId", "external_invoice_id"),
            serialization_alias="externalInvoiceId",
            description="[QUERY] Return invoices that match this external ID. This is typically the Government Invoice ID.",
        ),
    ]

    sort_by: Annotated[
        Optional[SortByEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("sortBy", "sort_by"),
            serialization_alias="sortBy",
            description="[QUERY] The attribute by which you want to sort the invoices in the response.",
        ),
    ]


"""
GetInvoicesResponse

Success.
"""


class GetInvoicesResponse(SpApiBaseModel):
    """Success."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    invoices: Annotated[
        Optional[List["Invoice"]], Field(None, description="A list of invoices.")
    ]

    next_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="This token is returned when the number of results exceeds the specified `pageSize` value. To get the next page of results, call the `getInvoices` operation and include this token with the previous call parameters.",
        ),
    ]


# Rebuild models to resolve forward references
AttributeOption.model_rebuild()
Error.model_rebuild()
Export.model_rebuild()
ExportInvoicesRequestBody.model_rebuild()
ExportInvoicesResponse.model_rebuild()
GetInvoiceResponse.model_rebuild()
GetInvoicesAttributesResponse.model_rebuild()
GetInvoicesDocumentResponse.model_rebuild()
GetInvoicesExportResponse.model_rebuild()
GetInvoicesExportsResponse.model_rebuild()
GetInvoicesResponse.model_rebuild()
Invoice.model_rebuild()
InvoicesAttributes.model_rebuild()
InvoicesDocument.model_rebuild()
TransactionIdentifier.model_rebuild()
ErrorList.model_rebuild()
GetInvoicesAttributesRequest.model_rebuild()
GetInvoicesDocumentRequest.model_rebuild()
CreateInvoicesExportRequest.model_rebuild()
GetInvoicesExportsRequest.model_rebuild()
GetInvoicesExportRequest.model_rebuild()
GetInvoicesRequest.model_rebuild()
GetInvoiceRequest.model_rebuild()
