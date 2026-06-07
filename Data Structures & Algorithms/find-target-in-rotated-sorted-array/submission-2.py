class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0,len(nums) - 1

        while left <= right :
            mid = (left + right) // 2

            if nums[mid] == target :
                return mid

            if left == right :
                return -1 

            # left sorted 
            if nums[mid] > nums[right] :
                if target > nums[mid] :
                    left = mid + 1

                elif target < nums[mid] and target >= nums[left] :
                    right = mid - 1

                elif target < nums[mid] and target < nums[left] :
                    left = mid + 1
            # right sorted 
            else :
                if target < nums[mid] :
                    right = mid -1

                elif target > nums[mid] and target > nums[right] :
                    right  = mid - 1

                elif target > nums[mid] and target <= nums[right] :
                    left = mid + 1
                

        return -1