class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        finalAnswer = []
        nums.sort()

        for i,num in enumerate(nums) :
            
            left = i + 1
            right = len(nums) - 1

            while left < right :
                currSum = nums[left] + nums[right] + num 
                if currSum == 0 :
                    if [num,nums[left],nums[right]] not in finalAnswer : 
                        finalAnswer.append([num,nums[left],nums[right]])
                    left += 1
                    right -= 1

                elif currSum > 0 :
                    right -= 1

                elif currSum < 0 :
                    left += 1 

        return finalAnswer
                    