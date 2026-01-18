from sp_api.base import Client, sp_endpoint
from sp_api.asyncio.base import AsyncBaseClient
from sp_api.base.helpers import create_md5
import urllib.parse


class Upload(AsyncBaseClient):
    @sp_endpoint("/uploads/2020-11-01/uploadDestinations/{}", method="POST")
    async def upload_document(self, resource, file, content_type="application/pdf", **kwargs):
        md5 = urllib.parse.quote(create_md5(file))
        kwargs.update(
            {
                "contentMD5": md5,
                "contentType": kwargs.pop("contentType", content_type),
                "marketplaceIds": self.marketplace_id,
            }
        )
        return await self._request(kwargs.pop("path").format(resource), params=kwargs)