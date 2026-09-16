
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: 
            return True

        def same(n1, n2):
            if not n1 and not n2:
                return True
            elif not n1 or not n2:
                return False
            else:
                if n1.val == n2.val:
                    return same(n1.left, n2.left) and same(n1.right, n2.right)
                return False
        def checkSubRoot(node):
            if not node:
                return False
            else:
                if node.val == subRoot.val and same(node, subRoot):
                    return True 
                r = checkSubRoot(node.right)
                l = checkSubRoot(node.left)
                return l or r
               
    
        return checkSubRoot(root)