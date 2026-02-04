from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse
from sp_api.asyncio.base import AsyncBaseClient


class MerchantFulfillment(AsyncBaseClient):
    """
    :link: https://github.com/amzn/selling-partner-api-docs/blob/main/references/merchant-fulfillment-api/merchantFulfillmentV0.md

    """

    @sp_endpoint("/mfn/v0/eligibleServices", method="POST")
    async def get_eligible_shipment_services_old(
        self, shipment_request_details: dict, **kwargs
    ) -> ApiResponse:
        """
        get_eligible_shipment_services_old(self, shipment_request_details, **kwargs) -> ApiResponse
        
        Returns a list of shipping service offers that satisfy the specified shipment request details.
        
        Examples:
            literal blocks::
            
                await MerchantFulfillment().get_eligible_shipment_services_old("value")
        
        Args:
            shipment_request_details:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        # GetEligibleShipmentServicesRequest
        data = {"ShipmentRequestDetails": shipment_request_details, **kwargs}

        return await self._request(kwargs.pop("path"), data=data)

    @sp_endpoint("/mfn/v0/eligibleShippingServices", method="POST")
    async def get_eligible_shipment_services(
        self, shipment_request_details: dict, **kwargs
    ) -> ApiResponse:
        """
        get_eligible_shipment_services(self, shipment_request_details, **kwargs) -> ApiResponse
        
        Returns a list of shipping service offers that satisfy the specified shipment request details.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        6                                       12
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await MerchantFulfillment().get_eligible_shipment_services("value")
        
        Args:
            body: GetEligibleShipmentServicesRequest | required The request schema for the `GetEligibleShipmentServices` operation.
        
        Returns:
            ApiResponse
        """

        # GetEligibleShipmentServicesRequest
        data = {"ShipmentRequestDetails": shipment_request_details, **kwargs}

        return await self._request(kwargs.pop("path"), data=data)

    @sp_endpoint("/mfn/v0/shipments/{}")
    async def get_shipment(self, shipment_id: str, **kwargs) -> ApiResponse:
        """
        get_shipment(self, shipment_id, **kwargs) -> ApiResponse
        
        Returns the shipment information for an existing shipment.
        
        Examples:
            literal blocks::
            
                await MerchantFulfillment().get_shipment("value")
        
        Args:
            shipment_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), shipment_id),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/mfn/v0/shipments/{}", method="DELETE")
    async def cancel_shipment(self, shipment_id: str, **kwargs) -> ApiResponse:
        """
        cancel_shipment(self, shipment_id, **kwargs) -> ApiResponse
        
        Cancel the shipment indicated by the specified shipment identifier.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await MerchantFulfillment().cancel_shipment("value")
        
        Args:
            shipmentId: object | required The Amazon-defined shipment identifier for the shipment to cancel.
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), shipment_id),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/mfn/v0/shipments/{}/cancel", method="PUT")
    async def cancel_shipment_old(self, shipment_id: str, **kwargs) -> ApiResponse:
        """
        cancel_shipment_old(self, shipment_id, **kwargs) -> ApiResponse
        
        Cancel the shipment indicated by the specified shipment identifer.
        
        Examples:
            literal blocks::
            
                await MerchantFulfillment().cancel_shipment_old("value")
        
        Args:
            shipment_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), shipment_id),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/mfn/v0/shipments", method="POST")
    async def create_shipment(
        self, shipment_request_details: dict, shipping_service_id: str, **kwargs
    ) -> ApiResponse:
        """
        create_shipment(self, shipment_request_details, shipping_service_id, **kwargs) -> ApiResponse
        
        Create a shipment with the information provided.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       2
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await MerchantFulfillment().create_shipment("value", "value")
        
        Args:
            body: CreateShipmentRequest | required The request schema for the `CreateShipment` operation.
        
        Returns:
            ApiResponse
        """

        # CreateShipmentRequest
        data = {
            "ShipmentRequestDetails": shipment_request_details,
            "ShippingServiceId": shipping_service_id,
            **kwargs,
        }
        return await self._request(kwargs.pop("path"), data=data, add_marketplace=False)

    @sp_endpoint("/mfn/v0/sellerInputs", method="POST")
    async def get_additional_seller_inputs_old(
        self, shipping_service_id: str, ship_from_address: dict, order_id: str, **kwargs
    ) -> ApiResponse:
        """
        get_additional_seller_inputs_old(self, shipping_service_id, ship_from_address, order_id, **kwargs) -> ApiResponse
        
        get_additional_seller_inputs_old(self, shipping_service_id: str,  ship_from_address: dict, order_id: str,
                                **kwargs) -> ApiResponse
                                Get a list of additional seller inputs required for a ship method. This is generally
                                used for international shipping.
        
        Examples:
            literal blocks::
            
                await MerchantFulfillment().get_additional_seller_inputs_old("value", "value", "value")
        
        Args:
            shipping_service_id:  | required
            ship_from_address:  | required
            order_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        # GetAdditionalSellerInputsRequest
        data = {
            "ShippingServiceId": shipping_service_id,
            "ShipFromAddress": ship_from_address,
            "OrderId": order_id,
        }
        return await self._request(kwargs.pop("path"), data=data, add_marketplace=False)

    @sp_endpoint("/mfn/v0/additionalSellerInputs", method="POST")
    async def get_additional_seller_inputs(
        self, shipping_service_id: str, ship_from_address: dict, order_id: str, **kwargs
    ) -> ApiResponse:
        """
        get_additional_seller_inputs(self, shipping_service_id, ship_from_address, order_id, **kwargs) -> ApiResponse
        
        Gets a list of additional seller inputs required for a ship method. This is generally used for international shipping.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await MerchantFulfillment().get_additional_seller_inputs("value", "value", "value")
        
        Args:
            body: GetAdditionalSellerInputsRequest | required The request schema for the `GetAdditionalSellerInputs` operation.
        
        Returns:
            ApiResponse
        """

        # GetAdditionalSellerInputsRequest
        data = {
            "ShippingServiceId": shipping_service_id,
            "ShipFromAddress": ship_from_address,
            "OrderId": order_id,
        }
        return await self._request(kwargs.pop("path"), data=data, add_marketplace=False)