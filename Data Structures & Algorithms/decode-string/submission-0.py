class Solution:
    def decodeString(self, s: str) -> str:
        def processTring(st : str) -> str:
            if len(st) <= 1:
                return st
            res = ""
            i = 0
            kAcc = ""

            while i < len(st):
                if st[i].isdigit():
                    kAcc = kAcc + st[i]
                elif st[i] == '[':
                    pairCount = 1
                    i += 1
                    start = i
                    while pairCount > 0:
                        if st[i] == '[':
                            pairCount += 1
                        elif st[i] == ']':
                            pairCount += -1
                            if pairCount == 0:
                                break
                        i += 1
                    res = res + processTring(st[start:i]) * int(kAcc)
                    kAcc = ""
                elif st[i] != "]":
                    res = res + st[i]
                i += 1
            return res

        return processTring(s)