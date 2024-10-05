# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        c = head
        while c and c.val == val:
            c = c.next

        result_head = c
        if not result_head:
            return None
        next_v = c.next
        while next_v:
            if next_v.val == val:
                c.next = next_v.next
                next_v = c.next
            else:
                c = next_v
                next_v = next_v.next

        return result_head
