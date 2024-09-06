# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # l = 0
        # c = head
        # while c:
        #     l += 1
        #     c = c.next
        #
        # c2 = head
        # if l % 2 == 0:
        #     l = l // 2 + 1
        # else:
        #     l = l // 2
        # while l:
        #     c2 = c2.next
        #     l -= 1
        #
        # return c2
        s = head
        f = head
        while f and f.next:
            s = s.next
            f = f.next.next

        return s