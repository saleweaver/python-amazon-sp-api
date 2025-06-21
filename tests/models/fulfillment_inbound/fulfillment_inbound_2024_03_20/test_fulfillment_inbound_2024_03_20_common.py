# Auto-generated tests for sp_api.api.models.fulfillment_inbound.fulfillment_inbound_2024_03_20.common.py
from datetime import datetime

import pytest
from sp_api.api.models.fulfillment_inbound.fulfillment_inbound_2024_03_20.common import (
    Address, AddressInput, AppointmentSlot, AppointmentSlotTime, Box, BoxInput,
    BoxRequirements, BoxUpdateInput, CancelInboundPlanRequest,
    CancelInboundPlanResponse, CancelSelfShipAppointmentRequest,
    CancelSelfShipAppointmentRequestBody, CancelSelfShipAppointmentResponse,
    Carrier, CarrierAppointment, ComplianceDetail,
    ConfirmDeliveryWindowOptionsRequest, ConfirmDeliveryWindowOptionsResponse,
    ConfirmPackingOptionRequest, ConfirmPackingOptionResponse,
    ConfirmPlacementOptionRequest, ConfirmPlacementOptionResponse,
    ConfirmShipmentContentUpdatePreviewRequest,
    ConfirmShipmentContentUpdatePreviewResponse,
    ConfirmTransportationOptionsRequest,
    ConfirmTransportationOptionsRequestBody,
    ConfirmTransportationOptionsResponse, ContactInformation,
    ContentUpdatePreview, CreateInboundPlanRequest,
    CreateInboundPlanRequestBody, CreateInboundPlanResponse,
    CreateMarketplaceItemLabelsRequest, CreateMarketplaceItemLabelsRequestBody,
    CreateMarketplaceItemLabelsResponse, Currency, CustomPlacementInput, Dates,
    DeliveryWindowOption, Dimensions, DocumentDownload, Error, ErrorList,
    FreightInformation, GenerateDeliveryWindowOptionsRequest,
    GenerateDeliveryWindowOptionsResponse, GeneratePackingOptionsRequest,
    GeneratePackingOptionsResponse, GeneratePlacementOptionsRequest,
    GeneratePlacementOptionsRequestBody, GeneratePlacementOptionsResponse,
    GenerateSelfShipAppointmentSlotsRequest,
    GenerateSelfShipAppointmentSlotsRequestBody,
    GenerateSelfShipAppointmentSlotsResponse,
    GenerateShipmentContentUpdatePreviewsRequest,
    GenerateShipmentContentUpdatePreviewsRequestBody,
    GenerateShipmentContentUpdatePreviewsResponse,
    GenerateTransportationOptionsRequest,
    GenerateTransportationOptionsRequestBody,
    GenerateTransportationOptionsResponse, GetDeliveryChallanDocumentRequest,
    GetDeliveryChallanDocumentResponse, GetInboundOperationStatusRequest,
    GetInboundPlanRequest, GetRequestSerializer,
    GetSelfShipAppointmentSlotsRequest, GetSelfShipAppointmentSlotsResponse,
    GetShipmentContentUpdatePreviewRequest, GetShipmentRequest,
    InboundOperationStatus, InboundPlan, InboundPlanSummary, Incentive, Item,
    ItemInput, ListDeliveryWindowOptionsRequest,
    ListDeliveryWindowOptionsResponse, ListInboundPlanBoxesRequest,
    ListInboundPlanBoxesResponse, ListInboundPlanItemsRequest,
    ListInboundPlanItemsResponse, ListInboundPlanPalletsRequest,
    ListInboundPlanPalletsResponse, ListInboundPlansRequest,
    ListInboundPlansResponse, ListItemComplianceDetailsRequest,
    ListItemComplianceDetailsResponse, ListPackingGroupBoxesRequest,
    ListPackingGroupBoxesResponse, ListPackingGroupItemsRequest,
    ListPackingGroupItemsResponse, ListPackingOptionsRequest,
    ListPackingOptionsResponse, ListPlacementOptionsRequest,
    ListPlacementOptionsResponse, ListPrepDetailsRequest,
    ListPrepDetailsResponse, ListShipmentBoxesRequest,
    ListShipmentBoxesResponse, ListShipmentContentUpdatePreviewsRequest,
    ListShipmentContentUpdatePreviewsResponse, ListShipmentItemsRequest,
    ListShipmentItemsResponse, ListShipmentPalletsRequest,
    ListShipmentPalletsResponse, ListTransportationOptionsRequest,
    ListTransportationOptionsResponse, LtlTrackingDetail,
    LtlTrackingDetailInput, MskuPrepDetail, MskuPrepDetailInput, MskuQuantity,
    OperationProblem, PackageGroupingInput, PackingConfiguration,
    PackingOption, PackingOptionSummary, Pagination, Pallet, PalletInput,
    PlacementOption, PlacementOptionSummary, PrepInstruction, Quote, Region,
    RequestedUpdates, RequestsBaseModel, ScheduleSelfShipAppointmentRequest,
    ScheduleSelfShipAppointmentRequestBody,
    ScheduleSelfShipAppointmentResponse, SelectedDeliveryWindow,
    SelfShipAppointmentDetails, SelfShipAppointmentSlotsAvailability,
    SetPackingInformationRequest, SetPackingInformationRequestBody,
    SetPackingInformationResponse, SetPrepDetailsRequest,
    SetPrepDetailsRequestBody, SetPrepDetailsResponse, Shipment,
    ShipmentDestination, ShipmentSource, ShipmentSummary,
    ShipmentTransportationConfiguration, ShippingConfiguration,
    ShippingRequirements, SortByEnum, SortOrderEnum, SpApiBaseModel,
    SpdTrackingDetail, SpdTrackingDetailInput, SpdTrackingItem,
    SpdTrackingItemInput, StatusEnum, TaxDetails, TaxRate, TrackingDetails,
    TrackingDetailsInput, TransportationOption, TransportationSelection,
    UpdateInboundPlanNameRequest, UpdateInboundPlanNameRequestBody,
    UpdateItemComplianceDetailsRequest, UpdateItemComplianceDetailsRequestBody,
    UpdateItemComplianceDetailsResponse, UpdateShipmentNameRequest,
    UpdateShipmentNameRequestBody, UpdateShipmentSourceAddressRequest,
    UpdateShipmentSourceAddressRequestBody,
    UpdateShipmentSourceAddressResponse, UpdateShipmentTrackingDetailsRequest,
    UpdateShipmentTrackingDetailsRequestBody,
    UpdateShipmentTrackingDetailsResponse, Weight, WeightRange, Window,
    WindowInput)


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
        "city": "",
        "company_name": None,
        "country_code": "",
        "email": None,
        "name": "",
        "phone_number": None,
        "postal_code": "",
        "state_or_province_code": None,
    }
    obj = Address(**kwargs)
    assert isinstance(obj, Address)


def test_addressinput_instantiates():
    """Instantiate AddressInput with dummy data"""
    kwargs = {
        "address_line1": "",
        "address_line2": None,
        "city": "",
        "company_name": None,
        "country_code": "",
        "email": None,
        "name": "",
        "phone_number": "",
        "postal_code": "",
        "state_or_province_code": None,
    }
    obj = AddressInput(**kwargs)
    assert isinstance(obj, AddressInput)


def test_appointmentslottime_instantiates():
    """Instantiate AppointmentSlotTime with dummy data"""
    kwargs = {
        "end_time": datetime(2000, 1, 1),
        "start_time": datetime(2000, 1, 1),
    }
    obj = AppointmentSlotTime(**kwargs)
    assert isinstance(obj, AppointmentSlotTime)


def test_appointmentslot_instantiates():
    """Instantiate AppointmentSlot with dummy data"""
    kwargs = {
        "slot_id": "",
        "slot_time": AppointmentSlotTime(
            **{"end_time": datetime(2000, 1, 1), "start_time": datetime(2000, 1, 1)}
        ),
    }
    obj = AppointmentSlot(**kwargs)
    assert isinstance(obj, AppointmentSlot)


def test_dimensions_instantiates():
    """Instantiate Dimensions with dummy data"""
    kwargs = {
        "height": 0.0,
        "length": 0.0,
        "unit_of_measurement": "",
        "width": 0.0,
    }
    obj = Dimensions(**kwargs)
    assert isinstance(obj, Dimensions)


def test_currency_instantiates():
    """Instantiate Currency with dummy data"""
    kwargs = {
        "amount": 0.0,
        "code": "",
    }
    obj = Currency(**kwargs)
    assert isinstance(obj, Currency)


def test_prepinstruction_instantiates():
    """Instantiate PrepInstruction with dummy data"""
    kwargs = {
        "fee": None,
        "prep_owner": None,
        "prep_type": None,
    }
    obj = PrepInstruction(**kwargs)
    assert isinstance(obj, PrepInstruction)


def test_item_instantiates():
    """Instantiate Item with dummy data"""
    kwargs = {
        "asin": "",
        "expiration": None,
        "fnsku": "",
        "label_owner": "",
        "manufacturing_lot_code": None,
        "msku": "",
        "prep_instructions": [],
        "quantity": 0,
    }
    obj = Item(**kwargs)
    assert isinstance(obj, Item)


def test_region_instantiates():
    """Instantiate Region with dummy data"""
    kwargs = {
        "country_code": None,
        "state": None,
        "warehouse_id": None,
    }
    obj = Region(**kwargs)
    assert isinstance(obj, Region)


def test_weight_instantiates():
    """Instantiate Weight with dummy data"""
    kwargs = {
        "unit": "",
        "value": 0.0,
    }
    obj = Weight(**kwargs)
    assert isinstance(obj, Weight)


def test_box_instantiates():
    """Instantiate Box with dummy data"""
    kwargs = {
        "box_id": None,
        "content_information_source": None,
        "destination_region": None,
        "dimensions": None,
        "external_container_identifier": None,
        "external_container_identifier_type": None,
        "items": None,
        "package_id": "",
        "quantity": None,
        "template_name": None,
        "weight": None,
    }
    obj = Box(**kwargs)
    assert isinstance(obj, Box)


def test_iteminput_instantiates():
    """Instantiate ItemInput with dummy data"""
    kwargs = {
        "expiration": None,
        "label_owner": "",
        "manufacturing_lot_code": None,
        "msku": "",
        "prep_owner": "",
        "quantity": 0,
    }
    obj = ItemInput(**kwargs)
    assert isinstance(obj, ItemInput)


def test_boxinput_instantiates():
    """Instantiate BoxInput with dummy data"""
    kwargs = {
        "content_information_source": "",
        "dimensions": Dimensions(
            **{"height": 0.0, "length": 0.0, "unit_of_measurement": "", "width": 0.0}
        ),
        "items": None,
        "quantity": 0,
        "weight": Weight(**{"unit": "", "value": 0.0}),
    }
    obj = BoxInput(**kwargs)
    assert isinstance(obj, BoxInput)


def test_weightrange_instantiates():
    """Instantiate WeightRange with dummy data"""
    kwargs = {
        "maximum": 0.0,
        "minimum": 0.0,
        "unit": "",
    }
    obj = WeightRange(**kwargs)
    assert isinstance(obj, WeightRange)


def test_boxrequirements_instantiates():
    """Instantiate BoxRequirements with dummy data"""
    kwargs = {
        "weight": WeightRange(**{"maximum": 0.0, "minimum": 0.0, "unit": ""}),
    }
    obj = BoxRequirements(**kwargs)
    assert isinstance(obj, BoxRequirements)


def test_boxupdateinput_instantiates():
    """Instantiate BoxUpdateInput with dummy data"""
    kwargs = {
        "content_information_source": "",
        "dimensions": Dimensions(
            **{"height": 0.0, "length": 0.0, "unit_of_measurement": "", "width": 0.0}
        ),
        "items": None,
        "package_id": None,
        "quantity": 0,
        "weight": Weight(**{"unit": "", "value": 0.0}),
    }
    obj = BoxUpdateInput(**kwargs)
    assert isinstance(obj, BoxUpdateInput)


def test_cancelinboundplanrequest_instantiates():
    """Instantiate CancelInboundPlanRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
    }
    obj = CancelInboundPlanRequest(**kwargs)
    assert isinstance(obj, CancelInboundPlanRequest)


def test_cancelinboundplanresponse_instantiates():
    """Instantiate CancelInboundPlanResponse with dummy data"""
    kwargs = {
        "operation_id": "",
    }
    obj = CancelInboundPlanResponse(**kwargs)
    assert isinstance(obj, CancelInboundPlanResponse)


def test_cancelselfshipappointmentrequestbody_instantiates():
    """Instantiate CancelSelfShipAppointmentRequestBody with dummy data"""
    kwargs = {
        "reason_comment": None,
    }
    obj = CancelSelfShipAppointmentRequestBody(**kwargs)
    assert isinstance(obj, CancelSelfShipAppointmentRequestBody)


def test_cancelselfshipappointmentrequest_instantiates():
    """Instantiate CancelSelfShipAppointmentRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "shipment_id": "",
        "body": CancelSelfShipAppointmentRequestBody(**{"reason_comment": None}),
    }
    obj = CancelSelfShipAppointmentRequest(**kwargs)
    assert isinstance(obj, CancelSelfShipAppointmentRequest)


def test_cancelselfshipappointmentresponse_instantiates():
    """Instantiate CancelSelfShipAppointmentResponse with dummy data"""
    kwargs = {
        "operation_id": "",
    }
    obj = CancelSelfShipAppointmentResponse(**kwargs)
    assert isinstance(obj, CancelSelfShipAppointmentResponse)


def test_carrier_instantiates():
    """Instantiate Carrier with dummy data"""
    kwargs = {
        "alpha_code": None,
        "name": None,
    }
    obj = Carrier(**kwargs)
    assert isinstance(obj, Carrier)


def test_carrierappointment_instantiates():
    """Instantiate CarrierAppointment with dummy data"""
    kwargs = {
        "end_time": datetime(2000, 1, 1),
        "start_time": datetime(2000, 1, 1),
    }
    obj = CarrierAppointment(**kwargs)
    assert isinstance(obj, CarrierAppointment)


def test_taxrate_instantiates():
    """Instantiate TaxRate with dummy data"""
    kwargs = {
        "cess_rate": None,
        "gst_rate": None,
        "tax_type": None,
    }
    obj = TaxRate(**kwargs)
    assert isinstance(obj, TaxRate)


def test_taxdetails_instantiates():
    """Instantiate TaxDetails with dummy data"""
    kwargs = {
        "declared_value": None,
        "hsn_code": None,
        "tax_rates": None,
    }
    obj = TaxDetails(**kwargs)
    assert isinstance(obj, TaxDetails)


def test_compliancedetail_instantiates():
    """Instantiate ComplianceDetail with dummy data"""
    kwargs = {
        "asin": None,
        "fnsku": None,
        "msku": None,
        "tax_details": None,
    }
    obj = ComplianceDetail(**kwargs)
    assert isinstance(obj, ComplianceDetail)


def test_confirmdeliverywindowoptionsrequest_instantiates():
    """Instantiate ConfirmDeliveryWindowOptionsRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "shipment_id": "",
        "delivery_window_option_id": "",
    }
    obj = ConfirmDeliveryWindowOptionsRequest(**kwargs)
    assert isinstance(obj, ConfirmDeliveryWindowOptionsRequest)


def test_confirmdeliverywindowoptionsresponse_instantiates():
    """Instantiate ConfirmDeliveryWindowOptionsResponse with dummy data"""
    kwargs = {
        "operation_id": "",
    }
    obj = ConfirmDeliveryWindowOptionsResponse(**kwargs)
    assert isinstance(obj, ConfirmDeliveryWindowOptionsResponse)


def test_confirmpackingoptionrequest_instantiates():
    """Instantiate ConfirmPackingOptionRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "packing_option_id": "",
    }
    obj = ConfirmPackingOptionRequest(**kwargs)
    assert isinstance(obj, ConfirmPackingOptionRequest)


def test_confirmpackingoptionresponse_instantiates():
    """Instantiate ConfirmPackingOptionResponse with dummy data"""
    kwargs = {
        "operation_id": "",
    }
    obj = ConfirmPackingOptionResponse(**kwargs)
    assert isinstance(obj, ConfirmPackingOptionResponse)


def test_confirmplacementoptionrequest_instantiates():
    """Instantiate ConfirmPlacementOptionRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "placement_option_id": "",
    }
    obj = ConfirmPlacementOptionRequest(**kwargs)
    assert isinstance(obj, ConfirmPlacementOptionRequest)


def test_confirmplacementoptionresponse_instantiates():
    """Instantiate ConfirmPlacementOptionResponse with dummy data"""
    kwargs = {
        "operation_id": "",
    }
    obj = ConfirmPlacementOptionResponse(**kwargs)
    assert isinstance(obj, ConfirmPlacementOptionResponse)


def test_confirmshipmentcontentupdatepreviewrequest_instantiates():
    """Instantiate ConfirmShipmentContentUpdatePreviewRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "shipment_id": "",
        "content_update_preview_id": "",
    }
    obj = ConfirmShipmentContentUpdatePreviewRequest(**kwargs)
    assert isinstance(obj, ConfirmShipmentContentUpdatePreviewRequest)


def test_confirmshipmentcontentupdatepreviewresponse_instantiates():
    """Instantiate ConfirmShipmentContentUpdatePreviewResponse with dummy data"""
    kwargs = {
        "operation_id": "",
    }
    obj = ConfirmShipmentContentUpdatePreviewResponse(**kwargs)
    assert isinstance(obj, ConfirmShipmentContentUpdatePreviewResponse)


def test_contactinformation_instantiates():
    """Instantiate ContactInformation with dummy data"""
    kwargs = {
        "email": None,
        "name": "",
        "phone_number": "",
    }
    obj = ContactInformation(**kwargs)
    assert isinstance(obj, ContactInformation)


def test_transportationselection_instantiates():
    """Instantiate TransportationSelection with dummy data"""
    kwargs = {
        "contact_information": None,
        "shipment_id": "",
        "transportation_option_id": "",
    }
    obj = TransportationSelection(**kwargs)
    assert isinstance(obj, TransportationSelection)


def test_confirmtransportationoptionsrequestbody_instantiates():
    """Instantiate ConfirmTransportationOptionsRequestBody with dummy data"""
    kwargs = {
        "transportation_selections": [],
    }
    obj = ConfirmTransportationOptionsRequestBody(**kwargs)
    assert isinstance(obj, ConfirmTransportationOptionsRequestBody)


def test_confirmtransportationoptionsrequest_instantiates():
    """Instantiate ConfirmTransportationOptionsRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "body": ConfirmTransportationOptionsRequestBody(
            **{"transportation_selections": []}
        ),
    }
    obj = ConfirmTransportationOptionsRequest(**kwargs)
    assert isinstance(obj, ConfirmTransportationOptionsRequest)


def test_confirmtransportationoptionsresponse_instantiates():
    """Instantiate ConfirmTransportationOptionsResponse with dummy data"""
    kwargs = {
        "operation_id": "",
    }
    obj = ConfirmTransportationOptionsResponse(**kwargs)
    assert isinstance(obj, ConfirmTransportationOptionsResponse)


def test_requestedupdates_instantiates():
    """Instantiate RequestedUpdates with dummy data"""
    kwargs = {
        "boxes": None,
        "items": None,
    }
    obj = RequestedUpdates(**kwargs)
    assert isinstance(obj, RequestedUpdates)


def test_quote_instantiates():
    """Instantiate Quote with dummy data"""
    kwargs = {
        "cost": Currency(**{"amount": 0.0, "code": ""}),
        "expiration": None,
        "voidable_until": None,
    }
    obj = Quote(**kwargs)
    assert isinstance(obj, Quote)


def test_transportationoption_instantiates():
    """Instantiate TransportationOption with dummy data"""
    kwargs = {
        "carrier": Carrier(**{"alpha_code": None, "name": None}),
        "carrier_appointment": None,
        "preconditions": [],
        "quote": None,
        "shipment_id": "",
        "shipping_mode": "",
        "shipping_solution": "",
        "transportation_option_id": "",
    }
    obj = TransportationOption(**kwargs)
    assert isinstance(obj, TransportationOption)


def test_contentupdatepreview_instantiates():
    """Instantiate ContentUpdatePreview with dummy data"""
    kwargs = {
        "content_update_preview_id": "",
        "expiration": datetime(2000, 1, 1),
        "requested_updates": RequestedUpdates(**{"boxes": None, "items": None}),
        "transportation_option": TransportationOption(
            **{
                "carrier": Carrier(**{"alpha_code": None, "name": None}),
                "carrier_appointment": None,
                "preconditions": [],
                "quote": None,
                "shipment_id": "",
                "shipping_mode": "",
                "shipping_solution": "",
                "transportation_option_id": "",
            }
        ),
    }
    obj = ContentUpdatePreview(**kwargs)
    assert isinstance(obj, ContentUpdatePreview)


def test_createinboundplanrequestbody_instantiates():
    """Instantiate CreateInboundPlanRequestBody with dummy data"""
    kwargs = {
        "destination_marketplaces": None,
        "items": [],
        "name": None,
        "source_address": AddressInput(
            **{
                "address_line1": "",
                "address_line2": None,
                "city": "",
                "company_name": None,
                "country_code": "",
                "email": None,
                "name": "",
                "phone_number": "",
                "postal_code": "",
                "state_or_province_code": None,
            }
        ),
    }
    obj = CreateInboundPlanRequestBody(**kwargs)
    assert isinstance(obj, CreateInboundPlanRequestBody)


def test_createinboundplanrequest_instantiates():
    """Instantiate CreateInboundPlanRequest with dummy data"""
    kwargs = {
        "body": CreateInboundPlanRequestBody(
            **{
                "destination_marketplaces": None,
                "items": [],
                "name": None,
                "source_address": AddressInput(
                    **{
                        "address_line1": "",
                        "address_line2": None,
                        "city": "",
                        "company_name": None,
                        "country_code": "",
                        "email": None,
                        "name": "",
                        "phone_number": "",
                        "postal_code": "",
                        "state_or_province_code": None,
                    }
                ),
            }
        ),
    }
    obj = CreateInboundPlanRequest(**kwargs)
    assert isinstance(obj, CreateInboundPlanRequest)


def test_createinboundplanresponse_instantiates():
    """Instantiate CreateInboundPlanResponse with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "operation_id": "",
    }
    obj = CreateInboundPlanResponse(**kwargs)
    assert isinstance(obj, CreateInboundPlanResponse)


def test_mskuquantity_instantiates():
    """Instantiate MskuQuantity with dummy data"""
    kwargs = {
        "msku": "",
        "quantity": 0,
    }
    obj = MskuQuantity(**kwargs)
    assert isinstance(obj, MskuQuantity)


def test_createmarketplaceitemlabelsrequestbody_instantiates():
    """Instantiate CreateMarketplaceItemLabelsRequestBody with dummy data"""
    kwargs = {
        "height": None,
        "label_type": "",
        "locale_code": None,
        "marketplace_id": None,
        "msku_quantities": [],
        "page_type": None,
        "width": None,
    }
    obj = CreateMarketplaceItemLabelsRequestBody(**kwargs)
    assert isinstance(obj, CreateMarketplaceItemLabelsRequestBody)


def test_createmarketplaceitemlabelsrequest_instantiates():
    """Instantiate CreateMarketplaceItemLabelsRequest with dummy data"""
    kwargs = {
        "body": CreateMarketplaceItemLabelsRequestBody(
            **{
                "height": None,
                "label_type": "",
                "locale_code": None,
                "marketplace_id": None,
                "msku_quantities": [],
                "page_type": None,
                "width": None,
            }
        ),
    }
    obj = CreateMarketplaceItemLabelsRequest(**kwargs)
    assert isinstance(obj, CreateMarketplaceItemLabelsRequest)


def test_documentdownload_instantiates():
    """Instantiate DocumentDownload with dummy data"""
    kwargs = {
        "download_type": "",
        "expiration": None,
        "uri": "",
    }
    obj = DocumentDownload(**kwargs)
    assert isinstance(obj, DocumentDownload)


def test_createmarketplaceitemlabelsresponse_instantiates():
    """Instantiate CreateMarketplaceItemLabelsResponse with dummy data"""
    kwargs = {
        "document_downloads": [],
    }
    obj = CreateMarketplaceItemLabelsResponse(**kwargs)
    assert isinstance(obj, CreateMarketplaceItemLabelsResponse)


def test_customplacementinput_instantiates():
    """Instantiate CustomPlacementInput with dummy data"""
    kwargs = {
        "items": [],
        "warehouse_id": "",
    }
    obj = CustomPlacementInput(**kwargs)
    assert isinstance(obj, CustomPlacementInput)


def test_window_instantiates():
    """Instantiate Window with dummy data"""
    kwargs = {
        "editable_until": None,
        "end": datetime(2000, 1, 1),
        "start": datetime(2000, 1, 1),
    }
    obj = Window(**kwargs)
    assert isinstance(obj, Window)


def test_dates_instantiates():
    """Instantiate Dates with dummy data"""
    kwargs = {
        "ready_to_ship_window": None,
    }
    obj = Dates(**kwargs)
    assert isinstance(obj, Dates)


def test_deliverywindowoption_instantiates():
    """Instantiate DeliveryWindowOption with dummy data"""
    kwargs = {
        "availability_type": "",
        "delivery_window_option_id": "",
        "end_date": datetime(2000, 1, 1),
        "start_date": datetime(2000, 1, 1),
        "valid_until": datetime(2000, 1, 1),
    }
    obj = DeliveryWindowOption(**kwargs)
    assert isinstance(obj, DeliveryWindowOption)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "details": None,
        "message": "",
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


def test_freightinformation_instantiates():
    """Instantiate FreightInformation with dummy data"""
    kwargs = {
        "declared_value": None,
        "freight_class": None,
    }
    obj = FreightInformation(**kwargs)
    assert isinstance(obj, FreightInformation)


def test_generatedeliverywindowoptionsrequest_instantiates():
    """Instantiate GenerateDeliveryWindowOptionsRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "shipment_id": "",
    }
    obj = GenerateDeliveryWindowOptionsRequest(**kwargs)
    assert isinstance(obj, GenerateDeliveryWindowOptionsRequest)


def test_generatedeliverywindowoptionsresponse_instantiates():
    """Instantiate GenerateDeliveryWindowOptionsResponse with dummy data"""
    kwargs = {
        "operation_id": "",
    }
    obj = GenerateDeliveryWindowOptionsResponse(**kwargs)
    assert isinstance(obj, GenerateDeliveryWindowOptionsResponse)


def test_generatepackingoptionsrequest_instantiates():
    """Instantiate GeneratePackingOptionsRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
    }
    obj = GeneratePackingOptionsRequest(**kwargs)
    assert isinstance(obj, GeneratePackingOptionsRequest)


def test_generatepackingoptionsresponse_instantiates():
    """Instantiate GeneratePackingOptionsResponse with dummy data"""
    kwargs = {
        "operation_id": "",
    }
    obj = GeneratePackingOptionsResponse(**kwargs)
    assert isinstance(obj, GeneratePackingOptionsResponse)


def test_generateplacementoptionsrequestbody_instantiates():
    """Instantiate GeneratePlacementOptionsRequestBody with dummy data"""
    kwargs = {
        "custom_placement": None,
    }
    obj = GeneratePlacementOptionsRequestBody(**kwargs)
    assert isinstance(obj, GeneratePlacementOptionsRequestBody)


def test_generateplacementoptionsrequest_instantiates():
    """Instantiate GeneratePlacementOptionsRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "body": GeneratePlacementOptionsRequestBody(**{"custom_placement": None}),
    }
    obj = GeneratePlacementOptionsRequest(**kwargs)
    assert isinstance(obj, GeneratePlacementOptionsRequest)


def test_generateplacementoptionsresponse_instantiates():
    """Instantiate GeneratePlacementOptionsResponse with dummy data"""
    kwargs = {
        "operation_id": "",
    }
    obj = GeneratePlacementOptionsResponse(**kwargs)
    assert isinstance(obj, GeneratePlacementOptionsResponse)


def test_generateselfshipappointmentslotsrequestbody_instantiates():
    """Instantiate GenerateSelfShipAppointmentSlotsRequestBody with dummy data"""
    kwargs = {
        "desired_end_date": None,
        "desired_start_date": None,
    }
    obj = GenerateSelfShipAppointmentSlotsRequestBody(**kwargs)
    assert isinstance(obj, GenerateSelfShipAppointmentSlotsRequestBody)


def test_generateselfshipappointmentslotsrequest_instantiates():
    """Instantiate GenerateSelfShipAppointmentSlotsRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "shipment_id": "",
        "body": GenerateSelfShipAppointmentSlotsRequestBody(
            **{"desired_end_date": None, "desired_start_date": None}
        ),
    }
    obj = GenerateSelfShipAppointmentSlotsRequest(**kwargs)
    assert isinstance(obj, GenerateSelfShipAppointmentSlotsRequest)


def test_generateselfshipappointmentslotsresponse_instantiates():
    """Instantiate GenerateSelfShipAppointmentSlotsResponse with dummy data"""
    kwargs = {
        "operation_id": "",
    }
    obj = GenerateSelfShipAppointmentSlotsResponse(**kwargs)
    assert isinstance(obj, GenerateSelfShipAppointmentSlotsResponse)


def test_generateshipmentcontentupdatepreviewsrequestbody_instantiates():
    """Instantiate GenerateShipmentContentUpdatePreviewsRequestBody with dummy data"""
    kwargs = {
        "boxes": [],
        "items": [],
    }
    obj = GenerateShipmentContentUpdatePreviewsRequestBody(**kwargs)
    assert isinstance(obj, GenerateShipmentContentUpdatePreviewsRequestBody)


def test_generateshipmentcontentupdatepreviewsrequest_instantiates():
    """Instantiate GenerateShipmentContentUpdatePreviewsRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "shipment_id": "",
        "body": GenerateShipmentContentUpdatePreviewsRequestBody(
            **{"boxes": [], "items": []}
        ),
    }
    obj = GenerateShipmentContentUpdatePreviewsRequest(**kwargs)
    assert isinstance(obj, GenerateShipmentContentUpdatePreviewsRequest)


def test_generateshipmentcontentupdatepreviewsresponse_instantiates():
    """Instantiate GenerateShipmentContentUpdatePreviewsResponse with dummy data"""
    kwargs = {
        "operation_id": "",
    }
    obj = GenerateShipmentContentUpdatePreviewsResponse(**kwargs)
    assert isinstance(obj, GenerateShipmentContentUpdatePreviewsResponse)


def test_palletinput_instantiates():
    """Instantiate PalletInput with dummy data"""
    kwargs = {
        "dimensions": None,
        "quantity": 0,
        "stackability": None,
        "weight": None,
    }
    obj = PalletInput(**kwargs)
    assert isinstance(obj, PalletInput)


def test_windowinput_instantiates():
    """Instantiate WindowInput with dummy data"""
    kwargs = {
        "start": datetime(2000, 1, 1),
    }
    obj = WindowInput(**kwargs)
    assert isinstance(obj, WindowInput)


def test_shipmenttransportationconfiguration_instantiates():
    """Instantiate ShipmentTransportationConfiguration with dummy data"""
    kwargs = {
        "contact_information": None,
        "freight_information": None,
        "pallets": None,
        "ready_to_ship_window": WindowInput(**{"start": datetime(2000, 1, 1)}),
        "shipment_id": "",
    }
    obj = ShipmentTransportationConfiguration(**kwargs)
    assert isinstance(obj, ShipmentTransportationConfiguration)


def test_generatetransportationoptionsrequestbody_instantiates():
    """Instantiate GenerateTransportationOptionsRequestBody with dummy data"""
    kwargs = {
        "placement_option_id": "",
        "shipment_transportation_configurations": [],
    }
    obj = GenerateTransportationOptionsRequestBody(**kwargs)
    assert isinstance(obj, GenerateTransportationOptionsRequestBody)


def test_generatetransportationoptionsrequest_instantiates():
    """Instantiate GenerateTransportationOptionsRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "body": GenerateTransportationOptionsRequestBody(
            **{"placement_option_id": "", "shipment_transportation_configurations": []}
        ),
    }
    obj = GenerateTransportationOptionsRequest(**kwargs)
    assert isinstance(obj, GenerateTransportationOptionsRequest)


def test_generatetransportationoptionsresponse_instantiates():
    """Instantiate GenerateTransportationOptionsResponse with dummy data"""
    kwargs = {
        "operation_id": "",
    }
    obj = GenerateTransportationOptionsResponse(**kwargs)
    assert isinstance(obj, GenerateTransportationOptionsResponse)


def test_getdeliverychallandocumentrequest_instantiates():
    """Instantiate GetDeliveryChallanDocumentRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "shipment_id": "",
    }
    obj = GetDeliveryChallanDocumentRequest(**kwargs)
    assert isinstance(obj, GetDeliveryChallanDocumentRequest)


def test_getdeliverychallandocumentresponse_instantiates():
    """Instantiate GetDeliveryChallanDocumentResponse with dummy data"""
    kwargs = {
        "document_download": DocumentDownload(
            **{"download_type": "", "expiration": None, "uri": ""}
        ),
    }
    obj = GetDeliveryChallanDocumentResponse(**kwargs)
    assert isinstance(obj, GetDeliveryChallanDocumentResponse)


def test_getinboundoperationstatusrequest_instantiates():
    """Instantiate GetInboundOperationStatusRequest with dummy data"""
    kwargs = {
        "operation_id": "",
    }
    obj = GetInboundOperationStatusRequest(**kwargs)
    assert isinstance(obj, GetInboundOperationStatusRequest)


def test_getinboundplanrequest_instantiates():
    """Instantiate GetInboundPlanRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
    }
    obj = GetInboundPlanRequest(**kwargs)
    assert isinstance(obj, GetInboundPlanRequest)


def test_getselfshipappointmentslotsrequest_instantiates():
    """Instantiate GetSelfShipAppointmentSlotsRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "shipment_id": "",
        "page_size": None,
        "pagination_token": None,
    }
    obj = GetSelfShipAppointmentSlotsRequest(**kwargs)
    assert isinstance(obj, GetSelfShipAppointmentSlotsRequest)


def test_pagination_instantiates():
    """Instantiate Pagination with dummy data"""
    kwargs = {
        "next_token": None,
    }
    obj = Pagination(**kwargs)
    assert isinstance(obj, Pagination)


def test_selfshipappointmentslotsavailability_instantiates():
    """Instantiate SelfShipAppointmentSlotsAvailability with dummy data"""
    kwargs = {
        "expires_at": None,
        "slots": None,
    }
    obj = SelfShipAppointmentSlotsAvailability(**kwargs)
    assert isinstance(obj, SelfShipAppointmentSlotsAvailability)


def test_getselfshipappointmentslotsresponse_instantiates():
    """Instantiate GetSelfShipAppointmentSlotsResponse with dummy data"""
    kwargs = {
        "pagination": None,
        "self_ship_appointment_slots_availability": SelfShipAppointmentSlotsAvailability(
            **{"expires_at": None, "slots": None}
        ),
    }
    obj = GetSelfShipAppointmentSlotsResponse(**kwargs)
    assert isinstance(obj, GetSelfShipAppointmentSlotsResponse)


def test_getshipmentcontentupdatepreviewrequest_instantiates():
    """Instantiate GetShipmentContentUpdatePreviewRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "shipment_id": "",
        "content_update_preview_id": "",
    }
    obj = GetShipmentContentUpdatePreviewRequest(**kwargs)
    assert isinstance(obj, GetShipmentContentUpdatePreviewRequest)


def test_getshipmentrequest_instantiates():
    """Instantiate GetShipmentRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "shipment_id": "",
    }
    obj = GetShipmentRequest(**kwargs)
    assert isinstance(obj, GetShipmentRequest)


def test_operationproblem_instantiates():
    """Instantiate OperationProblem with dummy data"""
    kwargs = {
        "code": "",
        "details": None,
        "message": "",
        "severity": "",
    }
    obj = OperationProblem(**kwargs)
    assert isinstance(obj, OperationProblem)


def test_inboundoperationstatus_instantiates():
    """Instantiate InboundOperationStatus with dummy data"""
    kwargs = {
        "operation": "",
        "operation_id": "",
        "operation_problems": [],
        "operation_status": "",
    }
    obj = InboundOperationStatus(**kwargs)
    assert isinstance(obj, InboundOperationStatus)


def test_packingoptionsummary_instantiates():
    """Instantiate PackingOptionSummary with dummy data"""
    kwargs = {
        "packing_option_id": "",
        "status": "",
    }
    obj = PackingOptionSummary(**kwargs)
    assert isinstance(obj, PackingOptionSummary)


def test_placementoptionsummary_instantiates():
    """Instantiate PlacementOptionSummary with dummy data"""
    kwargs = {
        "placement_option_id": "",
        "status": "",
    }
    obj = PlacementOptionSummary(**kwargs)
    assert isinstance(obj, PlacementOptionSummary)


def test_shipmentsummary_instantiates():
    """Instantiate ShipmentSummary with dummy data"""
    kwargs = {
        "shipment_id": "",
        "status": "",
    }
    obj = ShipmentSummary(**kwargs)
    assert isinstance(obj, ShipmentSummary)


def test_inboundplan_instantiates():
    """Instantiate InboundPlan with dummy data"""
    kwargs = {
        "created_at": datetime(2000, 1, 1),
        "inbound_plan_id": "",
        "last_updated_at": datetime(2000, 1, 1),
        "marketplace_ids": None,
        "name": "",
        "packing_options": None,
        "placement_options": None,
        "shipments": None,
        "source_address": Address(
            **{
                "address_line1": "",
                "address_line2": None,
                "city": "",
                "company_name": None,
                "country_code": "",
                "email": None,
                "name": "",
                "phone_number": None,
                "postal_code": "",
                "state_or_province_code": None,
            }
        ),
        "status": "",
    }
    obj = InboundPlan(**kwargs)
    assert isinstance(obj, InboundPlan)


def test_inboundplansummary_instantiates():
    """Instantiate InboundPlanSummary with dummy data"""
    kwargs = {
        "created_at": datetime(2000, 1, 1),
        "inbound_plan_id": "",
        "last_updated_at": datetime(2000, 1, 1),
        "marketplace_ids": None,
        "name": "",
        "source_address": Address(
            **{
                "address_line1": "",
                "address_line2": None,
                "city": "",
                "company_name": None,
                "country_code": "",
                "email": None,
                "name": "",
                "phone_number": None,
                "postal_code": "",
                "state_or_province_code": None,
            }
        ),
        "status": "",
    }
    obj = InboundPlanSummary(**kwargs)
    assert isinstance(obj, InboundPlanSummary)


def test_incentive_instantiates():
    """Instantiate Incentive with dummy data"""
    kwargs = {
        "description": "",
        "target": "",
        "type": "",
        "value": Currency(**{"amount": 0.0, "code": ""}),
    }
    obj = Incentive(**kwargs)
    assert isinstance(obj, Incentive)


def test_listdeliverywindowoptionsrequest_instantiates():
    """Instantiate ListDeliveryWindowOptionsRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "shipment_id": "",
        "page_size": None,
        "pagination_token": None,
    }
    obj = ListDeliveryWindowOptionsRequest(**kwargs)
    assert isinstance(obj, ListDeliveryWindowOptionsRequest)


def test_listdeliverywindowoptionsresponse_instantiates():
    """Instantiate ListDeliveryWindowOptionsResponse with dummy data"""
    kwargs = {
        "delivery_window_options": [],
        "pagination": None,
    }
    obj = ListDeliveryWindowOptionsResponse(**kwargs)
    assert isinstance(obj, ListDeliveryWindowOptionsResponse)


def test_listinboundplanboxesrequest_instantiates():
    """Instantiate ListInboundPlanBoxesRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "page_size": None,
        "pagination_token": None,
    }
    obj = ListInboundPlanBoxesRequest(**kwargs)
    assert isinstance(obj, ListInboundPlanBoxesRequest)


def test_listinboundplanboxesresponse_instantiates():
    """Instantiate ListInboundPlanBoxesResponse with dummy data"""
    kwargs = {
        "boxes": [],
        "pagination": None,
    }
    obj = ListInboundPlanBoxesResponse(**kwargs)
    assert isinstance(obj, ListInboundPlanBoxesResponse)


def test_listinboundplanitemsrequest_instantiates():
    """Instantiate ListInboundPlanItemsRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "page_size": None,
        "pagination_token": None,
    }
    obj = ListInboundPlanItemsRequest(**kwargs)
    assert isinstance(obj, ListInboundPlanItemsRequest)


def test_listinboundplanitemsresponse_instantiates():
    """Instantiate ListInboundPlanItemsResponse with dummy data"""
    kwargs = {
        "items": [],
        "pagination": None,
    }
    obj = ListInboundPlanItemsResponse(**kwargs)
    assert isinstance(obj, ListInboundPlanItemsResponse)


def test_listinboundplanpalletsrequest_instantiates():
    """Instantiate ListInboundPlanPalletsRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "page_size": None,
        "pagination_token": None,
    }
    obj = ListInboundPlanPalletsRequest(**kwargs)
    assert isinstance(obj, ListInboundPlanPalletsRequest)


def test_pallet_instantiates():
    """Instantiate Pallet with dummy data"""
    kwargs = {
        "dimensions": None,
        "package_id": "",
        "quantity": None,
        "stackability": None,
        "weight": None,
    }
    obj = Pallet(**kwargs)
    assert isinstance(obj, Pallet)


def test_listinboundplanpalletsresponse_instantiates():
    """Instantiate ListInboundPlanPalletsResponse with dummy data"""
    kwargs = {
        "pagination": None,
        "pallets": [],
    }
    obj = ListInboundPlanPalletsResponse(**kwargs)
    assert isinstance(obj, ListInboundPlanPalletsResponse)


def test_listinboundplansrequest_instantiates():
    """Instantiate ListInboundPlansRequest with dummy data"""
    kwargs = {
        "page_size": None,
        "pagination_token": None,
        "status": None,
        "sort_by": None,
        "sort_order": None,
    }
    obj = ListInboundPlansRequest(**kwargs)
    assert isinstance(obj, ListInboundPlansRequest)


def test_listinboundplansresponse_instantiates():
    """Instantiate ListInboundPlansResponse with dummy data"""
    kwargs = {
        "inbound_plans": None,
        "pagination": None,
    }
    obj = ListInboundPlansResponse(**kwargs)
    assert isinstance(obj, ListInboundPlansResponse)


def test_listitemcompliancedetailsrequest_instantiates():
    """Instantiate ListItemComplianceDetailsRequest with dummy data"""
    kwargs = {
        "mskus": [],
        "marketplace_id": None,
    }
    obj = ListItemComplianceDetailsRequest(**kwargs)
    assert isinstance(obj, ListItemComplianceDetailsRequest)


def test_listitemcompliancedetailsresponse_instantiates():
    """Instantiate ListItemComplianceDetailsResponse with dummy data"""
    kwargs = {
        "compliance_details": None,
    }
    obj = ListItemComplianceDetailsResponse(**kwargs)
    assert isinstance(obj, ListItemComplianceDetailsResponse)


def test_listpackinggroupboxesrequest_instantiates():
    """Instantiate ListPackingGroupBoxesRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "packing_group_id": "",
        "page_size": None,
        "pagination_token": None,
    }
    obj = ListPackingGroupBoxesRequest(**kwargs)
    assert isinstance(obj, ListPackingGroupBoxesRequest)


def test_listpackinggroupboxesresponse_instantiates():
    """Instantiate ListPackingGroupBoxesResponse with dummy data"""
    kwargs = {
        "boxes": [],
        "pagination": None,
    }
    obj = ListPackingGroupBoxesResponse(**kwargs)
    assert isinstance(obj, ListPackingGroupBoxesResponse)


def test_listpackinggroupitemsrequest_instantiates():
    """Instantiate ListPackingGroupItemsRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "packing_group_id": "",
        "page_size": None,
        "pagination_token": None,
    }
    obj = ListPackingGroupItemsRequest(**kwargs)
    assert isinstance(obj, ListPackingGroupItemsRequest)


def test_listpackinggroupitemsresponse_instantiates():
    """Instantiate ListPackingGroupItemsResponse with dummy data"""
    kwargs = {
        "items": [],
        "pagination": None,
    }
    obj = ListPackingGroupItemsResponse(**kwargs)
    assert isinstance(obj, ListPackingGroupItemsResponse)


def test_listpackingoptionsrequest_instantiates():
    """Instantiate ListPackingOptionsRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "page_size": None,
        "pagination_token": None,
    }
    obj = ListPackingOptionsRequest(**kwargs)
    assert isinstance(obj, ListPackingOptionsRequest)


def test_shippingrequirements_instantiates():
    """Instantiate ShippingRequirements with dummy data"""
    kwargs = {
        "modes": [],
        "solution": "",
    }
    obj = ShippingRequirements(**kwargs)
    assert isinstance(obj, ShippingRequirements)


def test_packingconfiguration_instantiates():
    """Instantiate PackingConfiguration with dummy data"""
    kwargs = {
        "box_packing_methods": None,
        "box_requirements": None,
        "shipping_requirements": None,
    }
    obj = PackingConfiguration(**kwargs)
    assert isinstance(obj, PackingConfiguration)


def test_shippingconfiguration_instantiates():
    """Instantiate ShippingConfiguration with dummy data"""
    kwargs = {
        "shipping_mode": None,
        "shipping_solution": None,
    }
    obj = ShippingConfiguration(**kwargs)
    assert isinstance(obj, ShippingConfiguration)


def test_packingoption_instantiates():
    """Instantiate PackingOption with dummy data"""
    kwargs = {
        "discounts": [],
        "expiration": None,
        "fees": [],
        "packing_groups": [],
        "packing_option_id": "",
        "status": "",
        "supported_configurations": [],
        "supported_shipping_configurations": [],
    }
    obj = PackingOption(**kwargs)
    assert isinstance(obj, PackingOption)


def test_listpackingoptionsresponse_instantiates():
    """Instantiate ListPackingOptionsResponse with dummy data"""
    kwargs = {
        "packing_options": [],
        "pagination": None,
    }
    obj = ListPackingOptionsResponse(**kwargs)
    assert isinstance(obj, ListPackingOptionsResponse)


def test_listplacementoptionsrequest_instantiates():
    """Instantiate ListPlacementOptionsRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "page_size": None,
        "pagination_token": None,
    }
    obj = ListPlacementOptionsRequest(**kwargs)
    assert isinstance(obj, ListPlacementOptionsRequest)


def test_placementoption_instantiates():
    """Instantiate PlacementOption with dummy data"""
    kwargs = {
        "discounts": [],
        "expiration": None,
        "fees": [],
        "placement_option_id": "",
        "shipment_ids": [],
        "status": "",
    }
    obj = PlacementOption(**kwargs)
    assert isinstance(obj, PlacementOption)


def test_listplacementoptionsresponse_instantiates():
    """Instantiate ListPlacementOptionsResponse with dummy data"""
    kwargs = {
        "pagination": None,
        "placement_options": [],
    }
    obj = ListPlacementOptionsResponse(**kwargs)
    assert isinstance(obj, ListPlacementOptionsResponse)


def test_listprepdetailsrequest_instantiates():
    """Instantiate ListPrepDetailsRequest with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "mskus": [],
    }
    obj = ListPrepDetailsRequest(**kwargs)
    assert isinstance(obj, ListPrepDetailsRequest)


def test_mskuprepdetail_instantiates():
    """Instantiate MskuPrepDetail with dummy data"""
    kwargs = {
        "all_owners_constraint": None,
        "label_owner_constraint": None,
        "msku": "",
        "prep_category": "",
        "prep_owner_constraint": None,
        "prep_types": [],
    }
    obj = MskuPrepDetail(**kwargs)
    assert isinstance(obj, MskuPrepDetail)


def test_listprepdetailsresponse_instantiates():
    """Instantiate ListPrepDetailsResponse with dummy data"""
    kwargs = {
        "msku_prep_details": [],
    }
    obj = ListPrepDetailsResponse(**kwargs)
    assert isinstance(obj, ListPrepDetailsResponse)


def test_listshipmentboxesrequest_instantiates():
    """Instantiate ListShipmentBoxesRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "shipment_id": "",
        "page_size": None,
        "pagination_token": None,
    }
    obj = ListShipmentBoxesRequest(**kwargs)
    assert isinstance(obj, ListShipmentBoxesRequest)


def test_listshipmentboxesresponse_instantiates():
    """Instantiate ListShipmentBoxesResponse with dummy data"""
    kwargs = {
        "boxes": [],
        "pagination": None,
    }
    obj = ListShipmentBoxesResponse(**kwargs)
    assert isinstance(obj, ListShipmentBoxesResponse)


def test_listshipmentcontentupdatepreviewsrequest_instantiates():
    """Instantiate ListShipmentContentUpdatePreviewsRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "shipment_id": "",
        "page_size": None,
        "pagination_token": None,
    }
    obj = ListShipmentContentUpdatePreviewsRequest(**kwargs)
    assert isinstance(obj, ListShipmentContentUpdatePreviewsRequest)


def test_listshipmentcontentupdatepreviewsresponse_instantiates():
    """Instantiate ListShipmentContentUpdatePreviewsResponse with dummy data"""
    kwargs = {
        "content_update_previews": [],
        "pagination": None,
    }
    obj = ListShipmentContentUpdatePreviewsResponse(**kwargs)
    assert isinstance(obj, ListShipmentContentUpdatePreviewsResponse)


def test_listshipmentitemsrequest_instantiates():
    """Instantiate ListShipmentItemsRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "shipment_id": "",
        "page_size": None,
        "pagination_token": None,
    }
    obj = ListShipmentItemsRequest(**kwargs)
    assert isinstance(obj, ListShipmentItemsRequest)


def test_listshipmentitemsresponse_instantiates():
    """Instantiate ListShipmentItemsResponse with dummy data"""
    kwargs = {
        "items": [],
        "pagination": None,
    }
    obj = ListShipmentItemsResponse(**kwargs)
    assert isinstance(obj, ListShipmentItemsResponse)


def test_listshipmentpalletsrequest_instantiates():
    """Instantiate ListShipmentPalletsRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "shipment_id": "",
        "page_size": None,
        "pagination_token": None,
    }
    obj = ListShipmentPalletsRequest(**kwargs)
    assert isinstance(obj, ListShipmentPalletsRequest)


def test_listshipmentpalletsresponse_instantiates():
    """Instantiate ListShipmentPalletsResponse with dummy data"""
    kwargs = {
        "pagination": None,
        "pallets": [],
    }
    obj = ListShipmentPalletsResponse(**kwargs)
    assert isinstance(obj, ListShipmentPalletsResponse)


def test_listtransportationoptionsrequest_instantiates():
    """Instantiate ListTransportationOptionsRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "page_size": None,
        "pagination_token": None,
        "placement_option_id": None,
        "shipment_id": None,
    }
    obj = ListTransportationOptionsRequest(**kwargs)
    assert isinstance(obj, ListTransportationOptionsRequest)


def test_listtransportationoptionsresponse_instantiates():
    """Instantiate ListTransportationOptionsResponse with dummy data"""
    kwargs = {
        "pagination": None,
        "transportation_options": [],
    }
    obj = ListTransportationOptionsResponse(**kwargs)
    assert isinstance(obj, ListTransportationOptionsResponse)


def test_ltltrackingdetail_instantiates():
    """Instantiate LtlTrackingDetail with dummy data"""
    kwargs = {
        "bill_of_lading_number": None,
        "freight_bill_number": None,
    }
    obj = LtlTrackingDetail(**kwargs)
    assert isinstance(obj, LtlTrackingDetail)


def test_ltltrackingdetailinput_instantiates():
    """Instantiate LtlTrackingDetailInput with dummy data"""
    kwargs = {
        "bill_of_lading_number": None,
        "freight_bill_number": [],
    }
    obj = LtlTrackingDetailInput(**kwargs)
    assert isinstance(obj, LtlTrackingDetailInput)


def test_mskuprepdetailinput_instantiates():
    """Instantiate MskuPrepDetailInput with dummy data"""
    kwargs = {
        "msku": "",
        "prep_category": "",
        "prep_types": [],
    }
    obj = MskuPrepDetailInput(**kwargs)
    assert isinstance(obj, MskuPrepDetailInput)


def test_packagegroupinginput_instantiates():
    """Instantiate PackageGroupingInput with dummy data"""
    kwargs = {
        "boxes": [],
        "packing_group_id": None,
        "shipment_id": None,
    }
    obj = PackageGroupingInput(**kwargs)
    assert isinstance(obj, PackageGroupingInput)


def test_scheduleselfshipappointmentrequestbody_instantiates():
    """Instantiate ScheduleSelfShipAppointmentRequestBody with dummy data"""
    kwargs = {
        "reason_comment": None,
    }
    obj = ScheduleSelfShipAppointmentRequestBody(**kwargs)
    assert isinstance(obj, ScheduleSelfShipAppointmentRequestBody)


def test_scheduleselfshipappointmentrequest_instantiates():
    """Instantiate ScheduleSelfShipAppointmentRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "shipment_id": "",
        "slot_id": "",
        "body": ScheduleSelfShipAppointmentRequestBody(**{"reason_comment": None}),
    }
    obj = ScheduleSelfShipAppointmentRequest(**kwargs)
    assert isinstance(obj, ScheduleSelfShipAppointmentRequest)


def test_selfshipappointmentdetails_instantiates():
    """Instantiate SelfShipAppointmentDetails with dummy data"""
    kwargs = {
        "appointment_id": None,
        "appointment_slot_time": None,
        "appointment_status": None,
    }
    obj = SelfShipAppointmentDetails(**kwargs)
    assert isinstance(obj, SelfShipAppointmentDetails)


def test_scheduleselfshipappointmentresponse_instantiates():
    """Instantiate ScheduleSelfShipAppointmentResponse with dummy data"""
    kwargs = {
        "self_ship_appointment_details": SelfShipAppointmentDetails(
            **{
                "appointment_id": None,
                "appointment_slot_time": None,
                "appointment_status": None,
            }
        ),
    }
    obj = ScheduleSelfShipAppointmentResponse(**kwargs)
    assert isinstance(obj, ScheduleSelfShipAppointmentResponse)


def test_selecteddeliverywindow_instantiates():
    """Instantiate SelectedDeliveryWindow with dummy data"""
    kwargs = {
        "availability_type": "",
        "delivery_window_option_id": "",
        "editable_until": None,
        "end_date": datetime(2000, 1, 1),
        "start_date": datetime(2000, 1, 1),
    }
    obj = SelectedDeliveryWindow(**kwargs)
    assert isinstance(obj, SelectedDeliveryWindow)


def test_setpackinginformationrequestbody_instantiates():
    """Instantiate SetPackingInformationRequestBody with dummy data"""
    kwargs = {
        "package_groupings": [],
    }
    obj = SetPackingInformationRequestBody(**kwargs)
    assert isinstance(obj, SetPackingInformationRequestBody)


def test_setpackinginformationrequest_instantiates():
    """Instantiate SetPackingInformationRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "body": SetPackingInformationRequestBody(**{"package_groupings": []}),
    }
    obj = SetPackingInformationRequest(**kwargs)
    assert isinstance(obj, SetPackingInformationRequest)


def test_setpackinginformationresponse_instantiates():
    """Instantiate SetPackingInformationResponse with dummy data"""
    kwargs = {
        "operation_id": "",
    }
    obj = SetPackingInformationResponse(**kwargs)
    assert isinstance(obj, SetPackingInformationResponse)


def test_setprepdetailsrequestbody_instantiates():
    """Instantiate SetPrepDetailsRequestBody with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "msku_prep_details": [],
    }
    obj = SetPrepDetailsRequestBody(**kwargs)
    assert isinstance(obj, SetPrepDetailsRequestBody)


def test_setprepdetailsrequest_instantiates():
    """Instantiate SetPrepDetailsRequest with dummy data"""
    kwargs = {
        "body": SetPrepDetailsRequestBody(
            **{"marketplace_id": None, "msku_prep_details": []}
        ),
    }
    obj = SetPrepDetailsRequest(**kwargs)
    assert isinstance(obj, SetPrepDetailsRequest)


def test_setprepdetailsresponse_instantiates():
    """Instantiate SetPrepDetailsResponse with dummy data"""
    kwargs = {
        "operation_id": "",
    }
    obj = SetPrepDetailsResponse(**kwargs)
    assert isinstance(obj, SetPrepDetailsResponse)


def test_shipmentdestination_instantiates():
    """Instantiate ShipmentDestination with dummy data"""
    kwargs = {
        "address": None,
        "destination_type": "",
        "warehouse_id": None,
    }
    obj = ShipmentDestination(**kwargs)
    assert isinstance(obj, ShipmentDestination)


def test_shipmentsource_instantiates():
    """Instantiate ShipmentSource with dummy data"""
    kwargs = {
        "address": None,
        "source_type": "",
    }
    obj = ShipmentSource(**kwargs)
    assert isinstance(obj, ShipmentSource)


def test_spdtrackingitem_instantiates():
    """Instantiate SpdTrackingItem with dummy data"""
    kwargs = {
        "box_id": None,
        "tracking_id": None,
        "tracking_number_validation_status": None,
    }
    obj = SpdTrackingItem(**kwargs)
    assert isinstance(obj, SpdTrackingItem)


def test_spdtrackingdetail_instantiates():
    """Instantiate SpdTrackingDetail with dummy data"""
    kwargs = {
        "spd_tracking_items": None,
    }
    obj = SpdTrackingDetail(**kwargs)
    assert isinstance(obj, SpdTrackingDetail)


def test_trackingdetails_instantiates():
    """Instantiate TrackingDetails with dummy data"""
    kwargs = {
        "ltl_tracking_detail": None,
        "spd_tracking_detail": None,
    }
    obj = TrackingDetails(**kwargs)
    assert isinstance(obj, TrackingDetails)


def test_shipment_instantiates():
    """Instantiate Shipment with dummy data"""
    kwargs = {
        "amazon_reference_id": None,
        "contact_information": None,
        "dates": None,
        "destination": ShipmentDestination(
            **{"address": None, "destination_type": "", "warehouse_id": None}
        ),
        "freight_information": None,
        "name": None,
        "placement_option_id": "",
        "selected_delivery_window": None,
        "selected_transportation_option_id": None,
        "self_ship_appointment_details": None,
        "shipment_confirmation_id": None,
        "shipment_id": "",
        "source": ShipmentSource(**{"address": None, "source_type": ""}),
        "status": None,
        "tracking_details": None,
    }
    obj = Shipment(**kwargs)
    assert isinstance(obj, Shipment)


def test_spdtrackingiteminput_instantiates():
    """Instantiate SpdTrackingItemInput with dummy data"""
    kwargs = {
        "box_id": "",
        "tracking_id": "",
    }
    obj = SpdTrackingItemInput(**kwargs)
    assert isinstance(obj, SpdTrackingItemInput)


def test_spdtrackingdetailinput_instantiates():
    """Instantiate SpdTrackingDetailInput with dummy data"""
    kwargs = {
        "spd_tracking_items": [],
    }
    obj = SpdTrackingDetailInput(**kwargs)
    assert isinstance(obj, SpdTrackingDetailInput)


def test_trackingdetailsinput_instantiates():
    """Instantiate TrackingDetailsInput with dummy data"""
    kwargs = {
        "ltl_tracking_detail": None,
        "spd_tracking_detail": None,
    }
    obj = TrackingDetailsInput(**kwargs)
    assert isinstance(obj, TrackingDetailsInput)


def test_updateinboundplannamerequestbody_instantiates():
    """Instantiate UpdateInboundPlanNameRequestBody with dummy data"""
    kwargs = {
        "name": "",
    }
    obj = UpdateInboundPlanNameRequestBody(**kwargs)
    assert isinstance(obj, UpdateInboundPlanNameRequestBody)


def test_updateinboundplannamerequest_instantiates():
    """Instantiate UpdateInboundPlanNameRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "body": UpdateInboundPlanNameRequestBody(**{"name": ""}),
    }
    obj = UpdateInboundPlanNameRequest(**kwargs)
    assert isinstance(obj, UpdateInboundPlanNameRequest)


def test_updateitemcompliancedetailsrequestbody_instantiates():
    """Instantiate UpdateItemComplianceDetailsRequestBody with dummy data"""
    kwargs = {
        "msku": "",
        "tax_details": TaxDetails(
            **{"declared_value": None, "hsn_code": None, "tax_rates": None}
        ),
    }
    obj = UpdateItemComplianceDetailsRequestBody(**kwargs)
    assert isinstance(obj, UpdateItemComplianceDetailsRequestBody)


def test_updateitemcompliancedetailsrequest_instantiates():
    """Instantiate UpdateItemComplianceDetailsRequest with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "body": UpdateItemComplianceDetailsRequestBody(
            **{
                "msku": "",
                "tax_details": TaxDetails(
                    **{"declared_value": None, "hsn_code": None, "tax_rates": None}
                ),
            }
        ),
    }
    obj = UpdateItemComplianceDetailsRequest(**kwargs)
    assert isinstance(obj, UpdateItemComplianceDetailsRequest)


def test_updateitemcompliancedetailsresponse_instantiates():
    """Instantiate UpdateItemComplianceDetailsResponse with dummy data"""
    kwargs = {
        "operation_id": "",
    }
    obj = UpdateItemComplianceDetailsResponse(**kwargs)
    assert isinstance(obj, UpdateItemComplianceDetailsResponse)


def test_updateshipmentnamerequestbody_instantiates():
    """Instantiate UpdateShipmentNameRequestBody with dummy data"""
    kwargs = {
        "name": "",
    }
    obj = UpdateShipmentNameRequestBody(**kwargs)
    assert isinstance(obj, UpdateShipmentNameRequestBody)


def test_updateshipmentnamerequest_instantiates():
    """Instantiate UpdateShipmentNameRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "shipment_id": "",
        "body": UpdateShipmentNameRequestBody(**{"name": ""}),
    }
    obj = UpdateShipmentNameRequest(**kwargs)
    assert isinstance(obj, UpdateShipmentNameRequest)


def test_updateshipmentsourceaddressrequestbody_instantiates():
    """Instantiate UpdateShipmentSourceAddressRequestBody with dummy data"""
    kwargs = {
        "address": AddressInput(
            **{
                "address_line1": "",
                "address_line2": None,
                "city": "",
                "company_name": None,
                "country_code": "",
                "email": None,
                "name": "",
                "phone_number": "",
                "postal_code": "",
                "state_or_province_code": None,
            }
        ),
    }
    obj = UpdateShipmentSourceAddressRequestBody(**kwargs)
    assert isinstance(obj, UpdateShipmentSourceAddressRequestBody)


def test_updateshipmentsourceaddressrequest_instantiates():
    """Instantiate UpdateShipmentSourceAddressRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "shipment_id": "",
        "body": UpdateShipmentSourceAddressRequestBody(
            **{
                "address": AddressInput(
                    **{
                        "address_line1": "",
                        "address_line2": None,
                        "city": "",
                        "company_name": None,
                        "country_code": "",
                        "email": None,
                        "name": "",
                        "phone_number": "",
                        "postal_code": "",
                        "state_or_province_code": None,
                    }
                )
            }
        ),
    }
    obj = UpdateShipmentSourceAddressRequest(**kwargs)
    assert isinstance(obj, UpdateShipmentSourceAddressRequest)


def test_updateshipmentsourceaddressresponse_instantiates():
    """Instantiate UpdateShipmentSourceAddressResponse with dummy data"""
    kwargs = {
        "operation_id": "",
    }
    obj = UpdateShipmentSourceAddressResponse(**kwargs)
    assert isinstance(obj, UpdateShipmentSourceAddressResponse)


def test_updateshipmenttrackingdetailsrequestbody_instantiates():
    """Instantiate UpdateShipmentTrackingDetailsRequestBody with dummy data"""
    kwargs = {
        "tracking_details": TrackingDetailsInput(
            **{"ltl_tracking_detail": None, "spd_tracking_detail": None}
        ),
    }
    obj = UpdateShipmentTrackingDetailsRequestBody(**kwargs)
    assert isinstance(obj, UpdateShipmentTrackingDetailsRequestBody)


def test_updateshipmenttrackingdetailsrequest_instantiates():
    """Instantiate UpdateShipmentTrackingDetailsRequest with dummy data"""
    kwargs = {
        "inbound_plan_id": "",
        "shipment_id": "",
        "body": UpdateShipmentTrackingDetailsRequestBody(
            **{
                "tracking_details": TrackingDetailsInput(
                    **{"ltl_tracking_detail": None, "spd_tracking_detail": None}
                )
            }
        ),
    }
    obj = UpdateShipmentTrackingDetailsRequest(**kwargs)
    assert isinstance(obj, UpdateShipmentTrackingDetailsRequest)


def test_updateshipmenttrackingdetailsresponse_instantiates():
    """Instantiate UpdateShipmentTrackingDetailsResponse with dummy data"""
    kwargs = {
        "operation_id": "",
    }
    obj = UpdateShipmentTrackingDetailsResponse(**kwargs)
    assert isinstance(obj, UpdateShipmentTrackingDetailsResponse)
