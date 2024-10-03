"""
timing.py
This module contains the run_timing_benchmark function which is used
to run a timing benchmark on a given algorithm.

Functions:
- run_timing_benchmark(
    benchmark,
    data_setup,
    max_size=1000,
    iterations=100,
    resolution=50,
    algo_name="algorithm"
) -> Tuple[List[float], List[int], float]: Run a timing benchmark on an algo
"""
import numpy as np
from progressbar import print_progress


class BenchmarkConfig:
    """
    Benchmark configuration class
    """

    def __init__(self, max_size, iterations, resolution, name):
        """
        Initialize the BenchmarkConfig class

        Parameters:
        max_size: int: The maximum size of the data
        iterations: int: The number of steps between min and max size
        resolution: int: The number of times to run the benchmark for each step
        name: str: The name of the algorithm
        """
        self.max_size = max_size
        self.iterations = iterations
        self.resolution = resolution
        self.name = name
        self.validate()

    def __str__(self):
        return (
            f"max_size: {self.max_size}, "
            f"iterations: {self.iterations}, "
            f"resolution: {self.resolution}, "
            f"name: {self.name}"
        )

    def validate(self):
        """
        Validate the configuration
        """
        if self.max_size <= 0:
            raise ValueError("max_size must be greater than 0.")
        if self.resolution <= 0:
            raise ValueError("resolution must be a positive integer.")
        if self.iterations <= 0:
            raise ValueError("iterations must be a positive integer.")


def filter_outliers(average_times_per_size):
    """
    filter_outliers is used to filter out the outliers from the data

    Parameters:
    average_times_per_size: List[List[float, int]]: The average times for each size

    Returns:
    Tuple[
    filtered_times: List[float] The avg time for the algorithm to run per size
    filtered_sizes: List[int] The size of the data at each step
    """
    times = [x[0] for x in average_times_per_size]
    sizes = [x[1] for x in average_times_per_size]

    mean_time = np.mean(times)
    std_dev_time = np.std(times)
    lower_bound = mean_time - 2 * std_dev_time
    upper_bound = mean_time + 2 * std_dev_time

    non_outlier_indices = np.where(
        (times >= lower_bound) & (times <= upper_bound))[0]
    filtered_times = [times[i] for i in non_outlier_indices]
    filtered_sizes = [sizes[i] for i in non_outlier_indices]

    return filtered_times, filtered_sizes


def run_timing_benchmark(benchmark, data_setup, config: BenchmarkConfig):
    """
    run_timing_benchmark is used to run a timing benchmark on a given algorithm

    Parameters:
    benchmark: Callable: The function to benchmark
    data_setup: Callable: The function to setup the data
    config: BenchmarkConfig: The configuration for the benchmark

    Returns:
    Tuple[
    filtered_times: List[float] The avg time for the algorithm to run per size
    filtered_sizes: List[int] The size of the data at each step
    total_time: float The total time taken to run the benchmark
    """
    print("Running benchmark...")
    try:
        config.validate()
    except ValueError as e:
        print(f"Error: {e}")
        return [], [], 0
    growth_rate = config.max_size // config.iterations
    size = growth_rate
    avg_times_per_size = []
    total_time = 0
    while size <= config.max_size:
        elapsed_times = []
        print("\r setting up data...", end="")
        data = data_setup(size)
        for x in range(config.resolution):
            elapsed = benchmark(data)
            elapsed_times.append(elapsed)
            total_time = total_time + elapsed
            print_progress(x + 1, config.resolution, size, config.name)
        avg_times_per_size.append([np.mean(elapsed_times), size])
        size = size + growth_rate

    print("\n")

    filtered_times, filtered_sizes = filter_outliers(avg_times_per_size)
    return filtered_times, filtered_sizes, total_time
