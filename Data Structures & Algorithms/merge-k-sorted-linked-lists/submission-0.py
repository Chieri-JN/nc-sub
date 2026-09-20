# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
merge k lists, i.e final step merge sort with k lists 
Assume a lists are lenght m, then runtime is kmlogk 
    - split list, 
        - base Case: 
            singleton and empty: return ll
        - recursive case:
            we split list then call merge on split
        - we then merge the halfs
            - new head is the smallest head and then we jsut "interleave" nodes
        - return result


alternative: space optimized (no recursion)
    use heap, where the lsts are order using 1st
        elem, and we iterate until heap is empty
"""
# import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def splitMerge(nodeList):
            if nodeList == []:
                return None 
            elif len(nodeList) == 1:
                return nodeList[0]
            else:
                split = len(nodeList) // 2 
                # x = [c.val for c in nodeList[:split]]
                # y = [c.val for c in nodeList[split:]]
                # print(f"nodeList[:split]: {x}")
                # print(f"nodeList[split:]: {y}")
                A, B = splitMerge(nodeList[:split]), splitMerge(nodeList[split:])
                # al = []
                # ad = A
                # while ad: 
                #     al.append(ad.val)
                #     ad = ad.next
                # bl = []
                # bd = B
                # while ad: 
                #     bl.append(bd.val)
                #     bd = bd.next
                # print(f"A: {al}")
                # print(f"B: {bl}")
                if not A:
                    return B
                elif not B:
                    return A
                head = None
                if A.val <= B.val:
                    head = A
                    A = A.next
                else:
                    head = B
                    B = B.next
                dummy = head
                while A and B: 
                    if A.val <= B.val:
                        dummy.next = A
                        A = A.next
                    else:
                        dummy.next = B
                        B = B.next
                    dummy = dummy.next
                if A:
                    dummy.next = A
                elif B: 
                    dummy.next = B
                # hl = []
                # hd = head
                # while hd: 
                #     hl.append(hd.val)
                #     hd = hd.next
                # print(f"Head: {hl}")
                return head
        return splitMerge(lists)



            