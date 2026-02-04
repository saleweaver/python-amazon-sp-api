from sp_api.base import ApiResponse, sp_endpoint, fill_query_params
from sp_api.asyncio.base import AsyncBaseClient


class SellerWalletV20240301(AsyncBaseClient):
    """
    SellerWallet SP-API Client
    :link:

    The Selling Partner API for Seller Wallet (Seller Wallet API) provides financial information that is relevant to a seller's Seller Wallet account. You can obtain financial events, balances, and transfer schedules for Seller Wallet accounts. You can also schedule and initiate transactions.
    """

    @sp_endpoint("/finances/transfers/wallet/2024-03-01/accounts", method="GET")
    async def list_accounts(self, **kwargs) -> ApiResponse:
        """
        list_accounts(self, **kwargs) -> ApiResponse
        
        Get Seller Wallet accounts for a seller.
        
        Examples:
            literal blocks::
            
                await SellerWalletV20240301().list_accounts()
        
        Args:
            key marketplaceId: object | required A marketplace identifier. Specifies the marketplace for which items are returned.
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/finances/transfers/wallet/2024-03-01/accounts/{accountId}", method="GET")
    async def get_account(self, accountId, **kwargs) -> ApiResponse:
        """
        get_account(self, accountId, **kwargs) -> ApiResponse
        
        Retrieve a Seller Wallet bank account by Amazon account identifier.
        
        Examples:
            literal blocks::
            
                await SellerWalletV20240301().get_account("value")
        
        Args:
            accountId: object | required ID of the Amazon SW account
            key marketplaceId: object | required The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), accountId), params=kwargs, add_marketplace=False)

    @sp_endpoint("/finances/transfers/wallet/2024-03-01/accounts/{accountId}/balance", method="GET")
    async def list_account_balances(self, accountId, **kwargs) -> ApiResponse:
        """
        list_account_balances(self, accountId, **kwargs) -> ApiResponse
        
        Retrieve the balance in a given Seller Wallet bank account.
        
        Examples:
            literal blocks::
            
                await SellerWalletV20240301().list_account_balances("value")
        
        Args:
            accountId: object | required ID of the Amazon SW account
            key marketplaceId: object | required The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), accountId), params=kwargs, add_marketplace=False)

    @sp_endpoint("/finances/transfers/wallet/2024-03-01/transactions", method="GET")
    async def list_account_transactions(self, **kwargs) -> ApiResponse:
        """
        list_account_transactions(self, **kwargs) -> ApiResponse
        
        Retrieve a list of transactions for a given Seller Wallet bank account.
        
        Examples:
            literal blocks::
            
                await SellerWalletV20240301().list_account_transactions()
        
        Args:
            key accountId: object | required ID of the Amazon SW account
            key nextPageToken: object |  Pagination token to retrieve a specific page of results.
            key marketplaceId: object | required The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/finances/transfers/wallet/2024-03-01/transactions", method="POST")
    async def create_transaction(self, **kwargs) -> ApiResponse:
        """
        create_transaction(self, **kwargs) -> ApiResponse
        
        Create a transaction request from a Seller Wallet account to another customer-provided account.
        
        Examples:
            literal blocks::
            
                await SellerWalletV20240301().create_transaction()
        
        Args:
            body: TransactionInitiationRequest | required Defines the actual payload of the request
            destAccountDigitalSignature: object | required Digital signature for the destination bank account details. For more information, refer to [Third-Party Provider Signature Guidance](https://developer-docs.amazon.com/sp-api/docs/tpp-registration-signature-guidance).
            amountDigitalSignature: object | required Digital signature for the source currency transaction amount. Sign in the order of the request definitions. You can omit empty or optional fields. For more information, refer to [Third-Party Provider Signature Guidance](https://developer-docs.amazon.com/sp-api/docs/tpp-registration-signature-guidance).
            key marketplaceId: object | required The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse
        """
        headers = await self._get_headers()
        if "destAccountDigitalSignature" in kwargs:
            headers["destAccountDigitalSignature"] = kwargs.pop("destAccountDigitalSignature")
        if "amountDigitalSignature" in kwargs:
            headers["amountDigitalSignature"] = kwargs.pop("amountDigitalSignature")
        params = {}
        if "marketplaceId" in kwargs:
            params["marketplaceId"] = kwargs.pop("marketplaceId")
        return await self._request(kwargs.pop("path"), params=params, data=kwargs, headers=headers, add_marketplace=False)

    @sp_endpoint("/finances/transfers/wallet/2024-03-01/transactions/{transactionId}", method="GET")
    async def get_transaction(self, transactionId, **kwargs) -> ApiResponse:
        """
        get_transaction(self, transactionId, **kwargs) -> ApiResponse
        
        Returns a transaction
        
        Examples:
            literal blocks::
            
                await SellerWalletV20240301().get_transaction("value")
        
        Args:
            transactionId: object | required ID of the Amazon SW transaction
            key marketplaceId: object | required The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), transactionId), params=kwargs, add_marketplace=False)

    @sp_endpoint("/finances/transfers/wallet/2024-03-01/transferPreview", method="GET")
    async def get_transfer_preview(self, **kwargs) -> ApiResponse:
        """
        get_transfer_preview(self, **kwargs) -> ApiResponse
        
        Returns list of potential fees on a transaction based on the source and destination country currency code
        
        Examples:
            literal blocks::
            
                await SellerWalletV20240301().get_transfer_preview()
        
        Args:
            key sourceCountryCode: object | required Represents 2 character country code of source transaction account in ISO 3166 standard format.
            key sourceCurrencyCode: object | required Represents 3 letter currency code in ISO 4217 standard format of the source transaction country.
            key destinationCountryCode: object | required Represents 2 character country code of destination transaction account in ISO 3166 standard format.
            key destinationCurrencyCode: object | required Represents 3 letter currency code in ISO 4217 standard format of the destination transaction country.
            key baseAmount: object | required Represents the base transaction amount without any markup fees, rates that will be used to get the transfer preview.
            key marketplaceId: object | required The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/finances/transfers/wallet/2024-03-01/transferSchedules", method="GET")
    async def list_transfer_schedules(self, **kwargs) -> ApiResponse:
        """
        list_transfer_schedules(self, **kwargs) -> ApiResponse
        
        Retrieve transfer schedules of a Seller Wallet bank account.
        
        Examples:
            literal blocks::
            
                await SellerWalletV20240301().list_transfer_schedules()
        
        Args:
            key accountId: object | required ID of the Amazon SW account
            key marketplaceId: object | required The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
            key nextPageToken: object |  Pagination token to retrieve a specific page of results.
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/finances/transfers/wallet/2024-03-01/transferSchedules", method="POST")
    async def create_transfer_schedule(self, **kwargs) -> ApiResponse:
        """
        create_transfer_schedule(self, **kwargs) -> ApiResponse
        
        Create a transfer schedule request from a Seller Wallet account to another customer-provided account.
        
        Examples:
            literal blocks::
            
                await SellerWalletV20240301().create_transfer_schedule()
        
        Args:
            body: TransferScheduleRequest | required Defines the actual payload of the request
            destAccountDigitalSignature: object | required Digital signature for the destination bank account details.
            amountDigitalSignature: object | required Digital signature for the source currency transaction amount.
            key marketplaceId: object | required The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse
        """
        headers = await self._get_headers()
        if "destAccountDigitalSignature" in kwargs:
            headers["destAccountDigitalSignature"] = kwargs.pop("destAccountDigitalSignature")
        if "amountDigitalSignature" in kwargs:
            headers["amountDigitalSignature"] = kwargs.pop("amountDigitalSignature")
        params = {}
        if "marketplaceId" in kwargs:
            params["marketplaceId"] = kwargs.pop("marketplaceId")
        return await self._request(kwargs.pop("path"), params=params, data=kwargs, headers=headers, add_marketplace=False)

    @sp_endpoint("/finances/transfers/wallet/2024-03-01/transferSchedules", method="PUT")
    async def update_transfer_schedule(self, **kwargs) -> ApiResponse:
        """
        update_transfer_schedule(self, **kwargs) -> ApiResponse
        
        Returns a transfer belonging to the updated scheduled transfer request
        
        Examples:
            literal blocks::
            
                await SellerWalletV20240301().update_transfer_schedule()
        
        Args:
            body: TransferSchedule | required Defines the actual payload of the scheduled transfer request that is to be updated.
            destAccountDigitalSignature: object | required Digital signature for the destination bank account details.
            amountDigitalSignature: object | required Digital signature for the source currency transaction amount.
            key marketplaceId: object | required The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse
        """
        headers = await self._get_headers()
        if "destAccountDigitalSignature" in kwargs:
            headers["destAccountDigitalSignature"] = kwargs.pop("destAccountDigitalSignature")
        if "amountDigitalSignature" in kwargs:
            headers["amountDigitalSignature"] = kwargs.pop("amountDigitalSignature")
        params = {}
        if "marketplaceId" in kwargs:
            params["marketplaceId"] = kwargs.pop("marketplaceId")
        return await self._request(kwargs.pop("path"), params=params, data=kwargs, headers=headers, add_marketplace=False)

    @sp_endpoint("/finances/transfers/wallet/2024-03-01/transferSchedules/{transferScheduleId}", method="DELETE")
    async def delete_schedule_transaction(self, transferScheduleId, **kwargs) -> ApiResponse:
        """
        delete_schedule_transaction(self, transferScheduleId, **kwargs) -> ApiResponse
        
        Delete a transaction request that is scheduled from Amazon Seller Wallet account to another customer-provided account.
        
        Examples:
            literal blocks::
            
                await SellerWalletV20240301().delete_schedule_transaction("value")
        
        Args:
            transferScheduleId: object | required A unique reference ID for a scheduled transfer.
            key marketplaceId: object | required The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse
        """
        params = {}
        if "marketplaceId" in kwargs:
            params["marketplaceId"] = kwargs.pop("marketplaceId")
        return await self._request(fill_query_params(kwargs.pop("path"), transferScheduleId), params=params, data=kwargs, add_marketplace=False)

    @sp_endpoint("/finances/transfers/wallet/2024-03-01/transferSchedules/{transferScheduleId}", method="GET")
    async def get_transfer_schedule(self, transferScheduleId, **kwargs) -> ApiResponse:
        """
        get_transfer_schedule(self, transferScheduleId, **kwargs) -> ApiResponse
        
        Find a particular Amazon Seller Wallet account transfer schedule.
        
        Examples:
            literal blocks::
            
                await SellerWalletV20240301().get_transfer_schedule("value")
        
        Args:
            transferScheduleId: object | required The schedule ID of the Amazon Seller Wallet transfer.
            key marketplaceId: object | required The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), transferScheduleId), params=kwargs, add_marketplace=False)
