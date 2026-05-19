class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int size = s.size();
        int left = 0,right = 0;

        int maxChar = 0;
        unordered_set<int> elements;

        while(right < size){
            if(elements.count(s[right])){
                maxChar = max(maxChar,(right-left));
                while(left < right && s[left] != s[right]){
                    elements.erase(s[left]);
                    left++;
                }
                elements.erase(s[left]);
                left++;
            }
            else{
                elements.insert(s[right]);
                right++;

            }
        }

        maxChar = max(maxChar,(right-left));
        return maxChar;
    }
};
