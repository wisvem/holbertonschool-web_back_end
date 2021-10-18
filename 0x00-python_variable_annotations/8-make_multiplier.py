#!/usr/bin/python3
"""module"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """outter function"""
    def func(n: float) -> float:
        """inner function"""
        return float(n * multiplier)

    return func
