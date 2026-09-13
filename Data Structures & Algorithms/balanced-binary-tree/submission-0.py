# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return True, 0
            else:
                l, lh = height(node.left)
                r, rh = height(node.right)
                return l and r and (abs(lh-rh)<=1), 1 + max(lh,rh)

        
        return height(root)[0]
            