""" 
given lst of heights
 want to find max container created usign two bars

[1,7,2,5,4,7,3,6] -> 36, using 7-6 we have min(6,7)*(idx7- idx1)= 36 water cap

human:
    - pick tallest then move out to see if greater volume can be achieved


algo: 
    similar idea, we start at ends, then we look at cap with that, then we move the smaller height unti
        better heigh is achieved (i.e move right until better right height is achieved or points overlap)

[7,8,2,5,4,7,3,6] 

[1,2,2,4,2] -> how to break ties? 
    idea -> find tallest and second tallest and work out from those



7*6 = 42


"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights) 

        i, j = 0, n - 1
        # t1, t2 = (0,0), (0,0)
        # for idx, h in enumerate(heights):
        #     if h > t1[0]:
        #         t2 = t1
        #         t1 = (h, idx)
        #     elif h > t2[0]:
        #         t2 = (h, idx)
        # i, j = min(t1[1], t2[1]), max(t1[1], t2[1])
        # i, j = n //2 -1, n // 2

        maxArea = 0
        # while i > -1 and j < n:
        while i < j:
            currArea = min(heights[i], heights[j]) * (j - i)
            # print(f"currArea: {currArea}")
            # print(f"maxArea: {maxArea}")
            maxArea = max(maxArea, currArea)
            # print(f"i: {i}, heights[i]: {heights[i]}")
            # print(f"j: {j}, heights[j]: {heights[j]}")

            if heights[i] >= heights[j]:
                # if j != n - 1:
                    j -= 1
                # else: 
                #     i -= 1
            else: 
                # if i > 0:
                    i += 1
                # else:
                #     j += 1


        return maxArea