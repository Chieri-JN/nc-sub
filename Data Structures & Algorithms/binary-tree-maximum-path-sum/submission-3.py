# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
return max Path sum

at each node the choice is max of
    - max  of itself (no children) vs leftChild + node vs right + node (can continue)
    - path of left + node + left (cant continue)

return 
    - max node.val
        max(node.val + l, node.val + r)
        max(node.val + l[0], node + r[0])
    - max (node.val + l[0] + r[0], l[1], r[1])


Waht this does:
    - capturs maxpath connected to curr node (can connect to ancestors)
    - max path seen in subtree 

"""

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        infMin = float("-inf")
        def maxPath(node):
            if not node:
                return infMin, infMin

            else:
                val = node.val
                lp, lmax = maxPath(node.left)
                rp, rmax = maxPath(node.right)
                parent = val
                left = val
                right = val
                if lp!=infMin:
                    parent += lp
                    left += lp
                if rp != infMin:
                    parent += rp
                    right += rp
                maxConnect = max(val, left, right)
                
                maxMax = max(parent, lmax, rmax, lp, rp)

                return maxConnect, maxMax


        return max(maxPath(root))
