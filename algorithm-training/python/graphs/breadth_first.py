import random, time
from reports import plot_time
from benchmark import run_timing_benchmark
from collections import deque

algo_name = "Breadth First Search"
def breadth_first_search(data, target, start):
	search_queue = deque([start])
	searched = set()
	steps = 0
	while search_queue:
		steps += 1
		searching = search_queue.popleft()
		if searching not in searched:
			if searching == target:
				return steps
			else:
				search_queue += data[searching]
				searched.add(searching)
	return -1

def search_benchmark(data):
	target = random.choice(range(len(data)))
	start = random.choice(range(len(data)))
	start_time = time.perf_counter()
	breadth_first_search(data, target, start)
	elapsed_time = time.perf_counter() - start_time
	
	return elapsed_time

def data_setup(size):
	graph = {}
	max_edges = 3
	for i in range(size):
		graph[i] = []
		edge_count = 0
		for j in range (i + 1, size):
			if edge_count >= max_edges:
				break
			elif random.random() < .3:
				edge_count += 1
				graph[i] =  graph[i] + [j]

	return graph

max_size = 10000
iterations = 100
resolution = 100

[times, sizes, total_time] = run_timing_benchmark(search_benchmark, data_setup, max_size, iterations, resolution, algo_name)
plot_time(times, sizes, f"{algo_name} - iter: {iterations}, res: {resolution} - {total_time :.2f}s")
