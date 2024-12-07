#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine, wait_random,
which waits for a random delay and returns the delay.
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds and then returns the delay.

    Args:
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        float: The random delay in seconds.
    """
    delay = random.uniform(0, max_delay)  # Generate a random float between 0 and max_delay
    await asyncio.sleep(delay)           # Pause execution for the delay
    return delay                          # Return the delay
