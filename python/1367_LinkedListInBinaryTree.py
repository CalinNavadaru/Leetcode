from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def verify(self, head: Optional[ListNode], root: Optional[TreeNode]):
        if not head:
            return True
        if not root:
            return False
        if root.val != head.val:
            return False
        return self.verify(head.next, root.left) or self.verify(head.next, root.right)

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val == head.val:
            return self.verify(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
