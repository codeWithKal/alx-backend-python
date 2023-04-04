#!/usr/bin/env python3
'''
a module for returning list of numbers generated asynchronously
'''
from typing import List
import importlib
async_generator = importlib.import_module('0-async_generator').async_generator


async def async_comprehension() -> List(float):
    '''
    a method returning 10 list of random float numbers
    '''
    return [i async for i in async_generator()]
