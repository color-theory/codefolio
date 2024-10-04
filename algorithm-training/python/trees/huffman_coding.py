"""
huffman_coding.py
This modules contains functions that both encode and decode a message
using huffman coding. This relies on the huffman tree data structure, which
is a binary tree that only has values at the leaves.
"""
import sys
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
    node = tree
    for bit in message:
        if bit == '0':
            node = node.left
        else:
            node = node.right

        if node.char:
            decoded_message += node.char
            node = tree

    return decoded_message


def serialize_tree(tree):
    """
    Serialize the huffman tree

    Parameters:
    tree: Dict: The huffman tree to serialize

    Returns:
    str: The serialized tree
    """
    serialized_tree = []

    def serialize_node(node):
        if node.char:
            serialized_tree.append(f"1{node.char}")
        else:
            serialized_tree.append("0")
            serialize_node(node.left)
            serialize_node(node.right)

    serialize_node(tree)

    return "".join(serialized_tree).encode('utf-8')


def deserialize_tree(serialized_tree):
    """
    Deserialize the huffman tree

    Parameters:
    serialized_tree: str: The serialized tree

    Returns:
    Dict: The deserialized tree
    """
    serialized_tree = serialized_tree.decode('utf-8')
    serialized_tree = list(serialized_tree)

    def deserialize_node():
        if serialized_tree:
            bit = serialized_tree.pop(0)
            if bit == '1':
                char = serialized_tree.pop(0)
                return TreeNode(char, 0)
            node = TreeNode(None, 0)
            node.left = deserialize_node()
            node.right = deserialize_node()
            return node
        return None
    return deserialize_node()


def save(length, message, tree, filename):
    """
    Save the huffman encoded message and tree to a binary file

    Parameters:
    length: int: The length of the message
    message: str: The huffman encoded message
    tree: Dict: The huffman tree

    Returns:
    file: The binary file
    """
    with open(filename, "wb") as binary_file:
        binary_file.write(length.to_bytes(4, byteorder='big'))
        binary_file.write(message)
        binary_file.write(tree)


def load(filename):
    """
    Load the huffman encoded message and tree from a binary file

    Parameters:
    filename: str: The name of the file to load

    Returns:
    Tuple: The length of the message, the huffman encoded message, and the huffman tree
    """
    with open(filename, "rb") as binary_file:
        length = int.from_bytes(binary_file.read(4), byteorder='big')

        padded_message_length = (length + 7) // 8
        message = binary_file.read(padded_message_length)
        tree = binary_file.read()

    message = "".join([f"{byte:08b}" for byte in message])
    message = message[:length]
    return message, tree


def huffman_string_to_bytes(huffman_encoded_string):
    """
    Convert a string of 1s and 0s to a bytearray
    """
    byte_array = bytearray()
    # Process each 8-bit chunk
    for i in range(0, len(huffman_encoded_string), 8):
        byte = huffman_encoded_string[i:i + 8]  # Get 8 bits
        # Convert to int and append to bytearray
        byte_array.append(int(byte, 2))

    return byte_array


def main(filename):
    """
    Main function to encode and decode a message using huffman coding
    """
    with open(filename, "r", encoding="utf-8") as original_text_file:
        original_text = original_text_file.read()

    huffman_message, huffman_tree = huffman_encode_message(original_text)

    msg_length = len(huffman_message)
    padding_length = (8 - (msg_length % 8)) % 8
    padded_message = ("0" * padding_length) + huffman_message
    serialized_msg = huffman_string_to_bytes(padded_message)

    serialized_tree = serialize_tree(huffman_tree[0])

    save(msg_length, serialized_msg, serialized_tree, filename + ".bin")

    loaded_message, loaded_tree = load(filename + ".bin")

    deserialized_tree = deserialize_tree(loaded_tree)

    decompressed_message = decode_message(loaded_message, deserialized_tree)
    print(decompressed_message)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python huffman_coding.py <filename>")
        sys.exit(1)
    param = sys.argv[1]  # 0 is the script name, 1 is the first parameter
    main(param)
