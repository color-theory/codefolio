"""
simplehashtable.py
Simple hash table implementation in Python.
"""


class SimpleHashTable:
    """
    Simple hash table implementation

    Available Functions:
    - insert(key, value): Insert a key-value pair
    - lookup(key): Lookup a value by key
    """

    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, key, value):
        """
        Insert a key-value pair

        Parameters:
        key: int: The key
        value: Any: The value
        """
        if key < 0 or key >= self.size:
            raise ValueError("Key out of range for this hash table")
        self.table[key] = value

    def __setitem__(self, key, value):
        """Allows for using the [] operator to insert a key-value pair"""
        self.insert(key, value)

    def lookup(self, key):
        """
        Lookup a value by key

        Parameters:
        key: int: The key

        Returns:
        Any: The value
        """
        if key < 0 or key >= self.size:
            return None
        return self.table[key]

    def __getitem__(self, key):
        """Allows for using the [] operator to lookup a value by key"""
        return self.lookup(key)
