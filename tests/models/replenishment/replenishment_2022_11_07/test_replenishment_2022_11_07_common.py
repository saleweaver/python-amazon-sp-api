# Auto-generated tests for sp_api.api.models.replenishment.replenishment_2022_11_07.common.py
from datetime import datetime

import pytest
from sp_api.api.models.replenishment.replenishment_2022_11_07.common import (
    DiscountFunding, Error, ErrorList, GetRequestSerializer,
    GetSellingPartnerMetricsRequest, GetSellingPartnerMetricsRequestBody,
    GetSellingPartnerMetricsResponse, GetSellingPartnerMetricsResponseMetric,
    ListOfferMetricsRequest, ListOfferMetricsRequestBody,
    ListOfferMetricsRequestFilters, ListOfferMetricsRequestPagination,
    ListOfferMetricsRequestSort, ListOfferMetricsResponse,
    ListOfferMetricsResponseOffer, ListOffersRequest, ListOffersRequestBody,
    ListOffersRequestFilters, ListOffersRequestPagination,
    ListOffersRequestSort, ListOffersResponse, ListOffersResponseOffer,
    OfferProgramConfiguration, OfferProgramConfigurationPreferences,
    OfferProgramConfigurationPromotions,
    OfferProgramConfigurationPromotionsDiscountFunding, PaginationResponse,
    Preference, Promotion, RequestsBaseModel, SpApiBaseModel, TimeInterval)


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


def test_discountfunding_instantiates():
    """Instantiate DiscountFunding with dummy data"""
    kwargs = {
        "percentage": None,
    }
    obj = DiscountFunding(**kwargs)
    assert isinstance(obj, DiscountFunding)


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


def test_timeinterval_instantiates():
    """Instantiate TimeInterval with dummy data"""
    kwargs = {
        "start_date": datetime(2000, 1, 1),
        "end_date": datetime(2000, 1, 1),
    }
    obj = TimeInterval(**kwargs)
    assert isinstance(obj, TimeInterval)


def test_getsellingpartnermetricsrequestbody_instantiates():
    """Instantiate GetSellingPartnerMetricsRequestBody with dummy data"""
    kwargs = {
        "aggregation_frequency": None,
        "time_interval": TimeInterval(
            **{"start_date": datetime(2000, 1, 1), "end_date": datetime(2000, 1, 1)}
        ),
        "metrics": None,
        "time_period_type": "",
        "marketplace_id": None,
        "program_types": [],
    }
    obj = GetSellingPartnerMetricsRequestBody(**kwargs)
    assert isinstance(obj, GetSellingPartnerMetricsRequestBody)


def test_getsellingpartnermetricsrequest_instantiates():
    """Instantiate GetSellingPartnerMetricsRequest with dummy data"""
    kwargs = {
        "body": None,
    }
    obj = GetSellingPartnerMetricsRequest(**kwargs)
    assert isinstance(obj, GetSellingPartnerMetricsRequest)


def test_getsellingpartnermetricsresponsemetric_instantiates():
    """Instantiate GetSellingPartnerMetricsResponseMetric with dummy data"""
    kwargs = {
        "not_delivered_due_to_o_o_s": None,
        "total_subscriptions_revenue": None,
        "shipped_subscription_units": None,
        "active_subscriptions": None,
        "subscriber_average_revenue": None,
        "non_subscriber_average_revenue": None,
        "lost_revenue_due_to_o_o_s": None,
        "subscriber_average_reorders": None,
        "non_subscriber_average_reorders": None,
        "coupons_revenue_penetration": None,
        "revenue_from_subscriptions_with_multiple_deliveries": None,
        "revenue_from_active_subscriptions_with_single_delivery": None,
        "revenue_from_cancelled_subscriptions_after_single_delivery": None,
        "subscriber_retention_for30_days": None,
        "subscriber_retention_for90_days": None,
        "revenue_penetration_for0_percent_seller_funding": None,
        "revenue_penetration_for5_percent_seller_funding": None,
        "revenue_penetration_for10_percent_seller_funding": None,
        "revenue_penetration_for5_plus_percent_seller_funding": None,
        "share_of_coupon_subscriptions": None,
        "time_interval": None,
        "currency_code": None,
    }
    obj = GetSellingPartnerMetricsResponseMetric(**kwargs)
    assert isinstance(obj, GetSellingPartnerMetricsResponseMetric)


def test_getsellingpartnermetricsresponse_instantiates():
    """Instantiate GetSellingPartnerMetricsResponse with dummy data"""
    kwargs = {
        "metrics": None,
    }
    obj = GetSellingPartnerMetricsResponse(**kwargs)
    assert isinstance(obj, GetSellingPartnerMetricsResponse)


def test_listoffermetricsrequestfilters_instantiates():
    """Instantiate ListOfferMetricsRequestFilters with dummy data"""
    kwargs = {
        "aggregation_frequency": None,
        "time_interval": TimeInterval(
            **{"start_date": datetime(2000, 1, 1), "end_date": datetime(2000, 1, 1)}
        ),
        "time_period_type": "",
        "marketplace_id": None,
        "program_types": [],
        "asins": None,
    }
    obj = ListOfferMetricsRequestFilters(**kwargs)
    assert isinstance(obj, ListOfferMetricsRequestFilters)


def test_listoffermetricsrequestpagination_instantiates():
    """Instantiate ListOfferMetricsRequestPagination with dummy data"""
    kwargs = {
        "limit": 0,
        "offset": 0,
    }
    obj = ListOfferMetricsRequestPagination(**kwargs)
    assert isinstance(obj, ListOfferMetricsRequestPagination)


def test_listoffermetricsrequestsort_instantiates():
    """Instantiate ListOfferMetricsRequestSort with dummy data"""
    kwargs = {
        "order": "",
        "key": "",
    }
    obj = ListOfferMetricsRequestSort(**kwargs)
    assert isinstance(obj, ListOfferMetricsRequestSort)


def test_listoffermetricsrequestbody_instantiates():
    """Instantiate ListOfferMetricsRequestBody with dummy data"""
    kwargs = {
        "pagination": ListOfferMetricsRequestPagination(**{"limit": 0, "offset": 0}),
        "sort": None,
        "filters": ListOfferMetricsRequestFilters(
            **{
                "aggregation_frequency": None,
                "time_interval": TimeInterval(
                    **{
                        "start_date": datetime(2000, 1, 1),
                        "end_date": datetime(2000, 1, 1),
                    }
                ),
                "time_period_type": "",
                "marketplace_id": None,
                "program_types": [],
                "asins": None,
            }
        ),
    }
    obj = ListOfferMetricsRequestBody(**kwargs)
    assert isinstance(obj, ListOfferMetricsRequestBody)


def test_listoffermetricsrequest_instantiates():
    """Instantiate ListOfferMetricsRequest with dummy data"""
    kwargs = {
        "body": None,
    }
    obj = ListOfferMetricsRequest(**kwargs)
    assert isinstance(obj, ListOfferMetricsRequest)


def test_listoffermetricsresponseoffer_instantiates():
    """Instantiate ListOfferMetricsResponseOffer with dummy data"""
    kwargs = {
        "asin": None,
        "not_delivered_due_to_o_o_s": None,
        "total_subscriptions_revenue": None,
        "shipped_subscription_units": None,
        "active_subscriptions": None,
        "revenue_penetration": None,
        "lost_revenue_due_to_o_o_s": None,
        "coupons_revenue_penetration": None,
        "share_of_coupon_subscriptions": None,
        "next30_day_total_subscriptions_revenue": None,
        "next60_day_total_subscriptions_revenue": None,
        "next90_day_total_subscriptions_revenue": None,
        "next30_day_shipped_subscription_units": None,
        "next60_day_shipped_subscription_units": None,
        "next90_day_shipped_subscription_units": None,
        "time_interval": None,
        "currency_code": None,
    }
    obj = ListOfferMetricsResponseOffer(**kwargs)
    assert isinstance(obj, ListOfferMetricsResponseOffer)


def test_paginationresponse_instantiates():
    """Instantiate PaginationResponse with dummy data"""
    kwargs = {
        "total_results": None,
    }
    obj = PaginationResponse(**kwargs)
    assert isinstance(obj, PaginationResponse)


def test_listoffermetricsresponse_instantiates():
    """Instantiate ListOfferMetricsResponse with dummy data"""
    kwargs = {
        "offers": None,
        "pagination": None,
    }
    obj = ListOfferMetricsResponse(**kwargs)
    assert isinstance(obj, ListOfferMetricsResponse)


def test_preference_instantiates():
    """Instantiate Preference with dummy data"""
    kwargs = {
        "auto_enrollment": None,
    }
    obj = Preference(**kwargs)
    assert isinstance(obj, Preference)


def test_promotion_instantiates():
    """Instantiate Promotion with dummy data"""
    kwargs = {
        "selling_partner_funded_base_discount": None,
        "selling_partner_funded_tiered_discount": None,
        "amazon_funded_base_discount": None,
        "amazon_funded_tiered_discount": None,
    }
    obj = Promotion(**kwargs)
    assert isinstance(obj, Promotion)


def test_listoffersrequestfilters_instantiates():
    """Instantiate ListOffersRequestFilters with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "skus": None,
        "asins": None,
        "eligibilities": None,
        "preferences": None,
        "promotions": None,
        "program_types": [],
    }
    obj = ListOffersRequestFilters(**kwargs)
    assert isinstance(obj, ListOffersRequestFilters)


def test_listoffersrequestpagination_instantiates():
    """Instantiate ListOffersRequestPagination with dummy data"""
    kwargs = {
        "limit": 0,
        "offset": 0,
    }
    obj = ListOffersRequestPagination(**kwargs)
    assert isinstance(obj, ListOffersRequestPagination)


def test_listoffersrequestsort_instantiates():
    """Instantiate ListOffersRequestSort with dummy data"""
    kwargs = {
        "order": "",
        "key": "",
    }
    obj = ListOffersRequestSort(**kwargs)
    assert isinstance(obj, ListOffersRequestSort)


def test_listoffersrequestbody_instantiates():
    """Instantiate ListOffersRequestBody with dummy data"""
    kwargs = {
        "pagination": ListOffersRequestPagination(**{"limit": 0, "offset": 0}),
        "filters": ListOffersRequestFilters(
            **{
                "marketplace_id": None,
                "skus": None,
                "asins": None,
                "eligibilities": None,
                "preferences": None,
                "promotions": None,
                "program_types": [],
            }
        ),
        "sort": None,
    }
    obj = ListOffersRequestBody(**kwargs)
    assert isinstance(obj, ListOffersRequestBody)


def test_listoffersrequest_instantiates():
    """Instantiate ListOffersRequest with dummy data"""
    kwargs = {
        "body": None,
    }
    obj = ListOffersRequest(**kwargs)
    assert isinstance(obj, ListOffersRequest)


def test_offerprogramconfigurationpreferences_instantiates():
    """Instantiate OfferProgramConfigurationPreferences with dummy data"""
    kwargs = {
        "auto_enrollment": None,
    }
    obj = OfferProgramConfigurationPreferences(**kwargs)
    assert isinstance(obj, OfferProgramConfigurationPreferences)


def test_offerprogramconfigurationpromotionsdiscountfunding_instantiates():
    """Instantiate OfferProgramConfigurationPromotionsDiscountFunding with dummy data"""
    kwargs = {
        "percentage": None,
    }
    obj = OfferProgramConfigurationPromotionsDiscountFunding(**kwargs)
    assert isinstance(obj, OfferProgramConfigurationPromotionsDiscountFunding)


def test_offerprogramconfigurationpromotions_instantiates():
    """Instantiate OfferProgramConfigurationPromotions with dummy data"""
    kwargs = {
        "selling_partner_funded_base_discount": None,
        "selling_partner_funded_tiered_discount": None,
        "amazon_funded_base_discount": None,
        "amazon_funded_tiered_discount": None,
    }
    obj = OfferProgramConfigurationPromotions(**kwargs)
    assert isinstance(obj, OfferProgramConfigurationPromotions)


def test_offerprogramconfiguration_instantiates():
    """Instantiate OfferProgramConfiguration with dummy data"""
    kwargs = {
        "preferences": None,
        "promotions": None,
        "enrollment_method": None,
    }
    obj = OfferProgramConfiguration(**kwargs)
    assert isinstance(obj, OfferProgramConfiguration)


def test_listoffersresponseoffer_instantiates():
    """Instantiate ListOffersResponseOffer with dummy data"""
    kwargs = {
        "sku": None,
        "asin": None,
        "marketplace_id": None,
        "eligibility": None,
        "offer_program_configuration": None,
        "program_type": None,
        "vendor_codes": None,
    }
    obj = ListOffersResponseOffer(**kwargs)
    assert isinstance(obj, ListOffersResponseOffer)


def test_listoffersresponse_instantiates():
    """Instantiate ListOffersResponse with dummy data"""
    kwargs = {
        "offers": None,
        "pagination": None,
    }
    obj = ListOffersResponse(**kwargs)
    assert isinstance(obj, ListOffersResponse)
