# Auto-generated tests for sp_api.api.models.vendor_direct_fulfillment_orders.vendor_direct_fulfillment_orders_2021_12_28.common.py
from datetime import datetime

import pytest
from sp_api.api.models.vendor_direct_fulfillment_orders.vendor_direct_fulfillment_orders_2021_12_28.common import (
    AcknowledgementStatus, Address, Error, ErrorList, GetOrderRequest,
    GetOrdersRequest, GetOrdersRequestSortOrderEnum,
    GetOrdersRequestStatusEnum, GetRequestSerializer, GiftDetails,
    ItemQuantity, ItemQuantityUnitOfMeasureEnum, Money, Order,
    OrderAcknowledgementItem, OrderDetails, OrderDetailsOrderStatusEnum,
    OrderItem, OrderItemAcknowledgement, OrderList, Pagination,
    PartyIdentification, RequestsBaseModel, ScheduledDeliveryShipment,
    ShipmentDates, ShipmentDetails, SpApiBaseModel,
    SubmitAcknowledgementRequest, SubmitAcknowledgementRequestBody,
    SubmitAcknowledgementResponse, TaxDetails, TaxDetailsTypeEnum,
    TaxItemDetails, TaxRegistrationDetails,
    TaxRegistrationDetailsTaxRegistrationTypeEnum, TransactionId,
    buyerCustomizedInfoDetail)


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


def test_acknowledgementstatus_instantiates():
    """Instantiate AcknowledgementStatus with dummy data"""
    kwargs = {
        "code": None,
        "description": None,
    }
    obj = AcknowledgementStatus(**kwargs)
    assert isinstance(obj, AcknowledgementStatus)


def test_address_instantiates():
    """Instantiate Address with dummy data"""
    kwargs = {
        "name": "",
        "attention": None,
        "address_line1": "",
        "address_line2": None,
        "address_line3": None,
        "city": None,
        "county": None,
        "district": None,
        "state_or_region": "",
        "postal_code": None,
        "country_code": "",
        "phone": None,
    }
    obj = Address(**kwargs)
    assert isinstance(obj, Address)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
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


def test_getorderrequest_instantiates():
    """Instantiate GetOrderRequest with dummy data"""
    kwargs = {
        "purchase_order_number": "",
    }
    obj = GetOrderRequest(**kwargs)
    assert isinstance(obj, GetOrderRequest)


def test_getordersrequest_instantiates():
    """Instantiate GetOrdersRequest with dummy data"""
    kwargs = {
        "ship_from_party_id": None,
        "status": None,
        "limit": None,
        "created_after": datetime(2000, 1, 1),
        "created_before": datetime(2000, 1, 1),
        "sort_order": None,
        "next_token": None,
        "include_details": None,
    }
    obj = GetOrdersRequest(**kwargs)
    assert isinstance(obj, GetOrdersRequest)


def test_giftdetails_instantiates():
    """Instantiate GiftDetails with dummy data"""
    kwargs = {
        "gift_message": None,
        "gift_wrap_id": None,
    }
    obj = GiftDetails(**kwargs)
    assert isinstance(obj, GiftDetails)


def test_itemquantity_instantiates():
    """Instantiate ItemQuantity with dummy data"""
    kwargs = {
        "amount": None,
        "unit_of_measure": None,
    }
    obj = ItemQuantity(**kwargs)
    assert isinstance(obj, ItemQuantity)


def test_money_instantiates():
    """Instantiate Money with dummy data"""
    kwargs = {
        "currency_code": None,
        "amount": None,
    }
    obj = Money(**kwargs)
    assert isinstance(obj, Money)


def test_scheduleddeliveryshipment_instantiates():
    """Instantiate ScheduledDeliveryShipment with dummy data"""
    kwargs = {
        "scheduled_delivery_service_type": None,
        "earliest_nominated_delivery_date": None,
        "latest_nominated_delivery_date": None,
    }
    obj = ScheduledDeliveryShipment(**kwargs)
    assert isinstance(obj, ScheduledDeliveryShipment)


def test_taxitemdetails_instantiates():
    """Instantiate TaxItemDetails with dummy data"""
    kwargs = {
        "tax_line_item": None,
    }
    obj = TaxItemDetails(**kwargs)
    assert isinstance(obj, TaxItemDetails)


def test_buyercustomizedinfodetail_instantiates():
    """Instantiate buyerCustomizedInfoDetail with dummy data"""
    kwargs = {
        "customized_url": None,
    }
    obj = buyerCustomizedInfoDetail(**kwargs)
    assert isinstance(obj, buyerCustomizedInfoDetail)


def test_orderitem_instantiates():
    """Instantiate OrderItem with dummy data"""
    kwargs = {
        "item_sequence_number": "",
        "buyer_product_identifier": None,
        "vendor_product_identifier": None,
        "title": None,
        "ordered_quantity": ItemQuantity(**{"amount": None, "unit_of_measure": None}),
        "scheduled_delivery_shipment": None,
        "gift_details": None,
        "net_price": Money(**{"currency_code": None, "amount": None}),
        "tax_details": None,
        "total_price": None,
        "buyer_customized_info": None,
    }
    obj = OrderItem(**kwargs)
    assert isinstance(obj, OrderItem)


def test_taxregistrationdetails_instantiates():
    """Instantiate TaxRegistrationDetails with dummy data"""
    kwargs = {
        "tax_registration_type": None,
        "tax_registration_number": "",
        "tax_registration_address": None,
        "tax_registration_messages": None,
    }
    obj = TaxRegistrationDetails(**kwargs)
    assert isinstance(obj, TaxRegistrationDetails)


def test_partyidentification_instantiates():
    """Instantiate PartyIdentification with dummy data"""
    kwargs = {
        "party_id": "",
        "address": None,
        "tax_info": None,
    }
    obj = PartyIdentification(**kwargs)
    assert isinstance(obj, PartyIdentification)


def test_shipmentdates_instantiates():
    """Instantiate ShipmentDates with dummy data"""
    kwargs = {
        "required_ship_date": datetime(2000, 1, 1),
        "promised_delivery_date": None,
    }
    obj = ShipmentDates(**kwargs)
    assert isinstance(obj, ShipmentDates)


def test_shipmentdetails_instantiates():
    """Instantiate ShipmentDetails with dummy data"""
    kwargs = {
        "is_priority_shipment": False,
        "is_scheduled_delivery_shipment": None,
        "is_pslip_required": False,
        "is_gift": None,
        "ship_method": "",
        "shipment_dates": ShipmentDates(
            **{
                "required_ship_date": datetime(2000, 1, 1),
                "promised_delivery_date": None,
            }
        ),
        "message_to_customer": "",
    }
    obj = ShipmentDetails(**kwargs)
    assert isinstance(obj, ShipmentDetails)


def test_orderdetails_instantiates():
    """Instantiate OrderDetails with dummy data"""
    kwargs = {
        "customer_order_number": "",
        "order_date": datetime(2000, 1, 1),
        "order_status": None,
        "shipment_details": ShipmentDetails(
            **{
                "is_priority_shipment": False,
                "is_scheduled_delivery_shipment": None,
                "is_pslip_required": False,
                "is_gift": None,
                "ship_method": "",
                "shipment_dates": ShipmentDates(
                    **{
                        "required_ship_date": datetime(2000, 1, 1),
                        "promised_delivery_date": None,
                    }
                ),
                "message_to_customer": "",
            }
        ),
        "tax_total": None,
        "selling_party": PartyIdentification(
            **{"party_id": "", "address": None, "tax_info": None}
        ),
        "ship_from_party": PartyIdentification(
            **{"party_id": "", "address": None, "tax_info": None}
        ),
        "ship_to_party": Address(
            **{
                "name": "",
                "attention": None,
                "address_line1": "",
                "address_line2": None,
                "address_line3": None,
                "city": None,
                "county": None,
                "district": None,
                "state_or_region": "",
                "postal_code": None,
                "country_code": "",
                "phone": None,
            }
        ),
        "bill_to_party": PartyIdentification(
            **{"party_id": "", "address": None, "tax_info": None}
        ),
        "items": [],
    }
    obj = OrderDetails(**kwargs)
    assert isinstance(obj, OrderDetails)


def test_order_instantiates():
    """Instantiate Order with dummy data"""
    kwargs = {
        "purchase_order_number": "",
        "order_details": None,
    }
    obj = Order(**kwargs)
    assert isinstance(obj, Order)


def test_orderitemacknowledgement_instantiates():
    """Instantiate OrderItemAcknowledgement with dummy data"""
    kwargs = {
        "item_sequence_number": "",
        "buyer_product_identifier": None,
        "vendor_product_identifier": None,
        "acknowledged_quantity": ItemQuantity(
            **{"amount": None, "unit_of_measure": None}
        ),
    }
    obj = OrderItemAcknowledgement(**kwargs)
    assert isinstance(obj, OrderItemAcknowledgement)


def test_orderacknowledgementitem_instantiates():
    """Instantiate OrderAcknowledgementItem with dummy data"""
    kwargs = {
        "purchase_order_number": "",
        "vendor_order_number": "",
        "acknowledgement_date": datetime(2000, 1, 1),
        "acknowledgement_status": AcknowledgementStatus(
            **{"code": None, "description": None}
        ),
        "selling_party": PartyIdentification(
            **{"party_id": "", "address": None, "tax_info": None}
        ),
        "ship_from_party": PartyIdentification(
            **{"party_id": "", "address": None, "tax_info": None}
        ),
        "item_acknowledgements": [],
    }
    obj = OrderAcknowledgementItem(**kwargs)
    assert isinstance(obj, OrderAcknowledgementItem)


def test_pagination_instantiates():
    """Instantiate Pagination with dummy data"""
    kwargs = {
        "next_token": None,
    }
    obj = Pagination(**kwargs)
    assert isinstance(obj, Pagination)


def test_orderlist_instantiates():
    """Instantiate OrderList with dummy data"""
    kwargs = {
        "pagination": None,
        "orders": None,
    }
    obj = OrderList(**kwargs)
    assert isinstance(obj, OrderList)


def test_submitacknowledgementrequestbody_instantiates():
    """Instantiate SubmitAcknowledgementRequestBody with dummy data"""
    kwargs = {
        "order_acknowledgements": None,
    }
    obj = SubmitAcknowledgementRequestBody(**kwargs)
    assert isinstance(obj, SubmitAcknowledgementRequestBody)


def test_submitacknowledgementrequest_instantiates():
    """Instantiate SubmitAcknowledgementRequest with dummy data"""
    kwargs = {
        "body": SubmitAcknowledgementRequestBody(**{"order_acknowledgements": None}),
    }
    obj = SubmitAcknowledgementRequest(**kwargs)
    assert isinstance(obj, SubmitAcknowledgementRequest)


def test_transactionid_instantiates():
    """Instantiate TransactionId with dummy data"""
    kwargs = {
        "transaction_id": None,
    }
    obj = TransactionId(**kwargs)
    assert isinstance(obj, TransactionId)


def test_submitacknowledgementresponse_instantiates():
    """Instantiate SubmitAcknowledgementResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = SubmitAcknowledgementResponse(**kwargs)
    assert isinstance(obj, SubmitAcknowledgementResponse)


def test_taxdetails_instantiates():
    """Instantiate TaxDetails with dummy data"""
    kwargs = {
        "tax_rate": None,
        "tax_amount": Money(**{"currency_code": None, "amount": None}),
        "taxable_amount": None,
        "type": None,
    }
    obj = TaxDetails(**kwargs)
    assert isinstance(obj, TaxDetails)
