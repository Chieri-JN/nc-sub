"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
Need to create deep copy of ll with rand pointer

    - insights / observations 
        - vals may not be unique 
    
idea: 
    - we we traverse usign next
    
    - for rand pointer node: if it exists use that, otherwise create new
        - map random pointer (og) to copy (handles dupe vals)
        - using "mem" lcoation as key which is unique 

    alternate: 
        - use tuple of node val and rand val but there's a chance thant two same vals have none rand p

"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        sourceMap = {}

        dummy = head
        prevCopy = None
        while dummy:
            sourceMap[dummy] = sourceMap.get(dummy, Node(dummy.val))
            
            if prevCopy:
                prevCopy.next = sourceMap[dummy]

            # if copy of dummy's random node already exists
            if dummy.random in sourceMap:
                sourceMap[dummy].random = sourceMap[dummy.random]
            elif dummy.random:
                sourceMap[dummy].random = Node(dummy.random.val)
                sourceMap[dummy.random] = sourceMap[dummy].random
            prevCopy = sourceMap[dummy]
            dummy = dummy.next


        return sourceMap[head]