class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left,right = 0,0
        numCount = {}

        if len(s1) > len(s2) :
            return False

        for char1 in s1 :
            numCount[char1] = 1 + numCount.get(char1,0)


        while right < len(s2) :

            if s2[right] not in numCount.keys() :
                while left < right :
                    numCount[s2[left]] = numCount.get(s2[left],0) + 1
                    left += 1

                left = right + 1

            elif s2[right] in numCount.keys() and numCount[s2[right]] == 0 :
                while left < right and s2[left] != s2[right] :
                    if s2[left] in s1 :
                        numCount[s2[left]] = numCount.get(s2[left],0) + 1

                    left += 1

                left += 1

            else :
                numCount[s2[right]] -= 1


            if sum(numCount.values()) == 0 :
                return True

            right += 1

                   
        return False 