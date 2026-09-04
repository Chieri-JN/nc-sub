"""
given list of nums and want to find longest consctiev sequebs of elemts -> return len of this

ex
[2,20,4,10,3,4,5]
then the otuput 4 -> [2,3,4,5]

human:
    - go through and add things into a list order then just count consec sequenc 
        - algo this is o(nlgn) bc orered insertion is Ologn
    
no need for order in og list 

[2,20,5,10,4,4,3]
iniital ideas: 
    - each number keeps a count so when we see it for the first time, we increment it and then we increment 
    neighbors 
        - afterwads we go through and find num with greatest count 

[2,20,4,10,3,4,5]
{2:2, 1:1, 3:3, 20:1, 21:1, 19:1, 4:3, 5:1, 10:1, 9:1, 11:1, 6:1}
go through nums again (keying in with actual values)
2, 1, 

we go through make a list of seen 
then go through again and for each element try and see if its increment exists in list (only if it doesn have smaller neighber)

 2,3? ,3. 4? ,4 5?, 6? no -> 4
 20 ->21? no


"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxSeqLen = 0
        while len(seen) > 0: 
            curr = seen.pop()
            decVal = curr - 1
            incVal = curr + 1
            count = 1
            while len(seen) > 0 and(decVal in seen or incVal in seen):
                
                if decVal in seen:
                    count += 1
                    seen.remove(decVal)
                    decVal -= 1
                if incVal in seen:
                    count += 1
                    seen.remove(incVal)
                    incVal += 1

            maxSeqLen = max(maxSeqLen, count)


        return maxSeqLen

