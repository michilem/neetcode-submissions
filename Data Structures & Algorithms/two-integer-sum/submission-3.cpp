class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> lookup;

        for(int i=0; i<nums.size(); i++){
            int s = target - nums[i];
            if(lookup.count(nums[i])){
                return {lookup[nums[i]], i};
            }

            lookup[s] = i;
        }
    }
};
