# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize(root):
    res = []

    def dfs(root):
        if not root:
            res.append('x')
            return

        res.append(root.val)
        dfs(root.left)
        dfs(root.right)
    dfs(root)
    return ''.join(res)



def deserialize(string_data):
    def dfs(string_data):
        val = next(string_data)
        if val == 'x':
            return
        root = TreeNode(int(val))
        root.left = dfs(string_data)
        root.right = dfs(string_data)

        return root

    return dfs(string_data)