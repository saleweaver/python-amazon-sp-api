import urllib.parse

from sp_api.base import sp_endpoint, fill_query_params, ApiResponse
from sp_api.asyncio.base import AsyncBaseClient


class ShippingV1(AsyncBaseClient):
    """
    Shipping SP-API Client
    :link:

    Provides programmatic access to Amazon Shipping APIs.
    """

    @sp_endpoint("/shipping/v1/shipments", method="POST")
    async def create_shipment(self, **kwargs) -> ApiResponse:
        """
        create_shipment(self, **kwargs) -> ApiResponse
        
        Create a new shipment.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       15
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ShippingV1().create_shipment()
        
        Args:
            body: CreateShipmentRequest | required CreateShipmentRequest Body
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/shipping/v1/shipments/{}", method="GET")
    async def get_shipment(self, shipmentId, **kwargs) -> ApiResponse:
        """
        get_shipment(self, shipmentId, **kwargs) -> ApiResponse
        
        Return the entire shipment object for the shipmentId.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       15
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ShippingV1().get_shipment("value")
        
        Args:
            shipmentId: object | required Shipment id to return the entire shipment object
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), shipmentId), params=kwargs
        )

    @sp_endpoint("/shipping/v1/shipments/{}/cancel", method="POST")
    async def cancel_shipment(self, shipmentId, **kwargs) -> ApiResponse:
        """
        cancel_shipment(self, shipmentId, **kwargs) -> ApiResponse
        
        Cancel a shipment by the given shipmentId.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       15
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ShippingV1().cancel_shipment("value")
        
        Args:
            shipmentId: object | required Shipment Id to cancel a shipment
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), shipmentId), data=kwargs
        )

    @sp_endpoint("/shipping/v1/shipments/{}/purchaseLabels", method="POST")
    async def purchase_labels(self, shipmentId, **kwargs) -> ApiResponse:
        """
        purchase_labels(self, shipmentId, **kwargs) -> ApiResponse
        
        Purchase shipping labels based on a given rate.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       15
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ShippingV1().purchase_labels("value")
        
        Args:
            shipmentId: object | required Shipment id for purchase shipping label
            body: PurchaseLabelsRequest | required PurchaseShippingLabelRequest body
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), shipmentId), data=kwargs
        )

    @sp_endpoint("/shipping/v1/shipments/{}/label", method="POST")
    async def retrieve_shipping_label(self, shipmentId, **kwargs) -> ApiResponse:
        """
        retrieve_shipping_label(self, shipmentId, **kwargs) -> ApiResponse
        
        Retrieve shipping label based on the shipment id and tracking id.
        
        Examples:
            literal blocks::
            
                await ShippingV1().retrieve_shipping_label("value")
        
        Args:
            shipmentId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), shipmentId), data=kwargs
        )

    @sp_endpoint("/shipping/v1/shipments/{}/containers/{}/label", method="POST")
    async def retrieve_shipping_label_for_container(
        self, shipmentId, trackingId, **kwargs
    ) -> ApiResponse:
        """
        retrieve_shipping_label_for_container(self, shipmentId, trackingId, **kwargs) -> ApiResponse
        
        Retrieve shipping label based on the shipment id and tracking id.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       15
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ShippingV1().retrieve_shipping_label_for_container("value", "value")
        
        Args:
            shipmentId: object | required Shipment Id to retreive label
            trackingId: object | required Tracking Id
            body: RetrieveShippingLabelRequest | required RetrieveShippingLabelRequest body
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), shipmentId, trackingId), data=kwargs
        )

    @sp_endpoint("/shipping/v1/purchaseShipment", method="POST")
    async def purchase_shipment(self, **kwargs) -> ApiResponse:
        """
        purchase_shipment(self, **kwargs) -> ApiResponse
        
        Purchase shipping labels.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       15
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ShippingV1().purchase_shipment()
        
        Args:
            body: PurchaseShipmentRequest | required PurchaseShipmentRequest body
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/shipping/v1/rates", method="POST")
    async def get_rates(self, **kwargs) -> ApiResponse:
        """
        get_rates(self, **kwargs) -> ApiResponse
        
        Get service rates.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       15
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ShippingV1().get_rates()
        
        Args:
            body: GetRatesRequest | required GetRatesRequest body
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/shipping/v1/account", method="GET")
    async def get_account(self, **kwargs) -> ApiResponse:
        """
        get_account(self, **kwargs) -> ApiResponse
        
        Verify if the current account is valid.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       15
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ShippingV1().get_account()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/shipping/v1/tracking/{}", method="GET")
    async def get_tracking_information(self, trackingId, **kwargs) -> ApiResponse:
        """
        get_tracking_information(self, trackingId, **kwargs) -> ApiResponse
        
        Return the tracking information of a shipment.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ShippingV1().get_tracking_information("value")
        
        Args:
            trackingId: object | required Tracking Id
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), trackingId), params=kwargs
        )
