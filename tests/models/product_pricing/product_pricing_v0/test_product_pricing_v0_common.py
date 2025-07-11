# Auto-generated tests for sp_api.api.models.product_pricing.product_pricing_v0.common.py
from datetime import datetime

import pytest
from sp_api.api.models.product_pricing.product_pricing_v0.common import (
    ASINIdentifier, AttributeSetList, BatchOffersRequestParams,
    BatchOffersResponse, BatchRequestBody, BuyBoxPriceType,
    CompetitivePriceType, CompetitivePricingType, DetailedShippingTimeType,
    DetailedShippingTimeTypeAvailabilityTypeEnum, Error, Errors,
    GetCompetitivePricingRequest, GetCompetitivePricingRequestCustomerTypeEnum,
    GetCompetitivePricingRequestItemTypeEnum, GetItemOffersBatchRequest,
    GetItemOffersBatchRequestBody, GetItemOffersBatchResponse,
    GetItemOffersRequest, GetItemOffersRequestCustomerTypeEnum,
    GetItemOffersRequestItemConditionEnum, GetListingOffersBatchRequest,
    GetListingOffersBatchRequestBody, GetListingOffersBatchResponse,
    GetListingOffersRequest, GetListingOffersRequestCustomerTypeEnum,
    GetListingOffersRequestItemConditionEnum, GetOffersHttpStatusLine,
    GetOffersResponse, GetOffersResult, GetPricingRequest,
    GetPricingRequestItemConditionEnum, GetPricingRequestItemTypeEnum,
    GetPricingRequestOfferTypeEnum, GetPricingResponse, GetRequestSerializer,
    HttpRequestHeaders, HttpResponseHeaders, IdentifierType, ItemIdentifier,
    ItemOffersRequestBody, ItemOffersRequestParams, ItemOffersResponse,
    ListingOffersRequestBody, ListingOffersRequestParams,
    ListingOffersResponse, LowestPriceType, MoneyType, OfferCountType,
    OfferDetail, OfferListingCountType, OfferType, Points, Price, PriceType,
    PrimeInformationType, Product, QuantityDiscountPriceType, RelationshipList,
    RequestsBaseModel, SalesRankType, SellerFeedbackType, SellerSKUIdentifier,
    ShipsFromType, SpApiBaseModel, Summary)


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


def test_asinidentifier_instantiates():
    """Instantiate ASINIdentifier with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "a_s_i_n": "",
    }
    obj = ASINIdentifier(**kwargs)
    assert isinstance(obj, ASINIdentifier)


def test_attributesetlist_instantiates():
    """Instantiate AttributeSetList with dummy data"""
    kwargs = {}
    obj = AttributeSetList(**kwargs)
    assert isinstance(obj, AttributeSetList)


def test_batchoffersrequestparams_instantiates():
    """Instantiate BatchOffersRequestParams with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "item_condition": "",
        "customer_type": None,
    }
    obj = BatchOffersRequestParams(**kwargs)
    assert isinstance(obj, BatchOffersRequestParams)


def test_getoffershttpstatusline_instantiates():
    """Instantiate GetOffersHttpStatusLine with dummy data"""
    kwargs = {
        "status_code": None,
        "reason_phrase": None,
    }
    obj = GetOffersHttpStatusLine(**kwargs)
    assert isinstance(obj, GetOffersHttpStatusLine)


def test_itemidentifier_instantiates():
    """Instantiate ItemIdentifier with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "a_s_i_n": None,
        "seller_s_k_u": None,
        "item_condition": "",
    }
    obj = ItemIdentifier(**kwargs)
    assert isinstance(obj, ItemIdentifier)


def test_moneytype_instantiates():
    """Instantiate MoneyType with dummy data"""
    kwargs = {
        "currency_code": None,
        "amount": None,
    }
    obj = MoneyType(**kwargs)
    assert isinstance(obj, MoneyType)


def test_summary_instantiates():
    """Instantiate Summary with dummy data"""
    kwargs = {
        "total_offer_count": 0,
        "number_of_offers": None,
        "lowest_prices": None,
        "buy_box_prices": None,
        "list_price": None,
        "competitive_price_threshold": None,
        "suggested_lower_price_plus_shipping": None,
        "sales_rankings": None,
        "buy_box_eligible_offers": None,
        "offers_available_time": None,
    }
    obj = Summary(**kwargs)
    assert isinstance(obj, Summary)


def test_getoffersresult_instantiates():
    """Instantiate GetOffersResult with dummy data"""
    kwargs = {
        "marketplace_i_d": None,
        "a_s_i_n": None,
        "s_k_u": None,
        "item_condition": "",
        "status": "",
        "identifier": ItemIdentifier(
            **{
                "marketplace_id": None,
                "a_s_i_n": None,
                "seller_s_k_u": None,
                "item_condition": "",
            }
        ),
        "summary": Summary(
            **{
                "total_offer_count": 0,
                "number_of_offers": None,
                "lowest_prices": None,
                "buy_box_prices": None,
                "list_price": None,
                "competitive_price_threshold": None,
                "suggested_lower_price_plus_shipping": None,
                "sales_rankings": None,
                "buy_box_eligible_offers": None,
                "offers_available_time": None,
            }
        ),
        "offers": [],
    }
    obj = GetOffersResult(**kwargs)
    assert isinstance(obj, GetOffersResult)


def test_getoffersresponse_instantiates():
    """Instantiate GetOffersResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetOffersResponse(**kwargs)
    assert isinstance(obj, GetOffersResponse)


def test_httpresponseheaders_instantiates():
    """Instantiate HttpResponseHeaders with dummy data"""
    kwargs = {
        "date": None,
        "x_amzn_request_id": None,
    }
    obj = HttpResponseHeaders(**kwargs)
    assert isinstance(obj, HttpResponseHeaders)


def test_batchoffersresponse_instantiates():
    """Instantiate BatchOffersResponse with dummy data"""
    kwargs = {
        "headers": None,
        "status": None,
        "body": GetOffersResponse(**{"payload": None, "errors": None}),
    }
    obj = BatchOffersResponse(**kwargs)
    assert isinstance(obj, BatchOffersResponse)


def test_httprequestheaders_instantiates():
    """Instantiate HttpRequestHeaders with dummy data"""
    kwargs = {}
    obj = HttpRequestHeaders(**kwargs)
    assert isinstance(obj, HttpRequestHeaders)


def test_batchrequestbody_instantiates():
    """Instantiate BatchRequestBody with dummy data"""
    kwargs = {
        "uri": "",
        "method": "",
        "headers": None,
    }
    obj = BatchRequestBody(**kwargs)
    assert isinstance(obj, BatchRequestBody)


def test_points_instantiates():
    """Instantiate Points with dummy data"""
    kwargs = {
        "points_number": None,
        "points_monetary_value": None,
    }
    obj = Points(**kwargs)
    assert isinstance(obj, Points)


def test_buyboxpricetype_instantiates():
    """Instantiate BuyBoxPriceType with dummy data"""
    kwargs = {
        "condition": "",
        "offer_type": None,
        "quantity_tier": None,
        "quantity_discount_type": None,
        "landed_price": MoneyType(**{"currency_code": None, "amount": None}),
        "listing_price": MoneyType(**{"currency_code": None, "amount": None}),
        "shipping": MoneyType(**{"currency_code": None, "amount": None}),
        "points": None,
        "seller_id": None,
    }
    obj = BuyBoxPriceType(**kwargs)
    assert isinstance(obj, BuyBoxPriceType)


def test_pricetype_instantiates():
    """Instantiate PriceType with dummy data"""
    kwargs = {
        "landed_price": None,
        "listing_price": MoneyType(**{"currency_code": None, "amount": None}),
        "shipping": None,
        "points": None,
    }
    obj = PriceType(**kwargs)
    assert isinstance(obj, PriceType)


def test_competitivepricetype_instantiates():
    """Instantiate CompetitivePriceType with dummy data"""
    kwargs = {
        "competitive_price_id": "",
        "price": PriceType(
            **{
                "landed_price": None,
                "listing_price": MoneyType(**{"currency_code": None, "amount": None}),
                "shipping": None,
                "points": None,
            }
        ),
        "condition": None,
        "subcondition": None,
        "offer_type": None,
        "quantity_tier": None,
        "quantity_discount_type": None,
        "seller_id": None,
        "belongs_to_requester": None,
    }
    obj = CompetitivePriceType(**kwargs)
    assert isinstance(obj, CompetitivePriceType)


def test_competitivepricingtype_instantiates():
    """Instantiate CompetitivePricingType with dummy data"""
    kwargs = {
        "competitive_prices": [],
        "number_of_offer_listings": [],
        "trade_in_value": None,
    }
    obj = CompetitivePricingType(**kwargs)
    assert isinstance(obj, CompetitivePricingType)


def test_detailedshippingtimetype_instantiates():
    """Instantiate DetailedShippingTimeType with dummy data"""
    kwargs = {
        "minimum_hours": None,
        "maximum_hours": None,
        "available_date": None,
        "availability_type": None,
    }
    obj = DetailedShippingTimeType(**kwargs)
    assert isinstance(obj, DetailedShippingTimeType)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_errors_instantiates():
    """Instantiate Errors with dummy data"""
    kwargs = {
        "errors": [],
    }
    obj = Errors(**kwargs)
    assert isinstance(obj, Errors)


def test_getcompetitivepricingrequest_instantiates():
    """Instantiate GetCompetitivePricingRequest with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "asins": None,
        "skus": None,
        "item_type": GetCompetitivePricingRequestItemTypeEnum.ASIN,
        "customer_type": None,
    }
    obj = GetCompetitivePricingRequest(**kwargs)
    assert isinstance(obj, GetCompetitivePricingRequest)


def test_getitemoffersbatchrequestbody_instantiates():
    """Instantiate GetItemOffersBatchRequestBody with dummy data"""
    kwargs = {
        "requests": None,
    }
    obj = GetItemOffersBatchRequestBody(**kwargs)
    assert isinstance(obj, GetItemOffersBatchRequestBody)


def test_getitemoffersbatchrequest_instantiates():
    """Instantiate GetItemOffersBatchRequest with dummy data"""
    kwargs = {
        "get_item_offers_batch_request_body": GetItemOffersBatchRequestBody(
            **{"requests": None}
        ),
    }
    obj = GetItemOffersBatchRequest(**kwargs)
    assert isinstance(obj, GetItemOffersBatchRequest)


def test_getitemoffersbatchresponse_instantiates():
    """Instantiate GetItemOffersBatchResponse with dummy data"""
    kwargs = {
        "responses": None,
    }
    obj = GetItemOffersBatchResponse(**kwargs)
    assert isinstance(obj, GetItemOffersBatchResponse)


def test_getitemoffersrequest_instantiates():
    """Instantiate GetItemOffersRequest with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "item_condition": GetItemOffersRequestItemConditionEnum.NEW,
        "asin": "",
        "customer_type": None,
    }
    obj = GetItemOffersRequest(**kwargs)
    assert isinstance(obj, GetItemOffersRequest)


def test_getlistingoffersbatchrequestbody_instantiates():
    """Instantiate GetListingOffersBatchRequestBody with dummy data"""
    kwargs = {
        "requests": None,
    }
    obj = GetListingOffersBatchRequestBody(**kwargs)
    assert isinstance(obj, GetListingOffersBatchRequestBody)


def test_getlistingoffersbatchrequest_instantiates():
    """Instantiate GetListingOffersBatchRequest with dummy data"""
    kwargs = {
        "get_listing_offers_batch_request_body": GetListingOffersBatchRequestBody(
            **{"requests": None}
        ),
    }
    obj = GetListingOffersBatchRequest(**kwargs)
    assert isinstance(obj, GetListingOffersBatchRequest)


def test_getlistingoffersbatchresponse_instantiates():
    """Instantiate GetListingOffersBatchResponse with dummy data"""
    kwargs = {
        "responses": None,
    }
    obj = GetListingOffersBatchResponse(**kwargs)
    assert isinstance(obj, GetListingOffersBatchResponse)


def test_getlistingoffersrequest_instantiates():
    """Instantiate GetListingOffersRequest with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "item_condition": GetListingOffersRequestItemConditionEnum.NEW,
        "seller_s_k_u": "",
        "customer_type": None,
    }
    obj = GetListingOffersRequest(**kwargs)
    assert isinstance(obj, GetListingOffersRequest)


def test_getpricingrequest_instantiates():
    """Instantiate GetPricingRequest with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "asins": None,
        "skus": None,
        "item_type": GetPricingRequestItemTypeEnum.ASIN,
        "item_condition": None,
        "offer_type": None,
    }
    obj = GetPricingRequest(**kwargs)
    assert isinstance(obj, GetPricingRequest)


def test_getpricingresponse_instantiates():
    """Instantiate GetPricingResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetPricingResponse(**kwargs)
    assert isinstance(obj, GetPricingResponse)


def test_sellerskuidentifier_instantiates():
    """Instantiate SellerSKUIdentifier with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "seller_id": "",
        "seller_s_k_u": "",
    }
    obj = SellerSKUIdentifier(**kwargs)
    assert isinstance(obj, SellerSKUIdentifier)


def test_identifiertype_instantiates():
    """Instantiate IdentifierType with dummy data"""
    kwargs = {
        "marketplace_a_s_i_n": None,
        "s_k_u_identifier": None,
    }
    obj = IdentifierType(**kwargs)
    assert isinstance(obj, IdentifierType)


def test_itemoffersrequestbody_instantiates():
    """Instantiate ItemOffersRequestBody with dummy data"""
    kwargs = {}
    obj = ItemOffersRequestBody(**kwargs)
    assert isinstance(obj, ItemOffersRequestBody)


def test_itemoffersrequestparams_instantiates():
    """Instantiate ItemOffersRequestParams with dummy data"""
    kwargs = {}
    obj = ItemOffersRequestParams(**kwargs)
    assert isinstance(obj, ItemOffersRequestParams)


def test_itemoffersresponse_instantiates():
    """Instantiate ItemOffersResponse with dummy data"""
    kwargs = {}
    obj = ItemOffersResponse(**kwargs)
    assert isinstance(obj, ItemOffersResponse)


def test_listingoffersrequestbody_instantiates():
    """Instantiate ListingOffersRequestBody with dummy data"""
    kwargs = {}
    obj = ListingOffersRequestBody(**kwargs)
    assert isinstance(obj, ListingOffersRequestBody)


def test_listingoffersrequestparams_instantiates():
    """Instantiate ListingOffersRequestParams with dummy data"""
    kwargs = {}
    obj = ListingOffersRequestParams(**kwargs)
    assert isinstance(obj, ListingOffersRequestParams)


def test_listingoffersresponse_instantiates():
    """Instantiate ListingOffersResponse with dummy data"""
    kwargs = {}
    obj = ListingOffersResponse(**kwargs)
    assert isinstance(obj, ListingOffersResponse)


def test_lowestpricetype_instantiates():
    """Instantiate LowestPriceType with dummy data"""
    kwargs = {
        "condition": "",
        "fulfillment_channel": "",
        "offer_type": None,
        "quantity_tier": None,
        "quantity_discount_type": None,
        "landed_price": None,
        "listing_price": MoneyType(**{"currency_code": None, "amount": None}),
        "shipping": None,
        "points": None,
    }
    obj = LowestPriceType(**kwargs)
    assert isinstance(obj, LowestPriceType)


def test_offercounttype_instantiates():
    """Instantiate OfferCountType with dummy data"""
    kwargs = {
        "condition": None,
        "fulfillment_channel": None,
        "offer_count": None,
    }
    obj = OfferCountType(**kwargs)
    assert isinstance(obj, OfferCountType)


def test_primeinformationtype_instantiates():
    """Instantiate PrimeInformationType with dummy data"""
    kwargs = {
        "is_prime": False,
        "is_national_prime": False,
    }
    obj = PrimeInformationType(**kwargs)
    assert isinstance(obj, PrimeInformationType)


def test_quantitydiscountpricetype_instantiates():
    """Instantiate QuantityDiscountPriceType with dummy data"""
    kwargs = {
        "quantity_tier": 0,
        "quantity_discount_type": "",
        "listing_price": MoneyType(**{"currency_code": None, "amount": None}),
    }
    obj = QuantityDiscountPriceType(**kwargs)
    assert isinstance(obj, QuantityDiscountPriceType)


def test_sellerfeedbacktype_instantiates():
    """Instantiate SellerFeedbackType with dummy data"""
    kwargs = {
        "seller_positive_feedback_rating": None,
        "feedback_count": 0,
    }
    obj = SellerFeedbackType(**kwargs)
    assert isinstance(obj, SellerFeedbackType)


def test_shipsfromtype_instantiates():
    """Instantiate ShipsFromType with dummy data"""
    kwargs = {
        "state": None,
        "country": None,
    }
    obj = ShipsFromType(**kwargs)
    assert isinstance(obj, ShipsFromType)


def test_offerdetail_instantiates():
    """Instantiate OfferDetail with dummy data"""
    kwargs = {
        "my_offer": None,
        "offer_type": None,
        "sub_condition": "",
        "seller_id": None,
        "condition_notes": None,
        "seller_feedback_rating": None,
        "shipping_time": DetailedShippingTimeType(
            **{
                "minimum_hours": None,
                "maximum_hours": None,
                "available_date": None,
                "availability_type": None,
            }
        ),
        "listing_price": MoneyType(**{"currency_code": None, "amount": None}),
        "quantity_discount_prices": None,
        "points": None,
        "shipping": MoneyType(**{"currency_code": None, "amount": None}),
        "ships_from": None,
        "is_fulfilled_by_amazon": False,
        "prime_information": None,
        "is_buy_box_winner": None,
        "is_featured_merchant": None,
    }
    obj = OfferDetail(**kwargs)
    assert isinstance(obj, OfferDetail)


def test_offerlistingcounttype_instantiates():
    """Instantiate OfferListingCountType with dummy data"""
    kwargs = {
        "count": 0,
        "condition": "",
    }
    obj = OfferListingCountType(**kwargs)
    assert isinstance(obj, OfferListingCountType)


def test_offertype_instantiates():
    """Instantiate OfferType with dummy data"""
    kwargs = {
        "offer_type": None,
        "buying_price": PriceType(
            **{
                "landed_price": None,
                "listing_price": MoneyType(**{"currency_code": None, "amount": None}),
                "shipping": None,
                "points": None,
            }
        ),
        "regular_price": MoneyType(**{"currency_code": None, "amount": None}),
        "business_price": None,
        "quantity_discount_prices": None,
        "fulfillment_channel": "",
        "item_condition": "",
        "item_sub_condition": "",
        "seller_s_k_u": "",
    }
    obj = OfferType(**kwargs)
    assert isinstance(obj, OfferType)


def test_relationshiplist_instantiates():
    """Instantiate RelationshipList with dummy data"""
    kwargs = {}
    obj = RelationshipList(**kwargs)
    assert isinstance(obj, RelationshipList)


def test_product_instantiates():
    """Instantiate Product with dummy data"""
    kwargs = {
        "identifiers": IdentifierType(
            **{"marketplace_a_s_i_n": None, "s_k_u_identifier": None}
        ),
        "attribute_sets": None,
        "relationships": None,
        "competitive_pricing": None,
        "sales_rankings": None,
        "offers": None,
    }
    obj = Product(**kwargs)
    assert isinstance(obj, Product)


def test_price_instantiates():
    """Instantiate Price with dummy data"""
    kwargs = {
        "status": "",
        "seller_s_k_u": None,
        "a_s_i_n": None,
        "product": None,
    }
    obj = Price(**kwargs)
    assert isinstance(obj, Price)


def test_salesranktype_instantiates():
    """Instantiate SalesRankType with dummy data"""
    kwargs = {
        "product_category_id": "",
        "rank": 0,
    }
    obj = SalesRankType(**kwargs)
    assert isinstance(obj, SalesRankType)
