class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        time = [(target - pos)/spd for pos , spd in zip(position,speed)]

        fleetStack = []
        sortedArr = sorted(zip(position,time))
        
        for pos,tm in sortedArr :
            while fleetStack and fleetStack[-1][1] <= tm :
                fleetStack.pop()

            fleetStack.append([pos,tm])

        return len(fleetStack)
