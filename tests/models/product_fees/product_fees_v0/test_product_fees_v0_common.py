# Auto-generated tests for sp_api.api.models.product_fees.product_fees_v0.common.py
from datetime import datetime

import pytest
from sp_api.api.models.product_fees.product_fees_v0.common import (
    Error, FeeDetail, FeesEstimate, FeesEstimateByIdRequestBody,
    FeesEstimateError, FeesEstimateErrorDetail, FeesEstimateIdentifier,
    FeesEstimateRequestBody, FeesEstimateResult,
    GetMyFeesEstimateForASINRequest, GetMyFeesEstimateForSKURequest,
    GetMyFeesEstimateRequestBody, GetMyFeesEstimateResponse,
    GetMyFeesEstimateResult, GetMyFeesEstimatesErrorList,
    GetMyFeesEstimatesRequest, GetRequestSerializer, IncludedFeeDetail,
    MoneyType, Points, PriceToEstimateFees, RequestsBaseModel, SpApiBaseModel)


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


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_moneytype_instantiates():
    """Instantiate MoneyType with dummy data"""
    kwargs = {
        "currency_code": None,
        "amount": None,
    }
    obj = MoneyType(**kwargs)
    assert isinstance(obj, MoneyType)


def test_feedetail_instantiates():
    """Instantiate FeeDetail with dummy data"""
    kwargs = {
        "fee_type": "",
        "fee_amount": MoneyType(**{"currency_code": None, "amount": None}),
        "fee_promotion": None,
        "tax_amount": None,
        "final_fee": MoneyType(**{"currency_code": None, "amount": None}),
        "included_fee_detail_list": None,
    }
    obj = FeeDetail(**kwargs)
    assert isinstance(obj, FeeDetail)


def test_feesestimate_instantiates():
    """Instantiate FeesEstimate with dummy data"""
    kwargs = {
        "time_of_fees_estimation": datetime(2000, 1, 1),
        "total_fees_estimate": None,
        "fee_detail_list": None,
    }
    obj = FeesEstimate(**kwargs)
    assert isinstance(obj, FeesEstimate)


def test_points_instantiates():
    """Instantiate Points with dummy data"""
    kwargs = {
        "points_number": None,
        "points_monetary_value": None,
    }
    obj = Points(**kwargs)
    assert isinstance(obj, Points)


def test_pricetoestimatefees_instantiates():
    """Instantiate PriceToEstimateFees with dummy data"""
    kwargs = {
        "listing_price": MoneyType(**{"currency_code": None, "amount": None}),
        "shipping": None,
        "points": None,
    }
    obj = PriceToEstimateFees(**kwargs)
    assert isinstance(obj, PriceToEstimateFees)


def test_feesestimaterequestbody_instantiates():
    """Instantiate FeesEstimateRequestBody with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "is_amazon_fulfilled": None,
        "price_to_estimate_fees": PriceToEstimateFees(
            **{
                "listing_price": MoneyType(**{"currency_code": None, "amount": None}),
                "shipping": None,
                "points": None,
            }
        ),
        "identifier": "",
        "optional_fulfillment_program": None,
    }
    obj = FeesEstimateRequestBody(**kwargs)
    assert isinstance(obj, FeesEstimateRequestBody)


def test_feesestimatebyidrequestbody_instantiates():
    """Instantiate FeesEstimateByIdRequestBody with dummy data"""
    kwargs = {
        "fees_estimate_request_body": None,
        "id_type": "",
        "id_value": "",
    }
    obj = FeesEstimateByIdRequestBody(**kwargs)
    assert isinstance(obj, FeesEstimateByIdRequestBody)


def test_feesestimateerrordetail_instantiates():
    """Instantiate FeesEstimateErrorDetail with dummy data"""
    kwargs = {}
    obj = FeesEstimateErrorDetail(**kwargs)
    assert isinstance(obj, FeesEstimateErrorDetail)


def test_feesestimateerror_instantiates():
    """Instantiate FeesEstimateError with dummy data"""
    kwargs = {
        "type": "",
        "code": "",
        "message": "",
        "detail": FeesEstimateErrorDetail(**{}),
    }
    obj = FeesEstimateError(**kwargs)
    assert isinstance(obj, FeesEstimateError)


def test_feesestimateidentifier_instantiates():
    """Instantiate FeesEstimateIdentifier with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "seller_id": None,
        "id_type": None,
        "id_value": None,
        "is_amazon_fulfilled": None,
        "price_to_estimate_fees": None,
        "seller_input_identifier": None,
        "optional_fulfillment_program": None,
    }
    obj = FeesEstimateIdentifier(**kwargs)
    assert isinstance(obj, FeesEstimateIdentifier)


def test_feesestimateresult_instantiates():
    """Instantiate FeesEstimateResult with dummy data"""
    kwargs = {
        "status": None,
        "fees_estimate_identifier": None,
        "fees_estimate": None,
        "error": None,
    }
    obj = FeesEstimateResult(**kwargs)
    assert isinstance(obj, FeesEstimateResult)


def test_getmyfeesestimaterequestbody_instantiates():
    """Instantiate GetMyFeesEstimateRequestBody with dummy data"""
    kwargs = {
        "fees_estimate_request_body": None,
    }
    obj = GetMyFeesEstimateRequestBody(**kwargs)
    assert isinstance(obj, GetMyFeesEstimateRequestBody)


def test_getmyfeesestimateforasinrequest_instantiates():
    """Instantiate GetMyFeesEstimateForASINRequest with dummy data"""
    kwargs = {
        "body": GetMyFeesEstimateRequestBody(**{"fees_estimate_request_body": None}),
        "asin": "",
    }
    obj = GetMyFeesEstimateForASINRequest(**kwargs)
    assert isinstance(obj, GetMyFeesEstimateForASINRequest)


def test_getmyfeesestimateforskurequest_instantiates():
    """Instantiate GetMyFeesEstimateForSKURequest with dummy data"""
    kwargs = {
        "body": GetMyFeesEstimateRequestBody(**{"fees_estimate_request_body": None}),
        "seller_s_k_u": "",
    }
    obj = GetMyFeesEstimateForSKURequest(**kwargs)
    assert isinstance(obj, GetMyFeesEstimateForSKURequest)


def test_getmyfeesestimateresult_instantiates():
    """Instantiate GetMyFeesEstimateResult with dummy data"""
    kwargs = {
        "fees_estimate_result": None,
    }
    obj = GetMyFeesEstimateResult(**kwargs)
    assert isinstance(obj, GetMyFeesEstimateResult)


def test_getmyfeesestimateresponse_instantiates():
    """Instantiate GetMyFeesEstimateResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetMyFeesEstimateResponse(**kwargs)
    assert isinstance(obj, GetMyFeesEstimateResponse)


def test_getmyfeesestimateserrorlist_instantiates():
    """Instantiate GetMyFeesEstimatesErrorList with dummy data"""
    kwargs = {
        "errors": [],
    }
    obj = GetMyFeesEstimatesErrorList(**kwargs)
    assert isinstance(obj, GetMyFeesEstimatesErrorList)


def test_getmyfeesestimatesrequest_instantiates():
    """Instantiate GetMyFeesEstimatesRequest with dummy data"""
    kwargs = {
        "body": [],
    }
    obj = GetMyFeesEstimatesRequest(**kwargs)
    assert isinstance(obj, GetMyFeesEstimatesRequest)


def test_includedfeedetail_instantiates():
    """Instantiate IncludedFeeDetail with dummy data"""
    kwargs = {
        "fee_type": "",
        "fee_amount": MoneyType(**{"currency_code": None, "amount": None}),
        "fee_promotion": None,
        "tax_amount": None,
        "final_fee": MoneyType(**{"currency_code": None, "amount": None}),
    }
    obj = IncludedFeeDetail(**kwargs)
    assert isinstance(obj, IncludedFeeDetail)
