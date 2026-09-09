
"""
wanna find lognest substring without repeathing char

somehwat bf ish 
    - trakc idx fo each char
    - when we see repeart we just truncate until then (remove all charts between current start and new)
    - track diff between end and start 
    - 
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: 
            return len(s)
        seen = {}
        maxSSLen = 0
        start = 0

        for i, c in enumerate(s):
            if c in seen: 
                newS = seen[c] + 1
                while start < newS:
                    rC = s[start]
                    seen.pop(rC)
                    start += 1
            seen[c] = i
            maxSSLen = max(maxSSLen, i - start)
        return maxSSLen + 1
                    