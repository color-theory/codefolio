import random, time
from reports import plot_time
from benchmark import run_timing_benchmark

def sequential_sort(data):
	for i in range(len(data)):
		lowest_number_index = i
		for j in range(i,len(data)):
			if data[j] < data[lowest_number_index]:
				lowest_number_index = j
		temp=data[i]
		data[i]=data[lowest_number_index]
		data[lowest_number_index]=temp

def search_benchmark(data):
	start_time = time.perf_counter()
	sequential_sort(data)
	elapsed_time = time.perf_counter() - start_time
	
	return elapsed_time

def data_setup(size):
	data = random.sample(range(size), size)
	return data

max_size = 10000
iterations = 50
resolution = 1

[times, sizes, total_time] = run_timing_benchmark(search_benchmark, data_setup, max_size, iterations, resolution)
plot_time(times, sizes, f"Sequential Sort - iter: {iterations}, res: {resolution} - {total_time :.2f}s")
