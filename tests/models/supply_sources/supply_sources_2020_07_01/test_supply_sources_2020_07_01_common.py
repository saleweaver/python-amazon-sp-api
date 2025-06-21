# Auto-generated tests for sp_api.api.models.supply_sources.supply_sources_2020_07_01.common.py
from datetime import datetime

import pytest
from sp_api.api.models.supply_sources.supply_sources_2020_07_01.common import (
    Address, AddressWithContact, ArchiveSupplySourceRequest, ContactDetails,
    CreateSupplySourceRequest, CreateSupplySourceRequestBody,
    CreateSupplySourceResponse, CurbsidePickupConfiguration, DeliveryChannel,
    Duration, Error, ErrorList, GetRequestSerializer, GetSupplySourceRequest,
    GetSupplySourcesRequest, GetSupplySourcesResponse,
    InStorePickupConfiguration, OperatingHour, OperatingHoursByDay,
    OperationalConfiguration, OutboundCapability, ParkingConfiguration,
    ParkingWithAddressConfiguration, PickupChannel, RequestsBaseModel,
    ReturnLocation, ServicesCapability, SpApiBaseModel, SupplySource,
    SupplySourceCapabilities, SupplySourceConfiguration, SupplySourceList,
    ThroughputCap, ThroughputConfig, UpdateSupplySourceRequest,
    UpdateSupplySourceRequestBody, UpdateSupplySourceStatusRequest,
    UpdateSupplySourceStatusRequestBody)


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
        "name": "",
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


def test_contactdetails_instantiates():
    """Instantiate ContactDetails with dummy data"""
    kwargs = {
        "primary": None,
    }
    obj = ContactDetails(**kwargs)
    assert isinstance(obj, ContactDetails)


def test_addresswithcontact_instantiates():
    """Instantiate AddressWithContact with dummy data"""
    kwargs = {
        "contact_details": None,
        "address": None,
    }
    obj = AddressWithContact(**kwargs)
    assert isinstance(obj, AddressWithContact)


def test_archivesupplysourcerequest_instantiates():
    """Instantiate ArchiveSupplySourceRequest with dummy data"""
    kwargs = {
        "supply_source_id": "",
    }
    obj = ArchiveSupplySourceRequest(**kwargs)
    assert isinstance(obj, ArchiveSupplySourceRequest)


def test_createsupplysourcerequestbody_instantiates():
    """Instantiate CreateSupplySourceRequestBody with dummy data"""
    kwargs = {
        "supply_source_code": "",
        "alias": "",
        "address": Address(
            **{
                "name": "",
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
    }
    obj = CreateSupplySourceRequestBody(**kwargs)
    assert isinstance(obj, CreateSupplySourceRequestBody)


def test_createsupplysourcerequest_instantiates():
    """Instantiate CreateSupplySourceRequest with dummy data"""
    kwargs = {
        "payload": CreateSupplySourceRequestBody(
            **{
                "supply_source_code": "",
                "alias": "",
                "address": Address(
                    **{
                        "name": "",
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
            }
        ),
    }
    obj = CreateSupplySourceRequest(**kwargs)
    assert isinstance(obj, CreateSupplySourceRequest)


def test_createsupplysourceresponse_instantiates():
    """Instantiate CreateSupplySourceResponse with dummy data"""
    kwargs = {
        "supply_source_id": "",
        "supply_source_code": "",
    }
    obj = CreateSupplySourceResponse(**kwargs)
    assert isinstance(obj, CreateSupplySourceResponse)


def test_duration_instantiates():
    """Instantiate Duration with dummy data"""
    kwargs = {
        "value": None,
        "time_unit": None,
    }
    obj = Duration(**kwargs)
    assert isinstance(obj, Duration)


def test_operatinghoursbyday_instantiates():
    """Instantiate OperatingHoursByDay with dummy data"""
    kwargs = {
        "monday": None,
        "tuesday": None,
        "wednesday": None,
        "thursday": None,
        "friday": None,
        "saturday": None,
        "sunday": None,
    }
    obj = OperatingHoursByDay(**kwargs)
    assert isinstance(obj, OperatingHoursByDay)


def test_throughputcap_instantiates():
    """Instantiate ThroughputCap with dummy data"""
    kwargs = {
        "value": None,
        "time_unit": None,
    }
    obj = ThroughputCap(**kwargs)
    assert isinstance(obj, ThroughputCap)


def test_throughputconfig_instantiates():
    """Instantiate ThroughputConfig with dummy data"""
    kwargs = {
        "throughput_cap": None,
        "throughput_unit": "",
    }
    obj = ThroughputConfig(**kwargs)
    assert isinstance(obj, ThroughputConfig)


def test_operationalconfiguration_instantiates():
    """Instantiate OperationalConfiguration with dummy data"""
    kwargs = {
        "contact_details": None,
        "throughput_config": None,
        "operating_hours_by_day": None,
        "handling_time": None,
    }
    obj = OperationalConfiguration(**kwargs)
    assert isinstance(obj, OperationalConfiguration)


def test_parkingwithaddressconfiguration_instantiates():
    """Instantiate ParkingWithAddressConfiguration with dummy data"""
    kwargs = {}
    obj = ParkingWithAddressConfiguration(**kwargs)
    assert isinstance(obj, ParkingWithAddressConfiguration)


def test_curbsidepickupconfiguration_instantiates():
    """Instantiate CurbsidePickupConfiguration with dummy data"""
    kwargs = {
        "is_supported": None,
        "operational_configuration": None,
        "parking_with_address_configuration": None,
    }
    obj = CurbsidePickupConfiguration(**kwargs)
    assert isinstance(obj, CurbsidePickupConfiguration)


def test_deliverychannel_instantiates():
    """Instantiate DeliveryChannel with dummy data"""
    kwargs = {
        "is_supported": None,
        "operational_configuration": None,
    }
    obj = DeliveryChannel(**kwargs)
    assert isinstance(obj, DeliveryChannel)


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


def test_getsupplysourcerequest_instantiates():
    """Instantiate GetSupplySourceRequest with dummy data"""
    kwargs = {
        "supply_source_id": "",
    }
    obj = GetSupplySourceRequest(**kwargs)
    assert isinstance(obj, GetSupplySourceRequest)


def test_getsupplysourcesrequest_instantiates():
    """Instantiate GetSupplySourcesRequest with dummy data"""
    kwargs = {
        "next_page_token": None,
        "page_size": None,
    }
    obj = GetSupplySourcesRequest(**kwargs)
    assert isinstance(obj, GetSupplySourcesRequest)


def test_supplysourcelist_instantiates():
    """Instantiate SupplySourceList with dummy data"""
    kwargs = {}
    obj = SupplySourceList(**kwargs)
    assert isinstance(obj, SupplySourceList)


def test_getsupplysourcesresponse_instantiates():
    """Instantiate GetSupplySourcesResponse with dummy data"""
    kwargs = {
        "supply_sources": None,
        "next_page_token": None,
    }
    obj = GetSupplySourcesResponse(**kwargs)
    assert isinstance(obj, GetSupplySourcesResponse)


def test_parkingconfiguration_instantiates():
    """Instantiate ParkingConfiguration with dummy data"""
    kwargs = {
        "parking_cost_type": None,
        "parking_spot_identification_type": None,
        "number_of_parking_spots": None,
    }
    obj = ParkingConfiguration(**kwargs)
    assert isinstance(obj, ParkingConfiguration)


def test_instorepickupconfiguration_instantiates():
    """Instantiate InStorePickupConfiguration with dummy data"""
    kwargs = {
        "is_supported": None,
        "parking_configuration": None,
    }
    obj = InStorePickupConfiguration(**kwargs)
    assert isinstance(obj, InStorePickupConfiguration)


def test_operatinghour_instantiates():
    """Instantiate OperatingHour with dummy data"""
    kwargs = {
        "start_time": None,
        "end_time": None,
    }
    obj = OperatingHour(**kwargs)
    assert isinstance(obj, OperatingHour)


def test_pickupchannel_instantiates():
    """Instantiate PickupChannel with dummy data"""
    kwargs = {
        "inventory_hold_period": None,
        "is_supported": None,
        "operational_configuration": None,
        "in_store_pickup_configuration": None,
        "curbside_pickup_configuration": None,
    }
    obj = PickupChannel(**kwargs)
    assert isinstance(obj, PickupChannel)


def test_returnlocation_instantiates():
    """Instantiate ReturnLocation with dummy data"""
    kwargs = {
        "supply_source_id": None,
        "address_with_contact": None,
    }
    obj = ReturnLocation(**kwargs)
    assert isinstance(obj, ReturnLocation)


def test_outboundcapability_instantiates():
    """Instantiate OutboundCapability with dummy data"""
    kwargs = {
        "is_supported": None,
        "operational_configuration": None,
        "return_location": None,
        "delivery_channel": None,
        "pickup_channel": None,
    }
    obj = OutboundCapability(**kwargs)
    assert isinstance(obj, OutboundCapability)


def test_servicescapability_instantiates():
    """Instantiate ServicesCapability with dummy data"""
    kwargs = {
        "is_supported": None,
        "operational_configuration": None,
    }
    obj = ServicesCapability(**kwargs)
    assert isinstance(obj, ServicesCapability)


def test_supplysourcecapabilities_instantiates():
    """Instantiate SupplySourceCapabilities with dummy data"""
    kwargs = {
        "outbound": None,
        "services": None,
    }
    obj = SupplySourceCapabilities(**kwargs)
    assert isinstance(obj, SupplySourceCapabilities)


def test_supplysourceconfiguration_instantiates():
    """Instantiate SupplySourceConfiguration with dummy data"""
    kwargs = {
        "operational_configuration": None,
        "timezone": None,
    }
    obj = SupplySourceConfiguration(**kwargs)
    assert isinstance(obj, SupplySourceConfiguration)


def test_supplysource_instantiates():
    """Instantiate SupplySource with dummy data"""
    kwargs = {
        "supply_source_id": None,
        "supply_source_code": None,
        "alias": None,
        "status": None,
        "address": None,
        "configuration": None,
        "capabilities": None,
        "created_at": None,
        "updated_at": None,
    }
    obj = SupplySource(**kwargs)
    assert isinstance(obj, SupplySource)


def test_updatesupplysourcerequestbody_instantiates():
    """Instantiate UpdateSupplySourceRequestBody with dummy data"""
    kwargs = {
        "alias": None,
        "configuration": None,
        "capabilities": None,
    }
    obj = UpdateSupplySourceRequestBody(**kwargs)
    assert isinstance(obj, UpdateSupplySourceRequestBody)


def test_updatesupplysourcerequest_instantiates():
    """Instantiate UpdateSupplySourceRequest with dummy data"""
    kwargs = {
        "supply_source_id": "",
        "payload": None,
    }
    obj = UpdateSupplySourceRequest(**kwargs)
    assert isinstance(obj, UpdateSupplySourceRequest)


def test_updatesupplysourcestatusrequestbody_instantiates():
    """Instantiate UpdateSupplySourceStatusRequestBody with dummy data"""
    kwargs = {
        "status": None,
    }
    obj = UpdateSupplySourceStatusRequestBody(**kwargs)
    assert isinstance(obj, UpdateSupplySourceStatusRequestBody)


def test_updatesupplysourcestatusrequest_instantiates():
    """Instantiate UpdateSupplySourceStatusRequest with dummy data"""
    kwargs = {
        "supply_source_id": "",
        "payload": None,
    }
    obj = UpdateSupplySourceStatusRequest(**kwargs)
    assert isinstance(obj, UpdateSupplySourceStatusRequest)
