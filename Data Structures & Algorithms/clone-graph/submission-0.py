"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


"""
just traverse the graph, keep map of node val to copy so we dont have to make new copys
use stack for dfs
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        copies = {} 
        stack = [node]

        while stack:
            currNode = stack.pop()
            copy = None
            if currNode.val in copies:
                copy = copies[currNode.val]
            else: 
                copy = Node(currNode.val)
                copies[currNode.val] = copy

            for n in currNode.neighbors:
                n_copy = None
                if n.val not in copies:
                    stack.append(n)
                    n_copy = Node(n.val)
                    copies[n.val] = n_copy
                else:
                    n_copy = copies[n.val]
                if copy.neighbors is None:
                    copy.neighbors  = []
                copy.neighbors.append(n_copy)
                
                

        return copies[node.val]