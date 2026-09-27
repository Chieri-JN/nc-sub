"""

"""

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        res = []

        for c in operations:
            if c == "+":
                res.append(int(res[-1]) + int(res[-2]))
            elif c == "D":
                res.append(int(res[-1]) * 2)
            elif c == "C":
                res.pop()
            else:
                res.append(int(c))

        return sum(res)