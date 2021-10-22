#!/usr/bin/env python3
"""Module"""

from asyncio import sleep
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """wait random"""
    time = uniform(0, max_delay)
    await sleep(time)
    return time
