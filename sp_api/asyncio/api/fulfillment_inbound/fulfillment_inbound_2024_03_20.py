from sp_api.base import ApiResponse
from sp_api.asyncio.base import AsyncBaseClient
from sp_api.base import sp_endpoint, fill_query_params

import urllib.parse
from sp_api.util import ensure_csv


class FulfillmentInboundV20240320(AsyncBaseClient):
    """
    FulfillmentInbound SP-API Client
    :link:

    The Selling Partner API for Fulfillment By Amazon (FBA) Inbound. The FBA Inbound API enables building inbound workflows to create, manage, and send shipments into Amazon's fulfillment network. The API has interoperability with the Send-to-Amazon user interface.
    """

    @sp_endpoint("/fba/inbound/2024-03-20/itemsGuidance")
    async def item_guidance(self, **kwargs):
        """
        item_guidance(self, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().item_guidance()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/fba/inbound/2024-03-20/plans", method="POST")
    async def plans(self, data, **kwargs):
        """
        plans(self, data, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().plans("value")
        
        Args:
            data:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), data={**data, **kwargs})

    @sp_endpoint("/fba/inbound/2024-03-20/shipments/{}", method="POST")
    async def create_shipment(self, shipment_id, data, **kwargs):
        """
        create_shipment(self, shipment_id, data, **kwargs) -> ApiResponse
        
        create_shipment(self, shipment_id, data, **kwargs)
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().create_shipment("value", "value")
        
        Args:
            shipment_id:  | required
            data:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), shipment_id), data={**data, **kwargs}
        )

    @sp_endpoint("/fba/inbound/2024-03-20/shipments/{}", method="PUT")
    async def update_shipment(self, shipment_id, data, **kwargs):
        """
        update_shipment(self, shipment_id, data, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().update_shipment("value", "value")
        
        Args:
            shipment_id:  | required
            data:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), shipment_id), data={**data, **kwargs}
        )

    @sp_endpoint(
        "/inbound/fba/2024-03-20/inboundPlans/{}/shipments/{}/name", method="PUT"
    )
    async def update_shipment_name(self, inboundPlanId, shipmentId, **kwargs):
        """
        update_shipment_name(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse
        
        Updates the name of an existing shipment.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().update_shipment_name("value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            shipmentId: object | required Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            body: UpdateShipmentNameRequest | required The body of the request to `updateShipmentName`.
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId),
            data=kwargs,
        )

    @sp_endpoint("/fba/inbound/2024-03-20/shipments/{}/preorder")
    async def preorder(self, shipment_id, **kwargs):
        """
        preorder(self, shipment_id, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().preorder("value")
        
        Args:
            shipment_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), shipment_id), params=kwargs
        )

    @sp_endpoint("/fba/inbound/2024-03-20/shipments/{}/preorder/confirm", method="PUT")
    async def confirm_preorder(self, shipment_id, **kwargs):
        """
        confirm_preorder(self, shipment_id, **kwargs) -> ApiResponse
        
        confirm_preorder(self, shipment_id, **kwargs)
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().confirm_preorder("value")
        
        Args:
            shipment_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), shipment_id), params=kwargs
        )

    @sp_endpoint("/fba/inbound/2024-03-20/prepInstructions")
    async def prep_instruction(self, data, **kwargs):
        """
        prep_instruction(self, data, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().prep_instruction("value")
        
        Args:
            data:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), params={**data, **kwargs})

    @sp_endpoint("/fba/inbound/2024-03-20/shipments/{}/transport")
    async def get_transport_information(self, shipment_id, **kwargs):
        """
        get_transport_information(self, shipment_id, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().get_transport_information("value")
        
        Args:
            shipment_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), shipment_id), params=kwargs
        )

    @sp_endpoint("/fba/inbound/2024-03-20/shipments/{}/transport", method="PUT")
    async def update_transport_information(self, shipment_id, **kwargs):
        """
        update_transport_information(self, shipment_id, **kwargs) -> ApiResponse
        
        putTransportDetails
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().update_transport_information("value")
        
        Args:
            shipment_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), shipment_id), data=kwargs
        )

    @sp_endpoint("/fba/inbound/2024-03-20/shipments/{}/transport/void", method="POST")
    async def void_transport(self, shipment_id, **kwargs):
        """
        void_transport(self, shipment_id, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().void_transport("value")
        
        Args:
            shipment_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), shipment_id),
            data=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint(
        "/fba/inbound/2024-03-20/shipments/{}/transport/estimate", method="POST"
    )
    async def estimate_transport(self, shipment_id, **kwargs):
        """
        estimate_transport(self, shipment_id, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().estimate_transport("value")
        
        Args:
            shipment_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), shipment_id),
            data=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/fba/inbound/2024-03-20/shipments/{}/transport/confirm", method="POST")
    async def confirm_transport(self, shipment_id, **kwargs):
        return await self._request(
            fill_query_params(kwargs.pop("path"), shipment_id),
            data=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/fba/inbound/2024-03-20/shipments/{}/labels")
    async def get_labels(self, shipment_id, **kwargs):
        """
        get_labels(self, shipment_id, **kwargs) -> ApiResponse
        
        get_labels(self, shipment_id, **kwargs)
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().get_labels("value")
        
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

    @sp_endpoint("/fba/inbound/2024-03-20/shipments/{}/billOfLading")
    async def bill_of_lading(self, shipment_id, **kwargs):
        """
        bill_of_lading(self, shipment_id, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().bill_of_lading("value")
        
        Args:
            shipment_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), shipment_id), params=kwargs
        )

    @sp_endpoint("/fba/inbound/2024-03-20/shipments")
    async def get_shipments(self, **kwargs):
        """
        get_shipments(self, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().get_shipments()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/fba/inbound/2024-03-20/shipments/{}/items")
    async def shipment_items_by_shipment(self, shipment_id, **kwargs):
        """
        shipment_items_by_shipment(self, shipment_id, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().shipment_items_by_shipment("value")
        
        Args:
            shipment_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), shipment_id), params=kwargs
        )

    @sp_endpoint("/fba/inbound/2024-03-20/shipmentItems")
    async def shipment_items(self, **kwargs):
        """
        shipment_items(self, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().shipment_items()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), params=kwargs)

    async def get_shipments_by_id(self, shipment_id_list, **kwargs) -> ApiResponse:
        """
        get_shipments_by_id(self, shipment_id_list, **kwargs) -> ApiResponse
        
        FulfillmentInbound().get_shipments_by_id('FBA16TBYQ6J6')
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().get_shipments_by_id("value")
        
        Args:
            shipment_id_list:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        shipment_id_list = ensure_csv(shipment_id_list)
        return self.get_shipments(
            QueryType="SHIPMENT", ShipmentIdList=shipment_id_list, **kwargs
        )

    # 2024-03-20 API
    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans", method="GET")
    async def list_inbound_plans(self, **kwargs) -> ApiResponse:
        """
        list_inbound_plans(self, **kwargs) -> ApiResponse
        
        Provides a list of inbound plans with minimal information.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().list_inbound_plans()
        
        Args:
            key pageSize: object |  The number of inbound plans to return in the response matching the given query.
            key paginationToken: object |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.
            key status: object |  The status of an inbound plan.
            key sortBy: object |  Sort by field.
            key sortOrder: object |  The sort order.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans", method="POST")
    async def create_inbound_plan(self, **kwargs) -> ApiResponse:
        """
        create_inbound_plan(self, **kwargs) -> ApiResponse
        
        Creates an inbound plan. An inbound plan contains all the necessary information to send shipments into Amazon's fufillment network.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().create_inbound_plan()
        
        Args:
            body: CreateInboundPlanRequest | required The body of the request to `createInboundPlan`.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}", method="GET")
    async def get_inbound_plan(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        get_inbound_plan(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Fetches the top level information about an inbound plan.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().get_inbound_plan("value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), params=kwargs
        )

    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}/boxes", method="GET")
    async def list_inbound_plan_boxes(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        list_inbound_plan_boxes(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Provides a paginated list of box packages in an inbound plan.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().list_inbound_plan_boxes("value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            key pageSize: object |  The number of boxes to return in the response matching the given query.
            key paginationToken: object |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), params=kwargs
        )

    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}/cancellation", method="PUT")
    async def cancel_inbound_plan(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        cancel_inbound_plan(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Cancels an Inbound Plan. Charges may apply if the cancellation is performed outside of a void window. The window for Amazon Partnered Carriers is 24 hours for Small Parcel Delivery (SPD) and one hour for Less-Than-Truckload (LTL) carrier shipments.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().cancel_inbound_plan("value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), data=kwargs
        )

    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}/items", method="GET")
    async def list_inbound_plan_items(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        list_inbound_plan_items(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Provides a paginated list of item packages in an inbound plan.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().list_inbound_plan_items("value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            key pageSize: object |  The number of items to return in the response matching the given query.
            key paginationToken: object |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), params=kwargs
        )

    @sp_endpoint(
        "/inbound/fba/2024-03-20/inboundPlans/{}/packingInformation", method="POST"
    )
    async def set_packing_information(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        set_packing_information(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Sets packing information for an inbound plan. This should be called after an inbound plan is created to populate the box level information required for planning and transportation estimates.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().set_packing_information("value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            body: SetPackingInformationRequest | required The body of the request to `setPackingInformation`.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), data=kwargs
        )

    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}/packingOptions", method="GET")
    async def list_packing_options(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        list_packing_options(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Retrieves a list of all packing options for an inbound plan. Packing options must first be generated by the corresponding operation before becoming available.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().list_packing_options("value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            key pageSize: object |  The number of packing options to return in the response matching the given query.
            key paginationToken: object |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), params=kwargs
        )

    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}/packingOptions", method="POST")
    async def generate_packing_options(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        generate_packing_options(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Generates available packing options for the inbound plan.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().generate_packing_options("value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), data=kwargs
        )

    @sp_endpoint(
        "/inbound/fba/2024-03-20/inboundPlans/{}/packingOptions/{}/confirmation",
        method="POST",
    )
    async def confirm_packing_option(
        self, inboundPlanId, packingOptionId, **kwargs
    ) -> ApiResponse:
        """
        confirm_packing_option(self, inboundPlanId, packingOptionId, **kwargs) -> ApiResponse
        
        Confirms the packing option for an inbound plan.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().confirm_packing_option("value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            packingOptionId: object | required Identifier of a packing option.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId, packingOptionId),
            data=kwargs,
        )

    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}/packingGroups/{}/items", method="GET")
    async def list_packing_group_items(self, inboundPlanId, packingGroupId, **kwargs) -> ApiResponse:
        """
        list_packing_group_items(self, inboundPlanId, packingGroupId, **kwargs) -> ApiResponse
        
        Retrieves a page of items in a given packing group. Packing options must first be generated by the corresponding operation before packing group items can be listed.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().list_packing_group_items("value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            packingGroupId: object | required Identifier of a packing group.
            key pageSize: object |  The number of packing group items to return in the response matching the given query.
            key paginationToken: object |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId, packingGroupId), params=kwargs
        )

    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}/pallets", method="GET")
    async def list_inbound_plan_pallets(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        list_inbound_plan_pallets(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Provides a paginated list of pallet packages in an inbound plan. An inbound plan will have pallets when the related details are provided after generating Less-Than-Truckload (LTL) carrier shipments.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().list_inbound_plan_pallets("value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            key pageSize: object |  The number of pallets to return in the response matching the given query.
            key paginationToken: object |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), params=kwargs
        )

    @sp_endpoint(
        "/inbound/fba/2024-03-20/inboundPlans/{}/placementOptions", method="GET"
    )
    async def list_placement_options(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        list_placement_options(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Provides a list of all placement options for an inbound plan. Placement options must first be generated by the corresponding operation before becoming available.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().list_placement_options("value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            key pageSize: object |  The number of placement options to return in the response matching the given query.
            key paginationToken: object |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), params=kwargs
        )

    @sp_endpoint(
        "/inbound/fba/2024-03-20/inboundPlans/{}/placementOptions", method="POST"
    )
    async def generate_placement_options(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        generate_placement_options(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Generates placement options for the inbound plan.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().generate_placement_options("value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            body: GeneratePlacementOptionsRequest | required The body of the request to `generatePlacementOptions`.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), data=kwargs
        )

    @sp_endpoint(
        "/inbound/fba/2024-03-20/inboundPlans/{}/placementOptions/{}/confirmation",
        method="POST",
    )
    async def confirm_placement_option(
        self, inboundPlanId, placementOptionId, **kwargs
    ) -> ApiResponse:
        """
        confirm_placement_option(self, inboundPlanId, placementOptionId, **kwargs) -> ApiResponse
        
        Confirms the placement option for an inbound plan. Once confirmed, it cannot be changed for the Inbound Plan.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().confirm_placement_option("value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            placementOptionId: object | required The identifier of a placement option. A placement option represents the shipment splits and destinations of SKUs.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId, placementOptionId),
            data=kwargs,
        )

    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}/shipments/{}", method="GET")
    async def get_shipment(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse:
        """
        get_shipment(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse
        
        Provides the full details for a specific shipment within an inbound plan. The `transportationOptionId` inside `acceptedTransportationSelection` can be used to retrieve the transportation details for the shipment.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().get_shipment("value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            shipmentId: object | required Identifier of a shipment. A shipment contains the boxes and units being inbounded.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId),
            params=kwargs,
        )

    async def get_delivery_challan_document(
        self, inboundPlanId, shipmentId, **kwargs
    ) -> ApiResponse:
        """
        get_delivery_challan_document(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse
        
        Provide delivery challan document for PCP transportation in IN marketplace.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().get_delivery_challan_document("value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            shipmentId: object | required Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self.get_delivery_challan_document_get(
            inboundPlanId, shipmentId, **kwargs
        )

    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}/deliveryWindow", method="POST")
    async def update_shipment_delivery_window(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        update_shipment_delivery_window(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Update the time window that a shipment will be delivered to the warehouse. The window is used to provide the expected time that a non-Amazon partnered carrier will arrive at the warehouse.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().update_shipment_delivery_window("value")
        
        Args:
            inboundPlanId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), data=kwargs
        )

    async def get_self_ship_appointment_slots(
        self, inboundPlanId, shipmentId, **kwargs
    ) -> ApiResponse:
        """
        get_self_ship_appointment_slots(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse
        
        Retrieves a list of available self-ship appointment slots used to drop off a shipment at a warehouse.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().get_self_ship_appointment_slots("value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            shipmentId: object | required Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self.get_self_ship_appointment_slots_get(
            inboundPlanId, shipmentId, **kwargs
        )

    async def generate_self_ship_appointment_slots(
        self, inboundPlanId, shipmentId, **kwargs
    ) -> ApiResponse:
        """
        generate_self_ship_appointment_slots(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse
        
        Initiates the process of generating the appointment slots list.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().generate_self_ship_appointment_slots("value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            shipmentId: object | required Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self.generate_self_ship_appointment_slots_post(
            inboundPlanId, shipmentId, **kwargs
        )


    async def schedule_self_ship_appointment(
        self, inboundPlanId, shipmentId, slotId, **kwargs
    ) -> ApiResponse:
        """
        schedule_self_ship_appointment(self, inboundPlanId, shipmentId, slotId, **kwargs) -> ApiResponse
        
        Confirms or reschedules a self-ship appointment slot against a shipment.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().schedule_self_ship_appointment("value", "value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            shipmentId: object | required Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            slotId: object | required An identifier to a self-ship appointment slot.
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self.schedule_self_ship_appointment_post(
            inboundPlanId, shipmentId, slotId, **kwargs
        )

    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}/trackingDetails", method="PUT")
    async def update_shipment_tracking_details(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        update_shipment_tracking_details(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Updates a shipment's tracking details.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().update_shipment_tracking_details("value")
        
        Args:
            inboundPlanId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), data=kwargs
        )

    @sp_endpoint(
        "/inbound/fba/2024-03-20/inboundPlans/{}/transportationOptions", method="GET"
    )
    async def list_transportation_options(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        list_transportation_options(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Retrieves all transportation options for a shipment. Transportation options must first be generated by the `generateTransportationOptions` operation before becoming available.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().list_transportation_options("value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            key pageSize: object |  The number of transportation options to return in the response matching the given query.
            key paginationToken: object |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.
            key placementOptionId: object |  The placement option to get transportation options for. Either `placementOptionId` or `shipmentId` must be specified.
            key shipmentId: object |  The shipment to get transportation options for. Either `placementOptionId` or `shipmentId` must be specified.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), params=kwargs
        )

    @sp_endpoint(
        "/inbound/fba/2024-03-20/inboundPlans/{}/transportationOptions", method="POST"
    )
    async def generate_transportation_options(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        generate_transportation_options(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Generates available transportation options for a given placement option.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().generate_transportation_options("value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            body: GenerateTransportationOptionsRequest | required The body of the request to `generateTransportationOptions`.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), data=kwargs
        )

    @sp_endpoint(
        "/inbound/fba/2024-03-20/inboundPlans/{}/transportationOptions/confirmation",
        method="POST",
    )
    async def confirm_transportation_options(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        confirm_transportation_options(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Confirms all the transportation options for an inbound plan. A placement option must be confirmed prior to use of this API. Once confirmed, new transportation options can not be generated or confirmed for the Inbound Plan.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().confirm_transportation_options("value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            body: ConfirmTransportationOptionsRequest | required The body of the request to `confirmTransportationOptions`.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), data=kwargs
        )

    @sp_endpoint("/inbound/fba/2024-03-20/items/compliance", method="GET")
    async def list_item_compliance_details(self, **kwargs) -> ApiResponse:
        """
        list_item_compliance_details(self, **kwargs) -> ApiResponse
        
        List the inbound compliance details for MSKUs in a given marketplace.
        
        **Note:** MSKUs that contain certain characters must be encoded. For more information, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).
        
        The following characters must be double percent encoded:
        
        - `%`
        - `+`
        - `,`
        
        **Examples:** An MSKU value of `test%msku` is encoded as `test%2525msku`. An MSKU value of `test,msku` is encoded as `test%252Cmsku`.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().list_item_compliance_details()
        
        Args:
            key mskus: object | required A list of merchant SKUs, a merchant-supplied identifier of a specific SKU.
            key marketplaceId: object | required The Marketplace ID. For a list of possible values, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/inbound/fba/2024-03-20/items/compliance", method="PUT")
    async def update_item_compliance_details(self, **kwargs) -> ApiResponse:
        """
        update_item_compliance_details(self, **kwargs) -> ApiResponse
        
        Update compliance details for a list of MSKUs. The details provided here are only used for the India (IN - A21TJRUUN4KGV) marketplace compliance validation.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().update_item_compliance_details()
        
        Args:
            key marketplaceId: object | required The Marketplace ID. For a list of possible values, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
            body: UpdateItemComplianceDetailsRequest | required The body of the request to `updateItemComplianceDetails`.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/inbound/fba/2024-03-20/operations/{}", method="GET")
    async def get_inbound_operation_status(self, operationId, **kwargs) -> ApiResponse:
        """
        get_inbound_operation_status(self, operationId, **kwargs) -> ApiResponse
        
        Gets the status of the processing of an asynchronous API call.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().get_inbound_operation_status("value")
        
        Args:
            operationId: object | required Identifier of an asynchronous operation.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), operationId), params=kwargs
        )

    @sp_endpoint(
        "/inbound/fba/2024-03-20/inboundPlans/{}/shipments/{}/deliveryWindowOptions",
        method="POST",
    )
    async def generate_delivery_window_options(
        self, inboundPlanId, shipmentId, **kwargs
    ) -> ApiResponse:
        """
        generate_delivery_window_options(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse
        
        Generates available delivery window options for a given shipment.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().generate_delivery_window_options("value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            shipmentId: object | required The shipment to generate delivery window options for.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId),
            params=kwargs,
        )

    @sp_endpoint(
        "/inbound/fba/2024-03-20/inboundPlans/{}/shipments/{}/deliveryWindowOptions",
        method="GET",
    )
    async def list_delivery_window_options(
        self, inboundPlanId, shipmentId, **kwargs
    ) -> ApiResponse:
        """
        list_delivery_window_options(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse
        
        Retrieves all delivery window options for a shipment. Delivery window options must first be generated by the `generateDeliveryWindowOptions` operation before becoming available.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().list_delivery_window_options("value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            shipmentId: object | required The shipment to get delivery window options for.
            key pageSize: object |  The number of delivery window options to return in the response matching the given query.
            key paginationToken: object |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId),
            params=kwargs,
        )

    @sp_endpoint(
        "/inbound/fba/2024-03-20/inboundPlans/{}/shipments/{}/deliveryWindowOptions/{}/confirmation",
        method="POST",
    )
    async def confirm_delivery_window_options(
        self, inboundPlanId, shipmentId, deliveryWindowOptionId, **kwargs
    ) -> ApiResponse:
        """
        confirm_delivery_window_options(self, inboundPlanId, shipmentId, deliveryWindowOptionId, **kwargs) -> ApiResponse
        
        Confirms the delivery window option for chosen shipment within an inbound plan. A placement option must be confirmed prior to use of this API. Once confirmed, new delivery window options cannot be generated, but the chosen delivery window option can be updated before shipment closure. The window is used to provide the expected time when a shipment will arrive at the warehouse. All transportation options which have the program `CONFIRMED_DELIVERY_WINDOW` require a delivery window to be confirmed prior to transportation option confirmation.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().confirm_delivery_window_options("value", "value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            shipmentId: object | required The shipment to confirm the delivery window option for.
            deliveryWindowOptionId: object | required The id of the delivery window option to be confirmed.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(
                kwargs.pop("path"), inboundPlanId, shipmentId, deliveryWindowOptionId
            ),
            params=kwargs,
        )

    @sp_endpoint(
        "/inbound/fba/2024-03-20/inboundPlans/{}/shipments/{}/items", method="GET"
    )
    async def list_shipment_items(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse:
        """
        list_shipment_items(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse
        
        Provides a paginated list of item packages in a shipment.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().list_shipment_items("value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            shipmentId: object | required Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            key pageSize: object |  The number of items to return in the response matching the given query.
            key paginationToken: object |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId),
            params=kwargs,
        )

    @sp_endpoint("/inbound/fba/2024-03-20/items/labels", method="POST")
    async def create_marketplace_item_labels(self, **kwargs) -> ApiResponse:
        """
        create_marketplace_item_labels(self, **kwargs) -> ApiResponse
        
        For a given marketplace - creates labels for a list of MSKUs.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().create_marketplace_item_labels()
        
        Args:
            body: CreateMarketplaceItemLabelsRequest | required The body of the request to `createMarketplaceItemLabels`.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/inbound/fba/2024-03-20/items/prepDetails", method="GET")
    async def list_prep_details(self, **kwargs) -> ApiResponse:
        """
        list_prep_details(self, **kwargs) -> ApiResponse
        
        Get preparation details for a list of MSKUs in a specified marketplace.\n\n**Note:** MSKUs that contain certain characters must be encoded. For more information, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).\n\nThe following characters must be double percent encoded:\n\n- `%`\n- `+`\n- `,`\n\n**Examples:** An MSKU value of `test%msku` is encoded as `test%2525msku`. An MSKU value of `test,msku` is encoded as `test%252Cmsku`.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().list_prep_details()
        
        Args:
            key marketplaceId: object | required The marketplace ID. For a list of possible values, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
            key mskus: object | required A list of merchant SKUs, a merchant-supplied identifier of a specific SKU.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/inbound/fba/2024-03-20/items/prepDetails", method="POST")
    async def set_prep_details(self, **kwargs) -> ApiResponse:
        """
        set_prep_details(self, **kwargs) -> ApiResponse
        
        Set the preparation details for a list of MSKUs in a specified marketplace.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().set_prep_details()
        
        Args:
            body: SetPrepDetailsRequest | required The body of the request to `setPrepDetails`.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint(
        "/inbound/fba/2024-03-20/inboundPlans/{}/shipments/{}/boxes", method="GET"
    )
    async def list_shipment_boxes(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse:
        """
        list_shipment_boxes(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse
        
        Provides a paginated list of box packages in a shipment.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().list_shipment_boxes("value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            shipmentId: object | required Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            key pageSize: object |  The number of boxes to return in the response matching the given query.
            key paginationToken: object |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId),
            params=kwargs,
        )

    @sp_endpoint(
        "/inbound/fba/2024-03-20/inboundPlans/{}/shipments/{}/trackingDetails",
        method="PUT",
    )
    async def update_shipment_tracking_details(
        self, inboundPlanId, shipmentId, **kwargs
    ) -> ApiResponse:
        """
        update_shipment_tracking_details(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse
        
        Updates a shipment's tracking details.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().update_shipment_tracking_details("value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            shipmentId: object | required Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            body: UpdateShipmentTrackingDetailsRequest | required The body of the request to `updateShipmentTrackingDetails`.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId),
            data=kwargs,
        )







    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}/name", method="PUT")
    async def update_inbound_plan_name(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        update_inbound_plan_name(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Updates the name of an existing inbound plan.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().update_inbound_plan_name("value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            body: UpdateInboundPlanNameRequest | required The body of the request to `updateInboundPlanName`.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), inboundPlanId), data=kwargs)

    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}/packingGroups/{}/boxes", method="GET")
    async def list_packing_group_boxes(self, inboundPlanId, packingGroupId, **kwargs) -> ApiResponse:
        """
        list_packing_group_boxes(self, inboundPlanId, packingGroupId, **kwargs) -> ApiResponse
        
        Retrieves a page of boxes from a given packing group. These boxes were previously provided through the `setPackingInformation` operation. This API is used for workflows where boxes are packed before Amazon determines shipment splits.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().list_packing_group_boxes("value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            packingGroupId: object | required Identifier of a packing group.
            key pageSize: object |  The number of packing group boxes to return in the response matching the given query.
            key paginationToken: object |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), inboundPlanId, packingGroupId), params=kwargs)












    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}/shipments/{}/contentUpdatePreviews", method="GET")
    async def list_shipment_content_update_previews(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse:
        """
        list_shipment_content_update_previews(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse
        
        Retrieve a paginated list of shipment content update previews for a given shipment. The shipment content update preview is a summary of the requested shipment content changes along with the transportation cost implications of the change that can only be confirmed prior to the expiry date specified.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().list_shipment_content_update_previews("value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            shipmentId: object | required Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            key pageSize: object |  The number of content update previews to return.
            key paginationToken: object |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId), params=kwargs)

    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}/shipments/{}/contentUpdatePreviews", method="POST")
    async def generate_shipment_content_update_previews(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse:
        """
        generate_shipment_content_update_previews(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse
        
        Generate a shipment content update preview given a set of intended boxes and/or items for a shipment with a confirmed carrier. The shipment content update preview will be viewable with the updated costs and contents prior to confirmation.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().generate_shipment_content_update_previews("value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            shipmentId: object | required Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            body: GenerateShipmentContentUpdatePreviewsRequest | required The body of the request to `generateShipmentContentUpdatePreviews`.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId), data=kwargs)

    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}/shipments/{}/contentUpdatePreviews/{}", method="GET")
    async def get_shipment_content_update_preview(self, inboundPlanId, shipmentId, contentUpdatePreviewId, **kwargs) -> ApiResponse:
        """
        get_shipment_content_update_preview(self, inboundPlanId, shipmentId, contentUpdatePreviewId, **kwargs) -> ApiResponse
        
        Retrieve a shipment content update preview which provides a summary of the requested shipment content changes along with the transportation cost implications of the change that can only be confirmed prior to the expiry date specified.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().get_shipment_content_update_preview("value", "value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            shipmentId: object | required Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            contentUpdatePreviewId: object | required Identifier of a content update preview.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId, contentUpdatePreviewId), params=kwargs)

    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}/shipments/{}/contentUpdatePreviews/{}/confirmation", method="POST")
    async def confirm_shipment_content_update_preview(self, inboundPlanId, shipmentId, contentUpdatePreviewId, **kwargs) -> ApiResponse:
        """
        confirm_shipment_content_update_preview(self, inboundPlanId, shipmentId, contentUpdatePreviewId, **kwargs) -> ApiResponse
        
        Confirm a shipment content update preview and accept the changes in transportation cost.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().confirm_shipment_content_update_preview("value", "value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            shipmentId: object | required Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            contentUpdatePreviewId: object | required Identifier of a content update preview.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId, contentUpdatePreviewId), data=kwargs)

    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}/shipments/{}/deliveryChallanDocument", method="GET")
    async def get_delivery_challan_document_get(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse:
        """
        get_delivery_challan_document_get(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse
        
        Provide delivery challan document for PCP transportation in IN marketplace.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().get_delivery_challan_document_get("value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            shipmentId: object | required Identifier of a shipment. A shipment contains the boxes and units being inbounded.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId), params=kwargs)






    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}/shipments/{}/pallets", method="GET")
    async def list_shipment_pallets(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse:
        """
        list_shipment_pallets(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse
        
        Provides a paginated list of pallet packages in a shipment. A palletized shipment will have pallets when the related details are provided after generating Less-Than-Truckload (LTL) carrier shipments.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().list_shipment_pallets("value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            shipmentId: object | required Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            key pageSize: object |  The number of pallets to return in the response matching the given query.
            key paginationToken: object |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId), params=kwargs)

    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}/shipments/{}/selfShipAppointmentCancellation", method="PUT")
    async def cancel_self_ship_appointment_put(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse:
        """
        cancel_self_ship_appointment_put(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse
        
        Cancels a self-ship appointment slot against a shipment. Only available in the following [marketplaces](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids): MX, BR, EG, SA, AE, IN.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().cancel_self_ship_appointment_put("value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            shipmentId: object | required Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            body: CancelSelfShipAppointmentRequest | required The body of the request to `cancelSelfShipAppointment`.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId), data=kwargs)

    async def cancel_self_ship_appointment(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse:
        """
        cancel_self_ship_appointment(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse

        Backward-compatible alias for `cancel_self_ship_appointment_put`.
        """
        return await self.cancel_self_ship_appointment_put(inboundPlanId, shipmentId, **kwargs)

    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}/shipments/{}/selfShipAppointmentSlots", method="GET")
    async def get_self_ship_appointment_slots_get(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse:
        """
        get_self_ship_appointment_slots_get(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse
        
        Retrieves a list of available self-ship appointment slots used to drop off a shipment at a warehouse. Only available in the following [marketplaces](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids): MX, BR, EG, SA, AE, IN.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().get_self_ship_appointment_slots_get("value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            shipmentId: object | required Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            key pageSize: object |  The number of self ship appointment slots to return in the response matching the given query.
            key paginationToken: object |  A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId), params=kwargs)

    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}/shipments/{}/selfShipAppointmentSlots", method="POST")
    async def generate_self_ship_appointment_slots_post(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse:
        """
        generate_self_ship_appointment_slots_post(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse
        
        Initiates the process of generating the appointment slots list. Only available in the following [marketplaces](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids): MX, BR, EG, SA, AE, IN.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().generate_self_ship_appointment_slots_post("value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            shipmentId: object | required Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            body: GenerateSelfShipAppointmentSlotsRequest | required The body of the request to `generateSelfShipAppointmentSlots`.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId), data=kwargs)

    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}/shipments/{}/selfShipAppointmentSlots/{}/schedule", method="POST")
    async def schedule_self_ship_appointment_post(self, inboundPlanId, shipmentId, slotId, **kwargs) -> ApiResponse:
        """
        schedule_self_ship_appointment_post(self, inboundPlanId, shipmentId, slotId, **kwargs) -> ApiResponse
        
        Confirms or reschedules a self-ship appointment slot against a shipment. Only available in the following [marketplaces](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids): MX, BR, EG, SA, AE, IN.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().schedule_self_ship_appointment_post("value", "value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            shipmentId: object | required Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            slotId: object | required An identifier to a self-ship appointment slot.
            body: ScheduleSelfShipAppointmentRequest | required The body of the request to `scheduleSelfShipAppointment`.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId, slotId), data=kwargs)

    @sp_endpoint("/inbound/fba/2024-03-20/inboundPlans/{}/shipments/{}/sourceAddress", method="PUT")
    async def update_shipment_source_address(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse:
        """
        update_shipment_source_address(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse
        
        Updates the source address of an existing shipment. The shipment source address can only be updated prior to the confirmation of the shipment carriers. As a result of the updated source address, existing transportation options will be invalidated and will need to be regenerated to capture the potential difference in transportation options and quotes due to the new source address.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV20240320().update_shipment_source_address("value", "value")
        
        Args:
            inboundPlanId: object | required Identifier of an inbound plan.
            shipmentId: object | required Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            body: UpdateShipmentSourceAddressRequest | required The body of the request to `updateShipmentSourceAddress`.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId), data=kwargs)
