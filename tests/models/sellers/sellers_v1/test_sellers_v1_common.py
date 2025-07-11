# Auto-generated tests for sp_api.api.models.sellers.sellers_v1.common.py
from datetime import datetime

import pytest
from sp_api.api.models.sellers.sellers_v1.common import (
    Account, AccountBusinessTypeEnum, AccountSellingPlanEnum, Address,
    Business, Error, GetAccountResponse, GetMarketplaceParticipationsResponse,
    GetRequestSerializer, Marketplace, MarketplaceParticipation, Participation,
    PrimaryContact, RequestsBaseModel, SpApiBaseModel)


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


def test_address_instantiates():
    """Instantiate Address with dummy data"""
    kwargs = {
        "address_line1": "",
        "address_line2": None,
        "country_code": "",
        "state_or_province_code": None,
        "city": None,
        "postal_code": None,
    }
    obj = Address(**kwargs)
    assert isinstance(obj, Address)


def test_business_instantiates():
    """Instantiate Business with dummy data"""
    kwargs = {
        "name": "",
        "registered_business_address": Address(
            **{
                "address_line1": "",
                "address_line2": None,
                "country_code": "",
                "state_or_province_code": None,
                "city": None,
                "postal_code": None,
            }
        ),
        "company_registration_number": None,
        "company_tax_identification_number": None,
        "non_latin_name": None,
    }
    obj = Business(**kwargs)
    assert isinstance(obj, Business)


def test_primarycontact_instantiates():
    """Instantiate PrimaryContact with dummy data"""
    kwargs = {
        "name": "",
        "address": Address(
            **{
                "address_line1": "",
                "address_line2": None,
                "country_code": "",
                "state_or_province_code": None,
                "city": None,
                "postal_code": None,
            }
        ),
        "non_latin_name": None,
    }
    obj = PrimaryContact(**kwargs)
    assert isinstance(obj, PrimaryContact)


def test_account_instantiates():
    """Instantiate Account with dummy data"""
    kwargs = {
        "marketplace_participation_list": None,
        "business_type": AccountBusinessTypeEnum.CHARITY,
        "selling_plan": AccountSellingPlanEnum.PROFESSIONAL,
        "business": None,
        "primary_contact": None,
    }
    obj = Account(**kwargs)
    assert isinstance(obj, Account)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_getaccountresponse_instantiates():
    """Instantiate GetAccountResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetAccountResponse(**kwargs)
    assert isinstance(obj, GetAccountResponse)


def test_getmarketplaceparticipationsresponse_instantiates():
    """Instantiate GetMarketplaceParticipationsResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetMarketplaceParticipationsResponse(**kwargs)
    assert isinstance(obj, GetMarketplaceParticipationsResponse)


def test_marketplace_instantiates():
    """Instantiate Marketplace with dummy data"""
    kwargs = {
        "id": "",
        "name": "",
        "country_code": "",
        "default_currency_code": "",
        "default_language_code": "",
        "domain_name": "",
    }
    obj = Marketplace(**kwargs)
    assert isinstance(obj, Marketplace)


def test_participation_instantiates():
    """Instantiate Participation with dummy data"""
    kwargs = {
        "is_participating": False,
        "has_suspended_listings": False,
    }
    obj = Participation(**kwargs)
    assert isinstance(obj, Participation)


def test_marketplaceparticipation_instantiates():
    """Instantiate MarketplaceParticipation with dummy data"""
    kwargs = {
        "marketplace": None,
        "participation": Participation(
            **{"is_participating": False, "has_suspended_listings": False}
        ),
        "store_name": "",
    }
    obj = MarketplaceParticipation(**kwargs)
    assert isinstance(obj, MarketplaceParticipation)
