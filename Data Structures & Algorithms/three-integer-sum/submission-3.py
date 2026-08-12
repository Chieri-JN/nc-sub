class Solution:
  
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # idea here is use fix index i and have 2 pointers for 
        #indices j= i+1 k = len(nums)-1. 
        # where sum = nums[i] + nums[j] + nums[k]
        # we first want to sort nums so we can have an idea on how to move j and k
        # if sum == 0 then sick we have a solution so we can add it to our output list
        # if sum > 0, then we need to move k to a smaller val 
        # if sum < 0, then we need ot move j to a larger val
        # if j and k overlap then we must move on
        # if we need to also move j to a point where it is not same val to the prev
        # 
        nums.sort()
        outList = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            j = i + 1
            k = len(nums)-1
            # sum = nums[i] + nums[j] + nums[k]
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum > 0: 
                    k -= 1
                elif sum < 0: 
                    j += 1
                else: 
                    outList.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while (nums[j-1] == nums[j] and j < k):
                        j += 1
    
        return outList
