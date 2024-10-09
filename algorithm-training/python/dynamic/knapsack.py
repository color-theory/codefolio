"""
knapsack.py
This module contains an implementation of the knapsack problem using dynamic programming.
"""
from typing import List


class Item:
    """
    A class to represent an item in the knapsack problem
    """

    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __repr__(self):
        return f"Item({self.weight}, {self.value})"

    def validate(self):
        """
        Validate the item's weight and value
        """
        if self.weight < 0:
            raise ValueError("Weight must be a non-negative integer")
        if self.value < 0:
            raise ValueError("Value must be a non-negative integer")


def knapsack(items: List[Item], capacity):
    """
    Find the maximum value of items that can fit in the knapsack

    Parameters:
    items: List[Item]: The items to choose from
    capacity: int: The capacity of the knapsack

    Returns:
    int: The maximum value of items that can fit in the knapsack
    """
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            item = items[i - 1]
            if item.weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1]
                               [w - item.weight] + item.value)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


available_items = [Item(2, 6), Item(2, 10), Item(3, 12)]
print(knapsack(available_items, 5))
