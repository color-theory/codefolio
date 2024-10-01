import random, time
from reports import plot_time
from benchmark import run_timing_benchmark

def quick_sort(data):
	if len(data) < 2:
		return data
	elif len(data) == 2:
		return [min(data), max(data)]
	
	pivot = len(data) // 2
	lt_pivot = [x for x in data if x < data[pivot]]
	eq_pivot = [x for x in data if x == data[pivot]]
	gt_pivot = [x for x in data if x > data[pivot]]

	return quick_sort(lt_pivot) + eq_pivot + quick_sort(gt_pivot)

def search_benchmark(data):
	start_time = time.perf_counter()
	quick_sort(data)
	elapsed_time = time.perf_counter() - start_time
	return elapsed_time

def data_setup(size):
	data = random.sample(range(size), size)
	return data

max_size = 10000
iterations = 100
resolution = 100

[times, sizes, total_time] = run_timing_benchmark(search_benchmark, data_setup, max_size, iterations, resolution)
plot_time(times, sizes, f"Quick Sort - iter: {iterations}, res: {resolution} - {total_time :.2f}s")
