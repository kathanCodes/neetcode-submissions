class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashSet = defaultdict()

        for index , num in enumerate(nums) :
            if target - num in hashSet :
                return [hashSet[target-num],index]

            hashSet[num] = index

        return [0,0]