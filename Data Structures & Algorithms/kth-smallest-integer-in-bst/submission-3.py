# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
given bst return kth smallest

ideas: 
    - construct order list and then index into k-1 use dfs + extend or just + 
        - could add early termination for when we hit list len k
    - keep count of numbers i.e node count is number of nodes in left subtree + 1
        - right subtree is  parent + 1 
        - need to pass in count, so leaf count + 1 


"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        targetN = [None]

        def count(node, cnt):
            if not node: # non
                return cnt
            elif not node.left and not node.right: # leaf
                if cnt == k: # might be + 1
                    targetN[0] = node.val
                return cnt + 1
            else:
                # stop recursing early
                
                pCnt = count(node.left, cnt)
                if targetN[0] is not None: 
                    return cnt
                if pCnt == k:
                    targetN[0] = node.val
                    return pCnt + 1 
                rCnt = count(node.right, pCnt + 1)
                
                return rCnt

        count(root, 1)
        return targetN[0]

                