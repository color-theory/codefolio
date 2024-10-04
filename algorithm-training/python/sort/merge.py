"""
merge.py
this module contains the merge_sort function which is used
to sort a list of elements by dividing the list into two halves
and then merging the sorted halves.
"""
import random
import time
from benchmark import run_timing_benchmark, BenchmarkConfig
from reports import plot_time, PlotConfig


def merge_sort(arr):
    """
    Sort a list of elements by dividing the list into two halves
    and then merging the sorted halves.

    Parameters:
    arr: List: The list of elements to sort

    Returns:
    List: The sorted list of elements
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        if i < len(left_half):
            arr[k:] = left_half[i:]

        if j < len(right_half):
            arr[k:] = right_half[j:]

    return arr


def search_benchmark(data):
    """
    Benchmark the merge_sort function
    """
    start_time = time.perf_counter()
    merge_sort(data)
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time


def data_setup(size):
    """
    Generate random data
    """
    data = random.sample(range(size), size)
    return data


benchmark_config = BenchmarkConfig(
    name="Merge Sort",
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
