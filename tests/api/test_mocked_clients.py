import asyncio
import ast
import importlib
import inspect
import pkgutil
import re
from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from typing import Iterable, List, Dict, Tuple

import httpx
import pytest

from sp_api.base import ApiResponse
from sp_api.base._transport_httpx import HttpxTransport
from sp_api.asyncio.base._transport_httpx import AsyncHttpxTransport
from sp_api.base import Client as SyncClientBase
from sp_api.asyncio.base import AsyncBaseClient as AsyncClientBase


ROOT = Path(__file__).resolve().parents[2]
SYNC_API_DIR = ROOT / "sp_api" / "api"
ASYNC_API_DIR = ROOT / "sp_api" / "asyncio" / "api"


@dataclass(frozen=True)
class EndpointSpec:
    module: str
    class_name: str
    func_name: str
    path: str
    http_method: str
    is_async: bool

    @property
    def id(self) -> str:
        return f"{self.module}.{self.class_name}.{self.func_name}"


class RequestRecorder:
    def __init__(self) -> None:
        self.requests: List[dict] = []

    def _response_for(self, method: str, url: str) -> httpx.Response:
        if "api.amazon.com" in url:
            payload = {"access_token": "TEST_TOKEN", "expires_in": 3600}
        else:
            payload = {
                "payload": {
                    "mocked": True,
                    "url": "https://example.com/document",
                    "method": method,
                }
            }
        return httpx.Response(
            200,
            json=payload,
            headers={"x-amzn-RateLimit-Limit": "1"},
        )

    def sync_request(
        self,
        method,
        url,
        *,
        params=None,
        data=None,
        content=None,
        headers=None,
    ):
        self.requests.append(
            {
                "method": method,
                "url": url,
                "params": params,
                "data": data,
                "content": content,
                "headers": headers,
            }
        )
        return self._response_for(method, url)

    async def async_request(
        self,
        method,
        url,
        *,
        params=None,
        data=None,
        content=None,
        headers=None,
        timeout=None,
    ):
        self.requests.append(
            {
                "method": method,
                "url": url,
                "params": params,
                "data": data,
                "content": content,
                "headers": headers,
            }
        )
        return self._response_for(method, url)


@pytest.fixture()
def httpx_recorder(monkeypatch):
    recorder = RequestRecorder()
    monkeypatch.setattr(HttpxTransport, "request", recorder.sync_request)
    monkeypatch.setattr(AsyncHttpxTransport, "request", recorder.async_request)
    monkeypatch.setattr(httpx, "Client", DummyHttpxClient)
    monkeypatch.setattr(httpx, "AsyncClient", DummyAsyncHttpxClient)
    return recorder


@pytest.fixture(scope="session")
def credentials():
    return {
        "refresh_token": "TEST_REFRESH_TOKEN",
        "lwa_app_id": "TEST_LWA_APP_ID",
        "lwa_client_secret": "TEST_LWA_CLIENT_SECRET",
    }


def _module_name_from_path(path: Path) -> str:
    rel = path.relative_to(ROOT).with_suffix("")
    return ".".join(rel.parts)


def _extract_decorator_info(dec: ast.AST):
    if not isinstance(dec, ast.Call):
        return None
    func_name = None
    if isinstance(dec.func, ast.Name):
        func_name = dec.func.id
    elif isinstance(dec.func, ast.Attribute):
        func_name = dec.func.attr
    if func_name != "sp_endpoint":
        return None
    path = None
    method = None
    if dec.args and isinstance(dec.args[0], ast.Constant) and isinstance(dec.args[0].value, str):
        path = dec.args[0].value
    if len(dec.args) > 1 and isinstance(dec.args[1], ast.Constant) and isinstance(dec.args[1].value, str):
        method = dec.args[1].value
    for kw in dec.keywords:
        if kw.arg == "method" and isinstance(kw.value, ast.Constant) and isinstance(kw.value.value, str):
            method = kw.value.value
    if path and method:
        return path, method.upper()
    return None


def collect_endpoint_specs(base_dir: Path, is_async: bool) -> List[EndpointSpec]:
    specs: Dict[Tuple[str, str, str], EndpointSpec] = {}
    for file in base_dir.rglob("*.py"):
        if file.name == "__init__.py":
            continue
        tree = ast.parse(file.read_text())
        module = _module_name_from_path(file)
        for node in tree.body:
            if not isinstance(node, ast.ClassDef):
                continue
            for item in node.body:
                if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                if item.name.startswith("_"):
                    continue
                for dec in item.decorator_list:
                    info = _extract_decorator_info(dec)
                    if info is None:
                        continue
                    path, method = info
                    key = (module, node.name, item.name)
                    specs[key] = EndpointSpec(
                        module=module,
                        class_name=node.name,
                        func_name=item.name,
                        path=path,
                        http_method=method,
                        is_async=is_async,
                    )
    return list(specs.values())


def iter_client_classes(package: str, base_class: type) -> Iterable[type]:
    pkg = importlib.import_module(package)
    for module_info in pkgutil.walk_packages(pkg.__path__, pkg.__name__ + "."):
        module = importlib.import_module(module_info.name)
        for _, obj in inspect.getmembers(module, inspect.isclass):
            if obj.__module__ != module.__name__:
                continue
            if obj is base_class:
                continue
            if issubclass(obj, base_class):
                yield obj


def _dummy_value_for(param: inspect.Parameter):
    name = param.name
    if name in {"file", "document"}:
        return BytesIO(b"test")
    if name in {"body", "data", "payload"}:
        return {}
    annotation = param.annotation
    origin = getattr(annotation, "__origin__", None)
    if annotation in (bool,):
        return True
    if annotation in (int,):
        return 1
    if annotation in (float,):
        return 1.0
    if annotation in (dict,):
        return {}
    if annotation in (list,):
        return []
    if origin in (list, List):
        return []
    if origin in (dict,):
        return {}
    return "value"


def _build_call_args(func, spec: EndpointSpec):
    sig = inspect.signature(func)
    args = []
    kwargs = {}
    for param in sig.parameters.values():
        if param.name == "self":
            continue
        if param.kind in (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD):
            continue
        if param.default is inspect._empty:
            value = _dummy_value_for(param)
            if param.kind in (inspect.Parameter.POSITIONAL_ONLY, inspect.Parameter.POSITIONAL_OR_KEYWORD):
                args.append(value)
            elif param.kind == inspect.Parameter.KEYWORD_ONLY:
                kwargs[param.name] = value
    if any(p.kind == inspect.Parameter.VAR_KEYWORD for p in sig.parameters.values()):
        kwargs.setdefault("body", {})
    return args, kwargs


def _expected_path(path: str, client) -> str:
    version = getattr(client, "version", None)
    if version:
        path = path.replace("<version>", version)
    path = re.sub(r"\{[^}]*\}", "value", path)
    return path


def _last_sp_api_request(requests: List[dict]) -> dict:
    for req in reversed(requests):
        if "sellingpartnerapi" in req["url"]:
            return req
    return requests[-1] if requests else {}


SYNC_ENDPOINT_SPECS = collect_endpoint_specs(SYNC_API_DIR, is_async=False)
ASYNC_ENDPOINT_SPECS = collect_endpoint_specs(ASYNC_API_DIR, is_async=True)

SYNC_CLIENT_CLASSES = list(iter_client_classes("sp_api.api", SyncClientBase))
ASYNC_CLIENT_CLASSES = list(iter_client_classes("sp_api.asyncio.api", AsyncClientBase))


@pytest.mark.parametrize("client_cls", SYNC_CLIENT_CLASSES, ids=lambda c: c.__name__)
def test_sync_client_instantiation(client_cls, credentials, httpx_recorder):
    client = client_cls(credentials=credentials)
    assert client is not None
    client.close()


@pytest.mark.parametrize("spec", SYNC_ENDPOINT_SPECS, ids=lambda s: s.id)
def test_sync_endpoint_calls(spec: EndpointSpec, credentials, httpx_recorder):
    httpx_recorder.requests.clear()
    module = importlib.import_module(spec.module)
    cls = getattr(module, spec.class_name)
    client = cls(credentials=credentials)
    method = getattr(client, spec.func_name)
    args, kwargs = _build_call_args(method, spec)
    response = method(*args, **kwargs)
    if isinstance(response, ApiResponse):
        assert response.payload.get("mocked") is True
    req = _last_sp_api_request(httpx_recorder.requests)
    expected = _expected_path(spec.path, client)
    assert req["method"].upper() == spec.http_method
    assert expected in req["url"]
    client.close()


@pytest.mark.parametrize("client_cls", ASYNC_CLIENT_CLASSES, ids=lambda c: c.__name__)
def test_async_client_instantiation(client_cls, credentials, httpx_recorder):
    client = client_cls(credentials=credentials)
    assert client is not None
    asyncio.run(client.aclose())


@pytest.mark.parametrize("spec", ASYNC_ENDPOINT_SPECS, ids=lambda s: s.id)
def test_async_endpoint_calls(spec: EndpointSpec, credentials, httpx_recorder):
    httpx_recorder.requests.clear()
    module = importlib.import_module(spec.module)
    cls = getattr(module, spec.class_name)
    client = cls(credentials=credentials)
    method = getattr(client, spec.func_name)
    args, kwargs = _build_call_args(method, spec)
    response = asyncio.run(method(*args, **kwargs))
    if isinstance(response, ApiResponse):
        assert response.payload.get("mocked") is True
    req = _last_sp_api_request(httpx_recorder.requests)
    expected = _expected_path(spec.path, client)
    assert req["method"].upper() == spec.http_method
    assert expected in req["url"]
    asyncio.run(client.aclose())


class DummyHttpxClient:
    def __init__(self, *args, **kwargs):
        self._headers = kwargs.get("headers", {})

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def close(self):
        return None

    def get(self, url, *args, **kwargs):
        return httpx.Response(
            200,
            content=b"{}",
            headers={},
            request=httpx.Request("GET", url),
        )

    def put(self, url, *args, **kwargs):
        return httpx.Response(
            200,
            json={},
            headers={},
            request=httpx.Request("PUT", url),
        )

    def stream(self, method, url, *args, **kwargs):
        return self

    @property
    def encoding(self):
        return "utf-8"

    @property
    def content(self):
        return b"{}"


class DummyAsyncHttpxClient:
    def __init__(self, *args, **kwargs):
        self._headers = kwargs.get("headers", {})

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        return False

    async def aclose(self):
        return None

    async def get(self, url, *args, **kwargs):
        return httpx.Response(
            200,
            content=b"{}",
            headers={},
            request=httpx.Request("GET", url),
        )

    async def put(self, url, *args, **kwargs):
        return httpx.Response(
            200,
            json={},
            headers={},
            request=httpx.Request("PUT", url),
        )

    def stream(self, method, url, *args, **kwargs):
        return self

    @property
    def encoding(self):
        return "utf-8"

    @property
    def content(self):
        return b"{}"
