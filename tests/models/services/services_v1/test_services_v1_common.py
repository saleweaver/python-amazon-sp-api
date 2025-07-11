# Auto-generated tests for sp_api.api.models.services.services_v1.common.py
from datetime import datetime

import pytest
from sp_api.api.models.services.services_v1.common import (
    AddAppointmentForServiceJobByServiceJobIdRequest,
    AddAppointmentRequestBody, Address, Appointment,
    AppointmentAppointmentStatusEnum, AppointmentResource, AppointmentSlot,
    AppointmentSlotReport, AppointmentSlotReportSchedulingTypeEnum,
    AppointmentTime, AppointmentTimeInput, AssignAppointmentResourcesRequest,
    AssignAppointmentResourcesRequestBody, AssignAppointmentResourcesResponse,
    AssociatedItem, AssociatedItemItemStatusEnum, AvailabilityRecord, Buyer,
    CancelReservationRequest, CancelReservationResponse,
    CancelServiceJobByServiceJobIdRequest,
    CancelServiceJobByServiceJobIdResponse,
    CompleteServiceJobByServiceJobIdRequest,
    CompleteServiceJobByServiceJobIdResponse, CreateReservationRecord,
    CreateReservationRequest, CreateReservationRequestBody,
    CreateReservationResponse, CreateServiceDocumentUploadDestination,
    CreateServiceDocumentUploadDestinationRequest, DateTimeRange,
    EncryptionDetails, EncryptionDetailsStandardEnum, Error,
    ErrorErrorLevelEnum, FixedSlot, FixedSlotCapacity, FixedSlotCapacityErrors,
    FixedSlotCapacityQuery, FulfillmentDocument, FulfillmentTime,
    GetAppointmentSlotsRequest, GetAppointmentSlotsResponse,
    GetAppointmmentSlotsByJobIdRequest, GetFixedSlotCapacityRequest,
    GetRangeSlotCapacityRequest, GetRequestSerializer,
    GetServiceJobByServiceJobIdRequest, GetServiceJobByServiceJobIdResponse,
    GetServiceJobsRequest, GetServiceJobsRequestServiceJobStatusEnum,
    GetServiceJobsRequestSortFieldEnum, GetServiceJobsRequestSortOrderEnum,
    GetServiceJobsResponse, ItemDelivery, ItemDeliveryPromise, JobListing, Poa,
    PoaPoaTypeEnum, RangeCapacity, RangeSlot, RangeSlotCapacity,
    RangeSlotCapacityErrors, RangeSlotCapacityQuery, Recurrence,
    RequestsBaseModel, RescheduleAppointmentForServiceJobByServiceJobIdRequest,
    RescheduleAppointmentRequestBody, Reservation, ReservationTypeEnum,
    ScopeOfWork, Seller, ServiceDocumentUploadDestination, ServiceJob,
    ServiceJobProvider, ServiceJobServiceJobStatusEnum, ServiceLocation,
    ServiceLocationServiceLocationTypeEnum, ServiceUploadDocument,
    ServiceUploadDocumentContentTypeEnum, SetAppointmentFulfillmentDataRequest,
    SetAppointmentFulfillmentDataRequestBody, SetAppointmentResponse,
    SpApiBaseModel, Technician, UpdateReservationRecord,
    UpdateReservationRequest, UpdateReservationRequestBody,
    UpdateReservationResponse, UpdateScheduleRecord, UpdateScheduleRequest,
    UpdateScheduleRequestBody, UpdateScheduleResponse, Warning)


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


def test_appointmenttimeinput_instantiates():
    """Instantiate AppointmentTimeInput with dummy data"""
    kwargs = {
        "start_time": datetime(2000, 1, 1),
        "duration_in_minutes": None,
    }
    obj = AppointmentTimeInput(**kwargs)
    assert isinstance(obj, AppointmentTimeInput)


def test_addappointmentrequestbody_instantiates():
    """Instantiate AddAppointmentRequestBody with dummy data"""
    kwargs = {
        "appointment_time": AppointmentTimeInput(
            **{"start_time": datetime(2000, 1, 1), "duration_in_minutes": None}
        ),
    }
    obj = AddAppointmentRequestBody(**kwargs)
    assert isinstance(obj, AddAppointmentRequestBody)


def test_addappointmentforservicejobbyservicejobidrequest_instantiates():
    """Instantiate AddAppointmentForServiceJobByServiceJobIdRequest with dummy data"""
    kwargs = {
        "service_job_id": "",
        "body": AddAppointmentRequestBody(
            **{
                "appointment_time": AppointmentTimeInput(
                    **{"start_time": datetime(2000, 1, 1), "duration_in_minutes": None}
                )
            }
        ),
    }
    obj = AddAppointmentForServiceJobByServiceJobIdRequest(**kwargs)
    assert isinstance(obj, AddAppointmentForServiceJobByServiceJobIdRequest)


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
        "state_or_region": None,
        "postal_code": None,
        "country_code": None,
        "phone": None,
    }
    obj = Address(**kwargs)
    assert isinstance(obj, Address)


def test_appointmenttime_instantiates():
    """Instantiate AppointmentTime with dummy data"""
    kwargs = {
        "start_time": datetime(2000, 1, 1),
        "duration_in_minutes": 0,
    }
    obj = AppointmentTime(**kwargs)
    assert isinstance(obj, AppointmentTime)


def test_technician_instantiates():
    """Instantiate Technician with dummy data"""
    kwargs = {
        "technician_id": None,
        "name": None,
    }
    obj = Technician(**kwargs)
    assert isinstance(obj, Technician)


def test_poa_instantiates():
    """Instantiate Poa with dummy data"""
    kwargs = {
        "appointment_time": None,
        "technicians": None,
        "uploading_technician": None,
        "upload_time": None,
        "poa_type": None,
    }
    obj = Poa(**kwargs)
    assert isinstance(obj, Poa)


def test_appointment_instantiates():
    """Instantiate Appointment with dummy data"""
    kwargs = {
        "appointment_id": None,
        "appointment_status": None,
        "appointment_time": None,
        "assigned_technicians": None,
        "rescheduled_appointment_id": None,
        "poa": None,
    }
    obj = Appointment(**kwargs)
    assert isinstance(obj, Appointment)


def test_appointmentresource_instantiates():
    """Instantiate AppointmentResource with dummy data"""
    kwargs = {
        "resource_id": None,
    }
    obj = AppointmentResource(**kwargs)
    assert isinstance(obj, AppointmentResource)


def test_appointmentslot_instantiates():
    """Instantiate AppointmentSlot with dummy data"""
    kwargs = {
        "start_time": None,
        "end_time": None,
        "capacity": None,
    }
    obj = AppointmentSlot(**kwargs)
    assert isinstance(obj, AppointmentSlot)


def test_appointmentslotreport_instantiates():
    """Instantiate AppointmentSlotReport with dummy data"""
    kwargs = {
        "scheduling_type": None,
        "start_time": None,
        "end_time": None,
        "appointment_slots": None,
    }
    obj = AppointmentSlotReport(**kwargs)
    assert isinstance(obj, AppointmentSlotReport)


def test_assignappointmentresourcesrequestbody_instantiates():
    """Instantiate AssignAppointmentResourcesRequestBody with dummy data"""
    kwargs = {
        "resources": [],
    }
    obj = AssignAppointmentResourcesRequestBody(**kwargs)
    assert isinstance(obj, AssignAppointmentResourcesRequestBody)


def test_assignappointmentresourcesrequest_instantiates():
    """Instantiate AssignAppointmentResourcesRequest with dummy data"""
    kwargs = {
        "service_job_id": "",
        "appointment_id": "",
        "body": AssignAppointmentResourcesRequestBody(**{"resources": []}),
    }
    obj = AssignAppointmentResourcesRequest(**kwargs)
    assert isinstance(obj, AssignAppointmentResourcesRequest)


def test_assignappointmentresourcesresponse_instantiates():
    """Instantiate AssignAppointmentResourcesResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = AssignAppointmentResourcesResponse(**kwargs)
    assert isinstance(obj, AssignAppointmentResourcesResponse)


def test_itemdeliverypromise_instantiates():
    """Instantiate ItemDeliveryPromise with dummy data"""
    kwargs = {
        "start_time": None,
        "end_time": None,
    }
    obj = ItemDeliveryPromise(**kwargs)
    assert isinstance(obj, ItemDeliveryPromise)


def test_itemdelivery_instantiates():
    """Instantiate ItemDelivery with dummy data"""
    kwargs = {
        "estimated_delivery_date": None,
        "item_delivery_promise": None,
    }
    obj = ItemDelivery(**kwargs)
    assert isinstance(obj, ItemDelivery)


def test_associateditem_instantiates():
    """Instantiate AssociatedItem with dummy data"""
    kwargs = {
        "asin": None,
        "title": None,
        "quantity": None,
        "order_id": None,
        "item_status": None,
        "brand_name": None,
        "item_delivery": None,
    }
    obj = AssociatedItem(**kwargs)
    assert isinstance(obj, AssociatedItem)


def test_recurrence_instantiates():
    """Instantiate Recurrence with dummy data"""
    kwargs = {
        "end_time": datetime(2000, 1, 1),
        "days_of_week": None,
        "days_of_month": None,
    }
    obj = Recurrence(**kwargs)
    assert isinstance(obj, Recurrence)


def test_availabilityrecord_instantiates():
    """Instantiate AvailabilityRecord with dummy data"""
    kwargs = {
        "start_time": datetime(2000, 1, 1),
        "end_time": datetime(2000, 1, 1),
        "recurrence": None,
        "capacity": None,
    }
    obj = AvailabilityRecord(**kwargs)
    assert isinstance(obj, AvailabilityRecord)


def test_buyer_instantiates():
    """Instantiate Buyer with dummy data"""
    kwargs = {
        "buyer_id": None,
        "name": None,
        "phone": None,
        "is_prime_member": None,
    }
    obj = Buyer(**kwargs)
    assert isinstance(obj, Buyer)


def test_cancelreservationrequest_instantiates():
    """Instantiate CancelReservationRequest with dummy data"""
    kwargs = {
        "reservation_id": "",
        "marketplace_ids": None,
    }
    obj = CancelReservationRequest(**kwargs)
    assert isinstance(obj, CancelReservationRequest)


def test_cancelreservationresponse_instantiates():
    """Instantiate CancelReservationResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = CancelReservationResponse(**kwargs)
    assert isinstance(obj, CancelReservationResponse)


def test_cancelservicejobbyservicejobidrequest_instantiates():
    """Instantiate CancelServiceJobByServiceJobIdRequest with dummy data"""
    kwargs = {
        "service_job_id": "",
        "cancellation_reason_code": "",
    }
    obj = CancelServiceJobByServiceJobIdRequest(**kwargs)
    assert isinstance(obj, CancelServiceJobByServiceJobIdRequest)


def test_cancelservicejobbyservicejobidresponse_instantiates():
    """Instantiate CancelServiceJobByServiceJobIdResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = CancelServiceJobByServiceJobIdResponse(**kwargs)
    assert isinstance(obj, CancelServiceJobByServiceJobIdResponse)


def test_completeservicejobbyservicejobidrequest_instantiates():
    """Instantiate CompleteServiceJobByServiceJobIdRequest with dummy data"""
    kwargs = {
        "service_job_id": "",
    }
    obj = CompleteServiceJobByServiceJobIdRequest(**kwargs)
    assert isinstance(obj, CompleteServiceJobByServiceJobIdRequest)


def test_completeservicejobbyservicejobidresponse_instantiates():
    """Instantiate CompleteServiceJobByServiceJobIdResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = CompleteServiceJobByServiceJobIdResponse(**kwargs)
    assert isinstance(obj, CompleteServiceJobByServiceJobIdResponse)


def test_reservation_instantiates():
    """Instantiate Reservation with dummy data"""
    kwargs = {
        "reservation_id": None,
        "type": ReservationTypeEnum.APPOINTMENT,
        "availability": AvailabilityRecord(
            **{
                "start_time": datetime(2000, 1, 1),
                "end_time": datetime(2000, 1, 1),
                "recurrence": None,
                "capacity": None,
            }
        ),
    }
    obj = Reservation(**kwargs)
    assert isinstance(obj, Reservation)


def test_createreservationrecord_instantiates():
    """Instantiate CreateReservationRecord with dummy data"""
    kwargs = {
        "reservation": None,
        "warnings": None,
        "errors": None,
    }
    obj = CreateReservationRecord(**kwargs)
    assert isinstance(obj, CreateReservationRecord)


def test_createreservationrequestbody_instantiates():
    """Instantiate CreateReservationRequestBody with dummy data"""
    kwargs = {
        "resource_id": "",
        "reservation": Reservation(
            **{
                "reservation_id": None,
                "type": ReservationTypeEnum.APPOINTMENT,
                "availability": AvailabilityRecord(
                    **{
                        "start_time": datetime(2000, 1, 1),
                        "end_time": datetime(2000, 1, 1),
                        "recurrence": None,
                        "capacity": None,
                    }
                ),
            }
        ),
    }
    obj = CreateReservationRequestBody(**kwargs)
    assert isinstance(obj, CreateReservationRequestBody)


def test_createreservationrequest_instantiates():
    """Instantiate CreateReservationRequest with dummy data"""
    kwargs = {
        "body": CreateReservationRequestBody(
            **{
                "resource_id": "",
                "reservation": Reservation(
                    **{
                        "reservation_id": None,
                        "type": ReservationTypeEnum.APPOINTMENT,
                        "availability": AvailabilityRecord(
                            **{
                                "start_time": datetime(2000, 1, 1),
                                "end_time": datetime(2000, 1, 1),
                                "recurrence": None,
                                "capacity": None,
                            }
                        ),
                    }
                ),
            }
        ),
        "marketplace_ids": None,
    }
    obj = CreateReservationRequest(**kwargs)
    assert isinstance(obj, CreateReservationRequest)


def test_createreservationresponse_instantiates():
    """Instantiate CreateReservationResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = CreateReservationResponse(**kwargs)
    assert isinstance(obj, CreateReservationResponse)


def test_encryptiondetails_instantiates():
    """Instantiate EncryptionDetails with dummy data"""
    kwargs = {
        "standard": EncryptionDetailsStandardEnum.AES,
        "initialization_vector": "",
        "key": "",
    }
    obj = EncryptionDetails(**kwargs)
    assert isinstance(obj, EncryptionDetails)


def test_servicedocumentuploaddestination_instantiates():
    """Instantiate ServiceDocumentUploadDestination with dummy data"""
    kwargs = {
        "upload_destination_id": "",
        "url": "",
        "encryption_details": EncryptionDetails(
            **{
                "standard": EncryptionDetailsStandardEnum.AES,
                "initialization_vector": "",
                "key": "",
            }
        ),
        "headers": None,
    }
    obj = ServiceDocumentUploadDestination(**kwargs)
    assert isinstance(obj, ServiceDocumentUploadDestination)


def test_createservicedocumentuploaddestination_instantiates():
    """Instantiate CreateServiceDocumentUploadDestination with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = CreateServiceDocumentUploadDestination(**kwargs)
    assert isinstance(obj, CreateServiceDocumentUploadDestination)


def test_serviceuploaddocument_instantiates():
    """Instantiate ServiceUploadDocument with dummy data"""
    kwargs = {
        "content_type": ServiceUploadDocumentContentTypeEnum.TIFF,
        "content_length": 0.0,
        "content_m_d5": None,
    }
    obj = ServiceUploadDocument(**kwargs)
    assert isinstance(obj, ServiceUploadDocument)


def test_createservicedocumentuploaddestinationrequest_instantiates():
    """Instantiate CreateServiceDocumentUploadDestinationRequest with dummy data"""
    kwargs = {
        "body": ServiceUploadDocument(
            **{
                "content_type": ServiceUploadDocumentContentTypeEnum.TIFF,
                "content_length": 0.0,
                "content_m_d5": None,
            }
        ),
    }
    obj = CreateServiceDocumentUploadDestinationRequest(**kwargs)
    assert isinstance(obj, CreateServiceDocumentUploadDestinationRequest)


def test_datetimerange_instantiates():
    """Instantiate DateTimeRange with dummy data"""
    kwargs = {
        "start_time": datetime(2000, 1, 1),
        "end_time": datetime(2000, 1, 1),
    }
    obj = DateTimeRange(**kwargs)
    assert isinstance(obj, DateTimeRange)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
        "error_level": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_fixedslot_instantiates():
    """Instantiate FixedSlot with dummy data"""
    kwargs = {
        "start_date_time": None,
        "scheduled_capacity": None,
        "available_capacity": None,
        "encumbered_capacity": None,
        "reserved_capacity": None,
    }
    obj = FixedSlot(**kwargs)
    assert isinstance(obj, FixedSlot)


def test_fixedslotcapacity_instantiates():
    """Instantiate FixedSlotCapacity with dummy data"""
    kwargs = {
        "resource_id": None,
        "slot_duration": None,
        "capacities": None,
        "next_page_token": None,
    }
    obj = FixedSlotCapacity(**kwargs)
    assert isinstance(obj, FixedSlotCapacity)


def test_fixedslotcapacityerrors_instantiates():
    """Instantiate FixedSlotCapacityErrors with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = FixedSlotCapacityErrors(**kwargs)
    assert isinstance(obj, FixedSlotCapacityErrors)


def test_fixedslotcapacityquery_instantiates():
    """Instantiate FixedSlotCapacityQuery with dummy data"""
    kwargs = {
        "capacity_types": None,
        "slot_duration": None,
        "start_date_time": datetime(2000, 1, 1),
        "end_date_time": datetime(2000, 1, 1),
    }
    obj = FixedSlotCapacityQuery(**kwargs)
    assert isinstance(obj, FixedSlotCapacityQuery)


def test_fulfillmentdocument_instantiates():
    """Instantiate FulfillmentDocument with dummy data"""
    kwargs = {
        "upload_destination_id": None,
        "content_sha256": None,
    }
    obj = FulfillmentDocument(**kwargs)
    assert isinstance(obj, FulfillmentDocument)


def test_fulfillmenttime_instantiates():
    """Instantiate FulfillmentTime with dummy data"""
    kwargs = {
        "start_time": None,
        "end_time": None,
    }
    obj = FulfillmentTime(**kwargs)
    assert isinstance(obj, FulfillmentTime)


def test_getappointmentslotsrequest_instantiates():
    """Instantiate GetAppointmentSlotsRequest with dummy data"""
    kwargs = {
        "asin": "",
        "store_id": "",
        "marketplace_ids": None,
        "start_time": None,
        "end_time": None,
    }
    obj = GetAppointmentSlotsRequest(**kwargs)
    assert isinstance(obj, GetAppointmentSlotsRequest)


def test_getappointmentslotsresponse_instantiates():
    """Instantiate GetAppointmentSlotsResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetAppointmentSlotsResponse(**kwargs)
    assert isinstance(obj, GetAppointmentSlotsResponse)


def test_getappointmmentslotsbyjobidrequest_instantiates():
    """Instantiate GetAppointmmentSlotsByJobIdRequest with dummy data"""
    kwargs = {
        "service_job_id": "",
        "marketplace_ids": None,
        "start_time": None,
        "end_time": None,
    }
    obj = GetAppointmmentSlotsByJobIdRequest(**kwargs)
    assert isinstance(obj, GetAppointmmentSlotsByJobIdRequest)


def test_getfixedslotcapacityrequest_instantiates():
    """Instantiate GetFixedSlotCapacityRequest with dummy data"""
    kwargs = {
        "resource_id": "",
        "body": FixedSlotCapacityQuery(
            **{
                "capacity_types": None,
                "slot_duration": None,
                "start_date_time": datetime(2000, 1, 1),
                "end_date_time": datetime(2000, 1, 1),
            }
        ),
        "marketplace_ids": None,
        "next_page_token": None,
    }
    obj = GetFixedSlotCapacityRequest(**kwargs)
    assert isinstance(obj, GetFixedSlotCapacityRequest)


def test_rangeslotcapacityquery_instantiates():
    """Instantiate RangeSlotCapacityQuery with dummy data"""
    kwargs = {
        "capacity_types": None,
        "start_date_time": datetime(2000, 1, 1),
        "end_date_time": datetime(2000, 1, 1),
    }
    obj = RangeSlotCapacityQuery(**kwargs)
    assert isinstance(obj, RangeSlotCapacityQuery)


def test_getrangeslotcapacityrequest_instantiates():
    """Instantiate GetRangeSlotCapacityRequest with dummy data"""
    kwargs = {
        "resource_id": "",
        "body": RangeSlotCapacityQuery(
            **{
                "capacity_types": None,
                "start_date_time": datetime(2000, 1, 1),
                "end_date_time": datetime(2000, 1, 1),
            }
        ),
        "marketplace_ids": None,
        "next_page_token": None,
    }
    obj = GetRangeSlotCapacityRequest(**kwargs)
    assert isinstance(obj, GetRangeSlotCapacityRequest)


def test_getservicejobbyservicejobidrequest_instantiates():
    """Instantiate GetServiceJobByServiceJobIdRequest with dummy data"""
    kwargs = {
        "service_job_id": "",
    }
    obj = GetServiceJobByServiceJobIdRequest(**kwargs)
    assert isinstance(obj, GetServiceJobByServiceJobIdRequest)


def test_scopeofwork_instantiates():
    """Instantiate ScopeOfWork with dummy data"""
    kwargs = {
        "asin": None,
        "title": None,
        "quantity": None,
        "required_skills": None,
    }
    obj = ScopeOfWork(**kwargs)
    assert isinstance(obj, ScopeOfWork)


def test_seller_instantiates():
    """Instantiate Seller with dummy data"""
    kwargs = {
        "seller_id": None,
    }
    obj = Seller(**kwargs)
    assert isinstance(obj, Seller)


def test_servicejobprovider_instantiates():
    """Instantiate ServiceJobProvider with dummy data"""
    kwargs = {
        "service_job_provider_id": None,
    }
    obj = ServiceJobProvider(**kwargs)
    assert isinstance(obj, ServiceJobProvider)


def test_servicelocation_instantiates():
    """Instantiate ServiceLocation with dummy data"""
    kwargs = {
        "service_location_type": None,
        "address": None,
    }
    obj = ServiceLocation(**kwargs)
    assert isinstance(obj, ServiceLocation)


def test_servicejob_instantiates():
    """Instantiate ServiceJob with dummy data"""
    kwargs = {
        "create_time": None,
        "service_job_id": None,
        "service_job_status": None,
        "scope_of_work": None,
        "seller": None,
        "service_job_provider": None,
        "preferred_appointment_times": None,
        "appointments": None,
        "service_order_id": None,
        "marketplace_id": None,
        "store_id": None,
        "buyer": None,
        "associated_items": None,
        "service_location": None,
    }
    obj = ServiceJob(**kwargs)
    assert isinstance(obj, ServiceJob)


def test_getservicejobbyservicejobidresponse_instantiates():
    """Instantiate GetServiceJobByServiceJobIdResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetServiceJobByServiceJobIdResponse(**kwargs)
    assert isinstance(obj, GetServiceJobByServiceJobIdResponse)


def test_getservicejobsrequest_instantiates():
    """Instantiate GetServiceJobsRequest with dummy data"""
    kwargs = {
        "service_order_ids": None,
        "service_job_status": None,
        "page_token": None,
        "page_size": None,
        "sort_field": None,
        "sort_order": None,
        "created_after": None,
        "created_before": None,
        "last_updated_after": None,
        "last_updated_before": None,
        "schedule_start_date": None,
        "schedule_end_date": None,
        "marketplace_ids": None,
        "asins": None,
        "required_skills": None,
        "store_ids": None,
    }
    obj = GetServiceJobsRequest(**kwargs)
    assert isinstance(obj, GetServiceJobsRequest)


def test_joblisting_instantiates():
    """Instantiate JobListing with dummy data"""
    kwargs = {
        "total_result_size": None,
        "next_page_token": None,
        "previous_page_token": None,
        "jobs": None,
    }
    obj = JobListing(**kwargs)
    assert isinstance(obj, JobListing)


def test_getservicejobsresponse_instantiates():
    """Instantiate GetServiceJobsResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetServiceJobsResponse(**kwargs)
    assert isinstance(obj, GetServiceJobsResponse)


def test_rangeslot_instantiates():
    """Instantiate RangeSlot with dummy data"""
    kwargs = {
        "start_date_time": None,
        "end_date_time": None,
        "capacity": None,
    }
    obj = RangeSlot(**kwargs)
    assert isinstance(obj, RangeSlot)


def test_rangecapacity_instantiates():
    """Instantiate RangeCapacity with dummy data"""
    kwargs = {
        "capacity_type": None,
        "slots": None,
    }
    obj = RangeCapacity(**kwargs)
    assert isinstance(obj, RangeCapacity)


def test_rangeslotcapacity_instantiates():
    """Instantiate RangeSlotCapacity with dummy data"""
    kwargs = {
        "resource_id": None,
        "capacities": None,
        "next_page_token": None,
    }
    obj = RangeSlotCapacity(**kwargs)
    assert isinstance(obj, RangeSlotCapacity)


def test_rangeslotcapacityerrors_instantiates():
    """Instantiate RangeSlotCapacityErrors with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = RangeSlotCapacityErrors(**kwargs)
    assert isinstance(obj, RangeSlotCapacityErrors)


def test_rescheduleappointmentrequestbody_instantiates():
    """Instantiate RescheduleAppointmentRequestBody with dummy data"""
    kwargs = {
        "appointment_time": AppointmentTimeInput(
            **{"start_time": datetime(2000, 1, 1), "duration_in_minutes": None}
        ),
        "reschedule_reason_code": "",
    }
    obj = RescheduleAppointmentRequestBody(**kwargs)
    assert isinstance(obj, RescheduleAppointmentRequestBody)


def test_rescheduleappointmentforservicejobbyservicejobidrequest_instantiates():
    """Instantiate RescheduleAppointmentForServiceJobByServiceJobIdRequest with dummy data"""
    kwargs = {
        "service_job_id": "",
        "appointment_id": "",
        "body": RescheduleAppointmentRequestBody(
            **{
                "appointment_time": AppointmentTimeInput(
                    **{"start_time": datetime(2000, 1, 1), "duration_in_minutes": None}
                ),
                "reschedule_reason_code": "",
            }
        ),
    }
    obj = RescheduleAppointmentForServiceJobByServiceJobIdRequest(**kwargs)
    assert isinstance(obj, RescheduleAppointmentForServiceJobByServiceJobIdRequest)


def test_setappointmentfulfillmentdatarequestbody_instantiates():
    """Instantiate SetAppointmentFulfillmentDataRequestBody with dummy data"""
    kwargs = {
        "estimated_arrival_time": None,
        "fulfillment_time": None,
        "appointment_resources": None,
        "fulfillment_documents": None,
    }
    obj = SetAppointmentFulfillmentDataRequestBody(**kwargs)
    assert isinstance(obj, SetAppointmentFulfillmentDataRequestBody)


def test_setappointmentfulfillmentdatarequest_instantiates():
    """Instantiate SetAppointmentFulfillmentDataRequest with dummy data"""
    kwargs = {
        "service_job_id": "",
        "appointment_id": "",
        "body": SetAppointmentFulfillmentDataRequestBody(
            **{
                "estimated_arrival_time": None,
                "fulfillment_time": None,
                "appointment_resources": None,
                "fulfillment_documents": None,
            }
        ),
    }
    obj = SetAppointmentFulfillmentDataRequest(**kwargs)
    assert isinstance(obj, SetAppointmentFulfillmentDataRequest)


def test_setappointmentresponse_instantiates():
    """Instantiate SetAppointmentResponse with dummy data"""
    kwargs = {
        "appointment_id": None,
        "warnings": None,
        "errors": None,
    }
    obj = SetAppointmentResponse(**kwargs)
    assert isinstance(obj, SetAppointmentResponse)


def test_updatereservationrecord_instantiates():
    """Instantiate UpdateReservationRecord with dummy data"""
    kwargs = {
        "reservation": None,
        "warnings": None,
        "errors": None,
    }
    obj = UpdateReservationRecord(**kwargs)
    assert isinstance(obj, UpdateReservationRecord)


def test_updatereservationrequestbody_instantiates():
    """Instantiate UpdateReservationRequestBody with dummy data"""
    kwargs = {
        "resource_id": "",
        "reservation": Reservation(
            **{
                "reservation_id": None,
                "type": ReservationTypeEnum.APPOINTMENT,
                "availability": AvailabilityRecord(
                    **{
                        "start_time": datetime(2000, 1, 1),
                        "end_time": datetime(2000, 1, 1),
                        "recurrence": None,
                        "capacity": None,
                    }
                ),
            }
        ),
    }
    obj = UpdateReservationRequestBody(**kwargs)
    assert isinstance(obj, UpdateReservationRequestBody)


def test_updatereservationrequest_instantiates():
    """Instantiate UpdateReservationRequest with dummy data"""
    kwargs = {
        "reservation_id": "",
        "body": UpdateReservationRequestBody(
            **{
                "resource_id": "",
                "reservation": Reservation(
                    **{
                        "reservation_id": None,
                        "type": ReservationTypeEnum.APPOINTMENT,
                        "availability": AvailabilityRecord(
                            **{
                                "start_time": datetime(2000, 1, 1),
                                "end_time": datetime(2000, 1, 1),
                                "recurrence": None,
                                "capacity": None,
                            }
                        ),
                    }
                ),
            }
        ),
        "marketplace_ids": None,
    }
    obj = UpdateReservationRequest(**kwargs)
    assert isinstance(obj, UpdateReservationRequest)


def test_updatereservationresponse_instantiates():
    """Instantiate UpdateReservationResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = UpdateReservationResponse(**kwargs)
    assert isinstance(obj, UpdateReservationResponse)


def test_updateschedulerecord_instantiates():
    """Instantiate UpdateScheduleRecord with dummy data"""
    kwargs = {
        "availability": None,
        "warnings": None,
        "errors": None,
    }
    obj = UpdateScheduleRecord(**kwargs)
    assert isinstance(obj, UpdateScheduleRecord)


def test_updateschedulerequestbody_instantiates():
    """Instantiate UpdateScheduleRequestBody with dummy data"""
    kwargs = {
        "schedules": [],
    }
    obj = UpdateScheduleRequestBody(**kwargs)
    assert isinstance(obj, UpdateScheduleRequestBody)


def test_updateschedulerequest_instantiates():
    """Instantiate UpdateScheduleRequest with dummy data"""
    kwargs = {
        "resource_id": "",
        "body": UpdateScheduleRequestBody(**{"schedules": []}),
        "marketplace_ids": None,
    }
    obj = UpdateScheduleRequest(**kwargs)
    assert isinstance(obj, UpdateScheduleRequest)


def test_updatescheduleresponse_instantiates():
    """Instantiate UpdateScheduleResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = UpdateScheduleResponse(**kwargs)
    assert isinstance(obj, UpdateScheduleResponse)


def test_warning_instantiates():
    """Instantiate Warning with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Warning(**kwargs)
    assert isinstance(obj, Warning)
