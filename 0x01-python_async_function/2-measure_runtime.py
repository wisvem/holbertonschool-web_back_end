#!/usr/bin/env python3
""" The basics of async """

from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure the runtime """
    return sum(run(wait_n(n, max_delay)))/n
