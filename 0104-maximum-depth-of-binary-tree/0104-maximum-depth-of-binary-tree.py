# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
      #  return self.maxDepthdfs(root)
        self.max_so_far = 0
        self.dfs(root, 1)
        return self.max_so_far
    
    def maxDepthdfs(self, root):
        if root is None:
            return 0

        left_depth = self.maxDepthdfs(root.left)
        right_depth = self.maxDepthdfs(root.right)

        return max(left_depth, right_depth) + 1
    def dfs(self,node,maxDepth):
        if node:
            self.max_so_far = max(self.max_so_far, maxDepth)
            # if not node.left and not node.right:
            #     maxDepth+=1
            
            self.dfs(node.left, maxDepth+1)
            self.dfs(node.right, maxDepth+1)

#         if not node:
#             return None
#         left = self.dfs(node.left, maxDepth+1)
#         right = self.dfs(node.right, maxDepth+1)

#         if not left and not right:
#             self.max_so_far = max(self.max_so_far, maxDepth)
            
