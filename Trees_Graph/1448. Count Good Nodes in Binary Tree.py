class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.total = 0
        self.dfs(root, -float('inf'))
        return self.total
    def dfs(self, node, max_so_far):
        if node:
            if node.val >= max_so_far:
                self.total+=1

            self.dfs(node.left,max(node.val, max_so_far))
            self.dfs(node.right, max(node.val, max_so_far))


