from durable_dot_dict.collection import FlatCollection
from durable_dot_dict.dotdict import DotDict


def test_collection():
    col = FlatCollection([
        DotDict({"id": 1}),
        DotDict({"id": 2})
    ])
    x = col >> {
        "a": "id"
    }
    print(list(x))

