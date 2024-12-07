#!/usr/bin/env python3
import time
import asyncio
from typing import List

# Import wait_n using __import__
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the runtime for executing wait_n(n, max_delay).
    
    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay for wait_random.
    
    Returns:
        float: Average time per wait_random execution.
    """
    # Record the start time
    start_time = time.perf_counter()
    
    # Execute wait_n
    asyncio.run(wait_n(n, max_delay))
    
    # Record the end time
    end_time = time.perf_counter()
    
    # Calculate the total time and return average
    total_time = end_time - start_time
    return total_time / n


