"""
we need to achive O(1) cost for each funciotn
the main issue is that pop might eliminate out min

idfea: each item stored as its value and the min at that point (not updated)

this means if we pop the current min we know what the prev min was 
this works becauses pushs and pops are orderd FILO 



"""

class MinStack:

    def __init__(self):
        self.minVal = None
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append((val, self.minVal))
        if self.minVal == None or val < self.minVal: 
            self.minVal = val
        # if val < self.minVal

    def pop(self) -> None:
        val, mv = self.stack.pop()
        if self.minVal == val:
            self.minVal = mv

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.minVal
        
