"""
dijkstra.py
This module contains an implementation of Dijkstra's algorithm for finding
the shortest path in a graph.
"""
import math
import heapq
from typing import Dict, Optional
from datastructures import Graph, WeightedDirectedGraphNode


def dijkstra(graph: Graph, start: WeightedDirectedGraphNode, end: WeightedDirectedGraphNode):
    """
    Find the shortest path in a graph using Dijkstra's algorithm

    Parameters:
    graph: Graph: The graph to search
    start: GraphNode: The starting node
    end: GraphNode: The ending node

    Returns:
    str: The shortest path from start to end
    """
    # Initialize the distance to each node
    distances = {node: math.inf for node in graph}
    distances[start] = 0

    # Initialize the previous node for each node
    parents: Dict[WeightedDirectedGraphNode, Optional[WeightedDirectedGraphNode]] = {
        node: None for node in graph}

    # Initialize the priority queue
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Check if we have already found a shorter path
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in current_node.neighbors:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    path = []
    current_node = end

    if parents[current_node] is None and current_node != start:
        return f"No path from {start.value} to {end.value}"

    while current_node and parents[current_node]:
        path.append(current_node.value)
        current_node = parents[current_node]

    path.append(start.value)
    return path[::-1]


test_graph = Graph()
test_graph.add_node(WeightedDirectedGraphNode("A"))
test_graph.add_node(WeightedDirectedGraphNode("B"))
test_graph.add_node(WeightedDirectedGraphNode("C"))
test_graph.add_node(WeightedDirectedGraphNode("D"))

test_graph["A"].add_neighbor(test_graph["B"], 6)
test_graph["A"].add_neighbor(test_graph["C"], 2)
test_graph["B"].add_neighbor(test_graph["D"], 1)
test_graph["C"].add_neighbor(test_graph["B"], 3)
test_graph["C"].add_neighbor(test_graph["D"], 5)

starting_node = test_graph["A"]
ending_node = test_graph["D"]

print(dijkstra(test_graph, starting_node, ending_node))
