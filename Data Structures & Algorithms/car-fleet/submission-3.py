class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
       times = [(target - pos) / spd for pos , spd in zip(position , speed)]
       
       posTime = [[pos,time] for pos , time in zip(position,times)]
       posTime.sort()
       NumFleet = 1
       prevTime = posTime[-1][1]

       for pos,time in reversed(posTime) :
        if time > prevTime :
            NumFleet += 1
            prevTime = time

    

       return NumFleet

       