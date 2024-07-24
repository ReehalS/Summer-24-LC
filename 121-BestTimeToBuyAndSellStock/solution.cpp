// redo this problem

// 98ms (13%), 95.96MB (27.43%)

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int minimum = prices[0];
        int cost= 0;
        for(int i=0;i<prices.size();i++){
            cost = prices[i]-minimum;
            profit= max(profit,cost);
            minimum = min(minimum, prices[i]);
        }
        return profit;
    }
};

/*
public:
    int maxProfit(vector<int>& prices) {
        int maxDiff= 0;
        int size = prices.size();
        for(int i=0; i<size-1; i++){
            for(int j=i+1;j<size;j++){
                if((prices[j]-prices[i]) >= maxDiff ){
                    maxDiff = prices[j]-prices[i];
                }
            }
        }
        return maxDiff;
    }
};
*/