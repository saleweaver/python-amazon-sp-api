import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class VendorShipments(Client):
    """
    VendorShipments SP-API Client
    :link:

    The Selling Partner API for Retail Procurement Shipments provides programmatic access to retail shipping data for vendors.
    """

    @sp_endpoint("/vendor/shipping/v1/shipmentConfirmations", method="POST")
    def submit_shipment_confirmations(self, **kwargs) -> ApiResponse:
        """
        submit_shipment_confirmations(self, **kwargs) -> ApiResponse
        
        Submits one or more shipment confirmations for vendor orders.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                VendorShipments().submit_shipment_confirmations()
        
        Args:
            body: SubmitShipmentConfirmationsRequest | required A request to submit shipment confirmation.
        
        Returns:
            ApiResponse
        """

        return self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/vendor/shipping/v1/shipments", method="POST")
    def submit_shipments(self, **kwargs) -> ApiResponse:
        """
        submit_shipments(self, **kwargs) -> ApiResponse
        
        Submits one or more shipment request for vendor Orders.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                VendorShipments().submit_shipments()
        
        Args:
            body: SubmitShipments | required A request to submit shipment request.
        
        Returns:
            ApiResponse
        """

        return self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/vendor/shipping/v1/shipments", method="GET")
    def get_shipment_details(self, **kwargs) -> ApiResponse:
        """
        get_shipment_details(self, **kwargs) -> ApiResponse
        
        Returns the Details about Shipment, Carrier Details,  status of the shipment, container details and other details related to shipment based on the filter parameters value that you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                VendorShipments().get_shipment_details()
        
        Args:
            key limit: object |  The limit to the number of records returned. Default value is 50 records.
            key sortOrder: object |  Sort in ascending or descending order by purchase order creation date.
            key nextToken: object |  Used for pagination when there are more shipments than the specified result size limit.
            key createdAfter: object |  Get Shipment Details that became available after this timestamp will be included in the result. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key createdBefore: object |  Get Shipment Details that became available before this timestamp will be included in the result. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key shipmentConfirmedBefore: object |  Get Shipment Details by passing Shipment confirmed create Date Before. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key shipmentConfirmedAfter: object |  Get Shipment Details by passing Shipment confirmed create Date After. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key packageLabelCreatedBefore: object |  Get Shipment Details by passing Package label create Date by buyer. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key packageLabelCreatedAfter: object |  Get Shipment Details by passing Package label create Date After by buyer. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key shippedBefore: object |  Get Shipment Details by passing Shipped Date Before. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key shippedAfter: object |  Get Shipment Details by passing Shipped Date After. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key estimatedDeliveryBefore: object |  Get Shipment Details by passing Estimated Delivery Date Before. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key estimatedDeliveryAfter: object |  Get Shipment Details by passing Estimated Delivery Date After. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key shipmentDeliveryBefore: object |  Get Shipment Details by passing Shipment Delivery Date Before. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key shipmentDeliveryAfter: object |  Get Shipment Details by passing Shipment Delivery Date After. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key requestedPickUpBefore: object |  Get Shipment Details by passing Before Requested pickup date. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key requestedPickUpAfter: object |  Get Shipment Details by passing After Requested pickup date. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key scheduledPickUpBefore: object |  Get Shipment Details by passing Before scheduled pickup date. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key scheduledPickUpAfter: object |  Get Shipment Details by passing After Scheduled pickup date. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key currentShipmentStatus: object |  Get Shipment Details by passing Current shipment status.
            key vendorShipmentIdentifier: object |  Get Shipment Details by passing Vendor Shipment ID
            key buyerReferenceNumber: object |  Get Shipment Details by passing buyer Reference ID
            key buyerWarehouseCode: object |  Get Shipping Details based on buyer warehouse code. This value should be same as 'shipToParty.partyId' in the Shipment.
            key sellerWarehouseCode: object |  Get Shipping Details based on vendor warehouse code. This value should be same as 'sellingParty.partyId' in the Shipment.
        
        Returns:
            ApiResponse
        """

        return self._request(kwargs.pop("path"), params=kwargs)


    @sp_endpoint("/vendor/shipping/v1/shipmentConfirmation", method="POST")
    def submit_shipment_confirmation(self, **kwargs) -> ApiResponse:
        """
        submit_shipment_confirmation(self, **kwargs) -> ApiResponse
        
        Submits one shipment confirmation for vendor orders and get response immediately.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                VendorShipments().submit_shipment_confirmation()
        
        Args:
            body: SubmitShipmentConfirmationRequest | required A request to submit shipment confirmation.
        
        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), data=kwargs)



    @sp_endpoint("/vendor/shipping/v1/transportLabels", method="GET")
    def get_shipment_labels(self, **kwargs) -> ApiResponse:
        """
        get_shipment_labels(self, **kwargs) -> ApiResponse
        
        Returns small parcel shipment labels based on the filters that you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                VendorShipments().get_shipment_labels()
        
        Args:
            key limit: object |  The limit to the number of records returned. Default value is 50 records.
            key sortOrder: object |  Sort the list by shipment label creation date in ascending or descending order.
            key nextToken: object |  A token that you use to retrieve the next page of results. The response includes `nextToken` when the number of results exceeds the specified `pageSize` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages.
            key labelCreatedAfter: object |  Shipment labels created after this time will be included in the result. This field must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format.
            key labelCreatedBefore: object |  Shipment labels created before this time will be included in the result. This field must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format.
            key buyerReferenceNumber: object |  Get Shipment labels by passing buyer reference number.
            key vendorShipmentIdentifier: object |  Get Shipment labels by passing vendor shipment identifier.
            key sellerWarehouseCode: object |  Get Shipping labels based on vendor warehouse code. This value must be same as the `sellingParty.partyId` in the shipment.
        
        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), params=kwargs)
