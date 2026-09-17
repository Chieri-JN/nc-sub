"""
want to find longest ss of consec chars with k replacements

insights: 
    - most frequent char in window is part of the longest ss
    - once the diff betwen WindowSize - freqCharCount > k we need to shrink window

    - one challenge is how do we find most freqChar in window?, its easy to switch max
        - but what if when we shrink window we reduce freqChar and another one beats it
            -  could we just recheck for updated window? is thisx 
            - can we do range max? this is still logn 
        - when we switch max we also switch most freq and what eats into k
            - we remove until condition changes or new char is new max
                - what if the new max isnt the new char iof k is 
                - what if we keep 2 maps. char-count, count-char that way when we lose th max we can pick 
                    n
AAACBBCBBB
k=3

s="AAAAABBBBCBB"
k=3



"""
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        charFreq = {}
        freqChar = defaultdict(set)
        mChar = None
        j = 0
        maxSS = 0
        for i in range(n):
            count = charFreq.get(s[i], 0)
            charFreq[s[i]] = count + 1
            freqChar[count].remove(s[i]) if s[i] in freqChar[count] else None
            freqChar[count + 1].add(s[i])

            mChar = mChar if mChar and charFreq[mChar] > charFreq[s[i]]  else s[i]

            while (i - j + 1) - charFreq[mChar] > k:
                rmC = s[j]
                count = charFreq[rmC]
                charFreq[rmC] = count - 1
                freqChar[count].remove(rmC)
                freqChar[count - 1].add(rmC)
                if len(freqChar[count]) > 0 and rmC == mChar: 
                    mChar = freqChar[count].pop()
                    freqChar[count].add(mChar)
                j += 1
            maxSS = max(i - j, maxSS)

        return maxSS +1
        