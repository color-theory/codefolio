"""
This module contains functions to plot the time complexity of algorithms.

Avaliable Functions:
- plot_time(times, sizes, title, trend, connect): Plot the time complexity
"""
import matplotlib.pyplot as plt
import numpy as np


class PlotConfig:
    """
    a class to configure the plot
    """

    def __init__(self, config):
        """
        Parameters:
        name: str: The name of the algorithm
        iterations: int: The number of iterations
        resolution: int: The resolution of the benchmark
        trend: bool: Whether to plot the trendline
        connect: bool: Whether to connect the points
        """
        self.name = config["name"] if "name" in config else "Algorithm"
        self.iterations = config["iterations"]
        self.resolution = config["resolution"]
        self.trend = config["trend"] if "trend" in config else False
        self.connect = config["connect"] if "connect" in config else False

    def __str__(self):
        return (
            f"name: {self.name}, "
            f"iterations: {self.iterations}, "
            f"resolution: {self.resolution}, "
            f"trend: {self.trend}, "
            f"connect: {self.connect}"
        )

    def validate(self):
        """
        Validate the configuration
        """
        if self.iterations <= 0:
            raise ValueError("iterations must be a positive integer.")
        if self.resolution <= 0:
            raise ValueError("resolution must be a positive integer.")


def plot_time(times, sizes, total_time, config):
    """
    Plot the time complexity of an algorithm

    Parameters:
    times: List[float]: The average time to complete for each size
    sizes: List[int]: The sizes of the data
    title: str: The title of the plot
    trend: bool: Whether to plot the trendline
    connect: bool: Whether to connect the points
    """
    slope, intercept = np.polyfit(sizes, times, 1)
    trendline = [slope * size + intercept for size in sizes]

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, times, color="blue", label='Sequential Search')
    if config.connect is True:
        plt.plot(sizes, times, color='lightblue',
                 linestyle='--', alpha=0.5)
    if config.trend is True:
        plt.plot(sizes, trendline, color='red',
                 linestyle='-', alpha=0.5, label='Trendline')
    plt.xlabel('Number of elements (n)')
    plt.ylabel('Average Time to Complete (s)')
    plt.title(
        f"{config.name} - iter: {config.iterations}, res: "
        f"{config.resolution} - {total_time:.2f}s"
    )
    plt.show()
