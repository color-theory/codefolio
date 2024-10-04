"""
breadth_first_traversal.py

This module contains the breadth_first_traversal function which is used
to traverse a graph using breadth-first approach.
"""
import random
import time
from collections import deque
from benchmark import run_timing_benchmark, BenchmarkConfig
from reports import plot_time, PlotConfig


def breadth_first_traverse(data):
    """
    traverse the entire tree using breadth-first approach

    Parameters:
    data: Dict: The tree to traverse
    """
    search_queue = deque([0])
    steps = 0
    while search_queue:
        steps += 1
        searching = search_queue.popleft()
        search_queue += data[searching]
    return -1


def search_benchmark(data):
    """
    Benchmark the breadth_first_search function
    """
    start_time = time.perf_counter()
    breadth_first_traverse(data)
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
    name="Breadth First Traversal",
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
