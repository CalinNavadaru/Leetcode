# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = list1
        for i in range(1, a):
            start = start.next

        final = start.next
        for i in range(a, b + 1):
            final = final.next

        start.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = final
        return list1
