import httpx


class HttpxTransport:
    def __init__(
        self, *, timeout=None, proxies=None, proxy=None, verify=True, client=None
    ):
        proxy_config = proxy if proxy is not None else proxies
        self._client = client or httpx.Client(
            timeout=timeout,
            proxy=proxy_config,
            verify=verify,
        )

    def request(self, method, url, *, params=None, data=None, content=None, headers=None):
        return self._client.request(
            method,
            url,
            params=params,
            data=data,
            content=content,
            headers=headers,
        )

    def stream(
        self, method, url, *, params=None, data=None, content=None, headers=None, timeout=None
    ):
        return self._client.stream(
            method,
            url,
            params=params,
            data=data,
            content=content,
            headers=headers,
            timeout=timeout,
        )

    def close(self):
        self._client.close()
