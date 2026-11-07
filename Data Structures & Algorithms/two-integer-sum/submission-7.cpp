class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> diffs;
        for(int i=0; i < nums.size(); i++){
            int num = nums[i];
            if(diffs.contains(num)){
                return {diffs[num], i};
            }
            int diff = target - num;
            diffs[diff] = i;
        }
        return {};
    }
};
