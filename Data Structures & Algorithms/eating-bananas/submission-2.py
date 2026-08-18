class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        kUpBound = 2*max(piles)
        kLowBound = 1

        def timeCalculator(k) :
            if k <= 0 :
                return 2*h
            time = 0

            for pile in piles :
                currTime = pile // k
                if pile%k :
                    currTime += 1 

                time += currTime

            return time 

        while kLowBound < kUpBound :
            possK = (kLowBound + kUpBound) // 2

            if timeCalculator(possK) <= h and timeCalculator(possK - 1) > h :
                return possK

            if timeCalculator(possK) > h :
                kLowBound = possK 

            else :
                kUpBound = possK 

        return possK