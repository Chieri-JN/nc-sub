"""

"""
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def digitSum(n):
            val = 0
            while n > 0:
                dig = n % 10
                n //= 10
                val += dig**2
            return val

        
        while True:
            

            val  = digitSum(n)
            if val == 1:
                return True

            if val in seen:
                return False
            seen.add(val)
            n = val
