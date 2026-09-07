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
        while fast.next and fast.next.next:
            if fast.val in seen:
                return True
            seen.add(fast.val)
            seen.add(slow.val)
            slow = slow.next
            fast = fast.next.next

        
        return False