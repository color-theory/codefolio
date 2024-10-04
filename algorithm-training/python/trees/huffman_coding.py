"""
huffman_coding.py
This modules contains functions that both encode and decode a message
using huffman coding. This relies on the huffman tree data structure, which
is a binary tree that only has values at the leaves.
"""
import heapq  # Uses a min-heap to act as the priority queue
from typing import Optional


class TreeNode:
    """
    A node for the huffman tree
    """

    def __init__(self, char, weight):
        self.char = char
        self.weight = weight
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        return self.weight == other.weight


def huffman_encode_message(message):
    """
    Encode a message using huffman coding.

    Parameters:
    message: str: The message to encode

    Returns:
    binary: str: The encoded message
    tree: Dict: The huffman tree used to decode the message
    """
    # Count the frequency of each character in the message
    frequency = {}
    for char in message:
        if char not in frequency:
            frequency[char] = 0
        frequency[char] += 1

    # Create a min-heap based priority queue of the characters
    heap = [TreeNode(char, weight) for char, weight in frequency.items()]
    heapq.heapify(heap)

    # Combine the two lowest frequency characters into a new node
    while len(heap) > 1:
        low1 = heapq.heappop(heap)
        low2 = heapq.heappop(heap)

        new_node = TreeNode(None, low1.weight + low2.weight)
        new_node.left = low1
        new_node.right = low2
        heapq.heappush(heap, new_node)

    # Create a dictionary to encode the characters
    encoding_dictionary = {}

    def encode_tree(node, encoding):
        if node.char:
            encoding_dictionary[node.char] = encoding
        else:
            encode_tree(node.left, encoding + '0')
            encode_tree(node.right, encoding + '1')

    encode_tree(heap[0], '')

    # Encode the message
    encoded_message = "".join([encoding_dictionary[char] for char in message])

    return encoded_message, heap


def decode_message(message, tree):
    """
    Decode a message using huffman coding.

    Parameters:
    message: str: The message to decode
    tree: Dict: The huffman tree used to decode the message

    Returns:
    str: The decoded message
    """
    decoded_message = ""
    node = tree[0]
    for bit in message:
        if bit == '0':
            node = node.left
        else:
            node = node.right

        if node.char:
            decoded_message += node.char
            node = tree[0]

    return decoded_message


compressed_message, huffman_tree = huffman_encode_message("hello world")
print(compressed_message)
decompressed_message = decode_message(compressed_message, huffman_tree)
print(decompressed_message)
