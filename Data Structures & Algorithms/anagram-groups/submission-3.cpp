class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hashMap;

        for (string& word : strs) {
            string key = word;
            sort(key.begin(), key.end());  // O(L log L) where L = word length
            hashMap[key].push_back(word);
        }

        vector<vector<string>> result;
        for (auto& entry : hashMap) {
            vector<string>& group = entry.second;
            sort(group.begin(), group.end());  // Optional: sort within group
            result.push_back(group);
        }

        // Optional: sort entire result lexicographically by group
        sort(result.begin(), result.end());

        return result;
    }
};
