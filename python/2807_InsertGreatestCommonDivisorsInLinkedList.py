from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def gcd(a, b):
        while b:
            r = a % b
            a = b
            b = r
        return a

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        prev = head
        curr = head.next
        while curr:
            v = ListNode(Solution.gcd(curr.val, prev.val), curr)
            prev.next = v
            prev = curr
            curr = curr.next

        return head