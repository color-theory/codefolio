"""
graph.py
This module contains a graph data structure
"""


class GraphNode:
    """
    A node in an undirected graph

    Attributes:
    value: Any: The value of the node
    neighbors: List[GraphNode]: The neighbors of the node

    Methods:
    add_neighbor: Add a neighbor to the node
    get_neighbors: Get the neighbors of the node
    """

    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, neighbor: "GraphNode"):
        """Add a neighbor to the node"""
        if neighbor not in self.neighbors:
            self.neighbors.append((neighbor))
            neighbor.add_neighbor(self)

    def get_neighbors(self):
        """Get the neighbors of the node"""
        return self.neighbors


class DirectedGraphNode(GraphNode):
    """
    A node in a directed graph

    Attributes:
    value: Any: The value of the node
    neighbors: List[DirectedGraphNode]: The neighbors of the node

    Methods:
    add_neighbor: Add a neighbor to the node
    """

    def add_neighbor(self, neighbor: "DirectedGraphNode"):
        """Add a neighbor to the node"""
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)


class WeightedGraphNode(GraphNode):
    """
    A node in an undirected graph with weighted edges

    Attributes:
    value: Any: The value of the node
    neighbors: List[Tuple[WeightedGraphNode, float]]: The neighbors of the
        node and the weight of the edge

    Methods:
    add_neighbor: Add a neighbor to the node
    """

    def add_neighbor(self, neighbor: "WeightedGraphNode", weight: float = 1.0):
        """Add a neighbor to the node"""
        if not any(n == neighbor for n, _ in self.neighbors):
            self.neighbors.append((neighbor, weight))
            neighbor.add_neighbor(self, weight)


class WeightedDirectedGraphNode(DirectedGraphNode):
    """
    A node in a directed graph with weighted edges

    Attributes:
    value: Any: The value of the node
    neighbors: List[Tuple[WeightedDirectedGraphNode, float]]: The neighbors of 
        the node and the weight of the edge

    Methods:
    add_neighbor: Add a neighbor to the node
    """

    def add_neighbor(self, neighbor: "WeightedDirectedGraphNode", weight: float = 1.0):
        """Add a neighbor to the node"""
        if not any(n == neighbor for n, _ in self.neighbors):
            self.neighbors.append((neighbor, weight))
