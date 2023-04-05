#!/usr/bin/env python3
'''
Solution for task 2.
'''
import asyncio
import time
from importlib import import_module


async_comprehension = import_module('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    executes 4 tasks simultanously.
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time