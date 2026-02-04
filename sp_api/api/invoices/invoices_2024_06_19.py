from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class InvoicesV20240619(Client):
    """
    Invoices SP-API Client
    :link:

    Use the Selling Partner API for Invoices to retrieve and manage invoice-related operations, which can help selling partners manage their bookkeeping processes.
    """

    @sp_endpoint("/tax/invoices/2024-06-19/attributes", method="GET")
    def get_invoices_attributes(self, **kwargs) -> ApiResponse:
        """
        get_invoices_attributes(self, **kwargs) -> ApiResponse
        
        Returns marketplace-dependent schemas and their respective set of possible values.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                InvoicesV20240619().get_invoices_attributes()
        
        Args:
            key marketplaceId: object | required The marketplace identifier.
        
        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/tax/invoices/2024-06-19/documents/{invoicesDocumentId}", method="GET")
    def get_invoices_document(self, invoicesDocumentId, **kwargs) -> ApiResponse:
        """
        get_invoices_document(self, invoicesDocumentId, **kwargs) -> ApiResponse
        
        Returns the invoice document's ID and URL. Use the URL to download the ZIP file, which contains the invoices from the corresponding `createInvoicesExport` request.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0167                                  1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                InvoicesV20240619().get_invoices_document("value")
        
        Args:
            invoicesDocumentId: object | required The export document identifier.
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), invoicesDocumentId), params=kwargs, add_marketplace=False)

    @sp_endpoint("/tax/invoices/2024-06-19/exports", method="GET")
    def get_invoices_exports(self, **kwargs) -> ApiResponse:
        """
        get_invoices_exports(self, **kwargs) -> ApiResponse
        
        Returns invoice exports details for exports that match the filters that you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.1                                     20
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                InvoicesV20240619().get_invoices_exports()
        
        Args:
            key marketplaceId: object | required The returned exports match the specified marketplace.
            key dateStart: object |  The earliest export creation date and time for exports that you want to include in the response. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default is 30 days ago.
            key nextToken: object |  The response includes `nextToken` when the number of results exceeds the specified `pageSize` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages.
            key pageSize: object |  The maximum number of invoices to return in a single call.
                Minimum: 1
                Maximum: 100
            key dateEnd: object |  The latest export creation date and time for exports that you want to include in the response. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default value is the time of the request.
            key status: object |  Return exports matching the status specified.
        
        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/tax/invoices/2024-06-19/exports", method="POST")
    def create_invoices_export(self, **kwargs) -> ApiResponse:
        """
        create_invoices_export(self, **kwargs) -> ApiResponse
        
        Creates an invoice export request.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.167                                   1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                InvoicesV20240619().create_invoices_export()
        
        Args:
            body: ExportInvoicesRequest | required Information required to create the export request.
        
        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)

    @sp_endpoint("/tax/invoices/2024-06-19/exports/{exportId}", method="GET")
    def get_invoices_export(self, exportId, **kwargs) -> ApiResponse:
        """
        get_invoices_export(self, exportId, **kwargs) -> ApiResponse
        
        Returns invoice export details (including the `exportDocumentId`, if available) for the export that you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       15
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                InvoicesV20240619().get_invoices_export("value")
        
        Args:
            exportId: object | required The unique identifier for the export.
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), exportId), params=kwargs, add_marketplace=False)

    @sp_endpoint("/tax/invoices/2024-06-19/governmentInvoiceRequests", method="GET")
    def get_government_invoice_status(self, **kwargs) -> ApiResponse:
        """
        get_government_invoice_status(self, **kwargs) -> ApiResponse
        
        Returns the status of an invoice generation request.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0167                                  1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                InvoicesV20240619().get_government_invoice_status()
        
        Args:
            key marketplaceId: object | required The invoices status will match the marketplace that you specify.
            key transactionType: object | required Marketplace specific classification of the transaction type that originated the invoice. Check 'transactionType' options using 'getInvoicesAttributes' operation.
            key shipmentId: object | required The unique shipment identifier to get an invoice for.
            key invoiceType: object | required Marketplace specific classification of the invoice type. Check 'invoiceType' options using 'getInvoicesAttributes' operation.
            key inboundPlanId: object |  The unique InboundPlan identifier in which the shipment is contained and for which the invoice will be created.
        
        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/tax/invoices/2024-06-19/governmentInvoiceRequests", method="POST")
    def create_government_invoice(self, **kwargs) -> ApiResponse:
        """
        create_government_invoice(self, **kwargs) -> ApiResponse
        
        Submits an asynchronous government invoice creation request.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0167                                  1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                InvoicesV20240619().create_government_invoice()
        
        Args:
            body: GovernmentInvoiceRequest | required Information required to create the government invoice.
        
        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)

    @sp_endpoint("/tax/invoices/2024-06-19/governmentInvoiceRequests/{shipmentId}", method="GET")
    def get_government_invoice_document(self, shipmentId, **kwargs) -> ApiResponse:
        """
        get_government_invoice_document(self, shipmentId, **kwargs) -> ApiResponse
        
        Returns an invoiceDocument object containing an invoiceDocumentUrl .
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0167                                  1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                InvoicesV20240619().get_government_invoice_document("value")
        
        Args:
            key marketplaceId: object | required The invoices returned will match the marketplace that you specify.
            key transactionType: object | required Marketplace specific classification of the transaction type that originated the invoice. Check 'transactionType' options using 'getInvoicesAttributes' operation.
            shipmentId: object | required The unique shipment identifier to get an invoice for.
            key invoiceType: object | required Marketplace specific classification of the invoice type. Check 'invoiceType' options using 'getInvoicesAttributes' operation.
            key inboundPlanId: object |  The unique InboundPlan identifier in which the shipment is contained and for which the invoice will be created.
            key fileFormat: object |  Requested file format. Default is XML
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), shipmentId), params=kwargs, add_marketplace=False)

    @sp_endpoint("/tax/invoices/2024-06-19/invoices", method="GET")
    def get_invoices(self, **kwargs) -> ApiResponse:
        """
        get_invoices(self, **kwargs) -> ApiResponse
        
        Returns invoice details for the invoices that match the filters that you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.1                                     20
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                InvoicesV20240619().get_invoices()
        
        Args:
            key transactionIdentifierName: object |  The name of the transaction identifier filter. If you provide a value for this field, you must also provide a value for the `transactionIdentifierId` field.Use the `getInvoicesAttributes` operation to check `transactionIdentifierName` options.
            key pageSize: object |  The maximum number of invoices you want to return in a single call.
                Minimum: 1
                Maximum: 200
            key dateEnd: object |  The latest invoice creation date for invoices that you want to include in the response. Dates are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default is the current date-time.
            key marketplaceId: object | required The response includes only the invoices that match the specified marketplace.
            key transactionType: object |  The marketplace-specific classification of the transaction type for which the invoice was created. Use the `getInvoicesAttributes` operation to check `transactionType` options.
            key transactionIdentifierId: object |  The ID of the transaction identifier filter. If you provide a value for this field, you must also provide a value for the `transactionIdentifierName` field.
            key dateStart: object |  The earliest invoice creation date for invoices that you want to include in the response. Dates are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default is 24 hours prior to the time of the request.
            key series: object |  Return invoices with the specified series number.
            key nextToken: object |  The response includes `nextToken` when the number of results exceeds the specified `pageSize` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages.
            key sortOrder: object |  Sort the invoices in the response in ascending or descending order.
            key invoiceType: object |  The marketplace-specific classification of the invoice type. Use the `getInvoicesAttributes` operation to check `invoiceType` options.
            key statuses: object |  A list of statuses that you can use to filter invoices. Use the `getInvoicesAttributes` operation to check invoice status options.
                Min count: 1
            key externalInvoiceId: object |  Return invoices that match this external ID. This is typically the Government Invoice ID.
            key sortBy: object |  The attribute by which you want to sort the invoices in the response.
        
        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/tax/invoices/2024-06-19/invoices/{invoiceId}", method="GET")
    def get_invoice(self, invoiceId, **kwargs) -> ApiResponse:
        """
        get_invoice(self, invoiceId, **kwargs) -> ApiResponse
        
        Returns invoice data for the specified invoice. This operation returns only a subset of the invoices data; refer to the response definition to get all the possible attributes.
        To get the full invoice, use the `createInvoicesExport` operation to start an export request.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       15
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                InvoicesV20240619().get_invoice("value")
        
        Args:
            key marketplaceId: object | required The marketplace from which you want the invoice.
            invoiceId: object | required The invoice identifier.
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), invoiceId), params=kwargs, add_marketplace=False)
