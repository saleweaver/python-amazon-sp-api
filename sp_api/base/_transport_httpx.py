import random

import httpx


def _httpx_client_kwargs(*, proxies=None, verify=True, timeout=None):
    client_kwargs = {"verify": verify}
    if timeout is not None:
        client_kwargs["timeout"] = timeout
    if proxies is not None:
        if isinstance(proxies, (list, tuple)):
            proxy_value = random.choice(proxies)
        else:
            proxy_value = proxies
        client_kwargs["proxy"] = proxy_value
    return client_kwargs


class HttpxTransport:
    def __init__(
        self, *, timeout=None, proxies=None, proxy=None, verify=True, client=None
    ):
        proxy_config = proxy if proxy is not None else proxies
        self._client = client or httpx.Client(
            **_httpx_client_kwargs(
                timeout=timeout,
                proxies=proxy_config,
                verify=verify,
            )
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
