"""
given int array, return out array where each out[i] = prod of all elements besides elem i

human/bf approach
    - for each index, get product of of all other idx
    - idx = 0, 2*4*6, for idx=1 : 1*4*6....

faster sol w/ division: 
    - to get whole array product, hten for each idx we jsut divide tha tval out
    - O(n) 

faster sol w/o: 
    - calulate prod from start to end, end to start, then fro each idx, we just multiple outer idx, 

[1,2,4,6]
[1,2,8,48] -> s-e
[48,48,24,6]-> e-s

[48, 24, 12, 8]

"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        startToEnd = [1]*n
        endToStart = [1]*n
        es = 1
        se = 1
        for i in range(n):
            se *=  nums[i]
            startToEnd[i] = se 
            es *= nums[n-i-1]
            endToStart[n-i-1] = es 

        result = [1]*n

        for i in range(n):
            if i == 0:
                result[i] = endToStart[i+1]
            elif i == n - 1:
                result[i] = startToEnd[i-1]
            
            else:
                result[i] = startToEnd[i-1] * endToStart[i+1]
 
        return result

        