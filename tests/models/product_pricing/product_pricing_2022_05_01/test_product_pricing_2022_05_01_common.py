# Auto-generated tests for sp_api.api.models.product_pricing.product_pricing_2022_05_01.common.py
from datetime import datetime

import pytest
from sp_api.api.models.product_pricing.product_pricing_2022_05_01.common import (
    BatchRequestBody, BatchResponse, BuyingOptionTypeEnum,
    CompetitiveSummaryBatchRequestBody, CompetitiveSummaryBatchResponse,
    CompetitiveSummaryRequestBody, CompetitiveSummaryResponse,
    CompetitiveSummaryResponseBody, CustomerMembershipEnum, EligibilityEnum,
    Error, Errors, FeaturedBuyingOption, FeaturedOffer,
    FeaturedOfferExpectedPrice, FeaturedOfferExpectedPriceRequestBody,
    FeaturedOfferExpectedPriceRequestParams,
    FeaturedOfferExpectedPriceResponse, FeaturedOfferExpectedPriceResponseBody,
    FeaturedOfferExpectedPriceResult, FeaturedOfferSegment,
    GetCompetitiveSummaryRequest, GetFeaturedOfferExpectedPriceBatchRequest,
    GetFeaturedOfferExpectedPriceBatchRequestBody,
    GetFeaturedOfferExpectedPriceBatchResponse, GetRequestSerializer, HttpBody,
    HttpHeaders, HttpStatusLine, LowestPricedOffer, LowestPricedOffersInput,
    MoneyType, Offer, OfferIdentifier, OfferTypeEnum, Points, PostalCode,
    Price, PrimeDetails, ReferencePrice, RequestsBaseModel, SampleLocation,
    Segment, SegmentDetails, SegmentedFeaturedOffer, ShippingOption,
    ShippingOptionTypeEnum, SpApiBaseModel, SubConditionEnum)


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


def test_httpbody_instantiates():
    """Instantiate HttpBody with dummy data"""
    kwargs = {}
    obj = HttpBody(**kwargs)
    assert isinstance(obj, HttpBody)


def test_httpheaders_instantiates():
    """Instantiate HttpHeaders with dummy data"""
    kwargs = {}
    obj = HttpHeaders(**kwargs)
    assert isinstance(obj, HttpHeaders)


def test_batchrequestbody_instantiates():
    """Instantiate BatchRequestBody with dummy data"""
    kwargs = {
        "uri": "",
        "method": "",
        "body": None,
        "headers": None,
    }
    obj = BatchRequestBody(**kwargs)
    assert isinstance(obj, BatchRequestBody)


def test_httpstatusline_instantiates():
    """Instantiate HttpStatusLine with dummy data"""
    kwargs = {
        "status_code": None,
        "reason_phrase": None,
    }
    obj = HttpStatusLine(**kwargs)
    assert isinstance(obj, HttpStatusLine)


def test_batchresponse_instantiates():
    """Instantiate BatchResponse with dummy data"""
    kwargs = {
        "headers": HttpHeaders(**{}),
        "status": HttpStatusLine(**{"status_code": None, "reason_phrase": None}),
    }
    obj = BatchResponse(**kwargs)
    assert isinstance(obj, BatchResponse)


def test_competitivesummarybatchrequestbody_instantiates():
    """Instantiate CompetitiveSummaryBatchRequestBody with dummy data"""
    kwargs = {
        "requests": [],
    }
    obj = CompetitiveSummaryBatchRequestBody(**kwargs)
    assert isinstance(obj, CompetitiveSummaryBatchRequestBody)


def test_competitivesummarybatchresponse_instantiates():
    """Instantiate CompetitiveSummaryBatchResponse with dummy data"""
    kwargs = {
        "responses": [],
    }
    obj = CompetitiveSummaryBatchResponse(**kwargs)
    assert isinstance(obj, CompetitiveSummaryBatchResponse)


def test_lowestpricedoffersinput_instantiates():
    """Instantiate LowestPricedOffersInput with dummy data"""
    kwargs = {
        "item_condition": "",
        "offer_type": OfferTypeEnum.CONSUMER,
    }
    obj = LowestPricedOffersInput(**kwargs)
    assert isinstance(obj, LowestPricedOffersInput)


def test_competitivesummaryrequestbody_instantiates():
    """Instantiate CompetitiveSummaryRequestBody with dummy data"""
    kwargs = {
        "asin": "",
        "marketplace_id": None,
        "included_data": [],
        "lowest_priced_offers_inputs": None,
        "method": "",
        "uri": "",
    }
    obj = CompetitiveSummaryRequestBody(**kwargs)
    assert isinstance(obj, CompetitiveSummaryRequestBody)


def test_segmentedfeaturedoffer_instantiates():
    """Instantiate SegmentedFeaturedOffer with dummy data"""
    kwargs = {}
    obj = SegmentedFeaturedOffer(**kwargs)
    assert isinstance(obj, SegmentedFeaturedOffer)


def test_featuredbuyingoption_instantiates():
    """Instantiate FeaturedBuyingOption with dummy data"""
    kwargs = {
        "buying_option_type": BuyingOptionTypeEnum.NEW,
        "segmented_featured_offers": [],
    }
    obj = FeaturedBuyingOption(**kwargs)
    assert isinstance(obj, FeaturedBuyingOption)


def test_moneytype_instantiates():
    """Instantiate MoneyType with dummy data"""
    kwargs = {
        "currency_code": None,
        "amount": None,
    }
    obj = MoneyType(**kwargs)
    assert isinstance(obj, MoneyType)


def test_points_instantiates():
    """Instantiate Points with dummy data"""
    kwargs = {
        "points_number": None,
        "points_monetary_value": None,
    }
    obj = Points(**kwargs)
    assert isinstance(obj, Points)


def test_primedetails_instantiates():
    """Instantiate PrimeDetails with dummy data"""
    kwargs = {
        "eligibility": EligibilityEnum.NATIONAL,
    }
    obj = PrimeDetails(**kwargs)
    assert isinstance(obj, PrimeDetails)


def test_shippingoption_instantiates():
    """Instantiate ShippingOption with dummy data"""
    kwargs = {
        "shipping_option_type": ShippingOptionTypeEnum.DEFAULT,
        "price": MoneyType(**{"currency_code": None, "amount": None}),
    }
    obj = ShippingOption(**kwargs)
    assert isinstance(obj, ShippingOption)


def test_offer_instantiates():
    """Instantiate Offer with dummy data"""
    kwargs = {
        "seller_id": "",
        "condition": "",
        "sub_condition": None,
        "fulfillment_type": "",
        "listing_price": MoneyType(**{"currency_code": None, "amount": None}),
        "shipping_options": None,
        "points": None,
        "prime_details": None,
    }
    obj = Offer(**kwargs)
    assert isinstance(obj, Offer)


def test_lowestpricedoffer_instantiates():
    """Instantiate LowestPricedOffer with dummy data"""
    kwargs = {
        "lowest_priced_offers_input": LowestPricedOffersInput(
            **{"item_condition": "", "offer_type": OfferTypeEnum.CONSUMER}
        ),
        "offers": [],
    }
    obj = LowestPricedOffer(**kwargs)
    assert isinstance(obj, LowestPricedOffer)


def test_referenceprice_instantiates():
    """Instantiate ReferencePrice with dummy data"""
    kwargs = {
        "name": "",
        "price": MoneyType(**{"currency_code": None, "amount": None}),
    }
    obj = ReferencePrice(**kwargs)
    assert isinstance(obj, ReferencePrice)


def test_competitivesummaryresponsebody_instantiates():
    """Instantiate CompetitiveSummaryResponseBody with dummy data"""
    kwargs = {
        "asin": "",
        "marketplace_id": None,
        "featured_buying_options": None,
        "lowest_priced_offers": None,
        "reference_prices": None,
        "errors": None,
    }
    obj = CompetitiveSummaryResponseBody(**kwargs)
    assert isinstance(obj, CompetitiveSummaryResponseBody)


def test_competitivesummaryresponse_instantiates():
    """Instantiate CompetitiveSummaryResponse with dummy data"""
    kwargs = {
        "status": HttpStatusLine(**{"status_code": None, "reason_phrase": None}),
        "body": CompetitiveSummaryResponseBody(
            **{
                "asin": "",
                "marketplace_id": None,
                "featured_buying_options": None,
                "lowest_priced_offers": None,
                "reference_prices": None,
                "errors": None,
            }
        ),
    }
    obj = CompetitiveSummaryResponse(**kwargs)
    assert isinstance(obj, CompetitiveSummaryResponse)


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


def test_offeridentifier_instantiates():
    """Instantiate OfferIdentifier with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "seller_id": None,
        "sku": None,
        "asin": "",
        "fulfillment_type": None,
    }
    obj = OfferIdentifier(**kwargs)
    assert isinstance(obj, OfferIdentifier)


def test_price_instantiates():
    """Instantiate Price with dummy data"""
    kwargs = {
        "listing_price": MoneyType(**{"currency_code": None, "amount": None}),
        "shipping_price": None,
        "points": None,
    }
    obj = Price(**kwargs)
    assert isinstance(obj, Price)


def test_featuredoffer_instantiates():
    """Instantiate FeaturedOffer with dummy data"""
    kwargs = {
        "offer_identifier": OfferIdentifier(
            **{
                "marketplace_id": None,
                "seller_id": None,
                "sku": None,
                "asin": "",
                "fulfillment_type": None,
            }
        ),
        "condition": None,
        "price": None,
    }
    obj = FeaturedOffer(**kwargs)
    assert isinstance(obj, FeaturedOffer)


def test_featuredofferexpectedprice_instantiates():
    """Instantiate FeaturedOfferExpectedPrice with dummy data"""
    kwargs = {
        "listing_price": MoneyType(**{"currency_code": None, "amount": None}),
        "points": None,
    }
    obj = FeaturedOfferExpectedPrice(**kwargs)
    assert isinstance(obj, FeaturedOfferExpectedPrice)


def test_featuredofferexpectedpricerequestbody_instantiates():
    """Instantiate FeaturedOfferExpectedPriceRequestBody with dummy data"""
    kwargs = {}
    obj = FeaturedOfferExpectedPriceRequestBody(**kwargs)
    assert isinstance(obj, FeaturedOfferExpectedPriceRequestBody)


def test_postalcode_instantiates():
    """Instantiate PostalCode with dummy data"""
    kwargs = {
        "country_code": None,
        "value": None,
    }
    obj = PostalCode(**kwargs)
    assert isinstance(obj, PostalCode)


def test_samplelocation_instantiates():
    """Instantiate SampleLocation with dummy data"""
    kwargs = {
        "postal_code": None,
    }
    obj = SampleLocation(**kwargs)
    assert isinstance(obj, SampleLocation)


def test_segmentdetails_instantiates():
    """Instantiate SegmentDetails with dummy data"""
    kwargs = {
        "glance_view_weight_percentage": None,
        "sample_location": None,
    }
    obj = SegmentDetails(**kwargs)
    assert isinstance(obj, SegmentDetails)


def test_segment_instantiates():
    """Instantiate Segment with dummy data"""
    kwargs = {
        "segment_details": None,
    }
    obj = Segment(**kwargs)
    assert isinstance(obj, Segment)


def test_featuredofferexpectedpricerequestparams_instantiates():
    """Instantiate FeaturedOfferExpectedPriceRequestParams with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "sku": "",
        "segment": None,
    }
    obj = FeaturedOfferExpectedPriceRequestParams(**kwargs)
    assert isinstance(obj, FeaturedOfferExpectedPriceRequestParams)


def test_featuredofferexpectedpriceresponse_instantiates():
    """Instantiate FeaturedOfferExpectedPriceResponse with dummy data"""
    kwargs = {}
    obj = FeaturedOfferExpectedPriceResponse(**kwargs)
    assert isinstance(obj, FeaturedOfferExpectedPriceResponse)


def test_featuredofferexpectedpriceresponsebody_instantiates():
    """Instantiate FeaturedOfferExpectedPriceResponseBody with dummy data"""
    kwargs = {
        "offer_identifier": None,
        "featured_offer_expected_price_results": None,
        "errors": None,
    }
    obj = FeaturedOfferExpectedPriceResponseBody(**kwargs)
    assert isinstance(obj, FeaturedOfferExpectedPriceResponseBody)


def test_featuredofferexpectedpriceresult_instantiates():
    """Instantiate FeaturedOfferExpectedPriceResult with dummy data"""
    kwargs = {
        "featured_offer_expected_price": None,
        "result_status": "",
        "competing_featured_offer": None,
        "current_featured_offer": None,
    }
    obj = FeaturedOfferExpectedPriceResult(**kwargs)
    assert isinstance(obj, FeaturedOfferExpectedPriceResult)


def test_featuredoffersegment_instantiates():
    """Instantiate FeaturedOfferSegment with dummy data"""
    kwargs = {
        "customer_membership": CustomerMembershipEnum.PRIME,
        "segment_details": SegmentDetails(
            **{"glance_view_weight_percentage": None, "sample_location": None}
        ),
    }
    obj = FeaturedOfferSegment(**kwargs)
    assert isinstance(obj, FeaturedOfferSegment)


def test_getcompetitivesummaryrequest_instantiates():
    """Instantiate GetCompetitiveSummaryRequest with dummy data"""
    kwargs = {
        "requests": CompetitiveSummaryBatchRequestBody(**{"requests": []}),
    }
    obj = GetCompetitiveSummaryRequest(**kwargs)
    assert isinstance(obj, GetCompetitiveSummaryRequest)


def test_getfeaturedofferexpectedpricebatchrequestbody_instantiates():
    """Instantiate GetFeaturedOfferExpectedPriceBatchRequestBody with dummy data"""
    kwargs = {
        "requests": None,
    }
    obj = GetFeaturedOfferExpectedPriceBatchRequestBody(**kwargs)
    assert isinstance(obj, GetFeaturedOfferExpectedPriceBatchRequestBody)


def test_getfeaturedofferexpectedpricebatchrequest_instantiates():
    """Instantiate GetFeaturedOfferExpectedPriceBatchRequest with dummy data"""
    kwargs = {
        "get_featured_offer_expected_price_batch_request_body": GetFeaturedOfferExpectedPriceBatchRequestBody(
            **{"requests": None}
        ),
    }
    obj = GetFeaturedOfferExpectedPriceBatchRequest(**kwargs)
    assert isinstance(obj, GetFeaturedOfferExpectedPriceBatchRequest)


def test_getfeaturedofferexpectedpricebatchresponse_instantiates():
    """Instantiate GetFeaturedOfferExpectedPriceBatchResponse with dummy data"""
    kwargs = {
        "responses": None,
    }
    obj = GetFeaturedOfferExpectedPriceBatchResponse(**kwargs)
    assert isinstance(obj, GetFeaturedOfferExpectedPriceBatchResponse)
