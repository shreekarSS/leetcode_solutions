# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.mindepth = float('inf')
        dfs(root, 1)
        return self.mindepth
        def dfs(root,mindepthsofar):
            if not root:
                return 0

            if not root.left and not root.right:
                self.mindepth = min(mindepthsofar, self.mindepth)

            dfs(root.left, mindepthsofar+1)
            dfs(root.right, mindepthsofar+1)