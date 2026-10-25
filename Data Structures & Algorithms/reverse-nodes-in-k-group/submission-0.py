# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
need to reverse groups of k nodes, c

use helper function to reverse nodes

idea:
    - fro each group track head of group then reverse and set next to next group
        - could do recursively ish 
"""

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, tail):
            curr, prev = head, None
            # print(f"reversing: {head.val  if head else None} to {tail.val if tail else None}")
            while curr and curr != tail and curr.next:
                # print(f"node {curr.val}")
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            curr.next = prev
            # print(f"new head: {tail.val if tail else None}, new tail: {head.val if head else None}")
            return tail, head

        newHead = head
        groupCount = 0
        count = 1

        tempHead, tempTail = None, None
        currHead, currTail = head, None
        curr, prev = head, None

        while curr:
            # print(f"curr.val: {curr.val}, count: {count}")
            if count == k:
                currTail = curr
                temp = curr.next
                tempHead, tempTail = reverse(currHead, currTail)
                currHead = temp
                if groupCount == 0:
                    newHead = tempHead
                if prev:
                    prev.next = tempHead
                count = 1
                groupCount += 1
                prev = tempTail
                curr = temp

            if curr: 
                curr = curr.next
            count += 1
    
        if prev:
            prev.next = currHead

        return newHead