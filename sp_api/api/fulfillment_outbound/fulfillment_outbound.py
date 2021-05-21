import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class FulfillmentOutbound(Client):
    """
    FulfillmentOutbound SP-API Client
    :link: 

    The Selling Partner API for Fulfillment Outbound lets you create applications that help a seller fulfill Multi-Channel Fulfillment orders using their inventory in Amazon's fulfillment network. You can get information on both potential and existing fulfillment orders.
    """


    @sp_endpoint('/fba/outbound/2020-07-01/fulfillmentOrders/preview', method='POST')
    def get_fulfillment_preview(self, **kwargs) -> ApiResponse:
        """
        get_fulfillment_preview(self, **kwargs) -> ApiResponse

        Returns a list of fulfillment order previews based on shipping criteria that you specify.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 2 | 30 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            body: | * REQUIRED {'description': 'The request body schema for the getFulfillmentPreview operation.',
 'properties': {'address': {'$ref': '#/definitions/Address', 'description': 'The destination address for the fulfillment order preview.'},
                'featureConstraints': {'description': 'A list of features and their fulfillment policies to apply to the order.', 'items': {'$ref': '#/definitions/FeatureSettings'}, 'type': 'array'},
                'includeCODFulfillmentPreview': {'description': 'Specifies whether to return fulfillment order previews that are for COD (Cash On Delivery).\n'
                                                                '\n'
                                                                'Possible values:\n'
                                                                '\n'
                                                                '* true - Returns all fulfillment order previews (both for COD and not for COD).\n'
                                                                '* false - Returns only fulfillment order previews that are not for COD.',
                                                 'type': 'boolean'},
                'includeDeliveryWindows': {'description': 'Specifies whether to return the ScheduledDeliveryInfo response object, which contains the available delivery windows for a Scheduled Delivery. The ScheduledDeliveryInfo response object can '
                                                          'only be returned for fulfillment order previews with ShippingSpeedCategories = ScheduledDelivery.',
                                           'type': 'boolean'},
                'items': {'$ref': '#/definitions/GetFulfillmentPreviewItemList', 'description': 'Identifying information and quantity information for the items in the fulfillment order preview.'},
                'marketplaceId': {'description': 'The marketplace the fulfillment order is placed against.', 'type': 'string'},
                'shippingSpeedCategories': {'$ref': '#/definitions/ShippingSpeedCategoryList',
                                            'description': 'A list of shipping methods used for creating fulfillment order previews.\n'
                                                           '\n'
                                                           'Possible values:\n'
                                                           '\n'
                                                           '* Standard - Standard shipping method.\n'
                                                           '* Expedited - Expedited shipping method.\n'
                                                           '* Priority - Priority shipping method.\n'
                                                           '* ScheduledDelivery - Scheduled Delivery shipping method.\n'
                                                           'Note: Shipping method service level agreements vary by marketplace. Sellers should see the Seller Central website in their marketplace for shipping method service level agreements and '
                                                           'fulfillment fees.'}},
 'required': ['address', 'items'],
 'type': 'object'}
        

         Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  data=kwargs)
    

    @sp_endpoint('/fba/outbound/2020-07-01/fulfillmentOrders', method='GET')
    def list_all_fulfillment_orders(self, **kwargs) -> ApiResponse:
        """
        list_all_fulfillment_orders(self, **kwargs) -> ApiResponse

        Returns a list of fulfillment orders fulfilled after (or at) a specified date-time, or indicated by the next token parameter.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 2 | 30 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            key queryStartDate:string |  A date used to select fulfillment orders that were last updated after (or at) a specified time. An update is defined as any change in fulfillment order status, including the creation of a new fulfillment order.
        
            key nextToken:string |  A string token returned in the response to your previous request.
        

         Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  params=kwargs)
    

    @sp_endpoint('/fba/outbound/2020-07-01/fulfillmentOrders', method='POST')
    def create_fulfillment_order(self, **kwargs) -> ApiResponse:
        """
        create_fulfillment_order(self, **kwargs) -> ApiResponse

        Requests that Amazon ship items from the seller's inventory in Amazon's fulfillment network to a destination address.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 2 | 30 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            body: | * REQUIRED {'description': 'The request body schema for the createFulfillmentOrder operation.',
 'properties': {'codSettings': {'$ref': '#/definitions/CODSettings'},
                'deliveryWindow': {'$ref': '#/definitions/DeliveryWindow'},
                'destinationAddress': {'$ref': '#/definitions/Address', 'description': 'The destination address for the fulfillment order.'},
                'displayableOrderComment': {'description': 'Order-specific text that appears in recipient-facing materials such as the outbound shipment packing slip.', 'maxLength': 1000, 'type': 'string'},
                'displayableOrderDate': {'$ref': '#/definitions/Timestamp', 'description': 'The date and time of the fulfillment order. Displays as the order date in recipient-facing materials such as the outbound shipment packing slip.'},
                'displayableOrderId': {'description': 'A fulfillment order identifier that the seller creates. This value displays as the order identifier in recipient-facing materials such as the outbound shipment packing slip. The value of '
                                                      'DisplayableOrderId should match the order identifier that the seller provides to the recipient. The seller can use the SellerFulfillmentOrderId for this value or they can specify an alternate '
                                                      'value if they want the recipient to reference an alternate order identifier.\n'
                                                      '\n'
                                                      'The value must be an alpha-numeric or ISO 8859-1 compliant string from one to 40 characters in length. Cannot contain two spaces in a row. Leading and trailing white space is removed.',
                                       'maxLength': 40,
                                       'type': 'string'},
                'featureConstraints': {'description': 'A list of features and their fulfillment policies to apply to the order.', 'items': {'$ref': '#/definitions/FeatureSettings'}, 'type': 'array'},
                'fulfillmentAction': {'$ref': '#/definitions/FulfillmentAction'},
                'fulfillmentPolicy': {'$ref': '#/definitions/FulfillmentPolicy'},
                'items': {'$ref': '#/definitions/CreateFulfillmentOrderItemList', 'description': 'A list of items to include in the fulfillment order preview, including quantity.'},
                'marketplaceId': {'description': 'The marketplace the fulfillment order is placed against.', 'type': 'string'},
                'notificationEmails': {'$ref': '#/definitions/NotificationEmailList'},
                'sellerFulfillmentOrderId': {'description': 'A fulfillment order identifier that the seller creates to track their fulfillment order. The SellerFulfillmentOrderId must be unique for each fulfillment order that a seller creates. If '
                                                            "the seller's system already creates unique order identifiers, then these might be good values for them to use.",
                                             'maxLength': 40,
                                             'type': 'string'},
                'shipFromCountryCode': {'description': 'The two-character country code for the country from which the fulfillment order ships. Must be in ISO 3166-1 alpha-2 format.', 'type': 'string'},
                'shippingSpeedCategory': {'$ref': '#/definitions/ShippingSpeedCategory', 'description': 'The shipping method for the fulfillment order.'}},
 'required': ['destinationAddress', 'displayableOrderComment', 'displayableOrderDate', 'displayableOrderId', 'items', 'sellerFulfillmentOrderId', 'shippingSpeedCategory'],
 'type': 'object'}
        

         Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  data=kwargs)
    

    @sp_endpoint('/fba/outbound/2020-07-01/tracking', method='GET')
    def get_package_tracking_details(self, **kwargs) -> ApiResponse:
        """
        get_package_tracking_details(self, **kwargs) -> ApiResponse

        Returns delivery tracking information for a package in an outbound shipment for a Multi-Channel Fulfillment order.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 2 | 30 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            key packageNumber:integer | * REQUIRED The unencrypted package identifier returned by the getFulfillmentOrder operation.
        

         Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  params=kwargs)
    

    @sp_endpoint('/fba/outbound/2020-07-01/returnReasonCodes', method='GET')
    def list_return_reason_codes(self, **kwargs) -> ApiResponse:
        """
        list_return_reason_codes(self, **kwargs) -> ApiResponse

        Returns a list of return reason codes for a seller SKU in a given marketplace.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 2 | 30 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            key sellerSku:string | * REQUIRED The seller SKU for which return reason codes are required.
        
            key marketplaceId:string |  The marketplace for which the seller wants return reason codes.
        
            key sellerFulfillmentOrderId:string |  The identifier assigned to the item by the seller when the fulfillment order was created. The service uses this value to determine the marketplace for which the seller wants return reason codes.
        
            key language:string | * REQUIRED The language that the TranslatedDescription property of the ReasonCodeDetails response object should be translated into.
        

         Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  params=kwargs)
    

    @sp_endpoint('/fba/outbound/2020-07-01/fulfillmentOrders/{}/return', method='PUT')
    def create_fulfillment_return(self, sellerFulfillmentOrderId, **kwargs) -> ApiResponse:
        """
        create_fulfillment_return(self, sellerFulfillmentOrderId, **kwargs) -> ApiResponse

        Creates a fulfillment return. 

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 2 | 30 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            body: | * REQUIRED {'description': 'The createFulfillmentReturn operation creates a fulfillment return for items that were fulfilled using the createFulfillmentOrder operation. For calls to createFulfillmentReturn, you must include ReturnReasonCode values returned by '
                'a previous call to the listReturnReasonCodes operation.',
 'properties': {'items': {'$ref': '#/definitions/CreateReturnItemList'}},
 'required': ['items'],
 'type': 'object'}
        
            sellerFulfillmentOrderId:string | * REQUIRED An identifier assigned by the seller to the fulfillment order at the time it was created. The seller uses their own records to find the correct SellerFulfillmentOrderId value based on the buyer's request to return items.
        

         Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop('path'), sellerFulfillmentOrderId), data=kwargs)
    

    @sp_endpoint('/fba/outbound/2020-07-01/fulfillmentOrders/{}', method='GET')
    def get_fulfillment_order(self, sellerFulfillmentOrderId, **kwargs) -> ApiResponse:
        """
        get_fulfillment_order(self, sellerFulfillmentOrderId, **kwargs) -> ApiResponse

        Returns the fulfillment order indicated by the specified order identifier.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 2 | 30 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            sellerFulfillmentOrderId:string | * REQUIRED The identifier assigned to the item by the seller when the fulfillment order was created.
        

         Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop('path'), sellerFulfillmentOrderId), params=kwargs)
    

    @sp_endpoint('/fba/outbound/2020-07-01/fulfillmentOrders/{}', method='PUT')
    def update_fulfillment_order(self, sellerFulfillmentOrderId, **kwargs) -> ApiResponse:
        """
        update_fulfillment_order(self, sellerFulfillmentOrderId, **kwargs) -> ApiResponse

        Updates and/or requests shipment for a fulfillment order with an order hold on it.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 2 | 30 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            body: | * REQUIRED {'properties': {'destinationAddress': {'$ref': '#/definitions/Address', 'description': 'The destination address for the fulfillment order.'},
                'displayableOrderComment': {'description': 'Order-specific text that appears in recipient-facing materials such as the outbound shipment packing slip.', 'maxLength': 1000, 'type': 'string'},
                'displayableOrderDate': {'$ref': '#/definitions/Timestamp', 'description': 'The date and time of the fulfillment order. Displays as the order date in recipient-facing materials such as the outbound shipment packing slip.'},
                'displayableOrderId': {'description': 'A fulfillment order identifier that the seller creates. This value displays as the order identifier in recipient-facing materials such as the outbound shipment packing slip. The value of '
                                                      'DisplayableOrderId should match the order identifier that the seller provides to the recipient. The seller can use the SellerFulfillmentOrderId for this value or they can specify an alternate '
                                                      'value if they want the recipient to reference an alternate order identifier.',
                                       'maxLength': 40,
                                       'type': 'string'},
                'featureConstraints': {'description': 'A list of features and their fulfillment policies to apply to the order.', 'items': {'$ref': '#/definitions/FeatureSettings'}, 'type': 'array'},
                'fulfillmentAction': {'$ref': '#/definitions/FulfillmentAction'},
                'fulfillmentPolicy': {'$ref': '#/definitions/FulfillmentPolicy'},
                'items': {'$ref': '#/definitions/UpdateFulfillmentOrderItemList', 'description': 'A list of items to include in the fulfillment order preview, including quantity.'},
                'marketplaceId': {'description': 'The marketplace the fulfillment order is placed against.', 'type': 'string'},
                'notificationEmails': {'$ref': '#/definitions/NotificationEmailList'},
                'shipFromCountryCode': {'description': 'The two-character country code for the country from which the fulfillment order ships. Must be in ISO 3166-1 alpha-2 format.', 'type': 'string'},
                'shippingSpeedCategory': {'$ref': '#/definitions/ShippingSpeedCategory'}},
 'type': 'object'}
        
            sellerFulfillmentOrderId:string | * REQUIRED The identifier assigned to the item by the seller when the fulfillment order was created.
        

         Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop('path'), sellerFulfillmentOrderId), data=kwargs)
    

    @sp_endpoint('/fba/outbound/2020-07-01/fulfillmentOrders/{}/cancel', method='PUT')
    def cancel_fulfillment_order(self, sellerFulfillmentOrderId, **kwargs) -> ApiResponse:
        """
        cancel_fulfillment_order(self, sellerFulfillmentOrderId, **kwargs) -> ApiResponse

        Requests that Amazon stop attempting to fulfill the fulfillment order indicated by the specified order identifier.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 2 | 30 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            sellerFulfillmentOrderId:string | * REQUIRED The identifier assigned to the item by the seller when the fulfillment order was created.
        

         Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop('path'), sellerFulfillmentOrderId), data=kwargs)
    

    @sp_endpoint('/fba/outbound/2020-07-01/features', method='GET')
    def get_features(self, **kwargs) -> ApiResponse:
        """
        get_features(self, **kwargs) -> ApiResponse

        Returns a list of features available for Multi-Channel Fulfillment orders in the marketplace you specify, and whether the seller for which you made the call is enrolled for each feature.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 2 | 30 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            key marketplaceId:string | * REQUIRED The marketplace for which to return the list of features.
        

         Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  params=kwargs)
    

    @sp_endpoint('/fba/outbound/2020-07-01/features/inventory/{}', method='GET')
    def get_feature_inventory(self, featureName, **kwargs) -> ApiResponse:
        """
        get_feature_inventory(self, featureName, **kwargs) -> ApiResponse

        Returns a list of inventory items that are eligible for the fulfillment feature you specify.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 2 | 30 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            key marketplaceId:string | * REQUIRED The marketplace for which to return a list of the inventory that is eligible for the specified feature.
        
            featureName:string | * REQUIRED The name of the feature for which to return a list of eligible inventory.
        
            key nextToken:string |  A string token returned in the response to your previous request that is used to return the next response page. A value of null will return the first page.
        

         Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop('path'), featureName), params=kwargs)
    

    @sp_endpoint('/fba/outbound/2020-07-01/features/inventory/{}', method='GET')
    def get_feature_s_k_u(self, featureName, **kwargs) -> ApiResponse:
        """
        get_feature_s_k_u(self, featureName, **kwargs) -> ApiResponse

        Returns the number of items with the sellerSKU you specify that can have orders fulfilled using the specified feature. Note that if the sellerSKU isn't eligible, the response will contain an empty skuInfo object.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 2 | 30 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            key marketplaceId:string | * REQUIRED The marketplace for which to return the count.
        
            featureName:string | * REQUIRED The name of the feature.
        
            sellerSku:string | * REQUIRED Used to identify an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.
        

         Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop('path'), featureName), params=kwargs)
    
