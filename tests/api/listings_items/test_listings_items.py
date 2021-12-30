from sp_api.api import ListingsItems
from sp_api.base import Marketplaces


def test_get_listings_item():
    res = ListingsItems().get_listings_item('xxx', 'xxx')
    assert res is not None


def test_put_listings_item():
    res = ListingsItems().put_listings_item('xxx', 'xxx', body={
              "productType": "string",
              "requirements": "LISTING",
              "attributes": {},

            }, marketplaceIds=[Marketplaces.US.marketplace_id])
    assert res('status') == 'ACCEPTED'


def test_patch_listings_item():
    res = ListingsItems().patch_listings_item('xxx', 'xxx', body={
              "productType": "string",
              "patches": [
                {
                  "op": "add",
                  "path": "string",
                  "value": [
                    {}
                  ]
                }
              ]
            })
    assert res('status') == 'ACCEPTED'


def test_delete_listings_item():
    res = ListingsItems().delete_listings_item('xxx', 'xxx')
    assert res('status') == 'ACCEPTED'
