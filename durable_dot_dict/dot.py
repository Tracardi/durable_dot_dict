from typing import MutableMapping, Union, List, Any, Dict


class DotList(list):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        if isinstance(value, dict):
            return Dot(value)
        return value

    def flatten(self, allow: List[str] = None) -> List[Dict[str, Any]]:
        result = [item.flat() for item in self]
        if allow is not None:
            result = [
                {k: v for k, v in d.items() if k.startswith(tuple(allow))}
                for d in result
            ]
            # remove empty dicts
            result = [d for d in result if d]
        return result

    def merge(self, allow: List[str] = None, allow_null_value:bool=True) -> dict:
        list = self.flatten(allow)
        result = {}
        if allow_null_value:
            for item in list:
                result.update(item)
        else:
            for item in list:
                for k, v in item.items():
                    if v is not None:
                        result[k] = v
        return result


class Dot(dict):

    def __getattr__(self, item) -> Union['Dot', DotList]:
        value = self[item]
        if isinstance(value, dict):
            return Dot(value)
        elif isinstance(value, list):
            return DotList(value)
        return value
