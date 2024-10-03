"""
sequential.py
This module contains the sequential_search function which is used
to search for an element in a list sequentially.
"""
import random
import time
from benchmark import run_timing_benchmark, BenchmarkConfig
from reports import plot_time, PlotConfig


def sequential_search(data, target):
    """
    Search for an element in a list sequentially

    Parameters:
    data: List: The list to search
    target: Any: The element to search for

    Returns:
    int: The index of the element in the list
    """
    for i, item in enumerate(data):
        if item == target:
            return i
    return -1


def search_benchmark(data):
    """
    Benchmark the sequential search function
    """
    target = random.choice(data)
    start_time = time.perf_counter()
    sequential_search(data, target)
    elapsed_time = time.perf_counter() - start_time

    return elapsed_time


def data_setup(size):
    """
    Generate random data
    """
    data = random.sample(range(size), size)
    return data


benchmark_config = BenchmarkConfig(
    {
        "name": "Sequential Search",
        "max_size": 20000,
        "iterations": 100,
        "resolution": 100,
    }
)

[times, sizes, total_time] = run_timing_benchmark(
    search_benchmark, data_setup, benchmark_config)

plot_config = PlotConfig(
    {
        "name": benchmark_config.name,
        "iterations": benchmark_config.iterations,
        "resolution": benchmark_config.resolution,
        "trend": True,
    }
)

plot_time(times, sizes, total_time, plot_config)
