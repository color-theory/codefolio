"""
This module contains functions to plot the time complexity of algorithms.

Avaliable Functions:
- plot_time(times, sizes_of_n, title, trend, connect): Plot the time complexity
"""
import matplotlib.pyplot as plt
import numpy as np


def plot_time(times, sizes_of_n, title, trend=False, connect=False):
    """
    Plot the time complexity of an algorithm

    Parameters:
    times: List[float]: The average time to complete for each size
    sizes_of_n: List[int]: The sizes of the data
    title: str: The title of the plot
    trend: bool: Whether to plot the trendline
    connect: bool: Whether to connect the points
    """
    slope, intercept = np.polyfit(sizes_of_n, times, 1)
    trendline = [slope * size + intercept for size in sizes_of_n]

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes_of_n, times, color="blue", label='Sequential Search')
    if connect is True:
        plt.plot(sizes_of_n, times, color='lightblue',
                 linestyle='--', alpha=0.5)
    if trend is True:
        plt.plot(sizes_of_n, trendline, color='red',
                 linestyle='-', alpha=0.5, label='Trendline')
    plt.xlabel('Number of elements (n)')
    plt.ylabel('Average Time to Complete (s)')
    plt.title(title)
    plt.show()
