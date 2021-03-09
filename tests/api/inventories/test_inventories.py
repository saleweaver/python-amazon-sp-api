from sp_api.api import Inventories
from sp_api.base import SellingApiServerException, SellingApiForbiddenException, Marketplaces


def test_get_inventory_summary_marketplace():
    res = Inventories().get_inventory_summary_marketplace(**{
        "details": True,
        "marketplaceIds": ["ATVPDKIKX0DER"]
    })
    assert res.errors is None
    assert res.pagination.get('nextToken') == 'seed'
    assert res.payload.get('granularity').get('granularityType') == 'Marketplace'


def test_get_inventory_summary_marketplace_expect_500():
    try:
        Inventories().get_inventory_summary_marketplace(**{
            "marketplaceIds": ["1"],
        })
    except SellingApiForbiddenException as se:
        assert se.code == 403

