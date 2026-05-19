class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int left = 0,up = 0,right = matrix[0].size()-1,down = matrix.size()-1;
        int indexVertical = -1;
        while(up <= down){
            int mid = (up + down)/2;
            if(matrix[mid][left] <= target && matrix[mid][right] >= target){
                indexVertical = mid;
                break;
            }
            else if(matrix[mid][left] > target)down = mid-1;
            else if(matrix[mid][right] < target)up = mid+1;
        }
        if(indexVertical == -1)return false;
        while(left <= right){
            int mid = (left + right)/2;
            if(matrix[indexVertical][mid] == target)return true;
            else if(matrix[indexVertical][mid] > target)right = mid-1;
            else if(matrix[indexVertical][mid] < target)left = mid+1;
        }
        return false;
    }
};
