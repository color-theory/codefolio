/*
https://leetcode.com/problems/binary-tree-right-side-view
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]

Example 3:
Input: root = [1,null,3]
Output: [1,3]

Example 4:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
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

export const rightSideView = (root: TreeNode | null): number[] => {
    let visibleValues: number[] = [];
    let levelValues: number[][] = [];
    let curr: TreeNode | null = root;
    let queue: Array<TreeNode | null> = [];

    if (!root) {
        return [];
    }

    queue.push(root);
    let levelLength = queue.length;
    let level = 0;
    while (levelLength > 0) {
        levelValues[level] = [];
        for (let i = 0; i < levelLength; i++) {
            curr = queue.shift() || null;
            levelValues[level].push(curr!.val);
            if (curr?.left) {
                queue.push(curr.left);
            }
            if (curr?.right) {
                queue.push(curr.right);
            }
        }
        levelLength = queue.length;
        level++;
    }
    levelValues.forEach((levelValue) => {
        visibleValues.push(levelValue[levelValue.length - 1]);
    });

    return visibleValues;
};
