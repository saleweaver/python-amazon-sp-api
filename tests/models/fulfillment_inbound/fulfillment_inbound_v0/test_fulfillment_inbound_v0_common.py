# Auto-generated tests for sp_api.api.models.fulfillment_inbound.fulfillment_inbound_v0.common.py
from datetime import datetime

import pytest
from sp_api.api.models.fulfillment_inbound.fulfillment_inbound_v0.common import (
    Address, AmazonPrepFeesDetails, Amount, ASINPrepInstructions,
    BillOfLadingDownloadURL, BoxContentsFeeDetails, Error,
    GetBillOfLadingRequest, GetBillOfLadingResponse, GetLabelsRequest,
    GetLabelsResponse, GetPrepInstructionsRequest, GetPrepInstructionsResponse,
    GetPrepInstructionsResult, GetRequestSerializer,
    GetShipmentItemsByShipmentIdRequest, GetShipmentItemsRequest,
    GetShipmentItemsResponse, GetShipmentItemsResult, GetShipmentsRequest,
    GetShipmentsResponse, GetShipmentsResult, InboundShipmentInfo,
    InboundShipmentItem, InvalidASIN, InvalidSKU, LabelDownloadURL,
    LabelTypeEnum, PageTypeEnum, PrepDetails, QueryTypeEnum, RequestsBaseModel,
    ShipmentStatusListEnum, SKUPrepInstructions, SpApiBaseModel)


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


def test_asinprepinstructions_instantiates():
    """Instantiate ASINPrepInstructions with dummy data"""
    kwargs = {
        "a_s_i_n": None,
        "barcode_instruction": None,
        "prep_guidance": None,
        "prep_instruction_list": None,
    }
    obj = ASINPrepInstructions(**kwargs)
    assert isinstance(obj, ASINPrepInstructions)


def test_address_instantiates():
    """Instantiate Address with dummy data"""
    kwargs = {
        "name": "",
        "address_line1": "",
        "address_line2": None,
        "district_or_county": None,
        "city": "",
        "state_or_province_code": "",
        "country_code": "",
        "postal_code": "",
    }
    obj = Address(**kwargs)
    assert isinstance(obj, Address)


def test_amount_instantiates():
    """Instantiate Amount with dummy data"""
    kwargs = {
        "currency_code": "",
        "value": 0.0,
    }
    obj = Amount(**kwargs)
    assert isinstance(obj, Amount)


def test_amazonprepfeesdetails_instantiates():
    """Instantiate AmazonPrepFeesDetails with dummy data"""
    kwargs = {
        "prep_instruction": None,
        "fee_per_unit": None,
    }
    obj = AmazonPrepFeesDetails(**kwargs)
    assert isinstance(obj, AmazonPrepFeesDetails)


def test_billofladingdownloadurl_instantiates():
    """Instantiate BillOfLadingDownloadURL with dummy data"""
    kwargs = {
        "download_u_r_l": None,
    }
    obj = BillOfLadingDownloadURL(**kwargs)
    assert isinstance(obj, BillOfLadingDownloadURL)


def test_boxcontentsfeedetails_instantiates():
    """Instantiate BoxContentsFeeDetails with dummy data"""
    kwargs = {
        "total_units": None,
        "fee_per_unit": None,
        "total_fee": None,
    }
    obj = BoxContentsFeeDetails(**kwargs)
    assert isinstance(obj, BoxContentsFeeDetails)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_getbillofladingrequest_instantiates():
    """Instantiate GetBillOfLadingRequest with dummy data"""
    kwargs = {
        "shipment_id": "",
    }
    obj = GetBillOfLadingRequest(**kwargs)
    assert isinstance(obj, GetBillOfLadingRequest)


def test_getbillofladingresponse_instantiates():
    """Instantiate GetBillOfLadingResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetBillOfLadingResponse(**kwargs)
    assert isinstance(obj, GetBillOfLadingResponse)


def test_getlabelsrequest_instantiates():
    """Instantiate GetLabelsRequest with dummy data"""
    kwargs = {
        "shipment_id": "",
        "page_type": PageTypeEnum.PACKAGE_LABEL_LETTER_2,
        "label_type": LabelTypeEnum.BARCODE_2_D,
        "number_of_packages": None,
        "package_labels_to_print": None,
        "number_of_pallets": None,
        "page_size": None,
        "page_start_index": None,
    }
    obj = GetLabelsRequest(**kwargs)
    assert isinstance(obj, GetLabelsRequest)


def test_labeldownloadurl_instantiates():
    """Instantiate LabelDownloadURL with dummy data"""
    kwargs = {
        "download_u_r_l": None,
    }
    obj = LabelDownloadURL(**kwargs)
    assert isinstance(obj, LabelDownloadURL)


def test_getlabelsresponse_instantiates():
    """Instantiate GetLabelsResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetLabelsResponse(**kwargs)
    assert isinstance(obj, GetLabelsResponse)


def test_getprepinstructionsrequest_instantiates():
    """Instantiate GetPrepInstructionsRequest with dummy data"""
    kwargs = {
        "ship_to_country_code": "",
        "seller_s_k_u_list": None,
        "a_s_i_n_list": None,
    }
    obj = GetPrepInstructionsRequest(**kwargs)
    assert isinstance(obj, GetPrepInstructionsRequest)


def test_getprepinstructionsresult_instantiates():
    """Instantiate GetPrepInstructionsResult with dummy data"""
    kwargs = {
        "s_k_u_prep_instructions_list": None,
        "invalid_s_k_u_list": None,
        "a_s_i_n_prep_instructions_list": None,
        "invalid_a_s_i_n_list": None,
    }
    obj = GetPrepInstructionsResult(**kwargs)
    assert isinstance(obj, GetPrepInstructionsResult)


def test_getprepinstructionsresponse_instantiates():
    """Instantiate GetPrepInstructionsResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetPrepInstructionsResponse(**kwargs)
    assert isinstance(obj, GetPrepInstructionsResponse)


def test_getshipmentitemsbyshipmentidrequest_instantiates():
    """Instantiate GetShipmentItemsByShipmentIdRequest with dummy data"""
    kwargs = {
        "shipment_id": "",
        "marketplace_id": None,
    }
    obj = GetShipmentItemsByShipmentIdRequest(**kwargs)
    assert isinstance(obj, GetShipmentItemsByShipmentIdRequest)


def test_getshipmentitemsrequest_instantiates():
    """Instantiate GetShipmentItemsRequest with dummy data"""
    kwargs = {
        "last_updated_after": None,
        "last_updated_before": None,
        "query_type": QueryTypeEnum.DATE_RANGE,
        "next_token": None,
        "marketplace_id": None,
    }
    obj = GetShipmentItemsRequest(**kwargs)
    assert isinstance(obj, GetShipmentItemsRequest)


def test_getshipmentitemsresult_instantiates():
    """Instantiate GetShipmentItemsResult with dummy data"""
    kwargs = {
        "item_data": None,
        "next_token": None,
    }
    obj = GetShipmentItemsResult(**kwargs)
    assert isinstance(obj, GetShipmentItemsResult)


def test_getshipmentitemsresponse_instantiates():
    """Instantiate GetShipmentItemsResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetShipmentItemsResponse(**kwargs)
    assert isinstance(obj, GetShipmentItemsResponse)


def test_getshipmentsrequest_instantiates():
    """Instantiate GetShipmentsRequest with dummy data"""
    kwargs = {
        "shipment_status_list": None,
        "shipment_id_list": None,
        "last_updated_after": None,
        "last_updated_before": None,
        "query_type": QueryTypeEnum.DATE_RANGE,
        "next_token": None,
        "marketplace_id": None,
    }
    obj = GetShipmentsRequest(**kwargs)
    assert isinstance(obj, GetShipmentsRequest)


def test_getshipmentsresult_instantiates():
    """Instantiate GetShipmentsResult with dummy data"""
    kwargs = {
        "shipment_data": None,
        "next_token": None,
    }
    obj = GetShipmentsResult(**kwargs)
    assert isinstance(obj, GetShipmentsResult)


def test_getshipmentsresponse_instantiates():
    """Instantiate GetShipmentsResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetShipmentsResponse(**kwargs)
    assert isinstance(obj, GetShipmentsResponse)


def test_inboundshipmentinfo_instantiates():
    """Instantiate InboundShipmentInfo with dummy data"""
    kwargs = {
        "shipment_id": None,
        "shipment_name": None,
        "ship_from_address": Address(
            **{
                "name": "",
                "address_line1": "",
                "address_line2": None,
                "district_or_county": None,
                "city": "",
                "state_or_province_code": "",
                "country_code": "",
                "postal_code": "",
            }
        ),
        "destination_fulfillment_center_id": None,
        "shipment_status": None,
        "label_prep_type": None,
        "are_cases_required": False,
        "confirmed_need_by_date": None,
        "box_contents_source": None,
        "estimated_box_contents_fee": None,
    }
    obj = InboundShipmentInfo(**kwargs)
    assert isinstance(obj, InboundShipmentInfo)


def test_inboundshipmentitem_instantiates():
    """Instantiate InboundShipmentItem with dummy data"""
    kwargs = {
        "shipment_id": None,
        "seller_s_k_u": "",
        "fulfillment_network_s_k_u": None,
        "quantity_shipped": 0,
        "quantity_received": None,
        "quantity_in_case": None,
        "release_date": None,
        "prep_details_list": None,
    }
    obj = InboundShipmentItem(**kwargs)
    assert isinstance(obj, InboundShipmentItem)


def test_invalidasin_instantiates():
    """Instantiate InvalidASIN with dummy data"""
    kwargs = {
        "a_s_i_n": None,
        "error_reason": None,
    }
    obj = InvalidASIN(**kwargs)
    assert isinstance(obj, InvalidASIN)


def test_invalidsku_instantiates():
    """Instantiate InvalidSKU with dummy data"""
    kwargs = {
        "seller_s_k_u": None,
        "error_reason": None,
    }
    obj = InvalidSKU(**kwargs)
    assert isinstance(obj, InvalidSKU)


def test_prepdetails_instantiates():
    """Instantiate PrepDetails with dummy data"""
    kwargs = {
        "prep_instruction": "",
        "prep_owner": "",
    }
    obj = PrepDetails(**kwargs)
    assert isinstance(obj, PrepDetails)


def test_skuprepinstructions_instantiates():
    """Instantiate SKUPrepInstructions with dummy data"""
    kwargs = {
        "seller_s_k_u": None,
        "a_s_i_n": None,
        "barcode_instruction": None,
        "prep_guidance": None,
        "prep_instruction_list": None,
        "amazon_prep_fees_details_list": None,
    }
    obj = SKUPrepInstructions(**kwargs)
    assert isinstance(obj, SKUPrepInstructions)
