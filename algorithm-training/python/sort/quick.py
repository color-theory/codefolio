"""
quick.py

This module contains the quick_sort function which is used
to sort a list of elements by divide and conquer. 
"""
import random
import time
from benchmark import run_timing_benchmark, BenchmarkConfig
from reports import plot_time, PlotConfig


def quick_sort(data):
    """
    Sort a list of elements by divide and conquer.

    Parameters:
    data: List: The list of elements to sort

    Returns:
    List: The sorted list of elements
    """
    if len(data) < 2:
        return data
    if len(data) == 2:
        return [min(data), max(data)]

    pivot = len(data) // 2
    lt_pivot = [x for x in data if x < data[pivot]]
    eq_pivot = [x for x in data if x == data[pivot]]
    gt_pivot = [x for x in data if x > data[pivot]]

    return quick_sort(lt_pivot) + eq_pivot + quick_sort(gt_pivot)


def search_benchmark(data):
    """
    Benchmark the quick_sort function
    """
    start_time = time.perf_counter()
    quick_sort(data)
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time


def data_setup(size):
    """
    Generate random data
    """
    data = random.sample(range(size), size)
    return data


benchmark_config = BenchmarkConfig(
    name="Quick Sort",
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
