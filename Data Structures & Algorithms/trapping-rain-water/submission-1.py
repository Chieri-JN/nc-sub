"""
given lss of nums representing heihts, we want to find the total amount of water thast can be trapped between the bars

ex:
[0,2,0,3,1,0,1,3,2,1] --> 9 
between 2:1 and 3:3 we have height of 2, then strech between 3to 3 we have 2,3,2 (the edges dont count)


insights
    - we are looking for "gaps" secitons between "taller heghts
    - we need to identify the left side and the right side 
    - we also subtrack "diff heights"
        - or we can just add the leftmost h - the height of the previous cell



human:
    - find dips 
    - count cells 

Algo: 
    - find 1st i (just first non zero )
    - then we look for j (which is geq than i) while calculating amount 
    - we then set i' = j and then lopok for new j

    edeg cases:
        - we never hit j geq to i. Then 

    'i' stops once we hit somethignb smaller, 'j' stops once we hit something >= i or end

"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefMax = []
        suffMax = [0]*n
        pmax = 0
        smax = 0
        for i in range(n):
            pmax = max(height[i], pmax)
            prefMax.append(pmax)

            smax = max(height[n - 1 - i], smax)
            suffMax[n - 1 - i] = smax

        # print(f"prefMax: {prefMax}")
        # print(f"suffMax: {suffMax}")

        vals = []
        for i in range(n):
            v = max(0, min(suffMax[i], prefMax[i]) - height[i])
            vals.append(v)

        return sum(vals)
