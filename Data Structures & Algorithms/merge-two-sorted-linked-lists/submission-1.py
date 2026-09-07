# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        prev = None
        if list1 and list2:
            if list1.val <= list2.val:
                head = list1
                list1 = list1.next
            else:
                head = list2
                list2 = list2.next
        else:
            return list1 if list1 else list2
            
        prev = head
        # lst = [prev.val if prev else None]
        # print(f"head: {head.val if head else None}")
        # print(f"head: {list1.val if list1 else None}")
        # print(f"head: {list2.val if list2 else None}")
        while list1 and list2:
            # print(f"head: {head}")
            # print(f"head: {lst}")
            if list1.val <= list2.val:
                prev.next = list1
                prev = list1
                # lst.append(prev.val)
                list1 = list1.next
            else:
                prev.next = list2
                prev = list2
                # lst.append(prev.val)
                list2 = list2.next

        if list1 and prev and not list2:
            prev.next = list1
        elif list2 and prev and not list1:
            prev.next = list2

        
        return head
