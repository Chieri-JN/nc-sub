"""
gievn an lst of nums, wnt to return list of all triplets with sum = 0

output can not contain dups, order does NOT matter 

BF approach: 
    - compare every triplet -> O(n^3) 

how to make faster?
    - look for corresponding target val for pairs -> O(n^2)

[-1,0,1,2,-1,-4]
res = [[-1,0, 1]]

{1: [-1,0]}
i = 0
j = 3

since no dupes, we do not want list of list i.e once we find triple, we can not reuse it 

try sorting 
"""

from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # n = len(nums)
        # # targets = {}
        # usedTargets = set()
        # for i in range(n):
        #     targets = {}
        #     for j in range(i+1, n):
        #         # print(f"i: {i}, j: {j}")
        #         # print(f"targets before: {targets}")
        #         if nums[j] in targets and nums[j] not in usedTargets:
        #             vals = targets.pop(nums[j])
        #             vals.append(nums[j])
        #             res.append(vals)
        #             usedTargets.add(nums[j])
        #         else:
        #             targets[- (nums[i] + nums[j])] = [nums[i], nums[j]]
        #         # print(f"targets after: {targets}")
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i -1]: continue
            j = i + 1
            k = n - 1
            while j < k:
                numSum = nums[i] + nums[j] + nums[k]
                if numSum > 0: 
                    k -= 1
                elif numSum < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1

            
        return res