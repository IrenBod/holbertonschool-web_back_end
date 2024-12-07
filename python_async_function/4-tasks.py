#!/usr/bin/env python3
import asyncio
from typing import List

# Import task_wait_random using __import__
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times and return a list of delays in ascending order.
    
    Args:
        n (int): Number of times to call task_wait_random.
        max_delay (int): Maximum delay for task_wait_random.
    
    Returns:
        List[float]: List of delays sorted in ascending order.
    """
    # Create a list of tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    # Process tasks as they complete
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    
    return delays
