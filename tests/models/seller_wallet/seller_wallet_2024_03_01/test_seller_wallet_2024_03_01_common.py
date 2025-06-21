# Auto-generated tests for sp_api.api.models.seller_wallet.seller_wallet_2024_03_01.common.py
from datetime import datetime

import pytest
from sp_api.api.models.seller_wallet.seller_wallet_2024_03_01.common import (
    AccountHolderAddress, Balance, BalanceListing, BankAccount,
    BankAccountListing, CreateTransactionRequest,
    CreateTransferScheduleRequest, Currency, DeleteScheduleTransactionRequest,
    DeleteTransferSchedule, Error, ErrorList, Fee, FxRateDetails,
    GetAccountRequest, GetRequestSerializer, GetTransactionRequest,
    GetTransferPreviewRequest, GetTransferScheduleRequest,
    ListAccountBalancesRequest, ListAccountsRequest,
    ListAccountTransactionsRequest, ListTransferSchedulesRequest,
    PaymentPreference, RequestsBaseModel, ScheduleExpression, SpApiBaseModel,
    Transaction, TransactionAccount, TransactionInitiationRequestBody,
    TransactionInstrumentDetails, TransactionListing, TransferRatePreview,
    TransferSchedule, TransferScheduleFailures, TransferScheduleInformation,
    TransferScheduleListing, TransferScheduleRequestBody,
    UpdateTransferScheduleRequest)


def test_requestsbasemodel_instantiates():
    """Instantiate RequestsBaseModel with dummy data"""
    kwargs = {}
    obj = RequestsBaseModel(**kwargs)
    assert isinstance(obj, RequestsBaseModel)


def test_spapibasemodel_instantiates():
    """Instantiate SpApiBaseModel with dummy data"""
    kwargs = {}
    obj = SpApiBaseModel(**kwargs)
    assert isinstance(obj, SpApiBaseModel)


def test_getrequestserializer_instantiates():
    """Instantiate GetRequestSerializer with dummy data"""
    kwargs = {}
    obj = GetRequestSerializer(**kwargs)
    assert isinstance(obj, GetRequestSerializer)


def test_accountholderaddress_instantiates():
    """Instantiate AccountHolderAddress with dummy data"""
    kwargs = {
        "address_line1": "",
        "address_line2": None,
        "city": "",
        "state": "",
        "postal_code": "",
        "country": None,
        "country_code": "",
    }
    obj = AccountHolderAddress(**kwargs)
    assert isinstance(obj, AccountHolderAddress)


def test_balance_instantiates():
    """Instantiate Balance with dummy data"""
    kwargs = {
        "account_id": "",
        "balance_type": None,
        "balance_amount": 0.0,
        "balance_currency": "",
        "last_update_date": datetime(2000, 1, 1),
    }
    obj = Balance(**kwargs)
    assert isinstance(obj, Balance)


def test_balancelisting_instantiates():
    """Instantiate BalanceListing with dummy data"""
    kwargs = {
        "balances": None,
    }
    obj = BalanceListing(**kwargs)
    assert isinstance(obj, BalanceListing)


def test_bankaccount_instantiates():
    """Instantiate BankAccount with dummy data"""
    kwargs = {
        "account_id": None,
        "account_holder_name": "",
        "bank_account_number_format": "",
        "bank_name": None,
        "bank_account_ownership_type": "",
        "routing_number": "",
        "bank_number_format": "",
        "account_country_code": "",
        "account_currency": "",
        "bank_account_number_tail": "",
        "bank_account_holder_status": None,
    }
    obj = BankAccount(**kwargs)
    assert isinstance(obj, BankAccount)


def test_bankaccountlisting_instantiates():
    """Instantiate BankAccountListing with dummy data"""
    kwargs = {
        "accounts": [],
    }
    obj = BankAccountListing(**kwargs)
    assert isinstance(obj, BankAccountListing)


def test_currency_instantiates():
    """Instantiate Currency with dummy data"""
    kwargs = {
        "currency_code": None,
        "currency_amount": None,
    }
    obj = Currency(**kwargs)
    assert isinstance(obj, Currency)


def test_transactioninstrumentdetails_instantiates():
    """Instantiate TransactionInstrumentDetails with dummy data"""
    kwargs = {
        "bank_account": BankAccount(
            **{
                "account_id": None,
                "account_holder_name": "",
                "bank_account_number_format": "",
                "bank_name": None,
                "bank_account_ownership_type": "",
                "routing_number": "",
                "bank_number_format": "",
                "account_country_code": "",
                "account_currency": "",
                "bank_account_number_tail": "",
                "bank_account_holder_status": None,
            }
        ),
        "bank_account_number": "",
    }
    obj = TransactionInstrumentDetails(**kwargs)
    assert isinstance(obj, TransactionInstrumentDetails)


def test_fee_instantiates():
    """Instantiate Fee with dummy data"""
    kwargs = {
        "fee_id": "",
        "fee_type": "",
        "fee_rate_value": 0.0,
        "fee_amount": Currency(**{"currency_code": None, "currency_amount": None}),
    }
    obj = Fee(**kwargs)
    assert isinstance(obj, Fee)


def test_fxratedetails_instantiates():
    """Instantiate FxRateDetails with dummy data"""
    kwargs = {
        "fx_rate_id": "",
        "base_rate": 0.0,
        "effective_fx_rate": 0.0,
        "rate_direction": "",
    }
    obj = FxRateDetails(**kwargs)
    assert isinstance(obj, FxRateDetails)


def test_transferratepreview_instantiates():
    """Instantiate TransferRatePreview with dummy data"""
    kwargs = {
        "base_amount": Currency(**{"currency_code": None, "currency_amount": None}),
        "fx_rate_details": FxRateDetails(
            **{
                "fx_rate_id": "",
                "base_rate": 0.0,
                "effective_fx_rate": 0.0,
                "rate_direction": "",
            }
        ),
        "transfer_amount": Currency(**{"currency_code": None, "currency_amount": None}),
        "fees": [],
    }
    obj = TransferRatePreview(**kwargs)
    assert isinstance(obj, TransferRatePreview)


def test_transactioninitiationrequestbody_instantiates():
    """Instantiate TransactionInitiationRequestBody with dummy data"""
    kwargs = {
        "source_account_id": "",
        "destination_account_id": None,
        "description": "",
        "destination_transaction_instrument": TransactionInstrumentDetails(
            **{
                "bank_account": BankAccount(
                    **{
                        "account_id": None,
                        "account_holder_name": "",
                        "bank_account_number_format": "",
                        "bank_name": None,
                        "bank_account_ownership_type": "",
                        "routing_number": "",
                        "bank_number_format": "",
                        "account_country_code": "",
                        "account_currency": "",
                        "bank_account_number_tail": "",
                        "bank_account_holder_status": None,
                    }
                ),
                "bank_account_number": "",
            }
        ),
        "destination_account_holder_address": None,
        "source_amount": Currency(**{"currency_code": None, "currency_amount": None}),
        "transfer_rate_details": None,
        "request_time": datetime(2000, 1, 1),
    }
    obj = TransactionInitiationRequestBody(**kwargs)
    assert isinstance(obj, TransactionInitiationRequestBody)


def test_createtransactionrequest_instantiates():
    """Instantiate CreateTransactionRequest with dummy data"""
    kwargs = {
        "body": TransactionInitiationRequestBody(
            **{
                "source_account_id": "",
                "destination_account_id": None,
                "description": "",
                "destination_transaction_instrument": TransactionInstrumentDetails(
                    **{
                        "bank_account": BankAccount(
                            **{
                                "account_id": None,
                                "account_holder_name": "",
                                "bank_account_number_format": "",
                                "bank_name": None,
                                "bank_account_ownership_type": "",
                                "routing_number": "",
                                "bank_number_format": "",
                                "account_country_code": "",
                                "account_currency": "",
                                "bank_account_number_tail": "",
                                "bank_account_holder_status": None,
                            }
                        ),
                        "bank_account_number": "",
                    }
                ),
                "destination_account_holder_address": None,
                "source_amount": Currency(
                    **{"currency_code": None, "currency_amount": None}
                ),
                "transfer_rate_details": None,
                "request_time": datetime(2000, 1, 1),
            }
        ),
    }
    obj = CreateTransactionRequest(**kwargs)
    assert isinstance(obj, CreateTransactionRequest)


def test_paymentpreference_instantiates():
    """Instantiate PaymentPreference with dummy data"""
    kwargs = {
        "payment_preference_payment_type": "",
        "value": 0.0,
    }
    obj = PaymentPreference(**kwargs)
    assert isinstance(obj, PaymentPreference)


def test_scheduleexpression_instantiates():
    """Instantiate ScheduleExpression with dummy data"""
    kwargs = {
        "schedule_expression_type": "",
        "recurring_frequency": None,
    }
    obj = ScheduleExpression(**kwargs)
    assert isinstance(obj, ScheduleExpression)


def test_transferscheduleinformation_instantiates():
    """Instantiate TransferScheduleInformation with dummy data"""
    kwargs = {
        "schedule_start_date": None,
        "schedule_end_date": None,
        "schedule_expression": None,
        "schedule_type": None,
    }
    obj = TransferScheduleInformation(**kwargs)
    assert isinstance(obj, TransferScheduleInformation)


def test_transferschedulerequestbody_instantiates():
    """Instantiate TransferScheduleRequestBody with dummy data"""
    kwargs = {
        "source_account_id": "",
        "source_currency_code": "",
        "destination_account_id": "",
        "destination_transaction_instrument": TransactionInstrumentDetails(
            **{
                "bank_account": BankAccount(
                    **{
                        "account_id": None,
                        "account_holder_name": "",
                        "bank_account_number_format": "",
                        "bank_name": None,
                        "bank_account_ownership_type": "",
                        "routing_number": "",
                        "bank_number_format": "",
                        "account_country_code": "",
                        "account_currency": "",
                        "bank_account_number_tail": "",
                        "bank_account_holder_status": None,
                    }
                ),
                "bank_account_number": "",
            }
        ),
        "transaction_type": "",
        "transfer_schedule_information": TransferScheduleInformation(
            **{
                "schedule_start_date": None,
                "schedule_end_date": None,
                "schedule_expression": None,
                "schedule_type": None,
            }
        ),
        "payment_preference": PaymentPreference(
            **{"payment_preference_payment_type": "", "value": 0.0}
        ),
        "transfer_schedule_status": None,
    }
    obj = TransferScheduleRequestBody(**kwargs)
    assert isinstance(obj, TransferScheduleRequestBody)


def test_createtransferschedulerequest_instantiates():
    """Instantiate CreateTransferScheduleRequest with dummy data"""
    kwargs = {
        "body": TransferScheduleRequestBody(
            **{
                "source_account_id": "",
                "source_currency_code": "",
                "destination_account_id": "",
                "destination_transaction_instrument": TransactionInstrumentDetails(
                    **{
                        "bank_account": BankAccount(
                            **{
                                "account_id": None,
                                "account_holder_name": "",
                                "bank_account_number_format": "",
                                "bank_name": None,
                                "bank_account_ownership_type": "",
                                "routing_number": "",
                                "bank_number_format": "",
                                "account_country_code": "",
                                "account_currency": "",
                                "bank_account_number_tail": "",
                                "bank_account_holder_status": None,
                            }
                        ),
                        "bank_account_number": "",
                    }
                ),
                "transaction_type": "",
                "transfer_schedule_information": TransferScheduleInformation(
                    **{
                        "schedule_start_date": None,
                        "schedule_end_date": None,
                        "schedule_expression": None,
                        "schedule_type": None,
                    }
                ),
                "payment_preference": PaymentPreference(
                    **{"payment_preference_payment_type": "", "value": 0.0}
                ),
                "transfer_schedule_status": None,
            }
        ),
    }
    obj = CreateTransferScheduleRequest(**kwargs)
    assert isinstance(obj, CreateTransferScheduleRequest)


def test_deletescheduletransactionrequest_instantiates():
    """Instantiate DeleteScheduleTransactionRequest with dummy data"""
    kwargs = {
        "transfer_schedule_id": "",
    }
    obj = DeleteScheduleTransactionRequest(**kwargs)
    assert isinstance(obj, DeleteScheduleTransactionRequest)


def test_deletetransferschedule_instantiates():
    """Instantiate DeleteTransferSchedule with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = DeleteTransferSchedule(**kwargs)
    assert isinstance(obj, DeleteTransferSchedule)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_errorlist_instantiates():
    """Instantiate ErrorList with dummy data"""
    kwargs = {
        "errors": [],
    }
    obj = ErrorList(**kwargs)
    assert isinstance(obj, ErrorList)


def test_getaccountrequest_instantiates():
    """Instantiate GetAccountRequest with dummy data"""
    kwargs = {
        "account_id": "",
    }
    obj = GetAccountRequest(**kwargs)
    assert isinstance(obj, GetAccountRequest)


def test_gettransactionrequest_instantiates():
    """Instantiate GetTransactionRequest with dummy data"""
    kwargs = {
        "transaction_id": "",
    }
    obj = GetTransactionRequest(**kwargs)
    assert isinstance(obj, GetTransactionRequest)


def test_gettransferpreviewrequest_instantiates():
    """Instantiate GetTransferPreviewRequest with dummy data"""
    kwargs = {
        "source_country_code": "",
        "source_currency_code": "",
        "destination_country_code": "",
        "destination_currency_code": "",
        "base_amount": 0.0,
    }
    obj = GetTransferPreviewRequest(**kwargs)
    assert isinstance(obj, GetTransferPreviewRequest)


def test_gettransferschedulerequest_instantiates():
    """Instantiate GetTransferScheduleRequest with dummy data"""
    kwargs = {
        "transfer_schedule_id": "",
    }
    obj = GetTransferScheduleRequest(**kwargs)
    assert isinstance(obj, GetTransferScheduleRequest)


def test_listaccountbalancesrequest_instantiates():
    """Instantiate ListAccountBalancesRequest with dummy data"""
    kwargs = {
        "account_id": "",
    }
    obj = ListAccountBalancesRequest(**kwargs)
    assert isinstance(obj, ListAccountBalancesRequest)


def test_listaccounttransactionsrequest_instantiates():
    """Instantiate ListAccountTransactionsRequest with dummy data"""
    kwargs = {
        "account_id": "",
        "next_page_token": None,
    }
    obj = ListAccountTransactionsRequest(**kwargs)
    assert isinstance(obj, ListAccountTransactionsRequest)


def test_listaccountsrequest_instantiates():
    """Instantiate ListAccountsRequest with dummy data"""
    kwargs = {
        "marketplace_id": None,
    }
    obj = ListAccountsRequest(**kwargs)
    assert isinstance(obj, ListAccountsRequest)


def test_listtransferschedulesrequest_instantiates():
    """Instantiate ListTransferSchedulesRequest with dummy data"""
    kwargs = {
        "account_id": "",
        "next_page_token": None,
    }
    obj = ListTransferSchedulesRequest(**kwargs)
    assert isinstance(obj, ListTransferSchedulesRequest)


def test_transactionaccount_instantiates():
    """Instantiate TransactionAccount with dummy data"""
    kwargs = {
        "account_id": None,
        "bank_account_holder_name": "",
        "bank_name": "",
        "bank_account_number_format": "",
        "bank_account_number_tail": None,
        "bank_account_country_code": None,
        "bank_account_currency": "",
    }
    obj = TransactionAccount(**kwargs)
    assert isinstance(obj, TransactionAccount)


def test_transaction_instantiates():
    """Instantiate Transaction with dummy data"""
    kwargs = {
        "transaction_id": "",
        "transaction_type": "",
        "transaction_status": "",
        "transaction_request_date": datetime(2000, 1, 1),
        "expected_completion_date": None,
        "transaction_actual_completion_date": None,
        "last_update_date": datetime(2000, 1, 1),
        "requester_name": None,
        "transaction_requester_source": "",
        "transaction_description": "",
        "transaction_source_account": TransactionAccount(
            **{
                "account_id": None,
                "bank_account_holder_name": "",
                "bank_name": "",
                "bank_account_number_format": "",
                "bank_account_number_tail": None,
                "bank_account_country_code": None,
                "bank_account_currency": "",
            }
        ),
        "transaction_destination_account": TransactionAccount(
            **{
                "account_id": None,
                "bank_account_holder_name": "",
                "bank_name": "",
                "bank_account_number_format": "",
                "bank_account_number_tail": None,
                "bank_account_country_code": None,
                "bank_account_currency": "",
            }
        ),
        "transaction_request_amount": Currency(
            **{"currency_code": None, "currency_amount": None}
        ),
        "transfer_rate_details": TransferRatePreview(
            **{
                "base_amount": Currency(
                    **{"currency_code": None, "currency_amount": None}
                ),
                "fx_rate_details": FxRateDetails(
                    **{
                        "fx_rate_id": "",
                        "base_rate": 0.0,
                        "effective_fx_rate": 0.0,
                        "rate_direction": "",
                    }
                ),
                "transfer_amount": Currency(
                    **{"currency_code": None, "currency_amount": None}
                ),
                "fees": [],
            }
        ),
        "transaction_final_amount": None,
        "transaction_failure_reason": None,
    }
    obj = Transaction(**kwargs)
    assert isinstance(obj, Transaction)


def test_transactionlisting_instantiates():
    """Instantiate TransactionListing with dummy data"""
    kwargs = {
        "next_page_token": None,
        "transactions": [],
    }
    obj = TransactionListing(**kwargs)
    assert isinstance(obj, TransactionListing)


def test_transferschedulefailures_instantiates():
    """Instantiate TransferScheduleFailures with dummy data"""
    kwargs = {
        "transfer_schedule_failure_date": datetime(2000, 1, 1),
        "transfer_schedule_failure_reason": "",
    }
    obj = TransferScheduleFailures(**kwargs)
    assert isinstance(obj, TransferScheduleFailures)


def test_transferschedule_instantiates():
    """Instantiate TransferSchedule with dummy data"""
    kwargs = {
        "transfer_schedule_id": "",
        "transaction_type": "",
        "transaction_source_account": None,
        "transaction_destination_account": TransactionAccount(
            **{
                "account_id": None,
                "bank_account_holder_name": "",
                "bank_name": "",
                "bank_account_number_format": "",
                "bank_account_number_tail": None,
                "bank_account_country_code": None,
                "bank_account_currency": "",
            }
        ),
        "transfer_schedule_status": "",
        "transfer_schedule_information": TransferScheduleInformation(
            **{
                "schedule_start_date": None,
                "schedule_end_date": None,
                "schedule_expression": None,
                "schedule_type": None,
            }
        ),
        "payment_preference": None,
        "transfer_schedule_failures": [],
    }
    obj = TransferSchedule(**kwargs)
    assert isinstance(obj, TransferSchedule)


def test_transferschedulelisting_instantiates():
    """Instantiate TransferScheduleListing with dummy data"""
    kwargs = {
        "next_page_token": None,
        "transfer_schedules": [],
    }
    obj = TransferScheduleListing(**kwargs)
    assert isinstance(obj, TransferScheduleListing)


def test_updatetransferschedulerequest_instantiates():
    """Instantiate UpdateTransferScheduleRequest with dummy data"""
    kwargs = {
        "body": TransferSchedule(
            **{
                "transfer_schedule_id": "",
                "transaction_type": "",
                "transaction_source_account": None,
                "transaction_destination_account": TransactionAccount(
                    **{
                        "account_id": None,
                        "bank_account_holder_name": "",
                        "bank_name": "",
                        "bank_account_number_format": "",
                        "bank_account_number_tail": None,
                        "bank_account_country_code": None,
                        "bank_account_currency": "",
                    }
                ),
                "transfer_schedule_status": "",
                "transfer_schedule_information": TransferScheduleInformation(
                    **{
                        "schedule_start_date": None,
                        "schedule_end_date": None,
                        "schedule_expression": None,
                        "schedule_type": None,
                    }
                ),
                "payment_preference": None,
                "transfer_schedule_failures": [],
            }
        ),
    }
    obj = UpdateTransferScheduleRequest(**kwargs)
    assert isinstance(obj, UpdateTransferScheduleRequest)
