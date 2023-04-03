#!/usr/bin/env python3
""""
module that implement an async await function
"""
import asyncio
import random


async def wait_random(max_delay=10) -> float:
    """"
    a method that implements an async await function
    """
    seconds = random.uniform(0, max_delay)
    await asyncio.sleep(seconds)
    return seconds
