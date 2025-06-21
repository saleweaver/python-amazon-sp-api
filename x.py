from sp_api.api import CatalogItemsVersion
from sp_api.api.clients.catalog_items.catalog_items_v_2022_04_01 import CatalogItems_V_2022_04_01
from sp_api.api.clients.catalog_items.catalog_items_v_v0 import CatalogItems_V_v0
from sp_api.base import Marketplaces, ApiResponse
from sp_api.api.models.catalog_items.catalog_items_2022_04_01 import SearchCatalogItemsRequest
from sp_api.api import CatalogItems
from sp_api.api.models.catalog_items.catalog_items_2022_04_01.common import IncludedDataEnum, IdentifiersTypeEnum, \
    ItemSearchResults

if __name__ == '__main__':
    req = SearchCatalogItemsRequest(
        keywords=['hello barbie'],
        included_data=[IncludedDataEnum.SUMMARIES],
    )
    x = req.model_dump()
    print(x)

    # for k,v in x.items():
    #     v = ','.join(str(vv) for vv in v)
    #     print(v)

    client: CatalogItems_V_2022_04_01 = CatalogItems(marketplace=Marketplaces.DE)

    print(client.search_catalog_items(req).payload_parsed)

