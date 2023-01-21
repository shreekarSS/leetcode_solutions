# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum = 0
        self.low= low
        self.high = high
        self.dfs(root)
        return self.sum
    def dfs(self, root):
        if root:
            if root.val in range(self.low, self.high+1):
                self.sum+=root.val

            return self.dfs(root.left) or self.dfs(root.right)