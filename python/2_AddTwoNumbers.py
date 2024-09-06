from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        transport, v = divmod(l1.val + l2.val, 10)
        result = ListNode(val=v)
        head = result
        l1 = l1.next
        l2 = l2.next
        while l1 or l2:
            v1 = 0
            v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            transport, v = divmod(v1 + v2 + transport, 10)
            result.next = ListNode(v)
            result = result.next

        if transport:
            result.next = ListNode(transport)

        return head
