# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res  = []

        def dfs(root):
            if not root:
                return None

            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        return res[k-1]