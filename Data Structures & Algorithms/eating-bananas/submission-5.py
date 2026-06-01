class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1


        def timeTaken(num : int) :
            time = 0
            for pile in piles :
                time += math.ceil(pile/num)

            return time 

        if timeTaken(1) <= h :
            return 1

        while left <= right :
            mid = (left + right)//2

            if timeTaken(mid) <= h and timeTaken(mid - 1) > h :
                return mid

            elif timeTaken(mid) > h :
                left = mid + 1

            else :
                right = mid - 1


        return max(piles)
            

