#!/usr/bin/env python3
'''
Task 0
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    A method that performs an async generator
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.rando() * 10
