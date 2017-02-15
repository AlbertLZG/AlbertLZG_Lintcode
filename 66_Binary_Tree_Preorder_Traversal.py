"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    # """
    # @param root: The root of binary tree.
    # @return: Preorder in ArrayList which contains node values.
    # """
    def __init__(self):
        self.res = []
        
    def preorderTraversal(self, root):
        # write your code here
        if root:
            self.res.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.res

