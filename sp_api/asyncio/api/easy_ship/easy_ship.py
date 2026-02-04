import urllib.parse

from sp_api.base import ApiResponse, fill_query_params, sp_endpoint
from sp_api.asyncio.base import AsyncBaseClient


class EasyShip(AsyncBaseClient):
    """
    Easy_ SP-API Client
    :link: 

    Use the Selling Partner API for Easy Ship to build applications for sellers to manage and ship Amazon Easy Ship orders. With this API, you can get available time slots, schedule and reschedule Easy Ship orders, and print shipping labels, invoices, and warranties. To review the differences in Easy Ship operations by marketplace, refer to [Marketplace support](https://developer-docs.amazon.com/sp-api/docs/easyship-api-v2022-03-23-use-case-guide#marketplace-support).
    """


    @sp_endpoint('/easyShip/2022-03-23/timeSlot', method='POST')
    async def list_handover_slots(self, **kwargs) -> ApiResponse:
        """
        list_handover_slots(self, **kwargs) -> ApiResponse
        
        Returns time slots available for Easy Ship orders to be scheduled based on the package weight and dimensions that the seller specifies.
        
        This operation is available for scheduled and unscheduled orders based on marketplace support. See **Get Time Slots** in the [Marketplace Support Table](doc:easyship-api-v2022-03-23-use-case-guide#marketplace-support-table).
        
        This operation can return time slots that have either pickup or drop-off handover methods - see **Supported Handover Methods** in the [Marketplace Support Table](doc:easyship-api-v2022-03-23-use-case-guide#marketplace-support-table).
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await EasyShip().list_handover_slots()
        
        Args:
            ListHandoverSlotsRequest: ListHandoverSlotsRequest |  The request schema for the `listHandoverSlots` operation.
        
        Returns:
            ApiResponse
        """
    
        return await self._request(kwargs.pop('path'), data=kwargs)
    

    @sp_endpoint('/easyShip/2022-03-23/package', method='GET')
    async def get_scheduled_package(self, **kwargs) -> ApiResponse:
        """
        get_scheduled_package(self, **kwargs) -> ApiResponse
        
        Returns information about a package, including dimensions, weight, time slot information for handover, invoice and item information, and status.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await EasyShip().get_scheduled_package()
        
        Args:
            key amazonOrderId: object | required An Amazon-defined order identifier. Identifies the order that the seller wants to deliver using Amazon Easy Ship.
            key marketplaceId: object | required An identifier for the marketplace in which the seller is selling.
        
        Returns:
            ApiResponse
        """
    
        return await self._request(kwargs.pop('path'), params=kwargs)
    

    @sp_endpoint('/easyShip/2022-03-23/package', method='POST')
    async def create_scheduled_package(self, **kwargs) -> ApiResponse:
        """
        create_scheduled_package(self, **kwargs) -> ApiResponse
        
        Schedules an Easy Ship order and returns the scheduled package information.
        
        This operation does the following:
        
        *  Specifies the time slot and handover method for the order to be scheduled for delivery.
        
        * Updates the Easy Ship order status.
        
        * Generates a shipping label and an invoice. Calling `createScheduledPackage` also generates a warranty document if you specify a `SerialNumber` value. To get these documents, see [How to get invoice, shipping label, and warranty documents](doc:easyship-api-v2022-03-23-use-case-guide).
        
        * Shows the status of Easy Ship orders when you call the `getOrders` operation of the Selling Partner API for Orders and examine the `EasyShipShipmentStatus` property in the response body.
        
        See the **Shipping Label**, **Invoice**, and **Warranty** columns in the [Marketplace Support Table](doc:easyship-api-v2022-03-23-use-case-guide#marketplace-support-table) to see which documents are supported in each marketplace.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await EasyShip().create_scheduled_package()
        
        Args:
            CreateScheduledPackageRequest: CreateScheduledPackageRequest | required The request schema for the `createScheduledPackage` operation.
        
        Returns:
            ApiResponse
        """
    
        return await self._request(kwargs.pop('path'), data=kwargs)
    

    @sp_endpoint('/easyShip/2022-03-23/package', method='PATCH')
    async def update_scheduled_packages(self, **kwargs) -> ApiResponse:
        """
        update_scheduled_packages(self, **kwargs) -> ApiResponse
        
        Updates the time slot for handing over the package indicated by the specified `scheduledPackageId`. You can get the new `slotId` value for the time slot by calling the `listHandoverSlots` operation before making another `patch` call.
        
        See the **Update Package** column in the [Marketplace Support Table](doc:easyship-api-v2022-03-23-use-case-guide#marketplace-support-table) to see which marketplaces this operation is supported in.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await EasyShip().update_scheduled_packages()
        
        Args:
            UpdateScheduledPackagesRequest: UpdateScheduledPackagesRequest |  The request schema for the `updateScheduledPackages` operation.
        
        Returns:
            ApiResponse
        """
    
        return await self._request(kwargs.pop('path'), data=kwargs)
    

    @sp_endpoint('/easyShip/2022-03-23/packages/bulk', method='POST')
    async def create_scheduled_package_bulk(self, **kwargs) -> ApiResponse:
        """
        create_scheduled_package_bulk(self, **kwargs) -> ApiResponse
        
        This operation automatically schedules a time slot for all the `amazonOrderId`s given as input, generating the associated shipping labels, along with other compliance documents according to the marketplace (refer to the [marketplace document support table](doc:easyship-api-v2022-03-23-use-case-guide#marketplace-support-table)).
        
        Developers calling this operation may optionally assign a `packageDetails` object, allowing them to input a preferred time slot for each order in ther request. In this case, Amazon will try to schedule the respective packages using their optional settings. On the other hand, *i.e.*, if the time slot is not provided, Amazon will then pick the earliest time slot possible. 
        
        Regarding the shipping label's file format, external developers are able to choose between PDF or ZPL, and Amazon will create the label accordingly.
        
        This operation returns an array composed of the scheduled packages, and a short-lived URL pointing to a zip file containing the generated shipping labels and the other documents enabled for your marketplace. If at least an order couldn't be scheduled, then Amazon adds the `rejectedOrders` list into the response, which contains an entry for each order we couldn't process. Each entry is composed of an error message describing the reason of the failure, so that sellers can take action.
        
        The table below displays the supported request and burst maximum rates:
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await EasyShip().create_scheduled_package_bulk()
        
        Args:
            CreateScheduledPackagesRequest: CreateScheduledPackagesRequest | required The request schema for the `createScheduledPackageBulk` operation.
        
        Returns:
            ApiResponse
        """
    
        return await self._request(kwargs.pop('path'), data=kwargs)
    