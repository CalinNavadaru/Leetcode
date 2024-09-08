# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l = 0
        c = head
        while c:
            l += 1
            c = c.next
        size, extra = divmod(l, k)
        c = head
        result = []
        index = 0
        while c:
            result.append(c if c else None)
            v = size + 1 if extra > 0 else size
            prev = c
            index += 1
            while v and c:
                prev = c
                c = c.next
                v -= 1
            prev.next = None
            extra -= 1

        for i in range(index, k):
            result.append(None)

        return result


print(a := Solution().splitListToParts(ListNode(1, ListNode(2, ListNode(3))), 5))
print(b := Solution().splitListToParts(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6,
                                                                                                            ListNode(7,
                                                                                                                     ListNode(
                                                                                                                         8,
                                                                                                                         ListNode(
                                                                                                                             9,
                                                                                                                             ListNode(
                                                                                                                                 10)))))))))),
                                       3))
print(3)
