# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.longest = 1
        self.dfs(root,root.val-1, 0)

        return self.longest
    def dfs(self, node , prev_val, cur_len):
        if node:
            if node.val-1 == prev_val:
                cur_len+=1
                self.longest = max(self.longest, cur_len)
                self.dfs(node.left, node.val,cur_len)
                self.dfs(node.right, node.val, cur_len)

            else:
                self.dfs(node.left,node.val,1)
                self.dfs(node.right,node.val,1)




