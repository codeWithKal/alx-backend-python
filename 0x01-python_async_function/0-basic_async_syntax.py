#!/usr/bin/env python3
""""
module that implement an async await function
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """"
    a method that implements an async await function
    """
    seconds = random.random() * max_delay
    await asyncio.sleep(seconds)
    return seconds
