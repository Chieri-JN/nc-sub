"""
ord a is 97

start = 97 + 3 * (int(digit[i]) - 1)

or just map of chars
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        n = len(digits)
        if n == 0:
            return res

        def backtrack(idx, curr):
            if len(curr) == n:
                newStr = "".join(curr)

                res.append(newStr)
            else:
                for c in letters[digits[idx]]:
                    curr.append(c)
                    backtrack(idx+1, curr)
                    curr.pop()

        backtrack(0, [])  


        return res