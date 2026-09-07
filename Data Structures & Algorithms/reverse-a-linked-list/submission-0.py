# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
revers ll

need prev, curr, next

curr -> prev
prev = curr
curr = next
next = curr.next
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currN = head
        nextN = None
        prevN = None

        while currN is not None:
            nextN = currN.next
            currN.next = prevN
            prevN = currN
            currN = nextN

        return prevN