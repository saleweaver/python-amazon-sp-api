import json
from datetime import datetime, timezone
from json import JSONDecodeError

from .ApiResponse import ApiResponse
from .exceptions import get_exception_for_code


def resolve_method(params, data):
    if params is None:
        params = {}
    if data is None:
        data = {}
    method = params.pop(
        "method", data.pop("method", "GET") if isinstance(data, dict) else "GET"
    )
    return method, params, data


def check_version(path, version):
    if "<version>" not in path:
        return path
    return path.replace("<version>", version)


def add_marketplaces(method, marketplace_id, data):
    post_keys = ["marketplaceIds", "MarketplaceIds"]
    get_keys = ["MarketplaceId", "MarketplaceIds", "marketplace_ids", "marketplaceIds"]

    if method == "POST":
        if any(key in data.keys() for key in post_keys):
            return
        data.update(
            {
                key: marketplace_id if not key.endswith("s") else [marketplace_id]
                for key in post_keys
            }
        )
        return
    if any(key in data.keys() for key in get_keys):
        return
    data.update(
        {
            key: marketplace_id if not key.endswith("s") else [marketplace_id]
            for key in get_keys
        }
    )


def build_headers(endpoint, user_agent, access_token, content_type="application/json"):
    return {
        "host": endpoint[8:],
        "user-agent": user_agent,
        "x-amz-access-token": access_token,
        "x-amz-date": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "content-type": content_type,
    }


def prepare_request(
    *,
    method,
    endpoint,
    path,
    params,
    data,
    headers,
    add_marketplace,
    marketplace_id,
    version,
):
    if add_marketplace:
        add_marketplaces(method, marketplace_id, data if method in ("POST", "PUT") else params)
    url = endpoint + check_version(path, version)
    content = (
        json.dumps(data) if data and method in ("POST", "PUT", "PATCH") else None
    )
    return {
        "method": method,
        "url": url,
        "params": params,
        "content": content,
        "headers": headers,
    }


def parse_response(res, *, method, res_no_data=False, bulk=False, wrap_list=False):
    if (method == "DELETE" or res_no_data) and 200 <= res.status_code < 300:
        try:
            js = res.json() or {}
        except JSONDecodeError:
            js = {"status_code": res.status_code}
    else:
        try:
            js = res.json() or {}
        except JSONDecodeError:
            js = {}

    if isinstance(js, list):
        if wrap_list:
            js = dict(payload=js)
        else:
            js = js[0]

    error = js.get("errors", None)
    if error:
        exception = get_exception_for_code(res.status_code)
        raise exception(error, headers=res.headers)

    return ApiResponse(**js, headers=res.headers)
