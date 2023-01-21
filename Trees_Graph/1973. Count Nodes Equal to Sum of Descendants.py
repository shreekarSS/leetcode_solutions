
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        self.counter = 0
        self.dfs(root)
        return self.counter

    def dfs(self, node):
        if not node:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        if left+right == node.val:
            self.counter+=1

        return left+right+node.val
