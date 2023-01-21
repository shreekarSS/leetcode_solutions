# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ctr = 0
        self.counter = 0
        self.dfs(root)
        return self.counter

    def dfs(self, node):
        total, n = 0, 0

        if node:
            left, left_count = self.dfs(node.left)
            right, right_count = self.dfs(node.right)

            n = 1 + left_count + right_count
            total = node.val + left + right
            print('total and n')
            print(total, n)

            if total // n == node.val:
                self.counter += 1

        return total, n