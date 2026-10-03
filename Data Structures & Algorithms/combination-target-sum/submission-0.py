"""
we want to construct a list of all possible unique combos that sum to target

two combos are the same if they use the same freq of numbers 

we pick with replacements to make combo (i.e the same number can be use any number of times)

How do we only create uniq combos ?
    - create combos with all valid counts of current number (this kind of exlodes memory tho)
    - if current sum is < target but the diff is < curr number (then quit that combo)
    - pass along incomplete combos that are still valid 

Idea: 
    - sort num so we start with smalllest (this means we can avoid uneeded work)
    - back tracking
    - for each number create  
    - each combp is a list and its curr sum 


"""
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        def backTrack(idx, comboSum):
            if idx == n:
                return
            cSum, combo = comboSum
            freq = 0
            num = nums[idx]
            newSum = cSum 
            newCombo = combo
            backTrack(idx + 1, (newSum, newCombo))
            while newSum <= target and target - newSum >= num:
                newCombo = newCombo + [num]
                newSum += num
                if newSum == target:
                    res.append(newCombo)
                # else
                backTrack(idx + 1, (newSum, newCombo))
                freq += 1
        backTrack(0, (0,[]))
        return res