#!/usr/bin/env python3
"""
Module containing the wait_n coroutine.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times and return a list of delays in ascending order.

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        List[float]: Sorted list of delays.
    """
    # Create tasks for wait_random
    tasks = [wait_random(max_delay) for _ in range(n)]
    
    # Wait for all tasks to complete and collect their results
    delays = [await task for task in asyncio.as_completed(tasks)]
    
    # Return the sorted list of delays
    return sorted(delays)
