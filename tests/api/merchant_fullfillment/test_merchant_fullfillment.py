from sp_api.api.merchant_fulfillment.merchant_fulfillment import MerchantFulfillment
from sp_api.base import SellingApiServerException, SellingApiForbiddenException

def test_get_eligible_shipment_services_old():
    res = MerchantFulfillment().get_eligible_shipment_services_old({
            "AmazonOrderId": "903-5563053-5647845",
            "ItemList": [
                {
                    "OrderItemId": "52986411826454",
                    "Quantity": 1
                }
            ],
            "ShipFromAddress": {
                "Name": "John Doe",
                "AddressLine1": "300 Turnbull Ave",
                "Email": "jdoeasdfllkj@yahoo.com",
                "City": "Detroit",
                "StateOrProvinceCode": "MI",
                "PostalCode": "48123",
                "CountryCode": "US",
                "Phone": "7132341234"
            },
            "PackageDimensions": {
                "Length": 10,
                "Width": 10,
                "Height": 10,
                "Unit": "inches"
            },
            "Weight": {
                "Value": 10,
                "Unit": "oz"
            },
            "ShippingServiceOptions": {
                "DeliveryExperience": "NoTracking",
                "CarrierWillPickUp": False,
                "CarrierWillPickUpOption": "ShipperWillDropOff"
            }
    })
    assert res.errors is None
    assert res.payload.get('ShippingServiceList') is not None


def test_get_eligible_shipment_services():
    res = MerchantFulfillment().get_eligible_shipment_services({
          "AmazonOrderId": "903-5563053-5647845",
          "ItemList": [
            {
              "OrderItemId": "52986411826454",
              "Quantity": 1
            }
          ],
          "ShipFromAddress": {
            "Name": "John Doe",
            "AddressLine1": "300 Turnbull Ave",
            "Email": "jdoeasdfllkj@yahoo.com",
            "City": "Detroit",
            "StateOrProvinceCode": "MI",
            "PostalCode": "48123",
            "CountryCode": "US",
            "Phone": "7132341234"
          },
          "PackageDimensions": {
            "Length": 10,
            "Width": 10,
            "Height": 10,
            "Unit": "inches"
          },
          "Weight": {
            "Value": 10,
            "Unit": "oz"
          },
          "ShippingServiceOptions": {
            "DeliveryExperience": "NoTracking",
            "CarrierWillPickUp": False,
            "CarrierWillPickUpOption": "ShipperWillDropOff"
          }
    })
    assert res.errors is None
    assert res.payload.get('ShippingServiceList') is not None


def test_get_shipment():
    res = MerchantFulfillment().get_shipment("abcddcba-00c3-4f6f-a63a-639f76ee9253")
    assert res.errors is None
    assert res.payload.get('ShipmentId') == "abcddcba-00c3-4f6f-a63a-639f76ee9253"


def test_cancel_shipment():
    res = MerchantFulfillment().cancel_shipment("be7a0a53-00c3-4f6f-a63a-639f76ee9253")
    assert res.errors is None
    assert res.payload.get('ShipmentId') == "be7a0a53-00c3-4f6f-a63a-639f76ee9253"

def test_cancel_shipment_old():
    res = MerchantFulfillment().cancel_shipment_old("be7a0a53-00c3-4f6f-a63a-639f76ee9253")
    assert res.errors is None
    assert res.payload.get('ShipmentId') == "be7a0a53-00c3-4f6f-a63a-639f76ee9253"

def test_create_shipment():
    res = MerchantFulfillment().create_shipment(
        shipment_request_details={
            "AmazonOrderId": "903-5563053-5647845",
            "ItemList": [
                {
                    "OrderItemId": "52986411826454",
                    "Quantity": 1
                }
            ],
            "ShipFromAddress": {
                "Name": "John Doe",
                "AddressLine1": "300 Turnbull Ave",
                "Email": "jdoeasdfllkj@yahoo.com",
                "City": "Detroit",
                "StateOrProvinceCode": "MI",
                "PostalCode": "48123",
                "CountryCode": "US",
                "Phone": "7132341234"
            },
            "PackageDimensions": {
                "Length": 10,
                "Width": 10,
                "Height": 10,
                "Unit": "inches"
            },
            "Weight": {
                "Value": 10,
                "Unit": "oz"
            },
            "ShippingServiceOptions": {
                "DeliveryExperience": "NoTracking",
                "CarrierWillPickUp": False,
                "CarrierWillPickUpOption": "ShipperWillDropOff"
            }
        },
        shipping_service_id="UPS_PTP_2ND_DAY_AIR",
        ShippingServiceOfferId="WHgxtyn6qjGGaCzOCog1azF5HLHje5Pz3Lc2Fmt5eKoZAReW8oJ1SMumuBS8lA/Hjuglhyiu0"
                               "+KRLvyJxFV0PB9YFMDhygs3VyTL0WGYkGxiuRkmuEvpqldUn9rrkWVodqnR4vx2VtXvtER"
                               "/Ju6RqYoddJZGy6RS2KLzzhQ2NclN0NYXMZVqpOe5RsRBddXaGuJr7oza3M52"
                               "+JzChocAHzcurIhCRynpbxfmNLzZMQEbgnpGLzuaoSMzfxg90/NaXFR/Ou01du/uKd5AbfMW"
                               "/AxAKP9ht6Oi9lDHq6WkGqvjkVLW0/jj/fBgblIwcs+t "
    )
    assert res.errors is None
    assert res.payload.get('ShipmentId') == "be7a0a53-00c3-4f6f-a63a-639f76ee9253"


def test_get_additional_seller_inputs_old():
    res = MerchantFulfillment().get_additional_seller_inputs_old(
        shipping_service_id="UPS_PTP_GND",
        ship_from_address={
            "Name": "John Doe",
            "AddressLine1": "300 Turnbull Ave",
            "Email": "jdoeasdfllkj@yahoo.com",
            "City": "Detroit",
            "StateOrProvinceCode": "MI",
            "PostalCode": "48123",
            "CountryCode": "US",
            "Phone": "7132341234"
        },
        order_id="903-5563053-5647845",
    )
    assert res.errors is None
    assert res.payload.get('ShipmentLevelFields') is not None


def test_get_additional_seller_inputs():
    res = MerchantFulfillment().get_additional_seller_inputs(
        shipping_service_id="UPS_PTP_GND",
        ship_from_address={
            "Name": "John Doe",
            "AddressLine1": "300 Turnbull Ave",
            "Email": "jdoeasdfllkj@yahoo.com",
            "City": "Detroit",
            "StateOrProvinceCode": "MI",
            "PostalCode": "48123",
            "CountryCode": "US",
            "Phone": "7132341234"
        },
        order_id="903-5563053-5647845",
    )
    assert res.errors is None
    assert res.payload.get('ShipmentLevelFields') is not None
