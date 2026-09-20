# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
add 2 nums that are represented as linked Lists output linekd list

alog:
    - create a new node for each digit, we keep a variable for carry over
    O(N) time, O(N) space (not)

O(1) space:
    - we reuse one of the ll, lets say l1, keep variable for carry over 

    - ideally we use the longest one but we'd have to calculate that
"""

class Solution:
    def listLen(self, l):
        dummy = l
        count = 0
        while dummy: 
            count += 1
            dummy = dummy.next
        return count
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Len, l2Len = self.listLen(l1), self.listLen(l2)
        if l1Len < l2Len:
            l1, l2  = l2, l1
        
        dummy1, dummy2 = l1, l2
        carryOver = 0
        # because l2 is the shorter one we can stop once we it
        prev1 = None
        while dummy1: 
            val = carryOver
            if dummy2: 
                val += dummy2.val
                dummy2 = dummy2.next
            val += dummy1.val
            carryOver = val // 10
            dummy1.val = val % 10
            prev1 = dummy1
            dummy1 = dummy1.next
        
        if carryOver: 
            prev1.next = ListNode(carryOver)

        return l1