"""
house robber but use flag to indicate wether 

we can jsut max of skip and nxt


"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        def robber(lst):
            nxt = 0
            skip = 0
            n = len(lst)
            for i in range(n):
                tp = max(lst[i] + skip, nxt)
                
                skip = nxt
                nxt = tp

            return nxt

        return max(nums[0], robber(nums[1:]), robber(nums[:-1]))
