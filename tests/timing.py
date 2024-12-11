import os
from dataclasses import dataclass
from functools import wraps
from time import time

OUTPUT_TIME = os.environ.get('CIMGRAPH_TIME', False)

@dataclass
class Counts:
    hits: int = 0
    total: float = 0.0

timing_keys: dict[str, Counts] = {}

def print_timing():
    for k, v in timing_keys.items():
        print(k, v)

def clear_timing():
    timing_keys.clear()


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        if OUTPUT_TIME:
            if f.__name__ not in timing_keys:
                timing_keys[f.__name__] = Counts()
            ts = time()
            result = f(*args, **kw)
            te = time()
            timing_keys[f.__name__].hits +=1
            timing_keys[f.__name__].total += te-ts
            return result
        else:
            return f(*args, **kw)
    return wrap
