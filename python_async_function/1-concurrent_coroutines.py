#!/usr/bin/env python3
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times and return a list of delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    # Process tasks as they are completed
    for task in asyncio.as_completed(tasks):
        delay = await task
        # Insert into the correct position without using sort()
        for i, d in enumerate(delays):
            if delay < d:
                delays.insert(i, delay)
                break
        else:
            delays.append(delay)
    
    return delays
