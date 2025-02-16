from durable_dot_dict.dot import Dot
from durable_dot_dict.dotdict import DotDict

class X:
    x = 100

def test_dot():
    dotdict = DotDict({"a": {"b": 1, "c": [{"d": 2, "e": X()}]}})
    dot = Dot(dotdict)
    # assert dot.a.c == [{"d": 2, "e": X()}]
    print(dot['a'])
    print(dot.a.c[0])
    print(dot.a.c[0].d)
    print(dot.a.c[0].e.x)

    dot = Dot()
    dot.a = 1
    dot.b = {}
    dot.b.a = 1
    print(dot)
