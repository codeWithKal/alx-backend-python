#!/usr/bin/env python3
'''
A module for concurrent coroutines
'''
import asyncio as ao
from typing import List

wait_random = __import__('0-basic_async_syntax.py').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    a method returning list of second delays
    '''
    waiting_seconds = await ao.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n))))
    return sorted(waiting_seconds)
