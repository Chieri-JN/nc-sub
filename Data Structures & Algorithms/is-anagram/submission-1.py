class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCountS = {}
        charCountT = {}
        if (len(s) != len(t)): return False

        for i in range(len(s)):
            charCountS[s[i]]  = charCountS.get(s[i], 0) + 1
            charCountT[t[i]]  = charCountT.get(t[i], 0) + 1

        return charCountS == charCountT