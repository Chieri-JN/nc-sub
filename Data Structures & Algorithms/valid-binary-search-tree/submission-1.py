# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
check if valid bst 
i.e everything to left is smaller, everything to right is large

"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, lo, hi):
            if not node:
                return True
            else:
                if node.val >= hi or node.val <= lo:
                    return False
                else:
                    return validate(node.left, lo, node.val) and validate(node.right, node.val, hi)

        return validate(root, float("-inf"), float("inf"))