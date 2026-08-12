"""
given list of sorted ints (incr) need to find idx of pair that sum to target

ex [1,2,3,4] t = 5
3

approach:
start w/ pointers at ends of lst. i, j
-> if current sum is too big -> mv j to left, if its too small mc i

so we have 1-4, 1-3, 2-3

since we are guarenteed a solution we do not need to stop/case on whether i==j

"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] < target:
                i += 1

        return [i+1,j+1]