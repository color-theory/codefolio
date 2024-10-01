import random, time
from reports import plot_time
from benchmark import run_timing_benchmark

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

def search_benchmark(data):
	start_time = time.perf_counter()
	merge_sort(data)
	elapsed_time = time.perf_counter() - start_time
	return elapsed_time

def data_setup(size):
	data = random.sample(range(size), size)
	return data

max_size = 10000
iterations = 50
resolution = 1

[times, sizes, total_time] = run_timing_benchmark(search_benchmark, data_setup, max_size, iterations, resolution)
plot_time(times, sizes, f"Quick Sort - iter: {iterations}, res: {resolution} - {total_time :.2f}s")
