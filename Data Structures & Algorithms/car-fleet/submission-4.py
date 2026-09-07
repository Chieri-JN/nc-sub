"""
given two lst + target. One for car positiona one for car speed
\
car can not pass one another, if they catch up they are considered part fo the fleet. Goal is to return the number of differnt car fleets

ex 
target = 10, position = [1,4], speed = [3,2] -> 1
car at 1 catches up to car at 4 

BF / human i.e O(N^2*t) where t is the number of ticks it takes the last fleet to reach dest
    - run simulation 
    - for every tick we move the cars, we check where eahc car goes, if it is gonna pass, it gets added to 
        the fleet, otherwise it moves
    - how to check already existign fleets?


Initial thoughtS:
    - we sort / user binary search 
    - union find for fleet leader / position
    - 

inital bf algo
    - sort, we now have speed + position
    - we could then create sub counts of how many ticks each car takes to reach dest (rounded)
    - then we sort again and "collect" each tick count

tick count = (dest - pos / speed) ## ceil?
target = 10, position = [4,1,0,7], speed = [2,2,1,1]

sorted = [(0,1), (1,2), (4,2), (7,1)]
ticks = [10, 5, 3, 3] --> three fleets


"""
import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        posSpeed = [(position[i], speed[i]) for i in range(n)]

        posSpeed.sort(reverse=True)

        fleets = []
        for p, s in posSpeed:
            # print(f"pos: {p}, speed: {s}")
            tickCountRaw = ((target - p) / s)
            tickCount = (tickCountRaw)
            # print(f"tickCount: {tickCount}, tickCountRaw: {tickCountRaw}")
            if fleets != [] and tickCount <= fleets[-1]:
                continue
            fleets.append(tickCount)

        return len(fleets)

        