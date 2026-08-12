class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        locations = {}

        for i in range(len(nums)):
            if target- nums[i] in locations:
                return [locations[target- nums[i]], i]
            else:
                locations[nums[i]] = i