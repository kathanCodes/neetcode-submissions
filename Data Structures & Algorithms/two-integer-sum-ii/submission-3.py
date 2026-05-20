class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right :
            currSum = numbers[left] + numbers[right]

            if target == currSum :
                return [left + 1 , right + 1]

            elif target < currSum :
                right -= 1

            elif target > currSum :
                left += 1


        return [-1,-1]
            
