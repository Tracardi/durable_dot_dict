from typing import Any, Callable


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

