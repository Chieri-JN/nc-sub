# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
we need to reorder list 
as 0, n-1, 1, n-2, 2, n-3, ...

idea gather nodes into list and then iterate from back and front 


"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodeList = []
        valLsit = [] # Debug 
        tmpHead = head
        while tmpHead:
            nodeList.append(tmpHead)
            valLsit.append(tmpHead.val) # Debug 
            tmpHead = tmpHead.next

        i, j = 0, len(nodeList) - 1
        n = len(nodeList)
        prev = None
        reorder = [] # Debug 
        while i < j: 
            # print(f"node[{i}] --> node[{j}]:  node({valLsit[i]}) --> node({valLsit[j]}) ") # Debug 
            nodeList[i].next = nodeList[j]
            nodeList[j].next = None
            if prev:
                # print(f"prev: {prev.val} --> prev.next: {nodeList[i].val}")# Debug 
                prev.next = nodeList[i]
            prev = nodeList[j]

            reorder.append(valLsit[i])# Debug 
            reorder.append(valLsit[j])# Debug 
            # print(f"reorder: {reorder}")# Debug 

            i += 1
            j -= 1
            if i == j:
                nodeList[j+1].next = nodeList[i] 
                nodeList[i].next = None
        # if n % 2 == 1:

  
        return 
