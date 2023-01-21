from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_so_far = 0
        self.dfs(root, 1)
        return self.max_so_far
    def dfs(self, node, maxDepth):
        if node:
            self.max_so_far = max(self.max_so_far,maxDepth)
            self.dfs(node.left, maxDepth+1)
            self.dfs(node.right, maxDepth+1)

        