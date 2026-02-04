from sp_api.base import ApiResponse, sp_endpoint, fill_query_params
from sp_api.asyncio.base import AsyncBaseClient


class InvoicesV20240619(AsyncBaseClient):
    """
    Invoices SP-API Client
    :link:

    Use the Selling Partner API for Invoices to retrieve and manage invoice-related operations, which can help selling partners manage their bookkeeping processes.
    """

    @sp_endpoint("/tax/invoices/2024-06-19/attributes", method="GET")
    async def get_invoices_attributes(self, **kwargs) -> ApiResponse:
        """
        get_invoices_attributes(self, **kwargs) -> ApiResponse
        
        Returns marketplace-dependent schemas and their respective set of possible values.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        
        Args:
            key marketplaceId:string | * REQUIRED The marketplace identifier.
        
        Returns:
            ApiResponse:
        """
        return await self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/tax/invoices/2024-06-19/documents/{invoicesDocumentId}", method="GET")
    async def get_invoices_document(self, invoicesDocumentId, **kwargs) -> ApiResponse:
        """
        get_invoices_document(self, invoicesDocumentId, **kwargs) -> ApiResponse
        
        Returns the invoice document's ID and URL. Use the URL to download the ZIP file, which contains the invoices from the corresponding `createInvoicesExport` request.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 1 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        
        Args:
            invoicesDocumentId:string | * REQUIRED The export document identifier.
        
        Returns:
            ApiResponse:
        """
        return await self._request(fill_query_params(kwargs.pop("path"), invoicesDocumentId), params=kwargs, add_marketplace=False)

    @sp_endpoint("/tax/invoices/2024-06-19/exports", method="GET")
    async def get_invoices_exports(self, **kwargs) -> ApiResponse:
        """
        get_invoices_exports(self, **kwargs) -> ApiResponse
        
        Returns invoice exports details for exports that match the filters that you specify.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.1 | 20 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        
        Args:
            key marketplaceId:string | * REQUIRED The returned exports match the specified marketplace.
            key dateStart:string | The earliest export creation date and time for exports that you want to include in the response. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default is 30 days ago.
            key nextToken:string | The response includes `nextToken` when the number of results exceeds the specified `pageSize` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages.
            key pageSize:integer | The maximum number of invoices to return in a single call.
        
        Minimum: 1
        
        Maximum: 100
            key dateEnd:string | The latest export creation date and time for exports that you want to include in the response. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default value is the time of the request.
            key status:string | Return exports matching the status specified.
        
        Returns:
            ApiResponse:
        """
        return await self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/tax/invoices/2024-06-19/exports", method="POST")
    async def create_invoices_export(self, **kwargs) -> ApiResponse:
        """
        create_invoices_export(self, **kwargs) -> ApiResponse
        
        Creates an invoice export request.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.167 | 1 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        
        Args:
            body: | * REQUIRED {'description': 'The information required to create the export request.',
         'example': {'dateEnd': '2024-07-30T23:59:59',
                     'dateStart': '2024-07-01T00:00:00',
                     'externalInvoiceId': '1283743',
                     'fileFormat': 'XML',
                     'invoiceType': 'SYMBOLIC_RETURN',
                     'marketplaceId': 'A2Q3Y263D00KWC',
                     'series': '32',
                     'statuses': ['AUTHORIZED'],
                     'transactionIdentifier': {'id': '94cd4e1a-5cc5-486d-b592-045a95a168e1', 'name': 'BUSINESS_TRANSACTION_ID'},
                     'transactionType': 'CUSTOMER_SALES'},
         'properties': {'dateEnd': {'description': 'The latest invoice creation date for invoices that you want to include in the response. Dates are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default is the '
                                                   'time of the request.',
                                    'format': 'date',
                                    'type': 'string'},
                        'dateStart': {'description': 'The earliest invoice creation date for invoices that you want to include in the response. Dates are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default is '
                                                     '24 hours prior to the time of the request.',
                                      'format': 'date',
                                      'type': 'string'},
                        'externalInvoiceId': {'description': 'The external ID of the invoices you want included in the response.', 'type': 'string'},
                        'fileFormat': {'$ref': '#/definitions/FileFormat'},
                        'invoiceType': {'description': 'The marketplace-specific classification of the invoice type. Use the `getInvoicesAttributes` operation to check `invoiceType` options.', 'type': 'string'},
                        'marketplaceId': {'description': 'The ID of the marketplace from which you want the invoices.', 'type': 'string'},
                        'series': {'description': 'The series number of the invoices you want included in the response.', 'type': 'string'},
                        'statuses': {'description': 'A list of statuses that you can use to filter invoices. Use the `getInvoicesAttributes` operation to check invoice status options.\n\nMin count: 1',
                                     'items': {'type': 'string'},
                                     'minItems': 1,
                                     'type': 'array'},
                        'transactionIdentifier': {'$ref': '#/definitions/TransactionIdentifier'},
                        'transactionType': {'description': 'The marketplace-specific classification of the transaction type for which the invoice was created. Use the `getInvoicesAttributes` operation to check `transactionType` options', 'type': 'string'}},
         'required': ['marketplaceId'],
         'type': 'object'}
        
        Returns:
            ApiResponse:
        """
        return await self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)

    @sp_endpoint("/tax/invoices/2024-06-19/exports/{exportId}", method="GET")
    async def get_invoices_export(self, exportId, **kwargs) -> ApiResponse:
        """
        get_invoices_export(self, exportId, **kwargs) -> ApiResponse
        
        Returns invoice export details (including the `exportDocumentId`, if available) for the export that you specify.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 15 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        
        Args:
            exportId:string | * REQUIRED The unique identifier for the export.
        
        Returns:
            ApiResponse:
        """
        return await self._request(fill_query_params(kwargs.pop("path"), exportId), params=kwargs, add_marketplace=False)

    @sp_endpoint("/tax/invoices/2024-06-19/governmentInvoiceRequests", method="GET")
    async def get_government_invoice_status(self, **kwargs) -> ApiResponse:
        """
        get_government_invoice_status(self, **kwargs) -> ApiResponse
        
        Returns the status of an invoice generation request.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 1 |
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Args:
            key marketplaceId:string | * REQUIRED The invoices status will match the marketplace that you specify.
            key transactionType:string | * REQUIRED Marketplace specific classification of the transaction type that originated the invoice. Check 'transactionType' options using 'getInvoicesAttributes' operation.
            key shipmentId:string | * REQUIRED The unique shipment identifier to get an invoice for.
            key invoiceType:string | * REQUIRED Marketplace specific classification of the invoice type. Check 'invoiceType' options using 'getInvoicesAttributes' operation.
            key inboundPlanId:string | The unique InboundPlan identifier in which the shipment is contained and for which the invoice will be created.
        
        Returns:
            ApiResponse:
        """
        return await self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/tax/invoices/2024-06-19/governmentInvoiceRequests", method="POST")
    async def create_government_invoice(self, **kwargs) -> ApiResponse:
        """
        create_government_invoice(self, **kwargs) -> ApiResponse
        
        Submits an asynchronous government invoice creation request.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 1 |
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Args:
            body: | * REQUIRED {'description': 'Information required to create the government invoice.',
         'example': {'contexts': [{'address': 'An address',
                                   'contextType': 'CarrierDetailsContext',
                                   'federalTaxId': '46204217000177',
                                   'name': 'testCarrier',
                                   'regionCode': 'SP',
                                   'regionTaxId': '503348865972',
                                   'vehicleLicensePlate': 'AAA0A00',
                                   'vehicleRegistrationRegionCode': 'SP'}],
                     'inboundPlanId': 'wf44e473-3f4d-4c6d-a80b-230e644b0c39',
                     'invoiceType': 'REMITTANCE',
                     'marketplaceId': 'A2Q3Y263D00KWC',
                     'shipmentId': 'sh109b72-7b27-4e97-9fd1-3b56915fbc95',
                     'transactionType': 'INBOUND_SHIPMENT'},
         'properties': {'contexts': {'description': 'Object that contains additional invoice creation information', 'items': {'$ref': '#/definitions/CarrierDetailsContext'}, 'type': 'array'},
                        'inboundPlanId': {'description': 'The unique InboundPlan identifier in which the shipment is contained and for which the invoice will be created.', 'type': 'string'},
                        'invoiceType': {'description': "Marketplace specific classification of the invoice type. Check 'invoiceType' options using 'getInvoicesAttributes' operation.", 'type': 'string'},
                        'marketplaceId': {'description': 'The government invoices creation request will match the national authoritative source of the given marketplace.', 'type': 'string'},
                        'shipmentId': {'description': 'The unique shipment identifier to get an invoice for.', 'type': 'string'},
                        'transactionType': {'description': "Marketplace specific classification of the transaction type that originated the invoice. Check 'transactionType' options using 'getInvoicesAttributes' operation.", 'type': 'string'}},
         'required': ['invoiceType', 'marketplaceId', 'shipmentId', 'transactionType'],
         'type': 'object'}
        
        Returns:
            ApiResponse:
        """
        return await self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)

    @sp_endpoint("/tax/invoices/2024-06-19/governmentInvoiceRequests/{shipmentId}", method="GET")
    async def get_government_invoice_document(self, shipmentId, **kwargs) -> ApiResponse:
        """
        get_government_invoice_document(self, shipmentId, **kwargs) -> ApiResponse
        
        Returns an invoiceDocument object containing an invoiceDocumentUrl .
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 1 |
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Args:
            key marketplaceId:string | * REQUIRED The invoices returned will match the marketplace that you specify.
            key transactionType:string | * REQUIRED Marketplace specific classification of the transaction type that originated the invoice. Check 'transactionType' options using 'getInvoicesAttributes' operation.
            shipmentId:string | * REQUIRED The unique shipment identifier to get an invoice for.
            key invoiceType:string | * REQUIRED Marketplace specific classification of the invoice type. Check 'invoiceType' options using 'getInvoicesAttributes' operation.
            key inboundPlanId:string | The unique InboundPlan identifier in which the shipment is contained and for which the invoice will be created.
            key fileFormat:string | Requested file format. Default is XML
        
        Returns:
            ApiResponse:
        """
        return await self._request(fill_query_params(kwargs.pop("path"), shipmentId), params=kwargs, add_marketplace=False)

    @sp_endpoint("/tax/invoices/2024-06-19/invoices", method="GET")
    async def get_invoices(self, **kwargs) -> ApiResponse:
        """
        get_invoices(self, **kwargs) -> ApiResponse
        
        Returns invoice details for the invoices that match the filters that you specify.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.1 | 20 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        
        Args:
            key transactionIdentifierName:string | The name of the transaction identifier filter. If you provide a value for this field, you must also provide a value for the `transactionIdentifierId` field.Use the `getInvoicesAttributes` operation to check `transactionIdentifierName` options.
            key pageSize:integer | The maximum number of invoices you want to return in a single call.
        
        Minimum: 1
        
        Maximum: 200
            key dateEnd:string | The latest invoice creation date for invoices that you want to include in the response. Dates are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default is the current date-time.
            key marketplaceId:string | * REQUIRED The response includes only the invoices that match the specified marketplace.
            key transactionType:string | The marketplace-specific classification of the transaction type for which the invoice was created. Use the `getInvoicesAttributes` operation to check `transactionType` options.
            key transactionIdentifierId:string | The ID of the transaction identifier filter. If you provide a value for this field, you must also provide a value for the `transactionIdentifierName` field.
            key dateStart:string | The earliest invoice creation date for invoices that you want to include in the response. Dates are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The default is 24 hours prior to the time of the request.
            key series:string | Return invoices with the specified series number.
            key nextToken:string | The response includes `nextToken` when the number of results exceeds the specified `pageSize` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages.
            key sortOrder:string | Sort the invoices in the response in ascending or descending order.
            key invoiceType:string | The marketplace-specific classification of the invoice type. Use the `getInvoicesAttributes` operation to check `invoiceType` options.
            key statuses:array | A list of statuses that you can use to filter invoices. Use the `getInvoicesAttributes` operation to check invoice status options.
        
        Min count: 1
            key externalInvoiceId:string | Return invoices that match this external ID. This is typically the Government Invoice ID.
            key sortBy:string | The attribute by which you want to sort the invoices in the response.
        
        Returns:
            ApiResponse:
        """
        return await self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/tax/invoices/2024-06-19/invoices/{invoiceId}", method="GET")
    async def get_invoice(self, invoiceId, **kwargs) -> ApiResponse:
        """
        get_invoice(self, invoiceId, **kwargs) -> ApiResponse
        
        Returns invoice data for the specified invoice. This operation returns only a subset of the invoices data; refer to the response definition to get all the possible attributes.
        To get the full invoice, use the `createInvoicesExport` operation to start an export request.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 15 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        
        Args:
            key marketplaceId:string | * REQUIRED The marketplace from which you want the invoice.
            invoiceId:string | * REQUIRED The invoice identifier.
        
        Returns:
            ApiResponse:
        """
        return await self._request(fill_query_params(kwargs.pop("path"), invoiceId), params=kwargs, add_marketplace=False)
