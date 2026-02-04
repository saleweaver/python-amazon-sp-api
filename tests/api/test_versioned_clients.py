from __future__ import annotations

from dataclasses import dataclass

import pytest

from sp_api.base import Marketplaces


TEST_CREDENTIALS = {
    "refresh_token": "test_refresh_token",
    "lwa_app_id": "test_lwa_app_id",
    "lwa_client_secret": "test_lwa_client_secret",
}


@dataclass(frozen=True)
class VersionCase:
    front: type
    default_cls: type
    latest_cls: type
    default_value: str
    latest_value: str
    default_enum: object
    latest_enum: object


def _make_client(cls: type, **kwargs):
    return cls(
        marketplace=Marketplaces.US,
        credentials=TEST_CREDENTIALS,
        refresh_token=TEST_CREDENTIALS["refresh_token"],
        **kwargs,
    )


def _assert_dispatch(case: VersionCase):
    client = _make_client(case.front)
    assert isinstance(client, case.default_cls)

    client = _make_client(case.front, version=case.default_value)
    assert isinstance(client, case.default_cls)

    client = _make_client(case.front, version=case.latest_value)
    assert isinstance(client, case.latest_cls)

    client = _make_client(case.front, version=case.latest_enum)
    assert isinstance(client, case.latest_cls)

    client = _make_client(case.front, version=case.default_enum)
    assert isinstance(client, case.default_cls)

    with pytest.raises(ValueError):
        _make_client(case.front, version="unsupported-version")


# Sync cases
from sp_api.api import (  # noqa: E402
    AmazonWarehousingAndDistribution,
    AmazonWarehousingAndDistributionVersion,
    AmazonWarehousingAndDistributionV20240509,
    CatalogItems,
    CatalogItemsVersion,
    CatalogItemsV20201201,
    CatalogItemsV20220401,
    ExternalFulfillmentInventory,
    ExternalFulfillmentInventoryVersion,
    ExternalFulfillmentInventoryV20210106,
    ExternalFulfillmentInventoryV20240911,
    ExternalFulfillmentReturns,
    ExternalFulfillmentReturnsVersion,
    ExternalFulfillmentReturnsV20210819,
    ExternalFulfillmentReturnsV20240911,
    ExternalFulfillmentShipping,
    ExternalFulfillmentShippingVersion,
    ExternalFulfillmentShippingV20210106,
    ExternalFulfillmentShippingV20240911,
    Feeds,
    FeedsVersion,
    FeedsV20210630,
    Finances,
    FinancesVersion,
    FinancesV0,
    FinancesV20240619,
    FulfillmentInbound,
    FulfillmentInboundVersion,
    FulfillmentInboundV0,
    FulfillmentInboundV20240320,
    ListingsItems,
    ListingsItemsVersion,
    ListingsItemsV20200901,
    ListingsItemsV20210801,
    Orders,
    OrdersVersion,
    OrdersV0,
    OrdersV20260101,
    Products,
    ProductsVersion,
    ProductsV0,
    ProductsV20220501,
    Shipping,
    ShippingVersion,
    ShippingV1,
    ShippingV2,
    VendorDirectFulfillmentOrders,
    VendorDirectFulfillmentOrdersVersion,
    VendorDirectFulfillmentOrdersV1,
    VendorDirectFulfillmentOrdersV20211228,
    VendorDirectFulfillmentShipping,
    VendorDirectFulfillmentShippingVersion,
    VendorDirectFulfillmentShippingV1,
    VendorDirectFulfillmentShippingV20211228,
    VendorDirectFulfillmentTransactions,
    VendorDirectFulfillmentTransactionsVersion,
    VendorDirectFulfillmentTransactionsV1,
    VendorDirectFulfillmentTransactionsV20211228,
)


SYNC_CASES = [
    VersionCase(
        front=Orders,
        default_cls=OrdersV0,
        latest_cls=OrdersV20260101,
        default_value="v0",
        latest_value="2026-01-01",
        default_enum=OrdersVersion("v0"),
        latest_enum=OrdersVersion.LATEST,
    ),
    VersionCase(
        front=Feeds,
        default_cls=FeedsV20210630,
        latest_cls=FeedsV20210630,
        default_value="2021-06-30",
        latest_value="2021-06-30",
        default_enum=FeedsVersion("2021-06-30"),
        latest_enum=FeedsVersion.LATEST,
    ),
    VersionCase(
        front=ListingsItems,
        default_cls=ListingsItemsV20200901,
        latest_cls=ListingsItemsV20210801,
        default_value="2020-09-01",
        latest_value="2021-08-01",
        default_enum=ListingsItemsVersion("2020-09-01"),
        latest_enum=ListingsItemsVersion.LATEST,
    ),
    VersionCase(
        front=Products,
        default_cls=ProductsV0,
        latest_cls=ProductsV20220501,
        default_value="v0",
        latest_value="2022-05-01",
        default_enum=ProductsVersion("v0"),
        latest_enum=ProductsVersion.LATEST,
    ),
    VersionCase(
        front=Shipping,
        default_cls=ShippingV1,
        latest_cls=ShippingV2,
        default_value="v1",
        latest_value="v2",
        default_enum=ShippingVersion("v1"),
        latest_enum=ShippingVersion.LATEST,
    ),
    VersionCase(
        front=VendorDirectFulfillmentOrders,
        default_cls=VendorDirectFulfillmentOrdersV1,
        latest_cls=VendorDirectFulfillmentOrdersV20211228,
        default_value="v1",
        latest_value="2021-12-28",
        default_enum=VendorDirectFulfillmentOrdersVersion("v1"),
        latest_enum=VendorDirectFulfillmentOrdersVersion.LATEST,
    ),
    VersionCase(
        front=VendorDirectFulfillmentShipping,
        default_cls=VendorDirectFulfillmentShippingV1,
        latest_cls=VendorDirectFulfillmentShippingV20211228,
        default_value="v1",
        latest_value="2021-12-28",
        default_enum=VendorDirectFulfillmentShippingVersion("v1"),
        latest_enum=VendorDirectFulfillmentShippingVersion.LATEST,
    ),
    VersionCase(
        front=VendorDirectFulfillmentTransactions,
        default_cls=VendorDirectFulfillmentTransactionsV1,
        latest_cls=VendorDirectFulfillmentTransactionsV20211228,
        default_value="v1",
        latest_value="2021-12-28",
        default_enum=VendorDirectFulfillmentTransactionsVersion("v1"),
        latest_enum=VendorDirectFulfillmentTransactionsVersion.LATEST,
    ),
    VersionCase(
        front=ExternalFulfillmentInventory,
        default_cls=ExternalFulfillmentInventoryV20210106,
        latest_cls=ExternalFulfillmentInventoryV20240911,
        default_value="2021-01-06",
        latest_value="2024-09-11",
        default_enum=ExternalFulfillmentInventoryVersion("2021-01-06"),
        latest_enum=ExternalFulfillmentInventoryVersion.LATEST,
    ),
    VersionCase(
        front=ExternalFulfillmentReturns,
        default_cls=ExternalFulfillmentReturnsV20210819,
        latest_cls=ExternalFulfillmentReturnsV20240911,
        default_value="2021-08-19",
        latest_value="2024-09-11",
        default_enum=ExternalFulfillmentReturnsVersion("2021-08-19"),
        latest_enum=ExternalFulfillmentReturnsVersion.LATEST,
    ),
    VersionCase(
        front=ExternalFulfillmentShipping,
        default_cls=ExternalFulfillmentShippingV20210106,
        latest_cls=ExternalFulfillmentShippingV20240911,
        default_value="2021-01-06",
        latest_value="2024-09-11",
        default_enum=ExternalFulfillmentShippingVersion("2021-01-06"),
        latest_enum=ExternalFulfillmentShippingVersion.LATEST,
    ),
    VersionCase(
        front=CatalogItems,
        default_cls=CatalogItemsV20201201,
        latest_cls=CatalogItemsV20220401,
        default_value="2020-12-01",
        latest_value="2022-04-01",
        default_enum=CatalogItemsVersion("2020-12-01"),
        latest_enum=CatalogItemsVersion.LATEST,
    ),
    VersionCase(
        front=Finances,
        default_cls=FinancesV0,
        latest_cls=FinancesV20240619,
        default_value="v0",
        latest_value="2024-06-19",
        default_enum=FinancesVersion("v0"),
        latest_enum=FinancesVersion.LATEST,
    ),
    VersionCase(
        front=FulfillmentInbound,
        default_cls=FulfillmentInboundV0,
        latest_cls=FulfillmentInboundV20240320,
        default_value="v0",
        latest_value="2024-03-20",
        default_enum=FulfillmentInboundVersion("v0"),
        latest_enum=FulfillmentInboundVersion.LATEST,
    ),
    VersionCase(
        front=AmazonWarehousingAndDistribution,
        default_cls=AmazonWarehousingAndDistributionV20240509,
        latest_cls=AmazonWarehousingAndDistributionV20240509,
        default_value="2024-05-09",
        latest_value="2024-05-09",
        default_enum=AmazonWarehousingAndDistributionVersion("2024-05-09"),
        latest_enum=AmazonWarehousingAndDistributionVersion.LATEST,
    ),
]


@pytest.mark.parametrize("case", SYNC_CASES, ids=[c.front.__name__ for c in SYNC_CASES])
def test_sync_versioned_dispatch(case: VersionCase):
    _assert_dispatch(case)


# Async cases
from sp_api.asyncio.api import (  # noqa: E402
    AmazonWarehousingAndDistribution as AsyncAmazonWarehousingAndDistribution,
    AmazonWarehousingAndDistributionVersion as AsyncAmazonWarehousingAndDistributionVersion,
    AmazonWarehousingAndDistributionV20240509 as AsyncAmazonWarehousingAndDistributionV20240509,
    CatalogItems as AsyncCatalogItems,
    CatalogItemsVersion as AsyncCatalogItemsVersion,
    CatalogItemsV20201201 as AsyncCatalogItemsV20201201,
    CatalogItemsV20220401 as AsyncCatalogItemsV20220401,
    ExternalFulfillmentInventory as AsyncExternalFulfillmentInventory,
    ExternalFulfillmentInventoryVersion as AsyncExternalFulfillmentInventoryVersion,
    ExternalFulfillmentInventoryV20210106 as AsyncExternalFulfillmentInventoryV20210106,
    ExternalFulfillmentInventoryV20240911 as AsyncExternalFulfillmentInventoryV20240911,
    ExternalFulfillmentReturns as AsyncExternalFulfillmentReturns,
    ExternalFulfillmentReturnsVersion as AsyncExternalFulfillmentReturnsVersion,
    ExternalFulfillmentReturnsV20210819 as AsyncExternalFulfillmentReturnsV20210819,
    ExternalFulfillmentReturnsV20240911 as AsyncExternalFulfillmentReturnsV20240911,
    ExternalFulfillmentShipping as AsyncExternalFulfillmentShipping,
    ExternalFulfillmentShippingVersion as AsyncExternalFulfillmentShippingVersion,
    ExternalFulfillmentShippingV20210106 as AsyncExternalFulfillmentShippingV20210106,
    ExternalFulfillmentShippingV20240911 as AsyncExternalFulfillmentShippingV20240911,
    Feeds as AsyncFeeds,
    FeedsVersion as AsyncFeedsVersion,
    FeedsV20210630 as AsyncFeedsV20210630,
    Finances as AsyncFinances,
    FinancesVersion as AsyncFinancesVersion,
    FinancesV0 as AsyncFinancesV0,
    FinancesV20240619 as AsyncFinancesV20240619,
    FulfillmentInbound as AsyncFulfillmentInbound,
    FulfillmentInboundVersion as AsyncFulfillmentInboundVersion,
    FulfillmentInboundV0 as AsyncFulfillmentInboundV0,
    FulfillmentInboundV20240320 as AsyncFulfillmentInboundV20240320,
    ListingsItems as AsyncListingsItems,
    ListingsItemsVersion as AsyncListingsItemsVersion,
    ListingsItemsV20200901 as AsyncListingsItemsV20200901,
    ListingsItemsV20210801 as AsyncListingsItemsV20210801,
    Orders as AsyncOrders,
    OrdersVersion as AsyncOrdersVersion,
    OrdersV0 as AsyncOrdersV0,
    OrdersV20260101 as AsyncOrdersV20260101,
    Products as AsyncProducts,
    ProductsVersion as AsyncProductsVersion,
    ProductsV0 as AsyncProductsV0,
    ProductsV20220501 as AsyncProductsV20220501,
    Shipping as AsyncShipping,
    ShippingVersion as AsyncShippingVersion,
    ShippingV1 as AsyncShippingV1,
    ShippingV2 as AsyncShippingV2,
    VendorDirectFulfillmentOrders as AsyncVendorDirectFulfillmentOrders,
    VendorDirectFulfillmentOrdersVersion as AsyncVendorDirectFulfillmentOrdersVersion,
    VendorDirectFulfillmentOrdersV1 as AsyncVendorDirectFulfillmentOrdersV1,
    VendorDirectFulfillmentOrdersV20211228 as AsyncVendorDirectFulfillmentOrdersV20211228,
    VendorDirectFulfillmentShipping as AsyncVendorDirectFulfillmentShipping,
    VendorDirectFulfillmentShippingVersion as AsyncVendorDirectFulfillmentShippingVersion,
    VendorDirectFulfillmentShippingV1 as AsyncVendorDirectFulfillmentShippingV1,
    VendorDirectFulfillmentShippingV20211228 as AsyncVendorDirectFulfillmentShippingV20211228,
    VendorDirectFulfillmentTransactions as AsyncVendorDirectFulfillmentTransactions,
    VendorDirectFulfillmentTransactionsVersion as AsyncVendorDirectFulfillmentTransactionsVersion,
    VendorDirectFulfillmentTransactionsV1 as AsyncVendorDirectFulfillmentTransactionsV1,
    VendorDirectFulfillmentTransactionsV20211228 as AsyncVendorDirectFulfillmentTransactionsV20211228,
)


ASYNC_CASES = [
    VersionCase(
        front=AsyncOrders,
        default_cls=AsyncOrdersV0,
        latest_cls=AsyncOrdersV20260101,
        default_value="v0",
        latest_value="2026-01-01",
        default_enum=AsyncOrdersVersion("v0"),
        latest_enum=AsyncOrdersVersion.LATEST,
    ),
    VersionCase(
        front=AsyncFeeds,
        default_cls=AsyncFeedsV20210630,
        latest_cls=AsyncFeedsV20210630,
        default_value="2021-06-30",
        latest_value="2021-06-30",
        default_enum=AsyncFeedsVersion("2021-06-30"),
        latest_enum=AsyncFeedsVersion.LATEST,
    ),
    VersionCase(
        front=AsyncListingsItems,
        default_cls=AsyncListingsItemsV20200901,
        latest_cls=AsyncListingsItemsV20210801,
        default_value="2020-09-01",
        latest_value="2021-08-01",
        default_enum=AsyncListingsItemsVersion("2020-09-01"),
        latest_enum=AsyncListingsItemsVersion.LATEST,
    ),
    VersionCase(
        front=AsyncProducts,
        default_cls=AsyncProductsV0,
        latest_cls=AsyncProductsV20220501,
        default_value="v0",
        latest_value="2022-05-01",
        default_enum=AsyncProductsVersion("v0"),
        latest_enum=AsyncProductsVersion.LATEST,
    ),
    VersionCase(
        front=AsyncShipping,
        default_cls=AsyncShippingV1,
        latest_cls=AsyncShippingV2,
        default_value="v1",
        latest_value="v2",
        default_enum=AsyncShippingVersion("v1"),
        latest_enum=AsyncShippingVersion.LATEST,
    ),
    VersionCase(
        front=AsyncVendorDirectFulfillmentOrders,
        default_cls=AsyncVendorDirectFulfillmentOrdersV1,
        latest_cls=AsyncVendorDirectFulfillmentOrdersV20211228,
        default_value="v1",
        latest_value="2021-12-28",
        default_enum=AsyncVendorDirectFulfillmentOrdersVersion("v1"),
        latest_enum=AsyncVendorDirectFulfillmentOrdersVersion.LATEST,
    ),
    VersionCase(
        front=AsyncVendorDirectFulfillmentShipping,
        default_cls=AsyncVendorDirectFulfillmentShippingV1,
        latest_cls=AsyncVendorDirectFulfillmentShippingV20211228,
        default_value="v1",
        latest_value="2021-12-28",
        default_enum=AsyncVendorDirectFulfillmentShippingVersion("v1"),
        latest_enum=AsyncVendorDirectFulfillmentShippingVersion.LATEST,
    ),
    VersionCase(
        front=AsyncVendorDirectFulfillmentTransactions,
        default_cls=AsyncVendorDirectFulfillmentTransactionsV1,
        latest_cls=AsyncVendorDirectFulfillmentTransactionsV20211228,
        default_value="v1",
        latest_value="2021-12-28",
        default_enum=AsyncVendorDirectFulfillmentTransactionsVersion("v1"),
        latest_enum=AsyncVendorDirectFulfillmentTransactionsVersion.LATEST,
    ),
    VersionCase(
        front=AsyncExternalFulfillmentInventory,
        default_cls=AsyncExternalFulfillmentInventoryV20210106,
        latest_cls=AsyncExternalFulfillmentInventoryV20240911,
        default_value="2021-01-06",
        latest_value="2024-09-11",
        default_enum=AsyncExternalFulfillmentInventoryVersion("2021-01-06"),
        latest_enum=AsyncExternalFulfillmentInventoryVersion.LATEST,
    ),
    VersionCase(
        front=AsyncExternalFulfillmentReturns,
        default_cls=AsyncExternalFulfillmentReturnsV20210819,
        latest_cls=AsyncExternalFulfillmentReturnsV20240911,
        default_value="2021-08-19",
        latest_value="2024-09-11",
        default_enum=AsyncExternalFulfillmentReturnsVersion("2021-08-19"),
        latest_enum=AsyncExternalFulfillmentReturnsVersion.LATEST,
    ),
    VersionCase(
        front=AsyncExternalFulfillmentShipping,
        default_cls=AsyncExternalFulfillmentShippingV20210106,
        latest_cls=AsyncExternalFulfillmentShippingV20240911,
        default_value="2021-01-06",
        latest_value="2024-09-11",
        default_enum=AsyncExternalFulfillmentShippingVersion("2021-01-06"),
        latest_enum=AsyncExternalFulfillmentShippingVersion.LATEST,
    ),
    VersionCase(
        front=AsyncCatalogItems,
        default_cls=AsyncCatalogItemsV20201201,
        latest_cls=AsyncCatalogItemsV20220401,
        default_value="2020-12-01",
        latest_value="2022-04-01",
        default_enum=AsyncCatalogItemsVersion("2020-12-01"),
        latest_enum=AsyncCatalogItemsVersion.LATEST,
    ),
    VersionCase(
        front=AsyncFinances,
        default_cls=AsyncFinancesV0,
        latest_cls=AsyncFinancesV20240619,
        default_value="v0",
        latest_value="2024-06-19",
        default_enum=AsyncFinancesVersion("v0"),
        latest_enum=AsyncFinancesVersion.LATEST,
    ),
    VersionCase(
        front=AsyncFulfillmentInbound,
        default_cls=AsyncFulfillmentInboundV0,
        latest_cls=AsyncFulfillmentInboundV20240320,
        default_value="v0",
        latest_value="2024-03-20",
        default_enum=AsyncFulfillmentInboundVersion("v0"),
        latest_enum=AsyncFulfillmentInboundVersion.LATEST,
    ),
    VersionCase(
        front=AsyncAmazonWarehousingAndDistribution,
        default_cls=AsyncAmazonWarehousingAndDistributionV20240509,
        latest_cls=AsyncAmazonWarehousingAndDistributionV20240509,
        default_value="2024-05-09",
        latest_value="2024-05-09",
        default_enum=AsyncAmazonWarehousingAndDistributionVersion("2024-05-09"),
        latest_enum=AsyncAmazonWarehousingAndDistributionVersion.LATEST,
    ),
]


@pytest.mark.parametrize("case", ASYNC_CASES, ids=[c.front.__name__ for c in ASYNC_CASES])
def test_async_versioned_dispatch(case: VersionCase):
    _assert_dispatch(case)
