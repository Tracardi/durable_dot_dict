from durable_dot_dict.collection import DotDictStream
from durable_dot_dict.dotdict import DotDict


class FlatSession(DotDict):
    pass


def test_collection_callables():
    col = DotDictStream([
        DotDict({"id": [1, 2], "x": "a"}),
        DotDict({"id": [2]})
    ])

    result = (col << {"id": lambda x: sum(x)}).list()
    assert result[0]['id'] == 3
    assert result[1]['id'] == 2

    # wrapped = (col >> {
    #         "a": "id"
    #     } >> {"b": "a"} << {"c": 1}).first(FlatSession)
    # print(type(wrapped), wrapped)

    # print(wrapped.list())
    # wrapped /= FlatSession
    # print(wrapped)


    # print(wrapped.first())  # Output: 1
    # print(wrapped.last())   # Output: 5
    # print(wrapped.list())  # Output: [1, 2, 3, 4, 5]


