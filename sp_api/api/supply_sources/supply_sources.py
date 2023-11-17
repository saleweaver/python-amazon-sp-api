from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class SupplySources(Client):
    """
    SupplySources SP-API Client
    :link: 

    Manage configurations and capabilities of seller supply sources.
    """

    @sp_endpoint('/supplySources/2020-07-01/supplySources', method='GET')
    def get_supply_sources(self, **kwargs) -> ApiResponse:
        """
        get_supply_sources(self, **kwargs) -> ApiResponse

        The path to retrieve paginated supply sources.

        Args:
        
            key nextPageToken:string |  The pagination token to retrieve a specific page of results.
        
            key pageSize:number |  The number of supply sources to return per paginated request.
        

        Returns:
            ApiResponse:
        """

        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint('/supplySources/2020-07-01/supplySources', method='POST')
    def create_supply_source(self, **kwargs) -> ApiResponse:
        """
        create_supply_source(self, **kwargs) -> ApiResponse

        Create a new supply source.

        Args:
        
            payload: | * REQUIRED {'description': 'A request to create a supply source.',
 'properties': {'address': {'$ref': '#/definitions/Address'}, 'alias': {'$ref': '#/definitions/SupplySourceAlias'}, 'supplySourceCode': {'$ref': '#/definitions/SupplySourceCode'}},
 'required': ['address', 'supplySourceCode', 'alias'],
 'type': 'object'}
        

        Returns:
            ApiResponse:
        """

        return self._request(kwargs.pop('path'), data=kwargs)

    @sp_endpoint('/supplySources/2020-07-01/supplySources/{}', method='GET')
    def get_supply_source(self, supplySourceId, **kwargs) -> ApiResponse:
        """
        get_supply_source(self, supplySourceId, **kwargs) -> ApiResponse

        Retrieve a supply source.

        Args:
        
            supplySourceId:string | * REQUIRED The unique identifier of a supply source.
        

        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), supplySourceId), params=kwargs)

    @sp_endpoint('/supplySources/2020-07-01/supplySources/{}', method='PUT')
    def update_supply_source(self, supplySourceId, **kwargs) -> ApiResponse:
        """
        update_supply_source(self, supplySourceId, **kwargs) -> ApiResponse

        Update the configuration and capabilities of a supply source.

        Args:
        
            supplySourceId:string | * REQUIRED The unique identitier of a supply source.
        
            payload: |  {'description': 'A request to update the configuration and capabilities of a supply source.',
                         'properties': {'alias': {'$ref': '#/definitions/SupplySourceAlias'}, 'capabilities': {'$ref': '#/definitions/SupplySourceCapabilities'}, 'configuration': {'$ref': '#/definitions/SupplySourceConfiguration'}},
                         'type': 'object'}
        

        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), supplySourceId), data=kwargs)

    @sp_endpoint('/supplySources/2020-07-01/supplySources/{}', method='DELETE')
    def archive_supply_source(self, supplySourceId, **kwargs) -> ApiResponse:
        """
        archive_supply_source(self, supplySourceId, **kwargs) -> ApiResponse

        Archive a supply source, making it inactive. Cannot be undone.

        Args:
        
            supplySourceId:string | * REQUIRED The unique identifier of a supply source.
        

        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), supplySourceId), data=kwargs)

    @sp_endpoint('/supplySources/2020-07-01/supplySources/{}/status', method='PUT')
    def update_supply_source_status(self, supplySourceId, **kwargs) -> ApiResponse:
        """
        update_supply_source_status(self, supplySourceId, **kwargs) -> ApiResponse

        Update the status of a supply source.

        Args:
        
            supplySourceId:string | * REQUIRED The unique identifier of a supply source.
        
            payload: |  {'description': 'A request to update the status of a supply source.', 'properties': {'status': {'$ref': '#/definitions/SupplySourceStatus'}}, 'type': 'object'}
        

        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), supplySourceId), data=kwargs)
