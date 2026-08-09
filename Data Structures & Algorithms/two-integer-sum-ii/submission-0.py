class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left , right = 0 , 1

        while True :
            sums = numbers[left] + numbers[-right]
            if sums == target :
                return [left + 1 , len(numbers) + 1 - right]

            elif sums > target :
                right += 1

            else :
                left += 1

        return [0 , 0]