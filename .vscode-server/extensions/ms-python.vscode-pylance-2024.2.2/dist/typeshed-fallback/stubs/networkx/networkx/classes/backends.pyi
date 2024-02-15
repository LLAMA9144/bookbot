from _typeshed import Incomplete
from collections.abc import Callable

__all__ = ["_dispatch", "_mark_tests"]

class PluginInfo:
    def __init__(self) -> None: ...
    def __bool__(self) -> bool: ...
    @property
    def items(self): ...
    def __contains__(self, name) -> bool: ...
    def __getitem__(self, name): ...

def _dispatch(func: Incomplete | None = None, *, name: Incomplete | None = None) -> Callable[..., Incomplete]: ...
def _mark_tests(items) -> None: ...
