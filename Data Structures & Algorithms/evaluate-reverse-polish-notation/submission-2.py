"""
evalutate rpn 
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        for t in tokens:
            if t not in "-*/+":
                stack.append(t)
            else:
                v1 = stack.pop()
                v2 = stack.pop()
                v3 = None
                # print(f"v1: {v1}")
                # print(f"v2: {v2}")
                if t == "+":
                    v3 = int(v2) + int(v1) 
                    
                elif t == "-":
                    v3 = int(v2) - int(v1) 
                elif t == "*":
                    v3 = int(v2) * int(v1) 
                elif t == "/":
                    v3 = int(int(v2) / int(v1) )
                # print(f"{v3} = {v2} {t} {v1}")

                stack.append(str(v3))
            # print(f"stack: {stack}")
        
        final = stack.pop()
        return int(final)
