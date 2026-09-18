# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
find lca 
    

insights: 
    - bst invariants -> everything to left is <, everything to rigth is >
    - given p,q and node, 
        if p or q == node, return node
        if node < both p and q, go right
        if ndoe > both p and q, go left
        if q, q split at node, return node
"""

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def findLCA(node):
            if not node:
                return node
            else:
                if node.val < p.val and node.val < q.val: 
                    return findLCA(node.right)
                elif node.val > p.val and node.val > q.val: 
                    return findLCA(node.left)
                else:
                    return node

        return findLCA(root)
