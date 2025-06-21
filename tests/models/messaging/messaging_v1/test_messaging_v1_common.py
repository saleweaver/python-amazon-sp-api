# Auto-generated tests for sp_api.api.models.messaging.messaging_v1.common.py
from datetime import datetime

import pytest
from sp_api.api.models.messaging.messaging_v1.common import (
    Attachment, ConfirmCustomizationDetailsRequest, CreateAmazonMotorsRequest,
    CreateAmazonMotorsRequestBody, CreateAmazonMotorsResponse,
    CreateConfirmCustomizationDetailsRequestBody,
    CreateConfirmCustomizationDetailsResponse,
    CreateConfirmDeliveryDetailsRequest,
    CreateConfirmDeliveryDetailsRequestBody,
    CreateConfirmDeliveryDetailsResponse, CreateConfirmOrderDetailsRequest,
    CreateConfirmOrderDetailsRequestBody, CreateConfirmOrderDetailsResponse,
    CreateConfirmServiceDetailsRequest, CreateConfirmServiceDetailsRequestBody,
    CreateConfirmServiceDetailsResponse, CreateDigitalAccessKeyRequest,
    CreateDigitalAccessKeyRequestBody, CreateDigitalAccessKeyResponse,
    CreateLegalDisclosureRequest, CreateLegalDisclosureRequestBody,
    CreateLegalDisclosureResponse, CreateNegativeFeedbackRemovalRequest,
    CreateNegativeFeedbackRemovalResponse, CreateUnexpectedProblemRequest,
    CreateUnexpectedProblemRequestBody, CreateUnexpectedProblemResponse,
    CreateWarrantyRequest, CreateWarrantyRequestBody, CreateWarrantyResponse,
    Error, GetAttributesRequest, GetAttributesResponse,
    GetMessagingActionResponse, GetMessagingActionsForOrderRequest,
    GetMessagingActionsForOrderResponse, GetRequestSerializer,
    GetSchemaResponse, InvoiceRequestBody, InvoiceResponse, LinkObject,
    MessagingAction, RequestsBaseModel, Schema, SendInvoiceRequest,
    SpApiBaseModel)


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


def test_attachment_instantiates():
    """Instantiate Attachment with dummy data"""
    kwargs = {
        "upload_destination_id": "",
        "file_name": "",
    }
    obj = Attachment(**kwargs)
    assert isinstance(obj, Attachment)


def test_createconfirmcustomizationdetailsrequestbody_instantiates():
    """Instantiate CreateConfirmCustomizationDetailsRequestBody with dummy data"""
    kwargs = {
        "text": None,
        "attachments": None,
    }
    obj = CreateConfirmCustomizationDetailsRequestBody(**kwargs)
    assert isinstance(obj, CreateConfirmCustomizationDetailsRequestBody)


def test_confirmcustomizationdetailsrequest_instantiates():
    """Instantiate ConfirmCustomizationDetailsRequest with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "marketplace_ids": None,
        "body": CreateConfirmCustomizationDetailsRequestBody(
            **{"text": None, "attachments": None}
        ),
    }
    obj = ConfirmCustomizationDetailsRequest(**kwargs)
    assert isinstance(obj, ConfirmCustomizationDetailsRequest)


def test_createamazonmotorsrequestbody_instantiates():
    """Instantiate CreateAmazonMotorsRequestBody with dummy data"""
    kwargs = {
        "attachments": None,
    }
    obj = CreateAmazonMotorsRequestBody(**kwargs)
    assert isinstance(obj, CreateAmazonMotorsRequestBody)


def test_createamazonmotorsrequest_instantiates():
    """Instantiate CreateAmazonMotorsRequest with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "marketplace_ids": None,
        "body": CreateAmazonMotorsRequestBody(**{"attachments": None}),
    }
    obj = CreateAmazonMotorsRequest(**kwargs)
    assert isinstance(obj, CreateAmazonMotorsRequest)


def test_createamazonmotorsresponse_instantiates():
    """Instantiate CreateAmazonMotorsResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = CreateAmazonMotorsResponse(**kwargs)
    assert isinstance(obj, CreateAmazonMotorsResponse)


def test_createconfirmcustomizationdetailsresponse_instantiates():
    """Instantiate CreateConfirmCustomizationDetailsResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = CreateConfirmCustomizationDetailsResponse(**kwargs)
    assert isinstance(obj, CreateConfirmCustomizationDetailsResponse)


def test_createconfirmdeliverydetailsrequestbody_instantiates():
    """Instantiate CreateConfirmDeliveryDetailsRequestBody with dummy data"""
    kwargs = {
        "text": None,
    }
    obj = CreateConfirmDeliveryDetailsRequestBody(**kwargs)
    assert isinstance(obj, CreateConfirmDeliveryDetailsRequestBody)


def test_createconfirmdeliverydetailsrequest_instantiates():
    """Instantiate CreateConfirmDeliveryDetailsRequest with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "marketplace_ids": None,
        "body": CreateConfirmDeliveryDetailsRequestBody(**{"text": None}),
    }
    obj = CreateConfirmDeliveryDetailsRequest(**kwargs)
    assert isinstance(obj, CreateConfirmDeliveryDetailsRequest)


def test_createconfirmdeliverydetailsresponse_instantiates():
    """Instantiate CreateConfirmDeliveryDetailsResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = CreateConfirmDeliveryDetailsResponse(**kwargs)
    assert isinstance(obj, CreateConfirmDeliveryDetailsResponse)


def test_createconfirmorderdetailsrequestbody_instantiates():
    """Instantiate CreateConfirmOrderDetailsRequestBody with dummy data"""
    kwargs = {
        "text": None,
    }
    obj = CreateConfirmOrderDetailsRequestBody(**kwargs)
    assert isinstance(obj, CreateConfirmOrderDetailsRequestBody)


def test_createconfirmorderdetailsrequest_instantiates():
    """Instantiate CreateConfirmOrderDetailsRequest with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "marketplace_ids": None,
        "body": CreateConfirmOrderDetailsRequestBody(**{"text": None}),
    }
    obj = CreateConfirmOrderDetailsRequest(**kwargs)
    assert isinstance(obj, CreateConfirmOrderDetailsRequest)


def test_createconfirmorderdetailsresponse_instantiates():
    """Instantiate CreateConfirmOrderDetailsResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = CreateConfirmOrderDetailsResponse(**kwargs)
    assert isinstance(obj, CreateConfirmOrderDetailsResponse)


def test_createconfirmservicedetailsrequestbody_instantiates():
    """Instantiate CreateConfirmServiceDetailsRequestBody with dummy data"""
    kwargs = {
        "text": None,
    }
    obj = CreateConfirmServiceDetailsRequestBody(**kwargs)
    assert isinstance(obj, CreateConfirmServiceDetailsRequestBody)


def test_createconfirmservicedetailsrequest_instantiates():
    """Instantiate CreateConfirmServiceDetailsRequest with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "marketplace_ids": None,
        "body": CreateConfirmServiceDetailsRequestBody(**{"text": None}),
    }
    obj = CreateConfirmServiceDetailsRequest(**kwargs)
    assert isinstance(obj, CreateConfirmServiceDetailsRequest)


def test_createconfirmservicedetailsresponse_instantiates():
    """Instantiate CreateConfirmServiceDetailsResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = CreateConfirmServiceDetailsResponse(**kwargs)
    assert isinstance(obj, CreateConfirmServiceDetailsResponse)


def test_createdigitalaccesskeyrequestbody_instantiates():
    """Instantiate CreateDigitalAccessKeyRequestBody with dummy data"""
    kwargs = {
        "text": None,
        "attachments": None,
    }
    obj = CreateDigitalAccessKeyRequestBody(**kwargs)
    assert isinstance(obj, CreateDigitalAccessKeyRequestBody)


def test_createdigitalaccesskeyrequest_instantiates():
    """Instantiate CreateDigitalAccessKeyRequest with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "marketplace_ids": None,
        "body": CreateDigitalAccessKeyRequestBody(
            **{"text": None, "attachments": None}
        ),
    }
    obj = CreateDigitalAccessKeyRequest(**kwargs)
    assert isinstance(obj, CreateDigitalAccessKeyRequest)


def test_createdigitalaccesskeyresponse_instantiates():
    """Instantiate CreateDigitalAccessKeyResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = CreateDigitalAccessKeyResponse(**kwargs)
    assert isinstance(obj, CreateDigitalAccessKeyResponse)


def test_createlegaldisclosurerequestbody_instantiates():
    """Instantiate CreateLegalDisclosureRequestBody with dummy data"""
    kwargs = {
        "attachments": None,
    }
    obj = CreateLegalDisclosureRequestBody(**kwargs)
    assert isinstance(obj, CreateLegalDisclosureRequestBody)


def test_createlegaldisclosurerequest_instantiates():
    """Instantiate CreateLegalDisclosureRequest with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "marketplace_ids": None,
        "body": CreateLegalDisclosureRequestBody(**{"attachments": None}),
    }
    obj = CreateLegalDisclosureRequest(**kwargs)
    assert isinstance(obj, CreateLegalDisclosureRequest)


def test_createlegaldisclosureresponse_instantiates():
    """Instantiate CreateLegalDisclosureResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = CreateLegalDisclosureResponse(**kwargs)
    assert isinstance(obj, CreateLegalDisclosureResponse)


def test_createnegativefeedbackremovalrequest_instantiates():
    """Instantiate CreateNegativeFeedbackRemovalRequest with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "marketplace_ids": None,
    }
    obj = CreateNegativeFeedbackRemovalRequest(**kwargs)
    assert isinstance(obj, CreateNegativeFeedbackRemovalRequest)


def test_createnegativefeedbackremovalresponse_instantiates():
    """Instantiate CreateNegativeFeedbackRemovalResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = CreateNegativeFeedbackRemovalResponse(**kwargs)
    assert isinstance(obj, CreateNegativeFeedbackRemovalResponse)


def test_createunexpectedproblemrequestbody_instantiates():
    """Instantiate CreateUnexpectedProblemRequestBody with dummy data"""
    kwargs = {
        "text": None,
    }
    obj = CreateUnexpectedProblemRequestBody(**kwargs)
    assert isinstance(obj, CreateUnexpectedProblemRequestBody)


def test_createunexpectedproblemrequest_instantiates():
    """Instantiate CreateUnexpectedProblemRequest with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "marketplace_ids": None,
        "body": CreateUnexpectedProblemRequestBody(**{"text": None}),
    }
    obj = CreateUnexpectedProblemRequest(**kwargs)
    assert isinstance(obj, CreateUnexpectedProblemRequest)


def test_createunexpectedproblemresponse_instantiates():
    """Instantiate CreateUnexpectedProblemResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = CreateUnexpectedProblemResponse(**kwargs)
    assert isinstance(obj, CreateUnexpectedProblemResponse)


def test_createwarrantyrequestbody_instantiates():
    """Instantiate CreateWarrantyRequestBody with dummy data"""
    kwargs = {
        "attachments": None,
        "coverage_start_date": None,
        "coverage_end_date": None,
    }
    obj = CreateWarrantyRequestBody(**kwargs)
    assert isinstance(obj, CreateWarrantyRequestBody)


def test_createwarrantyrequest_instantiates():
    """Instantiate CreateWarrantyRequest with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "marketplace_ids": None,
        "body": CreateWarrantyRequestBody(
            **{
                "attachments": None,
                "coverage_start_date": None,
                "coverage_end_date": None,
            }
        ),
    }
    obj = CreateWarrantyRequest(**kwargs)
    assert isinstance(obj, CreateWarrantyRequest)


def test_createwarrantyresponse_instantiates():
    """Instantiate CreateWarrantyResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = CreateWarrantyResponse(**kwargs)
    assert isinstance(obj, CreateWarrantyResponse)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_getattributesrequest_instantiates():
    """Instantiate GetAttributesRequest with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "marketplace_ids": None,
    }
    obj = GetAttributesRequest(**kwargs)
    assert isinstance(obj, GetAttributesRequest)


def test_getattributesresponse_instantiates():
    """Instantiate GetAttributesResponse with dummy data"""
    kwargs = {
        "buyer": None,
        "errors": None,
    }
    obj = GetAttributesResponse(**kwargs)
    assert isinstance(obj, GetAttributesResponse)


def test_messagingaction_instantiates():
    """Instantiate MessagingAction with dummy data"""
    kwargs = {
        "name": "",
    }
    obj = MessagingAction(**kwargs)
    assert isinstance(obj, MessagingAction)


def test_getmessagingactionresponse_instantiates():
    """Instantiate GetMessagingActionResponse with dummy data"""
    kwargs = {
        "links": None,
        "embedded": None,
        "payload": None,
        "errors": None,
    }
    obj = GetMessagingActionResponse(**kwargs)
    assert isinstance(obj, GetMessagingActionResponse)


def test_getmessagingactionsfororderrequest_instantiates():
    """Instantiate GetMessagingActionsForOrderRequest with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "marketplace_ids": None,
    }
    obj = GetMessagingActionsForOrderRequest(**kwargs)
    assert isinstance(obj, GetMessagingActionsForOrderRequest)


def test_getmessagingactionsfororderresponse_instantiates():
    """Instantiate GetMessagingActionsForOrderResponse with dummy data"""
    kwargs = {
        "links": None,
        "embedded": None,
        "errors": None,
    }
    obj = GetMessagingActionsForOrderResponse(**kwargs)
    assert isinstance(obj, GetMessagingActionsForOrderResponse)


def test_schema_instantiates():
    """Instantiate Schema with dummy data"""
    kwargs = {}
    obj = Schema(**kwargs)
    assert isinstance(obj, Schema)


def test_getschemaresponse_instantiates():
    """Instantiate GetSchemaResponse with dummy data"""
    kwargs = {
        "links": None,
        "payload": None,
        "errors": None,
    }
    obj = GetSchemaResponse(**kwargs)
    assert isinstance(obj, GetSchemaResponse)


def test_invoicerequestbody_instantiates():
    """Instantiate InvoiceRequestBody with dummy data"""
    kwargs = {
        "attachments": None,
    }
    obj = InvoiceRequestBody(**kwargs)
    assert isinstance(obj, InvoiceRequestBody)


def test_invoiceresponse_instantiates():
    """Instantiate InvoiceResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = InvoiceResponse(**kwargs)
    assert isinstance(obj, InvoiceResponse)


def test_linkobject_instantiates():
    """Instantiate LinkObject with dummy data"""
    kwargs = {
        "href": "",
        "name": None,
    }
    obj = LinkObject(**kwargs)
    assert isinstance(obj, LinkObject)


def test_sendinvoicerequest_instantiates():
    """Instantiate SendInvoiceRequest with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "marketplace_ids": None,
        "body": InvoiceRequestBody(**{"attachments": None}),
    }
    obj = SendInvoiceRequest(**kwargs)
    assert isinstance(obj, SendInvoiceRequest)
