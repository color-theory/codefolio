"""
bubble.py
"""
import random
import time
from benchmark import run_timing_benchmark, BenchmarkConfig
from reports import plot_time, PlotConfig


def bubble_sort(data):
    """
    Sort a list of elements by bubbling

    Parameters:
    data: List: The list of elements to sort

    Returns:
    List: The sorted list of elements
    """
    for i in range(len(data)):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def search_benchmark(data):
    """
    Benchmark the quick_sort function
    """
    start_time = time.perf_counter()
    bubble_sort(data)
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time


def data_setup(size):
    """
    Generate random data
    """
    data = random.sample(range(size), size)
    return data


benchmark_config = BenchmarkConfig(
    name="Bubble Sort",
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
