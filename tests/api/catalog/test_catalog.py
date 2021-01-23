from sp_api.api import Catalog
from sp_api.base import Marketplaces


def test_catalog_get_item():
    asin = 'B008DZ2JT4'
    print(Catalog(marketplace=Marketplaces.DE).get_item(asin))
    # print(Catalog(marketplace=Marketplaces.DE).list_items(EAN='0730143302517'))

