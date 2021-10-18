#!/usr/bin/env python3
"""module"""

from typing import Any, Iterable, List, Sequence, Tuple, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """function"""
    if lst:
        return lst[0]
    else:
        return None
