#!/usr/bin/env python3
"""Task 1: Async Comprehensions
"""

import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """Creates a list of 10 numbers from a 10-number generator.
    """
    return [rand async for rand in async_generator()]
