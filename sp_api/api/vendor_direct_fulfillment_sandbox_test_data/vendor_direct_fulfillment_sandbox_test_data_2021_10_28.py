from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class VendorDirectFulfillmentSandboxTestDataV20211028(Client):
    """
    VendorDirectFulfillmentSandboxTestData SP-API Client
    :link:

    The Selling Partner API for Vendor Direct Fulfillment Sandbox Test Data provides programmatic access to vendor direct fulfillment sandbox test data.
    """

    @sp_endpoint("/vendor/directFulfillment/sandbox/2021-10-28/orders", method="POST")
    def generate_order_scenarios(self, **kwargs) -> ApiResponse:
        """
        generate_order_scenarios(self, **kwargs) -> ApiResponse
        
        Submits a request to generate test order data for Vendor Direct Fulfillment API entities.
        
        Args:
            body: | * REQUIRED {'description': 'The request body for the generateOrderScenarios operation.',
         'properties': {'orders': {'description': 'The list of test orders requested as indicated by party identifiers.', 'items': {'$ref': '#/definitions/OrderScenarioRequest'}, 'type': 'array'}},
         'type': 'object'}
        
        Returns:
            ApiResponse:
        """
        return self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)

    @sp_endpoint("/vendor/directFulfillment/sandbox/2021-10-28/transactions/{transactionId}", method="GET")
    def get_order_scenarios(self, transactionId, **kwargs) -> ApiResponse:
        """
        get_order_scenarios(self, transactionId, **kwargs) -> ApiResponse
        
        Returns the status of the transaction indicated by the specified transactionId. If the transaction was successful, also returns the requested test order data.
        
        Args:
            transactionId:string | * REQUIRED The transaction identifier returned in the response to the generateOrderScenarios operation.
        
        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path"), transactionId), params=kwargs, add_marketplace=False)
