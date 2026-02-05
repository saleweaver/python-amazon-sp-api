import random

from sp_api.base._transport_httpx import _httpx_client_kwargs


def test_httpx_client_kwargs_uses_single_proxy_string():
    proxies = "https://proxy.example"

    kwargs = _httpx_client_kwargs(proxies=proxies, verify=True, timeout=5)

    assert kwargs["proxy"] == "https://proxy.example"
    assert kwargs["verify"] is True
    assert kwargs["timeout"] == 5


def test_httpx_client_kwargs_selects_proxy_from_list(monkeypatch):
    proxies = ["https://proxy.example", "https://other.example"]

    monkeypatch.setattr(random, "choice", lambda values: values[0])

    kwargs = _httpx_client_kwargs(proxies=proxies, verify=False)

    assert kwargs["proxy"] == "https://proxy.example"
    assert kwargs["verify"] is False
