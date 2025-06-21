# Auto-generated tests for sp_api.api.models.amazon_warehousing_and_distribution.amazon_warehousing_and_distribution_2024_05_09.common.py
from datetime import datetime

import pytest
from sp_api.api.models.amazon_warehousing_and_distribution.amazon_warehousing_and_distribution_2024_05_09.common import (
    Address, CancelInboundRequest, CarrierCode, CheckInboundEligibilityRequest,
    ConfirmInboundRequest, CreateInboundRequest, DestinationDetails,
    DetailsEnum, DistributionPackage, DistributionPackageContents,
    DistributionPackageQuantity, Error, ErrorList, ExpirationDetails,
    FormatTypeEnum, GetInboundRequest, GetInboundShipmentLabelsRequest,
    GetInboundShipmentRequest, GetRequestSerializer, InboundEligibility,
    InboundOrder, InboundOrderCreationData, InboundOrderReference,
    InboundPackages, InboundPreferences, InboundShipment,
    InboundShipmentSummary, InventoryDetails, InventoryListing,
    InventoryQuantity, InventorySummary, ListInboundShipmentsRequest,
    ListInventoryRequest, MeasurementData, OrderIneligibilityReason,
    PackageDimensions, PackageVolume, PackageWeight, PageTypeEnum, PrepDetails,
    PrepInstruction, ProductAttribute, ProductQuantity, RequestsBaseModel,
    ShipmentLabels, ShipmentListing, ShipmentStatusEnum, SkuEligibility,
    SkuIneligibilityReason, SkuQuantitiesEnum, SkuQuantity, SortByEnum,
    SortOrderEnum, SpApiBaseModel, TrackingDetails, TransportationDetails,
    UpdateInboundRequest, UpdateInboundShipmentTransportDetailsRequest)


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
        "address_line3": None,
        "city": None,
        "country_code": "",
        "county": None,
        "district": None,
        "name": "",
        "phone_number": None,
        "postal_code": None,
        "state_or_region": "",
    }
    obj = Address(**kwargs)
    assert isinstance(obj, Address)


def test_cancelinboundrequest_instantiates():
    """Instantiate CancelInboundRequest with dummy data"""
    kwargs = {
        "order_id": "",
    }
    obj = CancelInboundRequest(**kwargs)
    assert isinstance(obj, CancelInboundRequest)


def test_carriercode_instantiates():
    """Instantiate CarrierCode with dummy data"""
    kwargs = {
        "carrier_code_type": None,
        "carrier_code_value": None,
    }
    obj = CarrierCode(**kwargs)
    assert isinstance(obj, CarrierCode)


def test_prepinstruction_instantiates():
    """Instantiate PrepInstruction with dummy data"""
    kwargs = {
        "prep_owner": None,
        "prep_type": None,
    }
    obj = PrepInstruction(**kwargs)
    assert isinstance(obj, PrepInstruction)


def test_prepdetails_instantiates():
    """Instantiate PrepDetails with dummy data"""
    kwargs = {
        "label_owner": None,
        "prep_category": None,
        "prep_instructions": None,
        "prep_owner": None,
    }
    obj = PrepDetails(**kwargs)
    assert isinstance(obj, PrepDetails)


def test_productattribute_instantiates():
    """Instantiate ProductAttribute with dummy data"""
    kwargs = {
        "name": None,
        "value": None,
    }
    obj = ProductAttribute(**kwargs)
    assert isinstance(obj, ProductAttribute)


def test_productquantity_instantiates():
    """Instantiate ProductQuantity with dummy data"""
    kwargs = {
        "attributes": None,
        "quantity": 0,
        "sku": "",
        "expiration": None,
        "prep_details": None,
    }
    obj = ProductQuantity(**kwargs)
    assert isinstance(obj, ProductQuantity)


def test_distributionpackagecontents_instantiates():
    """Instantiate DistributionPackageContents with dummy data"""
    kwargs = {
        "packages": None,
        "products": None,
    }
    obj = DistributionPackageContents(**kwargs)
    assert isinstance(obj, DistributionPackageContents)


def test_packagedimensions_instantiates():
    """Instantiate PackageDimensions with dummy data"""
    kwargs = {
        "height": 0.0,
        "length": 0.0,
        "unit_of_measurement": "",
        "width": 0.0,
    }
    obj = PackageDimensions(**kwargs)
    assert isinstance(obj, PackageDimensions)


def test_packagevolume_instantiates():
    """Instantiate PackageVolume with dummy data"""
    kwargs = {
        "unit_of_measurement": "",
        "volume": 0.0,
    }
    obj = PackageVolume(**kwargs)
    assert isinstance(obj, PackageVolume)


def test_packageweight_instantiates():
    """Instantiate PackageWeight with dummy data"""
    kwargs = {
        "unit_of_measurement": "",
        "weight": 0.0,
    }
    obj = PackageWeight(**kwargs)
    assert isinstance(obj, PackageWeight)


def test_measurementdata_instantiates():
    """Instantiate MeasurementData with dummy data"""
    kwargs = {
        "dimensions": None,
        "volume": None,
        "weight": PackageWeight(**{"unit_of_measurement": "", "weight": 0.0}),
    }
    obj = MeasurementData(**kwargs)
    assert isinstance(obj, MeasurementData)


def test_distributionpackage_instantiates():
    """Instantiate DistributionPackage with dummy data"""
    kwargs = {
        "contents": DistributionPackageContents(**{"packages": None, "products": None}),
        "measurements": MeasurementData(
            **{
                "dimensions": None,
                "volume": None,
                "weight": PackageWeight(**{"unit_of_measurement": "", "weight": 0.0}),
            }
        ),
        "type": "",
    }
    obj = DistributionPackage(**kwargs)
    assert isinstance(obj, DistributionPackage)


def test_distributionpackagequantity_instantiates():
    """Instantiate DistributionPackageQuantity with dummy data"""
    kwargs = {
        "count": 0,
        "distribution_package": DistributionPackage(
            **{
                "contents": DistributionPackageContents(
                    **{"packages": None, "products": None}
                ),
                "measurements": MeasurementData(
                    **{
                        "dimensions": None,
                        "volume": None,
                        "weight": PackageWeight(
                            **{"unit_of_measurement": "", "weight": 0.0}
                        ),
                    }
                ),
                "type": "",
            }
        ),
    }
    obj = DistributionPackageQuantity(**kwargs)
    assert isinstance(obj, DistributionPackageQuantity)


def test_inboundpackages_instantiates():
    """Instantiate InboundPackages with dummy data"""
    kwargs = {
        "packages_to_inbound": [],
    }
    obj = InboundPackages(**kwargs)
    assert isinstance(obj, InboundPackages)


def test_checkinboundeligibilityrequest_instantiates():
    """Instantiate CheckInboundEligibilityRequest with dummy data"""
    kwargs = {
        "body": InboundPackages(**{"packages_to_inbound": []}),
    }
    obj = CheckInboundEligibilityRequest(**kwargs)
    assert isinstance(obj, CheckInboundEligibilityRequest)


def test_confirminboundrequest_instantiates():
    """Instantiate ConfirmInboundRequest with dummy data"""
    kwargs = {
        "order_id": "",
    }
    obj = ConfirmInboundRequest(**kwargs)
    assert isinstance(obj, ConfirmInboundRequest)


def test_inboundpreferences_instantiates():
    """Instantiate InboundPreferences with dummy data"""
    kwargs = {
        "destination_region": None,
    }
    obj = InboundPreferences(**kwargs)
    assert isinstance(obj, InboundPreferences)


def test_inboundordercreationdata_instantiates():
    """Instantiate InboundOrderCreationData with dummy data"""
    kwargs = {
        "external_reference_id": None,
        "origin_address": Address(
            **{
                "address_line1": "",
                "address_line2": None,
                "address_line3": None,
                "city": None,
                "country_code": "",
                "county": None,
                "district": None,
                "name": "",
                "phone_number": None,
                "postal_code": None,
                "state_or_region": "",
            }
        ),
        "packages_to_inbound": [],
        "preferences": None,
    }
    obj = InboundOrderCreationData(**kwargs)
    assert isinstance(obj, InboundOrderCreationData)


def test_createinboundrequest_instantiates():
    """Instantiate CreateInboundRequest with dummy data"""
    kwargs = {
        "body": InboundOrderCreationData(
            **{
                "external_reference_id": None,
                "origin_address": Address(
                    **{
                        "address_line1": "",
                        "address_line2": None,
                        "address_line3": None,
                        "city": None,
                        "country_code": "",
                        "county": None,
                        "district": None,
                        "name": "",
                        "phone_number": None,
                        "postal_code": None,
                        "state_or_region": "",
                    }
                ),
                "packages_to_inbound": [],
                "preferences": None,
            }
        ),
    }
    obj = CreateInboundRequest(**kwargs)
    assert isinstance(obj, CreateInboundRequest)


def test_destinationdetails_instantiates():
    """Instantiate DestinationDetails with dummy data"""
    kwargs = {
        "destination_address": None,
        "destination_region": None,
        "shipment_id": None,
    }
    obj = DestinationDetails(**kwargs)
    assert isinstance(obj, DestinationDetails)


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


def test_expirationdetails_instantiates():
    """Instantiate ExpirationDetails with dummy data"""
    kwargs = {
        "expiration": None,
        "onhand_quantity": None,
    }
    obj = ExpirationDetails(**kwargs)
    assert isinstance(obj, ExpirationDetails)


def test_getinboundrequest_instantiates():
    """Instantiate GetInboundRequest with dummy data"""
    kwargs = {
        "order_id": "",
    }
    obj = GetInboundRequest(**kwargs)
    assert isinstance(obj, GetInboundRequest)


def test_getinboundshipmentlabelsrequest_instantiates():
    """Instantiate GetInboundShipmentLabelsRequest with dummy data"""
    kwargs = {
        "shipment_id": "",
        "page_type": None,
        "format_type": None,
    }
    obj = GetInboundShipmentLabelsRequest(**kwargs)
    assert isinstance(obj, GetInboundShipmentLabelsRequest)


def test_getinboundshipmentrequest_instantiates():
    """Instantiate GetInboundShipmentRequest with dummy data"""
    kwargs = {
        "shipment_id": "",
        "sku_quantities": None,
    }
    obj = GetInboundShipmentRequest(**kwargs)
    assert isinstance(obj, GetInboundShipmentRequest)


def test_orderineligibilityreason_instantiates():
    """Instantiate OrderIneligibilityReason with dummy data"""
    kwargs = {
        "code": "",
        "description": "",
    }
    obj = OrderIneligibilityReason(**kwargs)
    assert isinstance(obj, OrderIneligibilityReason)


def test_skuineligibilityreason_instantiates():
    """Instantiate SkuIneligibilityReason with dummy data"""
    kwargs = {
        "code": "",
        "description": "",
    }
    obj = SkuIneligibilityReason(**kwargs)
    assert isinstance(obj, SkuIneligibilityReason)


def test_skueligibility_instantiates():
    """Instantiate SkuEligibility with dummy data"""
    kwargs = {
        "ineligibility_reasons": None,
        "package_quantity": DistributionPackageQuantity(
            **{
                "count": 0,
                "distribution_package": DistributionPackage(
                    **{
                        "contents": DistributionPackageContents(
                            **{"packages": None, "products": None}
                        ),
                        "measurements": MeasurementData(
                            **{
                                "dimensions": None,
                                "volume": None,
                                "weight": PackageWeight(
                                    **{"unit_of_measurement": "", "weight": 0.0}
                                ),
                            }
                        ),
                        "type": "",
                    }
                ),
            }
        ),
        "status": "",
    }
    obj = SkuEligibility(**kwargs)
    assert isinstance(obj, SkuEligibility)


def test_inboundeligibility_instantiates():
    """Instantiate InboundEligibility with dummy data"""
    kwargs = {
        "ineligibility_reasons": None,
        "packages_to_inbound": [],
        "previewed_at": datetime(2000, 1, 1),
        "status": "",
    }
    obj = InboundEligibility(**kwargs)
    assert isinstance(obj, InboundEligibility)


def test_inboundorder_instantiates():
    """Instantiate InboundOrder with dummy data"""
    kwargs = {
        "created_at": datetime(2000, 1, 1),
        "destination_details": None,
        "external_reference_id": None,
        "order_id": "",
        "order_status": "",
        "origin_address": Address(
            **{
                "address_line1": "",
                "address_line2": None,
                "address_line3": None,
                "city": None,
                "country_code": "",
                "county": None,
                "district": None,
                "name": "",
                "phone_number": None,
                "postal_code": None,
                "state_or_region": "",
            }
        ),
        "packages_to_inbound": [],
        "preferences": None,
        "updated_at": None,
    }
    obj = InboundOrder(**kwargs)
    assert isinstance(obj, InboundOrder)


def test_inboundorderreference_instantiates():
    """Instantiate InboundOrderReference with dummy data"""
    kwargs = {
        "order_id": "",
    }
    obj = InboundOrderReference(**kwargs)
    assert isinstance(obj, InboundOrderReference)


def test_inventoryquantity_instantiates():
    """Instantiate InventoryQuantity with dummy data"""
    kwargs = {
        "quantity": 0.0,
        "unit_of_measurement": "",
    }
    obj = InventoryQuantity(**kwargs)
    assert isinstance(obj, InventoryQuantity)


def test_skuquantity_instantiates():
    """Instantiate SkuQuantity with dummy data"""
    kwargs = {
        "expected_quantity": InventoryQuantity(
            **{"quantity": 0.0, "unit_of_measurement": ""}
        ),
        "received_quantity": None,
        "sku": "",
    }
    obj = SkuQuantity(**kwargs)
    assert isinstance(obj, SkuQuantity)


def test_inboundshipment_instantiates():
    """Instantiate InboundShipment with dummy data"""
    kwargs = {
        "carrier_code": None,
        "created_at": None,
        "destination_address": Address(
            **{
                "address_line1": "",
                "address_line2": None,
                "address_line3": None,
                "city": None,
                "country_code": "",
                "county": None,
                "district": None,
                "name": "",
                "phone_number": None,
                "postal_code": None,
                "state_or_region": "",
            }
        ),
        "external_reference_id": None,
        "order_id": "",
        "origin_address": Address(
            **{
                "address_line1": "",
                "address_line2": None,
                "address_line3": None,
                "city": None,
                "country_code": "",
                "county": None,
                "district": None,
                "name": "",
                "phone_number": None,
                "postal_code": None,
                "state_or_region": "",
            }
        ),
        "received_quantity": None,
        "ship_by": None,
        "shipment_container_quantities": [],
        "shipment_id": "",
        "shipment_sku_quantities": None,
        "destination_region": None,
        "shipment_status": "",
        "tracking_id": None,
        "updated_at": None,
        "warehouse_reference_id": None,
    }
    obj = InboundShipment(**kwargs)
    assert isinstance(obj, InboundShipment)


def test_inboundshipmentsummary_instantiates():
    """Instantiate InboundShipmentSummary with dummy data"""
    kwargs = {
        "created_at": None,
        "external_reference_id": None,
        "order_id": "",
        "shipment_id": "",
        "shipment_status": "",
        "updated_at": None,
    }
    obj = InboundShipmentSummary(**kwargs)
    assert isinstance(obj, InboundShipmentSummary)


def test_inventorydetails_instantiates():
    """Instantiate InventoryDetails with dummy data"""
    kwargs = {
        "available_distributable_quantity": None,
        "replenishment_quantity": None,
        "reserved_distributable_quantity": None,
    }
    obj = InventoryDetails(**kwargs)
    assert isinstance(obj, InventoryDetails)


def test_inventorysummary_instantiates():
    """Instantiate InventorySummary with dummy data"""
    kwargs = {
        "expiration_details": None,
        "inventory_details": None,
        "sku": "",
        "total_inbound_quantity": None,
        "total_onhand_quantity": None,
    }
    obj = InventorySummary(**kwargs)
    assert isinstance(obj, InventorySummary)


def test_inventorylisting_instantiates():
    """Instantiate InventoryListing with dummy data"""
    kwargs = {
        "inventory": [],
        "next_token": None,
    }
    obj = InventoryListing(**kwargs)
    assert isinstance(obj, InventoryListing)


def test_listinboundshipmentsrequest_instantiates():
    """Instantiate ListInboundShipmentsRequest with dummy data"""
    kwargs = {
        "sort_by": None,
        "sort_order": None,
        "shipment_status": None,
        "updated_after": None,
        "updated_before": None,
        "max_results": None,
        "next_token": None,
    }
    obj = ListInboundShipmentsRequest(**kwargs)
    assert isinstance(obj, ListInboundShipmentsRequest)


def test_listinventoryrequest_instantiates():
    """Instantiate ListInventoryRequest with dummy data"""
    kwargs = {
        "sku": None,
        "sort_order": None,
        "details": None,
        "next_token": None,
        "max_results": None,
    }
    obj = ListInventoryRequest(**kwargs)
    assert isinstance(obj, ListInventoryRequest)


def test_shipmentlabels_instantiates():
    """Instantiate ShipmentLabels with dummy data"""
    kwargs = {
        "label_download_u_r_l": None,
        "label_status": "",
    }
    obj = ShipmentLabels(**kwargs)
    assert isinstance(obj, ShipmentLabels)


def test_shipmentlisting_instantiates():
    """Instantiate ShipmentListing with dummy data"""
    kwargs = {
        "next_token": None,
        "shipments": None,
    }
    obj = ShipmentListing(**kwargs)
    assert isinstance(obj, ShipmentListing)


def test_trackingdetails_instantiates():
    """Instantiate TrackingDetails with dummy data"""
    kwargs = {
        "carrier_code": None,
        "booking_id": "",
    }
    obj = TrackingDetails(**kwargs)
    assert isinstance(obj, TrackingDetails)


def test_transportationdetails_instantiates():
    """Instantiate TransportationDetails with dummy data"""
    kwargs = {
        "tracking_details": [],
    }
    obj = TransportationDetails(**kwargs)
    assert isinstance(obj, TransportationDetails)


def test_updateinboundrequest_instantiates():
    """Instantiate UpdateInboundRequest with dummy data"""
    kwargs = {
        "order_id": "",
        "body": InboundOrder(
            **{
                "created_at": datetime(2000, 1, 1),
                "destination_details": None,
                "external_reference_id": None,
                "order_id": "",
                "order_status": "",
                "origin_address": Address(
                    **{
                        "address_line1": "",
                        "address_line2": None,
                        "address_line3": None,
                        "city": None,
                        "country_code": "",
                        "county": None,
                        "district": None,
                        "name": "",
                        "phone_number": None,
                        "postal_code": None,
                        "state_or_region": "",
                    }
                ),
                "packages_to_inbound": [],
                "preferences": None,
                "updated_at": None,
            }
        ),
    }
    obj = UpdateInboundRequest(**kwargs)
    assert isinstance(obj, UpdateInboundRequest)


def test_updateinboundshipmenttransportdetailsrequest_instantiates():
    """Instantiate UpdateInboundShipmentTransportDetailsRequest with dummy data"""
    kwargs = {
        "shipment_id": "",
        "body": TransportationDetails(**{"tracking_details": []}),
    }
    obj = UpdateInboundShipmentTransportDetailsRequest(**kwargs)
    assert isinstance(obj, UpdateInboundShipmentTransportDetailsRequest)
