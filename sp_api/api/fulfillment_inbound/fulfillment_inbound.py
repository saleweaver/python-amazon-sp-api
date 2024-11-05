import enum

from sp_api.base import Client, Marketplaces, ApiResponse
from sp_api.base import sp_endpoint, fill_query_params

import urllib.parse


class FulfillmentInboundVersion(str, enum.Enum):
    V_v0 = "v0"
    V_2024_03_20 = "2024-03-20"
    LATEST = "2024-03-20"


class FulfillmentInbound(Client):
    """
    FulfillmentInbound SP-API Client
    :link:

    The Selling Partner API for Fulfillment By Amazon (FBA) Inbound. The FBA Inbound API enables building inbound workflows to create, manage, and send shipments into Amazon's fulfillment network. The API has interoperability with the Send-to-Amazon user interface.
    """
    version: FulfillmentInboundVersion = FulfillmentInboundVersion.V_v0

    def __init__(self, *args, **kwargs):
        if 'version' in kwargs:
            self.version = kwargs.get('version', FulfillmentInboundVersion.V_v0)
        super().__init__(*args, **{**kwargs, 'version': self.version})

    @sp_endpoint("/fba/inbound/<version>/itemsGuidance")
    def item_guidance(self, **kwargs):
        """
        item_guidance(self, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                FulfillmentInbound().item_guidance(**{"MarkeplaceId": "US", "ASINList": ["ASIN1"]})

        Args:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/fba/inbound/<version>/plans", method="POST")
    def plans(self, data, **kwargs):
        """
        plans(self, data, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                res = FulfillmentInbound().plans({
                        "ShipFromAddress": {
                            "Name": "Name",
                            "AddressLine1": "123 any st",
                            "AddressLine2": "AddressLine2",
                            "DistrictOrCounty": "Washtenaw",
                            "City": "Ann Arbor",
                            "StateOrProvinceCode": "MI",
                            "CountryCode": "US",
                            "PostalCode": "48188"
                        },
                        "LabelPrepPreference": "SELLER_LABEL",
                        "ShipToCountryCode": "ShipToCountryCode",
                        "ShipToCountrySubdivisionCode": "ShipToCountrySubdivisionCode",
                        "InboundShipmentPlanRequestItems": [
                            {
                                "SellerSKU": "SellerSKU",
                                "ASIN": "ASIN",
                                "Condition": "NewItem",
                                "Quantity": 1,
                                "QuantityInCase": 1,
                                "PrepDetailsList": [
                                    {
                                        "PrepInstruction": "Polybagging",
                                        "PrepOwner": "AMAZON"
                                    }
                                ]
                            }
                        ]
                    })

        Args:
            data:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), data={**data, **kwargs})

    @sp_endpoint("/fba/inbound/<version>/shipments/{}", method="POST")
    def create_shipment(self, shipment_id, data, **kwargs):
        """
        create_shipment(self, shipment_id, data, **kwargs)

        Examples:
            literal blocks::

                FulfillmentInbound().create_shipment('123', {
                        "InboundShipmentHeader": {
                            "ShipmentName": "43545345",
                            "ShipFromAddress": {
                                "Name": "35435345",
                                "AddressLine1": "123 any st",
                                "DistrictOrCounty": "Washtenaw",
                                "City": "Ann Arbor",
                                "StateOrProvinceCode": "Test",
                                "CountryCode": "US",
                                "PostalCode": "48103"
                            },
                            "DestinationFulfillmentCenterId": "AEB2",
                            "AreCasesRequired": True,
                            "ShipmentStatus": "WORKING",
                            "LabelPrepPreference": "SELLER_LABEL",
                            "IntendedBoxContentsSource": "NONE"
                        },
                        "InboundShipmentItems": [
                            {
                                "ShipmentId": "345453",
                                "SellerSKU": "34534545",
                                "FulfillmentNetworkSKU": "435435435",
                                "QuantityShipped": 0,
                                "QuantityReceived": 0,
                                "QuantityInCase": 0,
                                "ReleaseDate": "2020-04-23",
                                "PrepDetailsList": [
                                    {
                                        "PrepInstruction": "Polybagging",
                                        "PrepOwner": "AMAZON"
                                    }
                                ]
                            }
                        ],
                        "MarketplaceId": "MarketplaceId"
                    })

        Args:
            shipment_id:
            data:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), shipment_id), data={**data, **kwargs}
        )

    @sp_endpoint("/fba/inbound/<version>/shipments/{}", method="PUT")
    def update_shipment(self, shipment_id, data, **kwargs):
        """
        update_shipment(self, shipment_id, data, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                FulfillmentInbound().update_shipment('123', {
                        "MarketplaceId": "ATVPDKIKX0DER",
                        "InboundShipmentHeader": {
                            "ShipmentName": "Shipment for FBA15DJCQ1ZF",
                            "ShipFromAddress": {
                                "Name": "Uma Test",
                                "AddressLine1": "123 any st",
                                "AddressLine2": "",
                                "DistrictOrCounty": "Washtenaw",
                                "City": "Ann Arbor",
                                "StateOrProvinceCode": "CO",
                                "CountryCode": "US",
                                "PostalCode": "48104"
                            },
                            "DestinationFulfillmentCenterId": "ABE2",
                            "ShipmentStatus": "WORKING",
                            "LabelPrepPreference": "SELLER_LABEL"
                        },
                        "InboundShipmentItems": [
                            {
                                "SellerSKU": "PSMM-TEST-SKU-Apr-03_21_17_20-0379",
                                "QuantityShipped": 1
                            }
                        ]
                    })

        Args:
            shipment_id:
            data:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), shipment_id), data={**data, **kwargs}
        )

    @sp_endpoint("/fba/inbound/<version>/shipments/{}/preorder")
    def preorder(self, shipment_id, **kwargs):
        """
        preorder(self, shipment_id, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                FulfillmentInbound().preorder('shipmentId1', MarketplaceId='MarketplaceId1')

        Args:
            shipment_id:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), shipment_id), params=kwargs
        )

    @sp_endpoint("/fba/inbound/<version>/shipments/{}/preorder/confirm", method="PUT")
    def confirm_preorder(self, shipment_id, **kwargs):
        """
        confirm_preorder(self, shipment_id, **kwargs)

        Args:
            shipment_id:
            **kwargs:

        Returns:

        """
        return self._request(
            fill_query_params(kwargs.pop("path"), shipment_id), params=kwargs
        )

    @sp_endpoint("/fba/inbound/<version>/prepInstructions")
    def prep_instruction(self, data, **kwargs):
        """
        prep_instruction(self, data, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                FulfillmentInbound().prep_instruction({"ShipToCountryCode": "US", "ASINList": ["ASIN1"]})

        Args:
            data:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), params={**data, **kwargs})

    @sp_endpoint("/fba/inbound/<version>/shipments/{}/transport")
    def get_transport_information(self, shipment_id, **kwargs):
        """
        get_transport_information(self, shipment_id, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                FulfillmentInbound().get_transport_information('shipmentId1')

        Args:
            shipment_id:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), shipment_id), params=kwargs
        )

    @sp_endpoint("/fba/inbound/<version>/shipments/{}/transport", method="PUT")
    def update_transport_information(self, shipment_id, **kwargs):
        """
        update_transport_information(self, shipment_id, **kwargs) -> ApiResponse

        putTransportDetails

        Args:
            shipment_id:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), shipment_id), data=kwargs
        )

    @sp_endpoint("/fba/inbound/<version>/shipments/{}/transport/void", method="POST")
    def void_transport(self, shipment_id, **kwargs):
        """
        void_transport(self, shipment_id, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                FulfillmentInbound().void_transport('shipmentId1')

        Args:
            shipment_id:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), shipment_id),
            data=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/fba/inbound/<version>/shipments/{}/transport/estimate", method="POST")
    def estimate_transport(self, shipment_id, **kwargs):
        """
        estimate_transport(self, shipment_id, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                FulfillmentInbound().estimate_transport('shipmentId1')

        Args:
            shipment_id:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), shipment_id),
            data=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/fba/inbound/<version>/shipments/{}/transport/confirm", method="POST")
    def confirm_transport(self, shipment_id, **kwargs):
        return self._request(
            fill_query_params(kwargs.pop("path"), shipment_id),
            data=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/fba/inbound/<version>/shipments/{}/labels")
    def get_labels(self, shipment_id, **kwargs):
        """
        get_labels(self, shipment_id, **kwargs)

        Args:
            shipment_id:
            **kwargs:

        Returns:

        """
        return self._request(
            fill_query_params(kwargs.pop("path"), shipment_id),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/fba/inbound/<version>/shipments/{}/billOfLading")
    def bill_of_lading(self, shipment_id, **kwargs):
        """
        bill_of_lading(self, shipment_id, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                FulfillmentInbound().bill_of_lading('shipmentId')

        Args:
            shipment_id:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), shipment_id), params=kwargs
        )

    @sp_endpoint("/fba/inbound/<version>/shipments")
    def get_shipments(self, **kwargs):
        """
        get_shipments(self, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                FulfillmentInbound().get_shipments(QueryType='SHIPMENT', MarketplaceId="ATVPDKIKX0DER")

        Args:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/fba/inbound/<version>/shipments/{}/items")
    def shipment_items_by_shipment(self, shipment_id, **kwargs):
        """
        shipment_items_by_shipment(self, shipment_id, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                FulfillmentInbound().shipment_items_by_shipment('FBA15DJ9SVVD', MarketplaceId="ATVPDKIKX0DER")

        Args:
            shipment_id:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), shipment_id), params=kwargs
        )

    @sp_endpoint("/fba/inbound/<version>/shipmentItems")
    def shipment_items(self, **kwargs):
        """
        shipment_items(self, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                FulfillmentInbound().shipment_items(QueryType='SHIPMENT', MarketplaceId="ATVPDKIKX0DER", NextToken='NextToken')

        Args:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), params=kwargs)

    def get_shipments_by_id(self, shipment_id_list, **kwargs) -> ApiResponse:
        """
        get_shipments_by_id(self, shipment_id_list, **kwargs) -> ApiResponse

            FulfillmentInbound().get_shipments_by_id('FBA16TBYQ6J6')
        Args:
            shipment_id_list: str or [str]
            **kwargs:

        Returns:
            ApiResponse
        """
        if not isinstance(shipment_id_list, str):
            shipment_id_list = ','.join(shipment_id_list)
        return self.get_shipments(QueryType='SHIPMENT', ShipmentIdList=shipment_id_list, **kwargs)

    # 2024-03-20 API
    @sp_endpoint('/inbound/fba/<version>/inboundPlans', method='GET')
    def list_inbound_plans(self, **kwargs) -> ApiResponse:
        """
        list_inbound_plans(self, **kwargs) -> ApiResponse

        Provides a list of inbound plans with minimal information.

    **Usage Plan:**

    | Rate (requests per second) | Burst |
    | ---- | ---- |
    | 1 | 1 |

    The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

            Args:

                key pageSize:integer |  The number of inbound plans to return in the response matching the given query.

                key paginationToken:string |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.

                key status:string |  The status of an inbound plan.

                key sortBy:string |  Sort by field.

                key sortOrder:string |  The sort order.


            Returns:
                ApiResponse:
            """

        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans', method='POST')
    def create_inbound_plan(self, **kwargs) -> ApiResponse:
        """
        create_inbound_plan(self, **kwargs) -> ApiResponse

        Creates an inbound plan. An inbound plan contains all the necessary information to send shipments into Amazon's fufillment network.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 0.05 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            body: | * REQUIRED {'description': 'The `createInboundPlan` request.',
 'example': {'contactInformation': {'email': 'email@email.com', 'phoneNumber': '1234567890'},
             'destinationMarketplaces': ['ATVPDKIKX0DER'],
             'items': [{'expiration': '2024-01-01', 'labelOwner': 'AMAZON', 'manufacturingLotCode': 'manufacturingLotCode', 'msku': 'Sunglasses', 'prepOwner': 'AMAZON', 'quantity': 10}],
             'name': 'My inbound plan',
             'sourceAddress': {'addressLine1': '123 example street', 'addressLine2': 'Floor 19', 'city': 'Toronto', 'companyName': 'Acme', 'countryCode': 'CA', 'name': 'name', 'postalCode': 'M1M1M1', 'stateOrProvinceCode': 'ON'}},
 'properties': {'contactInformation': {'$ref': '#/definitions/ContactInformation'},
                'destinationMarketplaces': {'description': 'Marketplaces where the items need to be shipped to. Currently only one marketplace can be selected in this request.',
                                            'items': {'description': 'The Marketplace ID. Refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids) for a list of possible values.',
                                                      'maxLength': 256,
                                                      'minLength': 1,
                                                      'type': 'string'},
                                            'maxItems': 1,
                                            'minItems': 1,
                                            'type': 'array'},
                'items': {'description': 'Items included in this plan.', 'items': {'$ref': '#/definitions/ItemInput'}, 'maxItems': 2000, 'minItems': 1, 'type': 'array'},
                'name': {'description': "Name for the Inbound Plan. If one isn't provided, a default name will be provided.", 'maxLength': 40, 'minLength': 1, 'type': 'string'},
                'sourceAddress': {'$ref': '#/definitions/Address'}},
 'required': ['contactInformation', 'destinationMarketplaces', 'items', 'sourceAddress'],
 'type': 'object'}


        Returns:
            ApiResponse:
        """

        return self._request(kwargs.pop('path'), data=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}', method='GET')
    def get_inbound_plan(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        get_inbound_plan(self, inboundPlanId, **kwargs) -> ApiResponse

        Fetches the top level information about an inbound plan.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId), params=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/boxes', method='GET')
    def list_inbound_plan_boxes(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        list_inbound_plan_boxes(self, inboundPlanId, **kwargs) -> ApiResponse

        Provides a paginated list of box packages in an inbound plan.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.

            key pageSize:integer |  The number of boxes to return in the response matching the given query.

            key paginationToken:string |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId), params=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/cancellation', method='PUT')
    def cancel_inbound_plan(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        cancel_inbound_plan(self, inboundPlanId, **kwargs) -> ApiResponse

        Cancels an Inbound Plan. Charges may apply if the cancellation is performed outside of a void window. The window
    for Amazon Partnered Carriers is 24 hours for Small Parcel Delivery (SPD) and one hour for Less-Than-Truckload (LTL) carrier shipments.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 0.05 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId), data=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/items', method='GET')
    def list_inbound_plan_items(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        list_inbound_plan_items(self, inboundPlanId, **kwargs) -> ApiResponse

        Provides a paginated list of item packages in an inbound plan.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.

            key pageSize:integer |  The number of items to return in the response matching the given query.

            key paginationToken:string |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId), params=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/packingInformation', method='POST')
    def set_packing_information(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        set_packing_information(self, inboundPlanId, **kwargs) -> ApiResponse

        Sets packing information for an inbound plan. This should be called after an inbound plan is created to populate
    the box level information required for planning and transportation estimates.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 0.05 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.

            body: | * REQUIRED {'description': '`setPackingInformation` request.',
 'example': {'packageGroupings': [{'boxes': [{'boxId': 'boxId',
                                              'contentInformationSource': 'BOX_CONTENT_PROVIDED',
                                              'contents': [{'expiration': '2024-01-01', 'labelOwner': 'AMAZON', 'manufacturingLotCode': 'manufacturingLotCode', 'msku': 'Sunglasses', 'prepOwner': 'AMAZON', 'quantityInBox': 10}],
                                              'dimensions': {'height': 5, 'length': 3, 'unitOfMeasurement': 'CM', 'width': 4},
                                              'quantity': 2,
                                              'templateName': 'templateName',
                                              'weight': {'unit': 'KG', 'value': 5.5}}],
                                   'packingGroupId': 'pg1234abcd-1234-abcd-5678-1234abcd5678',
                                   'shipmentId': 'sh1234abcd-1234-abcd-5678-1234abcd5678'}]},
 'properties': {'packageGroupings': {'description': 'List of packing information for the inbound plan.', 'items': {'$ref': '#/definitions/PackageGroupingInput'}, 'type': 'array'}},
 'type': 'object'}


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId), data=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/packingOptions', method='GET')
    def list_packing_options(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        list_packing_options(self, inboundPlanId, **kwargs) -> ApiResponse

        Retrieves a list of all packing options for an inbound plan. Packing options must first be generated by the corresponding endpoint before becoming available.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.

            key pageSize:integer |  The number of packing options to return in the response matching the given query.

            key paginationToken:string |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId), params=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/packingOptions', method='POST')
    def generate_packing_options(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        generate_packing_options(self, inboundPlanId, **kwargs) -> ApiResponse

        Generates available packing options for the inbound plan.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 0.05 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId), data=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/packingOptions/{}/confirmation', method='POST')
    def confirm_packing_option(self, inboundPlanId, packingOptionId, **kwargs) -> ApiResponse:
        """
        confirm_packing_option(self, inboundPlanId, **kwargs) -> ApiResponse

        Confirms the packing option for an inbound plan.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 0.05 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.

            packingOptionId:string | * REQUIRED Identifier to a packing option.


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId, packingOptionId), data=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/items', method='GET')
    def list_packing_group_items(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        list_packing_group_items(self, inboundPlanId, **kwargs) -> ApiResponse

        Retrieves a list of all items in a packing options's packing group. Packing options must first be generated by the corresponding endpoint before packing group items can be listed.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.

            packingOptionId:string | * REQUIRED Identifier to a packing option.

            packingGroupId:string | * REQUIRED Identifier to a packing group.

            key pageSize:integer |  The number of packing group items to return in the response matching the given query.

            key paginationToken:string |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId), params=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/pallets', method='GET')
    def list_inbound_plan_pallets(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        list_inbound_plan_pallets(self, inboundPlanId, **kwargs) -> ApiResponse

        Provides a paginated list of pallet packages in an inbound plan. An inbound plan will have pallets when the related details are provided after generating Less-Than-Truckload (LTL) carrier shipments.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.

            key pageSize:integer |  The number of pallets to return in the response matching the given query.

            key paginationToken:string |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId), params=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/placementOptions', method='GET')
    def list_placement_options(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        list_placement_options(self, inboundPlanId, **kwargs) -> ApiResponse

        Provides a list of all placement options for an inbound plan. Placement options must first be generated by the corresponding endpoint before becoming available.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.

            key pageSize:integer |  The number of placement options to return in the response matching the given query.

            key paginationToken:string |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId), params=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/placementOptions', method='POST')
    def generate_placement_options(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        generate_placement_options(self, inboundPlanId, **kwargs) -> ApiResponse

        Generates placement options for the inbound plan.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 0.05 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.

            body: | * REQUIRED {'description': 'The `generatePlacementOptions` request.',
 'example': {'customPlacement': [{'items': [{'expiration': '2024-01-01', 'labelOwner': 'AMAZON', 'manufacturingLotCode': 'manufacturingLotCode', 'msku': 'Sunglasses', 'prepOwner': 'AMAZON', 'quantity': 10}], 'warehouseId': 'YYZ14'}]},
 'properties': {'customPlacement': {'description': 'Custom placements options to be added to the plan.', 'items': {'$ref': '#/definitions/CustomPlacementInput'}, 'type': 'array'}},
 'type': 'object'}


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId), data=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/placementOptions/{}/confirmation', method='POST')
    def confirm_placement_option(self, inboundPlanId, placementOptionId, **kwargs) -> ApiResponse:
        """
        confirm_placement_option(self, inboundPlanId, **kwargs) -> ApiResponse

        Confirms the placement option for an inbound plan. Once confirmed, it cannot be changed for the Inbound Plan.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 0.05 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.

            placementOptionId:string | * REQUIRED Identifier to a placement option. A placement option represents the shipment splits and destinations of SKUs.


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId, placementOptionId), data=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/shipments/{}', method='GET')
    def get_shipment(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse:
        """
        get_shipment(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse

        Provides the full details for a specific shipment within an inbound plan. The `transportationOptionId` inside `acceptedTransportationSelection` can be used to retrieve the transportation details for the shipment.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.

            shipmentId:string | * REQUIRED Identifier to a shipment. A shipment contains the boxes and units being inbounded.


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId, shipmentId), params=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/deliveryChallanDocument', method='GET')
    def get_delivery_challan_document(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        get_delivery_challan_document(self, inboundPlanId, **kwargs) -> ApiResponse

        Provide delivery challan document for PCP transportation in IN marketplace.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.

            shipmentId:string | * REQUIRED Identifier to a shipment. A shipment contains the boxes and units being inbounded.


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId), params=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/deliveryWindow', method='POST')
    def update_shipment_delivery_window(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        update_shipment_delivery_window(self, inboundPlanId, **kwargs) -> ApiResponse

        Update the time window that a shipment will be delivered to the warehouse. The window is used to provide the expected time that a non-Amazon partnered carrier will arrive at the warehouse.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.

            shipmentId:string | * REQUIRED Identifier to a shipment. A shipment contains the boxes and units being inbounded.

            body: | * REQUIRED {'description': 'The `updateShipmentDeliveryWindow` request.',
 'example': {'deliveryWindow': {'start': '2024-01-01T00:00Z'}},
 'properties': {'deliveryWindow': {'$ref': '#/definitions/WindowInput', 'description': 'The range of dates within which the seller expects that their shipment will be delivered to Amazon.\n'}},
 'required': ['deliveryWindow'],
 'type': 'object'}


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId), data=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/selfShipAppointmentSlots', method='GET')
    def get_self_ship_appointment_slots(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        get_self_ship_appointment_slots(self, inboundPlanId, **kwargs) -> ApiResponse

        Retrieves a list of available self-ship appointment slots used to drop off a shipment at a warehouse.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.

            shipmentId:string | * REQUIRED Identifier to a shipment. A shipment contains the boxes and units being inbounded.

            key pageSize:integer |  The number of self ship appointment slots to return in the response matching the given query.

            key paginationToken:string |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId), params=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/selfShipAppointmentSlots', method='POST')
    def generate_self_ship_appointment_slots(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        generate_self_ship_appointment_slots(self, inboundPlanId, **kwargs) -> ApiResponse

        Initiates the process of generating the appointment slots list.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.

            shipmentId:string | * REQUIRED Identifier to a shipment. A shipment contains the boxes and units being inbounded.

            body: | * REQUIRED {'description': 'The `generateSelfShipAppointmentSlots` request.',
 'example': {'desiredEndDate': '2024-01-06T14:48:00.000Z', 'desiredStartDate': '2024-01-05T14:48:00.000Z'},
 'properties': {'desiredEndDate': {'description': 'The ISO 8601 datetime with pattern `yyyy-MM-ddTHH:mm:ss.sssZ`.', 'format': 'date-time', 'type': 'string'},
                'desiredStartDate': {'description': 'The ISO 8601 datetime with pattern `yyyy-MM-ddTHH:mm:ss.sssZ`.', 'format': 'date-time', 'type': 'string'}},
 'type': 'object'}


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId), data=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/cancellation', method='PUT')
    def cancel_self_ship_appointment(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        cancel_self_ship_appointment(self, inboundPlanId, **kwargs) -> ApiResponse

        Cancels a self-ship appointment slot against a shipment.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.

            shipmentId:string | * REQUIRED Identifier to a shipment. A shipment contains the boxes and units being inbounded.

            slotId:string | * REQUIRED Identifier to a self-ship appointment slot.

            body: | * REQUIRED {'description': 'The `cancelSelfShipAppointment` request.', 'example': {'reasonComment': 'OTHER'}, 'properties': {'reasonComment': {'$ref': '#/definitions/ReasonComment'}}, 'type': 'object'}


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId), data=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/schedule', method='POST')
    def schedule_self_ship_appointment(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        schedule_self_ship_appointment(self, inboundPlanId, **kwargs) -> ApiResponse

        Confirms or reschedules a self-ship appointment slot against a shipment.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.

            shipmentId:string | * REQUIRED Identifier to a shipment. A shipment contains the boxes and units being inbounded.

            slotId:string | * REQUIRED Identifier to a self-ship appointment slot.

            body: | * REQUIRED {'description': '`scheduleSelfShipAppointment` request.', 'example': {'reasonComment': 'OTHER'}, 'properties': {'reasonComment': {'$ref': '#/definitions/ReasonComment'}}, 'type': 'object'}


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId), data=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/trackingDetails', method='PUT')
    def update_shipment_tracking_details(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        update_shipment_tracking_details(self, inboundPlanId, **kwargs) -> ApiResponse

        Updates a shipment's tracking details.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.

            shipmentId:string | * REQUIRED Identifier to a shipment. A shipment contains the boxes and units being inbounded.

            body: | * REQUIRED {'description': 'The `updateShipmentTrackingDetails` request.',
 'example': {'trackingDetails': {'spdTrackingDetail': {'spdTrackingItems': [{'boxId': 'FBA10ABC0YY100001', 'trackingId': 'FBA10002000'}]}}},
 'properties': {'trackingDetails': {'$ref': '#/definitions/TrackingDetailsInput'}},
 'required': ['trackingDetails'],
 'type': 'object'}


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId), data=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/transportationOptions', method='GET')
    def list_transportation_options(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        list_transportation_options(self, inboundPlanId, **kwargs) -> ApiResponse

        Retrieves all transportation options for a shipment. Transportation options must first be generated by the corresponding endpoint before becoming available.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.

            key pageSize:integer |  The number of transportation options to return in the response matching the given query.

            key paginationToken:string |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.

            key placementOptionId:string |  The placement option to get transportation options for. Either placementOptionId or shipmentId must be specified.

            key shipmentId:string |  The shipment to get transportation options for. Either placementOptionId or shipmentId must be specified.


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId), params=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/transportationOptions', method='POST')
    def generate_transportation_options(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        generate_transportation_options(self, inboundPlanId, **kwargs) -> ApiResponse

        Generates available transportation options for a given placement option.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 0.05 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.

            body: | * REQUIRED {'description': 'The `generateTransportationOptions` request.',
 'example': {'placementOptionId': 'pl1234abcd-1234-abcd-5678-1234abcd5678',
             'shipmentTransportationConfigurations': [{'contactInformation': {'email': 'email@email.com', 'name': 'John Smithy', 'phoneNumber': '1234567890'},
                                                       'palletInformation': {'declaredValue': {'amount': 500, 'code': 'USD'},
                                                                             'freightClass': 'FC_50',
                                                                             'pallets': [{'dimensions': {'height': 5, 'length': 3, 'unitOfMeasurement': 'CM', 'width': 4},
                                                                                          'quantity': 2,
                                                                                          'stackability': 'STACKABLE',
                                                                                          'weight': {'unit': 'KG', 'value': 5.5}}]},
                                                       'readyToShipWindow': {'start': '2024-01-01T00:00Z'},
                                                       'shipmentId': 'sh1234abcd-1234-abcd-5678-1234abcd5678'}]},
 'properties': {'placementOptionId': {'description': 'The placement option to generate transportation options for.', 'maxLength': 38, 'minLength': 38, 'pattern': '^[a-zA-Z0-9-]*$', 'type': 'string'},
                'shipmentTransportationConfigurations': {'description': 'List of shipment transportation configurations.', 'items': {'$ref': '#/definitions/ShipmentTransportationConfiguration'}, 'type': 'array'}},
 'required': ['placementOptionId', 'shipmentTransportationConfigurations'],
 'type': 'object'}


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId), data=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/transportationOptions/confirmation', method='POST')
    def confirm_transportation_options(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        confirm_transportation_options(self, inboundPlanId, **kwargs) -> ApiResponse

        Confirms all the transportation options for an inbound plan. A placement option must be confirmed prior to use of this API. Once confirmed, new transportation options can not be generated or confirmed for the Inbound Plan.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 0.05 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.

            body: | * REQUIRED {'description': 'The `confirmTransportationOptions` request.',
 'example': {'transportationSelections': [{'contactInformation': {'email': 'email@email.com', 'name': 'John Smithy', 'phoneNumber': '1234567890'},
                                           'deliveryWindow': {'start': '2024-01-01T00:00Z'},
                                           'shipmentId': 'sh1234abcd-1234-abcd-5678-1234abcd5678',
                                           'transportationOptionId': 'to1234abcd-1234-abcd-5678-1234abcd5678'}]},
 'properties': {'transportationSelections': {'description': 'Information needed to confirm one of the available transportation options.', 'items': {'$ref': '#/definitions/TransportationSelection'}, 'minItems': 1, 'type': 'array'}},
 'required': ['transportationSelections'],
 'type': 'object'}


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId), data=kwargs)

    @sp_endpoint('/inbound/fba/<version>/items/compliance', method='GET')
    def list_item_compliance_details(self, **kwargs) -> ApiResponse:
        """
        list_item_compliance_details(self, **kwargs) -> ApiResponse

        List the inbound compliance details for MSKUs in a given marketplace.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            key mskus:array | * REQUIRED List of merchant SKUs, a merchant-supplied identifier for a specific SKU.

            key marketplaceId:string | * REQUIRED The Marketplace ID. Refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids) for a list of possible values.


        Returns:
            ApiResponse:
        """

        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint('/inbound/fba/<version>/items/compliance', method='PUT')
    def update_item_compliance_details(self, **kwargs) -> ApiResponse:
        """
        update_item_compliance_details(self, **kwargs) -> ApiResponse

        Update compliance details for list of MSKUs. The details provided here are only used for the IN marketplace compliance validation.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            key marketplaceId:string | * REQUIRED The Marketplace ID. Refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids) for a list of possible values.

            body: | * REQUIRED {'description': 'The `updateItemComplianceDetails` request.',
 'example': {'msku': 'Sunglasses', 'taxDetails': {'declaredValue': {'amount': 5.5, 'code': 'CAD'}, 'hsnCode': 'hsnCode'}},
 'properties': {'msku': {'description': 'The merchant SKU, a merchant-supplied identifier for a specific SKU.', 'maxLength': 40, 'minLength': 1, 'type': 'string'}, 'taxDetails': {'$ref': '#/definitions/TaxDetails'}},
 'required': ['msku', 'taxDetails'],
 'type': 'object'}


        Returns:
            ApiResponse:
        """

        return self._request(kwargs.pop('path'), data=kwargs)

    @sp_endpoint('/inbound/fba/<version>/operations/{}', method='GET')
    def get_inbound_operation_status(self, operationId, **kwargs) -> ApiResponse:
        """
        get_inbound_operation_status(self, operationId, **kwargs) -> ApiResponse

        Gets the status of the processing of an asynchronous API call.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            operationId:string | * REQUIRED Identifier to an asynchronous operation.


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), operationId), params=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/shipments/{}/deliveryWindowOptions', method='POST')
    def generate_delivery_window_options(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse:
        """
        def generate_delivery_window_options(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse:

        Generates available delivery window options for a given shipment.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 2 | 30 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier of an inbound plan.
            shipmentId:string | * REQUIRED The shipment to generate delivery window options for.


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId, shipmentId), params=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/shipments/{}/deliveryWindowOptions', method='GET')
    def list_delivery_window_options(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse:
        """
        def generate_delivery_window_options(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse:

        Retrieves all delivery window options for a shipment. Delivery window options must first be generated by the generateDeliveryWindowOptions operation before becoming available.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 2 | 30 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier of an inbound plan.
            shipmentId:string | * REQUIRED The shipment to generate delivery window options for.


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId, shipmentId), params=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/shipments/{}/deliveryWindowOptions/{}/confirmation', method='POST')
    def confirm_delivery_window_options(self, inboundPlanId, shipmentId, deliveryWindowOptionId, **kwargs) -> ApiResponse:
        """
        def confirm_delivery_window_options(self, inboundPlanId, shipmentId, deliveryWindowOptionId, **kwargs) -> ApiResponse:

        Confirms the delivery window option for chosen shipment within an inbound plan. A placement option must be confirmed prior to use of this API. Once confirmed, new delivery window options cannot be generated, but the chosen delivery window option can be updated before shipment closure. The window is used to provide the expected time when a shipment will arrive at the warehouse. All transportation options which have the program CONFIRMED_DELIVERY_WINDOW require a delivery window to be confirmed prior to transportation option confirmation.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 2 | 30 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier of an inbound plan.
            shipmentId:string | * REQUIRED The shipment to generate delivery window options for.
            deliveryWindowOptionId:string | REQUIRED The id of the delivery window option to be confirmed.


        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId, shipmentId, deliveryWindowOptionId), params=kwargs)

    @sp_endpoint('/inbound/fba/<version>/inboundPlans/{}/shipments/{}/items', method='GET')
    def list_shipment_items(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse:
        """
        list_shipment_items(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse

        Provides a paginated list of item packages in a shipment.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 2 | 30 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            inboundPlanId:string | * REQUIRED Identifier to an inbound plan.

            shipmentId:string | * REQUIRED Identifier of a shipment. A shipment contains the boxes and units being inbounded.

            key pageSize:integer |  The number of items to return in the response matching the given query.

            key paginationToken:string |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.


        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop('path'), inboundPlanId, shipmentId), params=kwargs)

    @sp_endpoint('/inbound/fba/<version>/items/labels', method='POST')
    def create_marketplace_item_labels(self, **kwargs) -> ApiResponse:
        """
        create_marketplace_item_labels(self, **kwargs) -> ApiResponse

        For a given marketplace - creates labels for a list of MSKUs.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 2 | 30 |

The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to Usage Plans and Rate Limits in the Selling Partner API.
        Args:

            height:number | *OPTIONAL The height of the item label.
            labelType: | *RERQUIRED ndicates the type of print type for a given label.
            localeCode:string | *OPTIONAL The locale code constructed from ISO 639 language code and ISO 3166-1 alpha-2 standard of country codes separated by an underscore character.
            marketplaceId:string | *REQUIRED The marketplace ID.
            mskuQuantities:array | *REQUIRED Represents the quantity of an MSKU to print item labels for.
            pageType: | *OPTIONAL The page type to use to print the labels.
            width:number | *OPTIONAL The width of the item label.

        Returns:
            ApiResponse:
        """

        return self._request(kwargs.pop('path'), data=kwargs)

    @sp_endpoint('/inbound/fba/<version>/items/prepDetails', method='GET')
    def list_prep_details(self, **kwargs) -> ApiResponse:
        """
        list_prep_details(self, **kwargs) -> ApiResponse:

        Get preparation details for a list of MSKUs in a specified marketplace.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 2 | 30 |

The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to Usage Plans and Rate Limits in the Selling Partner API.
        Args:
            marketplaceId:string | *REQUIRED The marketplace ID.
            mskus:array | *REQUIRED A list of merchant SKUs, a merchant-supplied identifier of a specific SKU.

        Returns:
            ApiResponse:
        """

        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint('/inbound/fba/<version>/items/prepDetails', method='POST')
    def set_prep_details(self, **kwargs) -> ApiResponse:
        """
        set_prep_details(self, **kwargs) -> ApiResponse:

        Set the preparation details for a list of MSKUs in a specified marketplace.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 2 | 30 |

The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to Usage Plans and Rate Limits in the Selling Partner API.
        Args:

            marketplaceId:string | *REQUIRED The marketplace ID.
            mskuPrepDetails:array | *REQUIRED A list of MSKUs and related prep details.

        Returns:
            ApiResponse:
        """

        return self._request(kwargs.pop('path'), data=kwargs)

