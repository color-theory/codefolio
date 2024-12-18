/* 
https://leetcode.com/problems/binary-tree-level-order-traversal
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
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

export const levelOrder = (root: TreeNode | null): number[][] => {
    let queue = [];
    let result: number[][] = [];
    let level = 0;
    if (!root) {
        return [];
    }
    queue.push(root);
    let levelLength = queue.length;

    while (levelLength > 0) {
        result[level] = [];
        for (let i = 0; i < levelLength; i++) {
            const curr: TreeNode | null | undefined = queue.shift();
            if (curr) {
                result[level].push(curr.val);
                if (curr.left) {
                    queue.push(curr.left);
                }
                if (curr.right) {
                    queue.push(curr.right);
                }
            }
        }
        levelLength = queue.length;
        level++;
    }
    return result;
};
