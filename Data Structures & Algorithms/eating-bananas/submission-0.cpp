class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int maxK = *max_element(piles.begin(),piles.end());
        int minK = 1;
        while(minK <= maxK){
            int midK = (minK + maxK)/2;
            int hours = 0;
            bool sufficient = true;
            for(int i : piles){
                bool addOne = (i%midK != 0);
                hours += i/midK;
                if(addOne)hours++;
                if(hours > h){
                    sufficient = false;
                    break;
                }
            }
            if(sufficient)maxK = midK-1;
            else minK = midK + 1;
        }
        return minK;
    }
};
