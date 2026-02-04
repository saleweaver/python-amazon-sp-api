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
        
        Args:
            key marketplaceId:string | * REQUIRED A marketplace identifier. Specifies the marketplace for which items are returned.
        
        Returns:
            ApiResponse:
        """
        return await self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/finances/transfers/wallet/2024-03-01/accounts/{accountId}", method="GET")
    async def get_account(self, accountId, **kwargs) -> ApiResponse:
        """
        get_account(self, accountId, **kwargs) -> ApiResponse
        
        Retrieve a Seller Wallet bank account by Amazon account identifier.
        
        Args:
            accountId:string | * REQUIRED ID of the Amazon SW account
            key marketplaceId:string | * REQUIRED The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse:
        """
        return await self._request(fill_query_params(kwargs.pop("path"), accountId), params=kwargs, add_marketplace=False)

    @sp_endpoint("/finances/transfers/wallet/2024-03-01/accounts/{accountId}/balance", method="GET")
    async def list_account_balances(self, accountId, **kwargs) -> ApiResponse:
        """
        list_account_balances(self, accountId, **kwargs) -> ApiResponse
        
        Retrieve the balance in a given Seller Wallet bank account.
        
        Args:
            accountId:string | * REQUIRED ID of the Amazon SW account
            key marketplaceId:string | * REQUIRED The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse:
        """
        return await self._request(fill_query_params(kwargs.pop("path"), accountId), params=kwargs, add_marketplace=False)

    @sp_endpoint("/finances/transfers/wallet/2024-03-01/transactions", method="GET")
    async def list_account_transactions(self, **kwargs) -> ApiResponse:
        """
        list_account_transactions(self, **kwargs) -> ApiResponse
        
        Retrieve a list of transactions for a given Seller Wallet bank account.
        
        Args:
            key accountId:string | * REQUIRED ID of the Amazon SW account
            key nextPageToken:string | Pagination token to retrieve a specific page of results.
            key marketplaceId:string | * REQUIRED The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse:
        """
        return await self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/finances/transfers/wallet/2024-03-01/transactions", method="POST")
    async def create_transaction(self, **kwargs) -> ApiResponse:
        """
        create_transaction(self, **kwargs) -> ApiResponse
        
        Create a transaction request from a Seller Wallet account to another customer-provided account.
        
        Args:
            body: | * REQUIRED {'description': 'Request body to initiate a transaction from a SW bank account to another customer defined bank account\n',
         'example': {'customerPaymentReference': 'BG999999999',
                     'destinationTransactionInstrument': {'accountHolderName': 'John Doe',
                                                          'bankAccount': {'accountCountryCode': 'CN',
                                                                          'accountCurrency': 'CNY',
                                                                          'bankAccountNumberFormat': 'BBAN',
                                                                          'bankAccountNumberTail': '819',
                                                                          'bankAccountOwnershipType': 'SELF',
                                                                          'bankNumberFormat': 'BASIC',
                                                                          'routingNumber': 'HBUKGB4B'},
                                                          'bankAccountNumber': 'GB29RBOS60161331926819'},
                     'payeeContactInformation': {'addressLine1': 'Avenue John F. Kennedy 38',
                                                 'city': 'Luxembourg',
                                                 'countryCode': 'LU',
                                                 'emailAddress': 'johndoe@gmail.com',
                                                 'payeeEntityType': 'PERSON',
                                                 'payeeFirstName': 'John',
                                                 'payeeLastName': 'Doe',
                                                 'phoneNumber': '3450987121',
                                                 'postalCode': '1855',
                                                 'state': 'LUXEMBOURG'},
                     'requestTime': '2024-03-26T02:32:59.787Z',
                     'sourceAccountId': 'amzn1.account.SMUGN2EN3ZHWSRJKH2KCJPII5JEI',
                     'sourceAmount': {'amount': 100.0, 'currency': 'USD'},
                     'transactionDescription': 'This is transaction to partner',
                     'transferRateDetails': {'baseAmount': {'currencyAmount': 500.0, 'currencyCode': 'EUR'},
                                             'fees': [{'feeAmount': {'currencyAmount': 4.5, 'currencyCode': 'EUR'}, 'feeId': 'Unique_FeeId_001', 'feeRateValue': '0.9', 'feeType': 'TRANSACTION_FEE'},
                                                      {'feeAmount': {'currencyAmount': 0.9, 'currencyCode': 'EUR'}, 'feeId': 'Unique_FeeId_002', 'feeRateValue': '20.0', 'feeType': 'TAX'}],
                                             'fxRateDetails': {'baseRate': 7.6915, 'effectiveFxRate': 7.6084, 'fxRateId': 'UNIQUE_FX_RATE_ID_1', 'rateDirection': 'BUY'},
                                             'transferAmount': {'currencyAmount': 3804.2, 'currencyCode': 'CNY'}}},
         'properties': {'customerPaymentReference': {'description': 'If the payment is for VAT (Value-Added-Tax) then enter VAT identification number in this field which will be mandatory. The length constraint is 140 characters and do not allow user to '
                                                                    'enter any sensitive information other than VAT-ID.',
                                                     'example': 'BG999999999',
                                                     'type': 'string'},
                        'destinationAccountId': {'description': 'Optional field to specify the unique identifier of the destination bank account where the money needs to be deposited\n', 'example': 'amzn1.account.AJKBFWEJFBNH2KCJPII5FBN', 'type': 'string'},
                        'destinationTransactionInstrument': {'$ref': '#/definitions/TransactionInstrumentDetails', 'description': 'Destination bank account details of the transaction request\n'},
                        'payeeContactInformation': {'$ref': '#/definitions/PayeeContactInformation', 'description': 'The contact information of a payee.'},
                        'requestTime': {'description': 'The transaction initiation request time in date-time format\n', 'example': '2024-03-26T02:32:59.787Z', 'format': 'date-time', 'type': 'string'},
                        'sourceAccountId': {'description': 'The unique identifier of the source Amazon SW bank account from where the money needs to be debited\n', 'example': 'amzn1.account.SMUGN2EN3ZHWSRJKH2KCJPII5JEI', 'type': 'string'},
                        'sourceAmount': {'$ref': '#/definitions/Currency', 'description': "The transaction amount in the source account's currency format. Requests that use a currency other than the source bank account currency fail."},
                        'transactionDescription': {'description': 'A description of the transaction.', 'type': 'string'},
                        'transferRateDetails': {'$ref': '#/definitions/TransferRatePreview',
                                                'description': 'The fees and foreign exchange rates that apply to the transaction. Transfer Rate Preview is currently optional. This field is required when the third party honors the fees and rates of the '
                                                               'Seller Wallet transaction.'}},
         'required': ['sourceAccountId', 'destinationTransactionInstrument', 'sourceAmount', 'requestTime'],
         'type': 'object'}
            destAccountDigitalSignature:string | * REQUIRED Digital signature for the destination bank account details. For more information, refer to [Third-Party Provider Signature Guidance](https://developer-docs.amazon.com/sp-api/docs/tpp-registration-signature-guidance).
            amountDigitalSignature:string | * REQUIRED Digital signature for the source currency transaction amount. Sign in the order of the request definitions. You can omit empty or optional fields. For more information, refer to [Third-Party Provider Signature Guidance](https://developer-docs.amazon.com/sp-api/docs/tpp-registration-signature-guidance).
            key marketplaceId:string | * REQUIRED The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse:
        """
        headers = self.headers.copy()
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
        
        Args:
            transactionId:string | * REQUIRED ID of the Amazon SW transaction
            key marketplaceId:string | * REQUIRED The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse:
        """
        return await self._request(fill_query_params(kwargs.pop("path"), transactionId), params=kwargs, add_marketplace=False)

    @sp_endpoint("/finances/transfers/wallet/2024-03-01/transferPreview", method="GET")
    async def get_transfer_preview(self, **kwargs) -> ApiResponse:
        """
        get_transfer_preview(self, **kwargs) -> ApiResponse
        
        Returns list of potential fees on a transaction based on the source and destination country currency code
        
        Args:
            key sourceCountryCode:string | * REQUIRED Represents 2 character country code of source transaction account in ISO 3166 standard format.
            key sourceCurrencyCode:string | * REQUIRED Represents 3 letter currency code in ISO 4217 standard format of the source transaction country.
            key destinationCountryCode:string | * REQUIRED Represents 2 character country code of destination transaction account in ISO 3166 standard format.
            key destinationCurrencyCode:string | * REQUIRED Represents 3 letter currency code in ISO 4217 standard format of the destination transaction country.
            key baseAmount:number | * REQUIRED Represents the base transaction amount without any markup fees, rates that will be used to get the transfer preview.
            key marketplaceId:string | * REQUIRED The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse:
        """
        return await self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/finances/transfers/wallet/2024-03-01/transferSchedules", method="GET")
    async def list_transfer_schedules(self, **kwargs) -> ApiResponse:
        """
        list_transfer_schedules(self, **kwargs) -> ApiResponse
        
        Retrieve transfer schedules of a Seller Wallet bank account.
        
        Args:
            key accountId:string | * REQUIRED ID of the Amazon SW account
            key marketplaceId:string | * REQUIRED The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
            key nextPageToken:string | Pagination token to retrieve a specific page of results.
        
        Returns:
            ApiResponse:
        """
        return await self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/finances/transfers/wallet/2024-03-01/transferSchedules", method="POST")
    async def create_transfer_schedule(self, **kwargs) -> ApiResponse:
        """
        create_transfer_schedule(self, **kwargs) -> ApiResponse
        
        Create a transfer schedule request from a Seller Wallet account to another customer-provided account.
        
        Args:
            body: | * REQUIRED {'description': 'Request body to initiate a scheduled transfer from a SW bank account to another customer defined bank account\n',
         'example': {'destinationAccountId': 'amzn1.account.AJKBFWEJFBNH2KCJPII5FBN',
                     'destinationTransactionInstrument': {'accountHolderName': 'John Doe',
                                                          'bankAccount': {'accountCountryCode': 'CN',
                                                                          'accountCurrency': 'CNY',
                                                                          'bankAccountNumberFormat': 'BBAN',
                                                                          'bankAccountNumberTail': '819',
                                                                          'bankAccountOwnershipType': 'SELF',
                                                                          'bankNumberFormat': 'BASIC',
                                                                          'routingNumber': 'HBUKGB4B'},
                                                          'bankAccountNumber': 'GB29RBOS60161331926819'},
                     'paymentPreference': {'paymentPreferencePaymentType': 'PERCENTAGE', 'value': 25.5},
                     'sourceAccountId': 'amzn1.account.SMUGN2EN3ZHWSRJKH2KCJPII5JEI',
                     'sourceCurrencyCode': 'USD',
                     'transactionType': 'DEBIT',
                     'transferScheduleInformation': {'scheduleEndDate': '2027-03-01T00:00:00Z',
                                                     'scheduleExpression': {'recurringFrequency': 'WEEKLY', 'scheduleExpressionType': 'RECURRING'},
                                                     'scheduleStartDate': '2024-03-01T00:00:00Z',
                                                     'scheduleType': 'TIME_BASED'},
                     'transferScheduleStatus': 'ENABLED'},
         'properties': {'destinationAccountId': {'description': 'Optional field to specify the unique identifier of the destination bank account where the money needs to be deposited\n', 'example': 'amzn1.account.AJKBFWEJFBNH2KCJPII5FBN', 'type': 'string'},
                        'destinationTransactionInstrument': {'$ref': '#/definitions/TransactionInstrumentDetails', 'description': 'Destination bank account details of the transaction request\n'},
                        'paymentPreference': {'$ref': '#/definitions/PaymentPreference', 'description': 'Payment preference of the scheduled transfer\n'},
                        'sourceAccountId': {'description': 'The unique identifier of the source Amazon SW bank account from where the money needs to be debited\n', 'example': 'amzn1.account.SMUGN2EN3ZHWSRJKH2KCJPII5JEI', 'type': 'string'},
                        'sourceCurrencyCode': {'description': 'Represents 3 letter currency code in ISO 4217 standard format of the source payment method country\n', 'example': 'GBP', 'type': 'string'},
                        'transactionType': {'$ref': '#/definitions/TransactionType', 'description': 'Type of the scheduled transaction\n'},
                        'transferScheduleInformation': {'$ref': '#/definitions/TransferScheduleInformation', 'description': 'Fields required for the scheduled transfer\n'},
                        'transferScheduleStatus': {'$ref': '#/definitions/TransferScheduleStatus', 'description': 'Type of the transaction schedule which is mandatory field in request body if a transfer schedule needs to be updated\n'}},
         'required': ['sourceAccountId', 'sourceCurrencyCode', 'destinationAccountId', 'destinationTransactionInstrument', 'transactionType', 'transferScheduleInformation', 'paymentPreference'],
         'type': 'object'}
            destAccountDigitalSignature:string | * REQUIRED Digital signature for the destination bank account details.
            amountDigitalSignature:string | * REQUIRED Digital signature for the source currency transaction amount.
            key marketplaceId:string | * REQUIRED The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse:
        """
        headers = self.headers.copy()
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
        
        Args:
            body: | * REQUIRED {'description': 'Transfer schedule details and related historical details.',
         'example': {'paymentPreference': {'paymentPreferencePaymentType': 'PERCENTAGE', 'value': 25.5},
                     'transactionDestinationAccount': {'bankAccountCountryCode': 'EU',
                                                       'bankAccountCurrency': 'GBP',
                                                       'bankAccountHolderName': 'Dane Shipping',
                                                       'bankAccountNumberFormat': 'IBAN',
                                                       'bankAccountNumberTail': '819',
                                                       'bankName': 'Royal Bank of Scotland'},
                     'transactionSourceAccount': {'accountId': 'sourceAccountIdCase200',
                                                  'bankAccountCurrency': 'GBP',
                                                  'bankAccountHolderName': 'John Doe',
                                                  'bankAccountNumberFormat': 'IBAN',
                                                  'bankAccountNumberTail': '123',
                                                  'bankName': 'Amazon Seller Wallet'},
                     'transactionType': 'DEBIT',
                     'transferScheduleFailures': [{'transferScheduleFailureDate': '2024-04-01T10:30:00Z', 'transferScheduleFailureReason': 'INSUFFICIENT_BALANCE'}],
                     'transferScheduleId': 'amzn1.transferschedule.SMUGN2EN3ZHWSRJKH2KCJPII5JEI',
                     'transferScheduleInformation': {'scheduleEndDate': '2027-03-01T00:00:00Z',
                                                     'scheduleExpression': {'recurringFrequency': 'WEEKLY', 'scheduleExpressionType': 'RECURRING'},
                                                     'scheduleStartDate': '2024-03-01T00:00:00Z',
                                                     'scheduleType': 'TIME_BASED'},
                     'transferScheduleStatus': 'ENABLED'},
         'properties': {'paymentPreference': {'$ref': '#/definitions/PaymentPreference', 'description': 'Payment preference of the scheduled transfer. This information can be modified when updating a transfer schedule.\n'},
                        'transactionDestinationAccount': {'$ref': '#/definitions/TransactionAccount', 'description': 'Destination bank account details in the scheduled transfer. Here bankAccountCountryCode is a MANDATORY field\n'},
                        'transactionSourceAccount': {'$ref': '#/definitions/TransactionAccount', 'description': 'Source bank account details in the scheduled transfer\n'},
                        'transactionType': {'$ref': '#/definitions/TransactionType', 'description': 'Type of the transfer\n'},
                        'transferScheduleFailures': {'description': 'Collection that holds Transfer Schedules that has been cancelled or failed due to certain reasons.\n', 'items': {'$ref': '#/definitions/TransferScheduleFailures'}, 'type': 'array'},
                        'transferScheduleId': {'description': 'The unique identifier provided by Amazon to the scheduled transfer\n', 'type': 'string'},
                        'transferScheduleInformation': {'$ref': '#/definitions/TransferScheduleInformation', 'description': 'Fields required for the scheduled transfer. This information can be modified when updating a transfer schedule.\n'},
                        'transferScheduleStatus': {'$ref': '#/definitions/TransferScheduleStatus', 'description': 'Type of the transfer schedule. This information can be modified when updating a transfer schedule.\n'}},
         'required': ['transferScheduleId', 'transactionType', 'transactionDestinationAccount', 'transferScheduleStatus', 'transferScheduleInformation', 'transferScheduleFailures'],
         'type': 'object'}
            destAccountDigitalSignature:string | * REQUIRED Digital signature for the destination bank account details.
            amountDigitalSignature:string | * REQUIRED Digital signature for the source currency transaction amount.
            key marketplaceId:string | * REQUIRED The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse:
        """
        headers = self.headers.copy()
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
        
        Args:
            transferScheduleId:string | * REQUIRED A unique reference ID for a scheduled transfer.
            key marketplaceId:string | * REQUIRED The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse:
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
        
        Args:
            transferScheduleId:string | * REQUIRED The schedule ID of the Amazon Seller Wallet transfer.
            key marketplaceId:string | * REQUIRED The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse:
        """
        return await self._request(fill_query_params(kwargs.pop("path"), transferScheduleId), params=kwargs, add_marketplace=False)
