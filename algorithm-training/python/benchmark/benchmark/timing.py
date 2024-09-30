from progressbar import print_progress
import numpy as np

def run_timing_benchmark(benchmark_func, max_size=1000, iterations=10, resolution=10):
	growth_rate = max_size // iterations
	size = growth_rate
	average_times = []
	while size <= max_size:
		print("\n")
		elapsed_times = []
		for x in range(resolution):
			elapsed_times.append(benchmark_func(size))
			print_progress(x + 1, resolution, size)
		average_times.append(np.mean(elapsed_times), size)
		size = size + growth_rate
	
	return average_times

