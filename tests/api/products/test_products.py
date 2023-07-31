import traceback

from sp_api.api.products.products import Products
from sp_api.api.products.products_definitions import GetListingOffersBatchRequest, ListingOffersRequest
from sp_api.base import ApiResponse, Marketplaces, SellingApiBadRequestException


def test_pricing_for_sku():
    res = Products().get_product_pricing_for_skus([], MarketplaceId="ATVPDKIKX0DER")
    assert res.payload[0].get('status') == 'Success'


def test_pricing_for_asin():
    res = Products().get_product_pricing_for_asins([], MarketplaceId="ATVPDKIKX0DER")
    assert res.payload[0].get('status') == 'Success'


def test_pricing_for_asin_expect_400():
    try:
        Products().get_product_pricing_for_asins(['TEST_CASE_400'], MarketplaceId='TEST_CASE_400')
    except SellingApiBadRequestException:
        pass


def test_competitive_pricing_for_sku():
    res = Products().get_competitive_pricing_for_skus([], MarketplaceId="ATVPDKIKX0DER")
    assert res.payload[0].get('status') == 'Success'


def test_competitive_pricing_for_asin():
    res = Products().get_competitive_pricing_for_asins([], MarketplaceId="ATVPDKIKX0DER")
    assert res.payload[0].get('status') == 'Success'


def test_get_item_offers_batch():
    res = Products().get_item_offers_batch(requests_=[
        {
            "uri": "/products/pricing/v0/items/B000P6Q7MY/offers",
            "method": "GET",
            "MarketplaceId": "ATVPDKIKX0DER",
            "ItemCondition": "New",
            "CustomerType": "Consumer"
        },
        {
            "uri": "/products/pricing/v0/items/B001Q3KU9Q/offers",
            "method": "GET",
            "MarketplaceId": "ATVPDKIKX0DER",
            "ItemCondition": "New",
            "CustomerType": "Consumer"
        },
        {
            "uri": "/products/pricing/v0/items/B007Z07UK6/offers",
            "method": "GET",
            "MarketplaceId": "ATVPDKIKX0DER",
            "ItemCondition": "New",
            "CustomerType": "Consumer"
        },
        {
            "uri": "/products/pricing/v0/items/B000OQA3N4/offers",
            "method": "GET",
            "MarketplaceId": "ATVPDKIKX0DER",
            "ItemCondition": "New",
            "CustomerType": "Consumer"
        },
        {
            "uri": "/products/pricing/v0/items/B07PTMKYS7/offers",
            "method": "GET",
            "MarketplaceId": "ATVPDKIKX0DER",
            "ItemCondition": "New",
            "CustomerType": "Consumer"
        },
        {
            "uri": "/products/pricing/v0/items/B001PYUTII/offers",
            "method": "GET",
            "MarketplaceId": "ATVPDKIKX0DER",
            "ItemCondition": "New",
            "CustomerType": "Consumer"
        },
        {
            "uri": "/products/pricing/v0/items/B00505DW2I/offers",
            "method": "GET",
            "MarketplaceId": "ATVPDKIKX0DER",
            "ItemCondition": "New",
            "CustomerType": "Consumer"
        },
        {
            "uri": "/products/pricing/v0/items/B00CGZQU42/offers",
            "method": "GET",
            "MarketplaceId": "ATVPDKIKX0DER",
            "ItemCondition": "New",
            "CustomerType": "Consumer"
        },
        {
            "uri": "/products/pricing/v0/items/B01LY2ZYRF/offers",
            "method": "GET",
            "MarketplaceId": "ATVPDKIKX0DER",
            "ItemCondition": "New",
            "CustomerType": "Consumer"
        },
        {
            "uri": "/products/pricing/v0/items/B00KFRNZY6/offers",
            "method": "GET",
            "MarketplaceId": "ATVPDKIKX0DER",
            "ItemCondition": "New",
            "CustomerType": "Consumer"
        }
    ])
    assert res.errors is None
    assert isinstance(res, ApiResponse)

def test_get_listing_offers_batch():
    reqs = [
        ListingOffersRequest(
            uri="/products/pricing/v0/listings/GC-QTMS-SV2I/offers",
            MarketplaceId='ATVPDKIKX0DER',
            ItemCondition='New'
        ),
        ListingOffersRequest(
            uri="/products/pricing/v0/listings/VT-DEIT-57TQ/offers",
            MarketplaceId='ATVPDKIKX0DER',
            ItemCondition='New'
        ),
        ListingOffersRequest(
            uri="/products/pricing/v0/listings/NA-H7X1-JYTM/offers",
            MarketplaceId='ATVPDKIKX0DER',
            ItemCondition='New'
        ),
        ListingOffersRequest(
            uri="/products/pricing/v0/listings/RL-JVOC-MBSL/offers",
            MarketplaceId='ATVPDKIKX0DER',
            ItemCondition='New'
        ),
        ListingOffersRequest(
            uri="/products/pricing/v0/listings/74-64KG-H9W9/offers",
            MarketplaceId='ATVPDKIKX0DER',
            ItemCondition='New'
        ),
    ]

    batch_req = GetListingOffersBatchRequest(reqs)
    res = Products().get_listing_offers_batch(batch_req)
    assert res.errors is None
    assert isinstance(res, ApiResponse)