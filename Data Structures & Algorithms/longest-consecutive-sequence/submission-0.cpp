class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> hashSet;
        int longestSeq = 0;
        for(int i : nums)hashSet.insert(i);
        for(int i : nums){
            int currLongest = 0;
            if(hashSet.find(i-1) == hashSet.end()){
                while(hashSet.find(i++) != hashSet.end())currLongest++;
                longestSeq = max(longestSeq,currLongest);
            }
        }
        
        
        return longestSeq;
    }
};
