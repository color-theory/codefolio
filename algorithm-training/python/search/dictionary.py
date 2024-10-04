"""
dictionary.py
This module contains the dictionary_search function which is used
to search for an element in a dictionary.
"""
import random
import time
from benchmark import run_timing_benchmark, BenchmarkConfig
from reports import plot_time, PlotConfig


def dictionary_search(data, target):
    """
    Search for an element in a dictionary

    Parameters:
    data: Dict: The dictionary to search
    target: Any: The element to search for

    Returns:
    Any: The value of the element in the dictionary
    """
    return data[target]


def search_benchmark(data):
    """
    Benchmark the dictionary search function
    """
    keys = list(data.keys())
    target = random.choice(keys)

    start_time = time.perf_counter()
    dictionary_search(data, target)
    elapsed_time = time.perf_counter() - start_time

    return elapsed_time


def data_setup(size):
    """
    Generate random data
    """
    data = {}
    noise = random.sample(range(size), size)
    for i in noise:
        data[i] = i * 2

    return data


benchmark_config = BenchmarkConfig(
    name="Dictionary Lookup",
    max_size=20000,
    iterations=200,
    resolution=200,
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
