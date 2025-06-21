# Auto-generated tests for sp_api.api.models.vendor_shipments.vendor_shipments_v1.common.py
from datetime import datetime

import pytest
from sp_api.api.models.vendor_shipments.vendor_shipments_v1.common import (
    Address, CarrierDetails, Carton, CartonReferenceDetails,
    CollectFreightPickupDetails, ContainerIdentification,
    ContainerIdentificationTypeEnum, ContainerItem, Containers,
    ContainerSequenceNumbers, ContainerTypeEnum, CurrentShipmentStatusEnum,
    Dimensions, Duration, DurationUnitEnum, Error, Expiry, FunctionCodeEnum,
    GetRequestSerializer, GetShipmentDetailsRequest,
    GetShipmentDetailsResponse, GetShipmentLabels, GetShipmentLabelsRequest,
    HandlingCodeEnum, HandlingInstructionsEnum, ImportDetails,
    InnerContainersDetails, Item, ItemDetails, ItemQuantity, LabelData,
    LabelFormatEnum, Location, MethodOfPaymentEnum, Money, PackageItemDetails,
    PackedItems, PackedQuantity, Pagination, Pallet, PartyIdentification,
    PurchaseOrderItemDetails, PurchaseOrderItems, PurchaseOrders,
    RequestsBaseModel, Route, Shipment, ShipmentConfirmation,
    ShipmentConfirmationTypeEnum, ShipmentDetails, ShipmentFreightTermEnum,
    ShipmentInformation, ShipmentMeasurements, ShipmentStatusDetails,
    ShipmentStatusEnum, ShipmentStructureEnum, ShipmentTypeEnum, ShipModeEnum,
    SortOrderEnum, SpApiBaseModel, Stop, SubmitShipmentConfirmationsRequest,
    SubmitShipmentConfirmationsRequestBody,
    SubmitShipmentConfirmationsResponse, SubmitShipments,
    SubmitShipmentsRequest, TaxRegistrationDetails, TaxRegistrationTypeEnum,
    TotalWeight, TransactionReference, TransactionTypeEnum,
    TransportationDetails, TransportationDetailsForShipmentConfirmation,
    TransportationLabels, TransportationModeEnum, TransportLabel,
    TransportShipmentMeasurements, UnitOfMeasureEnum, VendorDetails, Volume,
    Weight)


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
        "state_or_region": None,
        "postal_code": None,
        "country_code": "",
        "phone": None,
    }
    obj = Address(**kwargs)
    assert isinstance(obj, Address)


def test_carrierdetails_instantiates():
    """Instantiate CarrierDetails with dummy data"""
    kwargs = {
        "name": None,
        "code": None,
        "phone": None,
        "email": None,
        "shipment_reference_number": None,
    }
    obj = CarrierDetails(**kwargs)
    assert isinstance(obj, CarrierDetails)


def test_containeridentification_instantiates():
    """Instantiate ContainerIdentification with dummy data"""
    kwargs = {
        "container_identification_type": ContainerIdentificationTypeEnum.SSCC,
        "container_identification_number": "",
    }
    obj = ContainerIdentification(**kwargs)
    assert isinstance(obj, ContainerIdentification)


def test_duration_instantiates():
    """Instantiate Duration with dummy data"""
    kwargs = {
        "duration_unit": DurationUnitEnum.DAYS,
        "duration_value": 0,
    }
    obj = Duration(**kwargs)
    assert isinstance(obj, Duration)


def test_expiry_instantiates():
    """Instantiate Expiry with dummy data"""
    kwargs = {
        "manufacturer_date": None,
        "expiry_date": None,
        "expiry_after_duration": None,
    }
    obj = Expiry(**kwargs)
    assert isinstance(obj, Expiry)


def test_money_instantiates():
    """Instantiate Money with dummy data"""
    kwargs = {
        "currency_code": "",
        "amount": "",
    }
    obj = Money(**kwargs)
    assert isinstance(obj, Money)


def test_itemdetails_instantiates():
    """Instantiate ItemDetails with dummy data"""
    kwargs = {
        "purchase_order_number": None,
        "lot_number": None,
        "expiry": None,
        "maximum_retail_price": None,
        "handling_code": None,
    }
    obj = ItemDetails(**kwargs)
    assert isinstance(obj, ItemDetails)


def test_totalweight_instantiates():
    """Instantiate TotalWeight with dummy data"""
    kwargs = {
        "unit_of_measure": UnitOfMeasureEnum.CASES,
        "amount": "",
    }
    obj = TotalWeight(**kwargs)
    assert isinstance(obj, TotalWeight)


def test_itemquantity_instantiates():
    """Instantiate ItemQuantity with dummy data"""
    kwargs = {
        "amount": 0,
        "unit_of_measure": UnitOfMeasureEnum.CASES,
        "unit_size": None,
        "total_weight": None,
    }
    obj = ItemQuantity(**kwargs)
    assert isinstance(obj, ItemQuantity)


def test_containeritem_instantiates():
    """Instantiate ContainerItem with dummy data"""
    kwargs = {
        "item_reference": "",
        "shipped_quantity": ItemQuantity(
            **{
                "amount": 0,
                "unit_of_measure": UnitOfMeasureEnum.CASES,
                "unit_size": None,
                "total_weight": None,
            }
        ),
        "item_details": None,
    }
    obj = ContainerItem(**kwargs)
    assert isinstance(obj, ContainerItem)


def test_dimensions_instantiates():
    """Instantiate Dimensions with dummy data"""
    kwargs = {
        "length": "",
        "width": "",
        "height": "",
        "unit_of_measure": UnitOfMeasureEnum.CASES,
    }
    obj = Dimensions(**kwargs)
    assert isinstance(obj, Dimensions)


def test_weight_instantiates():
    """Instantiate Weight with dummy data"""
    kwargs = {
        "unit_of_measure": UnitOfMeasureEnum.CASES,
        "value": "",
    }
    obj = Weight(**kwargs)
    assert isinstance(obj, Weight)


def test_carton_instantiates():
    """Instantiate Carton with dummy data"""
    kwargs = {
        "carton_identifiers": None,
        "carton_sequence_number": "",
        "dimensions": None,
        "weight": None,
        "tracking_number": None,
        "items": [],
    }
    obj = Carton(**kwargs)
    assert isinstance(obj, Carton)


def test_cartonreferencedetails_instantiates():
    """Instantiate CartonReferenceDetails with dummy data"""
    kwargs = {
        "carton_count": None,
        "carton_reference_numbers": [],
    }
    obj = CartonReferenceDetails(**kwargs)
    assert isinstance(obj, CartonReferenceDetails)


def test_collectfreightpickupdetails_instantiates():
    """Instantiate CollectFreightPickupDetails with dummy data"""
    kwargs = {
        "requested_pick_up": None,
        "scheduled_pick_up": None,
        "carrier_assignment_date": None,
    }
    obj = CollectFreightPickupDetails(**kwargs)
    assert isinstance(obj, CollectFreightPickupDetails)


def test_containersequencenumbers_instantiates():
    """Instantiate ContainerSequenceNumbers with dummy data"""
    kwargs = {
        "container_sequence_number": None,
    }
    obj = ContainerSequenceNumbers(**kwargs)
    assert isinstance(obj, ContainerSequenceNumbers)


def test_innercontainersdetails_instantiates():
    """Instantiate InnerContainersDetails with dummy data"""
    kwargs = {
        "container_count": None,
        "container_sequence_numbers": None,
    }
    obj = InnerContainersDetails(**kwargs)
    assert isinstance(obj, InnerContainersDetails)


def test_packageitemdetails_instantiates():
    """Instantiate PackageItemDetails with dummy data"""
    kwargs = {
        "purchase_order_number": None,
        "lot_number": None,
        "expiry": None,
    }
    obj = PackageItemDetails(**kwargs)
    assert isinstance(obj, PackageItemDetails)


def test_packeditems_instantiates():
    """Instantiate PackedItems with dummy data"""
    kwargs = {
        "item_sequence_number": None,
        "buyer_product_identifier": None,
        "vendor_product_identifier": None,
        "packed_quantity": None,
        "item_details": None,
    }
    obj = PackedItems(**kwargs)
    assert isinstance(obj, PackedItems)


def test_containers_instantiates():
    """Instantiate Containers with dummy data"""
    kwargs = {
        "container_type": ContainerTypeEnum.CARTON,
        "container_sequence_number": None,
        "container_identifiers": [],
        "tracking_number": None,
        "dimensions": None,
        "weight": None,
        "tier": None,
        "block": None,
        "inner_containers_details": None,
        "packed_items": None,
    }
    obj = Containers(**kwargs)
    assert isinstance(obj, Containers)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_getshipmentdetailsrequest_instantiates():
    """Instantiate GetShipmentDetailsRequest with dummy data"""
    kwargs = {
        "limit": None,
        "sort_order": None,
        "next_token": None,
        "created_after": None,
        "created_before": None,
        "shipment_confirmed_before": None,
        "shipment_confirmed_after": None,
        "package_label_created_before": None,
        "package_label_created_after": None,
        "shipped_before": None,
        "shipped_after": None,
        "estimated_delivery_before": None,
        "estimated_delivery_after": None,
        "shipment_delivery_before": None,
        "shipment_delivery_after": None,
        "requested_pick_up_before": None,
        "requested_pick_up_after": None,
        "scheduled_pick_up_before": None,
        "scheduled_pick_up_after": None,
        "current_shipment_status": None,
        "vendor_shipment_identifier": None,
        "buyer_reference_number": None,
        "buyer_warehouse_code": None,
        "seller_warehouse_code": None,
    }
    obj = GetShipmentDetailsRequest(**kwargs)
    assert isinstance(obj, GetShipmentDetailsRequest)


def test_pagination_instantiates():
    """Instantiate Pagination with dummy data"""
    kwargs = {
        "next_token": None,
    }
    obj = Pagination(**kwargs)
    assert isinstance(obj, Pagination)


def test_location_instantiates():
    """Instantiate Location with dummy data"""
    kwargs = {
        "type": None,
        "location_code": None,
        "country_code": None,
    }
    obj = Location(**kwargs)
    assert isinstance(obj, Location)


def test_stop_instantiates():
    """Instantiate Stop with dummy data"""
    kwargs = {
        "function_code": FunctionCodeEnum.PORT_OF_DISCHARGE,
        "location_identification": None,
        "arrival_time": None,
        "departure_time": None,
    }
    obj = Stop(**kwargs)
    assert isinstance(obj, Stop)


def test_route_instantiates():
    """Instantiate Route with dummy data"""
    kwargs = {
        "stops": [],
    }
    obj = Route(**kwargs)
    assert isinstance(obj, Route)


def test_importdetails_instantiates():
    """Instantiate ImportDetails with dummy data"""
    kwargs = {
        "method_of_payment": None,
        "seal_number": None,
        "route": None,
        "import_containers": None,
        "billable_weight": None,
        "estimated_ship_by_date": None,
        "handling_instructions": None,
    }
    obj = ImportDetails(**kwargs)
    assert isinstance(obj, ImportDetails)


def test_taxregistrationdetails_instantiates():
    """Instantiate TaxRegistrationDetails with dummy data"""
    kwargs = {
        "tax_registration_type": TaxRegistrationTypeEnum.VAT,
        "tax_registration_number": "",
    }
    obj = TaxRegistrationDetails(**kwargs)
    assert isinstance(obj, TaxRegistrationDetails)


def test_partyidentification_instantiates():
    """Instantiate PartyIdentification with dummy data"""
    kwargs = {
        "address": None,
        "party_id": "",
        "tax_registration_details": None,
    }
    obj = PartyIdentification(**kwargs)
    assert isinstance(obj, PartyIdentification)


def test_purchaseorderitems_instantiates():
    """Instantiate PurchaseOrderItems with dummy data"""
    kwargs = {
        "item_sequence_number": "",
        "buyer_product_identifier": None,
        "vendor_product_identifier": None,
        "shipped_quantity": ItemQuantity(
            **{
                "amount": 0,
                "unit_of_measure": UnitOfMeasureEnum.CASES,
                "unit_size": None,
                "total_weight": None,
            }
        ),
        "maximum_retail_price": None,
    }
    obj = PurchaseOrderItems(**kwargs)
    assert isinstance(obj, PurchaseOrderItems)


def test_purchaseorders_instantiates():
    """Instantiate PurchaseOrders with dummy data"""
    kwargs = {
        "purchase_order_number": None,
        "purchase_order_date": None,
        "ship_window": None,
        "items": None,
    }
    obj = PurchaseOrders(**kwargs)
    assert isinstance(obj, PurchaseOrders)


def test_shipmentstatusdetails_instantiates():
    """Instantiate ShipmentStatusDetails with dummy data"""
    kwargs = {
        "shipment_status": None,
        "shipment_status_date": None,
    }
    obj = ShipmentStatusDetails(**kwargs)
    assert isinstance(obj, ShipmentStatusDetails)


def test_volume_instantiates():
    """Instantiate Volume with dummy data"""
    kwargs = {
        "unit_of_measure": UnitOfMeasureEnum.CASES,
        "value": "",
    }
    obj = Volume(**kwargs)
    assert isinstance(obj, Volume)


def test_transportshipmentmeasurements_instantiates():
    """Instantiate TransportShipmentMeasurements with dummy data"""
    kwargs = {
        "total_carton_count": None,
        "total_pallet_stackable": None,
        "total_pallet_non_stackable": None,
        "shipment_weight": None,
        "shipment_volume": None,
    }
    obj = TransportShipmentMeasurements(**kwargs)
    assert isinstance(obj, TransportShipmentMeasurements)


def test_transportationdetails_instantiates():
    """Instantiate TransportationDetails with dummy data"""
    kwargs = {
        "ship_mode": None,
        "transportation_mode": None,
        "shipped_date": None,
        "estimated_delivery_date": None,
        "shipment_delivery_date": None,
        "carrier_details": None,
        "bill_of_lading_number": None,
    }
    obj = TransportationDetails(**kwargs)
    assert isinstance(obj, TransportationDetails)


def test_shipment_instantiates():
    """Instantiate Shipment with dummy data"""
    kwargs = {
        "vendor_shipment_identifier": "",
        "transaction_type": TransactionTypeEnum.NEW,
        "buyer_reference_number": None,
        "transaction_date": datetime(2000, 1, 1),
        "current_shipment_status": None,
        "currentshipment_status_date": None,
        "shipment_status_details": None,
        "shipment_create_date": None,
        "shipment_confirm_date": None,
        "package_label_create_date": None,
        "shipment_freight_term": None,
        "selling_party": PartyIdentification(
            **{"address": None, "party_id": "", "tax_registration_details": None}
        ),
        "ship_from_party": PartyIdentification(
            **{"address": None, "party_id": "", "tax_registration_details": None}
        ),
        "ship_to_party": PartyIdentification(
            **{"address": None, "party_id": "", "tax_registration_details": None}
        ),
        "shipment_measurements": None,
        "collect_freight_pickup_details": None,
        "purchase_orders": None,
        "import_details": None,
        "containers": None,
        "transportation_details": None,
    }
    obj = Shipment(**kwargs)
    assert isinstance(obj, Shipment)


def test_shipmentdetails_instantiates():
    """Instantiate ShipmentDetails with dummy data"""
    kwargs = {
        "pagination": None,
        "shipments": None,
    }
    obj = ShipmentDetails(**kwargs)
    assert isinstance(obj, ShipmentDetails)


def test_getshipmentdetailsresponse_instantiates():
    """Instantiate GetShipmentDetailsResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetShipmentDetailsResponse(**kwargs)
    assert isinstance(obj, GetShipmentDetailsResponse)


def test_labeldata_instantiates():
    """Instantiate LabelData with dummy data"""
    kwargs = {
        "label_sequence_number": None,
        "label_format": None,
        "carrier_code": None,
        "tracking_id": None,
        "label": None,
    }
    obj = LabelData(**kwargs)
    assert isinstance(obj, LabelData)


def test_vendordetails_instantiates():
    """Instantiate VendorDetails with dummy data"""
    kwargs = {
        "selling_party": None,
        "vendor_shipment_identifier": None,
    }
    obj = VendorDetails(**kwargs)
    assert isinstance(obj, VendorDetails)


def test_shipmentinformation_instantiates():
    """Instantiate ShipmentInformation with dummy data"""
    kwargs = {
        "vendor_details": None,
        "buyer_reference_number": None,
        "ship_to_party": None,
        "ship_from_party": None,
        "warehouse_id": None,
        "master_tracking_id": None,
        "total_label_count": None,
        "ship_mode": None,
    }
    obj = ShipmentInformation(**kwargs)
    assert isinstance(obj, ShipmentInformation)


def test_transportlabel_instantiates():
    """Instantiate TransportLabel with dummy data"""
    kwargs = {
        "label_create_date_time": None,
        "shipment_information": None,
        "label_data": None,
    }
    obj = TransportLabel(**kwargs)
    assert isinstance(obj, TransportLabel)


def test_transportationlabels_instantiates():
    """Instantiate TransportationLabels with dummy data"""
    kwargs = {
        "pagination": None,
        "transport_labels": None,
    }
    obj = TransportationLabels(**kwargs)
    assert isinstance(obj, TransportationLabels)


def test_getshipmentlabels_instantiates():
    """Instantiate GetShipmentLabels with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetShipmentLabels(**kwargs)
    assert isinstance(obj, GetShipmentLabels)


def test_getshipmentlabelsrequest_instantiates():
    """Instantiate GetShipmentLabelsRequest with dummy data"""
    kwargs = {
        "limit": None,
        "sort_order": None,
        "next_token": None,
        "label_created_after": None,
        "label_created_before": None,
        "buyer_reference_number": None,
        "vendor_shipment_identifier": None,
        "seller_warehouse_code": None,
    }
    obj = GetShipmentLabelsRequest(**kwargs)
    assert isinstance(obj, GetShipmentLabelsRequest)


def test_item_instantiates():
    """Instantiate Item with dummy data"""
    kwargs = {
        "item_sequence_number": "",
        "amazon_product_identifier": None,
        "vendor_product_identifier": None,
        "shipped_quantity": ItemQuantity(
            **{
                "amount": 0,
                "unit_of_measure": UnitOfMeasureEnum.CASES,
                "unit_size": None,
                "total_weight": None,
            }
        ),
        "item_details": None,
    }
    obj = Item(**kwargs)
    assert isinstance(obj, Item)


def test_packedquantity_instantiates():
    """Instantiate PackedQuantity with dummy data"""
    kwargs = {
        "amount": 0,
        "unit_of_measure": UnitOfMeasureEnum.CASES,
        "unit_size": None,
    }
    obj = PackedQuantity(**kwargs)
    assert isinstance(obj, PackedQuantity)


def test_pallet_instantiates():
    """Instantiate Pallet with dummy data"""
    kwargs = {
        "pallet_identifiers": [],
        "tier": None,
        "block": None,
        "dimensions": None,
        "weight": None,
        "carton_reference_details": None,
        "items": None,
    }
    obj = Pallet(**kwargs)
    assert isinstance(obj, Pallet)


def test_purchaseorderitemdetails_instantiates():
    """Instantiate PurchaseOrderItemDetails with dummy data"""
    kwargs = {
        "maximum_retail_price": None,
    }
    obj = PurchaseOrderItemDetails(**kwargs)
    assert isinstance(obj, PurchaseOrderItemDetails)


def test_shipmentmeasurements_instantiates():
    """Instantiate ShipmentMeasurements with dummy data"""
    kwargs = {
        "gross_shipment_weight": None,
        "shipment_volume": None,
        "carton_count": None,
        "pallet_count": None,
    }
    obj = ShipmentMeasurements(**kwargs)
    assert isinstance(obj, ShipmentMeasurements)


def test_transportationdetailsforshipmentconfirmation_instantiates():
    """Instantiate TransportationDetailsForShipmentConfirmation with dummy data"""
    kwargs = {
        "carrier_scac": None,
        "carrier_shipment_reference_number": None,
        "transportation_mode": None,
        "bill_of_lading_number": None,
    }
    obj = TransportationDetailsForShipmentConfirmation(**kwargs)
    assert isinstance(obj, TransportationDetailsForShipmentConfirmation)


def test_shipmentconfirmation_instantiates():
    """Instantiate ShipmentConfirmation with dummy data"""
    kwargs = {
        "shipment_identifier": "",
        "shipment_confirmation_type": ShipmentConfirmationTypeEnum.ORIGINAL,
        "shipment_type": None,
        "shipment_structure": None,
        "transportation_details": None,
        "amazon_reference_number": None,
        "shipment_confirmation_date": datetime(2000, 1, 1),
        "shipped_date": None,
        "estimated_delivery_date": None,
        "selling_party": PartyIdentification(
            **{"address": None, "party_id": "", "tax_registration_details": None}
        ),
        "ship_from_party": PartyIdentification(
            **{"address": None, "party_id": "", "tax_registration_details": None}
        ),
        "ship_to_party": PartyIdentification(
            **{"address": None, "party_id": "", "tax_registration_details": None}
        ),
        "shipment_measurements": None,
        "import_details": None,
        "shipped_items": [],
        "cartons": None,
        "pallets": None,
    }
    obj = ShipmentConfirmation(**kwargs)
    assert isinstance(obj, ShipmentConfirmation)


def test_submitshipmentconfirmationsrequestbody_instantiates():
    """Instantiate SubmitShipmentConfirmationsRequestBody with dummy data"""
    kwargs = {
        "shipment_confirmations": None,
    }
    obj = SubmitShipmentConfirmationsRequestBody(**kwargs)
    assert isinstance(obj, SubmitShipmentConfirmationsRequestBody)


def test_submitshipmentconfirmationsrequest_instantiates():
    """Instantiate SubmitShipmentConfirmationsRequest with dummy data"""
    kwargs = {
        "body": SubmitShipmentConfirmationsRequestBody(
            **{"shipment_confirmations": None}
        ),
    }
    obj = SubmitShipmentConfirmationsRequest(**kwargs)
    assert isinstance(obj, SubmitShipmentConfirmationsRequest)


def test_transactionreference_instantiates():
    """Instantiate TransactionReference with dummy data"""
    kwargs = {
        "transaction_id": None,
    }
    obj = TransactionReference(**kwargs)
    assert isinstance(obj, TransactionReference)


def test_submitshipmentconfirmationsresponse_instantiates():
    """Instantiate SubmitShipmentConfirmationsResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = SubmitShipmentConfirmationsResponse(**kwargs)
    assert isinstance(obj, SubmitShipmentConfirmationsResponse)


def test_submitshipments_instantiates():
    """Instantiate SubmitShipments with dummy data"""
    kwargs = {
        "shipments": None,
    }
    obj = SubmitShipments(**kwargs)
    assert isinstance(obj, SubmitShipments)


def test_submitshipmentsrequest_instantiates():
    """Instantiate SubmitShipmentsRequest with dummy data"""
    kwargs = {
        "body": SubmitShipments(**{"shipments": None}),
    }
    obj = SubmitShipmentsRequest(**kwargs)
    assert isinstance(obj, SubmitShipmentsRequest)
