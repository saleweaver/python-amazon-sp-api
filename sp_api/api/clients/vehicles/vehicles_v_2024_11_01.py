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
from sp_api.api.models.vehicles.vehicles_2024_11_01 import *
from sp_api.base import ApiResponse, Client, fill_query_params, sp_endpoint

T = TypeVar("T")


class Vehicles_V_2024_11_01(Client):
    """
    The Selling Partner API for Automotive. - 2024-11-01

    The Selling Partner API for Automotive provides programmatic access to information needed by selling partners to provide compatibility information about their listed products.
    """

    @overload
    def get_vehicles(
        self, request: GetVehiclesRequest, *args, **kwargs
    ) -> ApiResponse[VehiclesResponse]:
        """
        Get the latest collection of vehicles
        """
        ...

    @sp_endpoint("/catalog/2024-11-01/automotive/vehicles", method="GET")
    def get_vehicles(self, *args, **kwargs) -> ApiResponse[VehiclesResponse]:
        """
        Get the latest collection of vehicles
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetVehiclesRequest):
            request = GetVehiclesRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=VehiclesResponse
        )
