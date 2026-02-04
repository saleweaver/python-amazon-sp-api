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


class ShippingV2(Client):
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


    @sp_endpoint("/shipping/v2/shipments/directPurchase", method="POST")
    def direct_purchase_shipment(self, **kwargs) -> ApiResponse:
        """
        direct_purchase_shipment(self, **kwargs) -> ApiResponse

        Purchases the shipping service for a shipment using the best fit service offering. Returns purchase related details and documents.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 80 | 100 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            body:DirectPurchaseRequest | * REQUIRED {'description': 'The request schema for the directPurchaseShipment operation. When the channel type is Amazon, the shipTo address is not required and will be ignored.',
             'properties': {'channelDetails': {'$ref': '#/definitions/ChannelDetails'},
                            'labelSpecifications': {'$ref': '#/definitions/RequestedDocumentSpecification',
                                                    'description': 'The document (label) specifications requested. The default label returned is PNG DPI 203 4x6 if no label specification is provided. Requesting an invalid file format results in a failure.'},
                            'packages': {'$ref': '#/definitions/PackageList'},
                            'returnTo': {'$ref': '#/definitions/Address', 'description': 'The address where the package will be returned if it cannot be delivered.'},
                            'shipFrom': {'$ref': '#/definitions/Address', 'description': 'The address where the package will be picked up.'},
                            'shipTo': {'$ref': '#/definitions/Address', 'description': 'The address where the shipment will be delivered. For vendor orders, shipTo information is pulled directly from the Amazon order.'}},
             'required': ['channelDetails'],
             'type': 'object'}
            x-amzn-IdempotencyKey:string |  A unique value which the server uses to recognize subsequent retries of the same request.
            locale:string |  The IETF Language Tag. Note that this only supports the primary language subtag with one secondary language subtag (i.e. en-US, fr-CA).
            The secondary language subtag is almost always a regional designation.
            This does not support additional subtags beyond the primary and secondary language subtags.
            x-amzn-shipping-business-id:string |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.

        Returns:
            ApiResponse:
        """
        return self._request(kwargs.pop("path"), data=kwargs)







    @sp_endpoint("/shipping/v2/carrierAccountFormInputs", method="GET")
    def get_carrier_account_form_inputs(self, **kwargs) -> ApiResponse:
        """
        get_carrier_account_form_inputs(self, **kwargs) -> ApiResponse

        This API will return a list of input schema required to register a shipper account with the carrier. 
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 80 | 100 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            x-amzn-shipping-business-id:string |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.

        Returns:
            ApiResponse:
        """
        return self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/shipping/v2/carrierAccounts", method="PUT")
    def get_carrier_accounts(self, **kwargs) -> ApiResponse:
        """
        get_carrier_accounts(self, **kwargs) -> ApiResponse

        This API will return Get all carrier accounts for a merchant. 
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 80 | 100 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            body:GetCarrierAccountsRequest | * REQUIRED {'description': 'The request schema for the GetCarrierAccounts operation.', 'properties': {'clientReferenceDetails': {'$ref': '#/definitions/ClientReferenceDetails'}}, 'type': 'object'}
            x-amzn-shipping-business-id:string |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.

        Returns:
            ApiResponse:
        """
        return self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/shipping/v2/carrierAccounts/{}", method="PUT")
    def link_carrier_account(self, carrierId, **kwargs) -> ApiResponse:
        """
        link_carrier_account(self, carrierId, **kwargs) -> ApiResponse

        This API associates/links the specified carrier account with the merchant. 
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 80 | 100 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            carrierId:string | * REQUIRED An identifier for the carrier with which the seller's account is being linked.
            body:LinkCarrierAccountRequest | * REQUIRED {'description': "The request schema for verify and add the merchant's account with a certain carrier.",
             'properties': {'carrierAccountAttributes': {'$ref': '#/definitions/CarrierAccountAttributes'},
                            'carrierAccountType': {'$ref': '#/definitions/CarrierAccountType'},
                            'clientReferenceDetails': {'$ref': '#/definitions/ClientReferenceDetails'},
                            'encryptedCarrierAccountAttributes': {'$ref': '#/definitions/CarrierAccountAttributes'}},
             'required': ['carrierAccountAttributes', 'carrierAccountType'],
             'type': 'object'}
            x-amzn-shipping-business-id:string |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.

        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path"), carrierId), data=kwargs)

    @sp_endpoint("/shipping/v2/carrierAccounts/{}", method="POST")
    def link_carrier_account_post(self, carrierId, **kwargs) -> ApiResponse:
        """
        link_carrier_account_post(self, carrierId, **kwargs) -> ApiResponse

        This API associates/links the specified carrier account with the merchant. 
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 5 | 10 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            carrierId:string | * REQUIRED An identifier for the carrier with which the seller's account is being linked.
            body:LinkCarrierAccountRequest | * REQUIRED {'description': "The request schema for verify and add the merchant's account with a certain carrier.",
             'properties': {'carrierAccountAttributes': {'$ref': '#/definitions/CarrierAccountAttributes'},
                            'carrierAccountType': {'$ref': '#/definitions/CarrierAccountType'},
                            'clientReferenceDetails': {'$ref': '#/definitions/ClientReferenceDetails'},
                            'encryptedCarrierAccountAttributes': {'$ref': '#/definitions/CarrierAccountAttributes'}},
             'required': ['carrierAccountAttributes', 'carrierAccountType'],
             'type': 'object'}
            x-amzn-shipping-business-id:string |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.

        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path"), carrierId), data=kwargs)

    @sp_endpoint("/shipping/v2/carrierAccounts/{}/unlink", method="PUT")
    def unlink_carrier_account(self, carrierId, **kwargs) -> ApiResponse:
        """
        unlink_carrier_account(self, carrierId, **kwargs) -> ApiResponse

        This API Unlink the specified carrier account with the merchant. 
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 80 | 100 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            carrierId:string | * REQUIRED carrier Id to unlink with merchant.
            body:UnlinkCarrierAccountRequest | * REQUIRED {'description': 'The request schema for remove the Carrier Account associated with the provided merchant.',
             'properties': {'accountId': {'$ref': '#/definitions/AccountId'}, 'clientReferenceDetails': {'$ref': '#/definitions/ClientReferenceDetails'}},
             'type': 'object'}
            x-amzn-shipping-business-id:string |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.

        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path"), carrierId), data=kwargs)

    @sp_endpoint("/shipping/v2/collectionForms", method="POST")
    def generate_collection_form(self, **kwargs) -> ApiResponse:
        """
        generate_collection_form(self, **kwargs) -> ApiResponse

        This API  Call to generate the collection form. 
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 80 | 100 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            body:GenerateCollectionFormRequest | * REQUIRED {'description': 'The request schema Call to generate the collection form.',
             'properties': {'carrierId': {'$ref': '#/definitions/CarrierId'}, 'clientReferenceDetails': {'$ref': '#/definitions/ClientReferenceDetails'}, 'shipFromAddress': {'$ref': '#/definitions/Address'}},
             'required': ['carrierId'],
             'type': 'object'}
            x-amzn-IdempotencyKey:string |  A unique value which the server uses to recognize subsequent retries of the same request.
            x-amzn-shipping-business-id:string |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.

        Returns:
            ApiResponse:
        """
        return self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/shipping/v2/collectionForms/history", method="PUT")
    def get_collection_form_history(self, **kwargs) -> ApiResponse:
        """
        get_collection_form_history(self, **kwargs) -> ApiResponse

        This API Call to get the history of the previously generated collection forms. 
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 80 | 100 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            body:GetCollectionFormHistoryRequest | * REQUIRED {'description': 'The request schema to get query collections form history API .',
             'properties': {'carrierId': {'$ref': '#/definitions/CarrierId'},
                            'clientReferenceDetails': {'$ref': '#/definitions/ClientReferenceDetails'},
                            'dateRange': {'$ref': '#/definitions/DateRange'},
                            'maxResults': {'description': 'max Number of Results for query .', 'type': 'integer'},
                            'shipFromAddress': {'$ref': '#/definitions/Address'}},
             'type': 'object'}
            x-amzn-shipping-business-id:string |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.

        Returns:
            ApiResponse:
        """
        return self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/shipping/v2/unmanifestedShipments", method="PUT")
    def get_unmanifested_shipments(self, **kwargs) -> ApiResponse:
        """
        get_unmanifested_shipments(self, **kwargs) -> ApiResponse

        This API Get all unmanifested carriers with shipment locations. Any locations which has unmanifested shipments
                with an eligible carrier for manifesting shall be returned. 
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 80 | 100 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            body:GetUnmanifestedShipmentsRequest | * REQUIRED {'description': 'The request schema for the GetUnmanifestedShipmentsRequest operation.', 'properties': {'clientReferenceDetails': {'$ref': '#/definitions/ClientReferenceDetails'}}, 'type': 'object'}
            x-amzn-shipping-business-id:string |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.

        Returns:
            ApiResponse:
        """
        return self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/shipping/v2/collectionForms/{}", method="GET")
    def get_collection_form(self, collectionFormId, **kwargs) -> ApiResponse:
        """
        get_collection_form(self, collectionFormId, **kwargs) -> ApiResponse

        This API reprint a collection form. 
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 80 | 100 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            collectionFormId:string | * REQUIRED collection form Id to reprint a collection.
            x-amzn-shipping-business-id:string |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.

        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path"), collectionFormId), params=kwargs)



    @sp_endpoint("/shipping/v2/claims", method="POST")
    def create_claim(self, **kwargs) -> ApiResponse:
        """
        create_claim(self, **kwargs) -> ApiResponse

        This API will be used to create claim for single eligible shipment.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 80 | 100 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            body:CreateClaimRequest | * REQUIRED {'description': 'The request schema for the CreateClaim operation',
             'properties': {'claimReason': {'$ref': '#/definitions/ClaimReason'},
                            'declaredValue': {'$ref': '#/definitions/Currency', 'description': 'This is required for off-Amazon shipments to determine value of shipments'},
                            'isReplacementPackageSent': {'description': 'Applicable for only On Amazon shipments to identify if replacement was sent', 'type': 'boolean'},
                            'proofs': {'$ref': '#/definitions/ClaimProofURLs'},
                            'settlementType': {'$ref': '#/definitions/SettlementType'},
                            'trackingId': {'$ref': '#/definitions/TrackingId'}},
             'required': ['trackingId', 'claimReason', 'settlementType'],
             'type': 'object'}
            x-amzn-shipping-business-id:string |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.

        Returns:
            ApiResponse:
        """
        return self._request(kwargs.pop("path"), data=kwargs)
