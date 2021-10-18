#!/usr/bin/env python3
"""module"""
from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function"""
    return tuple([k, v*v])
