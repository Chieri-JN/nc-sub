"""
since each candidate can be used at most once we just say we weither include or we dont (if we can)
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()

        def backTrack(idx, combo, prevTaken):
            s = combo[0]
            c = combo[1]
            if idx == n:
                if s == target:
                    res.append(c)
                return
            else:
                cand = candidates[idx]

                if cand > target - s:
                    return

                newSum = cand + s
                newCombo = c + [cand]

                if newSum == target:
                    res.append(newCombo)
                else:
                    if idx == 0 or cand != candidates[idx - 1] or prevTaken:
                        backTrack(idx + 1, (newSum, newCombo), True)
                    backTrack(idx + 1, combo, False)


        backTrack(0, (0, []), False)

        return res
        



