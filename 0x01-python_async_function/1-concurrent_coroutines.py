#!/usr/bin/env python3
"""concurrent_coroutines"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int,  max_delay: int) -> List[float]:
    """create 'n' tasks and return results in order of resolution

    Args:
        n (int): number of process to be spawn
        max_delay (int): delay of answer

    Returns:
        List[float]: results in order of resolution
    """
    # create list where all the task results will be saved
    tasks_done = list()
    # create task_process list to be called concurrently
    tasks_process = list()
    # create task to be done and add call back function that
    # will append the future object result to tasks_done list
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        task.add_done_callback(
            lambda future_obj: tasks_done.append(future_obj.result()))
        tasks_process.append(task)
    # start tasks concurrently and wait for the results
    # to be saved in tasks_done
    await asyncio.gather(*tasks_process)
    return tasks_done
