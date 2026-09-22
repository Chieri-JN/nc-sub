# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
bst lvl order traverals aka bfs 

use stack, while stack is not empty take node out and add children to new stack
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        stack = [root]

        while stack:

            nxtLayer = []
            layer = []
            for node in stack:
                if node:
                    layer.append(node.val)
                    if node.left:
                        nxtLayer.append(node.left)
                    if node.right:
                        nxtLayer.append(node.right)
            if layer != []:
                res.append(layer)
            stack = nxtLayer
        return res