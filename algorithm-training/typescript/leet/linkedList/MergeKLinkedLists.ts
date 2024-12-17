/*
https://leetcode.com/problems/merge-k-sorted-lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 

Constraints:
k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
*/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val === undefined ? 0 : val;
        this.next = next === undefined ? null : next;
    }
}

export const mergeKLists = (lists: Array<ListNode | null>): ListNode | null => {
    const merge = (
        arr: Array<ListNode | null>,
        startIndex: number,
        midIndex: number,
        endIndex: number
    ) => {
        let arrCurr = startIndex;

        let leftArr = [];
        let rightArr = [];
        for (let i = startIndex; i <= midIndex; i++) {
            leftArr.push(arr[i]);
        }

        for (let i = midIndex + 1; i <= endIndex; i++) {
            rightArr.push(arr[i]);
        }

        let leftCurr = 0;
        let rightCurr = 0;

        while (leftCurr < leftArr.length && rightCurr < rightArr.length) {
            if (leftArr[leftCurr]!.val <= rightArr[rightCurr]!.val) {
                arr[arrCurr] = leftArr[leftCurr];
                leftCurr++;
            } else {
                arr[arrCurr] = rightArr[rightCurr];
                rightCurr++;
            }
            arrCurr++;
        }
        while (leftCurr < leftArr.length) {
            arr[arrCurr] = leftArr[leftCurr];
            leftCurr++;
            arrCurr++;
        }
        while (rightCurr < rightArr.length) {
            arr[arrCurr] = rightArr[rightCurr];
            rightCurr++;
            arrCurr++;
        }
    };

    const rec = (
        arr: Array<ListNode | null>,
        startIndex: number,
        endIndex: number
    ) => {
        if (endIndex <= startIndex) {
            return;
        }

        const mid = Math.floor((startIndex + endIndex) / 2);

        rec(arr, startIndex, mid);
        rec(arr, mid + 1, endIndex);

        merge(arr, startIndex, mid, endIndex);
    };

    let nodes: Array<ListNode | null> = [];
    for (let i = 0; i <= lists.length; i++) {
        let curr = lists[i];
        while (curr) {
            nodes.push(curr);
            curr = curr.next;
        }
    }

    if (nodes.length < 1) {
        return null;
    } else if (nodes.length == 1) {
        return nodes[0];
    }

    rec(nodes, 0, nodes.length - 1);

    let next = null;
    for (let x = nodes.length - 1; x >= 0; x--) {
        nodes[x]!.next = next;
        next = nodes[x];
    }

    return nodes[0];
};
