from __future__ import annotations

import enum
from typing import Any, Literal, TYPE_CHECKING, overload
from sp_api.util.versioned_client import VersionedClientMeta

from sp_api.base import Client

from .products_2022_05_01 import ProductsV20220501
from .products_v0 import ProductsV0


class ProductsVersion(str, enum.Enum):
    V0 = "v0"
    V_2022_05_01 = "2022-05-01"
    LATEST = "2022-05-01"


if TYPE_CHECKING:

    class _ProductsMeta(VersionedClientMeta):
        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[ProductsVersion.V_2022_05_01, ProductsVersion.LATEST, "2022-05-01"],
            **kwargs: Any,
        ) -> ProductsV20220501: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: Literal[ProductsVersion.V0, "v0"],
            **kwargs: Any,
        ) -> ProductsV0: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> ProductsV0: ...

        @overload
        def __call__(
            cls,
            *args: Any,
            version: str | ProductsVersion,
            **kwargs: Any,
        ) -> Client: ...


else:
    _ProductsMeta = VersionedClientMeta


class Products(Client, metaclass=_ProductsMeta):
    """Product Pricing API client.

    This class dispatches to a versioned Product Pricing API client.

    If you do not pass a version, the constructor returns the oldest supported implementation ("v0").
    """

    if TYPE_CHECKING:
        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[ProductsVersion.V_2022_05_01, ProductsVersion.LATEST, "2022-05-01"],
            **kwargs: Any,
        ) -> ProductsV20220501: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: Literal[ProductsVersion.V0, "v0"],
            **kwargs: Any,
        ) -> ProductsV0: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: None = None,
            **kwargs: Any,
        ) -> ProductsV0: ...

        @overload
        def __new__(
            cls,
            *args: Any,
            version: str | ProductsVersion,
            **kwargs: Any,
        ) -> Client: ...

    _DISPATCH = True

    _DEFAULT_VERSION = "v0"

    _VERSION_MAP = {
        "v0": ProductsV0,
        "2022-05-01": ProductsV20220501,
    }

    _VERSION_ALIASES = {
        "v0": "v0",
        "2022-05-01": "2022-05-01",
    }
