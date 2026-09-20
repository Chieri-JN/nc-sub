"""
givrn lst of nums of len n + 1, ranging [1,n] find the dupe number

BF: 
    - keep set of nums when we find one we've seen before, return int
O(N) time O(N) space

how can we achieve O(1) extra space AND without moding nums (which makes solving this trival)
    - BF is to just do O(N^2) and compare everything to everythign else
        - trivial
    - BF 2 - we sort then check, O(1) space O(nlogn) time 
        (not valid) in place mods it or out of place uses extra space
    
Insights/obs: 
    - n possible values with n+1 slots --> one must be duplicated 
    - only one can appear more than once 
    - no guarentee of order
    - dupe must replace a number


ideas: 
    - culmulative product? does this really tell us whats there...
    - can compare count of even vs odd? but this does not work...
    - use median? 
    - each value points to a valid index, so the dupe number creates a "cycle"
        - we could use cycle detection -> how do we construct conections
            at idx i next idex is nums[i]
        
    - fast pointer starts to cycle


[1,2,3,2,2]

Node (1, 0) -> Node (2, 1) -> Node(3, 2) -> Node (2, 3)



"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        fast, slow = nums[nums[0]], nums[0]
        while nums[fast] != nums[slow]:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        slow = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
       
        return slow
