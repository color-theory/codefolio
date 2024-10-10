"""
longest_substring.py
This module contains an implementation of the longest common subsequence problem
using dynamic programming.
"""


def longest_common_subsequence(s1, s2):
    """
    Find the longest common subsequence between two strings

    Parameters:
    s1: str: The first string
    s2: str: The second string

    Returns:
    int: The length of the longest common subsequence between s1 and s2
    """
    m = len(s1)
    n = len(s2)
    dp_grid = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp_grid[i][j] = dp_grid[i - 1][j - 1] + 1
                if dp_grid[i][j] > max_length:
                    max_length = dp_grid[i][j]
            else:
                dp_grid[i][j] = max(dp_grid[i - 1][j], dp_grid[i][j - 1])

    return max_length


print(longest_common_subsequence("string one", "string two"))
print(longest_common_subsequence("hish", "fish"))
print(longest_common_subsequence("fish", "fosh"))