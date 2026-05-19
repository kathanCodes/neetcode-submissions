class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> hash;
        vector<int> answer;
        
        for(int i = 0;i<nums.size();i++){
            if(hash.find(target-nums[i]) != hash.end()){
                answer.push_back(hash[target-nums[i]]);
                answer.push_back(i);
            }
            hash[nums[i]] = i;
        }
        return answer;
    }
};
