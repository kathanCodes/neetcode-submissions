class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        if right == 0 :
            return nums[left]

        
        while left <= right :
            mid = (left + right)//2

            print(f'{left} --- {nums[left]}')
            print(f'{mid} --- {nums[mid]}')
            print(f'{right} --- {nums[right]}')

            print('-----------------------------------------------------')

            if nums[mid - 1] :
                if nums[mid] <= nums[mid - 1] :
                    return nums[mid]

            if nums[left] < nums[mid] < nums[right] :
                return nums[left]



            if nums[mid] >= nums[left] :
                left = mid + 1
            
            else :
                right = mid - 1
        return nums[0]

            