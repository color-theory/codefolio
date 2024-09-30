import random, time
from reports import plot_time
from benchmark import run_timing_benchmark

def sequential_search(data, target):
	for i in range(len(data)):
		if data[i] == target:
			return i
	return -1

def search_benchmark_with_size(n):
	data = random.sample(range(n), n)
	target = random.choice(data)
	
	start_time = time.perf_counter()
	sequential_search(data, target)
	elapsed_time = time.perf_counter() - start_time
	
	return elapsed_time

max_size = 10000
iterations = 200
resolution = 200
[times, sizes, total_time] = run_timing_benchmark(search_benchmark_with_size, max_size, iterations, resolution)

plot_time(times, sizes, f"Sequential Search - iter: {iterations}, res: {resolution} - {total_time :.2f}s", True)
