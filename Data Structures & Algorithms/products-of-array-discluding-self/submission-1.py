class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix , suffix = [1], [1]
        prefixProd , suffixProd = 1,1

        for num in nums :
            prefixProd *= num 
            prefix.append(prefixProd)

        for num in reversed(nums) :
            suffixProd *= num
            suffix.append(suffixProd)

        finalRes = []

        # print(prefix)
        # print(suffix)

        for i in range(0,len(nums)):
            currProduct = prefix[i]*suffix[len(nums)-i-1]
            # print(f'{prefix[i]} --- {suffix[len(nums)-1-i]}')

            finalRes.append(currProduct)





        return finalRes
