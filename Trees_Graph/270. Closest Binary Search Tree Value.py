# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.minval = root.val

        def dfs(root):
            if not root:
                return None

            if abs(root.val-target) < abs(self.minval-target):
                self.minval = root.val

            if target < root.val:
                dfs(root.left)
            else:
                dfs(root.right)

            return self.minval
        return dfs(root)