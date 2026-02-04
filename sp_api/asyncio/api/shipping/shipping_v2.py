import enum
import os
import urllib.parse
from datetime import datetime

from sp_api.base import (
    sp_endpoint,
    fill_query_params,
    ApiResponse,
    Marketplaces,
)
from sp_api.asyncio.base import AsyncBaseClient


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


class ShippingV2(AsyncBaseClient):
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

    async def _get_headers(self, access_token=None):
        headers = await super()._get_headers(access_token=access_token)
        headers["x-amzn-shipping-business-id"] = self.amzn_shipping_business.value
        return headers

    @sp_endpoint("/shipping/v2/shipments/rates", method="POST")
    async def get_rates(self, **kwargs) -> ApiResponse:
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
            
                await ShippingV2().get_rates()
        
        Args:
            body: GetRatesRequest | required GetRatesRequest body
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)

    @sp_endpoint("/shipping/v2/shipments", method="POST")
    async def purchase_shipment(self, **kwargs) -> ApiResponse:
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
            
                await ShippingV2().purchase_shipment()
        
        Args:
            body: PurchaseShipmentRequest | required PurchaseShipmentRequest body
            x-amzn-IdempotencyKey: object |  A unique value which the server uses to recognize subsequent retries of the same request.
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)

    @sp_endpoint("/shipping/v2/oneClickShipment", method="POST")
    async def one_click_shipment(self, **kwargs) -> ApiResponse:
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
            
                await ShippingV2().one_click_shipment()
        
        Args:
            body: OneClickShipmentRequest | required OneClickShipmentRequest body
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)

    @sp_endpoint("/shipping/v2/tracking", method="GET")
    async def get_tracking(self, **kwargs) -> ApiResponse:
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
            
                await ShippingV2().get_tracking()
        
        Args:
            key trackingId: object | required A carrier-generated tracking identifier originally returned by the purchaseShipment operation.
            key carrierId: object | required A carrier identifier originally returned by the getRates operation for the selected rate.
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/shipping/v2/shipments/{}/documents", method="GET")
    async def get_shipment_documents(self, shipmentId, **kwargs) -> ApiResponse:
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
            
                await ShippingV2().get_shipment_documents("value")
        
        Args:
            shipmentId: object | required The shipment identifier originally returned by the purchaseShipment operation.
            key packageClientReferenceId: object | required The package client reference identifier originally provided in the request body parameter for the getRates operation.
            key format: object |  The file format of the document. Must be one of the supported formats returned by the getRates operation.
            key dpi: object |  The resolution of the document (for example, 300 means 300 dots per inch). Must be one of the supported resolutions returned in the response to the getRates operation.
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), shipmentId),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/shipping/v2/shipments/{}/cancel", method="PUT")
    async def cancel_shipment(self, shipmentId, **kwargs) -> ApiResponse:
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
            
                await ShippingV2().cancel_shipment("value")
        
        Args:
            shipmentId: object | required The shipment identifier originally returned by the purchaseShipment operation.
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), shipmentId),
            data=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/shipping/v2/accessPoints", method="GET")
    async def get_access_points(self, **kwargs) -> ApiResponse:
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
            
                await ShippingV2().get_access_points()
        
        Args:
            key accessPointTypes: object | required Access point types
            key countryCode: object | required Country code for access point
            key postalCode: object | required postal code for access point
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/shipping/v2/ndrFeedback", method="POST")
    async def submit_ndr_feedback(self, **kwargs) -> ApiResponse:
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
            
                await ShippingV2().submit_ndr_feedback()
        
        Args:
            body: SubmitNdrFeedbackRequest | required Request body for ndrFeedback operation
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)

    @sp_endpoint("/shipping/v2/shipments/additionalInputs/schema", method="GET")
    async def get_additional_inputs(self, **kwargs) -> ApiResponse:
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
            
                await ShippingV2().get_additional_inputs()
        
        Args:
            key requestToken: object | required The request token returned in the response to the getRates operation.
            key rateId: object | required The rate identifier for the shipping offering (rate) returned in the response to the getRates operation.
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)


    @sp_endpoint("/shipping/v2/shipments/directPurchase", method="POST")
    async def direct_purchase_shipment(self, **kwargs) -> ApiResponse:
        """
        direct_purchase_shipment(self, **kwargs) -> ApiResponse
        
        Purchases the shipping service for a shipment using the best fit service offering. Returns purchase related details and documents.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        80                                      100
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ShippingV2().direct_purchase_shipment()
        
        Args:
            body: DirectPurchaseRequest | required DirectPurchaseRequest body
            x-amzn-IdempotencyKey: object |  A unique value which the server uses to recognize subsequent retries of the same request.
            locale: object |  The IETF Language Tag. Note that this only supports the primary language subtag with one secondary language subtag (i.e. en-US, fr-CA).
                The secondary language subtag is almost always a regional designation.
                This does not support additional subtags beyond the primary and secondary language subtags.
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), data=kwargs)







    @sp_endpoint("/shipping/v2/carrierAccountFormInputs", method="GET")
    async def get_carrier_account_form_inputs(self, **kwargs) -> ApiResponse:
        """
        get_carrier_account_form_inputs(self, **kwargs) -> ApiResponse
        
        This API will return a list of input schema required to register a shipper account with the carrier.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        80                                      100
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ShippingV2().get_carrier_account_form_inputs()
        
        Args:
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/shipping/v2/carrierAccounts", method="PUT")
    async def get_carrier_accounts(self, **kwargs) -> ApiResponse:
        """
        get_carrier_accounts(self, **kwargs) -> ApiResponse
        
        This API will return Get all carrier accounts for a merchant.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        80                                      100
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ShippingV2().get_carrier_accounts()
        
        Args:
            body: GetCarrierAccountsRequest | required GetCarrierAccountsRequest body
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/shipping/v2/carrierAccounts/{}", method="PUT")
    async def link_carrier_account(self, carrierId, **kwargs) -> ApiResponse:
        """
        link_carrier_account(self, carrierId, **kwargs) -> ApiResponse
        
        This API associates/links the specified carrier account with the merchant.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        80                                      100
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ShippingV2().link_carrier_account("value")
        
        Args:
            carrierId: object | required An identifier for the carrier with which the seller's account is being linked.
            body: LinkCarrierAccountRequest | required LinkCarrierAccountRequest body
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), carrierId), data=kwargs)

    @sp_endpoint("/shipping/v2/carrierAccounts/{}", method="POST")
    async def link_carrier_account_post(self, carrierId, **kwargs) -> ApiResponse:
        """
        link_carrier_account_post(self, carrierId, **kwargs) -> ApiResponse
        
        This API associates/links the specified carrier account with the merchant.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ShippingV2().link_carrier_account_post("value")
        
        Args:
            carrierId: object | required An identifier for the carrier with which the seller's account is being linked.
            body: LinkCarrierAccountRequest | required LinkCarrierAccountRequest body
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), carrierId), data=kwargs)

    @sp_endpoint("/shipping/v2/carrierAccounts/{}/unlink", method="PUT")
    async def unlink_carrier_account(self, carrierId, **kwargs) -> ApiResponse:
        """
        unlink_carrier_account(self, carrierId, **kwargs) -> ApiResponse
        
        This API Unlink the specified carrier account with the merchant.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        80                                      100
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ShippingV2().unlink_carrier_account("value")
        
        Args:
            carrierId: object | required carrier Id to unlink with merchant.
            body: UnlinkCarrierAccountRequest | required UnlinkCarrierAccountRequest body
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), carrierId), data=kwargs)

    @sp_endpoint("/shipping/v2/collectionForms", method="POST")
    async def generate_collection_form(self, **kwargs) -> ApiResponse:
        """
        generate_collection_form(self, **kwargs) -> ApiResponse
        
        This API  Call to generate the collection form.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        80                                      100
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ShippingV2().generate_collection_form()
        
        Args:
            body: GenerateCollectionFormRequest | required GenerateCollectionFormRequest body
            x-amzn-IdempotencyKey: object |  A unique value which the server uses to recognize subsequent retries of the same request.
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/shipping/v2/collectionForms/history", method="PUT")
    async def get_collection_form_history(self, **kwargs) -> ApiResponse:
        """
        get_collection_form_history(self, **kwargs) -> ApiResponse
        
        This API Call to get the history of the previously generated collection forms.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        80                                      100
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ShippingV2().get_collection_form_history()
        
        Args:
            body: GetCollectionFormHistoryRequest | required GetCollectionFormHistoryRequest body
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/shipping/v2/unmanifestedShipments", method="PUT")
    async def get_unmanifested_shipments(self, **kwargs) -> ApiResponse:
        """
        get_unmanifested_shipments(self, **kwargs) -> ApiResponse
        
        This API Get all unmanifested carriers with shipment locations. Any locations which has unmanifested shipments
                with an eligible carrier for manifesting shall be returned.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        80                                      100
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ShippingV2().get_unmanifested_shipments()
        
        Args:
            body: GetUnmanifestedShipmentsRequest | required GetUmanifestedShipmentsRequest body
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/shipping/v2/collectionForms/{}", method="GET")
    async def get_collection_form(self, collectionFormId, **kwargs) -> ApiResponse:
        """
        get_collection_form(self, collectionFormId, **kwargs) -> ApiResponse
        
        This API reprint a collection form.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        80                                      100
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ShippingV2().get_collection_form("value")
        
        Args:
            collectionFormId: object | required collection form Id to reprint a collection.
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), collectionFormId), params=kwargs)



    @sp_endpoint("/shipping/v2/claims", method="POST")
    async def create_claim(self, **kwargs) -> ApiResponse:
        """
        create_claim(self, **kwargs) -> ApiResponse
        
        This API will be used to create claim for single eligible shipment.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        80                                      100
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ShippingV2().create_claim()
        
        Args:
            body: CreateClaimRequest | required Request body for the createClaim operation
            x-amzn-shipping-business-id: object |  Amazon shipping business to assume for this request. The default is AmazonShipping_UK.
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), data=kwargs)
