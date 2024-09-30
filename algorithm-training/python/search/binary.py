import random, time
from reports import plot_time
from benchmark import run_timing_benchmark
import cProfile

def binary_search(data, target):
	low = 0
	high = len(data) - 1
	while low <= high:
		mid = (low + high) // 2
		if data[mid] == target:
			return mid
		elif data[mid] < target:
			low = mid + 1
		else:
			high = mid - 1
	return -1

def search_benchmark_with_size(n):
	data = random.sample(range(n), n)
	target = random.choice(data)
	
	start_time = time.perf_counter()
	binary_search(data, target)
	elapsed_time = time.perf_counter() - start_time
	
	return elapsed_time

max_size = 10000
iterations = 100
resolution = 100
cProfile.run("run_timing_benchmark(search_benchmark_with_size, max_size, iterations, resolution)")

#[times, sizes, total_time] = run_timing_benchmark(search_benchmark_with_size, max_size, iterations, resolution)
#plot_time(times, sizes, f"Binary Search - iter: {iterations}, res: {resolution} - {total_time :.2f}s")
