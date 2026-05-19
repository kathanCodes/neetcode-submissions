class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int prevMin = prices[0];
        int maxProf = 0;

        for(int i = 0;i<prices.size();i++){
            if(prevMin > prices[i])prevMin = prices[i];
            maxProf = max(maxProf,(prices[i]-prevMin));
        }

        return maxProf;
        
    }
};
