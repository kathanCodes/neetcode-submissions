class Solution {
public:
    int findMin(vector<int> &nums) {
        int left = 0;
        int right = nums.size()-1;
        int prevMid = nums[0];
        if(left == right)return prevMid;
        while(left <= right){
            int mid = (left + right)/2;
            if(mid == 0){
                return (nums[0] > nums[1]) ? nums[1] : nums[0];
            }
            else if(mid == nums.size()-1){
                if(nums[0] > nums[mid]){
                    return (nums[mid] > nums[mid-1]) ? nums[mid-1] : nums[mid];
                }
                else return nums[0];
            }
            else{
                if(nums[mid] < nums[mid+1] && nums[mid] < nums[mid-1])return nums[mid];
                if(nums[mid] > prevMid){
                    left = mid+1;
                }
                else{
                    right = mid-1;
                }
                prevMid = nums[mid];
                cout << prevMid << " " << left << "-" << right << " ";
            }
        }
        return prevMid;
    }
};
