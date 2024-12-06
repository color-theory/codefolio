/*
https://leetcode.com/problems/search-a-2d-matrix/description/

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
*/
export const searchMatrix = (matrix: number[][], target: number): boolean => {
    const rec = (arr: number[], target: number) => {
        if (arr.length == 1) {
            return arr[0] == target;
        }
        if (arr[0] > target) return false;
        if (arr[arr.length - 1] < target) return false;
        const midpoint = Math.floor(arr.length / 2);
        if (arr[midpoint] < target) {
            return rec(arr.slice(-midpoint), target);
        } else if (arr[midpoint] > target) {
            return rec(arr.slice(0, midpoint), target);
        } else {
            return true;
        }
    };

    for (let x = 0; x <= matrix.length - 1; x++) {
        if (rec(matrix[x], target)) return true;
    }

    return false;
};
