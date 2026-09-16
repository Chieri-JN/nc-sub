# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodeCount = {}
        count = 0
        dummy = head
        prev = None
        while dummy: 
            nodeCount[count] = [prev, dummy]
            prev = dummy
            dummy = dummy.next
            count += 1
        rmID = count - n
        rmNodePrev, rmNode = nodeCount[rmID]
        
        if rmNode: 
            if rmNodePrev:
                rmNodePrev.next = rmNode.next

            if rmNode == head:
                head=rmNode.next
            rmNode.next = None

        return head