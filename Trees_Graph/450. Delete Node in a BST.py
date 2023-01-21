# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None


        if key <  root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            if not root.left and not root.right:
                return None

            if not root.left and root.right:
                return root.right

            if root.left and not root.right:
                return root.left

            pnt = root.right

            while pnt.left:
                pnt = pnt.left

            root.val = pnt.val
            root.right = self.deleteNode(root.right, root.val)


        return root
