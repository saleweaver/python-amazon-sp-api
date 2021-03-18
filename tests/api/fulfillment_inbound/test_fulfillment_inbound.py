from datetime import datetime, timedelta

from sp_api.api import FulfillmentInbound


def test_item_guidance():
    res = FulfillmentInbound().item_guidance(SellerSKUList=','.join(["sku1", "sku2"]), MarketplaceId='MarketplaceId')
    assert res.errors is None


def test_plans():
    res = FulfillmentInbound().plans({
        "ShipFromAddress": {
            "Name": "Name",
            "AddressLine1": "123 any st",
            "AddressLine2": "AddressLine2",
            "DistrictOrCounty": "Washtenaw",
            "City": "Ann Arbor",
            "StateOrProvinceCode": "MI",
            "CountryCode": "US",
            "PostalCode": "48188"
        },
        "LabelPrepPreference": "SELLER_LABEL",
        "ShipToCountryCode": "ShipToCountryCode",
        "ShipToCountrySubdivisionCode": "ShipToCountrySubdivisionCode",
        "InboundShipmentPlanRequestItems": [
            {
                "SellerSKU": "SellerSKU",
                "ASIN": "ASIN",
                "Condition": "NewItem",
                "Quantity": 1,
                "QuantityInCase": 1,
                "PrepDetailsList": [
                    {
                        "PrepInstruction": "Polybagging",
                        "PrepOwner": "AMAZON"
                    }
                ]
            }
        ]
    })
    assert res.errors is None


def test_create_inbound_shipment():
    res = FulfillmentInbound().create_shipment('123', {
        "InboundShipmentHeader": {
            "ShipmentName": "43545345",
            "ShipFromAddress": {
                "Name": "35435345",
                "AddressLine1": "123 any st",
                "DistrictOrCounty": "Washtenaw",
                "City": "Ann Arbor",
                "StateOrProvinceCode": "Test",
                "CountryCode": "US",
                "PostalCode": "48103"
            },
            "DestinationFulfillmentCenterId": "AEB2",
            "AreCasesRequired": True,
            "ShipmentStatus": "WORKING",
            "LabelPrepPreference": "SELLER_LABEL",
            "IntendedBoxContentsSource": "NONE"
        },
        "InboundShipmentItems": [
            {
                "ShipmentId": "345453",
                "SellerSKU": "34534545",
                "FulfillmentNetworkSKU": "435435435",
                "QuantityShipped": 0,
                "QuantityReceived": 0,
                "QuantityInCase": 0,
                "ReleaseDate": "2020-04-23",
                "PrepDetailsList": [
                    {
                        "PrepInstruction": "Polybagging",
                        "PrepOwner": "AMAZON"
                    }
                ]
            }
        ],
        "MarketplaceId": "MarketplaceId"
    })
    assert res.errors is None


def test_update_shipment():
    res = FulfillmentInbound().update_shipment('123', {
        "MarketplaceId": "ATVPDKIKX0DER",
        "InboundShipmentHeader": {
            "ShipmentName": "Shipment for FBA15DJCQ1ZF",
            "ShipFromAddress": {
                "Name": "Uma Test",
                "AddressLine1": "123 any st",
                "AddressLine2": "",
                "DistrictOrCounty": "Washtenaw",
                "City": "Ann Arbor",
                "StateOrProvinceCode": "CO",
                "CountryCode": "US",
                "PostalCode": "48104"
            },
            "DestinationFulfillmentCenterId": "ABE2",
            "ShipmentStatus": "WORKING",
            "LabelPrepPreference": "SELLER_LABEL"
        },
        "InboundShipmentItems": [
            {
                "SellerSKU": "PSMM-TEST-SKU-Apr-03_21_17_20-0379",
                "QuantityShipped": 1
            }
        ]
    })
    assert res.errors is None


def test_preorder():
    res = FulfillmentInbound().preorder('shipmentId1', MarketplaceId='MarketplaceId1')
    assert res.errors is None

#
# def test_confirm_preorder():
#     res = FulfillmentInbound().confirm_preorder('shipmentId1', **{
#         "NeedByDate": "2020-10-10",
#         "MarketplaceId": "MarketplaceId1"
#     })
#     assert res.errors is None


def test_get_prep_orders():
    res = FulfillmentInbound().prep_instruction({"ShipToCountryCode": "US", "ASINList": ["ASIN1"]})
    assert res.errors is None


def test_get_transport():
    res = FulfillmentInbound().get_transport_information('shipmentId1')
    assert res.errors is None


def test_void_transport():
    res = FulfillmentInbound().void_transport('shipmentId1')
    assert res.errors is None


def test_estimate_transport():
    res = FulfillmentInbound().estimate_transport('shipmentId1')
    assert res.errors is None


def test_get_bill_of_lading():
    res = FulfillmentInbound().bill_of_lading('shipmentId')
    assert res.errors is None


def test_get_shipments():
    res = FulfillmentInbound().get_shipments(QueryType='SHIPMENT', MarketplaceId="ATVPDKIKX0DER")
    assert res.errors is None


def test_get_shipment_items():
    res = FulfillmentInbound().shipment_items_by_shipment('FBA15DJ9SVVD', MarketplaceId="ATVPDKIKX0DER")
    assert res.errors is None


def test_get_items():
    res = FulfillmentInbound().shipment_items(QueryType='SHIPMENT', MarketplaceId="ATVPDKIKX0DER", NextToken='NextToken')
    assert res.errors is None
