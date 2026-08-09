class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ''
        for char in s :
            if char.isalnum():
                newS += char.lower()

        for i in range(0, len(newS)//2) :
            if newS[i] != newS[-i-1] :
                return False

        return True