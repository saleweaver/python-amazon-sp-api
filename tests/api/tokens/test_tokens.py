from datetime import datetime, timedelta

import pytest
from sp_api.api import Orders, Tokens
from sp_api.base import Marketplaces, SellingApiBadRequestException

#
# def test_get_token_for_bulk_orders():
#     with pytest.raises(SellingApiBadRequestException) as info:
#         res = Tokens().create_restricted_data_token(restrictedResources=[
#             {
#                 "method": "GET",
#                 "path": "/orders/v0/orders",
#                 "dataElements": ["buyerInfo", "shippingAddress"]
#             }
#         ])
#         print(res)
#
#
# def test_get_order_with_token():
#     res = Orders(restricted_data_token='foo').get_orders(CreatedAfter=(datetime.now() - timedelta(days=10)).isoformat())
#     print(res)
