class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        newS = sorted(s)
        newT = sorted(t)

        if newS == newT :
            return True 

        return False


