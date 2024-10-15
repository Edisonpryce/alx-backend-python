#!/usr/bin/env python3
"""Task 0
"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """The coroutine will loop 10 times, each time asynchronously
    wait 1 sec
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
