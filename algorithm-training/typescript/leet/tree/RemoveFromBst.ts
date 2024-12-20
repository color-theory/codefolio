/*
https://leetcode.com/problems/delete-node-in-a-bst

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
Search for a node to remove.
If the node is found, delete the node.
 

Example 1:
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:
Input: root = [], key = 0
Output: []
 

Constraints:
The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105
 
Follow up: Could you solve it with time complexity O(height of tree)?
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

export const removeNode = (
    root: TreeNode | null,
    key: number
): TreeNode | null => {
    const findMin = (root: TreeNode): TreeNode => {
        let curr = root;
        while (curr && curr.left) {
            curr = curr.left;
        }
        return curr;
    };

    const rec = (root: TreeNode | null, val: number): TreeNode | null => {
        if (!root) {
            return null;
        }
        if (root.val > val) {
            root.left = rec(root.left, val);
        } else if (root.val < val) {
            root.right = rec(root.right, val);
        } else {
            if (!root.left) {
                return root.right;
            } else if (!root.right) {
                return root.left;
            } else {
                const minNode = findMin(root.right);
                root.val = minNode.val;
                root.right = rec(root.right, minNode.val);
            }
        }
        return root;
    };

    return rec(root, key);
};
