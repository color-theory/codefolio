import matplotlib.pyplot as plt
import numpy as np

def plot_time(times, sizes_of_n, title):
	slope, intercept = np.polyfit(sizes_of_n, times, 1)
	trendline = [slope * size + intercept for size in sizes_of_n]

	plt.figure(figsize=(10, 6))
	plt.scatter(sizes_of_n, times, color="blue", label='Sequential Search')
	plt.plot(sizes_of_n, times, color='lightblue', linestyle='--', alpha=0.5)
	plt.plot(sizes_of_n, trendline, color='red', linestyle='-', alpha=0.5, label='Trendline')
	plt.xlabel('Number of elements (n)')
	plt.ylabel('Average Time to Complete (s)')
	plt.title(title)
	plt.show()