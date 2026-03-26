from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `prediction_guard.resources` module.

    This is used so that we can lazily import `prediction_guard.resources` only when
    needed *and* so that users can just import `prediction_guard` and reference `prediction_guard.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("prediction_guard.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
