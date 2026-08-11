class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        prevNum = math.inf
        finalAns = list(list())
        nums.sort()

        for i in range(0,len(nums)) :
            left = i + 1 
            right = len(nums) - 1

            if prevNum == nums[i] :
                continue 

            prevNum = nums[i]

            while left < right :
                sumation = nums[i] + nums[left] + nums[right] 

                if sumation == 0 and (nums[i], nums[left] , nums[right]) not in finalAns :
                    finalAns.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    

                elif sumation > 0 :
                    right -= 1

                else :
                    left += 1


        return finalAns