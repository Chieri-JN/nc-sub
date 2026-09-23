"""
want to see if given str is palinfrom

given full sentences but it is case insensitve and only consider alphanums

ex: "Was it a car or a cat I saw?"

easiest way -> jsut create log string (skip non alpha num and then flip it and check)


"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        finalString = ""
        for c in s:
            if c.isalnum():
                finalString = finalString + c.lower()

        return finalString == finalString[::-1]