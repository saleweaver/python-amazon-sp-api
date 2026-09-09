import asyncio
from io import StringIO

import httpx
import pytest

from sp_api.api import Reports
from sp_api.asyncio.api import Reports as AsyncReports
from sp_api.base._transport_httpx import HttpxTransport
from sp_api.asyncio.base._transport_httpx import AsyncHttpxTransport


DOCUMENT_ID = "0356cf79-b8b0-4226-b4b9-0ee058ea5760"
DOCUMENT_URL = "https://example.com/document"
DOCUMENT_BODY = "sku\tname\nA1\tCafé\n"


@pytest.fixture()
def credentials():
    return {
        "refresh_token": "TEST_REFRESH_TOKEN",
        "lwa_app_id": "TEST_LWA_APP_ID",
        "lwa_client_secret": "TEST_LWA_CLIENT_SECRET",
    }


def _document_response(charset):
    headers = {}
    if charset:
        headers["Content-Type"] = f"text/plain; charset={charset}"
    return httpx.Response(
        200,
        content=DOCUMENT_BODY.encode(charset or "iso-8859-1"),
        headers=headers,
    )


def _api_response(method, url, extra_payload=None):
    if "api.amazon.com" in url:
        payload = {"access_token": "TEST_TOKEN", "expires_in": 3600}
    else:
        document = {"reportDocumentId": DOCUMENT_ID, "url": DOCUMENT_URL}
        document.update(extra_payload or {})
        payload = {"payload": document}
    return httpx.Response(200, json=payload, headers={})


class DummyDocumentClient:
    """Stands in for the ``httpx.Client`` the sync client downloads through."""

    charset = None

    def __init__(self, *args, **kwargs):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def get(self, url, *args, **kwargs):
        return _document_response(type(self).charset)


@pytest.fixture()
def sync_mock(monkeypatch):
    def _mock(charset, extra_payload=None):
        monkeypatch.setattr(
            HttpxTransport,
            "request",
            lambda self, method, url, **kwargs: _api_response(
                method, url, extra_payload
            ),
        )
        monkeypatch.setattr(DummyDocumentClient, "charset", charset)
        monkeypatch.setattr(httpx, "Client", DummyDocumentClient)

    return _mock


@pytest.fixture()
def async_mock(monkeypatch):
    def _mock(charset):
        async def request(self, method, url, **kwargs):
            if url == DOCUMENT_URL:
                return _document_response(charset)
            return _api_response(method, url)

        monkeypatch.setattr(AsyncHttpxTransport, "request", request)

    return _mock


@pytest.mark.parametrize("charset,expected", [("Cp1252", "cp1252"), ("UTF-8", "utf-8")])
def test_get_report_document_exposes_resolved_character_code(
    sync_mock, credentials, charset, expected
):
    sync_mock(charset)
    res = Reports(credentials=credentials).get_report_document(
        DOCUMENT_ID, download=True
    )
    assert res.character_code == expected


def test_get_report_document_exposes_character_code_when_writing_to_file(
    sync_mock, credentials
):
    sync_mock("Cp1252")
    file = StringIO()
    res = Reports(credentials=credentials).get_report_document(DOCUMENT_ID, file=file)
    assert res.character_code == "cp1252"
    assert file.getvalue() == DOCUMENT_BODY


def test_get_report_document_echoes_explicit_character_code(sync_mock, credentials):
    sync_mock("Cp1252")
    res = Reports(credentials=credentials).get_report_document(
        DOCUMENT_ID, download=True, character_code="utf-8"
    )
    assert res.character_code == "utf-8"


def test_get_report_document_falls_back_when_no_charset_declared(
    sync_mock, credentials
):
    sync_mock(None)
    res = Reports(credentials=credentials).get_report_document(
        DOCUMENT_ID, download=True
    )
    assert res.character_code == "iso-8859-1"


def test_get_report_document_character_code_is_none_without_download(
    sync_mock, credentials
):
    sync_mock("Cp1252")
    res = Reports(credentials=credentials).get_report_document(DOCUMENT_ID)
    assert res.character_code is None
    assert "document" not in res.payload


def test_get_report_document_character_code_ignores_colliding_payload_field(
    sync_mock, credentials
):
    """A ``character_code`` field in Amazon's payload must not leak through.

    ``ApiResponse.__getattr__`` falls back to ``payload.get(item)``, so the
    attribute has to be set on every path -- not only when the document is
    fetched -- for a metadata-only call to read as ``None``.
    """
    sync_mock("Cp1252", extra_payload={"character_code": "FROM_AMAZON_PAYLOAD"})
    res = Reports(credentials=credentials).get_report_document(DOCUMENT_ID)
    assert res.character_code is None


def test_async_get_report_document_exposes_resolved_character_code(
    async_mock, credentials
):
    async_mock("Cp1252")

    async def run():
        client = AsyncReports(credentials=credentials)
        try:
            return await client.get_report_document(DOCUMENT_ID, download=True)
        finally:
            await client.aclose()

    res = asyncio.run(run())
    assert res.character_code == "cp1252"
