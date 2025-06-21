"""
Generated API client from Swagger/OpenAPI specification.
This file was auto-generated. Do not edit manually.
"""

import json
from typing import (Any, Dict, Generic, List, Optional, TypeVar, Union, cast,
                    overload)

import httpx
from pydantic import BaseModel
# Import all models
from sp_api.api.models.seller_wallet.seller_wallet_2024_03_01 import *
from sp_api.base import ApiResponse, Client, fill_query_params, sp_endpoint

T = TypeVar("T")


class SellerWallet_V_2024_03_01(Client):
    """
    The Selling Partner API for Amazon Seller Wallet Open Banking API - 2024-03-01

    The Selling Partner API for Seller Wallet (Seller Wallet API) provides financial information that is relevant to a seller's Seller Wallet account. You can obtain financial events, balances, and transfer schedules for Seller Wallet accounts. You can also schedule and initiate transactions.
    """

    @overload
    def list_accounts(
        self, request: ListAccountsRequest, *args, **kwargs
    ) -> ApiResponse[BankAccountListing]:
        """
        Get all Seller Wallet accounts for a given seller.
        """
        ...

    @sp_endpoint("/finances/transfers/wallet/2024-03-01/accounts", method="GET")
    def list_accounts(self, *args, **kwargs) -> ApiResponse[BankAccountListing]:
        """
        Get all Seller Wallet accounts for a given seller.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, ListAccountsRequest):
            request = ListAccountsRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=BankAccountListing
        )

    @overload
    def get_account(
        self, request: GetAccountRequest, *args, **kwargs
    ) -> ApiResponse[BankAccount]:
        """
        Retrieve an Amazon Seller Wallet bank account by Amazon account identifier.
        """
        ...

    @sp_endpoint(
        "/finances/transfers/wallet/2024-03-01/accounts/{accountId}", method="GET"
    )
    def get_account(self, *args, **kwargs) -> ApiResponse[BankAccount]:
        """
        Retrieve an Amazon Seller Wallet bank account by Amazon account identifier.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetAccountRequest):
            request = GetAccountRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=BankAccount
        )

    @overload
    def list_account_balances(
        self, request: ListAccountBalancesRequest, *args, **kwargs
    ) -> ApiResponse[BalanceListing]:
        """
        Retrieve the balance in a given Amazon Seller Wallet bank account.
        """
        ...

    @sp_endpoint(
        "/finances/transfers/wallet/2024-03-01/accounts/{accountId}/balance",
        method="GET",
    )
    def list_account_balances(self, *args, **kwargs) -> ApiResponse[BalanceListing]:
        """
        Retrieve the balance in a given Amazon Seller Wallet bank account.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, ListAccountBalancesRequest):
            request = ListAccountBalancesRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=BalanceListing
        )

    @overload
    def get_transfer_preview(
        self, request: GetTransferPreviewRequest, *args, **kwargs
    ) -> ApiResponse[TransferRatePreview]:
        """
        Retrieve a list of potential fees on a transaction.
        """
        ...

    @sp_endpoint("/finances/transfers/wallet/2024-03-01/transferPreview", method="GET")
    def get_transfer_preview(self, *args, **kwargs) -> ApiResponse[TransferRatePreview]:
        """
        Retrieve a list of potential fees on a transaction.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetTransferPreviewRequest):
            request = GetTransferPreviewRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=TransferRatePreview
        )

    @overload
    def list_account_transactions(
        self, request: ListAccountTransactionsRequest, *args, **kwargs
    ) -> ApiResponse[TransactionListing]:
        """
        Retrieve a list of transactions for a given Amazon Seller Wallet bank account.
        """
        ...

    @sp_endpoint("/finances/transfers/wallet/2024-03-01/transactions", method="GET")
    def list_account_transactions(
        self, *args, **kwargs
    ) -> ApiResponse[TransactionListing]:
        """
        Retrieve a list of transactions for a given Amazon Seller Wallet bank account.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, ListAccountTransactionsRequest):
            request = ListAccountTransactionsRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=TransactionListing
        )

    @overload
    def create_transaction(
        self, request: CreateTransactionRequest, *args, **kwargs
    ) -> ApiResponse[Transaction]:
        """
        Create a transaction request from an Amazon Seller Wallet account to another customer-provided account.
        """
        ...

    @sp_endpoint("/finances/transfers/wallet/2024-03-01/transactions", method="POST")
    def create_transaction(self, *args, **kwargs) -> ApiResponse[Transaction]:
        """
        Create a transaction request from an Amazon Seller Wallet account to another customer-provided account.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, CreateTransactionRequest):
            request = CreateTransactionRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=Transaction
        )

    @overload
    def get_transaction(
        self, request: GetTransactionRequest, *args, **kwargs
    ) -> ApiResponse[Transaction]:
        """
        Find a transaction by the Amazon transaction identifier.
        """
        ...

    @sp_endpoint(
        "/finances/transfers/wallet/2024-03-01/transactions/{transactionId}",
        method="GET",
    )
    def get_transaction(self, *args, **kwargs) -> ApiResponse[Transaction]:
        """
        Find a transaction by the Amazon transaction identifier.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetTransactionRequest):
            request = GetTransactionRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=Transaction
        )

    @overload
    def list_transfer_schedules(
        self, request: ListTransferSchedulesRequest, *args, **kwargs
    ) -> ApiResponse[TransferScheduleListing]:
        """
        Returns all transfer schedules of a given Amazon Seller Wallet bank account with the schedule ID in response if present.
        """
        ...

    @sp_endpoint(
        "/finances/transfers/wallet/2024-03-01/transferSchedules", method="GET"
    )
    def list_transfer_schedules(
        self, *args, **kwargs
    ) -> ApiResponse[TransferScheduleListing]:
        """
        Returns all transfer schedules of a given Amazon Seller Wallet bank account with the schedule ID in response if present.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, ListTransferSchedulesRequest):
            request = ListTransferSchedulesRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=TransferScheduleListing
        )

    @overload
    def create_transfer_schedule(
        self, request: CreateTransferScheduleRequest, *args, **kwargs
    ) -> ApiResponse[TransferSchedule]:
        """
        Create a transfer schedule request from an Amazon Seller Wallet account to another customer-provided account.
        """
        ...

    @sp_endpoint(
        "/finances/transfers/wallet/2024-03-01/transferSchedules", method="POST"
    )
    def create_transfer_schedule(
        self, *args, **kwargs
    ) -> ApiResponse[TransferSchedule]:
        """
        Create a transfer schedule request from an Amazon Seller Wallet account to another customer-provided account.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, CreateTransferScheduleRequest):
            request = CreateTransferScheduleRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=TransferSchedule
        )

    @overload
    def update_transfer_schedule(
        self, request: UpdateTransferScheduleRequest, *args, **kwargs
    ) -> ApiResponse[TransferSchedule]:
        """
        Update transfer schedule information. Returns a transfer belonging to the updated scheduled transfer request.
        """
        ...

    @sp_endpoint(
        "/finances/transfers/wallet/2024-03-01/transferSchedules", method="PUT"
    )
    def update_transfer_schedule(
        self, *args, **kwargs
    ) -> ApiResponse[TransferSchedule]:
        """
        Update transfer schedule information. Returns a transfer belonging to the updated scheduled transfer request.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, UpdateTransferScheduleRequest):
            request = UpdateTransferScheduleRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=TransferSchedule
        )

    @overload
    def get_transfer_schedule(
        self, request: GetTransferScheduleRequest, *args, **kwargs
    ) -> ApiResponse[TransferSchedule]:
        """
        Find a particular Amazon Seller Wallet account transfer schedule.
        """
        ...

    @sp_endpoint(
        "/finances/transfers/wallet/2024-03-01/transferSchedules/{transferScheduleId}",
        method="GET",
    )
    def get_transfer_schedule(self, *args, **kwargs) -> ApiResponse[TransferSchedule]:
        """
        Find a particular Amazon Seller Wallet account transfer schedule.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetTransferScheduleRequest):
            request = GetTransferScheduleRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=TransferSchedule
        )

    @overload
    def delete_schedule_transaction(
        self, request: DeleteScheduleTransactionRequest, *args, **kwargs
    ) -> ApiResponse[DeleteTransferSchedule]:
        """
        Delete a transaction request that is scheduled from Amazon Seller Wallet account to another customer-provided account.
        """
        ...

    @sp_endpoint(
        "/finances/transfers/wallet/2024-03-01/transferSchedules/{transferScheduleId}",
        method="DELETE",
    )
    def delete_schedule_transaction(
        self, *args, **kwargs
    ) -> ApiResponse[DeleteTransferSchedule]:
        """
        Delete a transaction request that is scheduled from Amazon Seller Wallet account to another customer-provided account.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, DeleteScheduleTransactionRequest):
            request = DeleteScheduleTransactionRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=DeleteTransferSchedule
        )
