#!/usr/bin/env python3
"""module"""
import asyncio
from random import uniform
from typing import AsyncIterator


async def async_generator() -> AsyncIterator[float]:
    """function"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
