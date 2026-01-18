from collections import abc
from datetime import datetime


def to_csv(value, mapper=None):
    if value and isinstance(value, abc.Iterable) and not isinstance(value, str):
        if mapper:
            value = [mapper(item) for item in value]
        return ",".join(value)
    return value


def normalize_csv_param(kwargs, key, mapper=None):
    if key in kwargs:
        value = to_csv(kwargs.get(key), mapper)
        if value is not None:
            kwargs[key] = value
    return kwargs


def normalize_included_data(kwargs, enum_cls=None, key="includedData"):
    def mapper(value):
        if enum_cls and isinstance(value, enum_cls):
            return value.value
        return value

    return normalize_csv_param(kwargs, key, mapper)


def normalize_marketplace_ids(kwargs, marketplace_cls=None, key="marketplaceIds"):
    def mapper(value):
        if marketplace_cls and isinstance(value, marketplace_cls):
            return value.marketplace_id
        return value

    return normalize_csv_param(kwargs, key, mapper)


def normalize_datetime_kwargs(kwargs, keys):
    for key in keys:
        if isinstance(kwargs.get(key), datetime):
            kwargs[key] = kwargs.get(key).isoformat()
    return kwargs


def encode_kwarg(kwargs, key, encoder):
    if key in kwargs:
        kwargs[key] = encoder(kwargs.pop(key))
    return kwargs


def should_add_marketplace(kwargs, token_key="nextToken"):
    return token_key not in kwargs


def ensure_csv(value, mapper=None):
    return to_csv(value, mapper)
