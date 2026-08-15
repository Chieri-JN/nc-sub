"""
given an array of nums we want to return lsit of top k msot req nums
- they answer is always unique --> no tie breaks
- we can return in any order --> no need to maintain appearance ordere
- k is not greater than number of disctinct nums


ex [1,2,2,3,3,3] k = 2
 - scan thru, keep track of count of nums weve seen 
 - 1:1, 2:2, 3:3
 - 3, 2

algo: 
- scan thru create mappingof nums to freq count
- next sort, we can take map and make it a list of tuples (k,v) then sort of v
- then jsut slice off the top k items of thats

{}
{1:1}, {1:1, 2:1}, {1:1, 2:2}, {1:1,2:2, 3:1}... {1:1,2:2, 3:3}


"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numberMap = {}
        for n in nums: 
            numberMap[n] = numberMap.get(n, 0) + 1
        vals = []
        
        for key, v in numberMap.items():
            vals.append((key,v))
        
        vals.sort(reverse=True, key=lambda x: x[1])
        result = []
        for i in range(len(vals)):
            result.append(vals[i][0])
            if len(result) == k: 
                break
        
        return result[:k]

