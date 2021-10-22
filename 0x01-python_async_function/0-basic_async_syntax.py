#!/usr/bin/env python3
"""Module"""
from asyncio import sleep
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait random"""
    time = random.uniform(0, max_delay)
    await sleep(time)
    return time
