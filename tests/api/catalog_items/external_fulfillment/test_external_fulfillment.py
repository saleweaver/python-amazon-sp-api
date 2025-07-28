from sp_api.api.external_fulfillment.external_fulfillment import ExternalFulfillment
from sp_api.base import SellingApiBadRequestException


def test_get_shipments():
    res = ExternalFulfillment().get_shipments(
        **{
            "locationId": "TEST_CASE_200_LOCATION_ID",
            "status": "CONFIRMED",
            "maxResults": 2,
        }
    )
    assert res.errors is None
    assert res.payload.get("shipments") is not None
    assert len(res.payload.get("shipments")) == 2


def test_get_shipments_error():
    try:
        res = ExternalFulfillment().get_shipments()
        assert res.errors is None
    except SellingApiBadRequestException as br:
        assert br.code == 400
        assert type(br) == SellingApiBadRequestException
        assert br.message == "Missing or invalid request parameters: [status]"
        assert br.amzn_code == "InvalidInput"


def test_get_shipment():
    res = ExternalFulfillment().get_shipment(
        "TEST_CASE_200_FBA_SHIPMENT_ID"
    )

    assert res.errors is None
    assert res.payload.get("locationId") == "ABCD"


def test_process_shipment_confirm():
    res = ExternalFulfillment().process_shipment(
        "TEST_CASE_200_FBA_SHIPMENT_ID",
        "CONFIRM"
    )

    assert res.errors is None


def test_process_shipment_out_stock():
    res = ExternalFulfillment().process_shipment(
        "TEST_CASE_200_FBA_SHIPMENT_ID",
        "REJECT",
        **{
            "referenceId": "cancellation-reference-identifier1",
            "lineItems": [
                {
                    "lineItem": {
                        "id": "1",
                        "quantity": 0
                    },
                    "reason": "OUT_OF_STOCK"
                }
            ]
        }
    )

    assert res.errors is None


def test_create_packages_fba():
    res = ExternalFulfillment().create_packages(
        "TEST_CASE_200_FBA_SHIPMENT_ID",
        **{
            "packages": []
        }
    )

    assert res.errors is None


def test_create_packages_mfn():
    res = ExternalFulfillment().create_packages(
        "TEST_CASE_200_MFN_SHIPMENT_ID",
        **{
            "packages": []
        }
    )

    assert res.errors is None


def test_update_package_fba():
    res = ExternalFulfillment().update_package(
        "TEST_CASE_200_FBA_SHIPMENT_ID",
        "TEST_CASE_200_PACKAGE_ID",
        **{
            "packages": []
        }
    )

    assert res.errors is None


def test_update_package_mfn():
    res = ExternalFulfillment().update_package(
        "TEST_CASE_200_MFN_SHIPMENT_ID",
        "TEST_CASE_200_PACKAGE_ID",
        **{
            "packages": []
        }
    )

    assert res.errors is None


def test_update_package_status():
    res = ExternalFulfillment().update_package_status(
        "TEST_CASE_200_MFN_SHIPMENT_ID",
        "TEST_CASE_200_PACKAGE_ID",
        **{
            "status": "SHIPPED"
        }
    )

    assert res.errors is None


def test_generate_invoice():
    res = ExternalFulfillment().generate_invoice(
        "TEST_CASE_200_FBA_SHIPMENT_ID"
    )

    assert res.errors is None
    assert res.payload.get("document").get("format") == "PDF"
    assert res.payload.get("document").get("content") is not None


def test_retrieve_invoice():
    res = ExternalFulfillment().retrieve_invoice(
        "TEST_CASE_200_FBA_SHIPMENT_ID"
    )

    assert res.errors is None
    assert res.payload.get("document").get("format") == "PDF"
    assert res.payload.get("document").get("content") is not None


def test_retrieve_shipping_options_mfn():
    res = ExternalFulfillment().retrieve_shipping_options(
        "TEST_CASE_200_MFN_SHIPMENT_ID",
        "TEST_CASE_200_PACKAGE_ID"
    )
    assert res.errors is None
    assert res.payload.get("shippingOptions") is not None
    assert len(res.payload.get("shippingOptions")) == 1
    assert res.payload.get("recommendedShippingOption") is not None


def test_retrieve_shipping_options_fba():
    res = ExternalFulfillment().retrieve_shipping_options(
        "TEST_CASE_200_FBA_SHIPMENT_ID",
        "TEST_CASE_200_PACKAGE_ID"
    )
    assert res.errors is None
    assert len(res.payload.get("shippingOptions")) == 0


def test_generate_ship_labels():
    res = ExternalFulfillment().generate_ship_labels(
        "TEST_CASE_200_FBA_SHIPMENT_ID",
        "GENERATE",
        **{
            "packageIds": [
                "TEST_CASE_200_PACKAGE_ID"
            ],
            "courierSupportedAttributes": {
                "carrierName": "ATS",
                "trackingId": "151958276037"
            }
        }
    )

    assert res.errors is None
    assert res.payload.get("packageShipLabelList") is not None
    assert len(res.payload.get("packageShipLabelList")) == 1


def test_generate_ship_labels_with_shipping_option():
    res = ExternalFulfillment().generate_ship_labels(
        "TEST_CASE_200_MFN_SHIPMENT_ID",
        "GENERATE",
        shippingOptionId="TEST_CASE_200_SHIPPING_OPTION_ID",
        **{
            "packageIds": [
                "TEST_CASE_200_PACKAGE_ID"
            ],
            "courierSupportedAttributes": {
                "carrierName": "ATSPL",
                "trackingId": "343284200328"
            }
        }
    )

    assert res.errors is None
    assert res.payload.get("packageShipLabelList") is not None
    assert len(res.payload.get("packageShipLabelList")) == 1


def test_retrieve_ship_label():
    res = ExternalFulfillment().retrieve_ship_label(
        "TEST_CASE_200_MFN_SHIPMENT_ID",
        "TEST_CASE_200_PACKAGE_ID"
    )

    assert res.errors is None
    assert res.payload.get("document") is not None
    assert res.payload.get("document").get("content") is not None


def test_list_returns():
    res = ExternalFulfillment().list_returns(
        **{
            "rmaId": "rmaIdOneShipmentOneItemOneQty200"
        }
    )

    assert res.errors is None
    assert len(res.payload.get("returns", [])) >= 0


def test_list_returns_by_return_location():
    res = ExternalFulfillment().list_returns(
        **{
            "returnLocationId": "testReturnLocationId",
            "status": "CREATED",
            "lastUpdatedAfter": "2021-03-20T00:00:00Z"
        }
    )

    assert res.errors is None
    assert len(res.payload.get("returns", [])) >= 0


def test_get_return():
    res = ExternalFulfillment().get_return(
        "rmaIdOneShipmentOneItemOneQty200"
    )

    assert res.errors is None
    assert res.payload.get("id") == "rmaIdOneShipmentOneItemOneQty200"


def test_process_return_item():
    res = ExternalFulfillment().process_return_item(
        "ee39cdd9-9caa-47b6-a5b1-7b6a1c6d43d1",
        **{
            "op": "increment",
            "path": "/processedReturns",
            "value": {
                "Sellable": 1
            }
        }
    )

    assert res.errors is None


def test_update_inventory():
    res = ExternalFulfillment().update_inventory(
    "43cd8cd4-a944-4fa8-a584-5e3b3efdb045",
    "efptestsku2",
    15
    )

    assert res.errors is None
    assert res.payload.get("sellableQuantity") == 15


def test_get_inventory():
    res = ExternalFulfillment().get_inventory(
    "43cd8cd4-a944-4fa8-a584-5e3b3efdb045",
    "efptestsku2"
    )

    assert res.errors is None
    assert res.payload.get("sellableQuantity") == 15


def test_batch_inventory():
    res = ExternalFulfillment().batch_inventory(
        ** {
            "requests": [
                {
                    "method": "POST",
                    "uri": "/inventory/update?locationId=EXSB&skuId=efptestsku1",
                    "body": {
                        "quantity": 15,
                        "clientSequenceNumber": 12345678,
                        "marketplaceAttributes": {
                            "marketplaceId": "AXJDDKDFDKDF",
                            "channelName": "FBA"
                        }
                    }
                },
                {
                    "method": "POST",
                    "uri": "/inventory/fetch?locationId=EXSB&skuId=efptestsku2",
                    "body": {
                        "marketplaceAttributes": {
                            "marketplaceId": "AXJDDKDFDKDF",
                            "channelName": "FBA"
                        }
                    }
                }
            ]
        }
    )

    assert res.errors is None
    assert len(res.payload.get("responses")) == 2
    assert res.payload.get("responses")[0].get("status").get("statusCode") == 200
    assert res.payload.get("responses")[1].get("status").get("statusCode") == 400