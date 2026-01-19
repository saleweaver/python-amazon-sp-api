import hashlib


def build_cache_key(refresh_token, token_flavor=""):
    return "access_token_" + hashlib.md5(
        (token_flavor + (refresh_token or "__grantless__")).encode("utf-8"),
        usedforsecurity=False,
    ).hexdigest()


def build_refresh_token_data(credentials, grant_type):
    return {
        "grant_type": grant_type,
        "client_id": credentials.client_id,
        "refresh_token": credentials.refresh_token,
        "client_secret": credentials.client_secret,
    }


def build_grantless_data(credentials, scope_value):
    return {
        "grant_type": "client_credentials",
        "client_id": credentials.client_id,
        "scope": scope_value,
        "client_secret": credentials.client_secret,
    }


def build_auth_code_request_body(credentials, auth_code):
    return {
        "grant_type": "authorization_code",
        "code": auth_code,
        "client_id": credentials.client_id,
        "client_secret": credentials.client_secret,
    }


def build_headers(user_agent, content_type):
    return {"User-Agent": user_agent, "content-type": content_type}
