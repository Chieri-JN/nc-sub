"""
implemtn bin search

iteratively
[-1,0,2,4,6,8]

t= 4
bottom = 0, top = 6
mid = 3, nums[mid] = 4 !!!

t= 3
bottom = 0, top = 6
mid = 3, nums[mid] = 4 
bottom = 0, top = 3
mid = 1, nums[mid] = 0


"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bottom, top = 0, len(nums)

        while bottom < top:
            mid = (bottom + top) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                top = mid
            else:
                bottom = mid + 1

        return -1