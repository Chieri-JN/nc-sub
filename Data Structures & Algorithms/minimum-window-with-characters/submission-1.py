"""
given 2 str s and t find min winow ss in s such that all chars in t appear in it

Given / ideations:
    - the ouput is uniq 
    - we know exactly how many chars we need 


Ideas: 
    - get counts of chars in t
    - do 1 pass in S (check if a ss exist) if no then return ""
    - Other wise Ss exist an we want to find smallest:
        - user two pointers on ends of s
        - we move one side first until SS is no longer valid
        - then we move to other side and move it in until its no longer valid (i.e charcountS < charCountT)
        - return this ss

"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        charCountT = {}
        charCountS = {}

        for c in t:
            charCountT[c] = charCountT.get(c, 0) + 1

        for c in s:
            charCountS[c] = charCountS.get(c, 0) + 1

        # check that we have enough
        for c in charCountT:
            if c not in charCountS or charCountS[c] < charCountT[c]:
                return ""
        
        n = len(s)
        i, j = 0, n - 1 

        moveI, moveJ = True, True
        cnt = 0
        while  moveI or moveJ:
            if cnt % 2 and moveI:
                c = s[i]
                if c not in charCountT or charCountS[c] > charCountT[c]:
                    i += 1
                    charCountS[c] = charCountS.get(c, 0) - 1
                else:
                    moveI = False

            else:
                c = s[j]
                if c not in charCountT or charCountS[c] > charCountT[c]:
                    j -= 1
                    charCountS[c] = charCountS.get(c, 0) - 1
                else:
                    moveJ = False
            cnt += 1
        
        ss = s[i:j + 1]
        j += 1
        # try and see if we can shift bounds
        minSS = ss
        # print(f"Round 1 minSS: {minSS}")

        tpi = i
        tpj = j
        tpCharCountS = charCountS.copy()

        while j < n:
            c = s[j]
            charCountS[c] = charCountS.get(c, 0) + 1 
            if c in charCountT and charCountS[c] > charCountT[c]:
                # print(f"shifting i")
                # tc = c
                while c not in charCountT or charCountS[c] > charCountT[c] and i < j:
                    # print(f"shifted: {s[i:j+1]}")
                    charCountS[c] = charCountS.get(c, 0) - 1
                    i += 1
                    c = s[i]
                    
                # i += 1
                
                if len(s[i:j+1]) < len(minSS):
                    minSS = s[i:j+1]
            # else:
            j += 1
        # print(f"Round 2 minSS: {minSS}")

        return minSS
