/*
https://leetcode.com/problems/merge-two-sorted-lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
 
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
*/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val === undefined ? 0 : val;
        this.next = next === undefined ? null : next;
    }
}

export const mergeLinkedListInPlace = (
    list1: ListNode | null,
    list2: ListNode | null
): ListNode | null => {
    if (!list1 || !list2) return list1 || list2;

    let head = list1.val <= list2.val ? list1 : list2;
    let lCurr = head === list1 ? list1.next : list1;
    let rCurr = head === list2 ? list2.next : list2;
    let curr = head;

    while (lCurr && rCurr) {
        if (lCurr.val <= rCurr.val) {
            curr!.next = lCurr;
            lCurr = lCurr.next;
        } else {
            curr!.next = rCurr;
            rCurr = rCurr.next;
        }
        curr = curr.next;
    }
    curr!.next = lCurr || rCurr;

    return head;
};
