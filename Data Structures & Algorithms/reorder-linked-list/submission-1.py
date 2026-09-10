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
        tmpHead = head
        while tmpHead:
            nodeList.append(tmpHead)
            tmpHead = tmpHead.next

        i, j = 0, len(nodeList) - 1
        n = len(nodeList)
        prev = None
        while i < j: 
            nodeList[i].next = nodeList[j]
            nodeList[j].next = None
            if prev:
                prev.next = nodeList[i]
            prev = nodeList[j]

            i += 1
            j -= 1
            if i == j:
                nodeList[j+1].next = nodeList[i] 
                nodeList[i].next = None
  
        return 
