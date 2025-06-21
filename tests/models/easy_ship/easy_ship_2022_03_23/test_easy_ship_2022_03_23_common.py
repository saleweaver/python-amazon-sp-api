# Auto-generated tests for sp_api.api.models.easy_ship.easy_ship_2022_03_23.common.py
from datetime import datetime

import pytest
from sp_api.api.models.easy_ship.easy_ship_2022_03_23.common import (
    CreateScheduledPackageBulkRequest, CreateScheduledPackageRequest,
    CreateScheduledPackageRequestBody, CreateScheduledPackagesRequestBody,
    CreateScheduledPackagesResponse, Dimensions, Error, ErrorList,
    GetRequestSerializer, GetScheduledPackageRequest, InvoiceData, Item,
    ListHandoverSlotsRequest, ListHandoverSlotsRequestBody,
    ListHandoverSlotsResponse, OrderScheduleDetails, Package, PackageDetails,
    Packages, RejectedOrder, RequestsBaseModel, ScheduledPackageId,
    SpApiBaseModel, TimeSlot, TrackingDetails, UpdatePackageDetails,
    UpdateScheduledPackagesRequest, UpdateScheduledPackagesRequestBody, Weight)


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


def test_timeslot_instantiates():
    """Instantiate TimeSlot with dummy data"""
    kwargs = {
        "slot_id": "",
        "start_time": None,
        "end_time": None,
        "handover_method": None,
    }
    obj = TimeSlot(**kwargs)
    assert isinstance(obj, TimeSlot)


def test_packagedetails_instantiates():
    """Instantiate PackageDetails with dummy data"""
    kwargs = {
        "package_items": None,
        "package_time_slot": TimeSlot(
            **{
                "slot_id": "",
                "start_time": None,
                "end_time": None,
                "handover_method": None,
            }
        ),
        "package_identifier": None,
    }
    obj = PackageDetails(**kwargs)
    assert isinstance(obj, PackageDetails)


def test_orderscheduledetails_instantiates():
    """Instantiate OrderScheduleDetails with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "package_details": None,
    }
    obj = OrderScheduleDetails(**kwargs)
    assert isinstance(obj, OrderScheduleDetails)


def test_createscheduledpackagesrequestbody_instantiates():
    """Instantiate CreateScheduledPackagesRequestBody with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "order_schedule_details_list": [],
        "label_format": "",
    }
    obj = CreateScheduledPackagesRequestBody(**kwargs)
    assert isinstance(obj, CreateScheduledPackagesRequestBody)


def test_createscheduledpackagebulkrequest_instantiates():
    """Instantiate CreateScheduledPackageBulkRequest with dummy data"""
    kwargs = {
        "create_scheduled_packages_request_body": CreateScheduledPackagesRequestBody(
            **{
                "marketplace_id": None,
                "order_schedule_details_list": [],
                "label_format": "",
            }
        ),
    }
    obj = CreateScheduledPackageBulkRequest(**kwargs)
    assert isinstance(obj, CreateScheduledPackageBulkRequest)


def test_createscheduledpackagerequestbody_instantiates():
    """Instantiate CreateScheduledPackageRequestBody with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "marketplace_id": None,
        "package_details": PackageDetails(
            **{
                "package_items": None,
                "package_time_slot": TimeSlot(
                    **{
                        "slot_id": "",
                        "start_time": None,
                        "end_time": None,
                        "handover_method": None,
                    }
                ),
                "package_identifier": None,
            }
        ),
    }
    obj = CreateScheduledPackageRequestBody(**kwargs)
    assert isinstance(obj, CreateScheduledPackageRequestBody)


def test_createscheduledpackagerequest_instantiates():
    """Instantiate CreateScheduledPackageRequest with dummy data"""
    kwargs = {
        "create_scheduled_package_request_body": CreateScheduledPackageRequestBody(
            **{
                "amazon_order_id": "",
                "marketplace_id": None,
                "package_details": PackageDetails(
                    **{
                        "package_items": None,
                        "package_time_slot": TimeSlot(
                            **{
                                "slot_id": "",
                                "start_time": None,
                                "end_time": None,
                                "handover_method": None,
                            }
                        ),
                        "package_identifier": None,
                    }
                ),
            }
        ),
    }
    obj = CreateScheduledPackageRequest(**kwargs)
    assert isinstance(obj, CreateScheduledPackageRequest)


def test_dimensions_instantiates():
    """Instantiate Dimensions with dummy data"""
    kwargs = {
        "length": None,
        "width": None,
        "height": None,
        "unit": None,
        "identifier": None,
    }
    obj = Dimensions(**kwargs)
    assert isinstance(obj, Dimensions)


def test_invoicedata_instantiates():
    """Instantiate InvoiceData with dummy data"""
    kwargs = {
        "invoice_number": "",
        "invoice_date": None,
    }
    obj = InvoiceData(**kwargs)
    assert isinstance(obj, InvoiceData)


def test_scheduledpackageid_instantiates():
    """Instantiate ScheduledPackageId with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "package_id": None,
    }
    obj = ScheduledPackageId(**kwargs)
    assert isinstance(obj, ScheduledPackageId)


def test_trackingdetails_instantiates():
    """Instantiate TrackingDetails with dummy data"""
    kwargs = {
        "tracking_id": None,
    }
    obj = TrackingDetails(**kwargs)
    assert isinstance(obj, TrackingDetails)


def test_weight_instantiates():
    """Instantiate Weight with dummy data"""
    kwargs = {
        "value": None,
        "unit": None,
    }
    obj = Weight(**kwargs)
    assert isinstance(obj, Weight)


def test_package_instantiates():
    """Instantiate Package with dummy data"""
    kwargs = {
        "scheduled_package_id": ScheduledPackageId(
            **{"amazon_order_id": "", "package_id": None}
        ),
        "package_dimensions": Dimensions(
            **{
                "length": None,
                "width": None,
                "height": None,
                "unit": None,
                "identifier": None,
            }
        ),
        "package_weight": Weight(**{"value": None, "unit": None}),
        "package_items": None,
        "package_time_slot": TimeSlot(
            **{
                "slot_id": "",
                "start_time": None,
                "end_time": None,
                "handover_method": None,
            }
        ),
        "package_identifier": None,
        "invoice": None,
        "package_status": None,
        "tracking_details": None,
    }
    obj = Package(**kwargs)
    assert isinstance(obj, Package)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_rejectedorder_instantiates():
    """Instantiate RejectedOrder with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "error": None,
    }
    obj = RejectedOrder(**kwargs)
    assert isinstance(obj, RejectedOrder)


def test_createscheduledpackagesresponse_instantiates():
    """Instantiate CreateScheduledPackagesResponse with dummy data"""
    kwargs = {
        "scheduled_packages": None,
        "rejected_orders": None,
        "printable_documents_url": None,
    }
    obj = CreateScheduledPackagesResponse(**kwargs)
    assert isinstance(obj, CreateScheduledPackagesResponse)


def test_errorlist_instantiates():
    """Instantiate ErrorList with dummy data"""
    kwargs = {
        "errors": [],
    }
    obj = ErrorList(**kwargs)
    assert isinstance(obj, ErrorList)


def test_getscheduledpackagerequest_instantiates():
    """Instantiate GetScheduledPackageRequest with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "marketplace_id": None,
    }
    obj = GetScheduledPackageRequest(**kwargs)
    assert isinstance(obj, GetScheduledPackageRequest)


def test_item_instantiates():
    """Instantiate Item with dummy data"""
    kwargs = {
        "order_item_id": None,
        "order_item_serial_numbers": None,
    }
    obj = Item(**kwargs)
    assert isinstance(obj, Item)


def test_listhandoverslotsrequestbody_instantiates():
    """Instantiate ListHandoverSlotsRequestBody with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "amazon_order_id": "",
        "package_dimensions": Dimensions(
            **{
                "length": None,
                "width": None,
                "height": None,
                "unit": None,
                "identifier": None,
            }
        ),
        "package_weight": Weight(**{"value": None, "unit": None}),
    }
    obj = ListHandoverSlotsRequestBody(**kwargs)
    assert isinstance(obj, ListHandoverSlotsRequestBody)


def test_listhandoverslotsrequest_instantiates():
    """Instantiate ListHandoverSlotsRequest with dummy data"""
    kwargs = {
        "list_handover_slots_request_body": None,
    }
    obj = ListHandoverSlotsRequest(**kwargs)
    assert isinstance(obj, ListHandoverSlotsRequest)


def test_listhandoverslotsresponse_instantiates():
    """Instantiate ListHandoverSlotsResponse with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "time_slots": [],
    }
    obj = ListHandoverSlotsResponse(**kwargs)
    assert isinstance(obj, ListHandoverSlotsResponse)


def test_packages_instantiates():
    """Instantiate Packages with dummy data"""
    kwargs = {
        "packages": [],
    }
    obj = Packages(**kwargs)
    assert isinstance(obj, Packages)


def test_updatepackagedetails_instantiates():
    """Instantiate UpdatePackageDetails with dummy data"""
    kwargs = {
        "scheduled_package_id": ScheduledPackageId(
            **{"amazon_order_id": "", "package_id": None}
        ),
        "package_time_slot": TimeSlot(
            **{
                "slot_id": "",
                "start_time": None,
                "end_time": None,
                "handover_method": None,
            }
        ),
    }
    obj = UpdatePackageDetails(**kwargs)
    assert isinstance(obj, UpdatePackageDetails)


def test_updatescheduledpackagesrequestbody_instantiates():
    """Instantiate UpdateScheduledPackagesRequestBody with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "update_package_details_list": [],
    }
    obj = UpdateScheduledPackagesRequestBody(**kwargs)
    assert isinstance(obj, UpdateScheduledPackagesRequestBody)


def test_updatescheduledpackagesrequest_instantiates():
    """Instantiate UpdateScheduledPackagesRequest with dummy data"""
    kwargs = {
        "update_scheduled_packages_request_body": None,
    }
    obj = UpdateScheduledPackagesRequest(**kwargs)
    assert isinstance(obj, UpdateScheduledPackagesRequest)
