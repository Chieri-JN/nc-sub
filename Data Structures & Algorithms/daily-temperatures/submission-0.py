"""
given list of temps want return list where res[i] = number of days aftr temp[i] until a warmmer temp is achieved

brute force O(n^2)
    - for every day we go throgh array and see how many days auntil warmer day 

trying to avoid passing over every item n times
human: 
    - 

ideas:m 
    - binary insetion ? doesnt seme to work 
    - pref suf max? no 
    - monotonic stack: --> 
        - keep a stack, and the stack max? i think we can jsut ensure that teh stack is always dec
        - so we put something on the stack, if the top val is smaller, then we remove it and do (j - i)
        - we keep removign thigns until we can no longer and then continue
        - at the end anything left in the stack gets 0

[30,38,30,36,35,40,28]
[0]



assuming that warmer is strictly greater than 

"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0]*n
        
        for i in range(n):
            if i == 0:
                stack.append(i)
                continue
            cTemp = temperatures[i]
            while stack and cTemp > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)


        return res