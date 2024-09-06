# Definition for singly-linked list.
from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        nums = set(nums)
        while current.val in nums:
            current = current.next
        new_head = current
        while current.next:
            if current.next.val in nums:
                current.next = current.next.next
            else:
                current = current.next
        return new_head
