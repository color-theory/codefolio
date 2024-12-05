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

export function mergeLinkedListThirdList(
    list1: ListNode | null,
    list2: ListNode | null
): ListNode | null {
    if (!list1) {
        return list2;
    }
    if (!list2) {
        return list1;
    }
    let list1Curr: ListNode | null = list1;
    let list2Curr: ListNode | null = list2;
    let list3Head = null;

    if (list1Curr.val <= list2Curr.val) {
        list3Head = list1Curr;
        list1Curr = list1Curr.next;
    } else {
        list3Head = list2Curr;
        list2Curr = list2Curr.next;
    }

    let list3Curr = list3Head;
    while (list1Curr || list2Curr) {
        if (!list1Curr) {
            list3Curr.next = list2Curr;
            break;
        }
        if (!list2Curr) {
            list3Curr.next = list1Curr;
            break;
        }
        if (list1Curr.val <= list2Curr.val) {
            list3Curr.next = list1Curr;
            list1Curr = list1Curr.next;
        } else {
            list3Curr.next = list2Curr;
            list2Curr = list2Curr.next;
        }
        list3Curr = list3Curr.next;
    }
    return list3Head;
}
