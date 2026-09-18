"""
we want to find how much rain is captured

Insights:
    - amount of water stored at point is min(max l h, max r h) - height
    -  
we can use prefix and suffix max?

"""

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0]*n
        right = [0]*n
        mL = 0
        mR = 0
        for i in range(n):
            mL = max(mL, height[i])
            left[i] = mL

            mR = max(mR, height[n - i - 1])
            right[n - i - 1] = mR
        
        water = 0

        for i in range(n):
            water += max(0, min(left[i], right[i]) - height[i])

        return water