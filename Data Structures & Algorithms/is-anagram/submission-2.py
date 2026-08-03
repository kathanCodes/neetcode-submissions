class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # First Approach 

        # newS = sorted(s)
        # newT = sorted(t)

        # if newS == newT :
        #     return True 

        # return False

        hashSet = defaultdict()

        if len(s) != len(t) :
            return False

        for charS , charT in zip(s,t) :
            hashSet[charS] = hashSet.get(charS , 0) + 1

            hashSet[charT] = hashSet.get(charT , 0) - 1

        if not any(hashSet.values()) : 
            return True 


        return False 
 