class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s :
            return 0
        
        l,r = 0,0
        maxLength = 0
        seenElement = set()

        while r < len(s) :
            if s[r] in seenElement :
                maxLength = max(maxLength , r - l)
                while l < r :
                    seenElement.remove(s[l])
                    l += 1
                    if s[l-1] == s[r] :
                        break

            seenElement.add(s[r])
            r += 1

        return max(maxLength , r - l)