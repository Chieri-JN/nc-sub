# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
preorder - top to bottom left to right
inorder - left to right -top to bottom

what does preorder tell us? dfs path essential 
    - the root, 
    - what node is whos parent 
    - left child @ i +1, rc @ i +2 ()
what does inorder tell us?
    - the ordering of nodes (ie left right)
    - split left rigt at node ( can do this recursively using range)
    - lc @ i - 1, rc @ i + 1

use thes two to build subtree: 
    - preorder tells dfs path (always left subtree first), 
    - inorde tells use left to right ordering i.e lsubtree, parent, right subtree'
    - using recursion we can reconstruct tree 
        - use preorder as orderign and inorder as construction (i.e left right)

algo: 
    first pass, create nodes + their idx in preorder and inorder
        - map of list map[val] = [node, pre-idx, in-idx]

    second pass, make connections
        - build: parentIDX, dfs nodeIDx, 

"""
from collections import defaultdict

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        nodes = defaultdict(list)
        n = len(preorder)
        for i,v in enumerate(preorder):
            nodes[v] = [TreeNode(v), i, 0]

        for i,v in enumerate(inorder):
            nodes[v][2] = i
        self.currIDX = 0

        def build(left, right):
            if left > right:
                return None
            else:
                node = nodes[preorder[self.currIDX]][0]
                self.currIDX += 1
                split = nodes[node.val][2]
                node.left = build(left, split - 1)
                node.right = build(split + 1, right)
                return node

        root = build(0, n - 1)
        return root



        