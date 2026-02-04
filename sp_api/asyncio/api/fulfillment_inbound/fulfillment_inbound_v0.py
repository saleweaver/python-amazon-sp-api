from sp_api.base import ApiResponse
from sp_api.asyncio.base import AsyncBaseClient
from sp_api.base import sp_endpoint, fill_query_params

import urllib.parse
from sp_api.util import ensure_csv


class FulfillmentInboundV0(AsyncBaseClient):
    """
    FulfillmentInbound SP-API Client
    :link:

    The Selling Partner API for Fulfillment By Amazon (FBA) Inbound. The FBA Inbound API enables building inbound workflows to create, manage, and send shipments into Amazon's fulfillment network. The API has interoperability with the Send-to-Amazon user interface.
    """

    @sp_endpoint("/fba/inbound/v0/itemsGuidance")
    async def item_guidance(self, **kwargs):
        """
        item_guidance(self, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().item_guidance()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/fba/inbound/v0/plans", method="POST")
    async def plans(self, data, **kwargs):
        """
        plans(self, data, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().plans("value")
        
        Args:
            data:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), data={**data, **kwargs})

    @sp_endpoint("/fba/inbound/v0/shipments/{}", method="POST")
    async def create_shipment(self, shipment_id, data, **kwargs):
        """
        create_shipment(self, shipment_id, data, **kwargs) -> ApiResponse
        
        create_shipment(self, shipment_id, data, **kwargs)
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().create_shipment("value", "value")
        
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

    @sp_endpoint("/fba/inbound/v0/shipments/{}", method="PUT")
    async def update_shipment(self, shipment_id, data, **kwargs):
        """
        update_shipment(self, shipment_id, data, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().update_shipment("value", "value")
        
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
        "/inbound/fba/v0/inboundPlans/{}/shipments/{}/name", method="PUT"
    )
    async def update_shipment_name(self, inboundPlanId, shipmentId, **kwargs):
        """
        update_shipment_name(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse
        
        Updates the name of an existing shipment.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().update_shipment_name("value", "value")
        
        Args:
            inboundPlanId:  | required
            shipmentId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId),
            data=kwargs,
        )

    @sp_endpoint("/fba/inbound/v0/shipments/{}/preorder")
    async def preorder(self, shipment_id, **kwargs):
        """
        preorder(self, shipment_id, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().preorder("value")
        
        Args:
            shipment_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), shipment_id), params=kwargs
        )

    @sp_endpoint("/fba/inbound/v0/shipments/{}/preorder/confirm", method="PUT")
    async def confirm_preorder(self, shipment_id, **kwargs):
        """
        confirm_preorder(self, shipment_id, **kwargs) -> ApiResponse
        
        confirm_preorder(self, shipment_id, **kwargs)
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().confirm_preorder("value")
        
        Args:
            shipment_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), shipment_id), params=kwargs
        )

    @sp_endpoint("/fba/inbound/v0/prepInstructions")
    async def prep_instruction(self, data, **kwargs):
        """
        prep_instruction(self, data, **kwargs) -> ApiResponse
        
        Returns labeling requirements and item preparation instructions to help prepare items for shipment to Amazon's fulfillment network.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().prep_instruction("value")
        
        Args:
            data:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), params={**data, **kwargs})

    @sp_endpoint("/fba/inbound/v0/shipments/{}/transport")
    async def get_transport_information(self, shipment_id, **kwargs):
        """
        get_transport_information(self, shipment_id, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().get_transport_information("value")
        
        Args:
            shipment_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), shipment_id), params=kwargs
        )

    @sp_endpoint("/fba/inbound/v0/shipments/{}/transport", method="PUT")
    async def update_transport_information(self, shipment_id, **kwargs):
        """
        update_transport_information(self, shipment_id, **kwargs) -> ApiResponse
        
        putTransportDetails
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().update_transport_information("value")
        
        Args:
            shipment_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), shipment_id), data=kwargs
        )

    @sp_endpoint("/fba/inbound/v0/shipments/{}/transport/void", method="POST")
    async def void_transport(self, shipment_id, **kwargs):
        """
        void_transport(self, shipment_id, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().void_transport("value")
        
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
        "/fba/inbound/v0/shipments/{}/transport/estimate", method="POST"
    )
    async def estimate_transport(self, shipment_id, **kwargs):
        """
        estimate_transport(self, shipment_id, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().estimate_transport("value")
        
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

    @sp_endpoint("/fba/inbound/v0/shipments/{}/transport/confirm", method="POST")
    async def confirm_transport(self, shipment_id, **kwargs):
        return await self._request(
            fill_query_params(kwargs.pop("path"), shipment_id),
            data=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/fba/inbound/v0/shipments/{}/labels")
    async def get_labels(self, shipment_id, **kwargs):
        """
        get_labels(self, shipment_id, **kwargs) -> ApiResponse
        
        Returns package/pallet labels for faster and more accurate shipment processing at the Amazon fulfillment center.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().get_labels("value")
        
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

    @sp_endpoint("/fba/inbound/v0/shipments/{}/billOfLading")
    async def bill_of_lading(self, shipment_id, **kwargs):
        """
        bill_of_lading(self, shipment_id, **kwargs) -> ApiResponse
        
        Returns a bill of lading for a Less Than Truckload/Full Truckload (LTL/FTL) shipment. The getBillOfLading operation returns PDF document data for printing a bill of lading for an Amazon-partnered Less Than Truckload/Full Truckload (LTL/FTL) inbound shipment.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().bill_of_lading("value")
        
        Args:
            shipment_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), shipment_id), params=kwargs
        )

    @sp_endpoint("/fba/inbound/v0/shipments")
    async def get_shipments(self, **kwargs):
        """
        get_shipments(self, **kwargs) -> ApiResponse
        
        Returns a list of inbound shipments based on criteria that you specify.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().get_shipments()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/fba/inbound/v0/shipments/{}/items")
    async def shipment_items_by_shipment(self, shipment_id, **kwargs):
        """
        shipment_items_by_shipment(self, shipment_id, **kwargs) -> ApiResponse
        
        Returns a list of items in a specified inbound shipment.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().shipment_items_by_shipment("value")
        
        Args:
            shipment_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), shipment_id), params=kwargs
        )

    @sp_endpoint("/fba/inbound/v0/shipmentItems")
    async def shipment_items(self, **kwargs):
        """
        shipment_items(self, **kwargs) -> ApiResponse
        
        Returns a list of items in a specified inbound shipment, or a list of items that were updated within a specified time frame.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().shipment_items()
        
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
            
                await FulfillmentInboundV0().get_shipments_by_id("value")
        
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
    @sp_endpoint("/inbound/fba/v0/inboundPlans", method="GET")
    async def list_inbound_plans(self, **kwargs) -> ApiResponse:
        """
        list_inbound_plans(self, **kwargs) -> ApiResponse
        
        Provides a list of inbound plans with minimal information.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().list_inbound_plans()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/inbound/fba/v0/inboundPlans", method="POST")
    async def create_inbound_plan(self, **kwargs) -> ApiResponse:
        """
        create_inbound_plan(self, **kwargs) -> ApiResponse
        
        Creates an inbound plan. An inbound plan contains all the necessary information to send shipments into Amazon's fufillment network.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().create_inbound_plan()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/inbound/fba/v0/inboundPlans/{}", method="GET")
    async def get_inbound_plan(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        get_inbound_plan(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Fetches the top level information about an inbound plan.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().get_inbound_plan("value")
        
        Args:
            inboundPlanId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), params=kwargs
        )

    @sp_endpoint("/inbound/fba/v0/inboundPlans/{}/boxes", method="GET")
    async def list_inbound_plan_boxes(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        list_inbound_plan_boxes(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Provides a paginated list of box packages in an inbound plan.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().list_inbound_plan_boxes("value")
        
        Args:
            inboundPlanId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), params=kwargs
        )

    @sp_endpoint("/inbound/fba/v0/inboundPlans/{}/cancellation", method="PUT")
    async def cancel_inbound_plan(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        cancel_inbound_plan(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Cancels an Inbound Plan. Charges may apply if the cancellation is performed outside of a void window. The window
                                    for Amazon Partnered Carriers is 24 hours for Small Parcel Delivery (SPD) and one hour for Less-Than-Truckload (LTL) carrier shipments.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().cancel_inbound_plan("value")
        
        Args:
            inboundPlanId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), data=kwargs
        )

    @sp_endpoint("/inbound/fba/v0/inboundPlans/{}/items", method="GET")
    async def list_inbound_plan_items(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        list_inbound_plan_items(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Provides a paginated list of item packages in an inbound plan.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().list_inbound_plan_items("value")
        
        Args:
            inboundPlanId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), params=kwargs
        )

    @sp_endpoint(
        "/inbound/fba/v0/inboundPlans/{}/packingInformation", method="POST"
    )
    async def set_packing_information(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        set_packing_information(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Sets packing information for an inbound plan. This should be called after an inbound plan is created to populate
                                    the box level information required for planning and transportation estimates.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().set_packing_information("value")
        
        Args:
            inboundPlanId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), data=kwargs
        )

    @sp_endpoint("/inbound/fba/v0/inboundPlans/{}/packingOptions", method="GET")
    async def list_packing_options(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        list_packing_options(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Retrieves a list of all packing options for an inbound plan. Packing options must first be generated by the corresponding endpoint before becoming available.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().list_packing_options("value")
        
        Args:
            inboundPlanId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), params=kwargs
        )

    @sp_endpoint("/inbound/fba/v0/inboundPlans/{}/packingOptions", method="POST")
    async def generate_packing_options(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        generate_packing_options(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Generates available packing options for the inbound plan.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().generate_packing_options("value")
        
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
        "/inbound/fba/v0/inboundPlans/{}/packingOptions/{}/confirmation",
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
            
                await FulfillmentInboundV0().confirm_packing_option("value", "value")
        
        Args:
            inboundPlanId:  | required
            packingOptionId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId, packingOptionId),
            data=kwargs,
        )

    @sp_endpoint("/inbound/fba/v0/inboundPlans/{}/packingGroups/{}/items", method="GET")
    async def list_packing_group_items(self, inboundPlanId, packingGroupId, **kwargs) -> ApiResponse:
        """
        list_packing_group_items(self, inboundPlanId, packingGroupId, **kwargs) -> ApiResponse
        
        Retrieves a list of all items in a packing options's packing group. Packing options must first be generated by the corresponding endpoint before packing group items can be listed.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().list_packing_group_items("value", "value")
        
        Args:
            inboundPlanId:  | required
            packingGroupId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId, packingGroupId), params=kwargs
        )

    @sp_endpoint("/inbound/fba/v0/inboundPlans/{}/pallets", method="GET")
    async def list_inbound_plan_pallets(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        list_inbound_plan_pallets(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Provides a paginated list of pallet packages in an inbound plan. An inbound plan will have pallets when the related details are provided after generating Less-Than-Truckload (LTL) carrier shipments.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().list_inbound_plan_pallets("value")
        
        Args:
            inboundPlanId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), params=kwargs
        )

    @sp_endpoint(
        "/inbound/fba/v0/inboundPlans/{}/placementOptions", method="GET"
    )
    async def list_placement_options(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        list_placement_options(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Provides a list of all placement options for an inbound plan. Placement options must first be generated by the corresponding endpoint before becoming available.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().list_placement_options("value")
        
        Args:
            inboundPlanId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), params=kwargs
        )

    @sp_endpoint(
        "/inbound/fba/v0/inboundPlans/{}/placementOptions", method="POST"
    )
    async def generate_placement_options(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        generate_placement_options(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Generates placement options for the inbound plan.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().generate_placement_options("value")
        
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
        "/inbound/fba/v0/inboundPlans/{}/placementOptions/{}/confirmation",
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
            
                await FulfillmentInboundV0().confirm_placement_option("value", "value")
        
        Args:
            inboundPlanId:  | required
            placementOptionId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId, placementOptionId),
            data=kwargs,
        )

    @sp_endpoint("/inbound/fba/v0/inboundPlans/{}/shipments/{}", method="GET")
    async def get_shipment(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse:
        """
        get_shipment(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse
        
        Provides the full details for a specific shipment within an inbound plan. The `transportationOptionId` inside `acceptedTransportationSelection` can be used to retrieve the transportation details for the shipment.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().get_shipment("value", "value")
        
        Args:
            inboundPlanId:  | required
            shipmentId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId),
            params=kwargs,
        )

    @sp_endpoint(
        "/inbound/fba/v0/inboundPlans/{}/deliveryChallanDocument", method="GET"
    )
    async def get_delivery_challan_document(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        get_delivery_challan_document(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Provide delivery challan document for PCP transportation in IN marketplace.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().get_delivery_challan_document("value")
        
        Args:
            inboundPlanId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), params=kwargs
        )

    @sp_endpoint("/inbound/fba/v0/inboundPlans/{}/deliveryWindow", method="POST")
    async def update_shipment_delivery_window(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        update_shipment_delivery_window(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Update the time window that a shipment will be delivered to the warehouse. The window is used to provide the expected time that a non-Amazon partnered carrier will arrive at the warehouse.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().update_shipment_delivery_window("value")
        
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
        "/inbound/fba/v0/inboundPlans/{}/selfShipAppointmentSlots", method="GET"
    )
    async def get_self_ship_appointment_slots(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        get_self_ship_appointment_slots(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Retrieves a list of available self-ship appointment slots used to drop off a shipment at a warehouse.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().get_self_ship_appointment_slots("value")
        
        Args:
            inboundPlanId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), params=kwargs
        )

    @sp_endpoint(
        "/inbound/fba/v0/inboundPlans/{}/selfShipAppointmentSlots", method="POST"
    )
    async def generate_self_ship_appointment_slots(
        self, inboundPlanId, **kwargs
    ) -> ApiResponse:
        """
        generate_self_ship_appointment_slots(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Initiates the process of generating the appointment slots list.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().generate_self_ship_appointment_slots("value")
        
        Args:
            inboundPlanId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), data=kwargs
        )


    @sp_endpoint("/inbound/fba/v0/inboundPlans/{}/schedule", method="POST")
    async def schedule_self_ship_appointment(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        schedule_self_ship_appointment(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Confirms or reschedules a self-ship appointment slot against a shipment.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().schedule_self_ship_appointment("value")
        
        Args:
            inboundPlanId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), data=kwargs
        )

    @sp_endpoint("/inbound/fba/v0/inboundPlans/{}/trackingDetails", method="PUT")
    async def update_shipment_tracking_details(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        update_shipment_tracking_details(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Updates a shipment's tracking details.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().update_shipment_tracking_details("value")
        
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
        "/inbound/fba/v0/inboundPlans/{}/transportationOptions", method="GET"
    )
    async def list_transportation_options(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        list_transportation_options(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Retrieves all transportation options for a shipment. Transportation options must first be generated by the corresponding endpoint before becoming available.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().list_transportation_options("value")
        
        Args:
            inboundPlanId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), params=kwargs
        )

    @sp_endpoint(
        "/inbound/fba/v0/inboundPlans/{}/transportationOptions", method="POST"
    )
    async def generate_transportation_options(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        generate_transportation_options(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Generates available transportation options for a given placement option.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().generate_transportation_options("value")
        
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
        "/inbound/fba/v0/inboundPlans/{}/transportationOptions/confirmation",
        method="POST",
    )
    async def confirm_transportation_options(self, inboundPlanId, **kwargs) -> ApiResponse:
        """
        confirm_transportation_options(self, inboundPlanId, **kwargs) -> ApiResponse
        
        Confirms all the transportation options for an inbound plan. A placement option must be confirmed prior to use of this API. Once confirmed, new transportation options can not be generated or confirmed for the Inbound Plan.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().confirm_transportation_options("value")
        
        Args:
            inboundPlanId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId), data=kwargs
        )

    @sp_endpoint("/inbound/fba/v0/items/compliance", method="GET")
    async def list_item_compliance_details(self, **kwargs) -> ApiResponse:
        """
        list_item_compliance_details(self, **kwargs) -> ApiResponse
        
        List the inbound compliance details for MSKUs in a given marketplace.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().list_item_compliance_details()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/inbound/fba/v0/items/compliance", method="PUT")
    async def update_item_compliance_details(self, **kwargs) -> ApiResponse:
        """
        update_item_compliance_details(self, **kwargs) -> ApiResponse
        
        Update compliance details for list of MSKUs. The details provided here are only used for the IN marketplace compliance validation.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().update_item_compliance_details()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/inbound/fba/v0/operations/{}", method="GET")
    async def get_inbound_operation_status(self, operationId, **kwargs) -> ApiResponse:
        """
        get_inbound_operation_status(self, operationId, **kwargs) -> ApiResponse
        
        Gets the status of the processing of an asynchronous API call.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().get_inbound_operation_status("value")
        
        Args:
            operationId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), operationId), params=kwargs
        )

    @sp_endpoint(
        "/inbound/fba/v0/inboundPlans/{}/shipments/{}/deliveryWindowOptions",
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
            
                await FulfillmentInboundV0().generate_delivery_window_options("value", "value")
        
        Args:
            inboundPlanId:  | required
            shipmentId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId),
            params=kwargs,
        )

    @sp_endpoint(
        "/inbound/fba/v0/inboundPlans/{}/shipments/{}/deliveryWindowOptions",
        method="GET",
    )
    async def list_delivery_window_options(
        self, inboundPlanId, shipmentId, **kwargs
    ) -> ApiResponse:
        """
        list_delivery_window_options(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse
        
        Retrieves all delivery window options for a shipment. Delivery window options must first be generated by the generateDeliveryWindowOptions operation before becoming available.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().list_delivery_window_options("value", "value")
        
        Args:
            inboundPlanId:  | required
            shipmentId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId),
            params=kwargs,
        )

    @sp_endpoint(
        "/inbound/fba/v0/inboundPlans/{}/shipments/{}/deliveryWindowOptions/{}/confirmation",
        method="POST",
    )
    async def confirm_delivery_window_options(
        self, inboundPlanId, shipmentId, deliveryWindowOptionId, **kwargs
    ) -> ApiResponse:
        """
        confirm_delivery_window_options(self, inboundPlanId, shipmentId, deliveryWindowOptionId, **kwargs) -> ApiResponse
        
        Confirms the delivery window option for chosen shipment within an inbound plan. A placement option must be confirmed prior to use of this API. Once confirmed, new delivery window options cannot be generated, but the chosen delivery window option can be updated before shipment closure. The window is used to provide the expected time when a shipment will arrive at the warehouse. All transportation options which have the program CONFIRMED_DELIVERY_WINDOW require a delivery window to be confirmed prior to transportation option confirmation.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().confirm_delivery_window_options("value", "value", "value")
        
        Args:
            inboundPlanId:  | required
            shipmentId:  | required
            deliveryWindowOptionId:  | required
            **kwargs:
        
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
        "/inbound/fba/v0/inboundPlans/{}/shipments/{}/items", method="GET"
    )
    async def list_shipment_items(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse:
        """
        list_shipment_items(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse
        
        Provides a paginated list of item packages in a shipment.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().list_shipment_items("value", "value")
        
        Args:
            inboundPlanId:  | required
            shipmentId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId),
            params=kwargs,
        )

    @sp_endpoint("/inbound/fba/v0/items/labels", method="POST")
    async def create_marketplace_item_labels(self, **kwargs) -> ApiResponse:
        """
        create_marketplace_item_labels(self, **kwargs) -> ApiResponse
        
        For a given marketplace - creates labels for a list of MSKUs.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().create_marketplace_item_labels()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/inbound/fba/v0/items/prepDetails", method="GET")
    async def list_prep_details(self, **kwargs) -> ApiResponse:
        """
        list_prep_details(self, **kwargs) -> ApiResponse
        
        Get preparation details for a list of MSKUs in a specified marketplace.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().list_prep_details()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/inbound/fba/v0/items/prepDetails", method="POST")
    async def set_prep_details(self, **kwargs) -> ApiResponse:
        """
        set_prep_details(self, **kwargs) -> ApiResponse
        
        Set the preparation details for a list of MSKUs in a specified marketplace.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().set_prep_details()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint(
        "/inbound/fba/v0/inboundPlans/{}/shipments/{}/boxes", method="GET"
    )
    async def list_shipment_boxes(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse:
        """
        list_shipment_boxes(self, inboundPlanId, shipmentId, **kwargs) -> ApiResponse
        
        Provides a paginated list of box packages in a shipment.
        
        Examples:
            literal blocks::
            
                await FulfillmentInboundV0().list_shipment_boxes("value", "value")
        
        Args:
            inboundPlanId:  | required
            shipmentId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId),
            params=kwargs,
        )

    @sp_endpoint(
        "/inbound/fba/v0/inboundPlans/{}/shipments/{}/trackingDetails",
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
            
                await FulfillmentInboundV0().update_shipment_tracking_details("value", "value")
        
        Args:
            inboundPlanId:  | required
            shipmentId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), inboundPlanId, shipmentId),
            data=kwargs,
        )
