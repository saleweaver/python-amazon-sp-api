from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class FinancesV20240601(Client):
    """
    Finances Transfers SP-API Client
    :link:

    The Selling Partner API for Transfers enables selling partners to retrieve payment methods and initiate payouts for their seller accounts. This API supports the following marketplaces: DE, FR, IT, ES, SE, NL, PL, and BE.
    """

    @sp_endpoint("/finances/transfers/2024-06-01/payouts", method="POST")
    def initiate_payout(self, **kwargs) -> ApiResponse:
        """
        initiate_payout(self, **kwargs) -> ApiResponse

        Initiates an on-demand payout to the seller's default deposit method in Seller Central for the given `marketplaceId` and `accountType`, if eligible. You can only initiate one on-demand payout for each marketplace and account type within a 24-hour period.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.017 | 2 |

        The `x-amzn-RateLimit-Limit` response header contains the usage plan rate limits for the operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput might have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            body: | * REQUIRED The request body for the `initiatePayout` operation.

        Returns:
            ApiResponse:
        """
        return self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)

    @sp_endpoint("/finances/transfers/2024-06-01/paymentMethods", method="GET")
    def get_payment_methods(self, **kwargs) -> ApiResponse:
        """
        get_payment_methods(self, **kwargs) -> ApiResponse

        Returns the list of payment methods for the seller, which can be filtered by method type.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | .5 | 30 |

        The `x-amzn-RateLimit-Limit` response header contains the usage plan rate limits for the operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput might have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            key marketplaceId:string | * REQUIRED The identifier of the marketplace from which you want to retrieve payment methods. For the list of possible marketplace identifiers, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
            key paymentMethodTypes:string | A comma-separated list of the payment method types you want to include in the response.

        Returns:
            ApiResponse:
        """
        return self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)
