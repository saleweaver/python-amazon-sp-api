# Auto-generated tests for sp_api.api.models.invoices.invoices_2024_06_19.common.py
from datetime import datetime

import pytest
from sp_api.api.models.invoices.invoices_2024_06_19.common import (
    AttributeOption, CreateInvoicesExportRequest, Error, ErrorList, Export,
    ExportInvoicesRequestBody, ExportInvoicesResponse, GetInvoiceRequest,
    GetInvoiceResponse, GetInvoicesAttributesRequest,
    GetInvoicesAttributesResponse, GetInvoicesDocumentRequest,
    GetInvoicesDocumentResponse, GetInvoicesExportRequest,
    GetInvoicesExportResponse, GetInvoicesExportsRequest,
    GetInvoicesExportsResponse, GetInvoicesRequest, GetInvoicesResponse,
    GetRequestSerializer, Invoice, InvoicesAttributes, InvoicesDocument,
    RequestsBaseModel, SortByEnum, SortOrderEnum, SpApiBaseModel, StatusEnum,
    TransactionIdentifier)


def test_requestsbasemodel_instantiates():
    """Instantiate RequestsBaseModel with dummy data"""
    kwargs = {}
    obj = RequestsBaseModel(**kwargs)
    assert isinstance(obj, RequestsBaseModel)


def test_spapibasemodel_instantiates():
    """Instantiate SpApiBaseModel with dummy data"""
    kwargs = {}
    obj = SpApiBaseModel(**kwargs)
    assert isinstance(obj, SpApiBaseModel)


def test_getrequestserializer_instantiates():
    """Instantiate GetRequestSerializer with dummy data"""
    kwargs = {}
    obj = GetRequestSerializer(**kwargs)
    assert isinstance(obj, GetRequestSerializer)


def test_attributeoption_instantiates():
    """Instantiate AttributeOption with dummy data"""
    kwargs = {
        "description": None,
        "value": None,
    }
    obj = AttributeOption(**kwargs)
    assert isinstance(obj, AttributeOption)


def test_transactionidentifier_instantiates():
    """Instantiate TransactionIdentifier with dummy data"""
    kwargs = {
        "name": None,
        "id": None,
    }
    obj = TransactionIdentifier(**kwargs)
    assert isinstance(obj, TransactionIdentifier)


def test_exportinvoicesrequestbody_instantiates():
    """Instantiate ExportInvoicesRequestBody with dummy data"""
    kwargs = {
        "date_end": None,
        "date_start": None,
        "external_invoice_id": None,
        "file_format": None,
        "invoice_type": None,
        "marketplace_id": None,
        "series": None,
        "statuses": None,
        "transaction_identifier": None,
        "transaction_type": None,
    }
    obj = ExportInvoicesRequestBody(**kwargs)
    assert isinstance(obj, ExportInvoicesRequestBody)


def test_createinvoicesexportrequest_instantiates():
    """Instantiate CreateInvoicesExportRequest with dummy data"""
    kwargs = {
        "body": ExportInvoicesRequestBody(
            **{
                "date_end": None,
                "date_start": None,
                "external_invoice_id": None,
                "file_format": None,
                "invoice_type": None,
                "marketplace_id": None,
                "series": None,
                "statuses": None,
                "transaction_identifier": None,
                "transaction_type": None,
            }
        ),
    }
    obj = CreateInvoicesExportRequest(**kwargs)
    assert isinstance(obj, CreateInvoicesExportRequest)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "details": None,
        "message": "",
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_errorlist_instantiates():
    """Instantiate ErrorList with dummy data"""
    kwargs = {
        "errors": [],
    }
    obj = ErrorList(**kwargs)
    assert isinstance(obj, ErrorList)


def test_export_instantiates():
    """Instantiate Export with dummy data"""
    kwargs = {
        "error_message": None,
        "export_id": None,
        "generate_export_finished_at": None,
        "generate_export_started_at": None,
        "invoices_document_ids": None,
        "status": None,
    }
    obj = Export(**kwargs)
    assert isinstance(obj, Export)


def test_exportinvoicesresponse_instantiates():
    """Instantiate ExportInvoicesResponse with dummy data"""
    kwargs = {
        "export_id": None,
    }
    obj = ExportInvoicesResponse(**kwargs)
    assert isinstance(obj, ExportInvoicesResponse)


def test_getinvoicerequest_instantiates():
    """Instantiate GetInvoiceRequest with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "invoice_id": "",
    }
    obj = GetInvoiceRequest(**kwargs)
    assert isinstance(obj, GetInvoiceRequest)


def test_invoice_instantiates():
    """Instantiate Invoice with dummy data"""
    kwargs = {
        "date": None,
        "error_code": None,
        "external_invoice_id": None,
        "gov_response": None,
        "id": None,
        "invoice_type": None,
        "series": None,
        "status": None,
        "transaction_ids": None,
        "transaction_type": None,
    }
    obj = Invoice(**kwargs)
    assert isinstance(obj, Invoice)


def test_getinvoiceresponse_instantiates():
    """Instantiate GetInvoiceResponse with dummy data"""
    kwargs = {
        "invoice": None,
    }
    obj = GetInvoiceResponse(**kwargs)
    assert isinstance(obj, GetInvoiceResponse)


def test_getinvoicesattributesrequest_instantiates():
    """Instantiate GetInvoicesAttributesRequest with dummy data"""
    kwargs = {
        "marketplace_id": None,
    }
    obj = GetInvoicesAttributesRequest(**kwargs)
    assert isinstance(obj, GetInvoicesAttributesRequest)


def test_invoicesattributes_instantiates():
    """Instantiate InvoicesAttributes with dummy data"""
    kwargs = {
        "invoice_status_options": None,
        "invoice_type_options": None,
        "transaction_identifier_name_options": None,
        "transaction_type_options": None,
    }
    obj = InvoicesAttributes(**kwargs)
    assert isinstance(obj, InvoicesAttributes)


def test_getinvoicesattributesresponse_instantiates():
    """Instantiate GetInvoicesAttributesResponse with dummy data"""
    kwargs = {
        "invoices_attributes": None,
    }
    obj = GetInvoicesAttributesResponse(**kwargs)
    assert isinstance(obj, GetInvoicesAttributesResponse)


def test_getinvoicesdocumentrequest_instantiates():
    """Instantiate GetInvoicesDocumentRequest with dummy data"""
    kwargs = {
        "invoices_document_id": "",
    }
    obj = GetInvoicesDocumentRequest(**kwargs)
    assert isinstance(obj, GetInvoicesDocumentRequest)


def test_invoicesdocument_instantiates():
    """Instantiate InvoicesDocument with dummy data"""
    kwargs = {
        "invoices_document_id": None,
        "invoices_document_url": None,
    }
    obj = InvoicesDocument(**kwargs)
    assert isinstance(obj, InvoicesDocument)


def test_getinvoicesdocumentresponse_instantiates():
    """Instantiate GetInvoicesDocumentResponse with dummy data"""
    kwargs = {
        "invoices_document": None,
    }
    obj = GetInvoicesDocumentResponse(**kwargs)
    assert isinstance(obj, GetInvoicesDocumentResponse)


def test_getinvoicesexportrequest_instantiates():
    """Instantiate GetInvoicesExportRequest with dummy data"""
    kwargs = {
        "export_id": "",
    }
    obj = GetInvoicesExportRequest(**kwargs)
    assert isinstance(obj, GetInvoicesExportRequest)


def test_getinvoicesexportresponse_instantiates():
    """Instantiate GetInvoicesExportResponse with dummy data"""
    kwargs = {
        "export": None,
    }
    obj = GetInvoicesExportResponse(**kwargs)
    assert isinstance(obj, GetInvoicesExportResponse)


def test_getinvoicesexportsrequest_instantiates():
    """Instantiate GetInvoicesExportsRequest with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "date_start": None,
        "next_token": None,
        "page_size": None,
        "date_end": None,
        "status": None,
    }
    obj = GetInvoicesExportsRequest(**kwargs)
    assert isinstance(obj, GetInvoicesExportsRequest)


def test_getinvoicesexportsresponse_instantiates():
    """Instantiate GetInvoicesExportsResponse with dummy data"""
    kwargs = {
        "exports": None,
        "next_token": None,
    }
    obj = GetInvoicesExportsResponse(**kwargs)
    assert isinstance(obj, GetInvoicesExportsResponse)


def test_getinvoicesrequest_instantiates():
    """Instantiate GetInvoicesRequest with dummy data"""
    kwargs = {
        "transaction_identifier_name": None,
        "page_size": None,
        "date_end": None,
        "marketplace_id": None,
        "transaction_type": None,
        "transaction_identifier_id": None,
        "date_start": None,
        "series": None,
        "next_token": None,
        "sort_order": None,
        "invoice_type": None,
        "statuses": None,
        "external_invoice_id": None,
        "sort_by": None,
    }
    obj = GetInvoicesRequest(**kwargs)
    assert isinstance(obj, GetInvoicesRequest)


def test_getinvoicesresponse_instantiates():
    """Instantiate GetInvoicesResponse with dummy data"""
    kwargs = {
        "invoices": None,
        "next_token": None,
    }
    obj = GetInvoicesResponse(**kwargs)
    assert isinstance(obj, GetInvoicesResponse)
