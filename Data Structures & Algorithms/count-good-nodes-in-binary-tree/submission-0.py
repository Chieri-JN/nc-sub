# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
count good nodes
"""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def getGood(node, maxVal):
            if not node:
                return 0
            else:
                l = getGood(node.left, max(node.val, maxVal))
                r = getGood(node.right, max(node.val, maxVal))
                # count 
                return r + l + (1 if node.val >= maxVal else 0)

        return getGood(root, float("-inf"))
