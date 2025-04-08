import enum
import os
import urllib.parse
from datetime import datetime

from sp_api.base import (
    Client,
    sp_endpoint,
    fill_query_params,
    ApiResponse,
    Marketplaces,
)


class AmznShippingBusiness(str, enum.Enum):
    US = "AmazonShipping_US"
    IN = "AmazonShipping_IN"
    UK = "AmazonShipping_UK"
    AE = "AmazonShipping_UAE"
    SA = "AmazonShipping_SA"
    IT = "AmazonShipping_IT"
    EG = "AmazonShipping_EG"
    ES = "AmazonShipping_ES"
    FR = "AmazonShipping_FR"
    JP = "AmazonShipping_JP"

    @classmethod
    def has_key(cls, name):
        return name in cls.__members__


class Shipping(Client):
    """
    Shipping V2 SP-API Client
    :link:

    Provides programmatic access to Amazon Shipping APIs.
    """

    amzn_shipping_business: AmznShippingBusiness = AmznShippingBusiness.US

    def __init__(self, *args, **kwargs):
        if "amzn_shipping_business" in kwargs:
            self.amzn_shipping_business = kwargs.pop(
                "amzn_shipping_business", AmznShippingBusiness.US
            )
        else:
            marketplace = args[0] if len(args) > 0 else Marketplaces.US
            if os.environ.get("SP_API_DEFAULT_MARKETPLACE", None):
                marketplace = Marketplaces[os.environ.get("SP_API_DEFAULT_MARKETPLACE")]

            if AmznShippingBusiness.has_key(marketplace.name):
                self.amzn_shipping_business = AmznShippingBusiness[marketplace.name]

        super().__init__(*args, **kwargs)

    @property
    def headers(self):
        return {
            "host": self.endpoint[8:],
            "user-agent": self.user_agent,
            "x-amz-access-token": self.restricted_data_token or self.auth.access_token,
            "x-amz-date": datetime.utcnow().strftime("%Y%m%dT%H%M%SZ"),
            "content-type": "application/json",
            "x-amzn-shipping-business-id": self.amzn_shipping_business.value,
        }

    @sp_endpoint("/shipping/v2/shipments/rates", method="POST")
    def get_rates(self, **kwargs) -> ApiResponse:
        """
        get_rates(self, **kwargs) -> ApiResponse

        Returns the available shipping service offerings.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            body: {
                "shipTo": {
                    "name": "string",
                    "addressLine1": "string",
                    "addressLine2": "string",
                    "addressLine3": "string",
                    "companyName": "string",
                    "stateOrRegion": "string",
                    "city": "string",
                    "countryCode": "st",
                    "postalCode": "string",
                    "email": "string",
                    "phoneNumber": "string",
                    "geocode": {
                        "latitude": "string",
                        "longitude": "string"
                    }
                },
                "shipFrom": {
                    "name": "string",
                    "addressLine1": "string",
                    "addressLine2": "string",
                    "addressLine3": "string",
                    "companyName": "string",
                    "stateOrRegion": "string",
                    "city": "string",
                    "countryCode": "st",
                    "postalCode": "string",
                    "email": "string",
                    "phoneNumber": "string",
                    "geocode": {
                        "latitude": "string",
                        "longitude": "string"
                    }
                },
                "returnTo": {
                    "name": "string",
                    "addressLine1": "string",
                    "addressLine2": "string",
                    "addressLine3": "string",
                    "companyName": "string",
                    "stateOrRegion": "string",
                    "city": "string",
                    "countryCode": "st",
                    "postalCode": "string",
                    "email": "string",
                    "phoneNumber": "string",
                    "geocode": {
                        "latitude": "string",
                        "longitude": "string"
                    }
                },
                "shipDate": "2019-08-24T14:15:22Z",
                "shipperInstruction": {
                    "deliveryNotes": "string"
                },
                "packages": [
                    {
                        "dimensions": {
                            "length": 0,
                            "width": 0,
                            "height": 0,
                            "unit": "CENTIMETER"
                        },
                        "weight": {
                            "unit": "KILOGRAM",
                            "value": 0
                        },
                        "insuredValue":{
                            "value": 0.00,
                            "unit": "EUR",
                        },
                        "isHazmat": False,
                        "sellerDisplayName": "string",
                        "charges": [
                            {
                                "amount": {
                                    "value": 0.00,
                                    "unit": "EUR",
                                },
                                "chargeType": "TAX"
                            }
                        ],
                        "packageClientReferenceId": "string",
                        "items": [
                            {
                                "itemValue": {
                                    "value": 0.00,
                                    "unit": "EUR",
                                },
                                "description": "string",
                                "itemIdentifier": "string",
                                "quantity": 1,
                                "weight": {
                                    "value": 0.00,
                                    "unit": "KILOGRAM",
                                },
                                "liquidVolume": {
                                    "value": 0.00,
                                    "unit": "ML",
                                },
                                "isHazmat": False,
                                "dangerousGoodsDetails": {
                                    "unitedNationsRegulatoryId": "string",
                                    "transportationRegulatoryClass": "string",
                                    "packingGroup": "III",
                                    "packingInstruction": "PI965_SECTION_IA",
                                },
                                "productType": "string",
                                "invoiceDetails": {
                                    "invoiceNumber": "string",
                                    "invoiceDate": "2019-08-24T14:15:22Z"
                                },
                                "serialNumbers": ["string"],
                                "directFulfillmentItemIdentifiers": {
                                    "lineItemID": "string",
                                    "pieceNumber": "string"
                                }
                            }
                        ]
                    }
                ],
                "valueAddedServicesDetails": {
                    "collectOnDelivery": {
                        "amount": {
                            "value": 0.00,
                            "unit": "EUR",
                        }
                    }
                },
                "taxDetails": [
                    {
                        "taxType": "GST",
                        "taxRegistrationNumber": "string"
                    }
                ],
                "channelDetails": {
                    "channelType": "EXTERNAL",
                    "amazonOrderDetails": {
                        "orderId": "string"
                    },
                    "amazonShipmentDetails": {
                        "shipmentId": "string"
                    }
                },
                "clientReferenceDetails": [
                    {
                        "clientReferenceType": "IntegratorShipperId",
                        "clientReferenceId": "string"
                    }
                ],
                "shipmentType": "FORWARD",
                "destinationAccessPointDetails": {
                    "accessPointId": "string",
                }
            }

        Returns:
            ApiResponse:
        """

        return self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)

    @sp_endpoint("/shipping/v2/shipments", method="POST")
    def purchase_shipment(self, **kwargs) -> ApiResponse:
        """
        purchase_shipment(self, **kwargs) -> ApiResponse

        Purchases a shipping service and returns purchase related details and documents.

        Note: You must complete the purchase within 10 minutes of rate creation by the shipping service provider for channelType as EXTERNAL which is for OFF-Amazon volume. If you make the request after the 10 minutes have expired, you will receive an error response with the error code equal to "TOKEN_EXPIRED". If you receive this error response, you must get the rates for the shipment again.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            body: {
                "requestToken": "string",
                "rateId": "string",
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
                },
                "requestedValueAddedServices": [
                    {
                        "id": "string"
                    }
                ],
                "additionalInputs": {}
            }

        Returns:
            ApiResponse:
        """
        return self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)

    @sp_endpoint("/shipping/v2/oneClickShipment", method="POST")
    def one_click_shipment(self, **kwargs) -> ApiResponse:
        """
        one_click_shipment(self, **kwargs) -> ApiResponse

        Purchases a shipping service identifier and returns purchase-related details and documents.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            body: {
                "shipTo": {
                    "name": "string",
                    "addressLine1": "string",
                    "addressLine2": "string",
                    "addressLine3": "string",
                    "companyName": "string",
                    "stateOrRegion": "string",
                    "city": "string",
                    "countryCode": "st",
                    "postalCode": "string",
                    "email": "string",
                    "phoneNumber": "string",
                    "geocode": {
                        "latitude": "string",
                        "longitude": "string"
                    }
                },
                "shipFrom": {
                    "name": "string",
                    "addressLine1": "string",
                    "addressLine2": "string",
                    "addressLine3": "string",
                    "companyName": "string",
                    "stateOrRegion": "string",
                    "city": "string",
                    "countryCode": "st",
                    "postalCode": "string",
                    "email": "string",
                    "phoneNumber": "string",
                    "geocode": {
                        "latitude": "string",
                        "longitude": "string"
                    }
                },
                "returnTo": {
                    "name": "string",
                    "addressLine1": "string",
                    "addressLine2": "string",
                    "addressLine3": "string",
                    "companyName": "string",
                    "stateOrRegion": "string",
                    "city": "string",
                    "countryCode": "st",
                    "postalCode": "string",
                    "email": "string",
                    "phoneNumber": "string",
                    "geocode": {
                        "latitude": "string",
                        "longitude": "string"
                    }
                },
                "shipDate": "2019-08-24T14:15:22Z",
                "packages": [
                    {
                        "dimensions": {
                            "length": 0,
                            "width": 0,
                            "height": 0,
                            "unit": "CENTIMETER"
                        },
                        "weight": {
                            "unit": "KILOGRAM",
                            "value": 0
                        },
                        "insuredValue":{
                            "value": 0.00,
                            "unit": "EUR",
                        },
                        "isHazmat": False,
                        "sellerDisplayName": "string",
                        "charges": [
                            {
                                "amount": {
                                    "value": 0.00,
                                    "unit": "EUR",
                                },
                                "chargeType": "TAX"
                            }
                        ],
                        "packageClientReferenceId": "string",
                        "items": [
                            {
                                "itemValue": {
                                    "value": 0.00,
                                    "unit": "EUR",
                                },
                                "description": "string",
                                "itemIdentifier": "string",
                                "quantity": 1,
                                "weight": {
                                    "value": 0.00,
                                    "unit": "KILOGRAM",
                                },
                                "liquidVolume": {
                                    "value": 0.00,
                                    "unit": "ML",
                                },
                                "isHazmat": False,
                                "dangerousGoodsDetails": {
                                    "unitedNationsRegulatoryId": "string",
                                    "transportationRegulatoryClass": "string",
                                    "packingGroup": "III",
                                    "packingInstruction": "PI965_SECTION_IA",
                                },
                                "productType": "string",
                                "invoiceDetails": {
                                    "invoiceNumber": "string",
                                    "invoiceDate": "2019-08-24T14:15:22Z"
                                },
                                "serialNumbers": ["string"],
                                "directFulfillmentItemIdentifiers": {
                                    "lineItemID": "string",
                                    "pieceNumber": "string"
                                }
                            }
                        ]
                    }
                ],
                "valueAddedServicesDetails": [
                    "id": "string",
                    "amount": {
                        "value": 0.00,
                        "unit": "EUR",
                    },
                ],
                "taxDetails": [
                    {
                        "taxType": "GST",
                        "taxRegistrationNumber": "string"
                    }
                ],
                "channelDetails": {
                    "channelType": "EXTERNAL",
                    "amazonOrderDetails": {
                        "orderId": "string"
                    },
                    "amazonShipmentDetails": {
                        "shipmentId": "string"
                    }
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
                    "serviceId": ["prime-premium-uk-mfn", "std-uk-mfn", "econ-uk-mfn"]
                },
                "shipperInstruction": {
                    "deliveryNotes": "string"
                },
                "destinationAccessPointDetails": {
                    "accessPointId": "string"
                }

            }

        Returns:
            ApiResponse:
        """
        return self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)

    @sp_endpoint("/shipping/v2/tracking", method="GET")
    def get_tracking(self, **kwargs) -> ApiResponse:
        """
        get_tracking(self, **kwargs) -> ApiResponse

        Returns tracking information for a purchased shipment.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            key trackingId:string | * REQUIRED  A carrier-generated tracking identifier originally returned by the purchaseShipment operation.
            key carrierId:string | * REQUIRED  A carrier identifier originally returned by the getRates operation for the selected rate.

        Returns:
            ApiResponse:
        """
        return self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/shipping/v2/shipments/{}/documents", method="GET")
    def get_shipment_documents(self, shipmentId, **kwargs) -> ApiResponse:
        """
        get_shipment_documents(self, shipmentId, **kwargs) -> ApiResponse

        Returns the shipping documents associated with a package in a shipment.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipmentId:string | * REQUIRED The shipment identifier originally returned by the purchaseShipment operation.
            key packageClientReferenceId:string | * REQUIRED The shipment identifier originally returned by the purchaseShipment operation.
            key format:string | The file format of the document. Must be one of the supported formats returned by the getRates operation.
            key dpi:number | The resolution of the document (for example, 300 means 300 dots per inch). Must be one of the supported resolutions returned in the response to the getRates operation.

        Returns:
            ApiResponse:
        """

        return self._request(
            fill_query_params(kwargs.pop("path"), shipmentId),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/shipping/v2/shipments/{}/cancel", method="PUT")
    def cancel_shipment(self, shipmentId, **kwargs) -> ApiResponse:
        """
        cancel_shipment(self, shipmentId, **kwargs) -> ApiResponse

        Cancels a purchased shipment. Returns an empty object if the shipment is successfully cancelled.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipmentId:string | * REQUIRED The shipment identifier originally returned by the purchaseShipment operation.

        Returns:
            ApiResponse:
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), shipmentId),
            data=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/shipping/v2/accessPoints", method="GET")
    def get_access_points(self, **kwargs) -> ApiResponse:
        """
        get_access_points(self, **kwargs) -> ApiResponse

        Returns a list of access points in proximity of input postal code.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            key accessPointTypes:string | * REQUIRED
            key countryCode:string | * REQUIRED
            key postalCode:string | * REQUIRED

        Returns:
            ApiResponse:
        """
        return self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/shipping/v2/ndrFeedback", method="POST")
    def submit_ndr_feedback(self, **kwargs) -> ApiResponse:
        """
        submit_ndr_feedback(self, **kwargs) -> ApiResponse

        This API submits the NDR (Non-delivery Report) Feedback for any eligible shipment.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            body: {
                "trackingId": "string",
                "ndrAction": "RTO",
                "ndrRequestData": {
                    "rescheduleDate": "2024-12-12T05:24:00.00Z",
                    "additionalAddressNotes": "string"
                }
            }

        Returns:
            ApiResponse:
        """
        return self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)

    @sp_endpoint("/shipping/v2/shipments/additionalInputs/schema", method="GET")
    def get_additional_inputs(self, **kwargs) -> ApiResponse:
        """
        get_additional_inputs(self, **kwargs) -> ApiResponse

        Returns the JSON schema to use for providing additional inputs when needed to purchase a shipping offering. Call the getAdditionalInputs operation when the response to a previous call to the getRates operation indicates that additional inputs are required for the rate (shipping offering) that you want to purchase.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            key requestToken:string | * REQUIRED The request token returned in the response to the getRates operation.
            key rateId:string | * REQUIRED The rate identifier for the shipping offering (rate) returned in the response to the getRates operation.

        Returns:
            ApiResponse:
        """
        return self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)
