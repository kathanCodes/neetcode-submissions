class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
   // code here
        vector<int> result;
        bool onlyOneZero = true;
        long long productWithoutZero = 1;
        long long product = 1;
        for(int i : nums){
            if(onlyOneZero && i == 0){
                product *= i;
                onlyOneZero = false;
                continue;
            }
            product *= i;
            productWithoutZero *= i;
        }
        for(int i : nums){
            if(i == 0)result.push_back(productWithoutZero);
            else result.push_back(product/i);
        }
        return result;
        
    }
};
