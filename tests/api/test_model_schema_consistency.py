from __future__ import annotations

import ast
import json
import re
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import pytest


MODELS_REPO_URL = "https://github.com/amzn/selling-partner-api-models"
MODELS_REPO_DIRNAME = "selling-partner-api-models"

SERVICE_DIR_OVERRIDES = {
    "amazon-warehousing-and-distribution-model": "amazon_warehousing_and_distribu",
    "product-pricing-api-model": "products",
    "uploads-api-model": "upload",
    "fba-inventory-api-model": "inventories",
}

IGNORE_MODEL_FILES = {
    "catalogItemsV0.json",
    "externalFulfillmentInventory_2021-01-06.json",
    "externalFulfillmentReturns_2021-08-19.json",
    "externalFulfillmentShipments_2021-01-06.json",
}

HTTP_METHODS = {"get", "post", "put", "delete", "patch", "head", "options"}


def _ensure_models_repo() -> Path:
    base = Path(tempfile.gettempdir())
    repo_root = base / MODELS_REPO_DIRNAME
    models_dir = repo_root / "models"
    if models_dir.exists():
        return models_dir

    subprocess.run(
        ["git", "clone", "--depth", "1", MODELS_REPO_URL, str(repo_root)],
        check=True,
        capture_output=True,
        text=True,
    )
    return models_dir


def _normalize_service_dir(model_dir_name: str) -> str:
    override = SERVICE_DIR_OVERRIDES.get(model_dir_name)
    if override:
        return override
    name = model_dir_name
    if name.endswith("-api-model"):
        name = name[: -len("-api-model")]
    elif name.endswith("-model"):
        name = name[: -len("-model")]
    return name.replace("-", "_")


def _parse_model_version(file_stem: str) -> str | None:
    date_match = re.match(r"^.+_(\d{4}-\d{2}-\d{2})$", file_stem)
    if date_match:
        return date_match.group(1)
    ver_match = re.match(r"^.+V(\d+)$", file_stem)
    if ver_match:
        return f"v{ver_match.group(1)}"
    return None


def _parse_module_version(file_stem: str) -> str | None:
    date_match = re.match(r"^.+_(\d{4})_(\d{2})_(\d{2})$", file_stem)
    if date_match:
        return f"{date_match.group(1)}-{date_match.group(2)}-{date_match.group(3)}"
    ver_match = re.match(r"^.+_v(\d+)$", file_stem)
    if ver_match:
        return f"v{ver_match.group(1)}"
    return None


def _index_service_modules(base_dir: Path) -> dict[str, dict[str | None, Path]]:
    service_index: dict[str, dict[str | None, Path]] = {}
    for service_dir in base_dir.iterdir():
        if not service_dir.is_dir():
            continue
        versions: dict[str | None, Path] = {}
        for file_path in service_dir.glob("*.py"):
            if file_path.name == "__init__.py":
                continue
            version = _parse_module_version(file_path.stem)
            if version is None and file_path.stem != service_dir.name:
                continue
            versions[version] = file_path
        if versions:
            if None in versions and len(versions) > 1:
                versions.pop(None)
            service_index[service_dir.name] = versions
    return service_index


def _normalize_path(path: str) -> str:
    return re.sub(r"\{[^}]+\}", "{}", path)


def _operation_name(operation_id: str) -> str:
    return re.sub(
        r"([A-Z])",
        lambda match: f"_{match.group(1).lower()}",
        operation_id[0].lower() + operation_id[1:],
    )


def _literal_str(node: ast.AST | None) -> str | None:
    if node is None:
        return None
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.Str):
        return node.s
    return None


def _is_sp_endpoint_call(node: ast.AST) -> bool:
    if isinstance(node, ast.Name):
        return node.id == "sp_endpoint"
    if isinstance(node, ast.Attribute):
        return node.attr == "sp_endpoint"
    return False


@dataclass(frozen=True)
class EndpointInfo:
    name: str
    method: str
    path: str


def _extract_endpoints(module_path: Path) -> dict[str, EndpointInfo]:
    source = module_path.read_text()
    tree = ast.parse(source, filename=str(module_path))
    endpoints: dict[str, EndpointInfo] = {}

    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        for item in node.body:
            if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            for decorator in item.decorator_list:
                if not isinstance(decorator, ast.Call):
                    continue
                if not _is_sp_endpoint_call(decorator.func):
                    continue
                path = None
                method = "GET"
                if decorator.args:
                    path = _literal_str(decorator.args[0])
                for kw in decorator.keywords:
                    if kw.arg == "path":
                        path = _literal_str(kw.value)
                    if kw.arg == "method":
                        method = (_literal_str(kw.value) or method).upper()
                if path is None:
                    continue
                endpoints[item.name] = EndpointInfo(
                    name=item.name,
                    method=method,
                    path=_normalize_path(path),
                )
    return endpoints


def _iter_model_operations(model_path: Path) -> Iterable[EndpointInfo]:
    data = json.loads(model_path.read_text())
    paths = data.get("paths") or {}
    for path, methods in paths.items():
        if not isinstance(methods, dict):
            continue
        for method, info in methods.items():
            if method.lower() not in HTTP_METHODS:
                continue
            if not isinstance(info, dict):
                continue
            operation_id = info.get("operationId")
            if not operation_id:
                continue
            yield EndpointInfo(
                name=_operation_name(operation_id),
                method=method.upper(),
                path=_normalize_path(path),
            )


def _resolve_client_module(
    service_versions: dict[str | None, Path],
    model_path: Path,
    service_name: str,
) -> Path | None:
    model_version = _parse_model_version(model_path.stem)
    if model_version in service_versions:
        return service_versions[model_version]
    if model_version is None:
        if None in service_versions:
            return service_versions[None]
        if "v1" in service_versions and model_path.stem == service_name:
            return service_versions["v1"]
    if len(service_versions) == 1:
        return next(iter(service_versions.values()))
    return None


@pytest.mark.parametrize(
    "package_root",
    [Path("sp_api/api"), Path("sp_api/asyncio/api")],
    ids=["sync", "async"],
)
def test_models_match_clients(package_root: Path):
    models_dir = _ensure_models_repo()
    service_index = _index_service_modules(package_root)
    errors: list[str] = []

    for model_path in sorted(models_dir.rglob("*.json")):
        if model_path.name in IGNORE_MODEL_FILES:
            continue
        service_name = _normalize_service_dir(model_path.parent.name)
        service_versions = service_index.get(service_name)
        if service_versions is None:
            errors.append(
                f"{model_path}: no client package for service '{service_name}'"
            )
            continue

        if service_name == "external_fulfillment":
            model_version = _parse_model_version(model_path.stem)
            module_path = None
            if model_path.stem.startswith("externalFulfillmentInventory"):
                module_path = (
                    package_root
                    / "external_fulfillment"
                    / f"inventory_{model_version.replace('-', '_')}.py"
                )
            elif model_path.stem.startswith("externalFulfillmentReturns"):
                module_path = (
                    package_root
                    / "external_fulfillment"
                    / f"returns_{model_version.replace('-', '_')}.py"
                )
            elif model_path.stem.startswith("externalFulfillmentShipments"):
                module_path = (
                    package_root
                    / "external_fulfillment"
                    / f"shipping_{model_version.replace('-', '_')}.py"
                )
            if module_path is not None and not module_path.exists():
                module_path = None
        else:
            module_path = _resolve_client_module(
                service_versions, model_path, service_name
            )
        if module_path is None:
            model_version = _parse_model_version(model_path.stem)
            errors.append(
                f"{model_path}: no client module for version {model_version!r} in '{service_name}'"
            )
            continue

        endpoint_keys = {
            (info.method, info.path) for info in _extract_endpoints(module_path).values()
        }
        for expected in _iter_model_operations(model_path):
            key = (expected.method, expected.path)
            if key not in endpoint_keys:
                errors.append(
                    f"{model_path}: missing endpoint {expected.method} {expected.path} in {module_path}"
                )

    assert not errors, "Model/client mismatches:\n" + "\n".join(errors)
