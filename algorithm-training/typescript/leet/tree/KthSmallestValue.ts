/*
https://leetcode.com/problems/kth-smallest-element-in-a-bst
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 
Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
*/

class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val === undefined ? 0 : val;
        this.left = left === undefined ? null : left;
        this.right = right === undefined ? null : right;
    }
}

export const kthSmallest = (root: TreeNode | null, k: number): number => {
    let sortedValues: number[] = [];
    const rec = (root: TreeNode | null) => {
        if (!root) return;
        rec(root.left);
        sortedValues.push(root.val);
        rec(root.right);
    };
    rec(root);
    return sortedValues[k - 1];
};
