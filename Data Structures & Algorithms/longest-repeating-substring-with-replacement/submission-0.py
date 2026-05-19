class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        charCount = {}
        maxFreq = 0
        maxStep = 0

        for right in range(len(s)):
            # Update the count of the current character
            charCount[s[right]] = charCount.get(s[right], 0) + 1
            
            # Keep track of the most frequent character in the current window
            maxFreq = max(maxFreq, charCount[s[right]])

            # Check if the number of replacements needed is > k
            # Replacements needed = (window length) - (count of most frequent char)
            while (right - left + 1) - maxFreq > k:
                charCount[s[left]] -= 1
                left += 1
            
            # Calculate the max length found so far
            maxStep = max(maxStep, right - left + 1)

        return maxStep
        