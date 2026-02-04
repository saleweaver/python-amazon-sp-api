import enum
import os
import urllib.parse
from datetime import datetime, timezone

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
            "x-amz-date": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
            "content-type": "application/json",
            "x-amzn-shipping-business-id": self.amzn_shipping_business.value,
        }

    @sp_endpoint("/shipping/v2/shipments/rates", method="POST")
    def get_rates(self, **kwargs) -> ApiResponse:
        """
        get_rates(self, **kwargs) -> ApiResponse
        
        Returns the available shipping service offerings.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        80                                      100
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                Shipping().get_rates()
        
        Args:
            body: GetRatesRequest | required GetRatesRequest body
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """

        return self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)

    @sp_endpoint("/shipping/v2/shipments", method="POST")
    def purchase_shipment(self, **kwargs) -> ApiResponse:
        """
        purchase_shipment(self, **kwargs) -> ApiResponse
        
        Purchases a shipping service and returns purchase related details and documents.
        
        Note: You must complete the purchase within 10 minutes of rate creation by the shipping service provider. If you make the request after the 10 minutes have expired, you will receive an error response with the error code equal to "TOKEN_EXPIRED". If you receive this error response, you must get the rates for the shipment again.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        80                                      100
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                Shipping().purchase_shipment()
        
        Args:
            body: PurchaseShipmentRequest | required PurchaseShipmentRequest body
            x-amzn-IdempotencyKey: object |  A unique value which the server uses to recognize subsequent retries of the same request.
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)

    @sp_endpoint("/shipping/v2/oneClickShipment", method="POST")
    def one_click_shipment(self, **kwargs) -> ApiResponse:
        """
        one_click_shipment(self, **kwargs) -> ApiResponse
        
        Purchases a shipping service identifier and returns purchase-related details and documents.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        80                                      100
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                Shipping().one_click_shipment()
        
        Args:
            body: OneClickShipmentRequest | required OneClickShipmentRequest body
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)

    @sp_endpoint("/shipping/v2/tracking", method="GET")
    def get_tracking(self, **kwargs) -> ApiResponse:
        """
        get_tracking(self, **kwargs) -> ApiResponse
        
        Returns tracking information for a purchased shipment.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        80                                      100
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                Shipping().get_tracking()
        
        Args:
            key trackingId: object | required A carrier-generated tracking identifier originally returned by the purchaseShipment operation.
            key carrierId: object | required A carrier identifier originally returned by the getRates operation for the selected rate.
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/shipping/v2/shipments/{}/documents", method="GET")
    def get_shipment_documents(self, shipmentId, **kwargs) -> ApiResponse:
        """
        get_shipment_documents(self, shipmentId, **kwargs) -> ApiResponse
        
        Returns the shipping documents associated with a package in a shipment.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        80                                      100
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                Shipping().get_shipment_documents("value")
        
        Args:
            shipmentId: object | required The shipment identifier originally returned by the purchaseShipment operation.
            key packageClientReferenceId: object | required The package client reference identifier originally provided in the request body parameter for the getRates operation.
            key format: object |  The file format of the document. Must be one of the supported formats returned by the getRates operation.
            key dpi: object |  The resolution of the document (for example, 300 means 300 dots per inch). Must be one of the supported resolutions returned in the response to the getRates operation.
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
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
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        80                                      100
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                Shipping().cancel_shipment("value")
        
        Args:
            shipmentId: object | required The shipment identifier originally returned by the purchaseShipment operation.
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
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
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        80                                      100
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                Shipping().get_access_points()
        
        Args:
            key accessPointTypes: object | required Access point types
            key countryCode: object | required Country code for access point
            key postalCode: object | required postal code for access point
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/shipping/v2/ndrFeedback", method="POST")
    def submit_ndr_feedback(self, **kwargs) -> ApiResponse:
        """
        submit_ndr_feedback(self, **kwargs) -> ApiResponse
        
        This API submits the NDR (Non-delivery Report) Feedback for any eligible shipment.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        80                                      100
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                Shipping().submit_ndr_feedback()
        
        Args:
            body: SubmitNdrFeedbackRequest | required Request body for ndrFeedback operation
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)

    @sp_endpoint("/shipping/v2/shipments/additionalInputs/schema", method="GET")
    def get_additional_inputs(self, **kwargs) -> ApiResponse:
        """
        get_additional_inputs(self, **kwargs) -> ApiResponse
        
        Returns the JSON schema to use for providing additional inputs when needed to purchase a shipping offering. Call the getAdditionalInputs operation when the response to a previous call to the getRates operation indicates that additional inputs are required for the rate (shipping offering) that you want to purchase.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        80                                      100
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                Shipping().get_additional_inputs()
        
        Args:
            key requestToken: object | required The request token returned in the response to the getRates operation.
            key rateId: object | required The rate identifier for the shipping offering (rate) returned in the response to the getRates operation.
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)
