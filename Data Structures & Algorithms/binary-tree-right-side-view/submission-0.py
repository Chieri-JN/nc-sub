# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
return rightmost node of each layer 
"""

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack  = [root]
        res = []

        while stack:
            nxtLayer = []
            res.append(stack[-1].val)
            for node in stack:
                if node: 
                    if node.left:
                        nxtLayer.append(node.left)
                    if node.right:
                        nxtLayer.append(node.right)
            stack = nxtLayer
        return res