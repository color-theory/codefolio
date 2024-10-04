"""
simplehash.py
This module contains the simplehash_search function which is used
to search for an element in a SimpleHashTable.
"""
import random
import time
import numpy as np
from benchmark import run_timing_benchmark, BenchmarkConfig
from datastructures import SimpleHashTable
from reports import plot_time, PlotConfig


def simplehash_search(data: SimpleHashTable, target):
    """
    Search for an element in a SimpleHashTable

    Parameters:
    data: SimpleHashTable: The SimpleHashTable to search
    target: Any: The element to search for

    Returns:
    Any: The value of the element in the SimpleHashTable
    """
    return data[target]


def search_benchmark(data: SimpleHashTable):
    """
    Benchmark the simplehash_search function
    """
    target = random.choice(data.table)

    start_time = time.perf_counter()
    simplehash_search(data, target)
    elapsed_time = time.perf_counter() - start_time

    return elapsed_time


def data_setup(size):
    """
    Generate random data
    """
    data = SimpleHashTable(size)
    noise = random.sample(range(size), size)
    for i in noise:
        data[i] = i * 2

    return data


benchmark_config = BenchmarkConfig(
    name="SimpleHashTable Lookup",
    max_size=10000,
    iterations=500,
    resolution=100,
)

[times, sizes, total_time] = run_timing_benchmark(
    search_benchmark, data_setup, benchmark_config)

plot_config = PlotConfig(
    {
        "name": benchmark_config.name,
        "iterations": benchmark_config.iterations,
        "resolution": benchmark_config.resolution,
        "y_limit_min": np.float64(-.2e-5),
        "y_limit_max": np.float64(.5e-5),
    }
)

plot_time(times, sizes, total_time, plot_config)
