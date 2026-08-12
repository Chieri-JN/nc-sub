class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(lst,key,upper,lower):
            if lower + 1 == upper:
                return -1
            mid = (lower + upper)//2
            if key == lst[mid]: return mid
            if key < lst[mid]:
                return helper(lst,key,mid,lower)
            else:
                return helper(lst,key,upper,mid)

        return helper(nums,target,len(nums),-1)
