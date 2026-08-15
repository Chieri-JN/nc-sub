"""

"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {"}":"{", "]":"[", ")":"("}
        for c in s:
            if c in "{[(":
                stack.append(c)
            else:
                paren = False if len(stack)==0 else stack.pop()
                if pair[c] != paren:
                    return False
    
        return len(stack) == 0