class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shift = 97
        if len(s) != len(t): 
            return False
        sList = [0] * 26
        tList = [0] * 26

        for i in range(len(s)):
            idxS = ord(s[i]) - shift
            idxT = ord(t[i]) - shift
            sList[idxS] += 1 
            tList[idxT] += 1 
        

        return sList == tList

