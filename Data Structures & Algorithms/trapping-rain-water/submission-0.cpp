class Solution {
public:
    // These vectors store indices of increasing heights from the front and back respectively
    vector<int> HeightFront;
    vector<int> HeightBack;

    // This function trims the two vectors from the back until their last elements are equal
    void trimVectors(vector<int>& a, vector<int>& b) {
        while (!a.empty() && !b.empty()) {
            if (a.back() == b.back()) break;
            (a.back() > b.back()) ? a.pop_back() : b.pop_back();
        }
    }

    // This function stores indices of heights forming the left and right boundary walls for trapping water
    void storeHeightIndex(vector<int> &height) {
        HeightFront.push_back(0);                          // Start from the first index (left to right)
        HeightBack.push_back(height.size() - 1);           // Start from the last index (right to left)

        // Traverse from both ends towards the center
        for (int i = 1; i < height.size(); i++) {
            // Stop when the indices overlap or cross
            if (*HeightFront.rbegin() >= *HeightBack.rbegin()) break;

            // From the front, push if current height is greater than or equal to last recorded
            if (height[i] >= height[*HeightFront.rbegin()])
                HeightFront.push_back(i);

            // From the back, push if current height is greater than or equal to last recorded
            if (height[height.size() - 1 - i] >= height[*HeightBack.rbegin()])
                HeightBack.push_back(height.size() - 1 - i);
        }

        // Trim both vectors so their ends point to the same peak height
        trimVectors(HeightFront, HeightBack);
    }

    // Main function to calculate trapped rainwater
    int trap(vector<int>& height) {
        storeHeightIndex(height);  // Identify peaks from both ends

        int answer = 0;
        int left = 0, right = 0;

        // Traverse from left to the peak, compute water trapped between bars
        for (int i = 0; i < *HeightFront.rbegin(); i++) {
            if (HeightFront[left] == i) {
                left++;  // Move to next significant peak
            } else {
                int boundedHeight = min(height[HeightFront[left]], height[HeightFront[left - 1]]);
                answer += (boundedHeight - height[i]);
            }
        }

        // Traverse from right to the peak, compute water trapped similarly
        for (int i = height.size() - 1; i > *HeightBack.rbegin(); i--) {
            if (HeightBack[right] == i) {
                right++;  // Move to next significant peak
            } else {
                int boundedHeight = min(height[HeightBack[right]], height[HeightBack[right - 1]]);
                answer += (boundedHeight - height[i]);
            }
        }

        // Reverse HeightBack for comparison
        reverse(HeightBack.begin(), HeightBack.end());

        // If both ends match symmetrically, we counted twice, so divide by 2
        if (HeightFront == HeightBack) return answer / 2;

        // Otherwise, return the full answer
        return answer;
    }
};
