# Auto-generated tests for sp_api.api.models.vehicles.vehicles_2024_11_01.common.py
from datetime import datetime

import pytest
from sp_api.api.models.vehicles.vehicles_2024_11_01.common import (
    EngineOutput, Error, ErrorList, GetRequestSerializer, GetVehiclesRequest,
    MonthAndYear, Pagination, RequestsBaseModel, SpApiBaseModel, Vehicle,
    VehicleIdentifiers, VehiclesResponse, VehicleTypeEnum)


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


def test_engineoutput_instantiates():
    """Instantiate EngineOutput with dummy data"""
    kwargs = {
        "value": 0.0,
        "unit": "",
    }
    obj = EngineOutput(**kwargs)
    assert isinstance(obj, EngineOutput)


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


def test_getvehiclesrequest_instantiates():
    """Instantiate GetVehiclesRequest with dummy data"""
    kwargs = {
        "page_token": None,
        "marketplace_id": None,
        "vehicle_type": VehicleTypeEnum.CAR,
        "updated_after": None,
    }
    obj = GetVehiclesRequest(**kwargs)
    assert isinstance(obj, GetVehiclesRequest)


def test_monthandyear_instantiates():
    """Instantiate MonthAndYear with dummy data"""
    kwargs = {
        "year": None,
        "month": None,
    }
    obj = MonthAndYear(**kwargs)
    assert isinstance(obj, MonthAndYear)


def test_pagination_instantiates():
    """Instantiate Pagination with dummy data"""
    kwargs = {
        "next_token": None,
        "previous_token": None,
    }
    obj = Pagination(**kwargs)
    assert isinstance(obj, Pagination)


def test_vehicleidentifiers_instantiates():
    """Instantiate VehicleIdentifiers with dummy data"""
    kwargs = {
        "standard": "",
        "value": "",
    }
    obj = VehicleIdentifiers(**kwargs)
    assert isinstance(obj, VehicleIdentifiers)


def test_vehicle_instantiates():
    """Instantiate Vehicle with dummy data"""
    kwargs = {
        "make": "",
        "model": "",
        "variant_name": None,
        "body_style": None,
        "drive_type": None,
        "energy": None,
        "engine_output": None,
        "manufacturing_start_date": None,
        "manufacturing_stop_date": None,
        "last_processed_date": None,
        "status": None,
        "identifiers": [],
    }
    obj = Vehicle(**kwargs)
    assert isinstance(obj, Vehicle)


def test_vehiclesresponse_instantiates():
    """Instantiate VehiclesResponse with dummy data"""
    kwargs = {
        "pagination": None,
        "vehicles": [],
    }
    obj = VehiclesResponse(**kwargs)
    assert isinstance(obj, VehiclesResponse)
