import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class EasyShip(Client):
    """
    Easy_ SP-API Client
    :link: 

    Use the Selling Partner API for Easy Ship to build applications for sellers to manage and ship Amazon Easy Ship orders. With this API, you can get available time slots, schedule and reschedule Easy Ship orders, and print shipping labels, invoices, and warranties. To review the differences in Easy Ship operations by marketplace, refer to [Marketplace support](https://developer-docs.amazon.com/sp-api/docs/easyship-api-v2022-03-23-use-case-guide#marketplace-support).
    """


    @sp_endpoint('/easyShip/2022-03-23/timeSlot', method='POST')
    def list_handover_slots(self, **kwargs) -> ApiResponse:
        """
        list_handover_slots(self, **kwargs) -> ApiResponse

        Returns time slots available for Easy Ship orders to be scheduled based on the package weight and dimensions that the seller specifies.

This operation is available for scheduled and unscheduled orders based on marketplace support. See **Get Time Slots** in the [Marketplace Support Table](doc:easyship-api-v2022-03-23-use-case-guide#marketplace-support-table).

This operation can return time slots that have either pickup or drop-off handover methods - see **Supported Handover Methods** in the [Marketplace Support Table](doc:easyship-api-v2022-03-23-use-case-guide#marketplace-support-table).

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 5 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        
            ListHandoverSlotsRequest: |  {'description': 'The request schema for the `listHandoverSlots` operation.',
 'properties': {'amazonOrderId': {'$ref': '#/definitions/AmazonOrderId'}, 'marketplaceId': {'$ref': '#/definitions/String'}, 'packageDimensions': {'$ref': '#/definitions/Dimensions'}, 'packageWeight': {'$ref': '#/definitions/Weight'}},
 'required': ['marketplaceId', 'amazonOrderId', 'packageDimensions', 'packageWeight'],
 'type': 'object'}
        

        Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  data=kwargs)
    

    @sp_endpoint('/easyShip/2022-03-23/package', method='GET')
    def get_scheduled_package(self, **kwargs) -> ApiResponse:
        """
        get_scheduled_package(self, **kwargs) -> ApiResponse

        Returns information about a package, including dimensions, weight, time slot information for handover, invoice and item information, and status.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 5 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        
            key amazonOrderId:string | * REQUIRED An Amazon-defined order identifier. Identifies the order that the seller wants to deliver using Amazon Easy Ship.
        
            key marketplaceId:string | * REQUIRED An identifier for the marketplace in which the seller is selling.
        

        Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  params=kwargs)
    

    @sp_endpoint('/easyShip/2022-03-23/package', method='POST')
    def create_scheduled_package(self, **kwargs) -> ApiResponse:
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

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 5 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        
            CreateScheduledPackageRequest: | * REQUIRED {'description': 'The request schema for the `createScheduledPackage` operation.',
 'properties': {'amazonOrderId': {'$ref': '#/definitions/AmazonOrderId'}, 'marketplaceId': {'$ref': '#/definitions/String'}, 'packageDetails': {'$ref': '#/definitions/PackageDetails'}},
 'required': ['amazonOrderId', 'marketplaceId', 'packageDetails'],
 'type': 'object'}
        

        Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  data=kwargs)
    

    @sp_endpoint('/easyShip/2022-03-23/package', method='PATCH')
    def update_scheduled_packages(self, **kwargs) -> ApiResponse:
        """
        update_scheduled_packages(self, **kwargs) -> ApiResponse

        Updates the time slot for handing over the package indicated by the specified `scheduledPackageId`. You can get the new `slotId` value for the time slot by calling the `listHandoverSlots` operation before making another `patch` call.

See the **Update Package** column in the [Marketplace Support Table](doc:easyship-api-v2022-03-23-use-case-guide#marketplace-support-table) to see which marketplaces this operation is supported in.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 5 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        
            UpdateScheduledPackagesRequest: |  {'description': 'The request schema for the `updateScheduledPackages` operation.',
 'properties': {'marketplaceId': {'$ref': '#/definitions/String'}, 'updatePackageDetailsList': {'$ref': '#/definitions/UpdatePackageDetailsList'}},
 'required': ['marketplaceId', 'updatePackageDetailsList'],
 'type': 'object'}
        

        Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  data=kwargs)
    

    @sp_endpoint('/easyShip/2022-03-23/packages/bulk', method='POST')
    def create_scheduled_package_bulk(self, **kwargs) -> ApiResponse:
        """
        create_scheduled_package_bulk(self, **kwargs) -> ApiResponse

        This operation automatically schedules a time slot for all the `amazonOrderId`s given as input, generating the associated shipping labels, along with other compliance documents according to the marketplace (refer to the [marketplace document support table](doc:easyship-api-v2022-03-23-use-case-guide#marketplace-support-table)).

Developers calling this operation may optionally assign a `packageDetails` object, allowing them to input a preferred time slot for each order in their request. In this case, Amazon will try to schedule the respective packages using their optional settings. On the other hand, *i.e.*, if the time slot is not provided, Amazon will then pick the earliest time slot possible. 

Regarding the shipping label's file format, external developers are able to choose between PDF or ZPL, and Amazon will create the label accordingly.

This operation returns an array composed of the scheduled packages, and a short-lived URL pointing to a zip file containing the generated shipping labels and the other documents enabled for your marketplace. If at least an order couldn't be scheduled, then Amazon adds the `rejectedOrders` list into the response, which contains an entry for each order we couldn't process. Each entry is composed of an error message describing the reason of the failure, so that sellers can take action.

The table below displays the supported request and burst maximum rates:

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 5 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        
            CreateScheduledPackagesRequest: | * REQUIRED {'description': 'The request body for the POST /easyShip/2022-03-23/packages/bulk API.',
 'properties': {'labelFormat': {'$ref': '#/definitions/LabelFormat'},
                'marketplaceId': {'$ref': '#/definitions/String'},
                'orderScheduleDetailsList': {'description': 'An array allowing users to specify orders to be scheduled.', 'items': {'$ref': '#/definitions/OrderScheduleDetails'}, 'minItems': 1, 'type': 'array'}},
 'required': ['marketplaceId', 'orderScheduleDetailsList', 'labelFormat'],
 'type': 'object'}
        

        Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  data=kwargs)
    
