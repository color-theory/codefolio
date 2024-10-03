"""
breadth_first.py

This module contains the breadth_first_search function which is used
to search for an element in a graph using breadth-first search.
"""
import random
import time
from collections import deque
from benchmark import run_timing_benchmark, BenchmarkConfig
from reports import plot_time, PlotConfig


def breadth_first_search(data, target, start):
    """
    Search for an element in a graph using breadth-first search.

    Parameters:
    data: Dict: The graph to search
    target: Any: The element to search for
    start: Any: The starting element

    Returns:
    Any: The number of steps to find the element
    """
    search_queue = deque([start])
    searched = set()
    steps = 0
    while search_queue:
        steps += 1
        searching = search_queue.popleft()
        if searching not in searched:
            if searching == target:
                return steps
            search_queue += data[searching]
            searched.add(searching)
    return -1


def search_benchmark(data):
    """
    Benchmark the breadth_first_search function
    """
    target = random.choice(range(len(data)))
    start = random.choice(range(len(data)))
    start_time = time.perf_counter()
    breadth_first_search(data, target, start)
    elapsed_time = time.perf_counter() - start_time

    return elapsed_time


def data_setup(size):
    """
    Generate random graph data. It is important to ensure that the graph
    is balanced by limiting the number of edges to prevent the search
    from becoming too slow over time.
    """
    graph = {}
    max_edges = 3
    for i in range(size):
        graph[i] = []
        edge_count = 0
        for j in range(i + 1, size):
            if edge_count >= max_edges:
                break
            if random.random() < .3:
                edge_count += 1
                graph[i] = graph[i] + [j]

    return graph


benchmark_config = BenchmarkConfig(
    name="Breadth First Search",
    max_size=10000,
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
