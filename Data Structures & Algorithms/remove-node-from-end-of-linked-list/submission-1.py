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
        # if count == 1:
        #     return None
        rmID = count - n
        # print(f"nodeCount: {nodeCount}")
        # print(f"rmID: {rmID}, count: {count}")
        rmNodePrev, rmNode = nodeCount[rmID]

        
        if rmNode: 
            if rmNodePrev:
                rmNodePrev.next = rmNode.next
            print({rmNode == head})
            if rmNode == head:
                # print(f"prev ehad: {head.val if head else None}")
                head=rmNode.next
                # print(f"new ehad: {head.val if head else None}")
            rmNode.next = None

        return head