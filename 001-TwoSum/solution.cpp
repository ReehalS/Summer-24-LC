// Try hash tables in future and redo

// Bad O(n^2) solution
// 302ms (5.1%), 10.53MB (99.98%)

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i=0; i<nums.size();i++){
            for (int j=i+1; j<nums.size(); j++){
                if(nums[i]+nums[j] == target){
                    return {i ,j};
                }
            }
        }
        return {};
    }
};
