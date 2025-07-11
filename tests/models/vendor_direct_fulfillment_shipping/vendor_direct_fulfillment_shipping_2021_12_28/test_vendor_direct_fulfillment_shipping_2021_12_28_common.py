# Auto-generated tests for sp_api.api.models.vendor_direct_fulfillment_shipping.vendor_direct_fulfillment_shipping_2021_12_28.common.py
from datetime import datetime

import pytest
from sp_api.api.models.vendor_direct_fulfillment_shipping.vendor_direct_fulfillment_shipping_2021_12_28.common import (
    Address, Container, ContainerContainerTypeEnum, ContainerLabel,
    CreateContainerLabelRequest, CreateContainerLabelRequestBody,
    CreateContainerLabelResponse, CreateShippingLabelsRequest,
    CreateShippingLabelsRequestBody, CustomerInvoice, CustomerInvoiceList,
    Dimensions, DimensionsUnitOfMeasureEnum, Error, ErrorList,
    GetCustomerInvoiceRequest, GetCustomerInvoicesRequest,
    GetCustomerInvoicesRequestSortOrderEnum, GetPackingSlipRequest,
    GetPackingSlipsRequest, GetPackingSlipsRequestSortOrderEnum,
    GetRequestSerializer, GetShippingLabelRequest, GetShippingLabelsRequest,
    GetShippingLabelsRequestSortOrderEnum, Item, ItemQuantity, LabelData,
    Package, PackedItem, PackingSlip, PackingSlipContentTypeEnum,
    PackingSlipList, Pagination, PartyIdentification, RequestsBaseModel,
    ShipmentConfirmation, ShipmentDetails, ShipmentDetailsShipmentStatusEnum,
    ShipmentSchedule, ShipmentStatusUpdate, ShippingLabel,
    ShippingLabelLabelFormatEnum, ShippingLabelList, ShippingLabelRequestBody,
    SpApiBaseModel, StatusUpdateDetails, SubmitShipmentConfirmationsRequest,
    SubmitShipmentConfirmationsRequestBody, SubmitShipmentStatusUpdatesRequest,
    SubmitShipmentStatusUpdatesRequestBody,
    SubmitShippingLabelRequestBodyRequest, SubmitShippingLabelsRequestBody,
    TaxRegistrationDetails, TaxRegistrationDetailsTaxRegistrationTypeEnum,
    TransactionReference, Weight, WeightUnitOfMeasureEnum)


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


def test_dimensions_instantiates():
    """Instantiate Dimensions with dummy data"""
    kwargs = {
        "length": "",
        "width": "",
        "height": "",
        "unit_of_measure": DimensionsUnitOfMeasureEnum.IN,
    }
    obj = Dimensions(**kwargs)
    assert isinstance(obj, Dimensions)


def test_itemquantity_instantiates():
    """Instantiate ItemQuantity with dummy data"""
    kwargs = {
        "amount": 0,
        "unit_of_measure": "",
    }
    obj = ItemQuantity(**kwargs)
    assert isinstance(obj, ItemQuantity)


def test_packeditem_instantiates():
    """Instantiate PackedItem with dummy data"""
    kwargs = {
        "item_sequence_number": 0,
        "buyer_product_identifier": None,
        "piece_number": None,
        "vendor_product_identifier": None,
        "packed_quantity": ItemQuantity(**{"amount": 0, "unit_of_measure": ""}),
    }
    obj = PackedItem(**kwargs)
    assert isinstance(obj, PackedItem)


def test_weight_instantiates():
    """Instantiate Weight with dummy data"""
    kwargs = {
        "unit_of_measure": WeightUnitOfMeasureEnum.KG,
        "value": "",
    }
    obj = Weight(**kwargs)
    assert isinstance(obj, Weight)


def test_container_instantiates():
    """Instantiate Container with dummy data"""
    kwargs = {
        "container_type": ContainerContainerTypeEnum.CARTON,
        "container_identifier": "",
        "tracking_number": None,
        "manifest_id": None,
        "manifest_date": None,
        "ship_method": None,
        "scac_code": None,
        "carrier": None,
        "container_sequence_number": None,
        "dimensions": None,
        "weight": Weight(
            **{"unit_of_measure": WeightUnitOfMeasureEnum.KG, "value": ""}
        ),
        "packed_items": [],
    }
    obj = Container(**kwargs)
    assert isinstance(obj, Container)


def test_containerlabel_instantiates():
    """Instantiate ContainerLabel with dummy data"""
    kwargs = {
        "container_tracking_number": None,
        "content": "",
        "format": "",
    }
    obj = ContainerLabel(**kwargs)
    assert isinstance(obj, ContainerLabel)


def test_taxregistrationdetails_instantiates():
    """Instantiate TaxRegistrationDetails with dummy data"""
    kwargs = {
        "tax_registration_type": None,
        "tax_registration_number": "",
        "tax_registration_address": None,
        "tax_registration_messages": None,
    }
    obj = TaxRegistrationDetails(**kwargs)
    assert isinstance(obj, TaxRegistrationDetails)


def test_partyidentification_instantiates():
    """Instantiate PartyIdentification with dummy data"""
    kwargs = {
        "party_id": "",
        "address": None,
        "tax_registration_details": None,
    }
    obj = PartyIdentification(**kwargs)
    assert isinstance(obj, PartyIdentification)


def test_createcontainerlabelrequestbody_instantiates():
    """Instantiate CreateContainerLabelRequestBody with dummy data"""
    kwargs = {
        "selling_party": PartyIdentification(
            **{"party_id": "", "address": None, "tax_registration_details": None}
        ),
        "ship_from_party": PartyIdentification(
            **{"party_id": "", "address": None, "tax_registration_details": None}
        ),
        "carrier_id": "",
        "vendor_container_id": "",
        "packages": [],
    }
    obj = CreateContainerLabelRequestBody(**kwargs)
    assert isinstance(obj, CreateContainerLabelRequestBody)


def test_createcontainerlabelrequest_instantiates():
    """Instantiate CreateContainerLabelRequest with dummy data"""
    kwargs = {
        "body": CreateContainerLabelRequestBody(
            **{
                "selling_party": PartyIdentification(
                    **{
                        "party_id": "",
                        "address": None,
                        "tax_registration_details": None,
                    }
                ),
                "ship_from_party": PartyIdentification(
                    **{
                        "party_id": "",
                        "address": None,
                        "tax_registration_details": None,
                    }
                ),
                "carrier_id": "",
                "vendor_container_id": "",
                "packages": [],
            }
        ),
    }
    obj = CreateContainerLabelRequest(**kwargs)
    assert isinstance(obj, CreateContainerLabelRequest)


def test_createcontainerlabelresponse_instantiates():
    """Instantiate CreateContainerLabelResponse with dummy data"""
    kwargs = {
        "container_label": ContainerLabel(
            **{"container_tracking_number": None, "content": "", "format": ""}
        ),
    }
    obj = CreateContainerLabelResponse(**kwargs)
    assert isinstance(obj, CreateContainerLabelResponse)


def test_createshippinglabelsrequestbody_instantiates():
    """Instantiate CreateShippingLabelsRequestBody with dummy data"""
    kwargs = {
        "selling_party": PartyIdentification(
            **{"party_id": "", "address": None, "tax_registration_details": None}
        ),
        "ship_from_party": PartyIdentification(
            **{"party_id": "", "address": None, "tax_registration_details": None}
        ),
        "containers": None,
    }
    obj = CreateShippingLabelsRequestBody(**kwargs)
    assert isinstance(obj, CreateShippingLabelsRequestBody)


def test_createshippinglabelsrequest_instantiates():
    """Instantiate CreateShippingLabelsRequest with dummy data"""
    kwargs = {
        "purchase_order_number": "",
        "body": CreateShippingLabelsRequestBody(
            **{
                "selling_party": PartyIdentification(
                    **{
                        "party_id": "",
                        "address": None,
                        "tax_registration_details": None,
                    }
                ),
                "ship_from_party": PartyIdentification(
                    **{
                        "party_id": "",
                        "address": None,
                        "tax_registration_details": None,
                    }
                ),
                "containers": None,
            }
        ),
    }
    obj = CreateShippingLabelsRequest(**kwargs)
    assert isinstance(obj, CreateShippingLabelsRequest)


def test_customerinvoice_instantiates():
    """Instantiate CustomerInvoice with dummy data"""
    kwargs = {
        "purchase_order_number": "",
        "content": "",
    }
    obj = CustomerInvoice(**kwargs)
    assert isinstance(obj, CustomerInvoice)


def test_pagination_instantiates():
    """Instantiate Pagination with dummy data"""
    kwargs = {
        "next_token": None,
    }
    obj = Pagination(**kwargs)
    assert isinstance(obj, Pagination)


def test_customerinvoicelist_instantiates():
    """Instantiate CustomerInvoiceList with dummy data"""
    kwargs = {
        "pagination": None,
        "customer_invoices": None,
    }
    obj = CustomerInvoiceList(**kwargs)
    assert isinstance(obj, CustomerInvoiceList)


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


def test_getcustomerinvoicerequest_instantiates():
    """Instantiate GetCustomerInvoiceRequest with dummy data"""
    kwargs = {
        "purchase_order_number": "",
    }
    obj = GetCustomerInvoiceRequest(**kwargs)
    assert isinstance(obj, GetCustomerInvoiceRequest)


def test_getcustomerinvoicesrequest_instantiates():
    """Instantiate GetCustomerInvoicesRequest with dummy data"""
    kwargs = {
        "ship_from_party_id": None,
        "limit": None,
        "created_after": datetime(2000, 1, 1),
        "created_before": datetime(2000, 1, 1),
        "sort_order": None,
        "next_token": None,
    }
    obj = GetCustomerInvoicesRequest(**kwargs)
    assert isinstance(obj, GetCustomerInvoicesRequest)


def test_getpackingsliprequest_instantiates():
    """Instantiate GetPackingSlipRequest with dummy data"""
    kwargs = {
        "purchase_order_number": "",
    }
    obj = GetPackingSlipRequest(**kwargs)
    assert isinstance(obj, GetPackingSlipRequest)


def test_getpackingslipsrequest_instantiates():
    """Instantiate GetPackingSlipsRequest with dummy data"""
    kwargs = {
        "ship_from_party_id": None,
        "limit": None,
        "created_after": datetime(2000, 1, 1),
        "created_before": datetime(2000, 1, 1),
        "sort_order": None,
        "next_token": None,
    }
    obj = GetPackingSlipsRequest(**kwargs)
    assert isinstance(obj, GetPackingSlipsRequest)


def test_getshippinglabelrequest_instantiates():
    """Instantiate GetShippingLabelRequest with dummy data"""
    kwargs = {
        "purchase_order_number": "",
    }
    obj = GetShippingLabelRequest(**kwargs)
    assert isinstance(obj, GetShippingLabelRequest)


def test_getshippinglabelsrequest_instantiates():
    """Instantiate GetShippingLabelsRequest with dummy data"""
    kwargs = {
        "ship_from_party_id": None,
        "limit": None,
        "created_after": datetime(2000, 1, 1),
        "created_before": datetime(2000, 1, 1),
        "sort_order": None,
        "next_token": None,
    }
    obj = GetShippingLabelsRequest(**kwargs)
    assert isinstance(obj, GetShippingLabelsRequest)


def test_item_instantiates():
    """Instantiate Item with dummy data"""
    kwargs = {
        "item_sequence_number": 0,
        "buyer_product_identifier": None,
        "vendor_product_identifier": None,
        "shipped_quantity": ItemQuantity(**{"amount": 0, "unit_of_measure": ""}),
    }
    obj = Item(**kwargs)
    assert isinstance(obj, Item)


def test_labeldata_instantiates():
    """Instantiate LabelData with dummy data"""
    kwargs = {
        "package_identifier": None,
        "tracking_number": None,
        "ship_method": None,
        "ship_method_name": None,
        "content": "",
    }
    obj = LabelData(**kwargs)
    assert isinstance(obj, LabelData)


def test_package_instantiates():
    """Instantiate Package with dummy data"""
    kwargs = {
        "package_tracking_number": "",
    }
    obj = Package(**kwargs)
    assert isinstance(obj, Package)


def test_packingslip_instantiates():
    """Instantiate PackingSlip with dummy data"""
    kwargs = {
        "purchase_order_number": "",
        "content": "",
        "content_type": None,
    }
    obj = PackingSlip(**kwargs)
    assert isinstance(obj, PackingSlip)


def test_packingsliplist_instantiates():
    """Instantiate PackingSlipList with dummy data"""
    kwargs = {
        "pagination": None,
        "packing_slips": None,
    }
    obj = PackingSlipList(**kwargs)
    assert isinstance(obj, PackingSlipList)


def test_shipmentdetails_instantiates():
    """Instantiate ShipmentDetails with dummy data"""
    kwargs = {
        "shipped_date": datetime(2000, 1, 1),
        "shipment_status": ShipmentDetailsShipmentStatusEnum.SHIPPED,
        "is_priority_shipment": None,
        "vendor_order_number": None,
        "estimated_delivery_date": None,
    }
    obj = ShipmentDetails(**kwargs)
    assert isinstance(obj, ShipmentDetails)


def test_shipmentconfirmation_instantiates():
    """Instantiate ShipmentConfirmation with dummy data"""
    kwargs = {
        "purchase_order_number": "",
        "shipment_details": ShipmentDetails(
            **{
                "shipped_date": datetime(2000, 1, 1),
                "shipment_status": ShipmentDetailsShipmentStatusEnum.SHIPPED,
                "is_priority_shipment": None,
                "vendor_order_number": None,
                "estimated_delivery_date": None,
            }
        ),
        "selling_party": PartyIdentification(
            **{"party_id": "", "address": None, "tax_registration_details": None}
        ),
        "ship_from_party": PartyIdentification(
            **{"party_id": "", "address": None, "tax_registration_details": None}
        ),
        "items": [],
        "containers": None,
    }
    obj = ShipmentConfirmation(**kwargs)
    assert isinstance(obj, ShipmentConfirmation)


def test_shipmentschedule_instantiates():
    """Instantiate ShipmentSchedule with dummy data"""
    kwargs = {
        "estimated_delivery_date_time": None,
        "appt_window_start_date_time": None,
        "appt_window_end_date_time": None,
    }
    obj = ShipmentSchedule(**kwargs)
    assert isinstance(obj, ShipmentSchedule)


def test_statusupdatedetails_instantiates():
    """Instantiate StatusUpdateDetails with dummy data"""
    kwargs = {
        "tracking_number": "",
        "status_code": "",
        "reason_code": "",
        "status_date_time": datetime(2000, 1, 1),
        "status_location_address": Address(
            **{
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
        ),
        "shipment_schedule": None,
    }
    obj = StatusUpdateDetails(**kwargs)
    assert isinstance(obj, StatusUpdateDetails)


def test_shipmentstatusupdate_instantiates():
    """Instantiate ShipmentStatusUpdate with dummy data"""
    kwargs = {
        "purchase_order_number": "",
        "selling_party": PartyIdentification(
            **{"party_id": "", "address": None, "tax_registration_details": None}
        ),
        "ship_from_party": PartyIdentification(
            **{"party_id": "", "address": None, "tax_registration_details": None}
        ),
        "status_update_details": StatusUpdateDetails(
            **{
                "tracking_number": "",
                "status_code": "",
                "reason_code": "",
                "status_date_time": datetime(2000, 1, 1),
                "status_location_address": Address(
                    **{
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
                ),
                "shipment_schedule": None,
            }
        ),
    }
    obj = ShipmentStatusUpdate(**kwargs)
    assert isinstance(obj, ShipmentStatusUpdate)


def test_shippinglabel_instantiates():
    """Instantiate ShippingLabel with dummy data"""
    kwargs = {
        "purchase_order_number": "",
        "selling_party": PartyIdentification(
            **{"party_id": "", "address": None, "tax_registration_details": None}
        ),
        "ship_from_party": PartyIdentification(
            **{"party_id": "", "address": None, "tax_registration_details": None}
        ),
        "label_format": ShippingLabelLabelFormatEnum.PNG,
        "label_data": [],
    }
    obj = ShippingLabel(**kwargs)
    assert isinstance(obj, ShippingLabel)


def test_shippinglabellist_instantiates():
    """Instantiate ShippingLabelList with dummy data"""
    kwargs = {
        "pagination": None,
        "shipping_labels": None,
    }
    obj = ShippingLabelList(**kwargs)
    assert isinstance(obj, ShippingLabelList)


def test_shippinglabelrequestbody_instantiates():
    """Instantiate ShippingLabelRequestBody with dummy data"""
    kwargs = {
        "purchase_order_number": "",
        "selling_party": PartyIdentification(
            **{"party_id": "", "address": None, "tax_registration_details": None}
        ),
        "ship_from_party": PartyIdentification(
            **{"party_id": "", "address": None, "tax_registration_details": None}
        ),
        "containers": None,
    }
    obj = ShippingLabelRequestBody(**kwargs)
    assert isinstance(obj, ShippingLabelRequestBody)


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


def test_submitshipmentstatusupdatesrequestbody_instantiates():
    """Instantiate SubmitShipmentStatusUpdatesRequestBody with dummy data"""
    kwargs = {
        "shipment_status_updates": None,
    }
    obj = SubmitShipmentStatusUpdatesRequestBody(**kwargs)
    assert isinstance(obj, SubmitShipmentStatusUpdatesRequestBody)


def test_submitshipmentstatusupdatesrequest_instantiates():
    """Instantiate SubmitShipmentStatusUpdatesRequest with dummy data"""
    kwargs = {
        "body": SubmitShipmentStatusUpdatesRequestBody(
            **{"shipment_status_updates": None}
        ),
    }
    obj = SubmitShipmentStatusUpdatesRequest(**kwargs)
    assert isinstance(obj, SubmitShipmentStatusUpdatesRequest)


def test_submitshippinglabelsrequestbody_instantiates():
    """Instantiate SubmitShippingLabelsRequestBody with dummy data"""
    kwargs = {
        "shipping_label_requests": None,
    }
    obj = SubmitShippingLabelsRequestBody(**kwargs)
    assert isinstance(obj, SubmitShippingLabelsRequestBody)


def test_submitshippinglabelrequestbodyrequest_instantiates():
    """Instantiate SubmitShippingLabelRequestBodyRequest with dummy data"""
    kwargs = {
        "body": SubmitShippingLabelsRequestBody(**{"shipping_label_requests": None}),
    }
    obj = SubmitShippingLabelRequestBodyRequest(**kwargs)
    assert isinstance(obj, SubmitShippingLabelRequestBodyRequest)


def test_transactionreference_instantiates():
    """Instantiate TransactionReference with dummy data"""
    kwargs = {
        "transaction_id": None,
    }
    obj = TransactionReference(**kwargs)
    assert isinstance(obj, TransactionReference)
