import pytest

from sp_api.api.shipping.shippingV2 import Shipping, AmznShippingBusiness
from sp_api.base import SellingApiBadRequestException


def test_get_rates():
    res = Shipping(amzn_shipping_business=AmznShippingBusiness.UK).get_rates(
        **{
            "shipTo": {
                "name": "Arlene Purdy",
                "addressLine1": "8076 Armstrong Extensions",
                "city": "South Kristopherborough",
                "countryCode": "UK",
                "postalCode": "NW10 0TL",
                "email": "buyer@test.com",
                "phoneNumber": "700-008-5275",
            },
            "shipFrom": {
                "name": "Orville Miller I",
                "addressLine1": "16063 Daugherty Throughway",
                "city": "Connland",
                "countryCode": "UK",
                "postalCode": "NW10 0TL",
                "email": "seller@test.com",
                "phoneNumber": "662-302-7817",
            },
            "shipperInstruction": {
                "deliveryNotes": "TEST"
            },
            "packages": [
                {
                    "dimensions": {
                        "length": 30,
                        "width": 10,
                        "height": 10,
                        "unit": "CENTIMETER"
                    },
                    "weight": {
                        "unit": "KILOGRAM",
                        "value": 1.00,
                    },
                    "insuredValue": {
                        "value": 0.00,
                        "unit": "EUR",
                    },
                    "sellerDisplayName": "SELLER_NAME",
                    "packageClientReferenceId": "PACKAGE_ID_1",
                    "items": [
                        {
                            "description": "ITEM_1",
                            "quantity": 1,
                            "weight": {
                                "value": 1.00,
                                "unit": "KILOGRAM",
                            },
                        }
                    ]
                }
            ],
            "channelDetails": {
                "channelType": "EXTERNAL",
            },
            "shipmentType": "FORWARD",
        }
    )
    assert res.errors is None
    assert res.payload.get('requestToken') is not None
    assert len(res.payload.get('rates')) > 0


def test_get_additional_inputs_empty():
    res = Shipping().get_additional_inputs(
        **{
            "requestToken": "amzn1.rq.123456789.101",
            "rateId": "122324234543535321345436534321423423523452345"
        }
    )
    assert res.errors is None
    assert res.payload == {}


def test_get_additional_inputs_invalid():
    try:
        res = Shipping().get_additional_inputs(
            **{
                "requestToken": "null",
                "rateId": "2314346237423894905834905890346890789075"
            }
        )
    except SellingApiBadRequestException as br:
        assert br.code == 400
        assert type(br) == SellingApiBadRequestException
        assert br.error[0]["details"] == "RequestToken cannot be null"


def test_get_tracking():
    res = Shipping().get_tracking(
        **{
            "trackingId": "23AA47DE2B3B6",
            "carrierId": "AMZN_UK",
        }
    )
    assert res.errors is None
    assert res.payload.get("trackingId") == "23AA47DE2B3B6"
    assert res.payload.get("summary").get("status") == "Delivered"
    assert len(res.payload.get("eventHistory")) > 0


def test_cancel_shipment_not_found():
    try:
        res = Shipping().cancel_shipment("TEST_CASE_400")
        assert res.errors is None
    except SellingApiBadRequestException as br:
        assert br.code == 400
        assert type(br) == SellingApiBadRequestException
        assert br.error[0]["details"] == "Shipment not found for specified shipmentId"


def test_get_shipment_documents():
    try:
        res = Shipping().get_shipment_documents(
            "445454-3232-3232",
            packageClientReferenceId="ASUSDI-45343854"
        )
        assert res.errors is None
    except SellingApiBadRequestException as br:
        assert br.code == 400
        assert type(br) == SellingApiBadRequestException
        assert br.error[0]["details"] == "Shipment not found for specified shipmentId"


def test_purchase_shipment():
    try:
        res = Shipping().purchase_shipment(
            **{
                "requestToken": "amzn1.rq.123456789.101",
                "rateId": "122324234543535321345436534321423423523452345",
                "requestedDocumentSpecification": {
                    "format": "ZPL",
                    "size": {
                        "width": 4,
                        "length": 6,
                        "unit": "INCH"
                    },
                    "dpi": 203,
                    "pageLayout": "DEFAULT",
                    "needFileJoining": False,
                    "requestedDocumentTypes": ["LABEL"]
                }
            }
        )
        assert res.errors is None
    except SellingApiBadRequestException as br:
        assert br.code == 400
        assert type(br) == SellingApiBadRequestException
        assert br.error[0]["details"] == "Request not found for specified requestToken"


def test_submit_ndr_feedback():
    res = Shipping().submit_ndr_feedback(
        **{
            "trackingId": "TEST_CASE_200",
            "ndrAction": "RESCHEDULE",
            "ndrRequestData": {
                "rescheduleDate": "2024-12-12T05:24:00.00Z",
                "additionalAddressNotes": "string"
            }
        }
    )
    assert res.errors is None


def test_get_access_points():
    res = Shipping().get_access_points(
        **{
            "accessPointTypes": "HELIX",
            "countryCode": "UK",
            "postalCode": "EX332JL"
        }
    )
    assert res.errors is None


def test_one_click_shipment():
    res = Shipping(amzn_shipping_business=AmznShippingBusiness.UK).one_click_shipment(
        **{
            "shipTo": {
                "name": "Arlene Purdy",
                "addressLine1": "8076 Armstrong Extensions",
                "city": "South Kristopherborough",
                "countryCode": "UK",
                "postalCode": "NW10 0TL",
                "email": "buyer@test.com",
                "phoneNumber": "700-008-5275",
            },
            "shipFrom": {
                "name": "Orville Miller I",
                "addressLine1": "16063 Daugherty Throughway",
                "city": "Connland",
                "countryCode": "UK",
                "postalCode": "NW10 0TL",
                "email": "seller@test.com",
                "phoneNumber": "662-302-7817",
            },
            "shipperInstruction": {
                "deliveryNotes": "TEST"
            },
            "packages": [
                {
                    "dimensions": {
                        "length": 30,
                        "width": 10,
                        "height": 10,
                        "unit": "CENTIMETER"
                    },
                    "weight": {
                        "unit": "KILOGRAM",
                        "value": 1.00,
                    },
                    "insuredValue": {
                        "value": 0.00,
                        "unit": "EUR",
                    },
                    "sellerDisplayName": "SELLER_NAME",
                    "packageClientReferenceId": "PACKAGE_ID_1",
                    "items": [
                        {
                            "description": "ITEM_1",
                            "quantity": 1,
                            "weight": {
                                "value": 1.00,
                                "unit": "KILOGRAM",
                            },
                        }
                    ]
                }
            ],
            "channelDetails": {
                "channelType": "EXTERNAL",
            },
            "labelSpecifications": {
                "format": "ZPL",
                "size": {
                    "width": 4,
                    "length": 6,
                    "unit": "INCH"
                },
                "dpi": 203,
                "pageLayout": "DEFAULT",
                "needFileJoining": False,
                "requestedDocumentTypes": ["LABEL"]
            },
            "serviceSelection": {
                "serviceId": ["SWA-UK-PREM"]
            },
        }
    )
    assert res.errors is None
    assert res.payload.get('shipmentId')
    assert res.payload.get('packageDocumentDetails')[0]['trackingId']
    assert len(res.payload.get('packageDocumentDetails')[0]['packageDocuments']) > 0
