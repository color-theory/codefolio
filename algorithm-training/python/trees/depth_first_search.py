"""
depth_first_search.py

This module contains the depth_first_search function which is used
to search for an element in a graph using depth-first search.
"""
import random
import time
from benchmark import run_timing_benchmark, BenchmarkConfig
from reports import plot_time, PlotConfig


def depth_first_search(data, start, target):
    """
    Search for an element in a graph using depth-first search.

    Parameters:
    data: Dict: The graph to search
    start: Any: The starting element
    target: Any: The element to search for
    """
    if start == target:
        return True
    for node in data[start]:
        depth_first_search(data, node, target)
    return False


def search_benchmark(data):
    """
    Benchmark the breadth_first_search function
    """
    target = random.choice(range(len(data)))
    start = 0
    start_time = time.perf_counter()
    depth_first_search(data, start, target)
    elapsed_time = time.perf_counter() - start_time

    return elapsed_time


def data_setup(size):
    """
    Generate a tree of the correct size.
    Each node (except the root) has exactly one parent.
    """
    graph = {}
    for i in range(size):
        graph[i] = []

    for i in range(1, size):
        parent = random.randint(0, i - 1)
        graph[parent].append(i)
    return graph


benchmark_config = BenchmarkConfig(
    name="Depth First Search",
    max_size=10000,
    iterations=100,
    resolution=50,
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
