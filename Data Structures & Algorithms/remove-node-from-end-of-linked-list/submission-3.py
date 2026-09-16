# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        listLen = 0
        while dummy:
            listLen += 1
            dummy = dummy.next

        t = listLen - n
        count = 0
        dummy = head
        prev = None
        while dummy:
            if count == t:
                if prev:
                    prev.next = dummy.next
                if dummy == head:
                    head = dummy.next
                dummy.next = None
                break
            count += 1
            prev = dummy
            dummy = dummy.next

        return head