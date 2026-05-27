class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wmap = {}
        for s in strs: 
            k = "".join(sorted(s))
            wmap[k] =  wmap.get(k, []) + [s]

        
        # return wmap.values()
        res = []
        for v in wmap.values():
            res.append(v)

        return res 
