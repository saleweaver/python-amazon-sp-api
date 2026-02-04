from __future__ import annotations

from typing import Any


class VersionedClientMeta(type):
    """Metaclass that dispatches construction to a version-specific implementation.

    This keeps the call-site ergonomic (`Client(version=...)`) while allowing a single
    place to implement the dispatch logic.

    Subclasses should define:
      - `_VERSION_MAP`: mapping of normalized version strings to implementation classes
      - `_VERSION_ALIASES` (optional): mapping of alias strings to normalized versions
      - `_DEFAULT_VERSION`: default version when none is provided

    Front classes must set `_DISPATCH = True` in their class body.
    """

    def __call__(cls, *args: Any, **kwargs: Any):
        version = kwargs.pop("version", None)

        # Only dispatch for the public front class itself.
        if cls.__dict__.get("_DISPATCH", False):
            # Backwards-compatible default: if no version is provided, return the
            # oldest supported implementation.
            v_raw = version if version is not None else getattr(cls, "_DEFAULT_VERSION", None)
            if v_raw is None:
                return super().__call__(*args, **kwargs)

            v_raw = getattr(v_raw, "value", v_raw)
            v = str(v_raw)
            aliases: dict[str, str] = getattr(cls, "_VERSION_ALIASES", {})
            v_norm = aliases.get(v, v)

            impl_map: dict[str, type] = getattr(cls, "_VERSION_MAP", {})
            impl = impl_map.get(v_norm)
            if impl is not None:
                return impl(*args, **kwargs)

            supported = ", ".join(sorted(impl_map.keys()))
            raise ValueError(f"Unsupported version {v!r}. Supported: {supported}")

        return super().__call__(*args, **kwargs)
