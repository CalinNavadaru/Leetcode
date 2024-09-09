# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        c = None
        while list1 or list2:
            v1 = 51
            v2 = 51
            if list1:
                v1 = list1.val
            if list2:
                v2 = list2.val
            if v1 < v2:
                r = ListNode(v1)
                list1 = list1.next
            elif v2 != 51:
                r = ListNode(v2)
                list2 = list2.next

            if not head:
                head = r
                c = r
            else:
                c.next = r
                c = c.next

        return head
