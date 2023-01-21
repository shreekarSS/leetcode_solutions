# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total_sum_li = []


        def dfs(root):
            if not root:
                return 0


            left  , right = dfs(root.left), dfs(root.right)

            cur_sum = left+right+root.val
            total_sum_li.append(cur_sum)
            return cur_sum



        total_sum = dfs(root)
        max_product = 0

        for _sum in total_sum_li:
            max_product= max(max_product, _sum*(total_sum-_sum))

        return max_product%(10**9+7)
