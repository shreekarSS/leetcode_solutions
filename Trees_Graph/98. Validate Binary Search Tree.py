# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
     def isValidBST(self, root: Optional[TreeNode]) -> bool:
         return self.dfs(root, -float('inf'), float('inf'))

     def dfs(self, node, low, up):
         if node:
             if node.val <= low or node.val >= up:
                 return False

             return self.dfs(node.left,low,node.val) and self.dfs(node.right, node.val, up)

         return True