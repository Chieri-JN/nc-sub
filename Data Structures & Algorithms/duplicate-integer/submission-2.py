class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print((len(nums),len(set(nums))))
        return (len(nums)!= len(set(nums)))