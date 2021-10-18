#!/usr/bin/python3
"""module"""
from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return tuple([k, v*v])
