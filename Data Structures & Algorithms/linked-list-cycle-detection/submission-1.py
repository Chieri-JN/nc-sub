# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        seen = set()
        fast,slow = head, head
        seen.add(fast.val)
        while fast.next and fast.next.next:
            slow = slow.next
            if slow.val in seen:
                return True
            seen.add(fast.val)
            seen.add(slow.val)
            fast = fast.next.next

        
        return False