# Auto-generated tests for sp_api.api.models.shipping.shipping_v1.common.py
from datetime import datetime

import pytest
from sp_api.api.models.shipping.shipping_v1.common import (
    AcceptedRate, Account, Address, CancelShipmentRequest,
    CancelShipmentResponse, Container, ContainerContainerTypeEnum,
    ContainerItem, ContainerSpecification, CreateShipmentRequest,
    CreateShipmentRequestBody, CreateShipmentResponse, CreateShipmentResult,
    Currency, Dimensions, DimensionsUnitEnum, Error, Event, GetAccountResponse,
    GetRatesRequest, GetRatesRequestBody, GetRatesResponse, GetRatesResult,
    GetRequestSerializer, GetShipmentRequest, GetShipmentResponse,
    GetTrackingInformationRequest, GetTrackingInformationResponse, Label,
    LabelResult, LabelSpecification, LabelSpecificationLabelFormatEnum,
    LabelSpecificationLabelStockSizeEnum, Location, Party,
    PurchaseLabelsRequest, PurchaseLabelsRequestBody, PurchaseLabelsResponse,
    PurchaseLabelsResult, PurchaseShipmentRequest, PurchaseShipmentRequestBody,
    PurchaseShipmentResponse, PurchaseShipmentResult, Rate, RequestsBaseModel,
    RetrieveShippingLabelRequest, RetrieveShippingLabelRequestBody,
    RetrieveShippingLabelResponse, RetrieveShippingLabelResult, ServiceRate,
    Shipment, ShippingPromiseSet, SpApiBaseModel, TimeRange,
    TrackingInformation, TrackingSummary, Weight, WeightUnitEnum)


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


def test_currency_instantiates():
    """Instantiate Currency with dummy data"""
    kwargs = {
        "value": 0.0,
        "unit": "",
    }
    obj = Currency(**kwargs)
    assert isinstance(obj, Currency)


def test_timerange_instantiates():
    """Instantiate TimeRange with dummy data"""
    kwargs = {
        "start": None,
        "end": None,
    }
    obj = TimeRange(**kwargs)
    assert isinstance(obj, TimeRange)


def test_shippingpromiseset_instantiates():
    """Instantiate ShippingPromiseSet with dummy data"""
    kwargs = {
        "delivery_window": None,
        "receive_window": None,
    }
    obj = ShippingPromiseSet(**kwargs)
    assert isinstance(obj, ShippingPromiseSet)


def test_weight_instantiates():
    """Instantiate Weight with dummy data"""
    kwargs = {
        "unit": WeightUnitEnum.G,
        "value": 0.0,
    }
    obj = Weight(**kwargs)
    assert isinstance(obj, Weight)


def test_acceptedrate_instantiates():
    """Instantiate AcceptedRate with dummy data"""
    kwargs = {
        "total_charge": None,
        "billed_weight": None,
        "service_type": None,
        "promise": None,
    }
    obj = AcceptedRate(**kwargs)
    assert isinstance(obj, AcceptedRate)


def test_account_instantiates():
    """Instantiate Account with dummy data"""
    kwargs = {
        "account_id": "",
    }
    obj = Account(**kwargs)
    assert isinstance(obj, Account)


def test_address_instantiates():
    """Instantiate Address with dummy data"""
    kwargs = {
        "name": "",
        "address_line1": "",
        "address_line2": None,
        "address_line3": None,
        "state_or_region": "",
        "city": "",
        "country_code": "",
        "postal_code": "",
        "email": None,
        "copy_emails": None,
        "phone_number": None,
    }
    obj = Address(**kwargs)
    assert isinstance(obj, Address)


def test_cancelshipmentrequest_instantiates():
    """Instantiate CancelShipmentRequest with dummy data"""
    kwargs = {
        "shipment_id": "",
    }
    obj = CancelShipmentRequest(**kwargs)
    assert isinstance(obj, CancelShipmentRequest)


def test_cancelshipmentresponse_instantiates():
    """Instantiate CancelShipmentResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = CancelShipmentResponse(**kwargs)
    assert isinstance(obj, CancelShipmentResponse)


def test_containeritem_instantiates():
    """Instantiate ContainerItem with dummy data"""
    kwargs = {
        "quantity": 0.0,
        "unit_price": Currency(**{"value": 0.0, "unit": ""}),
        "unit_weight": Weight(**{"unit": WeightUnitEnum.G, "value": 0.0}),
        "title": "",
    }
    obj = ContainerItem(**kwargs)
    assert isinstance(obj, ContainerItem)


def test_dimensions_instantiates():
    """Instantiate Dimensions with dummy data"""
    kwargs = {
        "length": 0.0,
        "width": 0.0,
        "height": 0.0,
        "unit": DimensionsUnitEnum.IN,
    }
    obj = Dimensions(**kwargs)
    assert isinstance(obj, Dimensions)


def test_container_instantiates():
    """Instantiate Container with dummy data"""
    kwargs = {
        "container_type": None,
        "container_reference_id": "",
        "value": Currency(**{"value": 0.0, "unit": ""}),
        "dimensions": Dimensions(
            **{
                "length": 0.0,
                "width": 0.0,
                "height": 0.0,
                "unit": DimensionsUnitEnum.IN,
            }
        ),
        "items": [],
        "weight": Weight(**{"unit": WeightUnitEnum.G, "value": 0.0}),
    }
    obj = Container(**kwargs)
    assert isinstance(obj, Container)


def test_containerspecification_instantiates():
    """Instantiate ContainerSpecification with dummy data"""
    kwargs = {
        "dimensions": Dimensions(
            **{
                "length": 0.0,
                "width": 0.0,
                "height": 0.0,
                "unit": DimensionsUnitEnum.IN,
            }
        ),
        "weight": Weight(**{"unit": WeightUnitEnum.G, "value": 0.0}),
    }
    obj = ContainerSpecification(**kwargs)
    assert isinstance(obj, ContainerSpecification)


def test_createshipmentrequestbody_instantiates():
    """Instantiate CreateShipmentRequestBody with dummy data"""
    kwargs = {
        "client_reference_id": "",
        "ship_to": Address(
            **{
                "name": "",
                "address_line1": "",
                "address_line2": None,
                "address_line3": None,
                "state_or_region": "",
                "city": "",
                "country_code": "",
                "postal_code": "",
                "email": None,
                "copy_emails": None,
                "phone_number": None,
            }
        ),
        "ship_from": Address(
            **{
                "name": "",
                "address_line1": "",
                "address_line2": None,
                "address_line3": None,
                "state_or_region": "",
                "city": "",
                "country_code": "",
                "postal_code": "",
                "email": None,
                "copy_emails": None,
                "phone_number": None,
            }
        ),
        "containers": [],
    }
    obj = CreateShipmentRequestBody(**kwargs)
    assert isinstance(obj, CreateShipmentRequestBody)


def test_createshipmentrequest_instantiates():
    """Instantiate CreateShipmentRequest with dummy data"""
    kwargs = {
        "body": CreateShipmentRequestBody(
            **{
                "client_reference_id": "",
                "ship_to": Address(
                    **{
                        "name": "",
                        "address_line1": "",
                        "address_line2": None,
                        "address_line3": None,
                        "state_or_region": "",
                        "city": "",
                        "country_code": "",
                        "postal_code": "",
                        "email": None,
                        "copy_emails": None,
                        "phone_number": None,
                    }
                ),
                "ship_from": Address(
                    **{
                        "name": "",
                        "address_line1": "",
                        "address_line2": None,
                        "address_line3": None,
                        "state_or_region": "",
                        "city": "",
                        "country_code": "",
                        "postal_code": "",
                        "email": None,
                        "copy_emails": None,
                        "phone_number": None,
                    }
                ),
                "containers": [],
            }
        ),
    }
    obj = CreateShipmentRequest(**kwargs)
    assert isinstance(obj, CreateShipmentRequest)


def test_createshipmentresult_instantiates():
    """Instantiate CreateShipmentResult with dummy data"""
    kwargs = {
        "shipment_id": "",
        "eligible_rates": [],
    }
    obj = CreateShipmentResult(**kwargs)
    assert isinstance(obj, CreateShipmentResult)


def test_createshipmentresponse_instantiates():
    """Instantiate CreateShipmentResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = CreateShipmentResponse(**kwargs)
    assert isinstance(obj, CreateShipmentResponse)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


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
        "event_time": datetime(2000, 1, 1),
        "location": None,
    }
    obj = Event(**kwargs)
    assert isinstance(obj, Event)


def test_getaccountresponse_instantiates():
    """Instantiate GetAccountResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetAccountResponse(**kwargs)
    assert isinstance(obj, GetAccountResponse)


def test_getratesrequestbody_instantiates():
    """Instantiate GetRatesRequestBody with dummy data"""
    kwargs = {
        "ship_to": Address(
            **{
                "name": "",
                "address_line1": "",
                "address_line2": None,
                "address_line3": None,
                "state_or_region": "",
                "city": "",
                "country_code": "",
                "postal_code": "",
                "email": None,
                "copy_emails": None,
                "phone_number": None,
            }
        ),
        "ship_from": Address(
            **{
                "name": "",
                "address_line1": "",
                "address_line2": None,
                "address_line3": None,
                "state_or_region": "",
                "city": "",
                "country_code": "",
                "postal_code": "",
                "email": None,
                "copy_emails": None,
                "phone_number": None,
            }
        ),
        "service_types": [],
        "ship_date": None,
        "container_specifications": [],
    }
    obj = GetRatesRequestBody(**kwargs)
    assert isinstance(obj, GetRatesRequestBody)


def test_getratesrequest_instantiates():
    """Instantiate GetRatesRequest with dummy data"""
    kwargs = {
        "body": GetRatesRequestBody(
            **{
                "ship_to": Address(
                    **{
                        "name": "",
                        "address_line1": "",
                        "address_line2": None,
                        "address_line3": None,
                        "state_or_region": "",
                        "city": "",
                        "country_code": "",
                        "postal_code": "",
                        "email": None,
                        "copy_emails": None,
                        "phone_number": None,
                    }
                ),
                "ship_from": Address(
                    **{
                        "name": "",
                        "address_line1": "",
                        "address_line2": None,
                        "address_line3": None,
                        "state_or_region": "",
                        "city": "",
                        "country_code": "",
                        "postal_code": "",
                        "email": None,
                        "copy_emails": None,
                        "phone_number": None,
                    }
                ),
                "service_types": [],
                "ship_date": None,
                "container_specifications": [],
            }
        ),
    }
    obj = GetRatesRequest(**kwargs)
    assert isinstance(obj, GetRatesRequest)


def test_getratesresult_instantiates():
    """Instantiate GetRatesResult with dummy data"""
    kwargs = {
        "service_rates": [],
    }
    obj = GetRatesResult(**kwargs)
    assert isinstance(obj, GetRatesResult)


def test_getratesresponse_instantiates():
    """Instantiate GetRatesResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetRatesResponse(**kwargs)
    assert isinstance(obj, GetRatesResponse)


def test_getshipmentrequest_instantiates():
    """Instantiate GetShipmentRequest with dummy data"""
    kwargs = {
        "shipment_id": "",
    }
    obj = GetShipmentRequest(**kwargs)
    assert isinstance(obj, GetShipmentRequest)


def test_party_instantiates():
    """Instantiate Party with dummy data"""
    kwargs = {
        "account_id": None,
    }
    obj = Party(**kwargs)
    assert isinstance(obj, Party)


def test_shipment_instantiates():
    """Instantiate Shipment with dummy data"""
    kwargs = {
        "shipment_id": "",
        "client_reference_id": "",
        "ship_from": Address(
            **{
                "name": "",
                "address_line1": "",
                "address_line2": None,
                "address_line3": None,
                "state_or_region": "",
                "city": "",
                "country_code": "",
                "postal_code": "",
                "email": None,
                "copy_emails": None,
                "phone_number": None,
            }
        ),
        "ship_to": Address(
            **{
                "name": "",
                "address_line1": "",
                "address_line2": None,
                "address_line3": None,
                "state_or_region": "",
                "city": "",
                "country_code": "",
                "postal_code": "",
                "email": None,
                "copy_emails": None,
                "phone_number": None,
            }
        ),
        "accepted_rate": None,
        "shipper": None,
        "containers": [],
    }
    obj = Shipment(**kwargs)
    assert isinstance(obj, Shipment)


def test_getshipmentresponse_instantiates():
    """Instantiate GetShipmentResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetShipmentResponse(**kwargs)
    assert isinstance(obj, GetShipmentResponse)


def test_gettrackinginformationrequest_instantiates():
    """Instantiate GetTrackingInformationRequest with dummy data"""
    kwargs = {
        "tracking_id": "",
    }
    obj = GetTrackingInformationRequest(**kwargs)
    assert isinstance(obj, GetTrackingInformationRequest)


def test_trackingsummary_instantiates():
    """Instantiate TrackingSummary with dummy data"""
    kwargs = {
        "status": None,
    }
    obj = TrackingSummary(**kwargs)
    assert isinstance(obj, TrackingSummary)


def test_trackinginformation_instantiates():
    """Instantiate TrackingInformation with dummy data"""
    kwargs = {
        "tracking_id": "",
        "summary": TrackingSummary(**{"status": None}),
        "promised_delivery_date": "",
        "event_history": [],
    }
    obj = TrackingInformation(**kwargs)
    assert isinstance(obj, TrackingInformation)


def test_gettrackinginformationresponse_instantiates():
    """Instantiate GetTrackingInformationResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetTrackingInformationResponse(**kwargs)
    assert isinstance(obj, GetTrackingInformationResponse)


def test_labelspecification_instantiates():
    """Instantiate LabelSpecification with dummy data"""
    kwargs = {
        "label_format": LabelSpecificationLabelFormatEnum.PNG,
        "label_stock_size": LabelSpecificationLabelStockSizeEnum.VALUE_4X6,
    }
    obj = LabelSpecification(**kwargs)
    assert isinstance(obj, LabelSpecification)


def test_label_instantiates():
    """Instantiate Label with dummy data"""
    kwargs = {
        "label_stream": None,
        "label_specification": None,
    }
    obj = Label(**kwargs)
    assert isinstance(obj, Label)


def test_labelresult_instantiates():
    """Instantiate LabelResult with dummy data"""
    kwargs = {
        "container_reference_id": None,
        "tracking_id": None,
        "label": None,
    }
    obj = LabelResult(**kwargs)
    assert isinstance(obj, LabelResult)


def test_purchaselabelsrequestbody_instantiates():
    """Instantiate PurchaseLabelsRequestBody with dummy data"""
    kwargs = {
        "rate_id": "",
        "label_specification": LabelSpecification(
            **{
                "label_format": LabelSpecificationLabelFormatEnum.PNG,
                "label_stock_size": LabelSpecificationLabelStockSizeEnum.VALUE_4X6,
            }
        ),
    }
    obj = PurchaseLabelsRequestBody(**kwargs)
    assert isinstance(obj, PurchaseLabelsRequestBody)


def test_purchaselabelsrequest_instantiates():
    """Instantiate PurchaseLabelsRequest with dummy data"""
    kwargs = {
        "shipment_id": "",
        "body": PurchaseLabelsRequestBody(
            **{
                "rate_id": "",
                "label_specification": LabelSpecification(
                    **{
                        "label_format": LabelSpecificationLabelFormatEnum.PNG,
                        "label_stock_size": LabelSpecificationLabelStockSizeEnum.VALUE_4X6,
                    }
                ),
            }
        ),
    }
    obj = PurchaseLabelsRequest(**kwargs)
    assert isinstance(obj, PurchaseLabelsRequest)


def test_purchaselabelsresult_instantiates():
    """Instantiate PurchaseLabelsResult with dummy data"""
    kwargs = {
        "shipment_id": "",
        "client_reference_id": None,
        "accepted_rate": AcceptedRate(
            **{
                "total_charge": None,
                "billed_weight": None,
                "service_type": None,
                "promise": None,
            }
        ),
        "label_results": [],
    }
    obj = PurchaseLabelsResult(**kwargs)
    assert isinstance(obj, PurchaseLabelsResult)


def test_purchaselabelsresponse_instantiates():
    """Instantiate PurchaseLabelsResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = PurchaseLabelsResponse(**kwargs)
    assert isinstance(obj, PurchaseLabelsResponse)


def test_purchaseshipmentrequestbody_instantiates():
    """Instantiate PurchaseShipmentRequestBody with dummy data"""
    kwargs = {
        "client_reference_id": "",
        "ship_to": Address(
            **{
                "name": "",
                "address_line1": "",
                "address_line2": None,
                "address_line3": None,
                "state_or_region": "",
                "city": "",
                "country_code": "",
                "postal_code": "",
                "email": None,
                "copy_emails": None,
                "phone_number": None,
            }
        ),
        "ship_from": Address(
            **{
                "name": "",
                "address_line1": "",
                "address_line2": None,
                "address_line3": None,
                "state_or_region": "",
                "city": "",
                "country_code": "",
                "postal_code": "",
                "email": None,
                "copy_emails": None,
                "phone_number": None,
            }
        ),
        "ship_date": None,
        "service_type": "",
        "containers": [],
        "label_specification": LabelSpecification(
            **{
                "label_format": LabelSpecificationLabelFormatEnum.PNG,
                "label_stock_size": LabelSpecificationLabelStockSizeEnum.VALUE_4X6,
            }
        ),
    }
    obj = PurchaseShipmentRequestBody(**kwargs)
    assert isinstance(obj, PurchaseShipmentRequestBody)


def test_purchaseshipmentrequest_instantiates():
    """Instantiate PurchaseShipmentRequest with dummy data"""
    kwargs = {
        "body": PurchaseShipmentRequestBody(
            **{
                "client_reference_id": "",
                "ship_to": Address(
                    **{
                        "name": "",
                        "address_line1": "",
                        "address_line2": None,
                        "address_line3": None,
                        "state_or_region": "",
                        "city": "",
                        "country_code": "",
                        "postal_code": "",
                        "email": None,
                        "copy_emails": None,
                        "phone_number": None,
                    }
                ),
                "ship_from": Address(
                    **{
                        "name": "",
                        "address_line1": "",
                        "address_line2": None,
                        "address_line3": None,
                        "state_or_region": "",
                        "city": "",
                        "country_code": "",
                        "postal_code": "",
                        "email": None,
                        "copy_emails": None,
                        "phone_number": None,
                    }
                ),
                "ship_date": None,
                "service_type": "",
                "containers": [],
                "label_specification": LabelSpecification(
                    **{
                        "label_format": LabelSpecificationLabelFormatEnum.PNG,
                        "label_stock_size": LabelSpecificationLabelStockSizeEnum.VALUE_4X6,
                    }
                ),
            }
        ),
    }
    obj = PurchaseShipmentRequest(**kwargs)
    assert isinstance(obj, PurchaseShipmentRequest)


def test_servicerate_instantiates():
    """Instantiate ServiceRate with dummy data"""
    kwargs = {
        "total_charge": Currency(**{"value": 0.0, "unit": ""}),
        "billable_weight": Weight(**{"unit": WeightUnitEnum.G, "value": 0.0}),
        "service_type": "",
        "promise": ShippingPromiseSet(
            **{"delivery_window": None, "receive_window": None}
        ),
    }
    obj = ServiceRate(**kwargs)
    assert isinstance(obj, ServiceRate)


def test_purchaseshipmentresult_instantiates():
    """Instantiate PurchaseShipmentResult with dummy data"""
    kwargs = {
        "shipment_id": "",
        "service_rate": ServiceRate(
            **{
                "total_charge": Currency(**{"value": 0.0, "unit": ""}),
                "billable_weight": Weight(**{"unit": WeightUnitEnum.G, "value": 0.0}),
                "service_type": "",
                "promise": ShippingPromiseSet(
                    **{"delivery_window": None, "receive_window": None}
                ),
            }
        ),
        "label_results": [],
    }
    obj = PurchaseShipmentResult(**kwargs)
    assert isinstance(obj, PurchaseShipmentResult)


def test_purchaseshipmentresponse_instantiates():
    """Instantiate PurchaseShipmentResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = PurchaseShipmentResponse(**kwargs)
    assert isinstance(obj, PurchaseShipmentResponse)


def test_rate_instantiates():
    """Instantiate Rate with dummy data"""
    kwargs = {
        "rate_id": None,
        "total_charge": None,
        "billed_weight": None,
        "expiration_time": None,
        "service_type": None,
        "promise": None,
    }
    obj = Rate(**kwargs)
    assert isinstance(obj, Rate)


def test_retrieveshippinglabelrequestbody_instantiates():
    """Instantiate RetrieveShippingLabelRequestBody with dummy data"""
    kwargs = {
        "label_specification": LabelSpecification(
            **{
                "label_format": LabelSpecificationLabelFormatEnum.PNG,
                "label_stock_size": LabelSpecificationLabelStockSizeEnum.VALUE_4X6,
            }
        ),
    }
    obj = RetrieveShippingLabelRequestBody(**kwargs)
    assert isinstance(obj, RetrieveShippingLabelRequestBody)


def test_retrieveshippinglabelrequest_instantiates():
    """Instantiate RetrieveShippingLabelRequest with dummy data"""
    kwargs = {
        "shipment_id": "",
        "tracking_id": "",
        "body": RetrieveShippingLabelRequestBody(
            **{
                "label_specification": LabelSpecification(
                    **{
                        "label_format": LabelSpecificationLabelFormatEnum.PNG,
                        "label_stock_size": LabelSpecificationLabelStockSizeEnum.VALUE_4X6,
                    }
                )
            }
        ),
    }
    obj = RetrieveShippingLabelRequest(**kwargs)
    assert isinstance(obj, RetrieveShippingLabelRequest)


def test_retrieveshippinglabelresult_instantiates():
    """Instantiate RetrieveShippingLabelResult with dummy data"""
    kwargs = {
        "label_stream": "",
        "label_specification": LabelSpecification(
            **{
                "label_format": LabelSpecificationLabelFormatEnum.PNG,
                "label_stock_size": LabelSpecificationLabelStockSizeEnum.VALUE_4X6,
            }
        ),
    }
    obj = RetrieveShippingLabelResult(**kwargs)
    assert isinstance(obj, RetrieveShippingLabelResult)


def test_retrieveshippinglabelresponse_instantiates():
    """Instantiate RetrieveShippingLabelResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = RetrieveShippingLabelResponse(**kwargs)
    assert isinstance(obj, RetrieveShippingLabelResponse)
