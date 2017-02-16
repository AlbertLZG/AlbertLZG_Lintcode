# coding:utf-8
'''
@Copyright:LintCode
@Author:   aaajack
@Problem:  http://www.lintcode.com/problem/binary-tree-level-order-traversal
@Language: Python
@Datetime: 17-02-16 14:48
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def __init__(self):
        self.res = []
        
    def levelOrder(self, root):
        # write your code here
        if not root:
            return []
        else:
            
            level_now = [root]
            while level_now:
                self.res.append([])
                level_next = []
                for node in level_now:
                    self.res[-1].append(node.val)
                    if node.left:
                        level_next.append(node.left)
                    if node.right:
                        level_next.append(node.right)
                level_now = level_next
        return self.res

        