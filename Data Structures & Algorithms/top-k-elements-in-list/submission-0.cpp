class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> Frequency;
        unordered_map<int,vector<int>> Elements;
        for(int i : nums)Frequency[i]++;
        for(auto it : Frequency){
            Elements[it.second].push_back(it.first);
        }
        Frequency.clear();
        vector<int> answer;
        int maxFrequency = 0;
        int max = INT_MAX;
        while(answer.size() < k){
            maxFrequency = 0;
            vector<int> temp;
            for(auto it : Elements){
                if(it.first > maxFrequency && it.first < max){
                    temp = it.second;
                    maxFrequency = it.first;
                }
            }
            max = maxFrequency;
            answer.insert(answer.end(),temp.begin(),temp.end());
        }
        return answer;
    }
};
