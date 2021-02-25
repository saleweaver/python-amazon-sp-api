# from datetime import datetime, timedelta
#
# from sp_api.api import FulfillmentInbound
#
# def test_get_shipments():
#     r = FulfillmentInbound().get_shipments(QueryType='DATE_RANGE', LastUpdatedAfter=(datetime.now() - timedelta(days=30)).isoformat(), LastUpdatedBefore=datetime.now().isoformat(), ShipmentStatusList=','.join([
#         'WORKING','SHIPPED','RECEIVING','CANCELLED','DELETED','CLOSED','ERROR','IN_TRANSIT','DELIVERED','CHECKED_IN'
#     ]))
#     print(r)
