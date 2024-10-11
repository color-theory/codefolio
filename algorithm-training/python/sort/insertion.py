"""
insertion.py
Implement insertion sort algorithm. Insertion sort is small and efficient for small lists.
It has a time complexity of O(n^2) and a space complexity of O(1).
"""


def insertion_sort(arr):
    """
    Insertion sort algorithm
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


arraytest = [12, 11, 13, 5, 6]
print(insertion_sort(arraytest))
