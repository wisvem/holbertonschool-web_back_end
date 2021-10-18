#!/usr/bin/env python3
"""module"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function"""
    return [(i, len(i)) for i in lst]
