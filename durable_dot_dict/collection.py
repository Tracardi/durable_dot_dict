from typing import Any, Callable, List, Iterable
from typing import Generator, Iterator, TypeVar
from durable_dot_dict.dotdict import DotDict

T = TypeVar("T", bound=DotDict)


def first(*args: Callable[[], Any]) -> Any:
    for func in args:
        try:
            return func()
        except Exception:
            continue
    raise ValueError("All provided callables failed.")


def first_not_none(*args: Callable[[], Any]) -> Any:
    for func in args:
        try:
            result = func()
            if result is None:
                continue
            return result
        except Exception:
            continue
    raise ValueError("All provided callables failed.")


class FlatCollection:

    def __init__(self, collection: Iterable[T]):
        self.collection = collection

    def __lshift__(self, other) -> Generator[T, None, None]:
        for item in self.collection:
            yield item << other

    def __rshift__(self, other) -> Generator[T, None, None]:
        for item in self.collection:
            yield item >> other
