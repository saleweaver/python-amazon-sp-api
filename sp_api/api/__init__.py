"""
Generated API client package from Swagger/OpenAPI specification.
This file was auto-generated. Do not edit manually.
"""

import importlib
import sys
from typing import TYPE_CHECKING

# Static imports for type checkers/IDEs
if TYPE_CHECKING:
    from .clients.amazon_warehousing_and_distribution.amazon_warehousing_and_distribution_v_2024_05_09 import \
        AmazonWarehousingAndDistribution_V_2024_05_09
    from .clients.amazon_warehousing_and_distribution.base_client import (
        AmazonWarehousingAndDistribution,
        AmazonWarehousingAndDistributionVersion)
    from .clients.aplus_content.aplus_content_v_2020_11_01 import \
        AplusContent_V_2020_11_01
    from .clients.aplus_content.base_client import (AplusContent,
                                                    AplusContentVersion)
    from .clients.application_integrations.application_integrations_v_2024_04_01 import \
        ApplicationIntegrations_V_2024_04_01
    from .clients.application_integrations.base_client import (
        ApplicationIntegrations, ApplicationIntegrationsVersion)
    from .clients.application_management.application_management_v_2023_11_30 import \
        ApplicationManagement_V_2023_11_30
    from .clients.application_management.base_client import (
        ApplicationManagement, ApplicationManagementVersion)
    from .clients.catalog_items.base_client import (CatalogItems,
                                                    CatalogItemsVersion)
    from .clients.catalog_items.catalog_items_v_2020_12_01 import \
        CatalogItems_V_2020_12_01
    from .clients.catalog_items.catalog_items_v_2022_04_01 import \
        CatalogItems_V_2022_04_01
    from .clients.catalog_items.catalog_items_v_v0 import CatalogItems_V_v0
    from .clients.customer_feedback.base_client import (
        CustomerFeedback, CustomerFeedbackVersion)
    from .clients.customer_feedback.customer_feedback_v_2024_06_01 import \
        CustomerFeedback_V_2024_06_01
    from .clients.data_kiosk.base_client import DataKiosk, DataKioskVersion
    from .clients.data_kiosk.data_kiosk_v_2023_11_15 import \
        DataKiosk_V_2023_11_15
    from .clients.easy_ship.base_client import EasyShip, EasyShipVersion
    from .clients.easy_ship.easy_ship_v_2022_03_23 import EasyShip_V_2022_03_23
    from .clients.fba_inbound_eligibility.base_client import (
        FbaInboundEligibility, FbaInboundEligibilityVersion)
    from .clients.fba_inbound_eligibility.fba_inbound_eligibility_v_v1 import \
        FbaInboundEligibility_V_v1
    from .clients.fba_inventory.base_client import (FbaInventory,
                                                    FbaInventoryVersion)
    from .clients.fba_inventory.fba_inventory_v_v1 import FbaInventory_V_v1
    from .clients.feeds.base_client import Feeds, FeedsVersion
    from .clients.feeds.feeds_v_2021_06_30 import Feeds_V_2021_06_30
    from .clients.finances.base_client import Finances, FinancesVersion
    from .clients.finances.finances_v_2024_06_01 import Finances_V_2024_06_01
    from .clients.finances.finances_v_2024_06_19 import Finances_V_2024_06_19
    from .clients.finances.finances_v_v0 import Finances_V_v0
    from .clients.fulfillment_inbound.base_client import (
        FulfillmentInbound, FulfillmentInboundVersion)
    from .clients.fulfillment_inbound.fulfillment_inbound_v_2024_03_20 import \
        FulfillmentInbound_V_2024_03_20
    from .clients.fulfillment_inbound.fulfillment_inbound_v_v0 import \
        FulfillmentInbound_V_v0
    from .clients.fulfillment_outbound.base_client import (
        FulfillmentOutbound, FulfillmentOutboundVersion)
    from .clients.fulfillment_outbound.fulfillment_outbound_v_2020_07_01 import \
        FulfillmentOutbound_V_2020_07_01
    from .clients.invoices.base_client import Invoices, InvoicesVersion
    from .clients.invoices.invoices_v_2024_06_19 import Invoices_V_2024_06_19
    from .clients.listings_items.base_client import (ListingsItems,
                                                     ListingsItemsVersion)
    from .clients.listings_items.listings_items_v_2020_09_01 import \
        ListingsItems_V_2020_09_01
    from .clients.listings_items.listings_items_v_2021_08_01 import \
        ListingsItems_V_2021_08_01
    from .clients.listings_restrictions.base_client import (
        ListingsRestrictions, ListingsRestrictionsVersion)
    from .clients.listings_restrictions.listings_restrictions_v_2021_08_01 import \
        ListingsRestrictions_V_2021_08_01
    from .clients.merchant_fulfillment.base_client import (
        MerchantFulfillment, MerchantFulfillmentVersion)
    from .clients.merchant_fulfillment.merchant_fulfillment_v_v0 import \
        MerchantFulfillment_V_v0
    from .clients.messaging.base_client import Messaging, MessagingVersion
    from .clients.messaging.messaging_v_v1 import Messaging_V_v1
    from .clients.notifications.base_client import (Notifications,
                                                    NotificationsVersion)
    from .clients.notifications.notifications_v_v1 import Notifications_V_v1
    from .clients.orders.base_client import Orders, OrdersVersion
    from .clients.orders.orders_v_v0 import Orders_V_v0
    from .clients.product_fees.base_client import (ProductFees,
                                                   ProductFeesVersion)
    from .clients.product_fees.product_fees_v_v0 import ProductFees_V_v0
    from .clients.product_pricing.base_client import (ProductPricing,
                                                      ProductPricingVersion)
    from .clients.product_pricing.product_pricing_v_2022_05_01 import \
        ProductPricing_V_2022_05_01
    from .clients.product_pricing.product_pricing_v_v0 import \
        ProductPricing_V_v0
    from .clients.product_type_definitions.base_client import (
        ProductTypeDefinitions, ProductTypeDefinitionsVersion)
    from .clients.product_type_definitions.product_type_definitions_v_2020_09_01 import \
        ProductTypeDefinitions_V_2020_09_01
    from .clients.replenishment.base_client import (Replenishment,
                                                    ReplenishmentVersion)
    from .clients.replenishment.replenishment_v_2022_11_07 import \
        Replenishment_V_2022_11_07
    from .clients.reports.base_client import Reports, ReportsVersion
    from .clients.reports.reports_v_2021_06_30 import Reports_V_2021_06_30
    from .clients.sales.base_client import Sales, SalesVersion
    from .clients.sales.sales_v_v1 import Sales_V_v1
    from .clients.seller_wallet.base_client import (SellerWallet,
                                                    SellerWalletVersion)
    from .clients.seller_wallet.seller_wallet_v_2024_03_01 import \
        SellerWallet_V_2024_03_01
    from .clients.sellers.base_client import Sellers, SellersVersion
    from .clients.sellers.sellers_v_v1 import Sellers_V_v1
    from .clients.services.base_client import Services, ServicesVersion
    from .clients.services.services_v_v1 import Services_V_v1
    from .clients.shipment_invoicing.base_client import (
        ShipmentInvoicing, ShipmentInvoicingVersion)
    from .clients.shipment_invoicing.shipment_invoicing_v_v0 import \
        ShipmentInvoicing_V_v0
    from .clients.shipping.base_client import Shipping, ShippingVersion
    from .clients.shipping.shipping_v_v1 import Shipping_V_v1
    from .clients.shipping.shipping_v_v2 import Shipping_V_v2
    from .clients.solicitations.base_client import (Solicitations,
                                                    SolicitationsVersion)
    from .clients.solicitations.solicitations_v_v1 import Solicitations_V_v1
    from .clients.supply_sources.base_client import (SupplySources,
                                                     SupplySourcesVersion)
    from .clients.supply_sources.supply_sources_v_2020_07_01 import \
        SupplySources_V_2020_07_01
    from .clients.tokens.base_client import Tokens, TokensVersion
    from .clients.tokens.tokens_v_2021_03_01 import Tokens_V_2021_03_01
    from .clients.uploads.base_client import Uploads, UploadsVersion
    from .clients.uploads.uploads_v_2020_11_01 import Uploads_V_2020_11_01
    from .clients.vehicles.base_client import Vehicles, VehiclesVersion
    from .clients.vehicles.vehicles_v_2024_11_01 import Vehicles_V_2024_11_01
    from .clients.vendor_direct_fulfillment_inventory.base_client import (
        VendorDirectFulfillmentInventory,
        VendorDirectFulfillmentInventoryVersion)
    from .clients.vendor_direct_fulfillment_inventory.vendor_direct_fulfillment_inventory_v_v1 import \
        VendorDirectFulfillmentInventory_V_v1
    from .clients.vendor_direct_fulfillment_orders.base_client import (
        VendorDirectFulfillmentOrders, VendorDirectFulfillmentOrdersVersion)
    from .clients.vendor_direct_fulfillment_orders.vendor_direct_fulfillment_orders_v_2021_12_28 import \
        VendorDirectFulfillmentOrders_V_2021_12_28
    from .clients.vendor_direct_fulfillment_orders.vendor_direct_fulfillment_orders_v_v1 import \
        VendorDirectFulfillmentOrders_V_v1
    from .clients.vendor_direct_fulfillment_payments.base_client import (
        VendorDirectFulfillmentPayments,
        VendorDirectFulfillmentPaymentsVersion)
    from .clients.vendor_direct_fulfillment_payments.vendor_direct_fulfillment_payments_v_v1 import \
        VendorDirectFulfillmentPayments_V_v1
    from .clients.vendor_direct_fulfillment_sandbox_test_data.base_client import (
        VendorDirectFulfillmentSandboxTestData,
        VendorDirectFulfillmentSandboxTestDataVersion)
    from .clients.vendor_direct_fulfillment_sandbox_test_data.vendor_direct_fulfillment_sandbox_test_data_v_2021_10_28 import \
        VendorDirectFulfillmentSandboxTestData_V_2021_10_28
    from .clients.vendor_direct_fulfillment_shipping.base_client import (
        VendorDirectFulfillmentShipping,
        VendorDirectFulfillmentShippingVersion)
    from .clients.vendor_direct_fulfillment_shipping.vendor_direct_fulfillment_shipping_v_2021_12_28 import \
        VendorDirectFulfillmentShipping_V_2021_12_28
    from .clients.vendor_direct_fulfillment_shipping.vendor_direct_fulfillment_shipping_v_v1 import \
        VendorDirectFulfillmentShipping_V_v1
    from .clients.vendor_direct_fulfillment_transactions.base_client import (
        VendorDirectFulfillmentTransactions,
        VendorDirectFulfillmentTransactionsVersion)
    from .clients.vendor_direct_fulfillment_transactions.vendor_direct_fulfillment_transactions_v_2021_12_28 import \
        VendorDirectFulfillmentTransactions_V_2021_12_28
    from .clients.vendor_direct_fulfillment_transactions.vendor_direct_fulfillment_transactions_v_v1 import \
        VendorDirectFulfillmentTransactions_V_v1
    from .clients.vendor_invoices.base_client import (VendorInvoices,
                                                      VendorInvoicesVersion)
    from .clients.vendor_invoices.vendor_invoices_v_v1 import \
        VendorInvoices_V_v1
    from .clients.vendor_orders.base_client import (VendorOrders,
                                                    VendorOrdersVersion)
    from .clients.vendor_orders.vendor_orders_v_v1 import VendorOrders_V_v1
    from .clients.vendor_shipments.base_client import (VendorShipments,
                                                       VendorShipmentsVersion)
    from .clients.vendor_shipments.vendor_shipments_v_v1 import \
        VendorShipments_V_v1
    from .clients.vendor_transaction_status.base_client import (
        VendorTransactionStatus, VendorTransactionStatusVersion)
    from .clients.vendor_transaction_status.vendor_transaction_status_v_v1 import \
        VendorTransactionStatus_V_v1

# Public API
__all__ = [
    "EasyShip_V_2022_03_23",
    "AmazonWarehousingAndDistribution_V_2024_05_09",
    "CatalogItems_V_v0",
    "Finances_V_v0",
    "ListingsItems_V_2020_09_01",
    "DataKiosk_V_2023_11_15",
    "ListingsRestrictions_V_2021_08_01",
    "ApplicationManagement_V_2023_11_30",
    "FulfillmentInbound_V_2024_03_20",
    "MerchantFulfillment_V_v0",
    "Invoices_V_2024_06_19",
    "FulfillmentInbound_V_v0",
    "Finances_V_2024_06_01",
    "AplusContent_V_2020_11_01",
    "ListingsItems_V_2021_08_01",
    "Finances_V_2024_06_19",
    "ApplicationIntegrations_V_2024_04_01",
    "FbaInventory_V_v1",
    "CatalogItems_V_2022_04_01",
    "FbaInboundEligibility_V_v1",
    "CatalogItems_V_2020_12_01",
    "Feeds_V_2021_06_30",
    "CustomerFeedback_V_2024_06_01",
    "FulfillmentOutbound_V_2020_07_01",
    "Messaging_V_v1",
    "ProductFees_V_v0",
    "Notifications_V_v1",
    "Sales_V_v1",
    "ProductTypeDefinitions_V_2020_09_01",
    "ProductPricing_V_2022_05_01",
    "SellerWallet_V_2024_03_01",
    "Reports_V_2021_06_30",
    "Orders_V_v0",
    "ProductPricing_V_v0",
    "Replenishment_V_2022_11_07",
    "Sellers_V_v1",
    "Services_V_v1",
    "ShipmentInvoicing_V_v0",
    "Vehicles_V_2024_11_01",
    "Shipping_V_v2",
    "SupplySources_V_2020_07_01",
    "Uploads_V_2020_11_01",
    "VendorDirectFulfillmentInventory_V_v1",
    "Tokens_V_2021_03_01",
    "VendorDirectFulfillmentPayments_V_v1",
    "Solicitations_V_v1",
    "Shipping_V_v1",
    "VendorDirectFulfillmentOrders_V_2021_12_28",
    "VendorDirectFulfillmentOrders_V_v1",
    "VendorDirectFulfillmentSandboxTestData_V_2021_10_28",
    "VendorDirectFulfillmentTransactions_V_v1",
    "VendorDirectFulfillmentTransactions_V_2021_12_28",
    "VendorInvoices_V_v1",
    "VendorTransactionStatus_V_v1",
    "VendorOrders_V_v1",
    "VendorShipments_V_v1",
    "VendorDirectFulfillmentShipping_V_2021_12_28",
    "VendorDirectFulfillmentShipping_V_v1",
    "AmazonWarehousingAndDistribution",
    "AmazonWarehousingAndDistributionVersion",
    "AplusContent",
    "AplusContentVersion",
    "ApplicationIntegrations",
    "ApplicationIntegrationsVersion",
    "ApplicationManagement",
    "ApplicationManagementVersion",
    "CatalogItems",
    "CatalogItemsVersion",
    "CustomerFeedback",
    "CustomerFeedbackVersion",
    "DataKiosk",
    "DataKioskVersion",
    "EasyShip",
    "EasyShipVersion",
    "FbaInboundEligibility",
    "FbaInboundEligibilityVersion",
    "FbaInventory",
    "FbaInventoryVersion",
    "Feeds",
    "FeedsVersion",
    "Finances",
    "FinancesVersion",
    "FulfillmentInbound",
    "FulfillmentInboundVersion",
    "FulfillmentOutbound",
    "FulfillmentOutboundVersion",
    "Invoices",
    "InvoicesVersion",
    "ListingsItems",
    "ListingsItemsVersion",
    "ListingsRestrictions",
    "ListingsRestrictionsVersion",
    "MerchantFulfillment",
    "MerchantFulfillmentVersion",
    "Messaging",
    "MessagingVersion",
    "Notifications",
    "NotificationsVersion",
    "Orders",
    "OrdersVersion",
    "ProductFees",
    "ProductFeesVersion",
    "ProductPricing",
    "ProductPricingVersion",
    "ProductTypeDefinitions",
    "ProductTypeDefinitionsVersion",
    "Replenishment",
    "ReplenishmentVersion",
    "Reports",
    "ReportsVersion",
    "Sales",
    "SalesVersion",
    "SellerWallet",
    "SellerWalletVersion",
    "Sellers",
    "SellersVersion",
    "Services",
    "ServicesVersion",
    "ShipmentInvoicing",
    "ShipmentInvoicingVersion",
    "Shipping",
    "ShippingVersion",
    "Solicitations",
    "SolicitationsVersion",
    "SupplySources",
    "SupplySourcesVersion",
    "Tokens",
    "TokensVersion",
    "Uploads",
    "UploadsVersion",
    "Vehicles",
    "VehiclesVersion",
    "VendorDirectFulfillmentInventory",
    "VendorDirectFulfillmentInventoryVersion",
    "VendorDirectFulfillmentOrders",
    "VendorDirectFulfillmentOrdersVersion",
    "VendorDirectFulfillmentPayments",
    "VendorDirectFulfillmentPaymentsVersion",
    "VendorDirectFulfillmentSandboxTestData",
    "VendorDirectFulfillmentSandboxTestDataVersion",
    "VendorDirectFulfillmentShipping",
    "VendorDirectFulfillmentShippingVersion",
    "VendorDirectFulfillmentTransactions",
    "VendorDirectFulfillmentTransactionsVersion",
    "VendorInvoices",
    "VendorInvoicesVersion",
    "VendorOrders",
    "VendorOrdersVersion",
    "VendorShipments",
    "VendorShipmentsVersion",
    "VendorTransactionStatus",
    "VendorTransactionStatusVersion",
]

# Mapping of name to submodule path
_client_map = {
    "EasyShip_V_2022_03_23": "clients.easy_ship.easy_ship_v_2022_03_23",
    "AmazonWarehousingAndDistribution_V_2024_05_09": "clients.amazon_warehousing_and_distribution.amazon_warehousing_and_distribution_v_2024_05_09",
    "CatalogItems_V_v0": "clients.catalog_items.catalog_items_v_v0",
    "Finances_V_v0": "clients.finances.finances_v_v0",
    "ListingsItems_V_2020_09_01": "clients.listings_items.listings_items_v_2020_09_01",
    "DataKiosk_V_2023_11_15": "clients.data_kiosk.data_kiosk_v_2023_11_15",
    "ListingsRestrictions_V_2021_08_01": "clients.listings_restrictions.listings_restrictions_v_2021_08_01",
    "ApplicationManagement_V_2023_11_30": "clients.application_management.application_management_v_2023_11_30",
    "FulfillmentInbound_V_2024_03_20": "clients.fulfillment_inbound.fulfillment_inbound_v_2024_03_20",
    "MerchantFulfillment_V_v0": "clients.merchant_fulfillment.merchant_fulfillment_v_v0",
    "Invoices_V_2024_06_19": "clients.invoices.invoices_v_2024_06_19",
    "FulfillmentInbound_V_v0": "clients.fulfillment_inbound.fulfillment_inbound_v_v0",
    "Finances_V_2024_06_01": "clients.finances.finances_v_2024_06_01",
    "AplusContent_V_2020_11_01": "clients.aplus_content.aplus_content_v_2020_11_01",
    "ListingsItems_V_2021_08_01": "clients.listings_items.listings_items_v_2021_08_01",
    "Finances_V_2024_06_19": "clients.finances.finances_v_2024_06_19",
    "ApplicationIntegrations_V_2024_04_01": "clients.application_integrations.application_integrations_v_2024_04_01",
    "FbaInventory_V_v1": "clients.fba_inventory.fba_inventory_v_v1",
    "CatalogItems_V_2022_04_01": "clients.catalog_items.catalog_items_v_2022_04_01",
    "FbaInboundEligibility_V_v1": "clients.fba_inbound_eligibility.fba_inbound_eligibility_v_v1",
    "CatalogItems_V_2020_12_01": "clients.catalog_items.catalog_items_v_2020_12_01",
    "Feeds_V_2021_06_30": "clients.feeds.feeds_v_2021_06_30",
    "CustomerFeedback_V_2024_06_01": "clients.customer_feedback.customer_feedback_v_2024_06_01",
    "FulfillmentOutbound_V_2020_07_01": "clients.fulfillment_outbound.fulfillment_outbound_v_2020_07_01",
    "Messaging_V_v1": "clients.messaging.messaging_v_v1",
    "ProductFees_V_v0": "clients.product_fees.product_fees_v_v0",
    "Notifications_V_v1": "clients.notifications.notifications_v_v1",
    "Sales_V_v1": "clients.sales.sales_v_v1",
    "ProductTypeDefinitions_V_2020_09_01": "clients.product_type_definitions.product_type_definitions_v_2020_09_01",
    "ProductPricing_V_2022_05_01": "clients.product_pricing.product_pricing_v_2022_05_01",
    "SellerWallet_V_2024_03_01": "clients.seller_wallet.seller_wallet_v_2024_03_01",
    "Reports_V_2021_06_30": "clients.reports.reports_v_2021_06_30",
    "Orders_V_v0": "clients.orders.orders_v_v0",
    "ProductPricing_V_v0": "clients.product_pricing.product_pricing_v_v0",
    "Replenishment_V_2022_11_07": "clients.replenishment.replenishment_v_2022_11_07",
    "Sellers_V_v1": "clients.sellers.sellers_v_v1",
    "Services_V_v1": "clients.services.services_v_v1",
    "ShipmentInvoicing_V_v0": "clients.shipment_invoicing.shipment_invoicing_v_v0",
    "Vehicles_V_2024_11_01": "clients.vehicles.vehicles_v_2024_11_01",
    "Shipping_V_v2": "clients.shipping.shipping_v_v2",
    "SupplySources_V_2020_07_01": "clients.supply_sources.supply_sources_v_2020_07_01",
    "Uploads_V_2020_11_01": "clients.uploads.uploads_v_2020_11_01",
    "VendorDirectFulfillmentInventory_V_v1": "clients.vendor_direct_fulfillment_inventory.vendor_direct_fulfillment_inventory_v_v1",
    "Tokens_V_2021_03_01": "clients.tokens.tokens_v_2021_03_01",
    "VendorDirectFulfillmentPayments_V_v1": "clients.vendor_direct_fulfillment_payments.vendor_direct_fulfillment_payments_v_v1",
    "Solicitations_V_v1": "clients.solicitations.solicitations_v_v1",
    "Shipping_V_v1": "clients.shipping.shipping_v_v1",
    "VendorDirectFulfillmentOrders_V_2021_12_28": "clients.vendor_direct_fulfillment_orders.vendor_direct_fulfillment_orders_v_2021_12_28",
    "VendorDirectFulfillmentOrders_V_v1": "clients.vendor_direct_fulfillment_orders.vendor_direct_fulfillment_orders_v_v1",
    "VendorDirectFulfillmentSandboxTestData_V_2021_10_28": "clients.vendor_direct_fulfillment_sandbox_test_data.vendor_direct_fulfillment_sandbox_test_data_v_2021_10_28",
    "VendorDirectFulfillmentTransactions_V_v1": "clients.vendor_direct_fulfillment_transactions.vendor_direct_fulfillment_transactions_v_v1",
    "VendorDirectFulfillmentTransactions_V_2021_12_28": "clients.vendor_direct_fulfillment_transactions.vendor_direct_fulfillment_transactions_v_2021_12_28",
    "VendorInvoices_V_v1": "clients.vendor_invoices.vendor_invoices_v_v1",
    "VendorTransactionStatus_V_v1": "clients.vendor_transaction_status.vendor_transaction_status_v_v1",
    "VendorOrders_V_v1": "clients.vendor_orders.vendor_orders_v_v1",
    "VendorShipments_V_v1": "clients.vendor_shipments.vendor_shipments_v_v1",
    "VendorDirectFulfillmentShipping_V_2021_12_28": "clients.vendor_direct_fulfillment_shipping.vendor_direct_fulfillment_shipping_v_2021_12_28",
    "VendorDirectFulfillmentShipping_V_v1": "clients.vendor_direct_fulfillment_shipping.vendor_direct_fulfillment_shipping_v_v1",
    "AmazonWarehousingAndDistribution": "clients.amazon_warehousing_and_distribution.base_client",
    "AmazonWarehousingAndDistributionVersion": "clients.amazon_warehousing_and_distribution.base_client",
    "AplusContent": "clients.aplus_content.base_client",
    "AplusContentVersion": "clients.aplus_content.base_client",
    "ApplicationIntegrations": "clients.application_integrations.base_client",
    "ApplicationIntegrationsVersion": "clients.application_integrations.base_client",
    "ApplicationManagement": "clients.application_management.base_client",
    "ApplicationManagementVersion": "clients.application_management.base_client",
    "CatalogItems": "clients.catalog_items.base_client",
    "CatalogItemsVersion": "clients.catalog_items.base_client",
    "CustomerFeedback": "clients.customer_feedback.base_client",
    "CustomerFeedbackVersion": "clients.customer_feedback.base_client",
    "DataKiosk": "clients.data_kiosk.base_client",
    "DataKioskVersion": "clients.data_kiosk.base_client",
    "EasyShip": "clients.easy_ship.base_client",
    "EasyShipVersion": "clients.easy_ship.base_client",
    "FbaInboundEligibility": "clients.fba_inbound_eligibility.base_client",
    "FbaInboundEligibilityVersion": "clients.fba_inbound_eligibility.base_client",
    "FbaInventory": "clients.fba_inventory.base_client",
    "FbaInventoryVersion": "clients.fba_inventory.base_client",
    "Feeds": "clients.feeds.base_client",
    "FeedsVersion": "clients.feeds.base_client",
    "Finances": "clients.finances.base_client",
    "FinancesVersion": "clients.finances.base_client",
    "FulfillmentInbound": "clients.fulfillment_inbound.base_client",
    "FulfillmentInboundVersion": "clients.fulfillment_inbound.base_client",
    "FulfillmentOutbound": "clients.fulfillment_outbound.base_client",
    "FulfillmentOutboundVersion": "clients.fulfillment_outbound.base_client",
    "Invoices": "clients.invoices.base_client",
    "InvoicesVersion": "clients.invoices.base_client",
    "ListingsItems": "clients.listings_items.base_client",
    "ListingsItemsVersion": "clients.listings_items.base_client",
    "ListingsRestrictions": "clients.listings_restrictions.base_client",
    "ListingsRestrictionsVersion": "clients.listings_restrictions.base_client",
    "MerchantFulfillment": "clients.merchant_fulfillment.base_client",
    "MerchantFulfillmentVersion": "clients.merchant_fulfillment.base_client",
    "Messaging": "clients.messaging.base_client",
    "MessagingVersion": "clients.messaging.base_client",
    "Notifications": "clients.notifications.base_client",
    "NotificationsVersion": "clients.notifications.base_client",
    "Orders": "clients.orders.base_client",
    "OrdersVersion": "clients.orders.base_client",
    "ProductFees": "clients.product_fees.base_client",
    "ProductFeesVersion": "clients.product_fees.base_client",
    "ProductPricing": "clients.product_pricing.base_client",
    "ProductPricingVersion": "clients.product_pricing.base_client",
    "ProductTypeDefinitions": "clients.product_type_definitions.base_client",
    "ProductTypeDefinitionsVersion": "clients.product_type_definitions.base_client",
    "Replenishment": "clients.replenishment.base_client",
    "ReplenishmentVersion": "clients.replenishment.base_client",
    "Reports": "clients.reports.base_client",
    "ReportsVersion": "clients.reports.base_client",
    "Sales": "clients.sales.base_client",
    "SalesVersion": "clients.sales.base_client",
    "SellerWallet": "clients.seller_wallet.base_client",
    "SellerWalletVersion": "clients.seller_wallet.base_client",
    "Sellers": "clients.sellers.base_client",
    "SellersVersion": "clients.sellers.base_client",
    "Services": "clients.services.base_client",
    "ServicesVersion": "clients.services.base_client",
    "ShipmentInvoicing": "clients.shipment_invoicing.base_client",
    "ShipmentInvoicingVersion": "clients.shipment_invoicing.base_client",
    "Shipping": "clients.shipping.base_client",
    "ShippingVersion": "clients.shipping.base_client",
    "Solicitations": "clients.solicitations.base_client",
    "SolicitationsVersion": "clients.solicitations.base_client",
    "SupplySources": "clients.supply_sources.base_client",
    "SupplySourcesVersion": "clients.supply_sources.base_client",
    "Tokens": "clients.tokens.base_client",
    "TokensVersion": "clients.tokens.base_client",
    "Uploads": "clients.uploads.base_client",
    "UploadsVersion": "clients.uploads.base_client",
    "Vehicles": "clients.vehicles.base_client",
    "VehiclesVersion": "clients.vehicles.base_client",
    "VendorDirectFulfillmentInventory": "clients.vendor_direct_fulfillment_inventory.base_client",
    "VendorDirectFulfillmentInventoryVersion": "clients.vendor_direct_fulfillment_inventory.base_client",
    "VendorDirectFulfillmentOrders": "clients.vendor_direct_fulfillment_orders.base_client",
    "VendorDirectFulfillmentOrdersVersion": "clients.vendor_direct_fulfillment_orders.base_client",
    "VendorDirectFulfillmentPayments": "clients.vendor_direct_fulfillment_payments.base_client",
    "VendorDirectFulfillmentPaymentsVersion": "clients.vendor_direct_fulfillment_payments.base_client",
    "VendorDirectFulfillmentSandboxTestData": "clients.vendor_direct_fulfillment_sandbox_test_data.base_client",
    "VendorDirectFulfillmentSandboxTestDataVersion": "clients.vendor_direct_fulfillment_sandbox_test_data.base_client",
    "VendorDirectFulfillmentShipping": "clients.vendor_direct_fulfillment_shipping.base_client",
    "VendorDirectFulfillmentShippingVersion": "clients.vendor_direct_fulfillment_shipping.base_client",
    "VendorDirectFulfillmentTransactions": "clients.vendor_direct_fulfillment_transactions.base_client",
    "VendorDirectFulfillmentTransactionsVersion": "clients.vendor_direct_fulfillment_transactions.base_client",
    "VendorInvoices": "clients.vendor_invoices.base_client",
    "VendorInvoicesVersion": "clients.vendor_invoices.base_client",
    "VendorOrders": "clients.vendor_orders.base_client",
    "VendorOrdersVersion": "clients.vendor_orders.base_client",
    "VendorShipments": "clients.vendor_shipments.base_client",
    "VendorShipmentsVersion": "clients.vendor_shipments.base_client",
    "VendorTransactionStatus": "clients.vendor_transaction_status.base_client",
    "VendorTransactionStatusVersion": "clients.vendor_transaction_status.base_client",
}


def __getattr__(name: str):
    """
    Lazy-load API client classes on first access.
    """
    try:
        module_path = _client_map[name]
    except KeyError:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module = importlib.import_module(f".{module_path}", __name__)
    value = getattr(module, name)
    setattr(sys.modules[__name__], name, value)
    return value


def __dir__():
    return __all__
