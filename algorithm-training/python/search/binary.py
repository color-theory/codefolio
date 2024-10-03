"""
binary.py
This module contains the binary_search function which is used
to search for an element in a list using binary search.
"""
import random
import time
from benchmark import run_timing_benchmark, BenchmarkConfig
from reports import plot_time, PlotConfig


def binary_search(data, target):
    """
    Search for an element in a list using binary search

    Parameters:
    data: List: The list to search
    target: Any: The element to search for

    Returns:
    int: The index of the element in the list
    """
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def search_benchmark(data):
    """
    Benchmark the binary search function
    """
    target = random.choice(data)
    start_time = time.perf_counter()
    binary_search(data, target)
    elapsed_time = time.perf_counter() - start_time

    return elapsed_time


def data_setup(size):
    """
    Generate random data
    """
    data = random.sample(range(size), size)
    return data


benchmark_config = BenchmarkConfig(
    name="Binary Search",
    max_size=50000,
    iterations=100,
    resolution=500,
)

[times, sizes, total_time] = run_timing_benchmark(
    search_benchmark, data_setup, benchmark_config)

plot_config = PlotConfig(
    {
        "name": benchmark_config.name,
        "iterations": benchmark_config.iterations,
        "resolution": benchmark_config.resolution,
    }
)

plot_time(times, sizes, total_time, plot_config)
