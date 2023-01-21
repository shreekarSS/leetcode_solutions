# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # topological sorting
        #
        self.res = collections.defaultdict(list)
        self.dfs(root,0)
        return self.res.values()

#{ 0: [4,5,3], 1:[2], 2:[1]}

    def dfs(self, node, height):
        if not node:
            return 0

        left = self.dfs(node.left, height)
        right = self.dfs(node.right, height)
        #base leaf node has no kids, so index will be 0
        height = max(left, right)
        self.res[height].append(node.val)
        #increament index for upper node
        return height+1

