import random, time
from reports import plot_time
from benchmark import run_timing_benchmark

algo_name = "Dictionary Lookup"
def dictionary_search(data, target):
	result = data[target]

def search_benchmark(data):
	keys = [key for key in data.keys()]
	target = random.choice(keys)

	start_time = time.perf_counter()
	dictionary_search(data, target)
	elapsed_time = time.perf_counter() - start_time
	
	return elapsed_time

def data_setup(size):
	data = {}
	noise = random.sample(range(size), size)
	for i in noise:
		data[i] = i * 2

	return data

max_size = 100000
iterations = 100
resolution = 100

[times, sizes, total_time] = run_timing_benchmark(search_benchmark, data_setup, max_size, iterations, resolution, algo_name)
plot_time(times, sizes, f"{algo_name} - iter: {iterations}, res: {resolution} - {total_time :.2f}s")
