# Auto-generated tests for sp_api.api.models.finances.finances_2024_06_19.common.py
from datetime import datetime

import pytest
from sp_api.api.models.finances.finances_2024_06_19.common import (
    AmazonPayContext, Breakdown, BusinessContext, BusinessContextStoreNameEnum,
    Context, Currency, DeferredContext, Error, ErrorList, GetRequestSerializer,
    Item, ItemRelatedIdentifier,
    ItemRelatedIdentifierItemRelatedIdentifierNameEnum,
    ListTransactionsRequest, ListTransactionsResponse, MarketplaceDetails,
    PaymentsContext, ProductContext, RelatedIdentifier,
    RelatedIdentifierRelatedIdentifierNameEnum, RequestsBaseModel,
    SellingPartnerMetadata, SpApiBaseModel, TimeRangeContext, Transaction,
    TransactionsPayload)


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


def test_amazonpaycontext_instantiates():
    """Instantiate AmazonPayContext with dummy data"""
    kwargs = {
        "store_name": None,
        "order_type": None,
        "channel": None,
    }
    obj = AmazonPayContext(**kwargs)
    assert isinstance(obj, AmazonPayContext)


def test_currency_instantiates():
    """Instantiate Currency with dummy data"""
    kwargs = {
        "currency_code": None,
        "currency_amount": None,
    }
    obj = Currency(**kwargs)
    assert isinstance(obj, Currency)


def test_breakdown_instantiates():
    """Instantiate Breakdown with dummy data"""
    kwargs = {
        "breakdown_type": None,
        "breakdown_amount": None,
        "breakdowns": None,
    }
    obj = Breakdown(**kwargs)
    assert isinstance(obj, Breakdown)


def test_businesscontext_instantiates():
    """Instantiate BusinessContext with dummy data"""
    kwargs = {
        "store_name": None,
    }
    obj = BusinessContext(**kwargs)
    assert isinstance(obj, BusinessContext)


def test_context_instantiates():
    """Instantiate Context with dummy data"""
    kwargs = {}
    obj = Context(**kwargs)
    assert isinstance(obj, Context)


def test_deferredcontext_instantiates():
    """Instantiate DeferredContext with dummy data"""
    kwargs = {
        "deferral_reason": None,
        "maturity_date": None,
    }
    obj = DeferredContext(**kwargs)
    assert isinstance(obj, DeferredContext)


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


def test_item_instantiates():
    """Instantiate Item with dummy data"""
    kwargs = {
        "description": None,
        "related_identifiers": None,
        "total_amount": None,
        "breakdowns": None,
        "contexts": None,
    }
    obj = Item(**kwargs)
    assert isinstance(obj, Item)


def test_itemrelatedidentifier_instantiates():
    """Instantiate ItemRelatedIdentifier with dummy data"""
    kwargs = {
        "item_related_identifier_name": None,
        "item_related_identifier_value": None,
    }
    obj = ItemRelatedIdentifier(**kwargs)
    assert isinstance(obj, ItemRelatedIdentifier)


def test_listtransactionsrequest_instantiates():
    """Instantiate ListTransactionsRequest with dummy data"""
    kwargs = {
        "posted_after": datetime(2000, 1, 1),
        "posted_before": None,
        "marketplace_id": None,
        "transaction_status": None,
        "next_token": None,
    }
    obj = ListTransactionsRequest(**kwargs)
    assert isinstance(obj, ListTransactionsRequest)


def test_transactionspayload_instantiates():
    """Instantiate TransactionsPayload with dummy data"""
    kwargs = {
        "next_token": None,
        "transactions": None,
    }
    obj = TransactionsPayload(**kwargs)
    assert isinstance(obj, TransactionsPayload)


def test_listtransactionsresponse_instantiates():
    """Instantiate ListTransactionsResponse with dummy data"""
    kwargs = {
        "payload": None,
    }
    obj = ListTransactionsResponse(**kwargs)
    assert isinstance(obj, ListTransactionsResponse)


def test_marketplacedetails_instantiates():
    """Instantiate MarketplaceDetails with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "marketplace_name": None,
    }
    obj = MarketplaceDetails(**kwargs)
    assert isinstance(obj, MarketplaceDetails)


def test_paymentscontext_instantiates():
    """Instantiate PaymentsContext with dummy data"""
    kwargs = {
        "payment_type": None,
        "payment_method": None,
        "payment_reference": None,
        "payment_date": None,
    }
    obj = PaymentsContext(**kwargs)
    assert isinstance(obj, PaymentsContext)


def test_productcontext_instantiates():
    """Instantiate ProductContext with dummy data"""
    kwargs = {
        "asin": None,
        "sku": None,
        "quantity_shipped": None,
        "fulfillment_network": None,
    }
    obj = ProductContext(**kwargs)
    assert isinstance(obj, ProductContext)


def test_relatedidentifier_instantiates():
    """Instantiate RelatedIdentifier with dummy data"""
    kwargs = {
        "related_identifier_name": None,
        "related_identifier_value": None,
    }
    obj = RelatedIdentifier(**kwargs)
    assert isinstance(obj, RelatedIdentifier)


def test_sellingpartnermetadata_instantiates():
    """Instantiate SellingPartnerMetadata with dummy data"""
    kwargs = {
        "selling_partner_id": None,
        "account_type": None,
        "marketplace_id": None,
    }
    obj = SellingPartnerMetadata(**kwargs)
    assert isinstance(obj, SellingPartnerMetadata)


def test_timerangecontext_instantiates():
    """Instantiate TimeRangeContext with dummy data"""
    kwargs = {
        "start_time": None,
        "end_time": None,
    }
    obj = TimeRangeContext(**kwargs)
    assert isinstance(obj, TimeRangeContext)


def test_transaction_instantiates():
    """Instantiate Transaction with dummy data"""
    kwargs = {
        "selling_partner_metadata": None,
        "related_identifiers": None,
        "transaction_type": None,
        "transaction_id": None,
        "transaction_status": None,
        "description": None,
        "posted_date": None,
        "total_amount": None,
        "marketplace_details": None,
        "items": None,
        "contexts": None,
        "breakdowns": None,
    }
    obj = Transaction(**kwargs)
    assert isinstance(obj, Transaction)
