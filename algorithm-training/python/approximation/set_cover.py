"""
set_cover.py
This module contains an implementation of the set cover problem and a greedy
approximation algorithm for solving it.
"""
from typing import List, Set
import random
import time
from benchmark import run_timing_benchmark, BenchmarkConfig
from reports import plot_time, PlotConfig


def set_cover(universe: Set[int], subsets: List[Set[int]]) -> List[Set[int]]:
    """
    Find the minimum number of subsets that cover the universe

    Parameters:
    universe: Set[int]: The universe to cover
    subsets: List[Set[int]]: The subsets to use for covering

    Returns:
    List[Set[int]]: The minimum number of subsets that cover the universe
    """
    covered = set()
    cover = []

    while covered != universe:
        subset = max(subsets, key=lambda s: len(s - covered))
        cover.append(subset)
        covered |= subset
    return cover


def set_cover_benchmark(data):
    """
    Benchmark the binary search function
    """
    start_time = time.perf_counter()
    set_cover(**data)
    elapsed_time = time.perf_counter() - start_time

    return elapsed_time


def data_setup(size):
    """
    Generate random data
    """
    universe = set(range(size))
    subsets = []
    for item in universe:
        subsets.append(set([item]))
        additional = set(random.sample(
            list(universe), random.randint(1, size // 2)))
        subsets.append(additional)

    data = {"universe": set(universe), "subsets": subsets}
    return data


benchmark_config = BenchmarkConfig(
    name="Set Cover Approximation",
    max_size=500,
    iterations=100,
    resolution=20,
)

[times, sizes, total_time] = run_timing_benchmark(
    set_cover_benchmark, data_setup, benchmark_config)

plot_config = PlotConfig(
    {
        "name": benchmark_config.name,
        "iterations": benchmark_config.iterations,
        "resolution": benchmark_config.resolution,
    }
)

plot_time(times, sizes, total_time, plot_config)
