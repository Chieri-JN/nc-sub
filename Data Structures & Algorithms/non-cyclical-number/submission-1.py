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

        nSlow = n
        nFast = n
        while True:
            valSlow  = digitSum(nSlow)
            valFast  = digitSum(digitSum(nFast))
            if valSlow == 1 or valFast == 1:
                return True

            if valSlow == valFast:
                return False
            
            nSlow = valSlow
            nFast = valFast
