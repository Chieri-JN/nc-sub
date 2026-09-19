"""
given 2 strings, return weither s2 has a perm of s1 (As a substring)

insights/observations:
    - we know the size were looking for, 
    - chars must be continuous so if we break ss we can set new start there
    - 
idea/algoL 
    - we can construct map of chars in s1 w/ their counts
    - we have start pointer, and i pointer, 
    - if s2[i] in map and counts stil left, we continue
    - when start is moved: 
        - if s2[i] ot in s1 then we set start to idea
        - if s2[i] is in s1 but we don't have enough, we move start until
            - we gte the count back
    -how do we check that we hit our goal?
        - since we know how long s1 is, we can chcek if i - j == len(s1)
            - eithe ss is perm of its not
        -simpler just keep count of total correct chars found if its 0 we

"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charMap = {}
        for c in s1:
            charMap[c] = charMap.get(c, 0) + 1
        n = len(s1)
        len1 = n
        j = 0
        for i in range(len(s2)):
            c = s2[i]
            if c in charMap and charMap[c] > 0:
                charMap[c] = charMap[c] - 1
                n -= 1
            elif c in charMap and charMap[c] == 0:
                while charMap[c] == 0:
                   
                    rmC = s2[j]
                    charMap[rmC] = charMap[rmC] + 1
                    n += 1
                    j += 1
                charMap[c] = 0
                n -= 1
            else: # reset start
                while n < len1:
                    rmC = s2[j]
                    if rmC in charMap:
                        charMap[rmC] = charMap[rmC] + 1
                    n += 1
                    j += 1
                j = i + 1
            if n == 0:
                break

        return n == 0