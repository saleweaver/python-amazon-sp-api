# Auto-generated tests for sp_api.api.models.vendor_orders.vendor_orders_v1.common.py
from datetime import datetime

import pytest
from sp_api.api.models.vendor_orders.vendor_orders_v1.common import (
    AcknowledgementStatusDetails, Address, Error, GetPurchaseOrderRequest,
    GetPurchaseOrderResponse, GetPurchaseOrdersRequest,
    GetPurchaseOrdersRequestPoItemStateEnum,
    GetPurchaseOrdersRequestPurchaseOrderStateEnum,
    GetPurchaseOrdersRequestSortOrderEnum, GetPurchaseOrdersResponse,
    GetPurchaseOrdersStatusRequest,
    GetPurchaseOrdersStatusRequestItemConfirmationStatusEnum,
    GetPurchaseOrdersStatusRequestItemReceiveStatusEnum,
    GetPurchaseOrdersStatusRequestPurchaseOrderStatusEnum,
    GetPurchaseOrdersStatusRequestSortOrderEnum,
    GetPurchaseOrdersStatusResponse, GetRequestSerializer, ImportDetails,
    ImportDetailsInternationalCommercialTermsEnum,
    ImportDetailsMethodOfPaymentEnum, ItemQuantity,
    ItemQuantityUnitOfMeasureEnum, Money, MoneyUnitOfMeasureEnum, Order,
    OrderAcknowledgement, OrderAcknowledgementItem, OrderDetails,
    OrderDetailsPaymentMethodEnum, OrderDetailsPurchaseOrderTypeEnum,
    OrderedQuantityDetails, OrderItem, OrderItemAcknowledgement,
    OrderItemAcknowledgementAcknowledgementCodeEnum,
    OrderItemAcknowledgementRejectionReasonEnum, OrderItemStatus, OrderList,
    OrderListStatus, OrderPurchaseOrderStateEnum, OrderStatus,
    OrderStatusPurchaseOrderStatusEnum, Pagination, PartyIdentification,
    RequestsBaseModel, SpApiBaseModel, SubmitAcknowledgementRequest,
    SubmitAcknowledgementRequestBody, SubmitAcknowledgementResponse,
    TaxRegistrationDetails, TaxRegistrationDetailsTaxRegistrationTypeEnum,
    TransactionId)


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


def test_itemquantity_instantiates():
    """Instantiate ItemQuantity with dummy data"""
    kwargs = {
        "amount": None,
        "unit_of_measure": None,
        "unit_size": None,
    }
    obj = ItemQuantity(**kwargs)
    assert isinstance(obj, ItemQuantity)


def test_acknowledgementstatusdetails_instantiates():
    """Instantiate AcknowledgementStatusDetails with dummy data"""
    kwargs = {
        "acknowledgement_date": None,
        "accepted_quantity": None,
        "rejected_quantity": None,
    }
    obj = AcknowledgementStatusDetails(**kwargs)
    assert isinstance(obj, AcknowledgementStatusDetails)


def test_address_instantiates():
    """Instantiate Address with dummy data"""
    kwargs = {
        "name": "",
        "address_line1": "",
        "address_line2": None,
        "address_line3": None,
        "city": None,
        "county": None,
        "district": None,
        "state_or_region": None,
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


def test_getpurchaseorderrequest_instantiates():
    """Instantiate GetPurchaseOrderRequest with dummy data"""
    kwargs = {
        "purchase_order_number": "",
    }
    obj = GetPurchaseOrderRequest(**kwargs)
    assert isinstance(obj, GetPurchaseOrderRequest)


def test_importdetails_instantiates():
    """Instantiate ImportDetails with dummy data"""
    kwargs = {
        "method_of_payment": None,
        "international_commercial_terms": None,
        "port_of_delivery": None,
        "import_containers": None,
        "shipping_instructions": None,
    }
    obj = ImportDetails(**kwargs)
    assert isinstance(obj, ImportDetails)


def test_money_instantiates():
    """Instantiate Money with dummy data"""
    kwargs = {
        "currency_code": None,
        "amount": None,
        "unit_of_measure": None,
    }
    obj = Money(**kwargs)
    assert isinstance(obj, Money)


def test_orderitem_instantiates():
    """Instantiate OrderItem with dummy data"""
    kwargs = {
        "item_sequence_number": "",
        "amazon_product_identifier": None,
        "vendor_product_identifier": None,
        "ordered_quantity": ItemQuantity(
            **{"amount": None, "unit_of_measure": None, "unit_size": None}
        ),
        "is_back_order_allowed": False,
        "net_cost": None,
        "list_price": None,
    }
    obj = OrderItem(**kwargs)
    assert isinstance(obj, OrderItem)


def test_taxregistrationdetails_instantiates():
    """Instantiate TaxRegistrationDetails with dummy data"""
    kwargs = {
        "tax_registration_type": TaxRegistrationDetailsTaxRegistrationTypeEnum.VAT,
        "tax_registration_number": "",
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


def test_orderdetails_instantiates():
    """Instantiate OrderDetails with dummy data"""
    kwargs = {
        "purchase_order_date": datetime(2000, 1, 1),
        "purchase_order_changed_date": None,
        "purchase_order_state_changed_date": datetime(2000, 1, 1),
        "purchase_order_type": None,
        "import_details": None,
        "deal_code": None,
        "payment_method": None,
        "buying_party": None,
        "selling_party": None,
        "ship_to_party": None,
        "bill_to_party": None,
        "ship_window": None,
        "delivery_window": None,
        "items": [],
    }
    obj = OrderDetails(**kwargs)
    assert isinstance(obj, OrderDetails)


def test_order_instantiates():
    """Instantiate Order with dummy data"""
    kwargs = {
        "purchase_order_number": "",
        "purchase_order_state": OrderPurchaseOrderStateEnum.NEW,
        "order_details": None,
    }
    obj = Order(**kwargs)
    assert isinstance(obj, Order)


def test_getpurchaseorderresponse_instantiates():
    """Instantiate GetPurchaseOrderResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetPurchaseOrderResponse(**kwargs)
    assert isinstance(obj, GetPurchaseOrderResponse)


def test_getpurchaseordersrequest_instantiates():
    """Instantiate GetPurchaseOrdersRequest with dummy data"""
    kwargs = {
        "limit": None,
        "created_after": None,
        "created_before": None,
        "sort_order": None,
        "next_token": None,
        "include_details": None,
        "changed_after": None,
        "changed_before": None,
        "po_item_state": None,
        "is_p_o_changed": None,
        "purchase_order_state": None,
        "ordering_vendor_code": None,
    }
    obj = GetPurchaseOrdersRequest(**kwargs)
    assert isinstance(obj, GetPurchaseOrdersRequest)


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


def test_getpurchaseordersresponse_instantiates():
    """Instantiate GetPurchaseOrdersResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetPurchaseOrdersResponse(**kwargs)
    assert isinstance(obj, GetPurchaseOrdersResponse)


def test_getpurchaseordersstatusrequest_instantiates():
    """Instantiate GetPurchaseOrdersStatusRequest with dummy data"""
    kwargs = {
        "limit": None,
        "sort_order": None,
        "next_token": None,
        "created_after": None,
        "created_before": None,
        "updated_after": None,
        "updated_before": None,
        "purchase_order_number": None,
        "purchase_order_status": None,
        "item_confirmation_status": None,
        "item_receive_status": None,
        "ordering_vendor_code": None,
        "ship_to_party_id": None,
    }
    obj = GetPurchaseOrdersStatusRequest(**kwargs)
    assert isinstance(obj, GetPurchaseOrdersStatusRequest)


def test_orderstatus_instantiates():
    """Instantiate OrderStatus with dummy data"""
    kwargs = {
        "purchase_order_number": "",
        "purchase_order_status": OrderStatusPurchaseOrderStatusEnum.OPEN,
        "purchase_order_date": datetime(2000, 1, 1),
        "last_updated_date": None,
        "selling_party": PartyIdentification(
            **{"party_id": "", "address": None, "tax_info": None}
        ),
        "ship_to_party": PartyIdentification(
            **{"party_id": "", "address": None, "tax_info": None}
        ),
        "item_status": [],
    }
    obj = OrderStatus(**kwargs)
    assert isinstance(obj, OrderStatus)


def test_orderliststatus_instantiates():
    """Instantiate OrderListStatus with dummy data"""
    kwargs = {
        "pagination": None,
        "orders_status": None,
    }
    obj = OrderListStatus(**kwargs)
    assert isinstance(obj, OrderListStatus)


def test_getpurchaseordersstatusresponse_instantiates():
    """Instantiate GetPurchaseOrdersStatusResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetPurchaseOrdersStatusResponse(**kwargs)
    assert isinstance(obj, GetPurchaseOrdersStatusResponse)


def test_orderitemacknowledgement_instantiates():
    """Instantiate OrderItemAcknowledgement with dummy data"""
    kwargs = {
        "acknowledgement_code": OrderItemAcknowledgementAcknowledgementCodeEnum.ACCEPTED,
        "acknowledged_quantity": ItemQuantity(
            **{"amount": None, "unit_of_measure": None, "unit_size": None}
        ),
        "scheduled_ship_date": None,
        "scheduled_delivery_date": None,
        "rejection_reason": None,
    }
    obj = OrderItemAcknowledgement(**kwargs)
    assert isinstance(obj, OrderItemAcknowledgement)


def test_orderacknowledgementitem_instantiates():
    """Instantiate OrderAcknowledgementItem with dummy data"""
    kwargs = {
        "item_sequence_number": None,
        "amazon_product_identifier": None,
        "vendor_product_identifier": None,
        "ordered_quantity": ItemQuantity(
            **{"amount": None, "unit_of_measure": None, "unit_size": None}
        ),
        "net_cost": None,
        "list_price": None,
        "discount_multiplier": None,
        "item_acknowledgements": [],
    }
    obj = OrderAcknowledgementItem(**kwargs)
    assert isinstance(obj, OrderAcknowledgementItem)


def test_orderacknowledgement_instantiates():
    """Instantiate OrderAcknowledgement with dummy data"""
    kwargs = {
        "purchase_order_number": "",
        "selling_party": PartyIdentification(
            **{"party_id": "", "address": None, "tax_info": None}
        ),
        "acknowledgement_date": datetime(2000, 1, 1),
        "items": [],
    }
    obj = OrderAcknowledgement(**kwargs)
    assert isinstance(obj, OrderAcknowledgement)


def test_orderitemstatus_instantiates():
    """Instantiate OrderItemStatus with dummy data"""
    kwargs = {
        "item_sequence_number": "",
        "buyer_product_identifier": None,
        "vendor_product_identifier": None,
        "net_cost": None,
        "list_price": None,
        "ordered_quantity": None,
        "acknowledgement_status": None,
        "receiving_status": None,
    }
    obj = OrderItemStatus(**kwargs)
    assert isinstance(obj, OrderItemStatus)


def test_orderedquantitydetails_instantiates():
    """Instantiate OrderedQuantityDetails with dummy data"""
    kwargs = {
        "updated_date": None,
        "ordered_quantity": None,
        "cancelled_quantity": None,
    }
    obj = OrderedQuantityDetails(**kwargs)
    assert isinstance(obj, OrderedQuantityDetails)


def test_submitacknowledgementrequestbody_instantiates():
    """Instantiate SubmitAcknowledgementRequestBody with dummy data"""
    kwargs = {
        "acknowledgements": None,
    }
    obj = SubmitAcknowledgementRequestBody(**kwargs)
    assert isinstance(obj, SubmitAcknowledgementRequestBody)


def test_submitacknowledgementrequest_instantiates():
    """Instantiate SubmitAcknowledgementRequest with dummy data"""
    kwargs = {
        "body": SubmitAcknowledgementRequestBody(**{"acknowledgements": None}),
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
