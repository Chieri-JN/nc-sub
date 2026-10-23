class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnts = {}
        for c in arr:
            cnts[c] = cnts.get(c, 0) + 1

        res =[]
        for c, v in cnts.items():
            if v == 1:
                res.append(c)

        if k > len(res):
            return ""
        
        return res[k-1]