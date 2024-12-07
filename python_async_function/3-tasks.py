#!/usr/bin/env python3
import asyncio
from typing import Any

# Import wait_random from 0-basic_async_syntax using __import__
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task for wait_random.
    
    Args:
        max_delay (int): Maximum delay for wait_random.
    
    Returns:
        asyncio.Task: A task wrapping wait_random.
    """
    # Create and return the asyncio.Task
    return asyncio.create_task(wait_random(max_delay))
