# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""

"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best=[0]
        def getDepth(node):
            if not node:
                return 0
            else:
                l = getDepth(node.left)
                r = getDepth(node.right)
                best[0] = max(best[0], 1 + l + r)
                return max(l, r) + 1
        getDepth(root)
        return best[0] - 1