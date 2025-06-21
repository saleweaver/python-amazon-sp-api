"""
Generated API client from Swagger/OpenAPI specification.
This file was auto-generated. Do not edit manually.
"""

import json
from typing import (Any, Dict, Generic, List, Optional, TypeVar, Union, cast,
                    overload)

import httpx
from pydantic import BaseModel
# Import all models
from sp_api.api.models.supply_sources.supply_sources_2020_07_01 import *
from sp_api.base import ApiResponse, Client, fill_query_params, sp_endpoint

T = TypeVar("T")


class SupplySources_V_2020_07_01(Client):
    """
    Selling Partner API for Supply Sources - 2020-07-01

    Manage configurations and capabilities of seller supply sources.
    """

    @overload
    def get_supply_sources(
        self, request: GetSupplySourcesRequest, *args, **kwargs
    ) -> ApiResponse[GetSupplySourcesResponse]:
        """
        The path to retrieve paginated supply sources.
        """
        ...

    @sp_endpoint("/supplySources/2020-07-01/supplySources", method="GET")
    def get_supply_sources(
        self, *args, **kwargs
    ) -> ApiResponse[GetSupplySourcesResponse]:
        """
        The path to retrieve paginated supply sources.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetSupplySourcesRequest):
            request = GetSupplySourcesRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=GetSupplySourcesResponse
        )

    @overload
    def create_supply_source(
        self, request: CreateSupplySourceRequest, *args, **kwargs
    ) -> ApiResponse[CreateSupplySourceResponse]:
        """
        Create a new supply source.
        """
        ...

    @sp_endpoint("/supplySources/2020-07-01/supplySources", method="POST")
    def create_supply_source(
        self, *args, **kwargs
    ) -> ApiResponse[CreateSupplySourceResponse]:
        """
        Create a new supply source.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, CreateSupplySourceRequest):
            request = CreateSupplySourceRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=CreateSupplySourceResponse,
        )

    @overload
    def get_supply_source(
        self, request: GetSupplySourceRequest, *args, **kwargs
    ) -> ApiResponse[SupplySource]:
        """
        Retrieve a supply source.
        """
        ...

    @sp_endpoint(
        "/supplySources/2020-07-01/supplySources/{supplySourceId}", method="GET"
    )
    def get_supply_source(self, *args, **kwargs) -> ApiResponse[SupplySource]:
        """
        Retrieve a supply source.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetSupplySourceRequest):
            request = GetSupplySourceRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=SupplySource
        )

    @overload
    def update_supply_source(
        self, request: UpdateSupplySourceRequest, *args, **kwargs
    ) -> ApiResponse[ErrorList]:
        """
        Update the configuration and capabilities of a supply source.
        """
        ...

    @sp_endpoint(
        "/supplySources/2020-07-01/supplySources/{supplySourceId}", method="PUT"
    )
    def update_supply_source(self, *args, **kwargs) -> ApiResponse[ErrorList]:
        """
        Update the configuration and capabilities of a supply source.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, UpdateSupplySourceRequest):
            request = UpdateSupplySourceRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=ErrorList
        )

    @overload
    def archive_supply_source(
        self, request: ArchiveSupplySourceRequest, *args, **kwargs
    ) -> ApiResponse[ErrorList]:
        """
        Archive a supply source, making it inactive. Cannot be undone.
        """
        ...

    @sp_endpoint(
        "/supplySources/2020-07-01/supplySources/{supplySourceId}", method="DELETE"
    )
    def archive_supply_source(self, *args, **kwargs) -> ApiResponse[ErrorList]:
        """
        Archive a supply source, making it inactive. Cannot be undone.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, ArchiveSupplySourceRequest):
            request = ArchiveSupplySourceRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=ErrorList
        )

    @overload
    def update_supply_source_status(
        self, request: UpdateSupplySourceStatusRequest, *args, **kwargs
    ) -> ApiResponse[ErrorList]:
        """
        Update the status of a supply source.
        """
        ...

    @sp_endpoint(
        "/supplySources/2020-07-01/supplySources/{supplySourceId}/status", method="PUT"
    )
    def update_supply_source_status(self, *args, **kwargs) -> ApiResponse[ErrorList]:
        """
        Update the status of a supply source.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, UpdateSupplySourceStatusRequest):
            request = UpdateSupplySourceStatusRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=ErrorList
        )
