class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> uniqueTriplets; // to store unique sorted triplets
        int n = nums.size();

        for (int i = 0; i < n; ++i) {
            int target = -nums[i];
            unordered_set<int> seen;
            for (int j = i + 1; j < n; ++j) {
                int complement = target - nums[j];
                if (seen.count(complement)) {
                    vector<int> triplet = {nums[i], nums[j], complement};
                    sort(triplet.begin(), triplet.end()); // sort before inserting to handle permutations
                    uniqueTriplets.insert(triplet);
                }
                seen.insert(nums[j]);
            }
        }

        // Convert set to vector
        return vector<vector<int>>(uniqueTriplets.begin(), uniqueTriplets.end());
    }
};
