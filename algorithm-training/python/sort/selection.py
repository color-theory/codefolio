"""
selection.py

This module contains the selection function which is used
to sort a list of elements sequentially.
"""
import random
import time
from benchmark import run_timing_benchmark, BenchmarkConfig
from reports import plot_time, PlotConfig


def selection_sort(data):
    """
    Sort a list of elements sequentially

    Parameters:
    data: List: The list of elements to sort

    Returns:
    List: The sorted list of elements
    """
    for i in range(len(data)):
        lowest_number_index = i
        for j in range(i, len(data)):
            if data[j] < data[lowest_number_index]:
                lowest_number_index = j
        temp = data[i]
        data[i] = data[lowest_number_index]
        data[lowest_number_index] = temp
    return data


def search_benchmark(data):
    """
    Benchmark the sequential_sort function
    """
    start_time = time.perf_counter()
    selection_sort(data)
    elapsed_time = time.perf_counter() - start_time

    return elapsed_time


def data_setup(size):
    """
    Generate random data
    """
    data = random.sample(range(size), size)
    return data


benchmark_config = BenchmarkConfig(
    name="Selection Sort",
    max_size=1000,
    iterations=100,
    resolution=100,
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
