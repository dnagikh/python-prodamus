import collections
from copy import deepcopy
import json
import hmac
import hashlib
import re
from urllib.parse import parse_qsl


class ProdamusPy:
    def __init__(self, secret):
        self.secret = secret
        
    def sign(self, data: dict):
        obj_json = json.dumps(data, ensure_ascii=False, separators=(',', ':'), sort_keys=True)

        return hmac.new(bytes(self.secret, 'utf-8'),
                        msg=bytes(obj_json, 'utf-8'),
                        digestmod=hashlib.sha256).hexdigest()
    
    def verify(self, obj: dict, sign: str):
        _sign = self.sign(obj)

        return _sign and (_sign == sign.lower())
    
    def parse(self, body: str):
        payload = dict(parse_qsl(body, keep_blank_values=True, strict_parsing=True, errors='strict'))
        payload_dict = self.__php2dict(payload)

        return payload_dict
    
    def __php2dict(self, array: dict):
        dct = {}
        for k, v in array.items():
            m = re.fullmatch('([^\[]+)(\[.+\])', k)
            if m:
                idx = [m.group(1)] + list(re.findall('\[([^\]]+)\]', m.group(2)))
                subdct = self.__dict_build(idx, v)
            else:
                subdct = {k: v}
            dct = self.__dict_merge(dct, subdct)
        return dct
    
    def __dict_build(self, idx, value):
        value = deepcopy(value)
        if len(idx):
            i = idx.pop(0)
            if re.fullmatch('[0-9]+', i):
                return [{} for d in range(int(i))] + [self.__dict_build(idx, value)]
            else:
                return {i: self.__dict_build(idx, value)}
        else:
            return value
    
    # https://gist.github.com/angstwad/bf22d1822c38a92ec0a9?permalink_comment_id=3305932#gistcomment-3305932
    def __dict_merge(self, dct: dict, merge_dct: dict):
        dct = deepcopy(dct)
        for k, v in merge_dct.items():
            if not dct.get(k):
                dct[k] = deepcopy(v)
            elif k in dct and type(v) != type(dct[k]):
                raise TypeError(f"Overlapping keys exist with different types: original is {type(dct[k])}, new value is {type(v)}")
            elif isinstance(dct[k], dict) and isinstance(merge_dct[k], collections.abc.Mapping):
                dct[k] = self.__dict_merge(dct[k], merge_dct[k])
            elif isinstance(v, list):
                for li, lv in enumerate(v):
                    if len(dct[k]) <= li:
                        dct[k].append(lv)
                    else:
                        dct[k][li] = self.__dict_merge(dct[k][li], lv)
            else:
                dct[k] = v
        return dct