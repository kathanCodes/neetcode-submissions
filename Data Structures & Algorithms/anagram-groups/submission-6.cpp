class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hashMap;

        for (string& it : strs) {
            vector<int> comp(26, 0);
            for (char c : it) comp[c - 'a']++;

            string key;
            for (int i : comp) key += to_string(i) + 'A'; // Add delimiter to avoid ambiguity

            hashMap[key].push_back(it);
        }

        vector<vector<string>> result;
        for (auto& entry : hashMap) {
            result.push_back(entry.second);
        }

        // Sort groups by first element in each group (lexicographically)
        sort(result.begin(), result.end(), [](const vector<string>& a, const vector<string>& b) {
            return a[0] < b[0];
        });

        return result;
    }
};
