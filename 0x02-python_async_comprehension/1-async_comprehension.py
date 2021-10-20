#!/usr/bin/env python3
"""Module"""

import asyncio
from random import uniform

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """function"""
    result = []
    async for i in async_generator():
        result.append(i)
    return(result)
