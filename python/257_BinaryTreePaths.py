# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    result = []

    def __computePath(self, root: Optional[TreeNode], sol: list[str]):
        if not root:
            return
        sol.append(str(root.val))
        if not root.left and not root.right:
            Solution.result.append("->".join(x for x in sol.copy()))
        else:
            self.__computePath(root.left, sol)
            self.__computePath(root.right, sol)
        sol.pop()


    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        Solution.result = []
        self.__computePath(root, [])
        return Solution.result