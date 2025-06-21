# Auto-generated tests for sp_api.api.models.shipping.shipping_v2.common.py
from datetime import datetime

import pytest
from sp_api.api.models.shipping.shipping_v2.common import (
    AccessibilityAttributes, AccessPoint, AccessPointDetails, AccessPointsMap,
    AccessPointTypesEnum, ActiveAccount, Address, AmazonOrderDetails,
    AmazonShipmentDetails, AssistanceTypeEnum, AvailableValueAddedServiceGroup,
    Benefits, CancelShipmentRequest, CancelShipmentResponse,
    CancelShipmentResult, Carrier, CarrierAccount, CarrierAccountAttribute,
    CarrierAccountInput, ChannelDetails, ChargeComponent, ChargeTypeEnum,
    ClaimProofURLs, ClientReferenceDetail, ClientReferenceTypeEnum,
    CollectionFormsHistoryRecord, CollectionsFormDocument, CollectOnDelivery,
    CreateClaimRequest, CreateClaimRequestBody, CreateClaimResponse, Currency,
    DangerousGoodsDetails, DateRange, DayOfWeekTimeMap, Dimensions,
    DirectFulfillmentItemIdentifiers, DirectPurchaseRequestBody,
    DirectPurchaseResponse, DirectPurchaseResult,
    DirectPurchaseShipmentRequest, DocumentSize, Error, ErrorList, Event,
    ExceptionOperatingHours, ExcludedBenefit, ExcludedBenefitReasonCodes,
    GenerateCollectionFormRequest, GenerateCollectionFormRequestBody,
    GenerateCollectionFormResponse, Geocode, GetAccessPointsRequest,
    GetAccessPointsResponse, GetAccessPointsResult, GetAdditionalInputsRequest,
    GetAdditionalInputsResponse, GetAdditionalInputsResult,
    GetCarrierAccountFormInputsResponse, GetCarrierAccountsRequest,
    GetCarrierAccountsRequestBody, GetCarrierAccountsResponse,
    GetCollectionFormHistoryRequest, GetCollectionFormHistoryRequestBody,
    GetCollectionFormHistoryResponse, GetCollectionFormRequest,
    GetCollectionFormResponse, GetRatesRequest, GetRatesRequestBody,
    GetRatesResponse, GetRatesResult, GetRequestSerializer,
    GetShipmentDocumentsRequest, GetShipmentDocumentsResponse,
    GetShipmentDocumentsResult, GetTrackingRequest, GetTrackingResponse,
    GetTrackingResult, GetUnmanifestedShipmentsRequest,
    GetUnmanifestedShipmentsRequestBody, GetUnmanifestedShipmentsResponse,
    GoodsOwner, IncludedBenefits, IneligibilityReason, IneligibleRate,
    InvoiceDetails, Item, LinkableAccountType, LinkableCarrier,
    LinkCarrierAccountRequest, LinkCarrierAccountRequestBody,
    LinkCarrierAccountResponse, LiquidVolume, Location, NdrRequestData,
    OneClickShipmentRequest, OneClickShipmentRequestBody,
    OneClickShipmentResponse, OneClickShipmentResult,
    OneClickShipmentValueAddedService, OperatingHours, Package,
    PackageDocument, PackageDocumentDetail, PackingGroupEnum,
    PackingInstructionEnum, PrintOption, Promise, PurchaseShipmentRequest,
    PurchaseShipmentRequestBody, PurchaseShipmentResponse,
    PurchaseShipmentResult, Rate, RateItem, RequestedDocumentSpecification,
    RequestedLabelCustomization, RequestedValueAddedService, RequestsBaseModel,
    Service, ServiceIds, ServiceSelection, ShipperInstruction, SpApiBaseModel,
    SubmitNdrFeedbackRequest, SubmitNdrFeedbackRequestBody,
    SupportedDocumentDetail, SupportedDocumentSpecification, TaxDetail,
    TimeOfDay, TimeWindow, TrackingDetailCodes, TrackingSummary, UnitEnum,
    UnlinkCarrierAccountRequest, UnlinkCarrierAccountRequestBody,
    UnlinkCarrierAccountResponse, UnmanifestedCarrierInformation,
    UnmanifestedShipmentLocation, ValidationMetadata, ValueAddedService,
    ValueAddedServiceDetails, Weight)


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


def test_accessibilityattributes_instantiates():
    """Instantiate AccessibilityAttributes with dummy data"""
    kwargs = {
        "distance": None,
        "drive_time": None,
    }
    obj = AccessibilityAttributes(**kwargs)
    assert isinstance(obj, AccessibilityAttributes)


def test_geocode_instantiates():
    """Instantiate Geocode with dummy data"""
    kwargs = {
        "latitude": None,
        "longitude": None,
    }
    obj = Geocode(**kwargs)
    assert isinstance(obj, Geocode)


def test_address_instantiates():
    """Instantiate Address with dummy data"""
    kwargs = {
        "name": "",
        "address_line1": "",
        "address_line2": None,
        "address_line3": None,
        "company_name": None,
        "state_or_region": "",
        "city": "",
        "country_code": "",
        "postal_code": "",
        "email": None,
        "phone_number": None,
        "geocode": None,
    }
    obj = Address(**kwargs)
    assert isinstance(obj, Address)


def test_dayofweektimemap_instantiates():
    """Instantiate DayOfWeekTimeMap with dummy data"""
    kwargs = {}
    obj = DayOfWeekTimeMap(**kwargs)
    assert isinstance(obj, DayOfWeekTimeMap)


def test_daterange_instantiates():
    """Instantiate DateRange with dummy data"""
    kwargs = {
        "start_date": None,
        "end_date": None,
    }
    obj = DateRange(**kwargs)
    assert isinstance(obj, DateRange)


def test_timeofday_instantiates():
    """Instantiate TimeOfDay with dummy data"""
    kwargs = {
        "hour_of_day": None,
        "minute_of_hour": None,
        "second_of_minute": None,
    }
    obj = TimeOfDay(**kwargs)
    assert isinstance(obj, TimeOfDay)


def test_operatinghours_instantiates():
    """Instantiate OperatingHours with dummy data"""
    kwargs = {
        "closing_time": None,
        "opening_time": None,
        "mid_day_closures": None,
    }
    obj = OperatingHours(**kwargs)
    assert isinstance(obj, OperatingHours)


def test_exceptionoperatinghours_instantiates():
    """Instantiate ExceptionOperatingHours with dummy data"""
    kwargs = {
        "date_range": None,
        "operating_hours": None,
    }
    obj = ExceptionOperatingHours(**kwargs)
    assert isinstance(obj, ExceptionOperatingHours)


def test_accesspoint_instantiates():
    """Instantiate AccessPoint with dummy data"""
    kwargs = {
        "access_point_id": None,
        "name": None,
        "timezone": None,
        "type": None,
        "accessibility_attributes": None,
        "address": None,
        "exception_operating_hours": None,
        "assistance_type": None,
        "score": None,
        "standard_operating_hours": None,
    }
    obj = AccessPoint(**kwargs)
    assert isinstance(obj, AccessPoint)


def test_accesspointdetails_instantiates():
    """Instantiate AccessPointDetails with dummy data"""
    kwargs = {
        "access_point_id": None,
    }
    obj = AccessPointDetails(**kwargs)
    assert isinstance(obj, AccessPointDetails)


def test_accesspointsmap_instantiates():
    """Instantiate AccessPointsMap with dummy data"""
    kwargs = {}
    obj = AccessPointsMap(**kwargs)
    assert isinstance(obj, AccessPointsMap)


def test_activeaccount_instantiates():
    """Instantiate ActiveAccount with dummy data"""
    kwargs = {
        "account_id": None,
        "carrier_id": None,
    }
    obj = ActiveAccount(**kwargs)
    assert isinstance(obj, ActiveAccount)


def test_amazonorderdetails_instantiates():
    """Instantiate AmazonOrderDetails with dummy data"""
    kwargs = {
        "order_id": "",
    }
    obj = AmazonOrderDetails(**kwargs)
    assert isinstance(obj, AmazonOrderDetails)


def test_amazonshipmentdetails_instantiates():
    """Instantiate AmazonShipmentDetails with dummy data"""
    kwargs = {
        "shipment_id": "",
    }
    obj = AmazonShipmentDetails(**kwargs)
    assert isinstance(obj, AmazonShipmentDetails)


def test_currency_instantiates():
    """Instantiate Currency with dummy data"""
    kwargs = {
        "value": 0.0,
        "unit": "",
    }
    obj = Currency(**kwargs)
    assert isinstance(obj, Currency)


def test_valueaddedservice_instantiates():
    """Instantiate ValueAddedService with dummy data"""
    kwargs = {
        "id": "",
        "name": "",
        "cost": Currency(**{"value": 0.0, "unit": ""}),
    }
    obj = ValueAddedService(**kwargs)
    assert isinstance(obj, ValueAddedService)


def test_availablevalueaddedservicegroup_instantiates():
    """Instantiate AvailableValueAddedServiceGroup with dummy data"""
    kwargs = {
        "group_id": "",
        "group_description": "",
        "is_required": False,
        "value_added_services": None,
    }
    obj = AvailableValueAddedServiceGroup(**kwargs)
    assert isinstance(obj, AvailableValueAddedServiceGroup)


def test_includedbenefits_instantiates():
    """Instantiate IncludedBenefits with dummy data"""
    kwargs = {}
    obj = IncludedBenefits(**kwargs)
    assert isinstance(obj, IncludedBenefits)


def test_benefits_instantiates():
    """Instantiate Benefits with dummy data"""
    kwargs = {
        "included_benefits": IncludedBenefits(**{}),
        "excluded_benefits": [],
    }
    obj = Benefits(**kwargs)
    assert isinstance(obj, Benefits)


def test_cancelshipmentrequest_instantiates():
    """Instantiate CancelShipmentRequest with dummy data"""
    kwargs = {
        "shipment_id": "",
    }
    obj = CancelShipmentRequest(**kwargs)
    assert isinstance(obj, CancelShipmentRequest)


def test_cancelshipmentresult_instantiates():
    """Instantiate CancelShipmentResult with dummy data"""
    kwargs = {}
    obj = CancelShipmentResult(**kwargs)
    assert isinstance(obj, CancelShipmentResult)


def test_cancelshipmentresponse_instantiates():
    """Instantiate CancelShipmentResponse with dummy data"""
    kwargs = {
        "payload": None,
    }
    obj = CancelShipmentResponse(**kwargs)
    assert isinstance(obj, CancelShipmentResponse)


def test_carrier_instantiates():
    """Instantiate Carrier with dummy data"""
    kwargs = {
        "id": "",
        "name": "",
    }
    obj = Carrier(**kwargs)
    assert isinstance(obj, Carrier)


def test_carrieraccount_instantiates():
    """Instantiate CarrierAccount with dummy data"""
    kwargs = {
        "carrier_account_id": "",
        "carrier_id": "",
    }
    obj = CarrierAccount(**kwargs)
    assert isinstance(obj, CarrierAccount)


def test_carrieraccountattribute_instantiates():
    """Instantiate CarrierAccountAttribute with dummy data"""
    kwargs = {
        "attribute_name": None,
        "property_group": None,
        "value": None,
    }
    obj = CarrierAccountAttribute(**kwargs)
    assert isinstance(obj, CarrierAccountAttribute)


def test_carrieraccountinput_instantiates():
    """Instantiate CarrierAccountInput with dummy data"""
    kwargs = {
        "description_localization_key": None,
        "name": None,
        "group_name": None,
        "input_type": None,
        "is_mandatory": None,
        "is_confidential": None,
        "is_hidden": None,
        "validation_metadata": None,
    }
    obj = CarrierAccountInput(**kwargs)
    assert isinstance(obj, CarrierAccountInput)


def test_channeldetails_instantiates():
    """Instantiate ChannelDetails with dummy data"""
    kwargs = {
        "channel_type": "",
        "amazon_order_details": None,
        "amazon_shipment_details": None,
    }
    obj = ChannelDetails(**kwargs)
    assert isinstance(obj, ChannelDetails)


def test_chargecomponent_instantiates():
    """Instantiate ChargeComponent with dummy data"""
    kwargs = {
        "amount": None,
        "charge_type": None,
    }
    obj = ChargeComponent(**kwargs)
    assert isinstance(obj, ChargeComponent)


def test_claimproofurls_instantiates():
    """Instantiate ClaimProofURLs with dummy data"""
    kwargs = {}
    obj = ClaimProofURLs(**kwargs)
    assert isinstance(obj, ClaimProofURLs)


def test_clientreferencedetail_instantiates():
    """Instantiate ClientReferenceDetail with dummy data"""
    kwargs = {
        "client_reference_type": ClientReferenceTypeEnum.INTEGRATOR_SHIPPER_ID,
        "client_reference_id": "",
    }
    obj = ClientReferenceDetail(**kwargs)
    assert isinstance(obj, ClientReferenceDetail)


def test_collectondelivery_instantiates():
    """Instantiate CollectOnDelivery with dummy data"""
    kwargs = {
        "amount": Currency(**{"value": 0.0, "unit": ""}),
    }
    obj = CollectOnDelivery(**kwargs)
    assert isinstance(obj, CollectOnDelivery)


def test_collectionformshistoryrecord_instantiates():
    """Instantiate CollectionFormsHistoryRecord with dummy data"""
    kwargs = {
        "carrier_name": None,
        "creation_date": None,
        "generation_status": None,
        "collection_form_id": None,
        "ship_from_address": None,
    }
    obj = CollectionFormsHistoryRecord(**kwargs)
    assert isinstance(obj, CollectionFormsHistoryRecord)


def test_collectionsformdocument_instantiates():
    """Instantiate CollectionsFormDocument with dummy data"""
    kwargs = {
        "base64_encoded_content": None,
        "document_format": None,
    }
    obj = CollectionsFormDocument(**kwargs)
    assert isinstance(obj, CollectionsFormDocument)


def test_createclaimrequestbody_instantiates():
    """Instantiate CreateClaimRequestBody with dummy data"""
    kwargs = {
        "tracking_id": "",
        "declared_value": None,
        "claim_reason": "",
        "is_replacement_package_sent": None,
        "proofs": None,
        "settlement_type": "",
    }
    obj = CreateClaimRequestBody(**kwargs)
    assert isinstance(obj, CreateClaimRequestBody)


def test_createclaimrequest_instantiates():
    """Instantiate CreateClaimRequest with dummy data"""
    kwargs = {
        "body": CreateClaimRequestBody(
            **{
                "tracking_id": "",
                "declared_value": None,
                "claim_reason": "",
                "is_replacement_package_sent": None,
                "proofs": None,
                "settlement_type": "",
            }
        ),
    }
    obj = CreateClaimRequest(**kwargs)
    assert isinstance(obj, CreateClaimRequest)


def test_createclaimresponse_instantiates():
    """Instantiate CreateClaimResponse with dummy data"""
    kwargs = {
        "claim_id": None,
    }
    obj = CreateClaimResponse(**kwargs)
    assert isinstance(obj, CreateClaimResponse)


def test_dangerousgoodsdetails_instantiates():
    """Instantiate DangerousGoodsDetails with dummy data"""
    kwargs = {
        "united_nations_regulatory_id": None,
        "transportation_regulatory_class": None,
        "packing_group": None,
        "packing_instruction": None,
    }
    obj = DangerousGoodsDetails(**kwargs)
    assert isinstance(obj, DangerousGoodsDetails)


def test_dimensions_instantiates():
    """Instantiate Dimensions with dummy data"""
    kwargs = {
        "length": 0.0,
        "width": 0.0,
        "height": 0.0,
        "unit": UnitEnum.INCH,
    }
    obj = Dimensions(**kwargs)
    assert isinstance(obj, Dimensions)


def test_directfulfillmentitemidentifiers_instantiates():
    """Instantiate DirectFulfillmentItemIdentifiers with dummy data"""
    kwargs = {
        "line_item_i_d": "",
        "piece_number": None,
    }
    obj = DirectFulfillmentItemIdentifiers(**kwargs)
    assert isinstance(obj, DirectFulfillmentItemIdentifiers)


def test_documentsize_instantiates():
    """Instantiate DocumentSize with dummy data"""
    kwargs = {
        "width": 0.0,
        "length": 0.0,
        "unit": UnitEnum.INCH,
    }
    obj = DocumentSize(**kwargs)
    assert isinstance(obj, DocumentSize)


def test_requestedlabelcustomization_instantiates():
    """Instantiate RequestedLabelCustomization with dummy data"""
    kwargs = {
        "request_attributes": None,
    }
    obj = RequestedLabelCustomization(**kwargs)
    assert isinstance(obj, RequestedLabelCustomization)


def test_requesteddocumentspecification_instantiates():
    """Instantiate RequestedDocumentSpecification with dummy data"""
    kwargs = {
        "format": "",
        "size": DocumentSize(**{"width": 0.0, "length": 0.0, "unit": UnitEnum.INCH}),
        "dpi": None,
        "page_layout": None,
        "need_file_joining": False,
        "requested_document_types": [],
        "requested_label_customization": None,
    }
    obj = RequestedDocumentSpecification(**kwargs)
    assert isinstance(obj, RequestedDocumentSpecification)


def test_directpurchaserequestbody_instantiates():
    """Instantiate DirectPurchaseRequestBody with dummy data"""
    kwargs = {
        "ship_to": None,
        "ship_from": None,
        "return_to": None,
        "packages": None,
        "channel_details": ChannelDetails(
            **{
                "channel_type": "",
                "amazon_order_details": None,
                "amazon_shipment_details": None,
            }
        ),
        "label_specifications": None,
    }
    obj = DirectPurchaseRequestBody(**kwargs)
    assert isinstance(obj, DirectPurchaseRequestBody)


def test_directpurchaseresult_instantiates():
    """Instantiate DirectPurchaseResult with dummy data"""
    kwargs = {
        "shipment_id": "",
        "package_document_detail_list": None,
    }
    obj = DirectPurchaseResult(**kwargs)
    assert isinstance(obj, DirectPurchaseResult)


def test_directpurchaseresponse_instantiates():
    """Instantiate DirectPurchaseResponse with dummy data"""
    kwargs = {
        "payload": None,
    }
    obj = DirectPurchaseResponse(**kwargs)
    assert isinstance(obj, DirectPurchaseResponse)


def test_directpurchaseshipmentrequest_instantiates():
    """Instantiate DirectPurchaseShipmentRequest with dummy data"""
    kwargs = {
        "body": DirectPurchaseRequestBody(
            **{
                "ship_to": None,
                "ship_from": None,
                "return_to": None,
                "packages": None,
                "channel_details": ChannelDetails(
                    **{
                        "channel_type": "",
                        "amazon_order_details": None,
                        "amazon_shipment_details": None,
                    }
                ),
                "label_specifications": None,
            }
        ),
    }
    obj = DirectPurchaseShipmentRequest(**kwargs)
    assert isinstance(obj, DirectPurchaseShipmentRequest)


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


def test_location_instantiates():
    """Instantiate Location with dummy data"""
    kwargs = {
        "state_or_region": None,
        "city": None,
        "country_code": None,
        "postal_code": None,
    }
    obj = Location(**kwargs)
    assert isinstance(obj, Location)


def test_event_instantiates():
    """Instantiate Event with dummy data"""
    kwargs = {
        "event_code": "",
        "location": None,
        "event_time": datetime(2000, 1, 1),
        "shipment_type": None,
    }
    obj = Event(**kwargs)
    assert isinstance(obj, Event)


def test_excludedbenefitreasoncodes_instantiates():
    """Instantiate ExcludedBenefitReasonCodes with dummy data"""
    kwargs = {}
    obj = ExcludedBenefitReasonCodes(**kwargs)
    assert isinstance(obj, ExcludedBenefitReasonCodes)


def test_excludedbenefit_instantiates():
    """Instantiate ExcludedBenefit with dummy data"""
    kwargs = {
        "benefit": "",
        "reason_codes": None,
    }
    obj = ExcludedBenefit(**kwargs)
    assert isinstance(obj, ExcludedBenefit)


def test_generatecollectionformrequestbody_instantiates():
    """Instantiate GenerateCollectionFormRequestBody with dummy data"""
    kwargs = {
        "client_reference_details": None,
        "carrier_id": "",
        "ship_from_address": None,
    }
    obj = GenerateCollectionFormRequestBody(**kwargs)
    assert isinstance(obj, GenerateCollectionFormRequestBody)


def test_generatecollectionformrequest_instantiates():
    """Instantiate GenerateCollectionFormRequest with dummy data"""
    kwargs = {
        "body": GenerateCollectionFormRequestBody(
            **{
                "client_reference_details": None,
                "carrier_id": "",
                "ship_from_address": None,
            }
        ),
    }
    obj = GenerateCollectionFormRequest(**kwargs)
    assert isinstance(obj, GenerateCollectionFormRequest)


def test_generatecollectionformresponse_instantiates():
    """Instantiate GenerateCollectionFormResponse with dummy data"""
    kwargs = {
        "collections_form_document": None,
    }
    obj = GenerateCollectionFormResponse(**kwargs)
    assert isinstance(obj, GenerateCollectionFormResponse)


def test_getaccesspointsrequest_instantiates():
    """Instantiate GetAccessPointsRequest with dummy data"""
    kwargs = {
        "access_point_types": [],
        "country_code": "",
        "postal_code": "",
    }
    obj = GetAccessPointsRequest(**kwargs)
    assert isinstance(obj, GetAccessPointsRequest)


def test_getaccesspointsresult_instantiates():
    """Instantiate GetAccessPointsResult with dummy data"""
    kwargs = {
        "access_points_map": AccessPointsMap(**{}),
    }
    obj = GetAccessPointsResult(**kwargs)
    assert isinstance(obj, GetAccessPointsResult)


def test_getaccesspointsresponse_instantiates():
    """Instantiate GetAccessPointsResponse with dummy data"""
    kwargs = {
        "payload": None,
    }
    obj = GetAccessPointsResponse(**kwargs)
    assert isinstance(obj, GetAccessPointsResponse)


def test_getadditionalinputsrequest_instantiates():
    """Instantiate GetAdditionalInputsRequest with dummy data"""
    kwargs = {
        "request_token": "",
        "rate_id": "",
    }
    obj = GetAdditionalInputsRequest(**kwargs)
    assert isinstance(obj, GetAdditionalInputsRequest)


def test_getadditionalinputsresult_instantiates():
    """Instantiate GetAdditionalInputsResult with dummy data"""
    kwargs = {}
    obj = GetAdditionalInputsResult(**kwargs)
    assert isinstance(obj, GetAdditionalInputsResult)


def test_getadditionalinputsresponse_instantiates():
    """Instantiate GetAdditionalInputsResponse with dummy data"""
    kwargs = {
        "payload": None,
    }
    obj = GetAdditionalInputsResponse(**kwargs)
    assert isinstance(obj, GetAdditionalInputsResponse)


def test_getcarrieraccountforminputsresponse_instantiates():
    """Instantiate GetCarrierAccountFormInputsResponse with dummy data"""
    kwargs = {
        "linkable_carriers_list": None,
    }
    obj = GetCarrierAccountFormInputsResponse(**kwargs)
    assert isinstance(obj, GetCarrierAccountFormInputsResponse)


def test_getcarrieraccountsrequestbody_instantiates():
    """Instantiate GetCarrierAccountsRequestBody with dummy data"""
    kwargs = {
        "client_reference_details": None,
    }
    obj = GetCarrierAccountsRequestBody(**kwargs)
    assert isinstance(obj, GetCarrierAccountsRequestBody)


def test_getcarrieraccountsrequest_instantiates():
    """Instantiate GetCarrierAccountsRequest with dummy data"""
    kwargs = {
        "body": GetCarrierAccountsRequestBody(**{"client_reference_details": None}),
    }
    obj = GetCarrierAccountsRequest(**kwargs)
    assert isinstance(obj, GetCarrierAccountsRequest)


def test_getcarrieraccountsresponse_instantiates():
    """Instantiate GetCarrierAccountsResponse with dummy data"""
    kwargs = {
        "active_accounts": [],
    }
    obj = GetCarrierAccountsResponse(**kwargs)
    assert isinstance(obj, GetCarrierAccountsResponse)


def test_getcollectionformhistoryrequestbody_instantiates():
    """Instantiate GetCollectionFormHistoryRequestBody with dummy data"""
    kwargs = {
        "client_reference_details": None,
        "max_results": None,
        "carrier_id": None,
        "ship_from_address": None,
        "date_range": None,
    }
    obj = GetCollectionFormHistoryRequestBody(**kwargs)
    assert isinstance(obj, GetCollectionFormHistoryRequestBody)


def test_getcollectionformhistoryrequest_instantiates():
    """Instantiate GetCollectionFormHistoryRequest with dummy data"""
    kwargs = {
        "body": GetCollectionFormHistoryRequestBody(
            **{
                "client_reference_details": None,
                "max_results": None,
                "carrier_id": None,
                "ship_from_address": None,
                "date_range": None,
            }
        ),
    }
    obj = GetCollectionFormHistoryRequest(**kwargs)
    assert isinstance(obj, GetCollectionFormHistoryRequest)


def test_getcollectionformhistoryresponse_instantiates():
    """Instantiate GetCollectionFormHistoryResponse with dummy data"""
    kwargs = {
        "collection_forms_history_record_list": None,
        "last_refreshed_date": None,
    }
    obj = GetCollectionFormHistoryResponse(**kwargs)
    assert isinstance(obj, GetCollectionFormHistoryResponse)


def test_getcollectionformrequest_instantiates():
    """Instantiate GetCollectionFormRequest with dummy data"""
    kwargs = {
        "collection_form_id": "",
    }
    obj = GetCollectionFormRequest(**kwargs)
    assert isinstance(obj, GetCollectionFormRequest)


def test_getcollectionformresponse_instantiates():
    """Instantiate GetCollectionFormResponse with dummy data"""
    kwargs = {
        "collections_form_document": None,
    }
    obj = GetCollectionFormResponse(**kwargs)
    assert isinstance(obj, GetCollectionFormResponse)


def test_shipperinstruction_instantiates():
    """Instantiate ShipperInstruction with dummy data"""
    kwargs = {
        "delivery_notes": None,
    }
    obj = ShipperInstruction(**kwargs)
    assert isinstance(obj, ShipperInstruction)


def test_valueaddedservicedetails_instantiates():
    """Instantiate ValueAddedServiceDetails with dummy data"""
    kwargs = {
        "collect_on_delivery": None,
    }
    obj = ValueAddedServiceDetails(**kwargs)
    assert isinstance(obj, ValueAddedServiceDetails)


def test_getratesrequestbody_instantiates():
    """Instantiate GetRatesRequestBody with dummy data"""
    kwargs = {
        "ship_to": None,
        "ship_from": Address(
            **{
                "name": "",
                "address_line1": "",
                "address_line2": None,
                "address_line3": None,
                "company_name": None,
                "state_or_region": "",
                "city": "",
                "country_code": "",
                "postal_code": "",
                "email": None,
                "phone_number": None,
                "geocode": None,
            }
        ),
        "return_to": None,
        "ship_date": None,
        "shipper_instruction": None,
        "packages": [],
        "value_added_services": None,
        "tax_details": None,
        "channel_details": ChannelDetails(
            **{
                "channel_type": "",
                "amazon_order_details": None,
                "amazon_shipment_details": None,
            }
        ),
        "client_reference_details": None,
        "shipment_type": None,
        "destination_access_point_details": None,
        "carrier_accounts": None,
    }
    obj = GetRatesRequestBody(**kwargs)
    assert isinstance(obj, GetRatesRequestBody)


def test_getratesrequest_instantiates():
    """Instantiate GetRatesRequest with dummy data"""
    kwargs = {
        "body": GetRatesRequestBody(
            **{
                "ship_to": None,
                "ship_from": Address(
                    **{
                        "name": "",
                        "address_line1": "",
                        "address_line2": None,
                        "address_line3": None,
                        "company_name": None,
                        "state_or_region": "",
                        "city": "",
                        "country_code": "",
                        "postal_code": "",
                        "email": None,
                        "phone_number": None,
                        "geocode": None,
                    }
                ),
                "return_to": None,
                "ship_date": None,
                "shipper_instruction": None,
                "packages": [],
                "value_added_services": None,
                "tax_details": None,
                "channel_details": ChannelDetails(
                    **{
                        "channel_type": "",
                        "amazon_order_details": None,
                        "amazon_shipment_details": None,
                    }
                ),
                "client_reference_details": None,
                "shipment_type": None,
                "destination_access_point_details": None,
                "carrier_accounts": None,
            }
        ),
    }
    obj = GetRatesRequest(**kwargs)
    assert isinstance(obj, GetRatesRequest)


def test_getratesresult_instantiates():
    """Instantiate GetRatesResult with dummy data"""
    kwargs = {
        "request_token": "",
        "rates": [],
        "ineligible_rates": None,
    }
    obj = GetRatesResult(**kwargs)
    assert isinstance(obj, GetRatesResult)


def test_getratesresponse_instantiates():
    """Instantiate GetRatesResponse with dummy data"""
    kwargs = {
        "payload": None,
    }
    obj = GetRatesResponse(**kwargs)
    assert isinstance(obj, GetRatesResponse)


def test_getshipmentdocumentsrequest_instantiates():
    """Instantiate GetShipmentDocumentsRequest with dummy data"""
    kwargs = {
        "shipment_id": "",
        "package_client_reference_id": "",
        "format": None,
        "dpi": None,
    }
    obj = GetShipmentDocumentsRequest(**kwargs)
    assert isinstance(obj, GetShipmentDocumentsRequest)


def test_packagedocumentdetail_instantiates():
    """Instantiate PackageDocumentDetail with dummy data"""
    kwargs = {
        "package_client_reference_id": "",
        "package_documents": [],
        "tracking_id": None,
    }
    obj = PackageDocumentDetail(**kwargs)
    assert isinstance(obj, PackageDocumentDetail)


def test_getshipmentdocumentsresult_instantiates():
    """Instantiate GetShipmentDocumentsResult with dummy data"""
    kwargs = {
        "shipment_id": "",
        "package_document_detail": PackageDocumentDetail(
            **{
                "package_client_reference_id": "",
                "package_documents": [],
                "tracking_id": None,
            }
        ),
        "benefits": None,
    }
    obj = GetShipmentDocumentsResult(**kwargs)
    assert isinstance(obj, GetShipmentDocumentsResult)


def test_getshipmentdocumentsresponse_instantiates():
    """Instantiate GetShipmentDocumentsResponse with dummy data"""
    kwargs = {
        "payload": None,
    }
    obj = GetShipmentDocumentsResponse(**kwargs)
    assert isinstance(obj, GetShipmentDocumentsResponse)


def test_gettrackingrequest_instantiates():
    """Instantiate GetTrackingRequest with dummy data"""
    kwargs = {
        "tracking_id": "",
        "carrier_id": "",
    }
    obj = GetTrackingRequest(**kwargs)
    assert isinstance(obj, GetTrackingRequest)


def test_trackingdetailcodes_instantiates():
    """Instantiate TrackingDetailCodes with dummy data"""
    kwargs = {
        "forward": [],
        "returns": [],
    }
    obj = TrackingDetailCodes(**kwargs)
    assert isinstance(obj, TrackingDetailCodes)


def test_trackingsummary_instantiates():
    """Instantiate TrackingSummary with dummy data"""
    kwargs = {
        "status": None,
        "tracking_detail_codes": None,
    }
    obj = TrackingSummary(**kwargs)
    assert isinstance(obj, TrackingSummary)


def test_gettrackingresult_instantiates():
    """Instantiate GetTrackingResult with dummy data"""
    kwargs = {
        "tracking_id": "",
        "alternate_leg_tracking_id": "",
        "event_history": [],
        "promised_delivery_date": datetime(2000, 1, 1),
        "summary": TrackingSummary(**{"status": None, "tracking_detail_codes": None}),
    }
    obj = GetTrackingResult(**kwargs)
    assert isinstance(obj, GetTrackingResult)


def test_gettrackingresponse_instantiates():
    """Instantiate GetTrackingResponse with dummy data"""
    kwargs = {
        "payload": None,
    }
    obj = GetTrackingResponse(**kwargs)
    assert isinstance(obj, GetTrackingResponse)


def test_getunmanifestedshipmentsrequestbody_instantiates():
    """Instantiate GetUnmanifestedShipmentsRequestBody with dummy data"""
    kwargs = {
        "client_reference_details": None,
    }
    obj = GetUnmanifestedShipmentsRequestBody(**kwargs)
    assert isinstance(obj, GetUnmanifestedShipmentsRequestBody)


def test_getunmanifestedshipmentsrequest_instantiates():
    """Instantiate GetUnmanifestedShipmentsRequest with dummy data"""
    kwargs = {
        "body": GetUnmanifestedShipmentsRequestBody(
            **{"client_reference_details": None}
        ),
    }
    obj = GetUnmanifestedShipmentsRequest(**kwargs)
    assert isinstance(obj, GetUnmanifestedShipmentsRequest)


def test_getunmanifestedshipmentsresponse_instantiates():
    """Instantiate GetUnmanifestedShipmentsResponse with dummy data"""
    kwargs = {
        "unmanifested_carrier_information_list": None,
    }
    obj = GetUnmanifestedShipmentsResponse(**kwargs)
    assert isinstance(obj, GetUnmanifestedShipmentsResponse)


def test_goodsowner_instantiates():
    """Instantiate GoodsOwner with dummy data"""
    kwargs = {
        "merchant_id": "",
    }
    obj = GoodsOwner(**kwargs)
    assert isinstance(obj, GoodsOwner)


def test_ineligibilityreason_instantiates():
    """Instantiate IneligibilityReason with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
    }
    obj = IneligibilityReason(**kwargs)
    assert isinstance(obj, IneligibilityReason)


def test_ineligiblerate_instantiates():
    """Instantiate IneligibleRate with dummy data"""
    kwargs = {
        "service_id": "",
        "service_name": "",
        "carrier_name": "",
        "carrier_id": "",
        "ineligibility_reasons": [],
    }
    obj = IneligibleRate(**kwargs)
    assert isinstance(obj, IneligibleRate)


def test_invoicedetails_instantiates():
    """Instantiate InvoiceDetails with dummy data"""
    kwargs = {
        "invoice_number": None,
        "invoice_date": None,
    }
    obj = InvoiceDetails(**kwargs)
    assert isinstance(obj, InvoiceDetails)


def test_liquidvolume_instantiates():
    """Instantiate LiquidVolume with dummy data"""
    kwargs = {
        "unit": UnitEnum.INCH,
        "value": 0.0,
    }
    obj = LiquidVolume(**kwargs)
    assert isinstance(obj, LiquidVolume)


def test_weight_instantiates():
    """Instantiate Weight with dummy data"""
    kwargs = {
        "unit": UnitEnum.INCH,
        "value": 0.0,
    }
    obj = Weight(**kwargs)
    assert isinstance(obj, Weight)


def test_item_instantiates():
    """Instantiate Item with dummy data"""
    kwargs = {
        "item_value": None,
        "description": None,
        "item_identifier": None,
        "quantity": 0,
        "weight": None,
        "liquid_volume": None,
        "is_hazmat": None,
        "dangerous_goods_details": None,
        "product_type": None,
        "invoice_details": None,
        "serial_numbers": None,
        "direct_fulfillment_item_identifiers": None,
    }
    obj = Item(**kwargs)
    assert isinstance(obj, Item)


def test_linkcarrieraccountrequestbody_instantiates():
    """Instantiate LinkCarrierAccountRequestBody with dummy data"""
    kwargs = {
        "client_reference_details": None,
        "carrier_account_type": "",
        "carrier_account_attributes": [],
        "encrypted_carrier_account_attributes": None,
    }
    obj = LinkCarrierAccountRequestBody(**kwargs)
    assert isinstance(obj, LinkCarrierAccountRequestBody)


def test_linkcarrieraccountrequest_instantiates():
    """Instantiate LinkCarrierAccountRequest with dummy data"""
    kwargs = {
        "carrier_id": "",
        "body": LinkCarrierAccountRequestBody(
            **{
                "client_reference_details": None,
                "carrier_account_type": "",
                "carrier_account_attributes": [],
                "encrypted_carrier_account_attributes": None,
            }
        ),
    }
    obj = LinkCarrierAccountRequest(**kwargs)
    assert isinstance(obj, LinkCarrierAccountRequest)


def test_linkcarrieraccountresponse_instantiates():
    """Instantiate LinkCarrierAccountResponse with dummy data"""
    kwargs = {
        "registration_status": None,
        "account_id": None,
    }
    obj = LinkCarrierAccountResponse(**kwargs)
    assert isinstance(obj, LinkCarrierAccountResponse)


def test_linkableaccounttype_instantiates():
    """Instantiate LinkableAccountType with dummy data"""
    kwargs = {
        "account_type": None,
        "carrier_account_inputs": None,
    }
    obj = LinkableAccountType(**kwargs)
    assert isinstance(obj, LinkableAccountType)


def test_linkablecarrier_instantiates():
    """Instantiate LinkableCarrier with dummy data"""
    kwargs = {
        "carrier_id": None,
        "linkable_account_types": None,
    }
    obj = LinkableCarrier(**kwargs)
    assert isinstance(obj, LinkableCarrier)


def test_ndrrequestdata_instantiates():
    """Instantiate NdrRequestData with dummy data"""
    kwargs = {
        "reschedule_date": None,
        "additional_address_notes": None,
    }
    obj = NdrRequestData(**kwargs)
    assert isinstance(obj, NdrRequestData)


def test_serviceids_instantiates():
    """Instantiate ServiceIds with dummy data"""
    kwargs = {}
    obj = ServiceIds(**kwargs)
    assert isinstance(obj, ServiceIds)


def test_serviceselection_instantiates():
    """Instantiate ServiceSelection with dummy data"""
    kwargs = {
        "service_id": ServiceIds(**{}),
    }
    obj = ServiceSelection(**kwargs)
    assert isinstance(obj, ServiceSelection)


def test_oneclickshipmentrequestbody_instantiates():
    """Instantiate OneClickShipmentRequestBody with dummy data"""
    kwargs = {
        "ship_to": None,
        "ship_from": Address(
            **{
                "name": "",
                "address_line1": "",
                "address_line2": None,
                "address_line3": None,
                "company_name": None,
                "state_or_region": "",
                "city": "",
                "country_code": "",
                "postal_code": "",
                "email": None,
                "phone_number": None,
                "geocode": None,
            }
        ),
        "return_to": None,
        "ship_date": None,
        "goods_owner": None,
        "packages": [],
        "value_added_services_details": None,
        "tax_details": None,
        "channel_details": ChannelDetails(
            **{
                "channel_type": "",
                "amazon_order_details": None,
                "amazon_shipment_details": None,
            }
        ),
        "label_specifications": RequestedDocumentSpecification(
            **{
                "format": "",
                "size": DocumentSize(
                    **{"width": 0.0, "length": 0.0, "unit": UnitEnum.INCH}
                ),
                "dpi": None,
                "page_layout": None,
                "need_file_joining": False,
                "requested_document_types": [],
                "requested_label_customization": None,
            }
        ),
        "service_selection": ServiceSelection(**{"service_id": ServiceIds(**{})}),
        "shipper_instruction": None,
        "destination_access_point_details": None,
    }
    obj = OneClickShipmentRequestBody(**kwargs)
    assert isinstance(obj, OneClickShipmentRequestBody)


def test_oneclickshipmentrequest_instantiates():
    """Instantiate OneClickShipmentRequest with dummy data"""
    kwargs = {
        "body": OneClickShipmentRequestBody(
            **{
                "ship_to": None,
                "ship_from": Address(
                    **{
                        "name": "",
                        "address_line1": "",
                        "address_line2": None,
                        "address_line3": None,
                        "company_name": None,
                        "state_or_region": "",
                        "city": "",
                        "country_code": "",
                        "postal_code": "",
                        "email": None,
                        "phone_number": None,
                        "geocode": None,
                    }
                ),
                "return_to": None,
                "ship_date": None,
                "goods_owner": None,
                "packages": [],
                "value_added_services_details": None,
                "tax_details": None,
                "channel_details": ChannelDetails(
                    **{
                        "channel_type": "",
                        "amazon_order_details": None,
                        "amazon_shipment_details": None,
                    }
                ),
                "label_specifications": RequestedDocumentSpecification(
                    **{
                        "format": "",
                        "size": DocumentSize(
                            **{"width": 0.0, "length": 0.0, "unit": UnitEnum.INCH}
                        ),
                        "dpi": None,
                        "page_layout": None,
                        "need_file_joining": False,
                        "requested_document_types": [],
                        "requested_label_customization": None,
                    }
                ),
                "service_selection": ServiceSelection(
                    **{"service_id": ServiceIds(**{})}
                ),
                "shipper_instruction": None,
                "destination_access_point_details": None,
            }
        ),
    }
    obj = OneClickShipmentRequest(**kwargs)
    assert isinstance(obj, OneClickShipmentRequest)


def test_timewindow_instantiates():
    """Instantiate TimeWindow with dummy data"""
    kwargs = {
        "start": None,
        "end": None,
    }
    obj = TimeWindow(**kwargs)
    assert isinstance(obj, TimeWindow)


def test_promise_instantiates():
    """Instantiate Promise with dummy data"""
    kwargs = {
        "delivery_window": None,
        "pickup_window": None,
    }
    obj = Promise(**kwargs)
    assert isinstance(obj, Promise)


def test_service_instantiates():
    """Instantiate Service with dummy data"""
    kwargs = {
        "id": "",
        "name": "",
    }
    obj = Service(**kwargs)
    assert isinstance(obj, Service)


def test_oneclickshipmentresult_instantiates():
    """Instantiate OneClickShipmentResult with dummy data"""
    kwargs = {
        "shipment_id": "",
        "package_document_details": [],
        "promise": Promise(**{"delivery_window": None, "pickup_window": None}),
        "carrier": Carrier(**{"id": "", "name": ""}),
        "service": Service(**{"id": "", "name": ""}),
        "total_charge": Currency(**{"value": 0.0, "unit": ""}),
    }
    obj = OneClickShipmentResult(**kwargs)
    assert isinstance(obj, OneClickShipmentResult)


def test_oneclickshipmentresponse_instantiates():
    """Instantiate OneClickShipmentResponse with dummy data"""
    kwargs = {
        "payload": None,
    }
    obj = OneClickShipmentResponse(**kwargs)
    assert isinstance(obj, OneClickShipmentResponse)


def test_oneclickshipmentvalueaddedservice_instantiates():
    """Instantiate OneClickShipmentValueAddedService with dummy data"""
    kwargs = {
        "id": "",
        "amount": None,
    }
    obj = OneClickShipmentValueAddedService(**kwargs)
    assert isinstance(obj, OneClickShipmentValueAddedService)


def test_package_instantiates():
    """Instantiate Package with dummy data"""
    kwargs = {
        "dimensions": Dimensions(
            **{"length": 0.0, "width": 0.0, "height": 0.0, "unit": UnitEnum.INCH}
        ),
        "weight": Weight(**{"unit": UnitEnum.INCH, "value": 0.0}),
        "insured_value": Currency(**{"value": 0.0, "unit": ""}),
        "is_hazmat": None,
        "seller_display_name": None,
        "charges": None,
        "package_client_reference_id": "",
        "items": [],
    }
    obj = Package(**kwargs)
    assert isinstance(obj, Package)


def test_packagedocument_instantiates():
    """Instantiate PackageDocument with dummy data"""
    kwargs = {
        "type": "",
        "format": "",
        "contents": "",
    }
    obj = PackageDocument(**kwargs)
    assert isinstance(obj, PackageDocument)


def test_supporteddocumentdetail_instantiates():
    """Instantiate SupportedDocumentDetail with dummy data"""
    kwargs = {
        "name": "",
        "is_mandatory": False,
    }
    obj = SupportedDocumentDetail(**kwargs)
    assert isinstance(obj, SupportedDocumentDetail)


def test_printoption_instantiates():
    """Instantiate PrintOption with dummy data"""
    kwargs = {
        "supported_d_p_is": None,
        "supported_page_layouts": [],
        "supported_file_joining_options": [],
        "supported_document_details": [],
    }
    obj = PrintOption(**kwargs)
    assert isinstance(obj, PrintOption)


def test_purchaseshipmentrequestbody_instantiates():
    """Instantiate PurchaseShipmentRequestBody with dummy data"""
    kwargs = {
        "request_token": "",
        "rate_id": "",
        "requested_document_specification": RequestedDocumentSpecification(
            **{
                "format": "",
                "size": DocumentSize(
                    **{"width": 0.0, "length": 0.0, "unit": UnitEnum.INCH}
                ),
                "dpi": None,
                "page_layout": None,
                "need_file_joining": False,
                "requested_document_types": [],
                "requested_label_customization": None,
            }
        ),
        "requested_value_added_services": None,
        "additional_inputs": None,
    }
    obj = PurchaseShipmentRequestBody(**kwargs)
    assert isinstance(obj, PurchaseShipmentRequestBody)


def test_purchaseshipmentrequest_instantiates():
    """Instantiate PurchaseShipmentRequest with dummy data"""
    kwargs = {
        "body": PurchaseShipmentRequestBody(
            **{
                "request_token": "",
                "rate_id": "",
                "requested_document_specification": RequestedDocumentSpecification(
                    **{
                        "format": "",
                        "size": DocumentSize(
                            **{"width": 0.0, "length": 0.0, "unit": UnitEnum.INCH}
                        ),
                        "dpi": None,
                        "page_layout": None,
                        "need_file_joining": False,
                        "requested_document_types": [],
                        "requested_label_customization": None,
                    }
                ),
                "requested_value_added_services": None,
                "additional_inputs": None,
            }
        ),
    }
    obj = PurchaseShipmentRequest(**kwargs)
    assert isinstance(obj, PurchaseShipmentRequest)


def test_purchaseshipmentresult_instantiates():
    """Instantiate PurchaseShipmentResult with dummy data"""
    kwargs = {
        "shipment_id": "",
        "package_document_details": [],
        "promise": Promise(**{"delivery_window": None, "pickup_window": None}),
        "benefits": None,
    }
    obj = PurchaseShipmentResult(**kwargs)
    assert isinstance(obj, PurchaseShipmentResult)


def test_purchaseshipmentresponse_instantiates():
    """Instantiate PurchaseShipmentResponse with dummy data"""
    kwargs = {
        "payload": None,
    }
    obj = PurchaseShipmentResponse(**kwargs)
    assert isinstance(obj, PurchaseShipmentResponse)


def test_rate_instantiates():
    """Instantiate Rate with dummy data"""
    kwargs = {
        "rate_id": "",
        "carrier_id": "",
        "carrier_name": "",
        "service_id": "",
        "service_name": "",
        "billed_weight": None,
        "total_charge": Currency(**{"value": 0.0, "unit": ""}),
        "promise": Promise(**{"delivery_window": None, "pickup_window": None}),
        "supported_document_specifications": [],
        "available_value_added_service_groups": None,
        "requires_additional_inputs": False,
        "rate_item_list": None,
        "payment_type": None,
        "benefits": None,
    }
    obj = Rate(**kwargs)
    assert isinstance(obj, Rate)


def test_rateitem_instantiates():
    """Instantiate RateItem with dummy data"""
    kwargs = {
        "rate_item_i_d": None,
        "rate_item_type": None,
        "rate_item_charge": None,
        "rate_item_name_localization": None,
    }
    obj = RateItem(**kwargs)
    assert isinstance(obj, RateItem)


def test_requestedvalueaddedservice_instantiates():
    """Instantiate RequestedValueAddedService with dummy data"""
    kwargs = {
        "id": "",
    }
    obj = RequestedValueAddedService(**kwargs)
    assert isinstance(obj, RequestedValueAddedService)


def test_submitndrfeedbackrequestbody_instantiates():
    """Instantiate SubmitNdrFeedbackRequestBody with dummy data"""
    kwargs = {
        "tracking_id": "",
        "ndr_action": "",
        "ndr_request_data": None,
    }
    obj = SubmitNdrFeedbackRequestBody(**kwargs)
    assert isinstance(obj, SubmitNdrFeedbackRequestBody)


def test_submitndrfeedbackrequest_instantiates():
    """Instantiate SubmitNdrFeedbackRequest with dummy data"""
    kwargs = {
        "body": SubmitNdrFeedbackRequestBody(
            **{"tracking_id": "", "ndr_action": "", "ndr_request_data": None}
        ),
    }
    obj = SubmitNdrFeedbackRequest(**kwargs)
    assert isinstance(obj, SubmitNdrFeedbackRequest)


def test_supporteddocumentspecification_instantiates():
    """Instantiate SupportedDocumentSpecification with dummy data"""
    kwargs = {
        "format": "",
        "size": DocumentSize(**{"width": 0.0, "length": 0.0, "unit": UnitEnum.INCH}),
        "print_options": [],
    }
    obj = SupportedDocumentSpecification(**kwargs)
    assert isinstance(obj, SupportedDocumentSpecification)


def test_taxdetail_instantiates():
    """Instantiate TaxDetail with dummy data"""
    kwargs = {
        "tax_type": "",
        "tax_registration_number": "",
    }
    obj = TaxDetail(**kwargs)
    assert isinstance(obj, TaxDetail)


def test_unlinkcarrieraccountrequestbody_instantiates():
    """Instantiate UnlinkCarrierAccountRequestBody with dummy data"""
    kwargs = {
        "client_reference_details": None,
        "account_id": None,
    }
    obj = UnlinkCarrierAccountRequestBody(**kwargs)
    assert isinstance(obj, UnlinkCarrierAccountRequestBody)


def test_unlinkcarrieraccountrequest_instantiates():
    """Instantiate UnlinkCarrierAccountRequest with dummy data"""
    kwargs = {
        "carrier_id": "",
        "body": UnlinkCarrierAccountRequestBody(
            **{"client_reference_details": None, "account_id": None}
        ),
    }
    obj = UnlinkCarrierAccountRequest(**kwargs)
    assert isinstance(obj, UnlinkCarrierAccountRequest)


def test_unlinkcarrieraccountresponse_instantiates():
    """Instantiate UnlinkCarrierAccountResponse with dummy data"""
    kwargs = {
        "is_unlinked": None,
    }
    obj = UnlinkCarrierAccountResponse(**kwargs)
    assert isinstance(obj, UnlinkCarrierAccountResponse)


def test_unmanifestedcarrierinformation_instantiates():
    """Instantiate UnmanifestedCarrierInformation with dummy data"""
    kwargs = {
        "carrier_id": None,
        "carrier_name": None,
        "unmanifested_shipment_location_list": None,
    }
    obj = UnmanifestedCarrierInformation(**kwargs)
    assert isinstance(obj, UnmanifestedCarrierInformation)


def test_unmanifestedshipmentlocation_instantiates():
    """Instantiate UnmanifestedShipmentLocation with dummy data"""
    kwargs = {
        "address": None,
        "last_manifest_date": None,
    }
    obj = UnmanifestedShipmentLocation(**kwargs)
    assert isinstance(obj, UnmanifestedShipmentLocation)


def test_validationmetadata_instantiates():
    """Instantiate ValidationMetadata with dummy data"""
    kwargs = {
        "error_message": None,
        "validation_strategy": None,
        "value": None,
    }
    obj = ValidationMetadata(**kwargs)
    assert isinstance(obj, ValidationMetadata)
