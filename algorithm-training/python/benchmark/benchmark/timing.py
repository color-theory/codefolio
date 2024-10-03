from progressbar import print_progress
import time
import numpy as np

def run_timing_benchmark(benchmark_func, setup_func, max_size=1000, iterations=100, resolution=50, algo_name="algorithm"):
	growth_rate = max_size // iterations
	size = growth_rate
	avg_times_per_size = []
	total_time = 0
	while size <= max_size:
		elapsed_times = []
		print(f"\r setting up data...", end="")
		data = setup_func(size)
		for x in range(resolution):
			elapsed = benchmark_func(data)
			elapsed_times.append(elapsed)
			total_time = total_time + elapsed
			print_progress(x + 1, resolution, size, algo_name)
		avg_times_per_size.append([np.mean(elapsed_times), size])
		size = size + growth_rate

	print("\n")
	times = [x[0] for x in avg_times_per_size]
	sizes = [x[1] for x in avg_times_per_size]

	mean_time = np.mean(times)
	std_dev_time = np.std(times)
	lower_bound = mean_time - 2 * std_dev_time
	upper_bound = mean_time + 2 * std_dev_time

	non_outlier_indices = np.where((times >= lower_bound) & (times <= upper_bound))[0]
	filtered_times = [times[i] for i in non_outlier_indices]
	filtered_sizes = [sizes[i] for i in non_outlier_indices]
	
	return filtered_times, filtered_sizes, total_time

