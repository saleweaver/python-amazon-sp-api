from sp_api.api import Inventories


def test_get_inventory_summary_marketplace():
    res = Inventories().get_inventory_summary_marketplace(**{
        "details": True,
        "marketplaceIds": ["ATVPDKIKX0DER"]
    })
    assert res.errors is None
    assert res.pagination.get('nextToken') == 'seed'
    assert res.payload.get('granularity').get('granularityType') == 'Marketplace'
